from tkinter import *
from web3 import Web3

root = Tk()

root.title("My Ethereum App")
root.geometry("600x200")
root.configure(background="white")

block_name_label = Label(root, text="Ethereum gas fee in other currencies", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)

value_in_ether = Label(root, bg="white", font=("bold", 14))
value_in_ether.place(relx=0.5, rely=0.28, anchor=CENTER)
value_in_dollar = Label(root, bg="white", font=("bold", 10))
value_in_dollar.place(relx=0.5, rely=0.38, anchor=CENTER)
value_in_rupees = Label(root, bg="white", font=("bold", 10))
value_in_rupees.place(relx=0.5, rely=0.48, anchor=CENTER)
value_in_pounds = Label(root, bg="white", font=("bold", 10))
value_in_pounds.place(relx=0.5, rely=0.58, anchor=CENTER)

url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(url))

def ethereum_block():
    wei_price = web3.eth.gas_price
    gwei_price = wei_price / 10**9
    gas_price_in_ether = gwei_price / 10**9

    # Task 02: Convert the value of Gas to other currencies
    current_eth_value_in_dollars = 4053
    gas_price_in_dollar = gas_price_in_ether * current_eth_value_in_dollars

    # Task 03: Display the Prices in the application
    value_in_ether["text"] = "Value of gas in Ether: ETH " + str(gas_price_in_ether)
    value_in_dollar["text"] = "Value of gas in Dollar: $ " + str(gas_price_in_dollar)

    # Convert gas price to Rupees and Pounds
    current_eth_value_in_rupees = 335625.40
    gas_price_in_rupees = gas_price_in_ether * current_eth_value_in_rupees
    value_in_rupees["text"] = "Value of gas in Rupees: ₹ " + str(gas_price_in_rupees)

    current_eth_value_in_pounds = 3162.22
    gas_price_in_pounds = gas_price_in_ether * current_eth_value_in_pounds
    value_in_pounds["text"] = "Value of gas in Pounds: £ " + str(gas_price_in_pounds)

search_btn = Button(root, text="Search currency fee", command=ethereum_block, relief=FLAT)
search_btn.place(relx=0.5, rely=0.68, anchor=CENTER)
root.mainloop()
