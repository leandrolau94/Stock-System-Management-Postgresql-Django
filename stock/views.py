from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Item

# Create your views here.
def index(request):
    return render(request, 'stock/index.html')

def create_item(request):
    item_name = request.POST["item_name"]
    item_category = request.POST["item_category"]
    item_quantity = request.POST["item_quantity"]
    item_acquisition_price = request.POST["item_acquisition_price"]
    item_sell_price = request.POST["item_sell_price"]
    item_supplier = request.POST["item_supplier"]
    new_item = Item(
        name=item_name,
        category=item_category,
        quantity=item_quantity,
        acquisition_price=item_acquisition_price,
        sell_price=item_sell_price,
        supplier=item_supplier,
        created_at=timezone.now(),
        modified_at=timezone.now(),
    )
    new_item.save()
    return redirect(reverse('stock:index'))

def delete_item(request, item_id):
    del_item = Item.objects.get(id=item_id)
    del_item.delete()
    return redirect(reverse('stock:stock_list'))

def update_item(request, item_id):
    update_name = request.POST["update_name"]
    update_category = request.POST["update_category"]
    update_quantity = request.POST["update_quantity"]
    update_acquisition_price = request.POST["update_acquisition_price"]
    update_sell_price = request.POST["update_sell_price"]
    update_supplier = request.POST["update_supplier"]
    updated_item = Item.objects.get(id=item_id)
    updated_item.name = update_name
    updated_item.category = update_category
    updated_item.quantity = update_quantity
    updated_item.acquisition_price = update_acquisition_price
    updated_item.sell_price = update_sell_price
    updated_item.supplier = update_supplier
    updated_item.modified_at = timezone.now()
    updated_item.save()
    return redirect(reverse('stock:stock_list'))

def increase_item_quantity(request, item_id):
    increase_quantity = request.POST['increase_quantity']
    increase_item = Item.objects.get(id=item_id)
    increase_item.quantity += int(increase_quantity)
    increase_item.modified_at = timezone.now()
    increase_item.save()
    return redirect(reverse('stock:stock_list'))

def decrease_item_quantity(request, item_id):
    decrease_quantity = request.POST['decrease_quantity']
    increase_item = Item.objects.get(id=item_id)
    increase_item.quantity -= int(decrease_quantity)
    increase_item.modified_at = timezone.now()
    increase_item.save()
    return redirect(reverse('stock:stock_list'))

class StockDetailView(generic.DetailView):
    model = Item
    template_name = 'stock/stock_detail.html'

class StockListView(generic.ListView):
    template_name = 'stock/stock_list.html'
    context_object_name = "items"

    def get_queryset(self):
        return Item.objects.all().order_by('id')