from django import forms
    
class TweetInput(forms.Form):
    tweet = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":100}))

    class Meta:
        fields = ['tweet'] 