from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.


data = {
    "programlama":"programalama kategorisine ait kurslar",
    "web":"web kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
}
def kurslar(request):
    list_items= ""
    category_list = list(data.keys())

    for category in category_list:
        redirect_url = reverse('courses_by_category',args =[category])
        list_items +=  f"<li><a href = '{redirect_url}'></a></li>"
    
    html = f"<h1>Kurs Listesi</h1> <br> <ul>{list_items}</ul>"
    
    return HttpResponse('')

def details(request,kurs_adi):
    return HttpResponse(f'{kurs_adi} details')
def list(request):
    return HttpResponse('liste')

def getCoursesByCategory(req,category_name):
    try:
         category_text = data[category_name]

         return HttpResponse(f'{category_name} göre list')
    except:
        return HttpResponseNotFound("<h1>Yanlış</h1>")
    
def getCoursesByCategoryId(req,category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound("Yanlış")
    redirect_text = category_list[category_id - 1]
    return redirect('/kurs/kategori/' + redirect_text)