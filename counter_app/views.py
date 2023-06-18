from django.shortcuts import render, redirect

# Create your views here.

#def index(request):
    #return render(request, 'counter_page.html')



def session(request):
    counter=request.session.get('counter', 0)
    counter += 1
    request.session['counter'] = counter
    context = {
        "counterxx": counter
    }
    return render(request, 'counter_page.html', context)
#***********************************************************************

def destroy(request):
    request.session.clear()
    return redirect("/")