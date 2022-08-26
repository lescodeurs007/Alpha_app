#importing modules
from databasecreation import *
import random
import streamlit_authenticator as stauth
import streamlit as st
import mysql.connector as sqltor


#defining login check function with 2 paramaters for phone number and password
def logincheck():

	#defining query for fetching phone_num(int) and password(str) from "User_Details" table and executing it
	querystr1='''Select Ph_No,Pwd,User_Name from User_Details'''
	cursor.execute(querystr1)

	#fetching the data and storing it in variable user_data_list
	user_data_list=cursor.fetchall()

	#defining 3 variables for names,phone number(usernames) and passwords
	names=[]
	usernames=[]
	passwords=[]

	#appending all the details into the lists
	for i in user_data_list:
		usernames.append(str(i[0]))
		passwords.append(i[1])
		names.append(i[2])

	passwords1=stauth.Hasher(passwords).generate()




	#creating credentials dictionary in the format for the streamlit authenticater
	credentials = {"usernames":{}}

	for un, name, pw in zip(usernames, names, passwords1):
		user_dict = {"name":name,"password":pw}
		credentials["usernames"].update({un:user_dict})

	print(credentials)

	return credentials








	# #checking is the phonenumber and password match the details in the database
	# for i in user_data_list:
	# 	if Phone_num==i[0]:
	# 		if Password==i[1]:
	# 			return 1    #returning "1" when the phone number and password matches
	# 		else:
	# 			return 0	#returning "0" when the phone number and password does not match

	# return 0				#returning "0" when the phone number does not exist in the database



#defing unique id generation function 
def uniqueid_gen():

	#generating unique id using random module function randit
	Uniqueid=random.randint(10**16,((10**17)-1))

	#defing query for fetching unique id from "User_Details Table"
	querystr2='''Select Unique_ID from User_Details where Unique_ID={}'''.format(Uniqueid)
	cursor.execute(querystr2)

	#fetching the data and storing it in variable Unique_ID_list
	Unique_ID_list=cursor.fetchall()

	#checking if the unique id already exists
	if Unique_ID_list!=[]:
		uniqueid_gen()		#calling uniqueid_gen function to generate another id in the case it already exists
	else:
		return Uniqueid  	#returning the uniqueid to signup function



#defining signup function with four parameters for shopname(str),fullname(str),phone number(int) and password(str)
def signup_check(Shop_Name,Full_Name,Phone_Num,Password):

	#defining query for fetching phone numbers from "User_Details" table and executing it
	querystr3='''Select Ph_No from User_Details where Ph_No={}'''.format(Phone_Num)
	cursor.execute(querystr3)

	#fetching the data and storing it in variable user_data_list
	Phone_Number_data_list=cursor.fetchall()


	#checking if phone number already exists or not
	if Phone_Number_data_list!=[]:
		return 0		   #returning '0' if the phonenumber already exists  	
	else:

		#getting unique id
		Uniqueid=uniqueid_gen()



		#defining query for inserting data into "User_Details" table and executing iy
		querystr4='''Insert into User_Details(Shop_Name,User_Name,Ph_No,Pwd,Unique_ID) Values("{}","{}",{},"{}",{})'''.format(Shop_Name,Full_Name	,Phone_Num,Password,Uniqueid)
		cursor.execute(querystr4)
		
		mycon.commit()   #saving changes

		return 1     	 #returning '1' when the data is inserted successfully



#defining function for insert lattitude and longitudw
def insertlocation(ph_no,lat,long):
	#defining query for getting unique id using lat and long and executing it
	querystr5='''Select Unique_ID,Shop_Name from User_Details where Ph_No={}'''.format(int(ph_no))
	cursor.execute(querystr5)

	#fetching unique id and shop name and assigning it to unique_id variable and shop_name variable
	data_list=cursor.fetchall()
	unique_id=data_list[0][0]
	shop_name=data_list[0][1]

	# print('a')
	# print(unique_id)


	#defining query for inserting unique_id,latitude,longitude and shop namw and executing it
	querystr6='''INSERT INTO Shop_Details(Unique_ID,Latitude,Longitude,Shop_Name) Values({},"{}","{}","{}")'''.format(int(unique_id),str(lat),str(long),shop_name)
	cursor.execute(querystr6)

	mycon.commit()


def checking_lat_long(ph_no):
	#defining query for getting unique id using lat and long and executing it
	querystr5='''Select Unique_ID from User_Details where Ph_No={}'''.format(int(ph_no))
	cursor.execute(querystr5)

	#fetching unique id and assigning it to unique_id variable
	unique_id=cursor.fetchall()[0][0]

	#defining query for fetching lattittude and longitude
	querystr6='''Select Latitude,Longitude from Shop_Details where Unique_ID={}'''.format(int(unique_id))
	cursor.execute(querystr6)

	lat_long_data=cursor.fetchall()

	if lat_long_data!=[]:
		return 1
	else:
		return 0

def insertitems(Phone_Num,items_dict):
	categories=[]
	items=[]
	for i in items_dict:
		if items_dict[i]!=[]:
			categories.append(i)
			items.extend(items_dict[i])
	querystr5='''Select Unique_ID from User_Details where Ph_No={}'''.format(int(Phone_Num))
	cursor.execute(querystr5)
	#fetching unique id and assigning it to unique_id variable
	unique_id=cursor.fetchall()[0][0]
	# print(categories)
	# print(items)
	# print(unique_id)
	querystr6='''UPDATE Shop_Details set Categories="{}",Items_Price="{}" where Unique_ID={}'''.format(str(categories),str(items),int(unique_id))
	#print(querystr6)
	cursor.execute(querystr6)
	mycon.commit()
	return 1

# insertlocation(9876543210,'10.343434','`17.82918291') checked and converted to big int


# fruits=['a','b','c']
# vegetables=['d','e','f']
# snacks=[]
# juices=[]
# passing_value={"fruits":fruits,"vegetables":vegetables,"snacks":snacks,"juices":juices}
#
# insertitems(9988776611,passing_value)







