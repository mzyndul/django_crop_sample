from django.views.generic import ListView, CreateView, UpdateView
from crop_widget.models import Profile, AVATAR_SIZE
from crop_widget.forms import ProfileForm
from crop_widget.utils import aspect_ratio


class ProfileListView(ListView):
    model = Profile


class BaseProfileViewMixin(object):
    def get_context_data(self, **kwargs):
        context = super(BaseProfileViewMixin, self).get_context_data(**kwargs)
        context['aspect_ratio'] = aspect_ratio(AVATAR_SIZE[0], AVATAR_SIZE[1])
        return context


class ProfileCreateView(BaseProfileViewMixin, CreateView):
    form_class = ProfileForm
    model = Profile

    def form_valid(self, form):
        return super(ProfileCreateView, self).form_valid(form)


class ProfileUpdateView(BaseProfileViewMixin, UpdateView):
    form_class = ProfileForm
    model = Profile

