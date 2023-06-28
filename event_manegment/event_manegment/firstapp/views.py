from django.shortcuts import render , redirect
import psycopg2
from django.core.files.storage import FileSystemStorage
import datetime
import sqlite3
	
from firstapp.models import tbladmin,tblbookings,tbluser
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
		result=[]
		tbluser_list=tbluser.objects.filter(user_email_ID=email1)
		if(len(tbluser_list)<=0):
			m="user does not exist !!!!"
			return render(request,'firstapp/failed.html',{'msg':m})
		tbluser_list=tbluser.objects.filter(user_email_ID=email1,user_password=password1)
		if(len(tbluser_list)<=0):
			m="Wrong Password please try again!!!!"
			return render(request,'firstapp/failed.html',{'msg':m})
		for i in tbluser_list:
			result.append((i.firstname,i.lastname,i.user_email_ID,i.user_password,i.user_address,i.user_mobile_number,i.user_ID,i.profilepicture))
		booking_details=[]
		
		booking_details_list=tblbookings.objects.filter(booking_user_ID=tbluser_list[0])
		for j in booking_details_list:
			#  admin_ID,admin_firstname,admin_lastname,admin_emailID,hall_name,hall_add,hall_capasity,admin_mobile,hall_image,booking_total,booking_advance,booking_balance,booking_date,bookingID 
			booking_details.append((j.booking_admin_ID.admin_ID,j.booking_admin_ID.admin_firstname,j.booking_admin_ID.admin_lastname, j.booking_admin_ID.admin_emailID, j.booking_admin_ID.hall_name, j.booking_admin_ID.hall_address, j.booking_admin_ID.hall_capasity, j.booking_admin_ID.admin_mobile,j.booking_admin_ID.image,j.booking_total_amount, j.booking_advance_amount, j.bookihg_balance_amount, j.booking_dates,  j.booking_ID))
		print('#4444','booking_details',booking_details)
		
		return render(request,'firstapp/user_dash.html', {"record":result,"record_count":len(result),"bookings":booking_details})

# for user dashboard page
def user_dash_view(request):
	return render(request,'firstapp/user_dash.html')


