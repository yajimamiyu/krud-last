from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),

    path(
        'home/',
        views.home,
        name='home'
    ),

    path(
        'create/',
        views.create_application,
        name='create_application'
    ),

    path(
        'list/',
        views.application_list,
        name='application_list'
    ),

    path(
        'approve/<int:id>/',
        views.approve_application,
        name='approve_application'
    ),

    path(
        'reject/<int:id>/',
        views.reject_application,
        name='reject_application'
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "my-list/",
        views.my_application_list,
        name="my_application_list"
    ),

    path(
        'pending-list/',
        views.pending_list,
        name='pending_list'
    ),

    path(
        'detail/<int:id>/',
        views.application_detail,
        name='application_detail'
    ),
]