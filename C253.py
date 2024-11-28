from web3 import Web3

url='HTTP://127.0.0.1:7545'
web3= Web3(Web3.HTTPProvider(url))

for i in range(0,4):
	x= int(i)
	block= web3.eth.get_block(x)
	print('Block Number: ', block['number'])
	print('Hash Value: ', block['hash'].hex())
	print('Parent Hash Value: ', block['parentHash'].hex())
	print('Nonce Value: ', block['nonce'].hex())
	print('Transaction Details: ' ,block['transactions'])
	print('--------------------------------------------')

transaction_detail= web3.eth.get_transaction('0xe935ae398b6ee1cf9af1fc9df926fcde965e02e489a8fe9e97c77fb96f46cc40')
print('Transaction Data: ', transaction_detail)
print('************************************************')
print('Reciever: ', transaction_detail['to'])
print('Sender: ', transaction_detail['from'])
print('Value: ', transaction_detail['value'])