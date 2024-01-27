from rest_framework import serializers
from lessonsapp.models import Lesson, Course, Subscription
from lessonsapp.validators import VideoValidator



class LessonSerializer(serializers.ModelSerializer):
    # video = serializers.CharField(validators=[VideoValidator])
    class Meta:
        model = Lesson
        fields = 'id', 'title', 'description', 'video',
        validators = [
            VideoValidator(field='video'),
        ]


class LessonIncludeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['title']

class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonIncludeSerializer(many=True, read_only=True)
    subscribed = serializers.SerializerMethodField(read_only=True)



    def get_lessons_count(self, instance):
        return instance.lessons.count()


    def get_subscribed(self, instance):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            print(request and request.user)
            return Subscription.objects.filter(user=request.user, course=instance, subscribed=True).exists()
        return False


    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lessons_count', 'lessons', 'subscribed',)




class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


