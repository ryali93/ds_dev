from django.forms import ModelForm
from . models import Review

class ReviewForm(ModelForm):
	
	class Meta(object):
		model = Review
		fields = ['review']