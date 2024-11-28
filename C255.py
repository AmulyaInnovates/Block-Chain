from web3 import Web3 

rpc='HTTP://127.0.0.1:7545'
web3=Web3(Web3.HTTPProvider(rpc))

John='0x8ae489DC66a0Ad1eF6b43635F9Af554914815A54'
Sam='0xaF74E8Fc16e7D247E2fe1B4Bcc17acd8E6efc08a'

nonce= web3.eth.get_transaction_count(John)
transaction_data= {
	'nonce':nonce,
	'to':Sam,
	'value':web3.to_wei(5,'ether'),
	'gas': 21000,
	'gasPrice':web3.to_wei(40,'gwei')
}

pk='0x5b5dea2828eba00a0c60c92f945b356ec949886348477192ae978d17884134b4'
signed= web3.eth.account.sign_transaction(transaction_data,pk)
raw= web3.eth.send_raw_transaction(signed.rawTransaction)
print('The Hex value of the Transaction: ' , web3.to_hex(raw))