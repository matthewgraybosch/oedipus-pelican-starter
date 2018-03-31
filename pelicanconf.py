#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

BUILD_DATE = date.today()
START_YEAR = 1996
BUILD_YEAR = date.today().year
AUTHOR = 'Matthew Graybosch'
AUTHOR_EMAIL = 'public@matthewgraybosch.com'
AUTHOR_MASTODON = 'https://octodon.social/@starbreaker'
AUTHOR_LOCATION = 'Harrisburg, PA'
SITENAME = 'Matthew Graybosch'
SITESUBTITLE = 'a science fantasy author, developer, and metalhead with delusions of erudition'
SITEURL = ''
SITE_GENERATOR = 'Pelican 3.7.1 on OpenBSD -current'

SITE_BLOG_NAME = 'A Day Job and a Dream'
SITE_BLOG_DESC = 'When most writers start out, a day job and a dream is all they have. Even now, it is all I need to tell my story.'
SITE_OG_IMAGE = '/images/author-nyc.jpg'

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%d %B %Y'
LOCALE = 'en_US'
LOAD_CONTENT_CACHE = False
ARTICLE_EXCLUDES = ['drafts']
GITHUB_URL = 'https://github.com/matthewgraybosch/pelican.matthewgraybosch.com'

# Take advantage of the following defaults
STATIC_PATHS = [
    'images',
    'files',
]

EXTRA_PATH_METADATA = {
    'files/robots.txt': {'path': 'robots.txt'},
    'files/humans.txt': {'path': 'humans.txt'},
    'files/favicon.ico': {'path': 'favicon.ico'},
    'files/.htaccess': {'path': '.htaccess'},
}

# If you're a schmuck who still depends on Facebook, 
# you might want to set this. Otherwise, leave it blank.
FB_APP_ID = ''

# Plugin settings
PLUGIN_PATHS = ['/home/demifiend/documents/pelican.matthewgraybosch.com/pelican-plugins/']
PLUGINS = ['better_figures_and_images',
           'sitemap']

# Setting for the better_figures_and_images plugin
RESPONSIVE_IMAGES = True

# Setting for the better_figures_and_images plugin
FIGURE_NUMBERS = True

# Theme settings
THEME = "oedipus"

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Misc'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
SHOW_POST_CATEGORY = True
SHOW_POST_TAGS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Smart quotes and other things
TYPOGRIFY = True
# Stop putting &nbsp; in the fucking article titles
TYPOGRIFY_IGNORE_TAGS = [
    'pre', 'code', 'header', 'h1', 'h2', 'h3', 'aside',
]

# Custom nav menus for motherfucker theme
HEADER_NAV_MENU = (('Home', '/'),
                   ('About', '/about/'),
                   ('Projects', '/projects/'),
                   ('Blog', '/blog/'),)

FOOTER_NAV_MENU = (('Colophon', '/colophon/'),
                   ('Subscribe', '/subscribe/'),
                   ('Categories', '/blog/categories/'))

# More custom lists for my fiction.

FICTION = (('WIP', '<em>Shattered Guardian</em>', '#'),
		   ('2016', '<em>Silent Clarion</em>', '#'),
		   ('2015', '&quot;Limited Liability&quot;', '#'),
		   ('2014', '&quot;Steadfast&quot;', '#'),
		   ('2013', '<em>Without Bloodshed</em>', '#'),
		   ('2013', '&quot;The Milgram Battery&quot;', '#'),
		   ('2012', '&quot;The Holiday Rush&quot;', '#'),
		   ('2012', '&quot;Tattoo Vampire&quot;', '#'),
		   ('2009', '<em>Starbreaker</em>', '#'),)

DEFAULT_PAGINATION = 15

# For the landing page
TEMPLATE_PAGES = {
    '../oedipus/templates/home.html': 'index.html',
}

# Domains to DNS-prefetch for better performance.
DNS_PREFETCH_DOMAINS = ('www.youtube.com',
                        'www.youtube-nocookie.com',
                        's.ytimg.com',
                        'i.ytimg.com',
                        'www.google.com',)

# URL settings
ARCHIVES_URL = 'blog/archives/'
ARCHIVES_SAVE_AS = 'blog/archives/index.html'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
CATEGORIES_URL = 'blog/categories/'
CATEGORIES_SAVE_AS = 'blog/categories/index.html'
CATEGORY_URL = 'blog/category/{slug}/'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'
INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = 'blog/'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAGS_URL = 'blog/tags/'
TAGS_SAVE_AS = 'blog/tags/index.html'
TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'

# Sitemap settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
