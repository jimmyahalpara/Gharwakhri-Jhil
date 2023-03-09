



# class UserRegistrationForm(forms.Form):
#     username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
#     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
#     email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
#     phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
#     city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City'}))
#     security_question = forms.ChoiceField(choices=[
#         ('', '--Select a security question--'),
#         ('question1', 'Your Favourite Item?'),
#         ('question2', 'Your Favourite Name?'),
#         ('question3', 'Your Favourite Number?'),
#     ], widget=forms.Select(attrs={'class': 'form-select form-select-lg mb-3'}))
#     answer = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Answer'}))
#     role = forms.ChoiceField(choices=[('seller', 'Seller'), ('buyer', 'Buyer')], widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
#     agree_terms = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
