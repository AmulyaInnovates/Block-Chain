from tkinter import *
from tkinter import messagebox
from web3 import Web3
from PIL import ImageTk, Image

root= Tk()
root.title('My Crypto Bank')
root.geometry('600x600')
root.configure(background='white')

infura_link='HTTP://127.0.0.1:7545'
web3= Web3(Web3.HTTPProvider(infura_link))

image_1= ImageTk.PhotoImage(Image.open('logo.jpeg'))
label1= Label(root, image=image_1)
label1.pack(side= 'top')

f1=Frame(root, padx=5,pady=5,bg='white')

Label(f1, text='Sender:- ', bg='white').grid(row=0,column=0,sticky=W,pady=10)
Label(f1,text='Reciever:- ', bg='white').grid(row=1,column=0,sticky=W,pady=10)
Label(f1,text='Amount:- ', bg='white').grid(row=2,column=0,sticky=W,pady=10)
Label(f1,text='Private Key:- ', bg='white').grid(row=3,column=0,sticky=W,pady=10)
Label(f1,text='Gas Price[GWEI]:- ', bg='white').grid(row=4,column=0,sticky=W,pady=10)
Label(f1,text='Gas[GWEI]:- ', bg='white').grid(row=5,column=0,sticky=W,pady=10)

account1=Entry(f1)
account2=Entry(f1)
amount=Entry(f1)
pk=Entry(f1)
gp=Entry(f1)
gl=Entry(f1)

account1.grid(row=0,column=1,sticky=W,pady=10,padx=10)
account2.grid(row=1,column=1,sticky=W,pady=10,padx=10)
amount.grid(row=2,column=1,sticky=W,pady=10,padx=10)
pk.grid(row=3,column=1,sticky=W,pady=10,padx=10)
gp.grid(row=4,column=1,sticky=W,pady=10,padx=10)
gl.grid(row=5,column=1,sticky=W,pady=10,padx=10)

def Transaction_make():

	a1_data=account1.get()
	a2_data=account2.get()
	amount_data=int(amount.get())
	pk_data=pk.get()
	gp_data=int(gp.get())
	gl_data=int(gl.get())
	nonce=web3.eth.get_transaction_count(a1_data)
	tx={
	'nonce':nonce,
	'to':a2_data,
	'value':web3.to_wei(amount_data,'ether'),
	'gas':web3.to_wei(gl_data ,'gwei'),
	'gasPrice':gp_data
	}

	signed_tx = web3.eth.account.sign_transaction(tx, pk_data)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print('Your transaction is successful. Your Transaction ID is:', web3.to_hex(tx_hash))
    messagebox.showinfo('Transaction status!', 'Transaction Successful! Verify your metamask wallet!')

f1.pack()

check_balance = Button(root, text="MAKE TRANSACTION", width=15, command=Transaction_make, bg='light blue')
check_balance.pack(fill='both', pady=10)

root.mainloop()