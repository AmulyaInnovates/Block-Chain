from web3 import Web3
from tkinter import *

root = Tk()

root.title("My Ethereum App")
root.geometry("500x250")  # Increased height to accommodate the gas label
root.configure(background="white")

block_name_label = Label(root, text="Ethereum Block", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.1, anchor=CENTER)
block_entry = Entry(root, bd=2)
block_entry.insert(0, "19424646")  # Inserting the default block number
block_entry.place(relx=0.5, rely=0.3, anchor=CENTER)
gasused_info_label = Label(root, bg="white", font=("bold", 10))
gasused_info_label.place(relx=0.5, rely=0.45, anchor=CENTER)
gaslimit_info_label = Label(root, bg="white", font=("bold", 10))
gaslimit_info_label.place(relx=0.5, rely=0.6, anchor=CENTER)  # Adjusted position to avoid overlap

url = 'https://mainnet.infura.io/v3/800b34901df94fadabc75170fd2125e9'
web3 = Web3(Web3.HTTPProvider(url))

def ethereum_block():
    try:
        number = int(block_entry.get())
        block_data = web3.eth.get_block(number)
        
        # Check if block_data contains transactions
        if 'transactions' in block_data and len(block_data['transactions']) > 0:
            transaction = web3.eth.get_transaction(block_data['transactions'][-1])
            value = transaction['value']
            value_in_ether = int(value) / 10**18
            current_eth_value_in_dollars = 2522  # This should be fetched from a reliable source
            value_in_dollar = value_in_ether * current_eth_value_in_dollars
            
            gas_used = transaction['gasPrice'] * transaction['gas']
            
            gasused_info_label["text"] = "Value: $" + str(value_in_dollar)
            gaslimit_info_label["text"] = "Gas: " + str(transaction['gas']) + "\nGas Used: " + str(gas_used)
            block_name_label["text"] = "Ethereum Block: " + block_entry.get()
        else:
            gasused_info_label["text"] = "Error: No transactions found in the block"
            gaslimit_info_label["text"] = ""
            block_name_label["text"] = ""
    except KeyError:
        gasused_info_label["text"] = "Error: Block data structure does not contain 'value'"
        gaslimit_info_label["text"] = ""
        block_name_label["text"] = ""
    except Exception as e:
        gasused_info_label["text"] = "Error: " + str(e)
        gaslimit_info_label["text"] = ""
        block_name_label["text"] = ""

search_btn = Button(root, text="Search Ethereum transaction fee", command=ethereum_block, relief=FLAT)
search_btn.place(relx=0.5, rely=0.8, anchor=CENTER)  # Adjusted position to avoid overlap

root.mainloop()
