import hashlib
PB_current_hash = "83e07ec8afb5bcac4b149f2aa76eaf050ef6e50b39673ee87dcb9dc3b6b71b91"

string_data='Alice sends James 5 Eth amount to Amulya'

encoded= hashlib.sha256(string_data.encode())
hexadecimal_value= encoded.hexdigest()
print(hexadecimal_value)

if PB_current_hash == hexadecimal_value:
	print('The Previous Hash Value is same as Current hash value')
else:
	print('The Previous Hash Value is not same as Current hash value')