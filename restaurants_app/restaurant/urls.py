from django.urls import path

from restaurant import views


urlpatterns = [
    path('food-types/', views.FoodTypeList.as_view()),
    path('food-types/<int:pk>', views.FoodTypeDetail.as_view()),
    path('pay-types/', views.PayTypeList.as_view()),
    path('pay-types/<int:pk>', views.PayTypeDetail.as_view()),
    path('restaurants/', views.RestaurantList.as_view()),
    path('pay-days/', views.PayDayList.as_view()),
    path('pay-days/<int:pk>', views.PayDayDetail.as_view()),
    path('pay-monthly/',
         views.PayMonthly.as_view({'post': 'pay_monthly', 'get': 'payments'})),
    path('branches', views.BranchListView.as_view()),
]
