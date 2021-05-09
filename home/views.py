from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.conf import settings

from django.core.mail import EmailMessage 
from django.http import HttpResponseRedirect 
from django.shortcuts import render
from django.core.mail  import EmailMultiAlternatives
from django.core.mail import send_mail 
from django.conf  import settings

#model
from home.models import Client, Gruaduated, Instructor, Reviews

def save_data_msg(request, data):
    mensaje=request.POST["Message"]
    iid=data['idInst']
    sid=data['idEgres'] #mo es una id, es el objeto graduado.

    review=Reviews(menssage=mensaje,graduado=sid,id_instructor=iid)
    review.save()

def save_data_client(request, data) :
    name = data['name']
    last_name = data['lastName']
    phone = data['phone']
    email = data['email']
    sex = data['sex']
    type_document = data['typeDocument']
    number_document = data['numberDocument']
    city = request.POST['city']
    addres = request.POST['addres']
    user_client = request.POST['userClient']
    pass_client = request.POST['passClient']

    #acá guardamos en la base de datos
    client = Client(name=name,last_name=last_name, phone=phone, email_adrres=email, sex=sex, 
                    document_type=type_document, number_document=number_document, city=city,
                    addres=addres, user_client=user_client,  password_client=pass_client
                    )

    client.save()


def save_data_graduated(request, data) :
    name = data['name']
    last_name = data['lastName']
    phone = data['phone']
    email = data['email']
    sex = data['sex']
    type_document = data['typeDocument']
    number_document = data['numberDocument']
    city = request.POST['city']
    user_graduated = request.POST['userGraduated']
    pass_graduated = request.POST['passwordGraduated']
    addres = request.POST['addres']
    academic_traignin = request.POST['academicTraining']
    name_program = request.POST['nameProgram']
    experencie = request.POST['experiencie']
    time_enterprise = request.POST['timeEnterprise']
    name_enterprise = request.POST['nameEnterprise']
    addres_enterprise = request.POST['addresEnterprise']
    position_enterprise = request.POST['position']
    
    id = int( request.POST['idInstructor'] )

    #acá guardamos en la base de datos
    gruaduated = Gruaduated(name=name, last_name=last_name,sex=sex,phone=phone,
                            document_type=type_document, number_document=number_document,
                            email_adrres=email, city=city, addres=addres, addres_enterprise=addres_enterprise,
                            name_enterprise=name_enterprise, position=position_enterprise,
                            experencie=experencie, user_graduated=user_graduated, password_graduated=pass_graduated,
                            program_name=name_program, academic_training=academic_traignin,
                            id_instructor=id)
    

    gruaduated.save()


def save_data_instructor(request, data) :
    name = data['name']
    last_name = data['lastName']
    phone = data['phone']
    email = data['email']
    sex = data['sex']
    type_document = data['typeDocument']
    number_document = data['numberDocument']
    city = request.POST['city']
    user_instructor = request.POST['userInstructor']
    pass_instructor = request.POST['passInstructor']

    #acá guardamos en la base de datos
    instructor = Instructor(name=name,last_name=last_name, phone=phone, email_adrres=email, sex=sex, 
                    document_type=type_document, number_document=number_document, city=city,
                    user_instructor=user_instructor,  password_instructor=pass_instructor
                    )

    instructor.save()


@csrf_exempt #protejemos de los ataques
def register(request) :

    if request.method == 'POST' :
        #valores globales que se repiten
        name = request.POST['name']
        last_name = request.POST['lastName']
        phone = request.POST['phone']
        email = request.POST['email']
        sex = request.POST['sex']
        type_document = request.POST['typeDocument']
        number_document = request.POST['numberDocument']

        data = {
            'name': name,
            'lastName': last_name,
            'phone': phone,
            'email': email,
            'sex': sex,
            'typeDocument': type_document,
            'numberDocument' : number_document
        }

        #validamos si existen las llaves para poder guardar en la BD
        if 'client' in request.POST :
            save_data_client(request, data)
            return redirect('/login/')

        if 'graduated' in request.POST :
            save_data_graduated(request, data)
            return redirect('/login/')
        
        if 'instructor' in request.POST :
            save_data_instructor(request, data)
            return redirect('/login/')
            

    return render(request, 'home/register.html')

