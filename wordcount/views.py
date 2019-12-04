from django.http import HttpResponse
from django.shortcuts import render
import operator
def about(request):
    return render(request, 'About.html' )
def homepage(request):
    return render(request,'home.html')

def count(request):
    textforcounting = request.GET['textforcounting']

    wordlist = textforcounting.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] +=1
        else:
            #add to the dictionary
            worddictionary[word] =1



    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'textforcounting':textforcounting,'count':len(wordlist),'sortedwords':sortedwords})
def hack(request):
    return HttpResponse("<h1>Oh how i love to be a great hacker</h1>")
