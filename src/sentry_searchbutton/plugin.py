import sentry_searchbutton
from django import forms
import urllib
from sentry.plugins import Plugin
from django.utils.translation import ugettext_lazy as _


GOOGLE_URL = "https://www.google.com/search?q="


class SearchButtonForm(forms.Form):
    name = forms.CharField(
        label=_('Search Engine Name'),
        required=False,
        widget=forms.TextInput(attrs={'class': 'span6', 'placeholder': 'Google'}),
        )
    url = forms.CharField(
        label=_('Search Engine URL'),
        required=False,
        widget=forms.TextInput(attrs={'class': 'span6', 'placeholder': GOOGLE_URL}),
        help_text=_("The search URL used by your engine")
        )


class SearchButton(Plugin):
    author = "Timmy O'Mahony"
    author_url = 'https://github.com/timmyomahony/sentry_searchbutton'
    version = sentry_searchbutton.VERSION
    description = "A Sentry extension that introduces a search button for errors"
    resource_links = [
        ('Bug Tracker', 'https://github.com/getsentry/sentry-searchbutton/issues'),
        ('Source', 'https://github.com/getsentry/sentry-searchbutton'),
    ]

    slug = 'searchbutton'
    title = _('Search Button')
    conf_title = title
    conf_key = 'searchbutton'
    project_conf_form = SearchButtonForm

    def widget(self, request, group, **kwargs):
        name = self.get_option("name", group.project)
        if not name:
            name = "Google"
        url = self.get_option("url", group.project)
        if not url:
            url = GOOGLE_URL
        return self.render('searchbutton/widget.html', context={
            'name': name,
            'url': url,
            'value': group.message,
        })
