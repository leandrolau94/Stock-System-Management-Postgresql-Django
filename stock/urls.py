from django.urls import path
from . import views

app_name = 'stock'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('stock_list/', views.StockListView.as_view(), name='stock_list'),
    path('create_item/', views.create_item, name='create_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('update_item/<int:item_id>/', views.update_item, name='update_item'),
    path('increase_quantity/<int:item_id>', views.increase_item_quantity, name='increase_item_quantity'),
    path('decrease_quantity/<int:item_id>', views.decrease_item_quantity, name='decrease_item_quantity'),
    path('detail_item/<int:pk>', views.StockDetailView.as_view(), name='detail_item'),
    path('stock_sell_list/', views.StockSellListView.as_view(), name='stock_sell_list'),
    path('stock_sell_analysis/<int:sold_id>', views.stock_sell_analysis, name='stock_sell_analysis'),
    path('create_sell_report/', views.create_sell_report, name='create_sell_report'),
]