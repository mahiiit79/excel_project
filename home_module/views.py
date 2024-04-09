import xlwt
from django.http import HttpResponse
from django.views.generic import ListView
import datetime
from home_module.models import ProductTable


class HomePageView(ListView):
    template_name = 'home_module/index.html'
    model = ProductTable
    context_object_name = 'products'


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['content-Disposition'] = 'attachment;filename=phones' + str(datetime.datetime.now()) + '.xls'
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('product')
    columns = ['نام محصول','قیمت','تعداد','موجودی']
    rownumber = 0
    for col in range(len(columns)):
        worksheet.write(rownumber, col, columns[col])

    products = ProductTable.objects.all().values_list('title','price','count','is_active')

    for p in products:
        rownumber+=1
        for col in range(len(p)):
            worksheet.write(rownumber,col,p[col])
    workbook.save(response)
    return response
