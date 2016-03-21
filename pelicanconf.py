#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andrey Kaygorodov'
SITENAME = u'Andrey Kaygorodov'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = () 

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['extra/CNAME', 'images']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

THEME = './../voidy-bootstrap/'


SITESUBTITLE ='A Passionate Software Engineer.'
SITETAG = "- a passionate software engineer, geek and just a good man."

# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)

# Put taglist at end of articles, and use the default sharing button implementation.
CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Default sidebar template. Omit this line for single column mode without sidebar.
SIDEBAR = "sidebar.html"

SOCIAL = (('Twitter', 'https://twitter.com/kaygorodov',
           'fa fa-twitter-square fa-fw fa-lg'),
          ('LinkedIn', 'https://linkedin.com/in/kaygorodov',
           'fa fa-linkedin-square fa-fw fa-lg'),
          ('GitHub', 'https://github.com/kaygorodov',
           'fa fa-github-square fa-fw fa-lg'),)
