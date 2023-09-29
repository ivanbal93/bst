from django import forms


class NewRobotForm(forms.Form):
    """
    Форма для создания объектов класса "Robot"
    """
    serial = forms.CharField(max_length=5)
    model = forms.CharField(max_length=2)
    version = forms.CharField(max_length=2)
    created = forms.DateTimeField()
