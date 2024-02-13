import time
from typing import Union, Dict

from loguru import logger
from config import MAVERICK_CONTRACTS, MAVERICK_POSITION_ABI, ZKSYNC_TOKENS, MAVERICK_ROUTER_ABI, ZERO_ADDRESS,MAVERICK_POOLS,MAVERICK_POOL_ABI
from utils.gas_checker import check_gas
from utils.helpers import retry
from .account import Account


class Maverick(Account):
    def __init__(self, account_id: int, private_key: str, proxy: Union[None, str]) -> None:
        super().__init__(account_id=account_id, private_key=private_key, proxy=proxy, chain="zksync")

        self.swap_contract = self.get_contract(MAVERICK_CONTRACTS["router"], MAVERICK_ROUTER_ABI)

    async def get_min_amount_out(self, amount: int, token_a_in: bool, slippage: float):
        contract = self.get_contract(MAVERICK_CONTRACTS["pool_information"], MAVERICK_POSITION_ABI)

        amount = await contract.functions.calculateSwap(
            self.w3.to_checksum_address(MAVERICK_CONTRACTS["pool"]),
            amount,
            token_a_in,
            True,
            0
        ).call()

        return int(amount - (amount / 100 * slippage))
    
    async def get_min_amount_out_token(self, amount: int, token_a_in: bool, slippage: float, pool_address: str):
        contract = self.get_contract(MAVERICK_CONTRACTS["pool_information"], MAVERICK_POSITION_ABI)

        amount = await contract.functions.calculateSwap(
            self.w3.to_checksum_address(pool_address),
            amount,
            token_a_in,
            True,
            0
        ).call()
        print("Min Amount Out",amount)

        return int(amount - (amount / 100 * slippage))
    async def get_pool(self, from_token: str, to_token: str):
        if from_token+'/'+to_token  in MAVERICK_POOLS:
            pool_address = MAVERICK_POOLS.get(from_token+'/'+to_token)
        
        elif to_token+'/'+from_token in MAVERICK_POOLS:
            pool_address = MAVERICK_POOLS.get(to_token+'/'+from_token)
        else:
            pool_address = ZERO_ADDRESS
        
        return pool_address
    

    def get_path(self, from_token: str, to_token: str):
        path_data = [
            self.w3.to_checksum_address(ZKSYNC_TOKENS[from_token]),
            self.w3.to_checksum_address(MAVERICK_CONTRACTS["pool"]),
            self.w3.to_checksum_address(ZKSYNC_TOKENS[to_token]),
        ]

        path = b"".join([bytes.fromhex(address[2:]) for address in path_data])

        return path
    
    def get_path_token(self, from_token: str, to_token: str, pool_address: str):
        path_data = [
            self.w3.to_checksum_address(ZKSYNC_TOKENS[from_token]),
            self.w3.to_checksum_address(pool_address),
            self.w3.to_checksum_address(ZKSYNC_TOKENS[to_token]),
        ]

        path = b"".join([bytes.fromhex(address[2:]) for address in path_data])
        return path
    async def swap_to_token(self, from_token: str, to_token: str, amount: int, slippage: int):
        tx_data = await self.get_tx_data(amount)

        deadline = int(time.time()) + 1000000

        min_amount_out = await self.get_min_amount_out(amount, True, slippage)

        transaction_data = self.swap_contract.encodeABI(
            fn_name="exactInput",
            args=[(
                self.get_path(from_token, to_token),
                self.address,
                deadline,
                amount,
                min_amount_out
            )]
        )

        refund_data = self.swap_contract.encodeABI(
            fn_name="refundETH",
        )

        contract_txn = await self.swap_contract.functions.multicall(
            [transaction_data, refund_data]
        ).build_transaction(tx_data)
        print("Contract TXN:-",contract_txn)
        return contract_txn

    async def swap_tokenA_to_tokenB(self, from_token: str, to_token: str, amount: int, slippage: int, pool_address: str):
        await self.approve(amount, ZKSYNC_TOKENS[from_token], MAVERICK_CONTRACTS["router"])
        tx_data = await self.get_tx_data()
        deadline = int(time.time()) + 1000000
        # min_amount_out = await self.get_min_amount_out_token(amount, True, slippage, pool_address)
        min_amount_out = 0
        exact_input_params = {
            "path": self.get_path_token(from_token, to_token, pool_address),
            "recipient": self.address,
            "deadline": deadline,
            "amountIn": amount,
            "amountOutMinimum": min_amount_out
        }
        contract_txn = await self.swap_contract.functions.exactInput(
            exact_input_params
        ).build_transaction(tx_data)
        return contract_txn

    async def swap_to_eth(self, from_token: str, to_token: str, amount: int, slippage: int):
        await self.approve(amount, ZKSYNC_TOKENS[from_token], MAVERICK_CONTRACTS["router"])

        tx_data = await self.get_tx_data()

        deadline = int(time.time()) + 1000000

        min_amount_out = await self.get_min_amount_out(amount, False, slippage)

        transaction_data = self.swap_contract.encodeABI(
            fn_name="exactInput",
            args=[(
                self.get_path(from_token, to_token),
                ZERO_ADDRESS,
                deadline,
                amount,
                min_amount_out
            )]
        )

        unwrap_data = self.swap_contract.encodeABI(
            fn_name="unwrapWETH9",
            args=[
                0,
                self.address
            ]

        )

        contract_txn = await self.swap_contract.functions.multicall(
            [transaction_data, unwrap_data]
        ).build_transaction(tx_data)

        return contract_txn

    @retry
    @check_gas
    async def swap(
            self,
            from_token: str,
            to_token: str,
            min_amount: float,
            max_amount: float,
            decimal: int,
            slippage: int,
            all_amount: bool,
            min_percent: int,
            max_percent: int
    ):
        amount_wei, amount, balance = await self.get_amount(
            from_token,
            min_amount,
            max_amount,
            decimal,
            all_amount,
            min_percent,
            max_percent
        )

        logger.info(
            f"[{self.account_id}][{self.address}] Swap on Maverick – {from_token} -> {to_token} | {amount} {from_token}"
        )
       

        if from_token == "ETH":
            contract_txn = await self.swap_to_token(from_token, to_token, amount_wei, slippage)
        elif to_token == "ETH":
            contract_txn = await self.swap_to_eth(from_token, to_token, amount_wei, slippage)
        else:
             pool_address = await self.get_pool(from_token, to_token)
             contract_txn = await self.swap_tokenA_to_tokenB(from_token, to_token, amount_wei, slippage, pool_address)

        signed_txn = await self.sign(contract_txn)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())