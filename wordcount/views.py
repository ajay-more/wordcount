
from django.shortcuts import render
import operator
def homepage(request):
    return render(request ,'home.html',{'name' : 'Hii ajay more'})

def count(request):
    data  =request.GET['fulltextarea']
    word_list = data.split()
    counter =0
    for i in word_list:
        counter+=1

    word_dic = {}
    for word in word_list:
        if word in word_dic:
            word_dic[word]+=1
        else:
            word_dic[word] =1

    sorted_list =sorted(word_dic.items() ,key =operator.itemgetter(1),reverse =True)

    return render(request ,'count.html',{'text' : data,'count_no':counter,'word_dic':sorted_list})

def aboutus(request):
    return render(request , 'about_us.html')