from web3 import Web3

web3=Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

sender='0x8B113517A6308b30A15889594E7DB80653BC8ad6'
reciever='0x78dC86b89bc1e8e12E3eEf04FD39902135c984A3'
pk='0x576c19b2d2f5bce684a7647ecaf6c599af554527a4aa0175e947c69881d9ee33'
nonce=web3.eth.get_transaction_count(sender)
tx= {
	'nonce':nonce,
	'to':reciever,
	'value':web3.to_wei(10,'ether'),
	'gas':21987,
	'gasPrice':web3.to_wei(50,'gwei')
}

st=web3.eth.account.sign_transaction(tx,pk)
Raw_value=web3.eth.send_raw_transaction(st.rawTransaction)
Hash_value=web3.to_hex(Raw_value)
print('Raw Value : ',Raw_value)
print('Hash Value : ',Hash_value)