---
layout: post
title: Models
permalink: /models/
---

back to [home](home)

{% for model in site.data.models %}
{% if model.pages.size == 1 %}
# [{{model.name}}]({{model.dirname}}/{{model.pages[0].page}})
{% else %}
# [{{model.name}}]({{model.dirname}})
{% endif %}
{% endfor %}

back to [home](home)
