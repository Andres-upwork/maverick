from web3 import Web3

# Initialize endpoint URL
node_url = "https://bold-wispy-panorama.zksync-mainnet.quiknode.pro/94bf40dd8db9d409833b0306a5031502aa40f601/"

# Create the node connection
web3 = Web3(Web3.HTTPProvider(node_url))

# if web3.is_connected():
#     print("-" * 50)
#     print("Connection Successful")
#     print("-" * 50)
# else:
#     print("Connection Failed")

caller = "0x8FA132f0B40FE0d7E4012163E47E08f7e4700f0B"
private_key = "9d6f70bfa7d18f97ad9d233a81c8816760c46b808e56e7da170dcb607987f1ea"

# Initialize address nonce
nonce = web3.eth.get_transaction_count(caller)

abi = """[
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "poolAddress",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "fee",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "tickSpacing",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "int32",
                "name": "activeTick",
                "type": "int32"
            },
            {
                "indexed": false,
                "internalType": "int256",
                "name": "lookback",
                "type": "int256"
            },
            {
                "indexed": false,
                "internalType": "uint64",
                "name": "protocolFeeRatio",
                "type": "uint64"
            },
            {
                "indexed": false,
                "internalType": "contract IERC20",
                "name": "tokenA",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "contract IERC20",
                "name": "tokenB",
                "type": "address"
            }
        ],
        "name": "PoolCreated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "SetFactoryOwner",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint64",
                "name": "protocolFeeRatio",
                "type": "uint64"
            }
        ],
        "name": "SetFactoryProtocolFeeRatio",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_fee",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_tickSpacing",
                "type": "uint256"
            },
            {
                "internalType": "int256",
                "name": "_lookback",
                "type": "int256"
            },
            {
                "internalType": "int32",
                "name": "_activeTick",
                "type": "int32"
            },
            {
                "internalType": "contract IERC20",
                "name": "_tokenA",
                "type": "address"
            },
            {
                "internalType": "contract IERC20",
                "name": "_tokenB",
                "type": "address"
            }
        ],
        "name": "create",
        "outputs": [
            {
                "internalType": "contract IPool",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract IPool",
                "name": "pool",
                "type": "address"
            }
        ],
        "name": "isFactoryPool",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "fee",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tickSpacing",
                "type": "uint256"
            },
            {
                "internalType": "int256",
                "name": "lookback",
                "type": "int256"
            },
            {
                "internalType": "contract IERC20",
                "name": "tokenA",
                "type": "address"
            },
            {
                "internalType": "contract IERC20",
                "name": "tokenB",
                "type": "address"
            }
        ],
        "name": "lookup",
        "outputs": [
            {
                "internalType": "contract IPool",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "position",
        "outputs": [
            {
                "internalType": "contract IPosition",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "protocolFeeRatio",
        "outputs": [
            {
                "internalType": "uint64",
                "name": "",
                "type": "uint64"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]"""
