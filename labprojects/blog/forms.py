from django import forms

class CommentForm(forms.Form):
	author = forms.CharField(
		max_length = 60,
		widget = forms.TextInput(attrs={
				"class": "form-control",
				"placeholder": "Su nombre"
			})
		)
	body = forms.CharField(
		widget=forms.Textarea(
			attrs = {
				"class": "form-control",
				"placeholder": "Deje un comentario"

			})
		)

