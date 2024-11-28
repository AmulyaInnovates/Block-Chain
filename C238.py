import hashlib

text1= 'Amulya paid 100 on 13 October'
text_made1= hashlib.sha256(text1.encode())
print('13 October :- ' , text_made1.hexdigest())

text2= 'Amulya paid 300 on 1 January'
text_made2= hashlib.sha256(text2.encode())
print('1 January :- ' , text_made2.hexdigest())

text3= 'Amulya paid 500 on 9 January'
text_made3= hashlib.sha256(text3.encode())
print('9 January :- ' , text_made3.hexdigest())