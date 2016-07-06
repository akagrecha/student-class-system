from rest_framework import serializers
from class1.models import student

class StudentSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	first_name = serializers.CharField(max_length=30)
	last_name = serializers.CharField(max_length=30)
	marks1 = serializers.IntegerField()
	marks2 = serializers.IntegerField()
	marks3 = serializers.IntegerField()
	
	def create(self, validated_data):
		return student.objects.create(**validated_data)
	
	def update(self, instance, validated_data):
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.marks1 = validated_data.get('marks1', instance.marks1)
		instance.marks2 = validated_data.get('marks2', instance.marks2)
		instance.marks3 = validated_data.get('marks3', instance.marks3)
		instance.save()
		return instance
