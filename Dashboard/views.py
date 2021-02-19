from django.shortcuts import render, redirect


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "Dashboard/dashboard.html")
    return redirect('/')


def edit_details(request):
    if request.user.is_authenticated:
        return render(request, "Dashboard/details.html")
    return redirect('/')


def edit_designation(request):
    if request.user.is_authenticated:
        return render(request, "Dashboard/designation.html")
    return redirect('/')


def edit_activity(request):
    if request.user.is_authenticated:
        return render(request, "Dashboard/activity.html")
    return redirect('/')
