from django.conf import settings
from main.models import Users
from main.models import Vehicle
import requests


users_url = "https://api-us.nextgen.teletracnavman.net:8067/v1/users?status=ALL&pruning=B2B&key=bf6438440fb142d89d13f067a2cd76b3"

vehicles_url = "https://api-us.nextgen.teletracnavman.net:8067/v1/vehicles?status=ALL&pruning=B2B&key=bf6438440fb142d89d13f067a2cd76b3"
def schedule_api():

	users_request = requests.get(users_url)
	if users_request.status_code == 200:
		result = users_request.json()
		users = Users.objects.create()
		users.json = result.copy()
		users.save()

	vehicles_request = requests.get(vehicles_url)
	if vehicles_request.status_code == 200:
		result = vehicles_request.json()
		vehicles = Vehicle.objects.create()
		vehicles.json = result.copy()
		vehicles.save()




