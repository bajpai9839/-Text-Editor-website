from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("hi  This is your home page<h1> welcome<h1>")#


'''
def page(request):
    return HttpResponse("hellon how are you iama amitabh bacchan ")


def google(request):
    return HttpResponse(
        "<h1> CLICK BELOW LINK TO OPEN GOOGLE PAGE..... </h1> <a href='https://www.google.com'><h1>GOOGLE</H1> </a>")


def google(request):
    return HttpResponse("<h1> CLICK BELOW LINK TO open google.... </h1>")

'''


def analyse(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')


    if removepunc == "on":
        punctuations = ''';'\@#$%^&*()_+[]-=+/\,.{}""""'''
        analysed = ""
        for char in djtext:

            if char not in punctuations:


                analysed = analysed + char

        params = {'purpose': 'Removed Punctuations', 'analysed_text': analysed}
        djtext = analysed

    if newlineremover == "on":


        analysed=""
        for char in djtext:


            if char != '\n' and char != '\r':





                analysed = analysed + char
            else:
                print("no)")

        params = {'purpose': 'removed new lines', 'analysed_text': analysed}
        djtext = analysed

    if spaceremover == 'on':


        analysed = ""


        for index,char in enumerate(djtext):

            if djtext[index] == "    " and djtext[index+1] =="    ":
                pass

            else:

                analysed = analysed+char
        params = {'purpose': 'remove space','analysed_text': analysed}
        djtext = analysed



    if lowercase == 'on':
        analysed = ""
        for char in djtext:
            analysed = analysed + char.lower()
        params = {'purpose': 'change into lower case', 'analysed_text': analysed}
        djtext = analysed




    if (fullcaps == "on"):
        analysed = ""

        for char in djtext:
            analysed = analysed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analysed_text': analysed}
        djtext = analysed
    if(removepunc != "on" and newlineremover != "on" and fullcaps != "on" and lowercase != "on"):
        return HttpResponse("please select the option . ERROR!!!")





    return render(request, 'analyse.html', params)





















