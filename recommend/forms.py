from django import forms

from recommend.models import RecommendModel


class GetRecommendationForm(forms.ModelForm):
    class Meta:
        model = RecommendModel
        fields = (
            'user_id',
            'residing_city',
            'residing_country',
            'total_purchase',
            'total_cost',
        )

    def save(self, commit=True):
        recommend = super(GetRecommendationForm, self).save(commit=False)
        recommend.user_id = self.cleaned_data['user_id']
        recommend.residing_city = self.cleaned_data['residing_city']
        recommend.residing_country = self.cleaned_data['residing_country']
        recommend.total_purchase = self.cleaned_data['total_purchase']
        recommend.total_cost = self.cleaned_data['total_cost']

        if commit:
            recommend.save()
        return recommend
