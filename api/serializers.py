from rest_framework import serializers

from .models import ClientInfo, ClientPersDoc, PlatformRule, Qualification, ClientState


class ClientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientInfo
        fields = '__all__'


class ClientPersDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientPersDoc
        fields = '__all__'


class ClientStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientState
        fields = '__all__'


class PlatformRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformRule
        fields = '__all__'


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'
