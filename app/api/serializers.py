from rest_framework import serializers
from django.conf import settings

from .models import Sale, SaleChannel

class SaleSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(input_formats=[settings.DATETIME_MASK])
    sale_channel = serializers.PrimaryKeyRelatedField(
        queryset=SaleChannel.objects.all(),
        error_messages={
            'does_not_exist': 'The provided sale channel is not valid.',
            'required': 'This field is required.',
        }
    )

    class Meta:
        model = Sale
        fields = '__all__'

class SaleChannelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        error_messages={
            'required': 'This field is required.',
            'blank': 'This field cannot be blank.',
        }
    )

    class Meta:
        model = SaleChannel
        fields = '__all__'

    def validate_name(self, value):
        if SaleChannel.objects.filter(name=value).exists():
            raise serializers.ValidationError('A Sales Channel with this name already exists.')
        return value