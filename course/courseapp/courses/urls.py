

from django.urls import path

from . import views


urlpatterns = [
    # path('',views.index,'index.html'),
    path('',views.kurslar),
    path('list',views.list),
    path('details',views.details),
    path('<kurs_adi>',views.details),
    path('kategori/<int:category_id>',views.getCoursesByCategoryId),
    path('kategori/<str:category_name>',views.getCoursesByCategory),

    
]


# <category> değişken pathler için

# views.home views.py içerisinde tanımlanan viewsleri uygular.