def edit_view(request,val,id):
	print("**********")
	print(val)
	print(id)
	if(request.method == 'GET'):
		if(val=='a'):
			tbluser_list=tbluser.objects.filter(user_ID=id)
			if(len(tbluser_list)<=0):
				m="user does not exist !!!!"
				return render(request,'firstapp/failed.html',{'msg':m})
			tbluser_list=tbluser.objects.filter(user_ID=id)
			if(len(tbluser_list)<=0):
				m="Wrong Password please try again!!!!"
				return render(request,'firstapp/failed.html',{'msg':m})
			result=[]
			for i in tbluser_list:
				result.append((i.firstname,i.lastname,i.user_email_ID,i.user_password,i.user_address,i.user_mobile_number,i.user_ID,i.profilepicture))
			
			return render(request, 'firstapp/edit_user.html',{'record':result})
		elif(val=='b'):
			tbladmin_list=tbladmin.objects.filter(admin_ID=id)
			if(len(tbladmin_list)<=0):
				m="Wrong Password please try again!!!!"
				return render(request,'firstapp/failed.html',{'msg':m})
			result=[]
			for i in tbladmin_list:
				result.append((i.admin_ID,i.admin_firstname,i.admin_lastname,i.admin_emailID,i.admin_password,i.hall_name,i.hall_address,i.hall_price,i.hall_capasity,i.admin_mobile,i.image))
				
			return render(request, 'firstapp/edit_admin.html',{'record':result})
	elif(request.method == 'POST'):
		if(val=='a'):
			
			print("********************************")
			
			firstname1 = request.POST['txtfirstname']
			lastname1 = request.POST['txtlastname']
			add=request.POST['txtaddress']
			mobile1=request.POST['txtmobile']
			password1=request.POST['txtpassword']
			# uploadedfile=request.FILES["profile_image"]
			# if(uploadedfile):
			tbluser_list=tbluser.objects.filter(user_ID=id,user_password=password1).update(firstname=firstname1,lastname=lastname1,user_address=add,user_mobile_number=mobile1)
			
			result=[]
			tbluser_list=tbluser.objects.filter(user_ID=id,user_password=password1)
			if(len(tbluser_list)<=0):
				m="user does not exist !!!!"
				return render(request,'firstapp/failed.html',{'msg':m})
			tbluser_list=tbluser.objects.filter(user_ID=id,user_password=password1)
			if(len(tbluser_list)<=0):
				m="Wrong Password please try again!!!!"
				return render(request,'firstapp/failed.html',{'msg':m})
			for i in tbluser_list:
				result.append((i.firstname,i.lastname,i.user_email_ID,i.user_password,i.user_address,i.user_mobile_number,i.user_ID,i.profilepicture))
			booking_details=[]
			
			booking_details_list=tblbookings.objects.filter(booking_user_ID=tbluser_list[0])
			for j in booking_details_list:
				#  admin_ID,admin_firstname,admin_lastname,admin_emailID,hall_name,hall_add,hall_capasity,admin_mobile,hall_image,booking_total,booking_advance,booking_balance,booking_date,bookingID 
				booking_details.append((j.booking_admin_ID.admin_ID,j.booking_admin_ID.admin_firstname,j.booking_admin_ID.admin_lastname, j.booking_admin_ID.admin_emailID, j.booking_admin_ID.hall_name, j.booking_admin_ID.hall_address, j.booking_admin_ID.hall_capasity, j.booking_admin_ID.admin_mobile,j.booking_admin_ID.image,j.booking_total_amount, j.booking_advance_amount, j.bookihg_balance_amount, j.booking_dates,  j.booking_ID))
			print('#4444','booking_details',booking_details)
			
			
			m="Hello "+result[0][0]+" "+result[0][1]+"!! Your profile has been updated"
			print(m)
			# return render(request,'firstapp/user_dash.html', {"record":result,"record_cou nt":len(result),"bookings":booking_details})
			return render(request,'firstapp/user_dash.html', {"record":result,"record_count":len(result),"bookings":booking_details,'msg':m})	
			# else:
			# 	m="Wong password";
			# 	return	 render(request,'firstapp/failed.html',{'msg':m})
			# return render(request, 'firstapp/success.html',{'msg':m})
		elif(val=='b'):
			
			print("********************************")
			
			firstname1 = request.POST['txtfirstname']
			lastname1 = request.POST['txtlastname']
			# add=request.POST['txtaddress']
			mobile1=request.POST['txtmobile']
			password1=request.POST['txtpassword']
			hallname1=request.POST['txthallname']
			hallprice1=request.POST['txthallprice']

			# uploadedfile=request.FILES["hall_image"]
			print("**********")
			tbluser_list=tbladmin.objects.filter(admin_ID=id,admin_password=password1).update(admin_firstname=firstname1,admin_lastname=lastname1,hall_name=hallname1,hall_price=hallprice1,admin_mobile=mobile1)

			result=[]
			tbladmin_list=tbladmin.objects.filter(admin_ID=id,admin_password=password1)
			if(len(tbladmin_list)<=0):
				m="Wrong Password please try again!!!!"
				return render(request,'firstapp/failed.html',{'msg':m})
			result=[]
			for i in tbladmin_list:
				result.append((i.admin_ID,i.admin_firstname,i.admin_lastname,i.admin_emailID,i.admin_password,i.hall_name,i.hall_address,i.hall_price,i.hall_capasity,i.admin_mobile,i.image))
				booking_details=[]
				booking_total_amount=0
				bookihg_balance_amount=0
				booking_advance_amount=0
			booking_details_list=tblbookings.objects.filter(booking_admin_ID=tbladmin_list[0])
			for j in booking_details_list:
				booking_total_amount=booking_total_amount+j.booking_total_amount
				bookihg_balance_amount=bookihg_balance_amount+j.bookihg_balance_amount
				booking_advance_amount=booking_advance_amount+j.booking_advance_amount
				
				booking_details.append((j.booking_user_ID.firstname,j.booking_user_ID.lastname, j.booking_user_ID.user_email_ID, j.booking_user_ID.user_address, j.booking_user_ID.user_mobile_number, j.booking_user_ID.user_ID,j.booking_total_amount, j.booking_advance_amount, j.bookihg_balance_amount, j.booking_dates,  j.booking_ID))
			print('#333','booking_details',booking_details)
			total_earings_results=[(booking_total_amount,booking_advance_amount,bookihg_balance_amount)]
			# return render(request,'firstapp/admin_dash.html', {"record":result,"bookings":booking_details,'total_earings_records':total_earings_results})	
			

			
			m="Hello "+result[0][1]+" "+result[0][2]+"!! Your profile has been updated"
			print(m)
			# return render(request,'firstapp/user_dash.html', {"record":result,"record_cou nt":len(result),"bookings":booking_details})
			return render(request,'firstapp/admin_dash.html', {"record":result,"bookings":booking_details,'total_earings_records':total_earings_results,'msg':m})	
			
			m="Wong password";
			return	 render(request,'firstapp/failed.html',{'msg':m})
		

