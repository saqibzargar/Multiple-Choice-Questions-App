from django.shortcuts import redirect, render
from .models import Question ,Qno , marksObtained
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.



def home(request):
    return render(request, 'home.html')

def CreateAccount(request):
    return render(request, 'CreateAccount.html')


def questions(request):
    usr = User.objects.all()[0]
    if Qno.value < 0:
        Qno.value = len(Question.objects.all())-1
    res = Question.objects.all()[Qno.value]
    if Qno.value + 1 == len(Question.objects.all()):
        Qno.value = 0
        return render(request, 'questions.html',{'res':res, 'Qno':Qno, 'usr':usr} )
    else:
        return render(request, 'questions.html',{'res':res, 'Qno':Qno, 'usr':usr})





def submit(request):
    res = Question.objects.all()[Qno.value]
    correctAnswer = (Question.objects.all()[Qno.value].answer)
    if request.method == "POST":
        result = str(request.POST['answer'])
        print('answer is '+result)
        if result == correctAnswer:
            marksObtained.value += 1
            print(f'current marks are :{marksObtained.value}')
        else:
            return redirect('questions')
        Qno.value += 1
        return redirect('questions')



def finish(request):
    total = marksObtained
    return render(request, 'result.html',{'total': total})



def next(request):
    Qno.value += 1
    return redirect('questions')




def previous(request):
    if Qno.value < 0:
        Qno.value = len(Question.objects.all()) - 1
    Qno.value -= 1
    return redirect('questions')

def accountCreation(request):
    email = request.POST['email']
    username = request.POST['username']
    #passw = request.POST['password'] 
    password2 = request.POST.get('password2') 

    user = User.objects.create_user(username=username, email=email , password = password2)
    user.save()
    messages.success(request,'user added successfully ')
    return redirect('home')


def login(request):
    '''
    res = User.objects.all()
    username = request.POST['username']
    password = 'imrankhan'
    if username == res.username():
    '''
    return redirect('questions')


def addQuestions(request):

    return render(request,'addQuestions.html')


def uploadQuestions(request):
    questionText = request.POST.get('questionText')
    option1 = request.POST.get('option1')
    option2 = request.POST.get('option2')
    option3 = request.POST.get('option3')
    option4 = request.POST.get('option4')
    answer = request.POST.get('answer1')
    myQuestion = Question(questionText = questionText, opt1 = option1 ,opt2 = option2 , opt3 = option3 , opt4= option4 , answer= answer)
    myQuestion.save()
    return redirect('home')
