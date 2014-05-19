from django import forms

class Units(forms.Form):
	BTC = 'BTC'
	mBTC = 'mBTC'
	DOGE = 'DOGE'

	unit_choices = ((BTC,'BTC'),(mBTC,'mBTC'),(DOGE, 'DOGE'),)
	units = forms.ChoiceField(choices=unit_choices)