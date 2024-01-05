from rest_framework import serializers
from lessonsapp.models import Lesson, Course



class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = 'id', 'title', 'description', 'video'


class LessonIncludeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['title']

class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonIncludeSerializer(many=True)


    def get_lessons_count(self, instance):
        return instance.lessons.count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lessons_count', 'lessons')






