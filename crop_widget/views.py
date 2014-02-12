from django.views.generic import ListView, CreateView, UpdateView
from crop_widget.models import Profile
from crop_widget.forms import ProfileForm


class ProfileListView(ListView):
    model = Profile


class ProfileCreateView(CreateView):
    form_class = ProfileForm
    model = Profile

    def form_valid(self, form):
        return super(ProfileCreateView, self).form_valid(form)


class ProfileUpdateView(UpdateView):
    form_class = ProfileForm
    model = Profile
