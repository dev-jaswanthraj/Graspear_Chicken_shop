from math import ceil, remainder
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def calculator(request):
    if request.method == "POST":
        legs = int(request.POST['Legs'])
        wings = int(request.POST['Wings'])
        cuts = float(request.POST['Cuts'])

        count = ceil(max(legs, wings)/2)

        l = (legs*0.25)
        w = (wings*0.25)

        rem_kg = (count*2)-(l+w)

        check = rem_kg - cuts
        if(check == 0):
            context = {
                "RQ":count,
                "L":0,
                "W":0,
                "C":0
            }
        elif(check < 0):
            count += ceil(abs(check)/2)
            context = {
                "RQ":count,
                "L":0,
                "W":0,
                "C":(count*2)-abs(check),
            } 
        else:
            r_l = (count*2)-legs
            r_w = (count*2)-wings
            context = {
                "RQ":count,
                "L":r_l,
                "W":r_w,
                "C":check-((r_w+r_l)*0.25)
            }

    return render(request, "result.html", context )