pool_abi="""[
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint128",
                        "name": "deltaA",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "deltaB",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint256",
                        "name": "deltaLpBalance",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint128",
                        "name": "binId",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint8",
                        "name": "kind",
                        "type": "uint8"
                    },
                    {
                        "internalType": "int32",
                        "name": "lowerTick",
                        "type": "int32"
                    },
                    {
                        "internalType": "bool",
                        "name": "isActive",
                        "type": "bool"
                    }
                ],
                "indexed": false,
                "internalType": "struct IPool.BinDelta[]",
                "name": "binDeltas",
                "type": "tuple[]"
            }
        ],
        "name": "AddLiquidity",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "uint128",
                "name": "binId",
                "type": "uint128"
            },
            {
                "indexed": false,
                "internalType": "uint128",
                "name": "reserveA",
                "type": "uint128"
            },
            {
                "indexed": false,
                "internalType": "uint128",
                "name": "reserveB",
                "type": "uint128"
            },
            {
                "indexed": false,
                "internalType": "uint128",
                "name": "mergeId",
                "type": "uint128"
            }
        ],
        "name": "BinMerged",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "uint128",
                "name": "binId",
                "type": "uint128"
            },
            {
                "indexed": false,
                "internalType": "int128",
                "name": "previousTick",
                "type": "int128"
            },
            {
                "indexed": false,
                "internalType": "int128",
                "name": "newTick",
                "type": "int128"
            }
        ],
        "name": "BinMoved",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint128",
                "name": "binId",
                "type": "uint128"
            },
            {
                "indexed": false,
                "internalType": "uint32",
                "name": "maxRecursion",
                "type": "uint32"
            }
        ],
        "name": "MigrateBinsUpStack",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "protocolFee",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "bool",
                "name": "isTokenA",
                "type": "bool"
            }
        ],
        "name": "ProtocolFeeCollected",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint128",
                        "name": "deltaA",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "deltaB",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint256",
                        "name": "deltaLpBalance",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint128",
                        "name": "binId",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint8",
                        "name": "kind",
                        "type": "uint8"
                    },
                    {
                        "internalType": "int32",
                        "name": "lowerTick",
                        "type": "int32"
                    },
                    {
                        "internalType": "bool",
                        "name": "isActive",
                        "type": "bool"
                    }
                ],
                "indexed": false,
                "internalType": "struct IPool.BinDelta[]",
                "name": "binDeltas",
                "type": "tuple[]"
            }
        ],
        "name": "RemoveLiquidity",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "protocolFee",
                "type": "uint256"
            }
        ],
        "name": "SetProtocolFeeRatio",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "bool",
                "name": "tokenAIn",
                "type": "bool"
            },
            {
                "indexed": false,
                "internalType": "bool",
                "name": "exactOutput",
                "type": "bool"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amountIn",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amountOut",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "int32",
                "name": "activeTick",
                "type": "int32"
            }
        ],
        "name": "Swap",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "fromTokenId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "toTokenId",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint128",
                        "name": "binId",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "amount",
                        "type": "uint128"
                    }
                ],
                "indexed": false,
                "internalType": "struct IPool.RemoveLiquidityParams[]",
                "name": "params",
                "type": "tuple[]"
            }
        ],
        "name": "TransferLiquidity",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint8",
                        "name": "kind",
                        "type": "uint8"
                    },
                    {
                        "internalType": "int32",
                        "name": "pos",
                        "type": "int32"
                    },
                    {
                        "internalType": "bool",
                        "name": "isDelta",
                        "type": "bool"
                    },
                    {
                        "internalType": "uint128",
                        "name": "deltaA",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "deltaB",
                        "type": "uint128"
                    }
                ],
                "internalType": "struct IPool.AddLiquidityParams[]",
                "name": "params",
                "type": "tuple[]"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "addLiquidity",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "tokenAAmount",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenBAmount",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint128",
                        "name": "deltaA",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "deltaB",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint256",
                        "name": "deltaLpBalance",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint128",
                        "name": "binId",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint8",
                        "name": "kind",
                        "type": "uint8"
                    },
                    {
                        "internalType": "int32",
                        "name": "lowerTick",
                        "type": "int32"
                    },
                    {
                        "internalType": "bool",
                        "name": "isActive",
                        "type": "bool"
                    }
                ],
                "internalType": "struct IPool.BinDelta[]",
                "name": "binDeltas",
                "type": "tuple[]"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "uint128",
                "name": "binId",
                "type": "uint128"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "lpToken",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "binBalanceA",
        "outputs": [
            {
                "internalType": "uint128",
                "name": "",
                "type": "uint128"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "binBalanceB",
        "outputs": [
            {
                "internalType": "uint128",
                "name": "",
                "type": "uint128"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "int32",
                "name": "tick",
                "type": "int32"
            }
        ],
        "name": "binMap",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "int32",
                "name": "tick",
                "type": "int32"
            },
            {
                "internalType": "uint256",
                "name": "kind",
                "type": "uint256"
            }
        ],
        "name": "binPositions",
        "outputs": [
            {
                "internalType": "uint128",
                "name": "",
                "type": "uint128"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "factory",
        "outputs": [
            {
                "internalType": "contract IFactory",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "fee",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "lookback",
        "outputs": [
            {
                "internalType": "int256",
                "name": "",
                "type": "int256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint128",
                "name": "binId",
                "type": "uint128"
            }
        ],
        "name": "getBin",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint128",
                        "name": "reserveA",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "reserveB",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "mergeBinBalance",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "mergeId",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "totalSupply",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint8",
                        "name": "kind",
                        "type": "uint8"
                    },
                    {
                        "internalType": "int32",
                        "name": "lowerTick",
                        "type": "int32"
                    }
                ],
                "internalType": "struct IPool.BinState",
                "name": "bin",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getCurrentTwa",
        "outputs": [
            {
                "internalType": "int256",
                "name": "",
                "type": "int256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getState",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "int32",
                        "name": "activeTick",
                        "type": "int32"
                    },
                    {
                        "internalType": "uint8",
                        "name": "status",
                        "type": "uint8"
                    },
                    {
                        "internalType": "uint128",
                        "name": "binCounter",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint64",
                        "name": "protocolFeeRatio",
                        "type": "uint64"
                    }
                ],
                "internalType": "struct IPool.State",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getTwa",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "int96",
                        "name": "twa",
                        "type": "int96"
                    },
                    {
                        "internalType": "int96",
                        "name": "value",
                        "type": "int96"
                    },
                    {
                        "internalType": "uint64",
                        "name": "lastTimestamp",
                        "type": "uint64"
                    }
                ],
                "internalType": "struct IPool.TwaState",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint128",
                "name": "binId",
                "type": "uint128"
            },
            {
                "internalType": "uint32",
                "name": "maxRecursion",
                "type": "uint32"
            }
        ],
        "name": "migrateBinUpStack",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint128",
                        "name": "binId",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "amount",
                        "type": "uint128"
                    }
                ],
                "internalType": "struct IPool.RemoveLiquidityParams[]",
                "name": "params",
                "type": "tuple[]"
            }
        ],
        "name": "removeLiquidity",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "tokenAOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenBOut",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint128",
                        "name": "deltaA",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "deltaB",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint256",
                        "name": "deltaLpBalance",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint128",
                        "name": "binId",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint8",
                        "name": "kind",
                        "type": "uint8"
                    },
                    {
                        "internalType": "int32",
                        "name": "lowerTick",
                        "type": "int32"
                    },
                    {
                        "internalType": "bool",
                        "name": "isActive",
                        "type": "bool"
                    }
                ],
                "internalType": "struct IPool.BinDelta[]",
                "name": "binDeltas",
                "type": "tuple[]"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "tokenAIn",
                "type": "bool"
            },
            {
                "internalType": "bool",
                "name": "exactOutput",
                "type": "bool"
            },
            {
                "internalType": "uint256",
                "name": "sqrtPriceLimit",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "swap",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "amountIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountOut",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "tickSpacing",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "tokenA",
        "outputs": [
            {
                "internalType": "contract IERC20",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "tokenAScale",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "tokenB",
        "outputs": [
            {
                "internalType": "contract IERC20",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "tokenBScale",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "fromTokenId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "toTokenId",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint128",
                        "name": "binId",
                        "type": "uint128"
                    },
                    {
                        "internalType": "uint128",
                        "name": "amount",
                        "type": "uint128"
                    }
                ],
                "internalType": "struct IPool.RemoveLiquidityParams[]",
                "name": "params",
                "type": "tuple[]"
            }
        ],
        "name": "transferLiquidity",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]"""

