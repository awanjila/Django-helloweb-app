from registration.backends.simple.views import RegistrationView
#my new registration view, subclassing RegistrtionView
#from our plugin
class MyRegistrationView(RegistrationView):
	def get_success_url(self, request, user):
		#the named URL that we want to redirect to after
		#succesful registration
		return ('registration_create_thing')