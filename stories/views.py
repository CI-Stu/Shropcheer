from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Story
from .forms import CommentForm, StoryForm


# Create your views here.


class StoryList(generic.ListView):
    queryset = Story.objects.all()
    template_name = "stories/index.html"
    paginate_by = 6


def story_detail(request, slug):
    """
    Display an individual :model:`stories.Story`.

    **Context**

    ``post``
        An instance of :model:`stories.Story`.

    **Template:**

    :template:`stories/story_detail.html`
    """

    queryset = Story.objects.all()
    story = get_object_or_404(queryset, slug=slug)
    comments = story.comments.all().order_by("created_on")
    comment_count = story.comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.name = request.user
            comment.story = story
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment posted - thank you for sharing'
    )


    comment_form = CommentForm()

    return render(
        request,
        "stories/story_detail.html",
        {
            "story": story,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

class AddStory(LoginRequiredMixin, CreateView):
    """Add a story"""
    template_name = 'stories/add_story.html'
    model = Story
    form_class = StoryForm
    success_url= '/'
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Story added successfully')
        return super().form_valid(form)

