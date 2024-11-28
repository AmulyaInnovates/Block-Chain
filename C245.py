from web3 import Web3

url='https://mainnet.infura.io/v3/800b34901df94fadabc75170fd2125e9'
eth_url= Web3(Web3.HTTPProvider(url))
gas_prices=eth_url.eth.gas_price
print('Wei Gas Price : ',gas_prices)

l_cost= int(gas_prices *0.9)
a_cost= int(gas_prices *1.0)
f_cost= int(gas_prices *1.1)
fs_cost= int(gas_prices *1.2)

l_gwei= eth_url.from_wei(l_cost , 'gwei')
a_gwei= eth_url.from_wei(a_cost , 'gwei')
f_gwei= eth_url.from_wei(f_cost , 'gwei')
fs_gwei= eth_url.from_wei(fs_cost , 'gwei')

print('Slow Gas-Price: ' , l_gwei)
print('Average Gas-Price: ' , a_gwei)
print('Fast Gas-Price: ' , f_gwei)
print('Fastest Gas-Price: ' , fs_gwei)

new_gas_prices=eth_url.eth.gas_price
print('Gwei Gas Price : ', new_gas_prices)