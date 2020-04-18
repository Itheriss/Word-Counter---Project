from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')
def count(request):
    UserText = request.GET['UserText']
    textList = UserText.split()
    wordDict = {}
    for word in textList:
        if word in wordDict:
            #Increment Count
            wordDict[word] += 1
        else:
            #add to dict
            wordDict[word] = 1
    sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'UserText':UserText, 'count': len(textList), 'WordCount':sortedWords})
def about(request):
    return render(request, 'about.html')
