from web3 import Web3 

rpc='https://sepolia.infura.io/v3/800b34901df94fadabc75170fd2125e9'
web3=Web3(Web3.HTTPProvider(rpc))

John='0xbaDB4412391aa7882A9f2419D17899e64aaEe6Df'
Sam='0xA3307CBfb1ED1feC5B2769DC3fBdFD2eD7E50671'

nonce= web3.eth.get_transaction_count(John)
transaction_data= {
	'nonce':nonce,
	'to':Sam,
	'value':web3.to_wei(5,'ether'),
	'gas': 21000,
	'gasPrice':web3.to_wei(40,'gwei')
}

pk='0xe67751fec85e962c8c339c30e4ef14df05e02d7a9dd7ed195beef8e21c386212'
signed= web3.eth.account.sign_transaction(transaction_data,pk)
raw= web3.eth.send_raw_transaction(signed.rawTransaction)
print('The Hex value of the Transaction: ' , web3.to_hex(raw))