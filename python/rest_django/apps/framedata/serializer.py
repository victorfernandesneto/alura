from rest_framework import serializers
from apps.framedata.models import Character, Move

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class CharacterField(serializers.RelatedField):
    def to_representation(self, value):
        return value.character_name

    def to_internal_value(self, data):
        try:
            character = Character.objects.get(character_name=data)
            return character
        except Character.DoesNotExist:
            raise serializers.ValidationError("Character does not exist.")

class MoveSerializer(serializers.ModelSerializer):
    character = CharacterField(queryset=Character.objects.all())
    class Meta:
        model = Move
        fields = '__all__'

class ListMoveCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        exclude = ['character']