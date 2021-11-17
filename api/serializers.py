from rest_framework import serializers
from .models import Tblfop, Tbluo
import json

class JSONSerializerField(serializers.Field):
    
    def to_representation(self, value):
        json_data = {}
        try:
            json_data = json.loads(value)
        except ValueError as e:
            raise e
        finally:
             return json_data
    def to_internal_value(self, data):
        return json.dumps(data)

class UoSerializer(serializers.ModelSerializer):
    activity_kinds = JSONSerializerField() 
    class Meta:
        model = Tbluo
        fields = ("id", "name", "activity_kinds","address")
        lookup_field = 'id'
        extra_kwargs = {
            'url':{'lookup_field':'id'}
        }
