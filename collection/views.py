from django.shortcuts import render, redirect
from collection.forms import ThingForm
from collection.models import Thing


# Create your views here.
def index(request):
	things = Thing.objects.all()

	#things=Thing.objects.all()
	return render(request,'index.html', {
		'things':things,
		})
def thing_detail(request, slug):
	#grab the object
	thing= Thing.objects.get(slug=slug)
	#and pass to the template
	return render(request, 'things/thing_detail.html', {
		'thing':thing,
		})
def edit_thing(request, slug):
	#grab the object
	thing= Thing.objects.get(slug=slug)
	#set the form we're using
	form_class =ThingForm
	#if we are coming to this view from the submitted form
	if request.method == 'POST':
		#Grab data from the submitted form and apply to the form
		form=form_class(data=request.POST, instance=thing)
		if form.is_valid():
			#save the new data
			form.save()
			return redirect('thing_detail', slug=thing.slug)
		#otherwise just create the form
	else:
		form=form_class(instance=thing)
		#and render the template
		return render(request, 'things/edit_thing.html', {
		'thing':thing,
		'form' : form,
		})