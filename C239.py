import hashlib
import json
from time import time

chain= []

def block(proof,previous_hash=None):
	transaction= {'sender': 'Atulya' , 'reciever': 'Amulya' , 'amount': '5 ETH' }
	data= {'index': 1 , 'timestamp': time(),  'transactions': transaction , 'gas/fee': 0.1 , 'proof': proof , 'previous_hash': 'None' }

	chain.append(block)
	print('The Block Information' , data)
	dumped_data= json.dumps(data)
	encoded_data= hashlib.sha256(dumped_data.encode())
	print('Hash Code of The Block' , encoded_data.hexdigest())
block(previous_hash='No previous Hash as it is The 1st Block in the Block Chain.' , proof=000)