# for admin login page 
def login_admin_view(request):
	if(request.method == 'GET'):
		return render(request,'firstapp/login_admin.html')
	elif(request.method == 'POST'):
		email1 = request.POST['txtemail']
		password1 =request.POST['txtpassword']
		tbladmin_list=tbladmin.objects.filter(admin_emailID=email1,admin_password=password1)
		if(len(tbladmin_list)<=0):
			m="Wrong Password please try again!!!!"
			return render(request,'firstapp/failed.html',{'msg':m})
		result=[]
		for i in tbladmin_list:
			result.append((i.admin_ID,i.admin_firstname,i.admin_lastname,i.admin_emailID,i.admin_password,i.hall_name,i.hall_address,i.hall_price,i.hall_capasity,i.admin_mobile,i.image))
			booking_details=[]
			booking_total_amount=0
			bookihg_balance_amount=0
			booking_advance_amount=0
		booking_details_list=tblbookings.objects.filter(booking_admin_ID=tbladmin_list[0])
		for j in booking_details_list:
			booking_total_amount=booking_total_amount+j.booking_total_amount
			bookihg_balance_amount=bookihg_balance_amount+j.bookihg_balance_amount
			booking_advance_amount=booking_advance_amount+j.booking_advance_amount
			
			booking_details.append((j.booking_user_ID.firstname,j.booking_user_ID.lastname, j.booking_user_ID.user_email_ID, j.booking_user_ID.user_address, j.booking_user_ID.user_mobile_number, j.booking_user_ID.user_ID,j.booking_total_amount, j.booking_advance_amount, j.bookihg_balance_amount, j.booking_dates,  j.booking_ID))
		print('#333','booking_details',booking_details)
		total_earings_results=[(booking_total_amount,booking_advance_amount,bookihg_balance_amount)]
		return render(request,'firstapp/admin_dash.html', {"record":result,"bookings":booking_details,'total_earings_records':total_earings_results})	
		

# for admin dashboard page

def admin_dash_view(request):
	if request.method =='GET':
		return render(request,'admin_dash.html',{"record":result});
	elif request.method =='POST':
		return render(request,'firstapp/admin_dash.html',{"record":result})
def search_view(request):
	if request.method == 'GET':
		tbladmin_list=tbladmin.objects.all()
		result=[]
		for i in tbladmin_list:
			print('##########')
			result.append((i.admin_ID,i.admin_firstname,i.admin_lastname,i.admin_emailID,i.admin_password,i.hall_name,i.hall_address,i.hall_price,i.hall_capasity,i.admin_mobile,i.image))	
		print('*******************',result)
		
		return render(request,'firstapp/search.html',{"records":result})
	elif request== 'POST' :
		print("**********")
		sel=request.POST['txtopt']
		print("**********")
		return render(request,'firstapp/search.html')
def sort_view(request,id):
	if(request.method == 'GET'):
		print("********************************")
		print(id)
		if(id=='a'):
			column='hall_price'
		elif(id=='b'):
			column='hall_capasity'
		else:
			column='hall_name'
		
		tbladmin_list=tbladmin_list=tbladmin.objects.order_by(column)
		result=[]
		for i in tbladmin_list:
			result.append((i.admin_ID,i.admin_firstname,i.admin_lastname,i.admin_emailID,i.admin_password,i.hall_name,i.hall_address,i.hall_price,i.hall_capasity,i.admin_mobile,i.image))
		return render(request,'firstapp/search.html',{"records":result})
