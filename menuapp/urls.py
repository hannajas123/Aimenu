from django.urls import path

from menuapp import views

urlpatterns = [
    path('login/', views.login),
    path('login_post/', views.login_post),
    path('logout/',views.logout),
#################################ADMIN#################################
    path('Admin_home/', views.Admin_home),

    path('Admin_change_pswd/', views.Admin_change_pswd),
    path('Admin_change_pswd_post/', views.Admin_change_pswd_post),


    path('Add_Staff/', views.Add_Staff),
    path('Add_staff_post/', views.Add_staff_post),
    path('View_Staff/', views.View_Staff),
    path('Search_Staff_post/', views.Search_Staff_post),
    path('Edit_Staff/<did>', views.Edit_Staff),
    path('Edit_staff_post/', views.Edit_staff_post),
    path('Delete_staff_post/<did>', views.Delete_staff_post),

    path('Add_Menu/', views.Add_Menu),
    path('Add_Menu_post/', views.Add_Menu_post),
    path('View_Menu/', views.View_Menu),
    path('Search_Menu_post/', views.Search_Menu_post),
    path('Edit_Menu/<did>', views.Edit_Menu),
    path('Edit_Menu_post/', views.Edit_Menu_post),
    path('Delete_Menu_post/<did>', views.Delete_Menu_post),


    path('Add_Tdyscpcl/', views.Add_Tdyscpcl),
    path('Add_Tdyscpcl_post/', views.Add_Tdyscpcl_post),
    path('View_Tdyscpcl/', views.View_Tdyscpcl),
    path('Search_Tdyscpcl_post/', views.Search_Tdyscpcl_post),
    path('Edit_Tdyscpcl/<did>', views.Edit_Tdyscpcl),
    path('Edit_Tdyscpcl_post/', views.Edit_Tdyscpcl_post),
    path('Delete_Tdyscpcl_post/<did>', views.Delete_Tdyscpcl_post),

    path('Add_Table/', views.Add_Table),
    path('Add_Table_post/', views.Add_Table_post),
    path('View_Table/', views.View_Table),
    path('Search_Table_post/', views.Search_Table_post),
    path('Edit_Table/<did>', views.Edit_Table),
    path('Edit_Table_post/', views.Edit_Table_post),
    path('Delete_Table_post/<did>', views.Delete_Table_post),

    path('View_customers/', views.View_customers),
    path('Search_customer/', views.Search_customer),


    path('View_complaints/', views.View_complaints),
    path('Search_complaints/', views.Search_complaints),
    path('Send_Reply/<did>', views.Send_Reply),
    path('Send_reply_post/', views.Send_reply_post),

    path('View_Reports/', views.View_Reports),
    path('Search_Reports/', views.Search_Reports),


    path('View_Orders/', views.View_Orders),
    path('Search_Orders/', views.Search_Orders),

##############################Kitchen#################################
    path('Kitchen_home/', views.Kitchen_home),

    path('Kitchen_change_pswd/', views.Kitchen_change_pswd),
    path('Kitchen_change_pswd_post/', views.Kitchen_change_pswd_post),

    path('kitchen_View_New_Orders_nd_update_status/', views.kitchen_View_New_Orders_nd_update_status),
    path('kitchen_Update_status_Orders/<did>', views.kitchen_Update_status_Orders),
    path('kitchen_Search_New_Orders_nd_update_status/', views.kitchen_Search_New_Orders_nd_update_status),

    path('Add_timeDelay_details/', views.Add_timeDelay_details),
    path('time_delay/<did>',views.time_delay),
    path('Add_timeDelay_details_post/', views.Add_timeDelay_details_post),


    path('View_Reviews/', views.View_Reviews),
    path('Search_Reviews/', views.Search_Reviews),

###################################ServiceStation########################
    path('Servicestn_home/', views.Servicestn_home),

    path('Service_station_change_pswd/', views.Service_station_change_pswd),
    path('Service_station_change_pswd_post/', views.Service_station_change_pswd_post),


    path('View_Completed_Orders/', views.View_Completed_Orders),
    path('Search_Completed_Orders/', views.Search_Completed_Orders),


    path('Allocate_to_serving_staff/', views.Allocate_to_serving_staff),
    path('Allocate_to_serving_staff_post/<did>', views.Allocate_to_serving_staff_post),
    path('SearchStaff/',views.Search_Allocted_Staff_post),

    path('Service_update_Order_status/', views.Service_update_Order_status),
    path('Service_update_Order_status_post/<did>', views.Service_update_Order_status_post),
    path('Service_Search_Oder_complete/',views.Service_Search_Oder_complete),

####################################Cashier##############################
    path('Cashier_home/', views.Cashier_home),

    path('Cashier_change_pswd/', views.Cashier_change_pswd),
    path('Cashier_change_pswd_post/', views.Cashier_change_pswd_post),

    path('View_bills/', views.View_bills),
    path('Search_View_bills/', views.Search_View_bills),

    path('View_pament_reports/', views.View_pament_reports),
    path('Search_View_pament_reports/', views.Search_View_pament_reports),





##############################################Customer.................#############################################

    path('customerlogin/',views.customerlogin_post),
    path('Cust_Changepassword/',views.Cust_Changepassword),
    path('Cust_complaint/',views.Cust_complaint_post),
    path('view_reply/',views.view_reply),
    path('Cust_Register/',views.Cust_Register),
    path('Cust_View_Menu/',views.Cust_View_Menu),
    path('Cust_View_todays_special/',views.Cust_View_todays_special),
    path('Cust_View_reviews/',views.Cust_View_reviews),
    path('Cust_add_tocart/',views.Cust_add_tocart),
    path('AddCart_post/',views.AddCart_post),
    path('Cust_View_order_status/',views.Cust_View_order_status),
    path('Cust_View_bill/',views.Cust_View_bill),
    path('Cust_Payment/',views.Cust_Payment),
    path('Cust_Send_reviews/',views.Cust_Send_reviews),
    path('Cust_View_cart/',views.Cust_View_cart),

]