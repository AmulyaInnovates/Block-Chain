# --------------253 Proj----------------
from web3 import Web3
import time

ganache_url = 'HTTP://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0xa065E6114a1E8B7b414c39B78Afd3a2A4cAF0097'
James_account = '0x6100bB1c502ee5CFB3101848bF811F37Bc63Dd20'
Ryan_account  = '0xC27e3e933a0Fbb4E858953C18f01a95776786212'


nonce1 = web3_ganache_connection.eth.get_transaction_count(Alice_account)

transaction_data1 = {
    'nonce':nonce1,
    'to':James_account,
    'value':web3_ganache_connection.to_wei(2, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(50,'gwei')
}

private_key1 = '0x35a514e977337a9e28bda6c18510ae6327cdd1ea9189464c63dfdd8918d93de3'

singed_transaction1 = web3_ganache_connection.eth.account.sign_transaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction1.rawTransaction)


block= web3_ganache_connection.eth.get_block(0)
print('Block Number: ', block['number'])
print('Hash Value: ', block['hash'].hex())
print('Parent Hash Value: ', block['parentHash'].hex())
print('Nonce Value: ', block['nonce'].hex())
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
# -----------------
print('Wait for few seconds Transaction is in progress.')
time.sleep(5)




nonce2 = web3_ganache_connection.eth.get_transaction_count(James_account)

transaction_data2 = {
    'nonce':nonce2,
    'to':Ryan_account,
    'value':web3_ganache_connection.to_wei(1,'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(40,'gwei')
}

private_key2 = '0x19d0234e6fa155e38891a7e8c82ae82dc954f663a644720fb25068bb0b41fb5b'

singed_transaction2 = web3_ganache_connection.eth.account.sign_transaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction2.rawTransaction)

block= web3_ganache_connection.eth.get_block(1)
print('Block Number: ', block['number'])
print('Hash Value: ', block['hash'].hex())
print('Parent Hash Value: ', block['parentHash'].hex())
print('Nonce Value: ', block['nonce'].hex())
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')