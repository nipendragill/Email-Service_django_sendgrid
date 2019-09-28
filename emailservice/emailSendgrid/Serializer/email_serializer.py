from rest_framework import serializers
from ..models import EmailModel, EmailReceiverBCC, EmailReceiverCC
from django.db import models


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'

    def create(self, validated_data):
        list_cc = validated_data.pop('cc')
        list_bcc = validated_data.pop('bcc')
        email = models.objects.create(**validated_data)
        for receiver in list_cc:
            cc = models.EmailReceiverCC(
                email = email,
                receivers = receiver
            ).save()
        for receiver in list_bcc:
            bcc = models.EmailReceiverBCC(
                email=email,
                receivers = receiver
            ).save()
        return email