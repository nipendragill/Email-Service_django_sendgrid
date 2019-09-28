from rest_framework import serializers
from ..models import EmailModel, EmailReceiverBCC, EmailReceiverCC, EmailReceiverTo
from django.db import models


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'

    def create(self, validated_data):
        receivers = validated_data.pop('receivers')
        list_cc = validated_data.pop('cc')
        list_bcc = validated_data.pop('bcc')
        email = models.objects.create(**validated_data)
        for receiver in receivers:
            to = models.EmailReceiverTo(
                email = email,
                receivers = receiver
            ).save()
        for receiver in list_cc:
            cc = models.EmailReceiverCC(
                email = email,
                cc = receiver
            ).save()
        for receiver in list_bcc:
            bcc = models.EmailReceiverBCC(
                email=email,
                bcc = receiver
            ).save()
        return email