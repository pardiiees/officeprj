from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("welcome")
def information (request,esm):
    if (esm=="ershad" or esm=="sabt" or esm=="rah"):
        if (esm=="ershad"):d={"onvan":"اداره فرهنگ و ارشاد اسلامی","phone": "33334890-038","email":"ershad.shk@gmail.com"}
        if (esm=="sabt"):d={"onvan":"اداره ثبت احوال","phone": "32225258-038","email":"sabt.shk@gmail.com"}
        if (esm=="rah"):d={"onvan":"اداره راه و شهرسازی","phone": "33333222-038","email":"rah.shk@gmail.com"}
        return render(request,"shop/edare.html",context=d)
    else:
        return HttpResponse("<div style='color:red'> not found </div>")
