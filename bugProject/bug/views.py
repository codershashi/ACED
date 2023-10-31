from django.shortcuts import render, redirect
from .models import bugModel

# Create your views here.


def register_bug(request):
    if request.method == 'POST':
        description = request.POST['description']
        bug_type = request.POST['bug_type']
        report_date = request.POST['report_date']
        status = request.POST['status']
        bugModel.objects.create(description=description, bug_type=bug_type, report_date=report_date, status=status)
        return redirect('list_bugs')
    return render(request, 'bug/register_bug.html')

def view_bug(request, bug_id):
    bug = bugModel.objects.get(id=bug_id)
    return render(request, 'bug/view_bug.html', {'bug': bug})

def list_bugs(request):
    bugs = bugModel.objects.all()
    return render(request, 'bug/list_bugs.html', {'bugs': bugs})
