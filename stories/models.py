from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Choice Fields
STORY_LOCATION = (
    ('Telford', 'Telford'),
    ('Shrewsbury', 'Shrewsbury'),
    ('Bishops Castle', 'Bishops Castle'),
    ('Bridgnorth', 'Bridgnorth'),
    ('Broseley', 'Broseley'),
    ('Church Stretton', 'Church Stretton'),
    ('Cleobury Mortimer', 'Cleobury Mortimer'),
    ('Clun', 'Clun'),
    ('Craven Arms', 'Craven Arms'),
    ('Ellesmere', 'Ellesmere'),
    ('Ludlow', 'Ludlow'),
    ('Market Drayton', 'Market Drayton'),
    ('Much Wenlock', 'Much Wenlock'),
    ('Newport', 'Newport'),
    ('Oswestry', 'Oswestry'),
    ('Shifnal', 'Shifnal'),
    ('Wem', 'Wem'),
    ('Whitchurch', 'Whitchurch'),
    ('Shropshire', 'Shropshire'),
)

NEWS_CATEGORY = (
    ('General', 'General'),
    ('Business', 'Business'),
    ('Charity', 'Charity'),
    ('Culture & Lifestyle', 'Culture & Lifestyle'),
    ('Education', 'Education'),
    ('Entertainment', 'Entertainment'),
    ('Family', 'Family'),
    ('Food', 'Food'),
    ('Ideas & Innovation', 'Ideas & Innovation'),
    ('Motoring', 'Motoring'),
    ('Nature', 'Nature'),
    ('Sport', 'Sport'),
    ('Travel', 'Travel'),
)


class Story(models.Model):
    """
    Model to create and manage stories
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="stories_storys"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')
    story_location = models.CharField(max_length=50, choices=STORY_LOCATION)
    news_category = models.CharField(max_length=50, choices=NEWS_CATEGORY)


    class Meta:
        """
        Ordering stories
        """
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | by {self.author} | location {self.story_location} | category {self.news_category}" 


class Comment(models.Model):
    """
    Model to comment on stories
    """
    story = models.ForeignKey(
        Story, on_delete=models.CASCADE, related_name="comments")
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"