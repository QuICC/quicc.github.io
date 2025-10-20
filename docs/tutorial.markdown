---
layout: page
title: Tutorial
permalink: /tutorial/
---

{% for dir in site.data.tutorial %}
{% for page in dir.pages %}
# [{{page.name}}]({{page.page}})
{% endfor %}
{% endfor %}
