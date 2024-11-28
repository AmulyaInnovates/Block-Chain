from web3 import Web3

url='https://mainnet.infura.io/v3/800b34901df94fadabc75170fd2125e9'
eth_url= Web3(Web3.HTTPProvider(url))
block_used= eth_url.eth.get_block(19153651)
print('Transaction : ' , block_used['transactions'])

Transactions= eth_url.eth.get_transaction('0x953180892db9fae322b1a665524c48767cd3a58781c312ca3a6a7360615263ff')

print('Current Block Hash : ' , Transactions['blockHash'].hex())
print('Current Block Number : ' , Transactions['blockNumber'])
print('Gas : ' , Transactions['gas'])
print('Gas Price Required : ' , Transactions['gasPrice'])
print('Input Given : ' , Transactions['input'])
print('Signature : ' , Transactions['s'].hex())
print('From(The Sender) : ' , Transactions['from'])
print('Hash Of The Transaction : ' , Transactions['hash'].hex())
print('The Reciever : ' , Transactions['to'])
print('Amount Of Money Sent : ' , Transactions['value'])
print('Nonce Value Of The Transaction : ' , Transactions['nonce'])