factory_address = "0x2C1a605f843A2E18b7d7772f0Ce23c236acCF7f5"
pool_address = "0xafa8ca24eac27b5ae680b7856e54fdb06b5f60be"

contract = web3.eth.contract(address=factory_address, abi=abi)
contract_pool = web3.eth.contract(address=Web3.to_checksum_address(pool_address),abi=pool_abi)
transaction = {
    'from': '0x8FA132f0B40FE0d7E4012163E47E08f7e4700f0B',  # Replace with your Ethereum address
    'gas': 2000000,  # Adjust the gas limit accordingly
}
fee = 300000000000000
tick_spacing = 487
lookback = 0 
result = contract.functions.lookup(fee,tick_spacing,lookback,Web3.to_checksum_address("0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4"),Web3.to_checksum_address("0x5AEa5775959fBC2557Cc8789bC1bf90A239D9a91")).call() 
#result = contract.functions.isFactoryPool(Web3.to_checksum_address("0xafa8ca24eac27b5ae680b7856e54fdb06b5f60be")).call()
#result = contract_pool.functions.getCurrentTwa().call()
#print(result)

#USDC/ETH POOL
#Pool address 0xafa8ca24eac27b5ae680b7856e54fdb06b5f60be
#USDC address 0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4
#ETH ADdress 0x5AEa5775959fBC2557Cc8789bC1bf90A239D9a91
#FEE 300000000000000
#TICK_Spacing 487
#Lookback (159055952533836229656, 159153503972501594344, 1703265259) 159056792560113625851


ZKSYNC_POOLS = {
    "ETH/USDC": "0x42d106c4a1d0bc5c482c11853a3868d807a3781d",
    "WBTC/USDC": "0xae931c65e7cc843bb46ae63cc9de54adbf2e647d",
    "WBTC/ETH": "0xf47430bbbe7474ec024e66dee2470b4d05b48804",
    
}
fro = "USDC"
to = "ETH"
if fro+'/'+to or to+'/'+fro in ZKSYNC_POOLS:
    res = ZKSYNC_POOLS.get(to+'/'+fro)
    print(res)
else:
    print("Does not exist")