---
title: "How to contribute to the Netsysops website"
layout: single
permalink: /contribute/
description: "Have you found the Netsysops site to be useful to you? Find out how you can help and make it even better!"
author_profile: true
header:
  teaser: /assets/images/contribute-600x400.png
---
If you have found this website useful it would be great if you wanted to help us to improve it and spread the word about the site. There are a number of ways in which you can contribute.

### Suggestions and report errors

It might just be so simple that you want to learn more about a topic. Then you can [create an issue](https://github.com/netsysops/netsysops.github.io/issues) and send us your idea. Other ways to help out would be if you spot any typos, spelling or technical errors. Please create issues for those too.

### Spread the word

Another great way to help is to tell your friends about the website or share the site in your social media channels. If you haven't stared the project on GitHub go ahead and do so!<br />
{::nomarkdown}<iframe style="display: inline-block;" src="https://ghbtns.com/github-btn.html?user=netsysops&repo=netsysops.github.io&type=star&count=true&size=large" frameborder="0" scrolling="0" width="160px" height="30px"></iframe>{:/nomarkdown}

### Contributing to the content of the site

This website is written in Markdown and created using the static site generator [Jekyll](https://jekyllrb.com/), while Jekyll is written in Ruby you don't need to know Ruby in order to use Jekyll. To be able to test things locally you will however need to install Ruby on your machine. In order to setup the required Ruby gems you should also install [Bundler](http://bundler.io/). After that you should be ready to go. Fork and clone the repo then use bundler to install jekyll.

``` bash
bundle install
```

You can then serve the pages locally by running:

``` bash
bundle exec jekyll serve --config=_config.yml,_config-dev.yml
```

This will start a web server running on http://localhost:4000.

If you want to share what you have written you can send it as a [pull request](https://github.com/netsysops/netsysops.github.io/pulls).
