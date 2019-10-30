from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic
from django.http import Http404
from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.
class ProfileDetail(generic.ListView):
    model = UserProfile
    template_name = 'userprofile/profile_detail.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class ProfileUpdate(LoginRequiredMixin, generic.UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name_suffix = '_form'
