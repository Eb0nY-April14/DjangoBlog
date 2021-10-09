from .models import Comment
from django import forms


# This tells our comment form what model to use & which
# fields we want displayed on our form which in this case
# is the 'body'. It is very important to put this trailing
# comma at the end of 'body' or else Python will read it as
# a string instead of a tuple & that will cause an error.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
