from django.shortcuts import redirect

def redirect_from_home(request):
    return redirect('admin:index')