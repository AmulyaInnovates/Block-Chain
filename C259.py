from etherpad_lite import EtherpadLiteClient

etherpad_api= EtherpadLiteClient(base_params={'api', 'KEY'})

group=etherpad_lite.creatGroup()
print('Your new group is:- ', group)

pad_new=etherpad_lite.createPad(padID='Amulya_1',text='Hi')
print('Your New Pad ID is:- ',pad_new)