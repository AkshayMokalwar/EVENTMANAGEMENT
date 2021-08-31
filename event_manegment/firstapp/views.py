from django.shortcuts import render , redirect
import psycopg2
from django.core.files.storage import FileSystemStorage
import datetime

		
# Create your views here.

# the default home page of website
def home_view(request):
	# date =datetime.datetime.now()
	# print("**********")
	# print()
	return render(request,'firstapp/index.html');
def about_view(request):
	return render(request,'firstapp/about.html');

# for user login page 
def login_user_view(request):
	if(request.method == 'GET'):
		return render(request,'firstapp/login_user.html');
	elif(request.method == 'POST'):
		email1 = request.POST['txtemail']
		password1 =request.POST['txtpassword']

		mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
		mycursor=mydb.cursor()
		mycursor.execute('SELECT * FROM public.tbluser01 where tbluser01."user_email_ID"=%s;',(email1,))
		result=mycursor.fetchall();
		mydb.commit()
		mydb.close()

		
		
		# print("****************************************************************************")
		# print("********************************")
		# print(result[0][3]);
		# # because result is list of touple hence to access the password of user from database 

		if(result):
			
			if(password1==result[0][3]):
				mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
				mycursor=mydb.cursor()
				mycursor.execute('SELECT "admin_ID",admin_firstname, admin_lastname, "admin_emailID", hall_name, hall_address, hall_capasity, admin_mobile,image,booking_total_amount, booking_advance_amount, bookihg_balance_amount, booking_dates,  "booking_ID"  FROM public.tbladmin INNER JOIN public."tblbookings " ON tbladmin."admin_ID"= "booking_admin_ID" where "booking_user_ID"=%s;',(result[0][6],))

				booking_details = mycursor.fetchall();
				mydb.commit()
				mydb.close()
				print()
				
				# mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
				# mycursor=mydb.cursor()
				
			
				# mycursor.execute('SELECT * FROM public.tbladmin where "admin_ID"=%s;',(booking_details[i][1],))
				# k=mycursor.fetchall();
				# hall_d

				# mydb.commit()
				# mydb.close()
				# print("********************************")
				# print(booking_details)
				# print(len(hall_d));
				# user=[{"user":email1, "pass":password1}]
				# ,"hall_detailes":hall_d}
				return render(request,'firstapp/user_dash.html', {"record":result,"bookings":booking_details})	
				# return render(request,'firstapp/user_dash_2.html', {"record":result,"bookings":booking_details})	
			
			else:
				m="Wrong Password please try again!!!!";
				return render(request,'firstapp/failed.html',{'msg':m})
		else:
			m="user does not exist !!!!";
			return render(request,'firstapp/failed.html',{'msg':m})
		
		
		# return render(request,'firstapp/failed.html')
# for user dashboard page
def user_dash_view(request):
	return render(request,'firstapp/user_dash.html')


