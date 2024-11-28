from web3 import Web3
from web3 import Web3, HTTPProvider

# Task 01: Import the required module and establish connection with the Infura API
url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(HTTPProvider(url))

# Task 02: Get the latest block of the blockchain
latest_block = web3.eth.get_block('latest')

# Print the value of the latest_block variable
print("Latest Block of Ethereum Blockchain:")
print(latest_block)

# Task 03: Get block transaction count
block_transaction_count = web3.eth.get_block_transaction_count(19153374)

# Print the number of transactions happened in the block
print("Number of transactions happened in the block:", block_transaction_count)

# Task 04: Get transaction fee history
block_count = 10  # You can change this value as needed (between 1 to 1024)
newest_block = 'latest'
reward_percentiles = None
transaction_fee = web3.eth.fee_history(block_count, newest_block, reward_percentiles)

# Print the transaction fee history
print("Transaction Fee History:")
print(transaction_fee)
