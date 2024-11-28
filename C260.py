from etherpad_lite import EtherpadLiteClient
from datetime import datetime

api_connection= EtherpadLiteClient(base_params={'apikey':''})
group= api_connection.createGroup()
print(group)

pad_creation= api_connection.createPad(padID='mynewpad', text='Hi Everybody!')

author_creation= api_connection.createAuthor(name='Amulya')
print(author_creation)
no_of_users= api_connection.padUsersCount(padID='mynewpad')
print('Pad is opened: ' ,  no_of_users , ' times')
last_edited_data= api_connection.getLastEdited(padID='mynewpad')
t= last_edited_data('last_Edited')

time= datetime.timeStamp(t/1000.0)
print('The Last Time Edited: ', time)

deleted_pad_data=api_connection.deletePad(padID='mynewpad')
print('Deleted Pad Data is: ', deleted_pad_data)