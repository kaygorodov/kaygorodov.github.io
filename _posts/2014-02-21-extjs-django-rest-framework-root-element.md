---
layout: post
title: How to Add the Root Element to Django-Rest-Framework Responses
---

Because I use Ext JS on the project I work on, for a special reason (Ext JS proxy) I need a root element in some DRF-responses.

The following code shows how I've implemented it by defining the custom renderer class. It also works well with paginated view classes.

<script src="https://gist.github.com/kaygorodov/9121640.js"></script>

Here we set the renderer class to the particular view:

<script src="https://gist.github.com/kaygorodov/9121799.js"></script>

Additionally, I don't want to have such root element when I work with DRF in my tests, in order to achieve it, I use the following TestCase:

<script src="https://gist.github.com/kaygorodov/9122205.js"></script>

Good luck!