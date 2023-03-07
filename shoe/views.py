from django.shortcuts import render, redirect
from shoe.forms import ShoeForm
from shoe.models import Shoe

# Create your templates here.
# .save() is the ORM equivalent of the SQL insert to statement.
def shoe(request):
    if request.method == "POST":
        form = ShoeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ShoeForm()
    return render(request, 'index.html', {'form':form})

# .all() is the ORM equivalent of the SQL statement "SELECT * FROM tablename"
def show(request):
    shoes = Shoe.objects.all()
    return render(request, "show.html", {'shoes': shoes})


# .get is the ORM equivalent of the SQL statement "SELECT * FROM tablename WHERE id = ? "
# method update carries the update process for a single record

def edit(request, id):
    shoe = Shoe.objects.get(id=id)
    return render(request,'edit.html', {'shoe':shoe})

def update(request, id):
    shoe = Shoe.objects.get(id=id)
    form = ShoeForm(request.POST, instance = shoe)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'shoe': shoe})

# .delete() is the ORM equivalent of the statement SQL : " DELETE FROM tablename WHERE id = ? "
def destroy(request, id):
    shoe = Shoe.objects.get(id=id)
    shoe.delete()
    return redirect("/show")



























