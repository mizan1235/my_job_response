from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from job.models import user_cred,employee_cred,job_details,job_apllicaions
from django.contrib.auth.hashers import check_password,make_password
from rest_framework.response import Response

# Create your views here.
def index(request):
    return HttpResponse("Hello")

@api_view(['POST'])
def create_user(request,format=None):
    name_input=request.data['name']
    email_input=request.data['email']
    phone_input=request.data['phone']
    user_name=request.data['username']
    password_input=request.data['password']
    try:
        user_get=user_cred.objects.get(username=user_name)
        return Response({'message':'This username already exist'})
    except:
        obj=user_cred(
            name=name_input,
            email=email_input,
            phone=phone_input,
            username=user_name,
            password=make_password(password_input)
        )
        obj.save()
        return Response({'message':'Successfully Registered'})

@api_view(['POST'])
def create_employee(request,format=None):
    name_input=request.data['name']
    email_input=request.data['email']
    phone_input=request.data['phone']
    user_name=request.data['username']
    password_input=request.data['password']
    try:
        user_get=employee_cred.objects.get(username=user_name)
        return Response({'message':'This username already exist'})
    except:
        obj=employee_cred(
            name=name_input,
            email=email_input,
            phone=phone_input,
            username=user_name,
            password=make_password(password_input)
        )
        obj.save()
        return Response({'message':'Successfully Registered'})
@api_view(['POST'])
def create_job(request,format=None):
    
    companyLogo=request.data['company_logo']
    companyName=request.data['company_name']
    companyTitle=request.data['company_title']
    companyLocation=request.data['location']
    companyDate=request.data['date']
    jobId=request.data['job_id']
    applyLink=request.data['apply_link']
    user_name=request.data['username']
    
    obj=job_details(
            company_logo=companyLogo,
            company_title=companyTitle,
            company_name=companyName,
            location=companyLocation,
            date=companyDate,
            job_id=jobId,
            apply_link=applyLink,
            username=user_name
        )
    obj.save()
    return Response({'message':'Job added'})

@api_view(['POST'])
def login_user(request, format=None):
    user_name = request.data.get('username')
    password = request.data.get('password')
    try:
        user_get=user_cred.objects.get(username=user_name)
    except:
        return Response({'message':'user does not found'})
    #print(user_get.password)
    if(check_password(password,user_get.password)):
        return Response({'status':'successfull loged in'})
                    
    else:
        return Response({'status':'password doesnot match'})
    
@api_view(['POST'])
def login_employee(request, format=None):
    user_name = request.data.get('username')
    password = request.data.get('password')
    try:
        user_get=employee_cred.objects.get(username=user_name)
    except:
        return Response({'status':'user does not found'})
    #print(user_get.password)
    if(check_password(password,user_get.password)):
        return Response({'status':'successfull loged in'})
                    
    else:
        return Response({'status':'password doesnot match'})


@api_view(['GET'])
def get_job(request,format=None):
    obj=job_details.objects.all().values()
    return Response({'jobs':obj})

@api_view(['POST'])
def get_job_by_id(request,format=None):
    Id=request.data['job_id']
    get_job=job_details.objects.filter(id=Id).all().values()
    return Response({'job':get_job})


@api_view(['POST'])
def get_emp_job(request,format=None):
    user_name=request.data['username']
    print(user_name)
    try:
        get_job=job_details.objects.filter(username=user_name).all().values()
        return Response({'Jobs':get_job})
    except:
        return Response ({'job':'No jobs found'})



@api_view(['POST'])
def get_job_comp(request,format=None):
    companyName=request.data['company_name']
    try:
        if(companyName=="All"):
            job=job_details.objects.all().values()
            return Response({'Jobs':job})
        get_job=job_details.objects.filter(company_name=companyName).all().values()
        return Response({'Jobs':get_job})
    except:
        return Response({'message':'No jobs found'})


@api_view(['POST'])
def get_job_location(request,format=None):
    companyLocation=request.data['location']
    try:
        if(companyLocation=="All"):
            job=job_details.objects.all().values()
            return Response({'jobs':job})
        get_job=job_details.objects.filter(location=companyLocation).all().values()
        return Response({'jobs':get_job})
    except:
        return Response({'message':'No jobs found'})


@api_view(['PUT'])

def update_job(request,format=None):
    id=request.data['id']
    

    # print(job[0]['job_id'])
    companyLogo=request.data['company_logo']
    companyName=request.data['company_name']
    companyTitle=request.data['company_title']
    companyLocation=request.data['location']
    companyDate=request.data['date']
    jobId=request.data['job_id']
    applyLink=request.data['apply_link']
    user_name=request.data['username']
    job=job_details.objects.filter(id=id).update(company_logo=companyLogo,company_name
                                                 =companyName,company_title=companyTitle,
                                                 location=companyLocation,date=companyDate,
                                                 job_id=jobId,apply_link=applyLink,
                                                 username=user_name)
    
    
   

    return Response({'message':'updated successfully'})

@api_view(['POST'])
def get_user(request,format=None):
    userName=request.data['username']
    user=user_cred.objects.filter(username=userName).all().values()
    return Response({'user':user})

@api_view(['PUT'])
def update_user(request,format=None):
    Name=request.data['name']
    Email=request.data['email']
    userName=request.data['username']
    newUserName=request.data['new_user_name']
    Phone=request.data['phone']
    user=user_cred.objects.filter(username=userName).update(name=Name,
                                                            email=Email,
                                                            username=newUserName,
                                                            phone=Phone)
    return Response({'message':'Profile Updated Successfully'})

@api_view(['POST'])
def update_user_pass(request, format=None):
    try:
        userName = request.data['username']
        newPassword = request.data['password']

        # Fetch the user object based on the username
        user = user_cred.objects.get(username=userName)

        # Update the user's password using make_password
        user.password = make_password(newPassword)
        user.save()

        return Response({'message': 'Password updated successfully'})
    except user_cred.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
    
@api_view(['POST'])
def apply_job(request,format=None):
    userName=request.data['username']
    jobId=request.data['job_id']
    Name=request.data['name']
    father=request.data['father_name']
    mother=request.data['mother_name']
    dob=request.data['DOB']
    Email=request.data['email']
    Address=request.data['address']
    Town=request.data['hometown']
    PIN=request.data['pin']
    Experience=request.data['experience']
    Resume=request.data['resume']
    # try:
    #     get_user=job_apllicaions.objects.get(username=userName)
    #     return Response({'message':'You have applied already this job   '})
    # except:
    obj=job_apllicaions(
            username=userName,
            job_id=jobId,
            name=Name,
            father_name=father,
            mother_name=mother,
            DOB=dob,
            email=Email,
            address=Address,
            hometown=Town,
            pin=PIN,
            experience=Experience,
            resume=Resume
        )
    obj.save()
    return Response({'message':'Your Application submitted successfully'})

@api_view(['POST'])
def get_applied_job(request,foemat=None):
    user_name=request.data['username']
    get_applications=job_apllicaions.objects.filter(username=user_name).all().values()
    return Response({'applications':get_applications})


@api_view(['DELETE'])
def delete_application(request,format=None):
    Id=request.data['id']
    get_application=job_apllicaions.objects.filter(id=Id).delete()
    return Response({"message":"deleted successfullt",
                     'data':get_application
                     })

@api_view(['POST'])
def get_applications(request,format=None):
    id=request.data['id']
    applications=job_apllicaions.objects.filter(job_id=id).all().values()
    return Response({'applications':applications})