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
    person = serializers.CharField(source='person.first_name', read_only=True)
    memo = serializers.CharField(source='memo.title', read_only=True)
    class Meta:
        model = MemoPerson
        fields = ('id', 'memo', 'person')