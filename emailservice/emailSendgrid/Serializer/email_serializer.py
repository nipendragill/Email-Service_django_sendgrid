from rest_framework import serializers

class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
