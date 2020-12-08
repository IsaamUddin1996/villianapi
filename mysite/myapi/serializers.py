from rest_framework import serializers

from .models import Villian

class VillianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Villian
        fields = ('villian', 'DOB')