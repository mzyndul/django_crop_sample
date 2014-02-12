import StringIO
from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile
from crop_widget.models import Profile, AVATAR_SIZE
from PIL import Image


class ProfileForm (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['avatar_x'].widget = forms.HiddenInput()
        self.fields['avatar_y'].widget = forms.HiddenInput()
        self.fields['avatar_width'].widget = forms.HiddenInput()
        self.fields['avatar_height'].widget = forms.HiddenInput()

    def save(self, commit=True):
        obj = super(ProfileForm, self).save()
        print obj.__dict__
        print obj.image.file.name

        img = Image.open(obj.image.file.name)
        img = img.crop((obj.avatar_x, obj.avatar_y, obj.avatar_x+obj.avatar_width,  obj.avatar_y+obj.avatar_height))
        img = img.resize(AVATAR_SIZE, Image.ANTIALIAS)
        tempfile_io = StringIO.StringIO()
        img.save(tempfile_io, format='JPEG')
        image_file = InMemoryUploadedFile(tempfile_io, None, 'abc.jpg', 'image/jpeg', tempfile_io.len, None)
        obj.avatar.save('abc.jpg', image_file)
        obj.save()
        return obj

    class Meta:
        model = Profile
        fields = ('avatar_x', 'avatar_y', 'avatar_height', 'avatar_width', 'image')
