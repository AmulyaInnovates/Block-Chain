from web3 import Web3

API_url='https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98'
apiurl_coding= Web3(Web3.HTTPProvider(API_url))

getting_block= apiurl_coding.eth.get_block(19146030)
print('The Block : ', getting_block)

print('The Gas Used : ' , getting_block['gasUsed'])
print('The Total Difficulty : ' , getting_block['difficulty'])
print('The Transactions : ' , getting_block['transactions'])

transactions= apiurl_coding.eth.get_transaction('0x22812e58e2e000c9ae74dc56311c199e773533df3589923da6921634f9226e3d')
print('Transactions are as follows : ' , transactions)