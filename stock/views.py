from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Item
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.http import FileResponse
from reportlab.pdfgen import canvas
import datetime
import csv
import io

# Create your views here.
class Index(generic.TemplateView):
    template_name = 'stock/index.html'

class StockDetailView(generic.DetailView):
    model = Item
    template_name = 'stock/stock_detail.html'

class StockListView(generic.ListView):
    template_name = 'stock/stock_list.html'
    context_object_name = "items"

    def get_queryset(self):
        return Item.objects.all().order_by('id')

class StockSellListView(generic.ListView):
    template_name = 'stock/stock_sell_list.html'
    context_object_name = 'sell_item'

    def get_queryset(self):
        return Item.objects.all().order_by('id')

def stock_sell_analysis(request, sold_id):
    sold = request.POST["sold"]
    item_sold = Item.objects.get(id=sold_id)
    item_sold.sold_quantity = sold
    item_sold.save()
    return redirect(reverse('stock:stock_sell_list'))

def create_sell_report(request):
    option_choice = request.POST.getlist("inlineRadioOptions")
    if option_choice[0] == 'csv':
        today = datetime.datetime.today().date()
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": f'attachment; filename="Seal-Inform-{today}.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(["Daily Sales Inform", f"Date: {today}"])
        writer.writerow([
            "Name", "Category", "Quantity (Sold)", "Acquisition Price", "Sell Price",
            "On Discount", "Discount Percentage", "Supplier", "Arrival Date", "Latest Modified Date",
        ])
        for item in Item.objects.all():
            writer.writerow([
                item.name,
                item.category,
                f"{item.quantity} ({item.sold_quantity})",
                item.acquisition_price,
                item.sell_price,
                item.discount,
                item.discount_percentage,
                item.supplier,
                item.created_at,
                item.modified_at,
            ])
        return response
    elif option_choice[0] == 'pdf':
        # Create a file-like buffer to receive PDF data.
        buffer = io.BytesIO()
        # Create the PDF object, using the buffer as its "file."
        p = canvas.Canvas(buffer)
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        p.drawString(10, 800, f"Name | Category | Quantity(Sold) | Acquisition Price | Sell Price | On Discount | Discount Percentage | Supplier | Arrival Date | Latest Modified Date")
        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()
        # FileResponse sets the Content-Disposition header so that browsers
        # present the option to save the file.
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename="hello.pdf")
    else:
        return redirect(reverse('stock:stock_list'))

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