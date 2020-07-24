from rest_framework import serializers

from trainings.models import Training


class TrainingSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            "name": instance.name,
            "time": instance.time,
        }

