#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

BUILD_DATE = date.today()
START_YEAR = date.today().year
BUILD_YEAR = date.today().year
AUTHOR = 'Your Name Here'
AUTHOR_URL = 'Your URL Here'
AUTHOR_EMAIL = 'Your Email Here'
AUTHOR_MASTODON = 'If you don\'t know what this is, go to https://joinmastodon.org. Otherwise, use your profile URL, not just your handle.'
AUTHOR_LOCATION = 'Your Home City/Country'
SITENAME = 'Oedipus'
SITESUBTITLE = 'Build your own motherfucking website with Pelican. Patricide optional.'
SITEURL = ''
SITE_GENERATOR = 'Pelican 3.7.1 on OpenBSD -current'

SITE_BLOG_NAME = 'Patricidal Motherfucker'
SITE_BLOG_DESC = 'This is the personal blog of King Oedipus of Thebes, as dictated to his daughter Antigone.'

SITE_OG_IMAGE = '/images/carole-radatto-oedipus-and-sphinx.jpg'
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%d %B %Y'
LOCALE = 'en_US'
LOAD_CONTENT_CACHE = False
ARTICLE_EXCLUDES = ['drafts']
GITHUB_URL = 'https://github.com/matthewgraybosch/oedipus-pelican-starter'

ICON_URL = 'icon.png'
FAVICON_URL = 'favicon.ico'

# If you're a schmuck who still depends on Facebook, 
# you might want to set this. Otherwise, leave it blank.
FB_APP_ID = ''

# Plugin settings
PLUGIN_PATHS = ['~/git/oedipus-pelican-starter/pelican-plugins/']
PLUGINS = ['readtime', 'sitemap']

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
                   ('Blog', '/blog/'),)

FOOTER_NAV_MENU = (('Colophon', '/colophon/'),
                   ('Subscribe', '/subscribe/'),
                   ('Categories', '/blog/categories/'),)

DEFAULT_PAGINATION = 15

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
JSON_FEED_URL = 'feeds/feed.json'
JSON_FEED_COMMENT = 'Use this to read posts from this site in any feed reader that supports JSON feeds. Just copy the URL and paste it into your reader\'s feed URL field. It\'s almost as easy as Atom or RSS.'

# These variables are for generating ActivityPub data similar to a RSS/Atom/JSON feed.
# AP_PROFILE* variables refer to the "Actor" object (https://www.w3.org/TR/activitypub/#actor-objects).
# Valid values for AP_PROFILE_TYPE include 'Application', 'Group', 'Organization', 'Person',  and 'Service'
AP_PROFILE_TYPE = 'Application'
# The profile.json file ties everything together. When first joining a syndication site that uses ActivityPub
# the POSSE daemon should pull the original files from your website. You should then change the URLs
# for everything but the outbox.json feed to endpoints provided by the POSSE daemon. This lets you write
# JS to render current data (to show likes, mentions, etc) and also allows you to pull data if you want to
# move to a different syndication site or run your own.
AP_PROFILE_URL = 'feeds/ap/profile.json'
AP_FOLLOWING_URL = 'feeds/ap/following.json'
AP_FOLLOWERS_URL = 'feeds/ap/followers.json'
AP_LIKED_URL = 'feeds/ap/liked.json'
AP_INBOX_URL = 'feeds/ap/inbox.json'
AP_OUTBOX_URL = 'feeds/ap/outbox.json'
AP_PREFERRED_USERNAME = 'oedipus'
AP_NAME = SITENAME
AP_SUMMARY = SITESUBTITLE
AP_ICON = SITE_OG_IMAGE
AP_FOLLOWING_USE_LINKS_LIST = True

# Use this to define additional templates that Pelican doesn't know about by default.
# If you're using ActivityPub templates to implement POSSE support, you should edit your
# Makefile to pull the latest versions of all files but outbox.json and place them
# in the appropriate locations in your content/files directory. Then you
# should remove their entries from TEMPLATE_PAGES and add entries to EXTRA_PATH_METADATA.
TEMPLATE_PAGES = {
    '../oedipus/templates/home.html': 'index.html',
    '../oedipus/templates/feed.json': JSON_FEED_URL,
    '../oedipus/templates/activitypub/actor.json': AP_PROFILE_URL,
    '../oedipus/templates/activitypub/following.json': AP_FOLLOWING_URL,
    '../oedipus/templates/activitypub/followers.json': AP_FOLLOWERS_URL,
    '../oedipus/templates/activitypub/liked.json': AP_LIKED_URL,
    '../oedipus/templates/activitypub/inbox.json': AP_INBOX_URL,
    '../oedipus/templates/activitypub/outbox.json': AP_OUTBOX_URL,
}

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

# Blogroll
LINKS = (('Matthew Graybosch', 'https://www.matthewgraybosch.com/'),
         ('You can modify those links in your config file', '#'),)

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