def edit_view(request,val,id):
	print("**********")
	print(val)
	print(id)
	if(request.method == 'GET'):
		mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
		mycursor=mydb.cursor()
		
		if(val=='a'):

			mycursor.execute('SELECT * FROM public.tbluser01 where tbluser01."user_ID"=%s;',(id,))
			result=mycursor.fetchall();
			mydb.commit()
			mydb.close()
			return render(request, 'firstapp/edit_user.html',{'record':result})
		elif(val=='b'):
			mycursor.execute('SELECT * FROM public.tbladmin where tbladmin."admin_ID"=%s;',(id,))
			result=mycursor.fetchall();
			mydb.commit()
			mydb.close()
			return render(request, 'firstapp/edit_admin.html',{'record':result})
	elif(request.method == 'POST'):
		mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
		mycursor=mydb.cursor()
		if(val=='a'):

			mycursor.execute('SELECT * FROM public.tbluser01 where tbluser01."user_ID"=%s;',(id,))
			result=mycursor.fetchall();
			# mydb.commit()
			# mydb.close()
			print("********************************")
			print(result[0][3])
			firstname1 = request.POST['txtfirstname']
			lastname1 = request.POST['txtlastname']
			add=request.POST['txtaddress']
			mobile1=request.POST['txtmobile']
			password1=request.POST['txtpassword']

			if(password1==result[0][3]):
				mycursor.execute('UPDATE public.tbluser01 SET firstname=%s, lastname=%s, user_address=%s, user_mobile_number=%s WHERE  "user_ID"=%s;',(firstname1,lastname1,add,mobile1 ,id,))
				mycursor.execute('SELECT * FROM public.tbluser01 where tbluser01."user_ID"=%s;',(id,))
				result=mycursor.fetchall();
				mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
				mycursor=mydb.cursor()
				mycursor.execute('SELECT "admin_ID",admin_firstname, admin_lastname, "admin_emailID", hall_name, hall_address, hall_capasity, admin_mobile,image,booking_total_amount, booking_advance_amount, bookihg_balance_amount, booking_dates,  "booking_ID"  FROM public.tbladmin INNER JOIN public."tblbookings " ON tbladmin."admin_ID"= "booking_admin_ID" where "booking_user_ID"=%s;',(result[0][6],))

				booking_details = mycursor.fetchall();
				mydb.commit()
				mydb.close()
	
				m="Hello "+result[0][0]+" "+result[0][1]+"!! Your profile has been updated"
				return render(request,'firstapp/user_dash.html', {"record":result,"bookings":booking_details,'msg':m})	
			else:
				m="Wong password";
				return	 render(request,'firstapp/failed.html',{'msg':m})
			return render(request, 'firstapp/success.html',{'msg':m})
		elif(val=='b'):
			mycursor.execute('SELECT * FROM public.tbladmin where tbladmin."admin_ID"=%s;',(id,))
			result=mycursor.fetchall();
			
			
			print("********************************")
			print(result[0][3])
			firstname1 = request.POST['txtfirstname']
			lastname1 = request.POST['txtlastname']
			# add=request.POST['txtaddress']
			mobile1=request.POST['txtmobile']
			password1=request.POST['txtpassword']
			hallname1=request.POST['txthallname']
			hallprice1=request.POST['txthallprice']

			# uploadedfile=request.FILES["hall_image"]
			print("**********")
			print(result[0][4])
			if(password1==result[0][4]):
				mycursor.execute('UPDATE public.tbladmin SET admin_firstname=%s, admin_lastname=%s, hall_name=%s, hall_price=%s,  admin_mobile=%s WHERE  "admin_ID"=%s;',(firstname1,lastname1,hallname1,hallprice1,mobile1 ,id,))
				mycursor.execute('SELECT * FROM public.tbladmin where tbladmin."admin_ID"=%s;',(id,))
				result=mycursor.fetchall();
				mycursor.execute('SELECT firstname, lastname, "user_email_ID", user_address, user_mobile_number, "user_ID",booking_total_amount, booking_advance_amount, bookihg_balance_amount, booking_dates,  "booking_ID"  FROM public.tbluser01 INNER JOIN public."tblbookings " ON tbluser01."user_ID"= "booking_user_ID" where "booking_admin_ID"=%s;',(result[0][0],))
				
				booking_details = mycursor.fetchall();
				mydb.commit()
				mydb.close()
				m=" Successfully updated"
				# m="Hello "+result[0][0]+" "+result[0][1]+"!! Your profile has been updated"
				return render(request,'firstapp/admin_dash.html', {"record":result,"bookings":booking_details,'msg':m})	
			else:
				m="Wong password";
				return	 render(request,'firstapp/failed.html',{'msg':m})
			

# for admin login page 
def login_admin_view(request):
	if(request.method == 'GET'):
		return render(request,'firstapp/login_admin.html');
	elif(request.method == 'POST'):
		email1 = request.POST['txtemail']
		password1 =request.POST['txtpassword']

		mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
		mycursor=mydb.cursor()
		mycursor.execute('SELECT * FROM public.tbladmin where tbladmin."admin_emailID"=%s;',(email1,))
		result=mycursor.fetchall();
		mydb.commit()
		mydb.close()
		# result store admin data
		# print("****************************************************************************")
		# print("********************************")
		# print(result[0][4]);
		# # because result is list of touple hence to access the password of user from database 
		
		if(result):
			
			if(password1==result[0][4]):
				# user=[{"user":email1, "pass":password1}]
				mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
				mycursor=mydb.cursor()
				mycursor.execute('SELECT firstname, lastname, "user_email_ID", user_address, user_mobile_number, "user_ID",booking_total_amount, booking_advance_amount, bookihg_balance_amount, booking_dates,  "booking_ID"  FROM public.tbluser01 INNER JOIN public."tblbookings " ON tbluser01."user_ID"= "booking_user_ID" where "booking_admin_ID"=%s;',(result[0][0],))

				booking_details = mycursor.fetchall();
				mycursor.execute('SELECT sum(booking_total_amount),sum(booking_advance_amount),sum(bookihg_balance_amount) FROM public."tblbookings " where "booking_admin_ID"=%s;',(result[0][0],))

				total_earings_results = mycursor.fetchall();
				mydb.commit()
				mydb.close()
				# print("****	******")
				# print(booking_details)
				return render(request,'firstapp/admin_dash.html', {"record":result,"bookings":booking_details,'total_earings_records':total_earings_results})	
			else:
				m="Wrong Password please try again!!!!";
				return render(request,'firstapp/failed.html',{'msg':m})
		else:
			m="Admin does not exist !!!!";
			return render(request,'firstapp/failed.html',{'msg':m})
		
			

