def visitors():
	file_open= open('hi.txt','r')
	read_data= int(file_open.read())
	close_file_1= file_open.close()

	read_data= read_data + 1

	file_open_to_write= open('hi.txt','w')
	write_data=file_open_to_write.write(read_data)
	close_file_2= file_open_to_write.close()
visitors()

