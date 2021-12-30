
from rest_framework import serializers
from api.models import Users, Todos


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = [
            "id",
            "name",
            "username",
            "email",
            "street",
            "suite",
            "city",
            "zipcode",
            "geo_lat",
            "geo_lng",
            "phone",
            "website",
            "company_name",
            "company_catchPhrase",
            "company_bs"
        ]


class TodosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todos
        fields = [
            "userId",
            "id",
            "title",
            "completed"
        ]