#vistas del cliente
@csrf_exempt 
def home_client(request, id) :

    if request.method == 'GET' :

        #obtenemos los datos del cliente por su id
        user =  Client.objects.get(id_client=id)

        context = {
            'name': user.name,
            'last_name': user.last_name,
            'phone': user.phone,
            'sex': user.sex,
            'email_adrres': user.email_adrres,
            'addres': user.addres,
            'city': user.city,
            'id': user.id_client,
        }

        return render(request, 'home/client.html', context)

@csrf_exempt 
def home_client_students(request, id) :

    user =  Client.objects.get(id_client=id)
    

    if request.method == 'GET' :
        availables = []
        students = Gruaduated.objects.all()
        for student in students :
            student_data = {}
            student_data['name'] = student.name
            student_data['sid'] = student.id_graduated
            student_data['msgs']=Reviews.objects.filter(graduado_id=student.id_graduated)
            student_data['email'] = student.email_adrres
            student_data['phone'] = student.phone
            student_data['program'] = student.program_name

            

            availables.append(student_data)
    

        context = {
            'name': user.name,
            'id': user.id_client,
            'availables': availables
        }

        return render(request, 'home/client-students.html', context)
    
    if request.method == 'POST' :
        availables = []

        value = request.POST['program']
        students = Gruaduated.objects.filter(program_name=value)

        for student in students :
            student_data = {}
            student_data['name'] = student.name
            student_data['email'] = student.email_adrres
            student_data['sid'] = student.id_graduated
            student_data['msgs']=Reviews.objects.filter(graduado_id=student.id_graduated)
            student_data['phone'] = student.phone
            student_data['program'] = student.program_name


    
            availables.append(student_data) 
            
            print('estudiantes -> ', student.name)
            print('estudiantes -> ', student.id_graduated)

        context = {
            'name': user.name,
            'id': user.id_client,
            'availables': availables,
        }

        if 'TODOS' == request.POST['program'] : 
            availables = []

            students = Gruaduated.objects.all()
            
            for student in students :
                student_data = {}
                student_data['name'] = student.name
                student_data['email'] = student.email_adrres
                student_data['sid'] = student.id_graduated
                student_data['msgs']=Reviews.objects.filter(graduado_id=student.id_graduated)
                student_data['phone'] = student.phone
                student_data['program'] = student.program_name

               
                availables.append(student_data) 


            context = {
                'name': user.name,
                'id': user.id_client,
                'availables': availables

            }

            return render(request, 'home/client-students.html', context)

        return render(request, 'home/client-students.html', context)


  
#vista del instructor
def home_instructor(request, id) :
    if request.method == 'GET' :
        #obtenemos los datos del cliente por su id
        user =  Instructor.objects.get(id_instructor=id)
        #buscamos los estudiantes que coincidan con el id del instructor
        students = Gruaduated.objects.filter(id_instructor=user.id_instructor)
        students_list = []

        for student in students :
            student_data = {}
            student_data['name'] = student.name
            student_data['sid'] = student.id_graduated
            student_data['phone'] = student.phone
            student_data['email'] = student.email_adrres
            
            if student.id_instructor == user.id_instructor :
                print(student.name)
                students_list.append(student_data)
            
        context = {
            'name': user.name,
            'last_name': user.last_name,
            'phone': user.phone,
            'sex': user.sex,
            'email_adrres': user.email_adrres,
            'city': user.city,
            'id': user.id_instructor,
            'students': students_list
        }

        return render(request, 'home/instructor.html', context)


def home_graduated(request, id) :
    if request.method == 'GET' :
        #obtenemos los datos del cliente por su id
        user =  Gruaduated.objects.get(id_graduated=id)
        instructor_data = Instructor.objects.get(id_instructor=user.id_instructor)

        context = {
            'name': user.name,
            'last_name': user.last_name,
            'phone': user.phone,
            'sex': user.sex,
            'email_addres': user.email_adrres,
            'city': user.city,
            'addres': user.addres,
            'academic_traignin': user.academic_training,
            'program': user.program_name,
            'name_instructor': instructor_data.name,
            'email_instructor': instructor_data.email_adrres,
        }

        return render(request, 'home/graduated.html', context)
