# Helping out

Want to contribute to the project? Perhaps you've found a typo or some other error. Please submit [a new issue](https://github.com/netsysops/netsysops.github.io/issues/new) or send in a [pull request](https://github.com/netsysops/netsysops.github.io/pulls).

You can also use the issues to suggest content that you would like to read or to write yourself and contribute to the project.

Aside from working with this GitHub repo there are also other ways to [help the project](https://www.netsysops.io/contribute/).

## When contributing

In order to avoid broken links, and make sure the site looks nice when sharing on social media there are a few tests which have to pass before a PR will be considered. More information about these tests will be added later, for now you can take a look in the [.travis.yml](https://github.com/netsysops/netsysops.github.io/blob/master/.travis.yml) file and work from there. Create an issue if you are unsure about what to do.

The controls on the content is more strict for articles which are part of a longer guide or a tutorial like the ones in the [Principles of network automation](https://www.netsysops.io/principles/), the [Skills](https://www.netsysops.io/skills/) or the [Toolkit](https://www.netsysops.io/toolkit/). One such check is the existence of a header teaser image. An example in Patrick Ogenstads [profile page](https://github.com/netsysops/netsysops.github.io/blob/master/_pages/ogenstad.md) looks like this:

``` yaml

header:
  teaser: /assets/images/patrick-ogenstad-600x400.jpg

```

The header teaser image won't be enforced on blog articles. Another check which will be enforced is that of the meta description.

``` yaml

description: "This is the meta description which can show up in search results."

```
The meta description can be seen as an SEO optimization strategy and while you can view it that way it's purpose is to "sell the click", it often shows up in the search results page as a way of describing the page. Aim for this description to be 110-160 characters. Some more information about the meta description along with tips on writing them can be found [here](https://yoast.com/meta-descriptions/).


## Permalinks and naming content

Blog posts (which might not be a part of the site when launching) will be stored under `_posts/[author]/` in the format 2017-01-28-name-of-link.md. This would set creation date for the post and the url to /name-of-link/. For other content you might have to set the link in the metadata. An example would be:

``` yaml

permalink: /principles/start-simple/

```

Some of the [collections](https://jekyllrb.com/docs/collections/) will need to have a permalink set while others don't. For example in the [toolkit](https://www.netsysops.io/toolkit/) the navigation between the tools are in alphabetical order this means that as long as we name the files in the same way as the tool we don't have to enter the permalink. While in the [Principles](https://www.netsysops.io/principles/) the different posts doesn't follow an alphabetical order. That way we need to thing about the order when naming the files. That way 0010-why-bother.md comes before 0020-push.config.md, since we don't want the actual url to be /principles/0010-why-bother/ we need to set the permalinks in those files.

## Basic templates

Most of the content has two sections in each markdown file the first section is for the metadata and the second is for the content.

``` yaml
---
# The Title of the post
title: Don't reinvent
# The actual url which will host the site
permalink: /principles/dont-reinvent/
# Meta description (as described above)
description: "Click here to read about what you shouldn't be doing when automating your network."
# The excerpt can be used on pages which contain archives or listings. It's a short snipped which describes the text.
excerpt: ""
# The teaser image will often be shown when sharing the page on social media sites
header:
  teaser: /assets/images/cart-wheel-600x400.png
---
This is where you write the content. When linking internally it can help to use the format "{{ site.url }}/destination", that way the links work even if you are testing the site locally from your computer.

```

The Netsysops website is built using the Minimal Mistakes Jekyll theme. For more information about using metadata and creating content take a look at the [guides](https://mmistakes.github.io/minimal-mistakes/) on that site. An example of something to use from there could be a header image as in:

``` yaml

header:
  image: /assets/images/hero-background-1900x500.png

```

You might run into features on the Minimal Mistakes site which doesn't work here, that could be due to the fact that we need to merge the changes from the upstream repository.

## Using images

When using images in the content store the images for the pages, tutorials in /assets/images. For blog posts store the images in /images/2017/ (or whichever is the current year).


## Need more help?

If you feel that something is missing from this page please open a [new issue](https://github.com/netsysops/netsysops.github.io/issues/new) and tell us about what's missing.
