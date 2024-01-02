from rest_framework import serializers
from lessonsapp.models import Lesson, Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        # fields = ('title', 'description',)


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        # fields = ('title', 'description',)