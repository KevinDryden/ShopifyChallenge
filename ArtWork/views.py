from django.shortcuts import render
from .models import Image
from .forms import ImageUpload

# Create your views here.

def View(request):
    Images = Image.objects.all()
    context = {"Images":Images}

    return render(request, "Images.html",context)

def Manage(request):

  if request.method == "POST":

    if 'Delete' in request.POST:
      image = Image.objects.get(id = request.POST["id"])
      if image.Owner == request.user:
        image.delete()


    else:
      upload = ImageUpload(request.POST, request.FILES)
      if upload.is_valid():
        instance = upload.save(commit=False)
        instance.Owner = request.user
        instance.save()
        print("Upload Sucessful")
      else:
        print(upload.errors)
    

  Images = Image.objects.all()
  Form = ImageUpload()
  context = {"Form":Form,"Images":Images}
  return render(request,('Manage.html'),context)