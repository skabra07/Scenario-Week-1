from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=100,widget=forms.TextInput(attrs={'id':'username'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'id':'password'}))    

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'required': 'required'})
        self.fields['password'].widget.attrs.update({'required': 'required'})

class SignUpForm(forms.Form):
    username = forms.CharField(label='Username',max_length=100,widget=forms.TextInput(attrs={'id':'username'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'id':'password'}))
    fname = forms.CharField(label='First Name',max_length=100,widget=forms.TextInput(attrs={'id':'fname'}))
    lname = forms.CharField(label='Last Name',max_length=100,widget=forms.TextInput(attrs={'id':'lname'}))

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'required': 'required'})
        self.fields['password'].widget.attrs.update({'required': 'required',})
        self.fields['fname'].widget.attrs.update({'required': 'required'})
        self.fields['lname'].widget.attrs.update({'required': 'required'})