#instructor-students
@csrf_exempt 
def home_instructor_students(request, id) :

    user =  Instructor.objects.get(id_instructor=id)

    if request.method == 'GET' :
        availables = []
        students = Gruaduated.objects.all()
        for student in students :
            student_data = {}
            student_data['name'] = student.name
            student_data['email'] = student.email_adrres
            student_data['sid'] = student.id_graduated
            student_data['phone'] = student.phone
            student_data['program'] = student.program_name

            availables.append(student_data) 

        context = {
            'name': user.name,
            'id': user.id_instructor,
            'availables': availables
        }

        return render(request, 'home/instructor-students.html', context)
    
    if request.method == 'POST' :
        availables = []

        value = request.POST['program']
        students = Gruaduated.objects.filter(program_name=value)

        for student in students :
            student_data = {}
            student_data['name'] = student.name
            student_data['email'] = student.email_adrres
            student_data['sid'] = student.id_graduated
            student_data['phone'] = student.phone
            student_data['program'] = student.program_name


            availables.append(student_data) 
            
            print('estudiantes -> ', student.name)

        context = {
            'name': user.name,
            'id': user.id_instructor,
            'availables': availables
        }

        if 'TODOS' == request.POST['program'] : 
            availables = []

            students = Gruaduated.objects.all()
            for student in students :
                student_data = {}
                student_data['name'] = student.name
                #print("[               ] su id", student.id_graduated)
                #student_data['sid'] = student.id_graduated
                student_data['email'] = student.email_adrres
                student_data['sid'] = student.id_graduated
                student_data['phone'] = student.phone
                student_data['program'] = student.program_name

                availables.append(student_data) 

            context = {
                'name': user.name,
                'id': user.id_instructor,
                'availables': availables
            }

            return render(request, 'home/instructor-students.html', context)

        return render(request, 'home/instructor-students.html', context)


@csrf_exempt
def login(request) :

    if request.method == 'GET' : 
        return render(request, 'home/login.html')

    if request.method == 'POST' :
        user_name = request.POST['nameUser']
        password = request.POST['passUser']
        type_user = request.POST['typeUser']

        if type_user == 'client' :
            user_find =  Client.objects.get(user_client=user_name)

            if password == user_find.password_client :
                return redirect(f'/client-home/{user_find.id_client}')

        if type_user == 'instructor' :
            user_find =  Instructor.objects.get(user_instructor=user_name)
            print("1")
            if password == user_find.password_instructor :
                print("2")
                return redirect(f'/instructor-home/{user_find.id_instructor}')
            print("2.1")

        if type_user == 'graduated' :
            user_find =  Gruaduated.objects.get(user_graduated=user_name)

            if password == user_find.password_graduated :
                return redirect(f'/graduated-home/{user_find.id_graduated}')


def home(request):

    if request.method == 'GET' :
        return render(request, 'home/index.html')

@csrf_exempt
def contac(request, id, sid) :
    cliente =  Client.objects.get(id_client=id)
    egresado =  Gruaduated.objects.get(id_graduated=sid)
    context={'nombreCliente':cliente.name, "idCliente": cliente.id_client, "nombreEgresado":egresado.name, "mailto":egresado.email_adrres}
 
    if request.method == 'GET' :
        return render(request, 'home/contac.html', context)
    if request.method=='POST':
        mensaje=request.POST["Message"]
        content="Hola "+egresado.name+ ", "+cliente.name+" desea contactarte, aqui esta su mensaje: \n"+mensaje+""
        content=content+"\nContactalo por su correo: "+cliente.email_adrres+"\n" 

        send_mail(
            "Temporary Work SENA-tienes un mensaje de un cliente.",
            content,
            settings.EMAIL_HOST_USER,
            [egresado.email_adrres],
        )
        print("mensaje enviado")
        return HttpResponseRedirect(f'/client-home-students/{cliente.id_client}')
      
    

@csrf_exempt
def mensaje(request, id, sid) :
    instructor= Instructor.objects.get(id_instructor=id)
    egresado =  Gruaduated.objects.get(id_graduated=sid)
    context={'nombreInst':instructor.name, "idInst": instructor.id_instructor, "nombreEgresado":egresado.name, "mailto":egresado.email_adrres}
 
    if request.method == 'GET' :
        return render(request, 'home/msg-instructor-student.html', context)

    if request.method=='POST':
        mensaje=request.POST["Message"]
        print("mensaje enviado", mensaje)
        data = {
            "idInst": instructor.id_instructor,
            'idEgres': egresado,
        }
        save_data_msg(request,data)

        return HttpResponseRedirect(f'/instructor-home-students/{instructor.id_instructor}')
        
def handler404(request, exception):
    response = render(request, 'basic404.html')
    
    return response
        
        
 
   


    