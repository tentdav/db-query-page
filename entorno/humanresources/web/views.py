from django.shortcuts import render, redirect
from .models import Person, Employee
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#decorador para limitar el acceso a la view para lo que no inicien sesion
@login_required
def first_view(request):
    person = Person.objects.all()
    employee = Employee.objects.all()

    businessentityid = request.GET.get('businessentityid')
    jobtitle = request.GET.get('jobtitle')
    gender = request.GET.get('gender')

    # Aplica filtros solo si los campos no están vacíos
    if businessentityid:
        person = person.filter(businessentityid=businessentityid)

    if jobtitle:
        person = person.filter(employee__jobtitle=jobtitle)

    if gender:
        person = person.filter(employee__gender=gender)

    # Filtra combinación de campos (uso de Q)
    if businessentityid and jobtitle and gender:
        person = person.filter(
            Q(businessentityid=businessentityid) &
            Q(employee__jobtitle=jobtitle) &
            Q(employee__gender=gender)
        )

    elif businessentityid and jobtitle:
        person = person.filter(
            Q(businessentityid=businessentityid) &
            Q(employee__jobtitle=jobtitle)
        )

    elif businessentityid and gender:
        person = person.filter(
            Q(businessentityid=businessentityid) &
            Q(employee__gender=gender)
        )

    elif jobtitle and gender:
        person = person.filter(
            Q(employee__jobtitle=jobtitle) &
            Q(employee__gender=gender)
        )

    return render(request, 'index.html', {'person': person})






#View para ejecutar log in
def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('prueba')  # Redirige a la tabla después del login exitoso
        else:
            messages.error(request, 'Credenciales inválidas. Intente nuevamente.')
    return render(request, 'login.html')



#Funcion para ejecutar un log out
def view_logout(request):
    logout(request)
    return redirect('logout')

    