from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Service, ServiceRequest
from .forms import ServiceForm, ServiceRequestForm

@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

@login_required
def service_detail(request, service_id):
    services = Service.objects.all()
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.service = service
            service_request.status = 'pending'
            service_request.save()
            return redirect('service:my_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'services/service_detail.html', {'service': service, 'services': services, 'form': form})

@login_required
def service_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        icon = request.POST['icon']
    
        service = Service.objects.create(title=title, description=description, image=image, icon=icon)
        service.save()
        
        return redirect('service:service_list')
    else:
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form': form})

@login_required
def service_update(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service:service_detail', service_id=service_id)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/service_form.html', {'form': form, 'service': service})

@login_required
def service_delete(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('service:service_list')
    return render(request, 'services/service_delete.html', {'service': service})

@login_required
def service_request(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.service = service
            service_request.status = 'pending'
            service_request.save()
            return redirect('service:my_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'services/service_request_form.html', {'form': form, 'service': service})

@login_required
def my_requests(request):
    service_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'services/my_requests.html', {'service_requests': service_requests})

@login_required
def manager_requests(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'services/manager_requests.html', {'service_requests': service_requests})

@login_required
def update_service_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        service_request.status = request.POST['status']
        service_request.save()
        return redirect('service:manager_requests')
    return render(request, 'services/update_service_request.html', {'service_request': service_request})