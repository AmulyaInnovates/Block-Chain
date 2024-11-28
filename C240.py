class Vehicles:
	car1='Tesla'
	car2='BMW'
	def main(self):
		print('I have: ' , self.car1)
		print('I have: ' , self.car2)
Vehicle_function_copy=Vehicles()
print('Do you have a',Vehicle_function_copy.car2 ,' ??')
Vehicle_function_copy.main()