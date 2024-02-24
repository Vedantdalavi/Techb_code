from django.shortcuts import render,redirect
from .forms import List,ListForm
# Create your views here.
def list_view(request):
    form = ListForm()
    template_name = 'app1/team.html'
    if request.method =='POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('show_url')
    context = {'form':form}
    return render(request,template_name,context)

def show_view(request):
    obj = List.objects.all()
    template_name = 'app1/show.html'
    context = {'data':obj}
    return render(request, template_name, context)

def update_view(request,pk):
    obj = List.objects.get(rank=pk)
    form = ListForm(instance=obj)
    if request.method == 'POST':
        form = ListForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'app1/team.html'
    context = {'form':form}
    return render(request, template_name, context)

def delete_view(request,pk):
    template_name = 'app1/confirmation.html'
    if request.method == 'POST':
        obj = List.objects.get(rank=pk)
        obj.delete()
        return redirect('show_url')
    context = {}
    return render(request, template_name, context)