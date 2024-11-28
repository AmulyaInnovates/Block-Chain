from tkinter import *
from web3 import Web3
from PIL import ImageTk, Image

root = Tk()
root.title("Account Details")

ganache_url = 'HTTP://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
panel = Label(root, image=img, bg='white')
panel.pack(side="top")

frame = Frame(
    root,
    bg='white',
    padx=5,
    pady=5
)

# Create labels for account numbers
Label(frame, text="Account number 1:", fg='black', bg='white').grid(row=0, column=0, sticky=W, pady=10)
Label(frame, text="Account number 2:", fg='black', bg='white').grid(row=1, column=0, sticky=W, pady=10)
Label(frame, text="Account number 3:", fg='black', bg='white').grid(row=2, column=0, sticky=W, pady=10)
Label(frame, text="Account number 4:", fg='black', bg='white').grid(row=3, column=0, sticky=W, pady=10)
Label(frame, text="Account number 5:", fg='black', bg='white').grid(row=4, column=0, sticky=W, pady=10)

# Create entry elements
account1 = Entry(frame)
account2 = Entry(frame)
account3 = Entry(frame)
account4 = Entry(frame)
account5 = Entry(frame)

# Place the entry elements on the frame
account1.grid(row=0, column=1, padx=10, pady=20)
account2.grid(row=1, column=1, padx=10, pady=20)
account3.grid(row=2, column=1, padx=10, pady=20)
account4.grid(row=3, column=1, padx=10, pady=20)
account5.grid(row=4, column=1, padx=10, pady=20)

# Create the text box to show the results
result = Text(root, height=10, width=45, bg='light yellow')
result.pack(pady=5)

# Define a function to check the balance
def CHECK_BALANCE():
    account_no = []
    account_no.append(account1.get())
    account_no.append(account2.get())
    account_no.append(account3.get())
    account_no.append(account4.get())
    account_no.append(account5.get())
    
    count = 1
    for i in account_no:
        try:
            balance = web3.eth.get_balance(i)
            balance = balance * 0.000000000000000001  # Convert from Wei to Ether
            result.insert(END, f"Account {count}: {balance} Ether\n")
            print(END, f"Account {count}: {balance} Ether\n")
    		
        except Exception as e:
            result.insert(END, f"Account {count}: Error fetching balance\n")
            print(END, f"Account {count}: Error fetching balance\n")
        count += 1
    print('----------------------')
    result.insert(END, '---------------------------------------------')

# Create a button element to call the CHECK_BALANCE function
check_balance = Button(root, text="CHECK BALANCE", width=15, command=CHECK_BALANCE, bg='light blue')
check_balance.pack(fill='both', pady=10)

frame.pack()

root.mainloop()
