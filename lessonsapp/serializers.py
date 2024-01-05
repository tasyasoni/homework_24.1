from rest_framework import serializers
from lessonsapp.models import Lesson, Course



class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'



class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()


    def get_lessons_count(self, instance):
        return instance.lessons.count()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'lessons', 'lessons_count']






