from trainings.models import Training
from rest_framework import serializers


class TrainingSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'name': instance.name,
            'time': instance.time,

        }

