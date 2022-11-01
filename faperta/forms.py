from django.forms import ModelForm
from faperta.models import DOSEN
from faperta.models import MAHASISWA
from faperta.models import STAF

class FormDOSEN(ModelForm):
    class meta:
        model = DOSEN
        fields = '__all__'

class FormMAHASISWA(ModelForm):
    class meta:
        model = MAHASISWA
        fields = '__all__'

class FormSTAF(ModelForm):
    class meta:
        model = STAF
        fields = '__all__'