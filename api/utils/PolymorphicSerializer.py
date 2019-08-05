from typing import Dict

from rest_framework import serializers


class PolymorphicSerializer(serializers.Serializer):
    """
    Serializer to handle multiple subclasses of another class

    - For serialized dict representations, a 'type' key with the class name as
      the value is expected: ex. {'type': 'Decimal', ... }
    - This type information is used in tandem with get_serializer_map(...) to
      manage serializers for multiple subclasses
    """
    def get_serializer_map(self) -> Dict[str, serializers.Serializer]:
        """
        Return a dict to map class names to their respective serializer classes

        To be implemented by all PolymorphicSerializer subclasses
        """
        raise NotImplementedError

    def to_representation(self, obj):
        """
        Translate object to internal data representation

        Override to allow polymorphism
        """
        type_str = obj.__class__.__name__

        try:
            serializer = self.get_serializer_map()[type_str]
        except KeyError:
            raise ValueError(
                'Serializer for "{}" does not exist'.format(type_str),
            )

        data = serializer(obj, context=self.context).to_representation(obj)
        data['type'] = type_str
        return data

    def to_internal_value(self, data):
        """
        Validate data and initialize primitive types

        Override to allow polymorphism
        """
        try:
            type_str = data['type']
        except KeyError:
            raise serializers.ValidationError({
                'type': 'This field is required',
            })

        try:
            serializer = self.get_serializer_map()[type_str]
        except KeyError:
            raise serializers.ValidationError({
                'type': 'Serializer for "{}" does not exist'.format(type_str),
            })

        validated_data = serializer(context=self.context) \
            .to_internal_value(data)
        validated_data['type'] = type_str
        return validated_data

    def create(self, validated_data):
        """
        Translate validated data representation to object

        Override to allow polymorphism
        """
        serializer = self.get_serializer_map()[validated_data['type']]
        return serializer(context=self.context).create(validated_data)