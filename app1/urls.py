from django.urls import path
from app1.views import a1_king
app_name='app1'
urlpatterns=[path('a1_king/',a1_king,name='a1_king'),
]