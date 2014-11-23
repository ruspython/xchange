from django.shortcuts import redirect
from django.views.generic import ListView
from .models import Banner, Referral


class BannerListView(ListView):
    model = Banner
    template_name = 'referal/index.html'
    context_object_name = 'banners'


def banner_click(request, site_owner_id, banner_id):
    banner = Banner.objects.get(pk=banner_id)
    banner_owner = banner.banner_owner
    site_owner = Referral.objects.get(pk=site_owner_id)
    if site_owner == banner.site_owner:
        site_owner.points += 1
        site_owner.save()
        banner_owner.points -= 1
        banner_owner.save()
    return redirect(banner.url)