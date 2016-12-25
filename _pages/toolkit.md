---
title: "Network Automation Toolkit"
layout: splash
permalink: /toolkit/
excerpt: ""

intro:
  - excerpt: 'This is the toolkit'
    title: "Network Automation toolkit"


ansible:
  - title: "Ansible"
    image_path: /assets/images/ansible-600x400.png
    alt: "Ansible"
    excerpt: 'Ansible is an IT-automation framework'
    url: "/toolkit/ansible/"
    btn_label: "Read more"
    btn_class: "btn--inverse"


git:
  - title: "Git"
    excerpt: 'Git the VCS'
    url: "/toolkit/git/"
    btn_label: "Read more"
    btn_class: "btn--inverse"


napalm:
  - title: "Napalm"
    image_path: /assets/images/napalm-logo-600x400.png
    alt: "Napalm"
    excerpt: 'Napalm is a vendor neutral abstraction library for network devices'
    url: "/toolkit/napalm/"
    btn_label: "Read more"
    btn_class: "btn--inverse"


python:
  - title: "Python"
    excerpt: 'Develop your own integrations'
    url: "/toolkit/python/"
    btn_label: "Read more"
    btn_class: "btn--inverse"


salt:
  - title: "Salt"
    excerpt: 'Automation at scale'
    url: "/toolkit/salt/"
    btn_label: "Read more"
    btn_class: "btn--inverse"

stackstorm:
  - title: "Stackstorm"
    excerpt: 'Event-based automation.'
    url: "/toolkit/stackstorm/"
    btn_label: "Read more"
    btn_class: "btn--inverse"


---

{% include feature_row id="intro" type="center" %}

{% include feature_row id="ansible" type="right" %}
{% include feature_row id="git" type="left" %}
{% include feature_row id="napalm" type="right" %}
{% include feature_row id="python" type="left" %}
{% include feature_row id="salt" type="right" %}
{% include feature_row id="stackstorm" type="left" %}
