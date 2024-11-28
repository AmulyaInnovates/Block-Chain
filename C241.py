import hashlib
import json
from time import time

class Block:
	def __init__(self):
		self.count=0
		self.new_transactions= []
		self.chain=[]
		self.new_block(previous_hash='No Previous Hash As it is Genesis Block')
	def new_block(self , previous_hash=None):
		block= {'Block No  ':self.count ,'Transactions':self.new_transactions ,'GasFee':0.1 ,'Timestamp':time() ,'previous_hash':previous_hash}
		self.count=self.count+1
		self.chain.append(block)

		dumped_data=json.dumps(block)
		sha_value=hashlib.sha256(dumped_data.encode())
		hashed_data=sha_value.hexdigest()
		self.chain.append(('Current Hash: ' ,hashed_data))
		return Block

	def last_block(self):
		return self.chain[-1]
	def transactions(self,sender,recipient,amount):
		sender_encoded= hashlib.sha256(sender.encode())
		sender_hex= sender_encoded.hexdigest()
		recipient_encoded= hashlib.sha256(recipient.encode())
		recipient_hex= recipient_encoded.hexdigest()
		transactions_data={'sender' : sender_hex ,'recipient' : recipient_hex ,'amount' : amount }
		self.new_transactions.append(transactions_data)
		return self.last_block
	def hash(self,block):
		dumped_value=json.dumps(block)
		value_encoded= hashlib.sha256(dumped_value.encode())
		value_hex= value_encoded.hexdigest()
		self.chain.append('Current Hash : ' ,value_hex)
		return value_hex


Block_Object= Block()
transaction1=Block_Object.transactions('Amulya' ,'Atulya' ,'2 ETH')
transaction2=Block_Object.transactions('Amulya' ,'Atulya' ,'5 ETH')
transaction3=Block_Object.transactions('Amulya' ,'AShish' ,'9 ETH')
Block_Object.new_block()

print(Block_Object.chain)