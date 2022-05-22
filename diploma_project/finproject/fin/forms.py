from django import forms


class CalcForm(forms.Form):
    token = forms.CharField(label='Your token', max_length=100)
    period = forms.IntegerField(label='Calc period - number of months')

