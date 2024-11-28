import hashlib
import json
from time import time


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
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
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
            print('Getting proof of work:',hash_proof)
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

    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            current_block = chain[block_index]
            if current_block['previous_hash'] != previous_block['Current hash']:
                return False

            previous_nonce = previous_block['nonce']
            current_nonce = current_block['nonce']
            print('Previous nonce of previous block:',previous_nonce)
            print('Current nonce of current block:',current_nonce)
            compare_proof = current_nonce ** 2 - previous_nonce ** 2
            print('Comparison of proof:',compare_proof)
            string_compare_proof = str(compare_proof).encode()
            print('Conversion of proof into string:',string_compare_proof)
            encode_compare_proof = hashlib.sha256(string_compare_proof)
            print('Encoding of proof:',encode_compare_proof)
            hash_compare_proof = encode_compare_proof.hexdigest()
            print('Current block nonce is:',hash_compare_proof)
            if hash_compare_proof[:4] != '0000':
                return False
            previous_block = current_block
            block_index = block_index + 1

        return True



blockchain = Block()
# Task 01 starts from below



previous_block = blockchain.last_block()
previous_proof = previous_block['nonce']

proof = blockchain.proof_of_work(previous_proof)
print("Found proof of work at:",proof)

previous_hash = blockchain.hash(previous_block)
print('Previous block hash:',previous_hash)
block = blockchain.new_block(proof, previous_hash)

# Task 02 starts from below





previous_block = blockchain.last_block()
previous_proof = previous_block['nonce']

proof = blockchain.proof_of_work(previous_proof)
print("Found proof of work at:",proof)

previous_hash = blockchain.hash(previous_block)
print('Previous block hash:',previous_hash)
block1 = blockchain.new_block(proof, previous_hash)



print(blockchain.chain)
valid = blockchain.chain_valid(blockchain.chain)
if valid:
    print('The Blockchain is valid.')
else:
    print('The Blockchain is not valid.')

import hashlib
import json
from time import time


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
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
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
            print('Getting proof of work:', hash_proof)
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

    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            current_block = chain[block_index]
            if current_block['previous_hash'] != previous_block['Current hash']:
                return False

            previous_nonce = previous_block['nonce']
            current_nonce = current_block['nonce']
            print('Previous nonce of previous block:',previous_nonce)
            print('Current nonce of current block:',current_nonce)
            compare_proof = current_nonce ** 2 - previous_nonce ** 2
            print('Comparison of proof:',compare_proof)
            string_compare_proof = str(compare_proof).encode()
            print('Conversion of proof into string:',string_compare_proof)
            encode_compare_proof = hashlib.sha256(string_compare_proof)
            print('Encoding of proof:',encode_compare_proof)
            hash_compare_proof = encode_compare_proof.hexdigest()
            print('Current block nonce is:',hash_compare_proof)
            if hash_compare_proof[:4] != '0000':
                return False
            previous_block = current_block
            block_index = block_index + 1

        return True


blockchain = Block()

# Task 01
transaction1 = blockchain.transaction("Amulya", "Nabeela Mam", '3 ETH')  # Change YourName and TeacherName
transaction2 = blockchain.transaction("Amulya", "Nabeela Mam", '2 ETH')  # Change YourName and TeacherName

# Task 02
transaction3 = blockchain.transaction("Amulya", "Himali", '10 ETH')  # Change YourName and FamilyMemberName
transaction4 = blockchain.transaction("Amulya", "Atulya", '7 ETH')  # Change YourName and FriendName


print(blockchain.chain)
valid = blockchain.chain_valid(blockchain.chain)
if valid:
    print('The Blockchain is valid.')
else:
    print('The Blockchain is not valid.')
