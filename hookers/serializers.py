from rest_framework.serializers import Serializer, ModelSerializer
from .models import Hooker

class HookersModelSerializer(ModelSerializer):
    class Meta:
        model = Hooker
        fields = "__all__"