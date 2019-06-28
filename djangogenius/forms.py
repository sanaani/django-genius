from django import forms


class GeniusPaymentForm(forms.Form):
    paymentToken = forms.CharField(
        required=True,
        widget=forms.HiddenInput()
    )
