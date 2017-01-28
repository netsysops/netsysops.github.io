---
title: Automate your network, don't reinvent tools!
permalink: /principles/dont-reinvent/
header:
  teaser: /assets/images/cart-wheel-600x400.png
description: "While it feels great to create things, you might be missing the point of network automation if you are reinventing already existing tools."
---
Creating things feels great, it might be one of the reasons it can be so fun to [write code]({{ site.url }}/skills/writing-code/). You can feel tempted to improve everything, automate all the things and all that, there are a few things that you shouldn't do.

### Reinventing the wheel
Even though you might prefer [one solution]({{ site.url }}/toolkit/ansible/) over [the other]({{ site.url }}/toolkit/salt/), neither of them might work exactly like you want them to do. It could be that the [network library]({{ site.url }}/toolkit/napalm/) you are using doesn't return the data in the exact format you need it.

So what do you do about it? It can be tempting to set your [Python skills]({{ site.url }}/toolkit/python/) to use and write the whole solution **exactly** as you want it to be. It would be just **perfect** for your organization. While you should [keep improving]({{ site.url }}/principles/iterate/), you must also ask yourself what your actual goal is.

Is your goal to create the tool of all tools, or is it to automate your network? If your goal is to save time it just doesn't make any sense to spend your time rewriting tools which already exists.

Of course this idea isn't limited to full blown tools. If a library exists which basically does what you need, don't write your own copy of that library.

Spending extra time recreating things is one issue. The bigger problem is that of maintaining the thing you created.

### A troubled history
While we have the best buzzwords ever, SDN, serverless, OpenXYZ and such, network automation is nothing new. People were automating networks with Perl and [pushing config]({{ site.url }}/principles/push-config/) to devices in the nineties. This was however problematic, we are still complaining about the way many systems lack a proper API, but at that time it was much worse. Screen scraping was the only way to do, things like [change verification]({{ site.url }}/principles/verify-changes/) was much harder. People didn't talk about [abstracting the configuration]({{ site.url }}/principles/abstract/) or [owning the configuration]({{ site.url }}/principles/own-your-config/).

A bigger problem though was the legacy of those early automation system, often they were tied to the individual who created them. These tools tented to fall into oblivion after that person moved to another organization. It could also be that the tool which once served the organization so well now held them back since no one knew how to change it.

During that time a lot of people kept reinventing the wheel all the time as many organizations were solving the same kind of problems. While Sourceforge was launched in 1999 and made it easy to [share source code]({{ site.url }}/principles/have-fun/) it wasn't really easy to collaborate with the code. GitHub really changed when they launched in 2008 and soon replaced Sourceforge as the most popular repository for code in the world. As these changes have made it much easier to create projects with others a lot of new tools have also been launched since.

Today it makes more sense for you to use the code others have created instead of trying to write it by yourself.

### More code more problems
Aside from spending your time to write your own versions of the tools, as stated earlier the biggest problem is them maintaining your code. Of course your work should live on within your organization after you leave, but you you also have to maintain your code. More lines of code leads to more bugs. If you instead use existing tools there's a better chance on that code being tested and you can focus on [testing changes to your network]({{ site.url }}/principles/testing/) and the code you need, instead of testing the code for your new tool or library.

### A better solution
A better way if the tool you want to use doesn't fit your needs is to work with the maintainer of that project and improve it that way.
