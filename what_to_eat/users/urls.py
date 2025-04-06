from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', views.user_logout, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),word_change.html'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('pasword_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('pasword_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.user_register, name='register'),
    path('profile/<int:pk>/', include([
        path('', views.user_profile, name='profile'),
        path('edit/', views.user_edit, name='profile_edit'),
        path("delete/", views.user_delete, name='profile_delete'),
    ])),
]   
# TODO: change the rest of the I build views for testing purposes