# for admin dashboard page

def admin_dash_view(request):
	if request.method =='GET':
		return render(request,'admin_dash.html',{"record":result});
	elif request.method =='POST':
		return render(request,'firstapp/admin_dash.html',{"record":result})
def search_view(request):
	if request.method == 'GET':
		mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
		mycursor=mydb.cursor()
		mycursor.execute('SELECT * FROM public.tbladmin order by "admin_ID"')
		result=mycursor.fetchall();
		mydb.commit()
		mydb.close()
		# print(result);
		return render(request,'firstapp/search.html',{"records":result})
	elif request== 'POST' :
		print("**********")
		sel=request.POST['txtopt']
		print("**********")
		# print(sel);
		# mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
		# mycursor=mydb.cursor()
		# mycursor.execute('SELECT * FROM public.tbladmin where tbladmin.hall_address = %s',(cityname1))
		# result1=mycursor.fetchall();
		
		# print(result1);
		# return render(request,'firstapp/search.html',{"records":result1})
		return render(request,'firstapp/search.html')
def sort_view(request,id):
	if(request.method == 'GET'):
		print("********************************")
		print(id);
		mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
		mycursor=mydb.cursor()
		if(id=='a'):
			mycursor.execute('SELECT * FROM public.tbladmin order by hall_price ;')
		elif(id=='b'):
			mycursor.execute('SELECT * FROM public.tbladmin order by hall_capasity desc ;')
		result=mycursor.fetchall();
		mydb.commit()
		mydb.close()
		
		print("****************************************************************************")
		for i in range(int(len(result))):
			print("********************************")
			print(result[i]);
		return render(request,'firstapp/search.html',{"records":result})
def info_view(request,id):
	if(request.method == 'GET'):
		print(id);
		mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
		mycursor=mydb.cursor()
		mycursor.execute('SELECT * FROM public.tbladmin where "admin_ID"=%s;',(id,))
		result=mycursor.fetchall();
		mydb.commit()
		mydb.close()
		
		# print("****************************************************************************")
		# print("********************************")
		# print(result[0][4]);
		return render(request,'firstapp/info.html',{"records":result})
	elif request.method == "POST":
		user_email_ID1=request.POST['txtuser_email']
		user_password1=request.POST['txtuser_password']
		user_bookingd_date=request.POST['txt_user_date']
		user_advance_ammount=request.POST['txt_user_amount']
		# curerent=date=datetime.datetime.now()
		# if(user_bookingd_date>=):

		print(user_bookingd_date);
		# result store user records
		mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
		mycursor=mydb.cursor()
		mycursor.execute('SELECT * FROM public.tbluser01 where tbluser01."user_email_ID"=%s;',(user_email_ID1,))
		result=mycursor.fetchall();
		mydb.commit()
		mydb.close()
		
		# print("**************************************************************************")
		# print("********************************")
		# print(result);
		# print(user_advance_ammount)

		# result2 store admin records
		mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
		mycursor=mydb.cursor()
		mycursor.execute('SELECT * FROM public.tbladmin where "admin_ID"=%s;',(id,))
		result2=mycursor.fetchall();
		mydb.commit()
		mydb.close()

		print("****************************************************************************")
		print(int(result2[0][7]))
		print(int(result2[0][7])-int(user_advance_ammount));
		print(user_advance_ammount)
		# print(user_bookingd_date)
		# # because result is list of touple hence to access the password of user from database 
	
		
		if(user_password1==result[0][3]):
			# user=[{"user":email1, "pass":password1}]
			mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
			mycursor=mydb.cursor()
			mycursor.execute('INSERT INTO public."tblbookings "("booking_user_ID", "booking_admin_ID", booking_total_amount, booking_advance_amount, bookihg_balance_amount, booking_dates)VALUES (%s, %s, %s, %s,%s,%s);',(int(result[0][6]),int(id),int(result2[0][7]),int(user_advance_ammount),int(result2[0][7])-int(user_advance_ammount),user_bookingd_date,))
			print("********************************Sucess")
			mydb.commit()
			mydb.close()


			mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
			mycursor=mydb.cursor()
			mycursor.execute('SELECT "admin_ID",admin_firstname, admin_lastname, "admin_emailID", hall_name, hall_address, hall_capasity, admin_mobile,image,booking_total_amount, booking_advance_amount, bookihg_balance_amount, booking_dates, "booking_ID"  FROM public.tbladmin INNER JOIN public."tblbookings " ON tbladmin."admin_ID"= "booking_admin_ID" where "booking_user_ID"=%s;',(result[0][6],))

			booking_details = mycursor.fetchall();
			return render(request,'firstapp/user_dash.html', {"record":result,"bookings":booking_details});
			# return  redirect('/user-dashboard/', {"record":result})
		else:
			return render(request,'firstapp/failed.html')
		

	
