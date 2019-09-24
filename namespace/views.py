from namespace.models import Namespace
from rest_framework import serializers, viewsets


class NamespaceSerializer(serializers.HyperlinkedModelSerializer):
    addons = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="addon-detail"
    )

    class Meta:
        model = Namespace
        fields = ("id", "identifier", "addons")


class NamespaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Namespace.objects.all()
    serializer_class = NamespaceSerializer
