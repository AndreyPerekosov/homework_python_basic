from django import forms


class CalcForm(forms.Form):
    token = forms.CharField(label='Your token', max_length=200)
    months = forms.IntegerField(label='Calc period - number of months')
    number_iter = forms.IntegerField(label='Enter number of iter')
    risk = forms.FloatField(label='Enter free risk rate, %')