def user_registration_view(request):
	if(request.method == 'GET'):
		return render(request,'firstapp/user_registrastion.html');
	elif(request.method == 'POST'):
		firstname1 = request.POST['txtfirstname']
		lastname1 = request.POST['txtlastname']
		email1 = request.POST['txtemail']
		password1=request.POST['txtpassword']
		add=request.POST['txtaddress']
		mobile1=request.POST['txtmobile']

		mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
		mycursor=mydb.cursor()
		mycursor.execute('INSERT INTO public.tbluser01(firstname, lastname, "user_email_ID", user_password, user_address, user_mobile_number)VALUES (%s, %s, %s, %s,%s,%s);',(firstname1,lastname1,email1,password1,add,mobile1))

		mydb.commit()
		mydb.close()
		return redirect('/login-user/');
def admin_registration_view(request):
	if(request.method == 'GET'):
		return render(request,'firstapp/admin_registration.html');
	elif(request.method == 'POST'):
		firstname1 = request.POST['txtfirstname']
		lastname1 = request.POST['txtlastname']
		email1 = request.POST['txtemail']
		password1=request.POST['txtpassword']
		mobile1=request.POST['txtmobile']
		halladd=request.POST['txthalladdress']
		
		hallname1=request.POST['txthallname']
		hallprice1=request.POST['txthallprice']
		hallcapasity1=request.POST['txthallcapacity']

		uploadedfile=request.FILES["hall_image"]
		# print(uploaded_file.name)
		# print(uploaded_file.size)
		fs=FileSystemStorage();
		# uploaded_file.name='12.jpg'
		filename=fs.save(uploadedfile.name, uploadedfile)
		uploaded_file_urls = fs.url(filename)
		print(uploaded_file_urls)

		mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
		mycursor=mydb.cursor()
		mycursor.execute('INSERT INTO public.tbladmin(admin_firstname, admin_lastname, "admin_emailID", admin_password, hall_name, hall_address, hall_price, hall_capasity, admin_mobile,image)VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s);',(firstname1,lastname1,email1,password1,hallname1,halladd,hallprice1,hallcapasity1,mobile1,uploaded_file_urls))

		mydb.commit()
		mydb.close()
		return redirect('/login-admin/');
def categoryname_view(request, *args, **kwargs):
	return render(request,'firstapp/categoryname.html');
def category_preview_view(request,opt):
	print(opt)
	if(opt=='HL'):
		print("Successfully")
		return redirect('/Search/')
	elif(opt=='CS'):
		category = "Catering Service";
	elif(opt=='DJ'):
		category = "DJs"
	elif(opt=='CD'):
		category = "CLothings and Design"
	return render(request,'firstapp/category.html',{'cat':category});

# def upload_view(request):
# 	if request.method =='GET':
# 		return render(request,'firstapp/upload.html')
# 	elif request.method =='POST':
# 		uploadedfile=request.FILES['uploaded_file']
# 		firstname1 = request.POST['txtname']
# 		# print(uploaded_file.name)
# 		# print(uploaded_file.size)
# 		fs=FileSystemStorage();
# 		# uploaded_file.name='12.jpg'
# 		filename=fs.save(uploadedfile.name, uploadedfile)
# 		uploaded_file_urls = fs.url(filename)
# 		print(uploaded_file_urls)
# 		# arr.append(uploaded_file);
# 		mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
# 		mycursor=mydb.cursor()
# 		mycursor.execute('INSERT INTO  public.tblupload(name, image_path) VALUES (%s,%s);',(firstname1,filename))

# 		mydb.commit()
# 		mydb.close()
# 		return render(request,'firstapp/upload.html')

# def prev_view(request):
# 	if request.method =='GET':
# 		return render(request,'firstapp/prev1.html')
# 	if request.method =='POST':
# 		firstname1 = request.POST['txtname']
# 		mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
# 		mycursor=mydb.cursor()
# 		mycursor.execute('SELECT * FROM public.tblupload where tblupload.name=%s;',(firstname1,))
# 		result=mycursor.fetchall();
# 		print(result[0][1]);
# 		mydb.commit()
# 		mydb.close()
# 		return render(request,'firstapp/img_prev.html',{'path':result[0][1]})