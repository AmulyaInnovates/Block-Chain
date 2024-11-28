from web3 import Web3
import json
import requests

url='https://mainnet.infura.io/v3/800b34901df94fadabc75170fd2125e9'
eth_url= Web3(Web3.HTTPProvider(url))

api= 'https://ethgasstation.info/jsonethgasAPI.json'
json_api= json.loads(api)

print('SafeLow : ' , json_api['safeLow'])
print('Average : ' , json_api['average'])
print('Fast : ' , json_api['fast'])
print('Fastest : ' , json_api['fastest'])
print('Block Number : ' , json_api['blockNumber'])

gas_prices=json_api.eth.gas_price
gas_price_in_ether= int(int(gas_price) /10**18)
gas_price_in_dollars= gas_price_in_ether *2552
print('Gas Price In Ether : ' , gas_price_in_ether)
print('Gas Price In Dollars : ' , gas_price_in_dollars)
Block = eth_url.eth.get_block(19203853)

latest= Block['transactions'][-1].hex()
print('The Latest Transaction Performed : ' , latest)
transaction_details= eth_url.eth.get_transaction(latest)
estimated_gas_price= eth_url.eth.estimate_gas({'to': transaction_details['to'] ,'from': transaction_details['from']})
print('The Estimated Gas Price = ' ,  estimated_gas_price)
print('The Actual Gas Price = ' , gas_price_in_ether, '  Ether')