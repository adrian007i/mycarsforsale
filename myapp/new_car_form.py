from django import forms
from myapp.models import UserInfo,CarInfo,BlogTopics

class UserInfoForm (forms.ModelForm):
    class Meta():
        model=UserInfo
        fields='__all__'

class CarInfoForm(forms.ModelForm):
    class Meta():
        model=CarInfo
        fields=('license_no','make','model','year','color','engine','millage','trans','price','owner','car_image_1','car_image_2','car_image_3')


class BlogTopicsForm (forms.ModelForm):
    class Meta():
        model=BlogTopics
        fields=('title','text','author')
