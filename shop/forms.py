from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (
            'name',
            'rating',
            'comments',
        )

    def save(self, commit=True):
        feedback = super(FeedbackForm, self).save(commit=False)
        feedback.name = self.cleaned_data['name']
        feedback.rating = self.cleaned_data['rating']
        feedback.comments = self.cleaned_data['comments']

        if commit:
            feedback.save()
        return feedback
