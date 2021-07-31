from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
        #UpdateForm 에서 username이 변경되지 못하도록 설정한 후 AccountUpdateForm으로 변경해준다#