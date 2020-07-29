from django.shortcuts import render, redirect, get_object_or_404
from .models import item
from .forms import itemForm

# Create your views here.


def get_todo_list(request):
    items = item.objects.all()
    # gets query set of all the items in the database.
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
    # adding the context var in our render will ensure that
    # we have access to it in our todo list .html template.
    # The render function takes an HTTP request and
    # a template name as it's two arguments


def add_item(request):
    if request.method == "POST":
        form = itemForm(request.POST)
        if form.is_valid():
            form.save()
            # done = "item_done" in request.POST
            # it will chk if done chkbox is in the form request
            # item.objects.create(name=name, done=done)
            # this will create the item in our db
            return redirect("get_todo_list")
    form = itemForm()
    # it will create an instance of our form class from form.py
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    itm = get_object_or_404(item, id=item_id)
    # d above gets a copy of the item form from the db
    # Which ll use tosay we want to get an instance of the item model.
    # With an ID equal to the item ID that was passed
    #  into the view via the URL.
    if request.method == "POST":
        form = itemForm(request.POST, instance=itm)
        if form.is_valid():
            form.save()
            return redirect("get_todo_list")
    form = itemForm(instance=itm)
    # it tells it to prepopulate our form wit the data we got frm d db
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    itm = get_object_or_404(item, id=item_id)
    itm.done = not itm.done
    #  it will change the done status the opposite
    #  of whtevr it is save as wen a user clicks on
    #  our view it will get the done item and if it
    #  is true it will flip to false and vice versa
    itm.save()
    return redirect("get_todo_list")


def delete_item(request, item_id):
    itm = get_object_or_404(item, id=item_id)
    itm.delete()
    return redirect("get_todo_list")
