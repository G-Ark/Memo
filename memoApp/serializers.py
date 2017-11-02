from rest_framework import serializers
from .models import Memo, Person, Data, MemoPerson

class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = ('id', 'title', 'text', 'date')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'phone_number')

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'name', 'data_type', 'memo_id')

class MemoPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoPerson
        fields = ('id', 'memo_id', 'person_id')