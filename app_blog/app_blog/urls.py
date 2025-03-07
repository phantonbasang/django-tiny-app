# project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),  # URL của trang quản trị
    path('', redirect_to_login),      # URL gốc định tuyến đến trang đăng nhập
    path('app/', include('todo.urls')),  # Định tuyến URL ứng dụng của bạn
]
