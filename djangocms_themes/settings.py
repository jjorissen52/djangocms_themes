import os, configparser, socket
from django.utils.translation import ugettext_lazy as _
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THEME = "axiom"
THEME_DIR = os.path.join(BASE_DIR, 'djangocms_themes', 'private_themes', THEME)
SECRET_KEY = 12
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'djangocms_themes.urls'
WSGI_APPLICATION = 'djangocms_themes.wsgi.application'
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = os.path.join(DATA_DIR, 'djangocms_themes', 'media')
STATICFILES_DIRS = (
    os.path.join(THEME_DIR, 'static'),
    os.path.join(THEME_DIR, 'assets'),
    os.path.join(BASE_DIR, 'node_modules'),
)
print(STATICFILES_DIRS)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)
INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_column',
    'djangocms_link',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_utils',
    'cmsplugin_cascade',
    'cms',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',
    'djangocms_themes',
    # 'storages',
    'zappa_django_utils',
)
LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)
CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

SITE_ID = 1
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(THEME_DIR, 'templates'),
            # os.path.join(BASE_DIR, 'djangocms_themes', 'themes', 'base', 'templates'),
         ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
                # 'djangocms_themes.contextprocessors.theme_color',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]
THEME_COLOR = 'blue'
THEME_TEMPLATES = os.path.join(THEME_DIR, 'templates')
CMS_TEMPLATES = (
    tuple(map(lambda x: (x, x), set(os.listdir(THEME_TEMPLATES)) - {'base.html', 'menu'}))
)

CMS_PERMISSION = True
CMSPLUGIN_CASCADE_PLUGINS = ['cmsplugin_cascade.bootstrap3']
CMSPLUGIN_CASCADE_PLUGINS.append('cmsplugin_cascade.generic')
CMSPLUGIN_CASCADE_PLUGINS.append('cmsplugin_cascade.icon')

CMSPLUGIN_CASCADE = {
    'bootstrap3': {
        'breakpoints': (
            ('xs', (768, 'mobile-phone', _("mobile phones"), 750, 768)),
            ('sm', (768, 'tablet', _("tablets"), 750, 992)),
            ('md', (992, 'laptop', _("laptops"), 970, 1200)),
            ('lg', (1200, 'desktop', _("large desktops"), 1170, 2500)),
            # ('xl', (1600, 'desktop icon-large', _("xlarge desktops"), 1570, 8000)),
        ),
    }
}
CMS_PLACEHOLDER_CONF = {
    'Main Content Placeholder': {
        'plugins': ['BootstrapContainerPlugin'],
        'text_only_plugins': ['TextLinkPlugin'],
        'parent_classes': {'BootstrapContainerPlugin': None},
        'glossary': {
            'breakpoints': ['xs', 'sm', 'md', 'lg'],
            'container_max_widths': {'xs': 750, 'sm': 750, 'md': 970, 'lg': 1170},
            'fluid': False,
            'media_queries': {
                'xs': ['(max-width: 768px)'],
                'sm': ['(min-width: 768px)', '(max-width: 992px)'],
                'md': ['(min-width: 992px)', '(max-width: 1200px)'],
                # 'lg': ['(min-width: 1200px)'],
            },
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'djangocms_themes.db',
    }
}


MIGRATION_MODULES = {
    
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)