def info_view(request,id):
	if(request.method == 'GET'):
		print(id)
		column='hall_name'
		tbladmin_list=tbladmin_list=tbladmin.objects.filter(admin_ID=id)
		result=[]
		for i in tbladmin_list:
			result.append((i.admin_ID,i.admin_firstname,i.admin_lastname,i.admin_emailID,i.admin_password,i.hall_name,i.hall_address,i.hall_price,i.hall_capasity,i.admin_mobile,i.image))
		
		return render(request,'firstapp/info.html',{"records":result})
	elif request.method == "POST":
		user_email_ID1=request.POST['txtuser_email']
		user_password1=request.POST['txtuser_password']
		user_bookingd_date=request.POST['txt_user_date']
		user_advance_ammount=request.POST['txt_user_amount']
		tbladmin_list=tbladmin.objects.filter(admin_ID=id)
		result=[]
		tbluser_list=tbluser.objects.filter(user_email_ID=user_email_ID1)
		if(len(tbluser_list)<=0):
			m="user does not exist !!!!"
			return render(request,'firstapp/failed.html',{'msg':m})
		tbluser_list=tbluser.objects.filter(user_email_ID=user_email_ID1,user_password=user_password1)
		if(len(tbluser_list)<=0):
			m="Wrong Password please try again!!!!"
			return render(request,'firstapp/failed.html',{'msg':m})
		for i in tbluser_list:
			result.append((i.firstname,i.lastname,i.user_email_ID,i.user_password,i.user_address,i.user_mobile_number,i.user_ID,i.profilepicture))
		# booking_details=[]
		print(user_bookingd_date)
		booking_details_list=tblbookings.objects.filter(booking_user_ID=tbluser_list[0],booking_dates=user_bookingd_date)
		if(len(booking_details_list)>0):
			m="Sorry , Hall is booked already !!!!"
			return render(request,'firstapp/failed.html',{'msg':m})
		
		format_data = "%d%m%y%H%M%S%f"
		dt_ts =datetime.datetime.now().strftime(format_data)
		booking=tblbookings(booking_ID=dt_ts,booking_user_ID=tbluser_list[0],booking_admin_ID=tbladmin_list[0],booking_total_amount=int(tbladmin_list[0].hall_price),booking_advance_amount=user_advance_ammount,bookihg_balance_amount=(int(tbladmin_list[0].hall_price)-int(user_advance_ammount)),booking_dates=user_bookingd_date)
		booking.save()
		# result store user records
		
		booking_details=[]
		booking_details_list=tblbookings.objects.filter(booking_user_ID=tbluser_list[0])
		for j in booking_details_list:
			#  admin_ID,admin_firstname,admin_lastname,admin_emailID,hall_name,hall_add,hall_capasity,admin_mobile,hall_image,booking_total,booking_advance,booking_balance,booking_date,bookingID 
			booking_details.append((j.booking_admin_ID.admin_ID,j.booking_admin_ID.admin_firstname,j.booking_admin_ID.admin_lastname, j.booking_admin_ID.admin_emailID, j.booking_admin_ID.hall_name, j.booking_admin_ID.hall_address, j.booking_admin_ID.hall_capasity, j.booking_admin_ID.admin_mobile,j.booking_admin_ID.image,j.booking_total_amount, j.booking_advance_amount, j.bookihg_balance_amount, j.booking_dates,  j.booking_ID))
		print('#4444','booking_details',booking_details)
		return render(request,'firstapp/user_dash.html', {"record":result,"bookings":booking_details})
		

	
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
		uploadedfile=request.FILES["profile_image"]
		format_data = "%d%m%y%H%M%S%f"
		dt_ts =datetime.datetime.now().strftime(format_data)
		user=tbluser(user_ID=dt_ts,firstname=firstname1,lastname=lastname1,user_email_ID=email1,user_password=password1,user_address=add,user_mobile_number=mobile1,profilepicture=uploadedfile)
		user.save()
		return redirect('/login-user/')
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
		format_data = "%d%m%y%H%M%S%f"
		dt_ts =datetime.datetime.now().strftime(format_data)
		
		admin=tbladmin(admin_ID=dt_ts,admin_firstname=firstname1,admin_lastname=lastname1,admin_emailID=email1,admin_password=password1,hall_name=hallname1,hall_address=halladd,hall_price=hallprice1,hall_capasity=hallcapasity1,admin_mobile=mobile1,image=uploadedfile)
		admin.save()
		
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