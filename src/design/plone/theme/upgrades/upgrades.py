# -*- coding: utf-8 -*-
from plone import api
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces.controlpanel import IImagingSchema
from design.plone.theme import logger
from design.plone.theme.controlpanel.interfaces import IDesignPloneThemeSettings  # noqa
from zope.component import getUtility


DEFAULT_PROFILE = 'profile-design.plone.theme:default'


def import_registry(registry_id, dependencies=False):
    setup_tool = api.portal.get_tool('portal_setup')
    setup_tool.runImportStepFromProfile(DEFAULT_PROFILE, registry_id,
                                        run_dependencies=dependencies)


def import_css_registry(context):
    'Import CSS registry configuration'
    logger.info('Importing CSS registry configuration for ' +
                'design.plone.theme')
    import_registry('cssregistry')


def import_js_registry(context):
    'Import js registry configuration'
    logger.info('Importing js registry configuration for ' +
                'design.plone.theme')
    import_registry('jsregistry')


def import_actions_registry(context):
    'Import actions registry configuration'
    logger.info('Importing actions registry configuration for ' +
                'design.plone.theme')
    import_registry('actions')


def import_types_registry(context):
    'Import types registry configuration'
    logger.info('Importing types registry configuration for ' +
                'design.plone.theme')
    import_registry('typeinfo')


def import_viewlets_registry(context):
    'Import viewlets registry configuration'
    logger.info('Importing viewlets registry configuration for ' +
                'design.plone.theme')
    import_registry('viewlets')


def import_properties_registry(context):
    'Import properties registry configuration'
    logger.info('Importing properties registry configuration for ' +
                'design.plone.theme')
    import_registry('propertiestool')


def import_records_registry(context):
    'Import records and settings'
    logger.info('Importing records and settings configuration for' +
                'design.plone.theme')
    import_registry('plone.app.registry')


def remove_ellipsed(context):
    'Import the removeellipsed profile'
    setup_tool = api.portal.get_tool('portal_setup')
    setup_tool.runImportStepFromProfile(
        'profile-design.plone.theme:removeellipsed',
        'plone.app.registry',
        run_dependencies=False
    )


def remove_old_bundle(context):
    'Import the removeoldbundle profile'
    setup_tool = api.portal.get_tool('portal_setup')
    setup_tool.runImportStepFromProfile(
        'profile-design.plone.theme:removeoldbundle',
        'plone.app.registry',
        run_dependencies=False
    )


def changenewshome(context):
    'Import the changenewshome profile'

    registry = getUtility(IRegistry)
    settings = registry.forInterface(
                    IImagingSchema,
                    prefix='plone',
                    check=False
                )

    allowed_sizes = [x for x in settings.allowed_sizes if 'newshome' not in x]
    allowed_sizes.append(u'newshome 450:300')

    settings.allowed_sizes = allowed_sizes


def clean_follow_us_fields(context):
    remove_fields = [
        'header_facebook_link',
        'header_youtube_link',
        'header_twitter_link'
    ]
    registry = getUtility(IRegistry)
    for field in remove_fields:
        try:
            del registry.records['{0}.{1}'.format(
                IDesignPloneThemeSettings.__identifier__,
                field
            )]
        except KeyError:
            # entry not present in registry
            continue
    import_records_registry(context)


def fix_default_header_links(context):
    header_link_label = api.portal.get_registry_record(
        'header_link_label',
        interface=IDesignPloneThemeSettings)
    header_link_url = api.portal.get_registry_record(
        'header_link_url',
        interface=IDesignPloneThemeSettings)
    if not header_link_label:
        api.portal.set_registry_record(
            'header_link_label',
            u'Governo Italiano',
            interface=IDesignPloneThemeSettings)
    if not header_link_url:
        api.portal.set_registry_record(
            'header_link_url',
            'http://www.governo.it',
            interface=IDesignPloneThemeSettings)