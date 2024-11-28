for nonce in range(10): # set a range for iteration
	equation = 25-5+nonce
	if equation == 24:
		print('Verified, Your Nonce Value is : ' , nonce) #display as "verified" and mention the nonce value at which it got verified. 
		break
	else:
		print('Not Verified')#display as " not verified"