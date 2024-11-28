import hashlib
import json
from time import time
import random

class Block(object):
    def __init__(self):
        self.chain = []
        self.new_transactions = []
        self.count = 0
        self.new_block(previous_hash="No previous Hash. Since this is the first block.", proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'Block No': self.count,
            'timestamp': time(),
            'transactions': self.new_transactions or 'No Transactions First Genesis Block',
            'gasfee': 0.1,
            'nonce': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]) ,

        }
        self.new_transactions = []
        self.count = self.count + 1
        self.chain.append(block)

        return block

    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof_condition = False

        while check_proof_condition is False:
            compare_proof = new_proof ** 2 - previous_proof ** 2
            string_compare_proof = str(compare_proof).encode()
            encode_proof = hashlib.sha256(string_compare_proof)
            hash_proof = encode_proof.hexdigest()
            if hash_proof[:4] == '0000':
                check_proof_condition = True
            else:
                new_proof = new_proof + 1

        return new_proof

    def transaction(self, sender, recipient, amount):
        sender_encoder = hashlib.sha256(sender.encode())
        sender_hash = sender_encoder.hexdigest()
        recipient_encoder = hashlib.sha256(recipient.encode())
        recipient_hash = recipient_encoder.hexdigest()

        transaction_data = {
            'sender': sender_hash,
            'recipient': recipient_hash,
            'amount': amount
        }
        self.new_transactions.append(transaction_data)
        return self.last_block

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        block['Current hash'] = hex_hash
        return hex_hash

    def mine(self):
        last_block_value= blockchain.last_block()
        proof_value=last_block_value['nonce']
        proof_ow_value=blockchain.proof_of_work(proof_value)
        hash_value=blockchain.hash(last_block_value)
        blockchain.new_block(proof_ow_value , hash_value) 
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            current_block = chain[block_index]
            if current_block['previous_hash'] != previous_block['Current hash']:
                return False

            previous_nonce = previous_block['nonce']
            current_nonce = current_block['nonce']
            compare_proof = current_nonce ** 2 - previous_nonce ** 2

            string_compare_proof = str(compare_proof).encode()

            encode_compare_proof = hashlib.sha256(string_compare_proof)

            hash_compare_proof = encode_compare_proof.hexdigest()

            if hash_compare_proof[:4] != '0000':
                return False
            previous_block = current_block
            block_index = block_index + 1

        return True


blockchain = Block()
##predefined code ends

for i in range(5):
    print('Enter the details for the New Block Number :-', i)
    sender=input('Enter the Name of Sender: ')
    reciever=input('Enter the Name of Reciever: ')
    amount=input('Enter the Number of ETH to be sent: ')
    blockchain.transaction(sender,reciever,amount)
    blockchain.mine()
print('Entire Block-Chain :- ',blockchain.chain)
#predefined code begins

valid = blockchain.chain_valid(blockchain.chain)
if valid:
    print('The Blockchain is valid.')
else:
    print('The Blockchain is not valid.')
##predefined code ends