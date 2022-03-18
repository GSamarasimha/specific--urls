from django.urls import path
from app2.views import a2_queen
app_name='app2'
urlpatterns=[path('a2_queen/',a2_queen,name='a2_queen'),
]