---
title: Why Bother with network automation?
permalink: /principles/why-bother/
header:
  teaser: /assets/images/why-bother-600x400.png
description: "Why should you learn about network automation? How will not learning it impact you? Is it as hard as it's made out to be?"
---
You have heard the standard reasons for network automation; It saves time, does what it's told to do, is consistent, doesn't complain. It's hard to argue against network automation as a concept. The question is how does this impact you? Why should you bother to learn about network automation.

### Looking ahead
The thing to consider is how you will be impacted if you don't learn to automate your network. If you imagine that things evolve towards more automation and that the cli is more or less abandoned, how will that change your day to day work.

For junior people starting out you might be sitting somewhere today having a day job consisting of making acl changes to firewalls, or adding and removing bgp peers. As the network automation system gets [exposed through an api]({{ site.url }}/principles/expose/) to the rest of your organization, there's a very good possibility that your current job just won't exist in a few years time. Junior people shouldn't worry to much about this, as long as you have a mindset to continue learning new things. The dangers instead are to those who've been stuck in their current skill level for a few years, if you are in this position it's time to wake up. The sad part of course is that those kind of people usually don't try to find this kind of information in books or online. So if you have been stuck doing the same thing for some time, you're probably better off than others in a similar situation.

At the other end of the spectrum we have the network architects or designers. If you are in this category you might not configure any actual devices anymore. Do you have to care about network automation? Well for starters, there's a good chance that it will impact your HLD and LLD. Taking a step back it's hard to design for something when you don't have a good understanding of how it will be operated or in what way the network will be [integrated to other systems]({{ site.url }}/skills/whole-system/).

### What is needed
Regardless if you are new to the industry or an old networking veteran, having a fundamental knowledge about [how networking works]({{ site.url }}/skills/foundation/) has been, and will remain, crucial in order to understand what you are doing. It's just common sense that it's valuable to know how the things you are trying to automate actually works. Learning new skills have always been a part of this industry, protocols evolve, features are added and old technology has died. In that regard not much changes when it comes to network automation, it's just more things to learn.

A difference is however is [the skill set]({{ site.url }}/skills/). While you don't need any specific skills to use network automation, to really understand it you will need to learn things which traditionally was the server admins or [developers domain]({{ site.url }}/skills/version-control/).

Your latest router might have a Linux shell which you can access just as a server. While this can be great you might not be able to take advantage of it if you don't know the [basics of Linux]({{ site.url }}/skills/linux/).

### Overwhelmed

Looking at the tools and skillset needed to master network automation can seem very challenging. It used to be so simple, you had your cli or gui. Now people are talking about if the device has a good api. Is it rest-api or something using netconf? It might be one of those awful xml things or perhaps restconf. How does netconf differ from restconf?

Then there's tools like [Ansible]({{ site.url }}/toolkit/ansible/) or [Salt]({{ site.url }}/toolkit/salt/), and [tomorrow it will be something else]({{ site.url }}/skills/future-tools/).

Another thing is called [Napalm]({{ site.url }}/toolkit/napalm/), how is that different from Ansible and Salt? And while no one is asking you do become a full blown developer, learning how to [write some scripts]({{ site.url }}/skills/writing-code/) will enable you to do so much more. But should you learn Golang or [Python]({{ site.url }}/toolkit/python/)? Or perhaps Node.js or Ruby? Will your old Perl knowledge do you any good? As long as you store the code in [Git]({{ site.url }}/toolkit/git/), you are probably fine. Because you know Git right?

### The bright side
While you will hear that it's [all about the data]({{ site.url }}/principles/data/), that you should create a [service catalog]({{ site.url }}/principles/service-catalog/) and [test everyting]({{ site.url }}/principles/testing/), keep in mind that that's in the deep end. You have to [walk]({{ site.url }}/principles/start-simple/) before you can run. Once you have learned the basics, it's just a matter of [evolving]({{ site.url }}/principles/iterate/) one step at a time.

One of the goals of network automation is to save time, your time and the time of your organization. As you learn the ropes don't try to do it [all by yourself]({{ site.url }}/principles/heroism/), chances are you will end up wasting time in the long run. Instead remember to ask for help when you get stuck and perhaps one day you can be the one that gives advice and [shares your knowledge]({{ site.url }}/principles/have-fun/) with the world.
