from django.urls import path
from . import views

app_name = 'stock'
urlpatterns = [
    path('', views.index, name='index'),
    path('stock_list/', views.StockListView.as_view(), name='stock_list'),
    path('create_item/', views.create_item, name='create_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('update_item/<int:item_id>/', views.update_item, name='update_item'),
    path('detail_item/<int:pk>', views.StockDetailView.as_view(), name='detail_item'),
]