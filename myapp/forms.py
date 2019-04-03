from django import forms

class FormName(forms.Form):

    MAKE = ('','NISSAN','TOYOTA','HONDA','MAZDA','Suzuki','BMW','Porsche','FORD',
    'AUDI','HYUNDAI',' Mitsubishi','OTHER')
    TRANS=('','AUTOMATIC','MANUAL','TIPTRONIC','5 FORWARD')

    MAKE=forms.ChoiceField(choices=[(x, x) for x in MAKE])
    TRANSMISSION=forms.ChoiceField(choices=[(x, x) for x in TRANS])
    ASKING_MIN=forms.ChoiceField(choices=[(x, x) for x in range(0, 250000,25000)])
    ASKING_MAX=forms.ChoiceField(choices=[(x, x) for x in range(0, 1000000,100000)])
