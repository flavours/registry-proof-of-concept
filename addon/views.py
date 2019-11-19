from addon.models import Addon, AddonVersion, Stack
from namespace.models import Namespace
from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class StackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stack
        fields = ("id", "identifier")


class StackViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer


class AddonSerializer(serializers.HyperlinkedModelSerializer):
    addonversions = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="addonversion-detail"
    )

    class Meta:
        model = Addon
        fields = (
            "id",
            "namespace",
            "identifier",
            "description",
            "addonversions",
        )


class AddonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Addon.objects.all()
    serializer_class = AddonSerializer


class AddonVersionSerializer(serializers.HyperlinkedModelSerializer):

    yaml = serializers.SerializerMethodField()

    platforms = serializers.SerializerMethodField()

    class Meta:
        model = AddonVersion
        fields = ("id", "addon", "identifier", "yaml", "stacks", "platforms")

    def get_yaml(self, obj):
        """
        clean the newlines and lineendings
        """
        return "\n".join(obj.yaml.splitlines()) + "\n"

    def get_platforms(self, obj):
        """ legacy shim"""
        return [
            i.get_api_url(request=self.context["request"])
            for i in obj.stacks.all()
        ]


class AddonVersionResolveSerializer(serializers.Serializer):
    query = serializers.CharField(max_length=255)


class AddonVersionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AddonVersion.objects.all()

    def get_serializer_class(self):
        if self.action == "resolve":
            return AddonVersionResolveSerializer
        return AddonVersionSerializer

    @action(detail=True)
    def yaml(self, request, pk):
        return Response(self.get_object().yaml)

    @action(methods=["post"], detail=False)
    def resolve(self, request):
        """
        query = `<namespace>/<addon>:<addonversion>`
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            namespace = serializer.validated_data["query"].split("/", 1)[0]
            addon_name = (
                serializer.validated_data["query"]
                .split(":", 1)[0]
                .split("/", 1)[1]
            )
            try:
                addonversion = serializer.validated_data["query"].split(
                    ":", 1
                )[1]
            except IndexError:
                addonversion = "latest"
        except:
            raise serializers.ValidationError(
                {
                    "non_field_errors": [
                        "I dont understand the query. It must be in the form `<namespace>/<addon>:<addonversion>` "
                    ]
                }
            )

        try:
            addon = Namespace.objects.get(identifier=namespace).addons.get(
                identifier=addon_name
            )
            version = addon.addonversions.get(identifier=addonversion)
            result = {"id": version.pk, "identifier": str(version)}
            return Response(
                {"query": serializer.validated_data["query"], "result": result}
            )
        except Addon.DoesNotExist:
            raise serializers.ValidationError(
                {"non_field_errors": [f"Addon `{addon_name}` not found."]}
            )
        except AddonVersion.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "non_field_errors": [
                        f"Addon Version `{addonversion}` not found."
                    ]
                }
            )
        except:
            raise serializers.ValidationError(
                {"non_field_errors": ["No result found."]}
            )
        return Response(f"{namespace} - {addon} - {addonversion}")
