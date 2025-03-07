from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import ResetPasswordForm
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.middleware.csrf import get_token

# Định nghĩa inline cho UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'

# Tùy chỉnh UserAdmin để thêm inline
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'is_staff', 'is_blocked')
    list_filter = ('is_staff', 'userprofile__is_blocked')

    def is_blocked(self, obj):
        return obj.userprofile.is_blocked
    is_blocked.boolean = True

    actions = ['block_users', 'unblock_users']

    def block_users(self, request, queryset):
        for user in queryset:
            user.userprofile.is_blocked = True
            user.userprofile.save()
        messages.success(request, 'Đã khóa tài khoản người dùng thành công.')

    def unblock_users(self, request, queryset):
        for user in queryset:
            user.userprofile.is_blocked = False
            user.userprofile.save()
        messages.success(request, 'Đã mở khóa tài khoản người dùng thành công.')

    block_users.short_description = "Khóa tài khoản người dùng"
    unblock_users.short_description = "Mở khóa tài khoản người dùng"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<id>/reset_password/', self.admin_site.admin_view(self.reset_password), name='user_reset_password'),
        ]
        return custom_urls + urls

    @csrf_protect
    def reset_password(self, request, id):
        user = User.objects.get(pk=id)
        if request.method == 'POST':
            form = ResetPasswordForm(request.POST, instance=user)
            if form.is_valid():
                user.set_password(form.cleaned_data['new_password'])
                user.save()
                messages.success(request, 'Mật khẩu đã được reset thành công.')
                return redirect('..')
        else:
            form = ResetPasswordForm(instance=user)
        return render(request, 'admin/reset_password.html', {'form': form, 'user': user, 'csrf_token': get_token(request)})

# Hủy đăng ký User mặc định và đăng ký CustomUserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)