from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'home.html',)

def result(request):

    num_1 = request.GET['n1']
    num_2 = request.GET['n2']
    num_3 = request.GET['n3']
    num_4 = request.GET['n4']
    num_5 = request.GET['n5']
    num_6 = request.GET['n6']

    list = []
    number = random.randint(1, 45)
     
    for i in range(6):
        while number in list:
            number = random.randint(1,45)
        list.append(number)

    match = 0
    if int(num_1) in list:
        match+=1
    if int(num_2) in list:
        match+=1
    if int(num_3) in list:
        match+=1
    if int(num_4) in list:
        match+=1
    if int(num_5) in list:
        match+=1
    if int(num_6) in list:
        match+=1


    grade = 0
    if(match == 6): 
        grade = 1
    if(match == 5): 
        grade = 2
    if(match == 4): 
        grade = 3
    if(match == 3): 
        grade = 4
    if(match == 2): 
        grade = 5
    if(match == 1): 
        grade = 0
    if(match == 0): 
        grade = 0

    return render(request, 'result.html', {'list_1': list[0], 'list_2':list[1],'list_3':list[2],'list_4':list[3],'list_5':list[4],'list_6':list[5], 
    'num_1':num_1, 'num_2':num_2, 'num_3':num_3, 'num_4':num_4, 'num_5':num_5, 'num_6':num_6, 'testlist':list, 'match':match,'grade':grade})
