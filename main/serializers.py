from rest_framework import serializers
from .models import Cafe
from django.utils import timezone

class DateTimeTzAwareField(serializers.DateTimeField):
    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeTzAwareField, self).to_representation(value)

class CafeSerializer(serializers.ModelSerializer):
    create_date = DateTimeTzAwareField()

    class Meta:
        model = Cafe
        fields = '__all__'