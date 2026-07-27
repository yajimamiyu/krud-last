from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ApplicationForm
from .models import Application
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator

def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('/admin/')
            else:
                return redirect('home')

    return render(
        request,
        "registration/login.html"
    )

@login_required
def application_list(request):

    if request.user.is_staff:
        applications = Application.objects.order_by("-created_at")
    else:
        applications = Application.objects.filter(
            user=request.user
        ).order_by("-created_at")


    paginator = Paginator(
        applications,
        10
    )

    page_number = request.GET.get('page')

    applications = paginator.get_page(page_number)


    return render(
        request,
        'application/list.html',
        {
            'applications': applications
        }
    )

def home(request):
    return render(request, 'application/home.html')

def login_redirect(request):
    if request.user.is_staff:
        return redirect('/admin/')
    else:
        return redirect('home')

@login_required
def create_application(request):

    if request.method == 'POST':

        form = ApplicationForm(request.POST)

        if form.is_valid():

            application = form.save(commit=False)

            application.user = request.user

            application.save()

            messages.success(
                request,
                "申請が送信されました"
            )

            return redirect('home')

    else:
        form = ApplicationForm()


    return render(
        request,
        'application/create.html',
        {'form': form}
    )

from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def approve_application(request, id):

    application = get_object_or_404(
        Application,
        id=id
    )

    application.status = "approved"
    application.save()

    messages.success(
        request,
        "申請を承認しました"
    )

    if request.GET.get("next") == "list":
        return redirect('application_list')

    return redirect('pending_list')


@staff_member_required
def reject_application(request, id):

    application = get_object_or_404(
        Application,
        id=id
    )

    application.status = "rejected"
    application.save()

    messages.error(
        request,
        "申請を却下しました"
    )

    if request.GET.get("next") == "list":
        return redirect('application_list')

    return redirect('pending_list')

@login_required
def application_detail(request, id):

    application = get_object_or_404(
        Application,
        id=id
    )

    return render(
        request,
        "application/detail.html",
        {
            "application": application
        }
    )

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def dashboard(request):

    total = Application.objects.count()

    pending = Application.objects.filter(
        status="pending"
    ).count()

    approved = Application.objects.filter(
        status="approved"
    ).count()

    rejected = Application.objects.filter(
        status="rejected"
    ).count()

    recent = Application.objects.order_by("-created_at")[:5]

    return render(
        request,
        "application/dashboard.html",
        {
            "total": total,
            "pending": pending,
            "approved": approved,
            "rejected": rejected,
            "recent": recent,
        }
    )

@login_required
def my_application_list(request):

    applications = Application.objects.filter(
        user=request.user
    ).order_by("-created_at")

    paginator = Paginator(
        applications,
        10
    )

    page_number = request.GET.get('page')

    applications = paginator.get_page(page_number)

    return render(
        request,
        "application/my_list.html",
        {
            "applications": applications
        }
    )

@staff_member_required
def pending_list(request):

    applications = Application.objects.filter(
        status="pending"
    ).order_by("-created_at")


    paginator = Paginator(
        applications,
        10
    )

    page_number = request.GET.get('page')

    applications = paginator.get_page(page_number)


    return render(
        request,
        "application/pending_list.html",
        {
            "applications": applications
        }
    )


