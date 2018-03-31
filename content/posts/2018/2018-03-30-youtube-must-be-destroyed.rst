YouTube Must Be Destroyed
#########################

:date: 2018-03-30 13:03
:category: Just Tech Things
:summary: If web pages are bloated (and they are), YouTube embeds are one of the biggest culprits. Never embed what you can link!
:tags: web development, front end, web design, youtube, bloat, performance, linking, embedding
:slug: youtube-must-be-destroyed


If you build websites, you really should be testing pages using tools like the one Pingdom_ offers, if only to see just how bloated your pages are in production and where the bloat is coming from.

In the case of a blog post from last year, the page weighs in at 601KB total. That might be respectable by current standards, given the `website obesity crisis <http://idlewords.com/talks/website_obesity.htm>`_. I suspect that anybody stuck on dialup or using a metered mobile data connection would still find 601KB for a blog post unacceptable. 

Where does the bloat come from? It comes from a YouTube embed. `See for yourself <https://tools.pingdom.com/#!/cyHrzi/https://www.matthewgraybosch.com/blog/2017/09/15/mid-september-update-small-dark-Lines/>`_.

We're looking at a total page size of 601.77 KB, of which only 6.27 KB comes from **matthewgraybosch.com**. By way of comparison, `this page <https://tools.pingdom.com/#!/eLLVTo/https://www.matthewgraybosch.com/blog/2018/03/30/youtube-must-be-destroyed/>`_ weighs in at around 6.5KB. 

Where's the rest of it coming from? Here's the breakdown.

========================	=======	=========
Domain                      	Percent Size
========================	=======	=========
s.ytimg.com	                87.4 %	525.82 KB
i.ytimg.com	                4.8 %	29.10 KB
fonts.gstatic.com	        3.3 %	19.88 KB
www.youtube-nocookie.com	2.5 %	15.31 KB
www.matthewgraybosch.com	1.0 %	6.27 KB
www.google.com              	0.9 %   5.38 KB
========================	=======	=========

Most of the data is coming from **s.ytimg.com**, and it's nothing but *JavaScript*. That's right. Google, a megacorporation that supposedly hires the best and brightest developers on earth, needs to shove over 500KB of JavaScript down the pipe just to display a still from a video and a play button.

One hopes that this gets cached so that multiple embeds on a page or on a site can reuse it, but I doubt it. I don't think anybody at Google cares that much, or remembers what it was like to surf the web on a 56K dialup connection.

This is why YouTube must be destroyed. Preferably along with the rest of Alphabet, including Google. In the meantime, we need a better way to include multimedia content.

Hyperlinks to the Rescue
========================

If you want fast pages, never embed anything from other sites just because you can. Think before embedding video or audio.

If you absolutely must have images on your page, optimize the living hell out of them. If they look crappy afterward, wrap the image tag in a link to the original. 

However, it's much harder to optimize audio and video content than it is to optimize images. If your only concerns are speed and size, you might be better off linking.

However, there's a trade-off. If people click links to view multimedia content, they're leaving your page and must decide to come back once they're done. Given the algorithms sites like YouTube use to keep viewers from leaving, you might be better off taking the performance hit and embedding videos on your pages.

The upside to linking is that if the target is removed, the other site looks bad instead of yours.

Middle Ground?
==============

Somebody on the Fediverse `suggested another way <https://friendica.mrpetovan.com/display/735a2029155abe7d3f72bf4237393497>`_:

    The middle ground we found at #Friendica is to put the Youtube embed behind a click. If you don’t click, nothing is loaded.

    --hypolite@friendica.mrpetovan.com

If you have other suggestions, try replying to `my toot on Mastodon <https://octodon.social/@starbreaker/99774132808363818>`_

.. _Pingdom: https://tools.pingdom.com
