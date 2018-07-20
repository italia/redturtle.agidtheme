# -*- coding: utf-8 -*-
from ..controlpanel.interfaces import IRedturtleAgidthemeSettings
from ..vocabularies import SHARES
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.layout.viewlets import common as base
from plone.app.layout.viewlets.common import SearchBoxViewlet
from plone.app.layout.viewlets.content import DocumentBylineViewlet
from plone.app.multilingual.browser.selector import LanguageSelectorViewlet
from Products.CMFPlone.utils import getSiteLogo
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from urllib2 import quote

import logging

logger = logging.getLogger(__name__)

socialCSSClassDict = {
    'facebook': 'fab fa-facebook-f',
    'twitter': 'fab fa-twitter',
    'instagram': 'fab fa-instagram',
    'telegram': 'fab fa-telegram',
    'youtube': 'fab fa-youtube',
    'linkedin': 'fab fa-linkedin-in',
    'medium': 'fab fa-medium-m',
    'newsletter': 'far fa-newspaper',
    'rss': 'fas fa-rss',
    'google': 'fab fa-google-plus-g',
    'pinterest': 'fab fa-pinterest',
    'flickr': 'fab fa-flickr',
    'pocket': 'fab fa-get-pocket',
}


class CustomDocumentBylineViewlet(DocumentBylineViewlet):

    index = ViewPageTemplateFile('templates/document_by_line.pt')

    def show(self):
        # always show: anonymous need to see some infos
        return True

    def creator(self):
        """ show creator infos only for authenticated users """
        return not self.anonymous and self.context.Creator() or ''


class SocialViewlet(base.ViewletBase):
    def __init__(self, context, request, view, manager):
        super(SocialViewlet, self).__init__(context, request, view, manager)

    def render(self):
        """
        """
        allowed_types = api.portal.get_registry_record(
            'available_types', interface=IRedturtleAgidthemeSettings)
        if self.context.portal_type in allowed_types:
            return self.index()
        return ''

    def get_socials(self):
        socials = api.portal.get_registry_record(
            'available_socials', interface=IRedturtleAgidthemeSettings)
        return socials

    def get_css_class(self, social_type):
        cssClass = SHARES[social_type]['cssClass']
        return cssClass or ''

    def get_sharer_url(self, social_type):
        share_url = SHARES[social_type]['share_url']
        title = quote(self.context.title.encode('utf-8'))
        item_url = self.context.absolute_url()
        if social_type == 'linkedin':
            return share_url.format(item_url, title)
        if social_type == 'twitter':
            return share_url.format(item_url, title)
        if social_type == 'pinterest':
            return share_url.format('', item_url, 'false', title)
        if social_type == 'pocket':
            return share_url.format(item_url, title)
        return share_url.format(item_url)


class LogoViewlet(base.ViewletBase):
    index = ViewPageTemplateFile('templates/logo.pt')

    def update(self):

        super(LogoViewlet, self).update()
        self.site_title = api.portal.get_registry_record('plone.site_title', )

        # TODO: should this be changed to settings.site_title?  # noqa
        self.navigation_root_title = self.site_title
        self.logo_title = self.site_title
        self.img_src = getSiteLogo()


class HeaderSocialViewlet(base.ViewletBase):
    '"Follow us" viewlet'
    index = ViewPageTemplateFile('templates/header_social_viewlet.pt')

    def get_links_list(self):
        try:
            return api.portal.get_registry_record(
                'follow_us_links', interface=IRedturtleAgidthemeSettings)
        except InvalidParameterError:
            return []

    def get_social_links(self):
        links = self.get_links_list()
        res = []
        for link in links:
            try:
                social, url = link.split('|')
                cssClass = socialCSSClassDict.get(social.strip(), '')
                res.append({'id': social, 'url': url, 'cssClass': cssClass})
            except ValueError:
                logger.warning(
                    '[HeaderSocialViewlet] - skipped entry "{0}"'
                    ' because is malformed. Check it in control panel.')
                continue
        return res


class SkipLinksViewlet(base.ViewletBase):
    'Skiplinks viewlet'
    index = ViewPageTemplateFile('templates/skip_links_viewlet.pt')


class AgidSearchBoxViewlet(SearchBoxViewlet):
    """ Search viewlet """
    index = ViewPageTemplateFile('templates/searchbox.pt')


class HeaderBannerViewlet(LanguageSelectorViewlet):
    """ Header banner viewlet """

    def update(self):
        super(HeaderBannerViewlet, self).update()

        self.header_second_link_url = api.portal.get_registry_record(
            'header_second_link_url', interface=IRedturtleAgidthemeSettings)

        self.header_link_label = api.portal.get_registry_record(
            'header_link_label', interface=IRedturtleAgidthemeSettings)

        self.header_link_url = api.portal.get_registry_record(
            'header_link_url', interface=IRedturtleAgidthemeSettings)

        self.header_second_link_label = api.portal.get_registry_record(
            'header_second_link_label', interface=IRedturtleAgidthemeSettings)

    def showLanguageSelector(self):
        return (self.header_link_label and self.header_link_url) or (
            self.header_second_link_url
            and self.header_second_link_url) or self.available()
