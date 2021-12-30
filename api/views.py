from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets

import requests
import csv

from api.models import Users, Todos
from api.serializers import UsersSerializer, TodosSerializer


def get_data(request):
    # Add users to database
    users_url = "https://jsonplaceholder.typicode.com/users"
    r = requests.get(users_url)
    users_request = r.json()
    for user in users_request:
        data = {
            'name': user['name'],
            'username': user['username'],
            'email': user['email'],
            'street': user['address']['street'],
            'suite': user['address']['suite'],
            'city': user['address']['city'],
            'zipcode': user['address']['zipcode'],
            'geo_lat': user['address']['geo']['lat'],
            'geo_lng': user['address']['geo']['lng'],
            'phone': user['phone'],
            'website': user['website'],
            'company_name': user['company']['name'],
            'company_catchPhrase': user['company']['catchPhrase'],
            'company_bs': user['company']['bs']
        }
        Users.objects.update_or_create(**data)

    # Add user tasks to database
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    r = requests.get(todos_url)
    todos_request = r.json()
    for todo in todos_request:
        user_id = todo['userId']
        data = {
            'userId': Users.objects.get(pk=user_id),
            'title': todo['title'],
            'completed': todo['completed'],
        }
        Todos.objects.update_or_create(**data)

    return JsonResponse('Data downloaded successfully ', safe=False)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class TodosViewSet(viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

def send_data(request):

    # Export data from database to CSV file
    response = HttpResponse(content_type='text/scv')
    users = Users.objects.all()
    user_task = []
    for user in users:
        todos = user.user_todos.values('title', 'completed')
        for todo in todos:
            user_task.append([user.name, user.city, todo['title'], todo['completed']])
        user_task.append([user.name, user.city])

    fields_name = ['name', 'city', 'title', 'completed']
    writer = csv.writer(response)
    writer.writerow(fields_name)
    writer.writerows(user_task)

    response['Content-Disposition'] = 'attachment; filename="users_todos.csv"'

    return response