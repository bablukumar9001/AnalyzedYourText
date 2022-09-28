
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "analyze1.html")

def analyze(request):

    #get the text
    djtext = request.POST.get("text", "default")    

    removepunc = request.POST.get("removepunc", "off")
    capitalizefirst = request.POST.get("capitalizefirst", "off")
    lowerfirst = request.POST.get("lowerfirst", "off")
    newlineremover = request.POST.get("newlineremover", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    
    # logic

    if removepunc == "on":
        punctuations = '''!!@#$%^&*()<>?/.,;""\/|[]{}~`*_'''
        analyzed = ""
        for char in djtext:
          if char not in punctuations:
           analyzed = analyzed+char
        params={'purpose':'Punctuations Removed  ','analyzed_text':analyzed}  
        djtext=analyzed

    if capitalizefirst =="on":
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
            params = {'purpose': 'Changed To UpperCase ', 'analyzed_text': analyzed}
            djtext=analyzed
    
    if lowerfirst =="on":
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.lower()
            params = {'purpose': 'Changed To LowerCase ', 'analyzed_text': analyzed}
            djtext=analyzed
    
      
    if newlineremover =="on":
        analyzed=''
        for char in djtext:
            if char!='\n' and char!="\r":
                analyzed=analyzed+char
                params = {'purpose': 'NewLines Removed  ', 'analyzed_text': analyzed}
                djtext=analyzed

    if extraspaceremover=="on":
        analyzed=''
        for index, char in enumerate(djtext):
         if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
                params = {'purpose': 'Removed extra space ', 'analyzed_text': analyzed}

   

    if(removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and capitalizefirst!="on" and lowerfirst!="on"):
       return HttpResponse("<h1>Please select any operation and Try again !</h1>")   
    
    return render(request, 'analyze2.html', params)
   
