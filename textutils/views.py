from django.http import HttpResponse
from django.shortcuts import render
import string


def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')


    #check whether which checkbox is on
    if removepunc == "on":
        punctuations = string.punctuation
        analyzed = ""
        for item in djtext:
            if item not in punctuations:
                analyzed += item
        params = {'purpose': "Removed Punctuations", 'analyzed_text': analyzed}
        #analyze the texts
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for item in djtext:
            analyzed += item.upper()
        params = {'purpose': "Changed to Upper Case", 'analyzed_text': analyzed}
        #analyze the texts
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for item in djtext:
            if item != "\n" and item != "\r":
                analyzed = analyzed + item
        params = {'purpose': "Removed NewLines", 'analyzed_text': analyzed}
        #analyze the texts
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, item in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + item
        params = {'purpose': "Removed Extra Spaces", 'analyzed_text': analyzed}
        #analyze the texts
        djtext = analyzed
    
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")
    
    
    return render(request, "analyze.html", params)