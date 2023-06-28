# custom created urls by akshay date 28/11/2020

from django.urls import path
from firstapp import views

urlpatterns = [
	path('home/',views.home_view),
	path('login-user/',views.login_user_view),
	path('user-dashboard/',views.user_dash_view),
	path('login-admin/',views.login_admin_view),
	path('admin-dashboard/',views.admin_dash_view),
	path('user-registration/',views.user_registration_view),
	path('admin-registration/',views.admin_registration_view),
	path('Search/',views.search_view),
	# path('delete/<str:val>/<int:id>/',views.delete_view,name="Delete"),
	path('edit/<str:val>/<str:id>/',views.edit_view,name="Edit"),
	path('info/<int:id>/',views.info_view,name="Info"),
	path('sort_view/<str:id>/',views.sort_view,name="sort_view"),
	path('about/',views.about_view),
	path('categoryname/',views.categoryname_view),
	path('category/<str:opt>/',views.category_preview_view,name="category"),
	# path('upload/',views.upload_view),
	# path('prev/',views.prev_view),
]