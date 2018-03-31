Creating a System Serif Font Stack for Web Development
######################################################

:date: 2017-01-24 10:36
:modified: 2017-01-30 11:15
:slug: creating-system-serif-font-stack-web-Development
:category: Just Tech Things
:tags: serif fonts, system font stack, css, web design, front end, web fonts
:summary: An overview of the use of system UI fonts in stylesheets, with ideas on how to do the same with serif and monospace fonts.

Because I do web development at my day job, I try to keep up with the latest trends in web development. One of them is `the use of system user interface (UI) fonts in CSS instead of downloading fonts <https://css-tricks.com/snippets/css/system-font-stack/>`_.

I'd like to tell you a bit about this trend, because I'm rebuilding my personal website using Jekyll_ to get away from Squarespace_, and that means I've got to come up with my own HTML and CSS.

I suppose some context is necessary first.

What is the "system UI font stack"?
===================================

Ire Aderinokun describes and compares stacks used by WordPress_, Medium_, Ghost_ (not the band), and GitHub_ in `"The New System Font Stack?" <https://bitsofco.de/the-new-system-font-stack/>`_. Toward the end, she recommends using WordPress' set, implemented as follows:

.. code:: css

    body {  
        font-family: -apple-system,
                     BlinkMacSystemFont,  
                     "Segoe UI",
                     Roboto,
                     Oxygen-Sans,
                     Ubuntu,
                     Cantarell,
                     "Helvetica Neue",
                     sans-serif;  
    }

I've extended this stack, borrowing from other stacks and adding Adobe's "Source Sans" font. Like GitHub's, my stack also supports emoji.

.. code:: css

    body {  
        font-family: -apple-system,
                     BlinkMacSystemFont,
                     "Segoe UI",
                     Roboto,
                     Oxygen,
                     Oxygen-Sans,
                     Ubuntu,
                     Cantarell,
                     "Fira Sans",
                     "Droid Sans",
                     "Helvetica Neue",
                     "Source Sans Pro",
                     sans-serif,
                     "Apple Color Emoji",
                     "Segoe UI Emoji",
                     "Segoe UI Symbol";
    }

My custom stack has the advantage of being compatible with most desktop-oriented GNU/Linux systems, and will also use a nicer font on desktop BSD systems whose users have installed fonts like Cantarell and Fira Sans.

Why use a system UI font stack?
===============================

This approach has a couple of advantages, which Ire Aderinokun explained in her article. I'll paraphrase them below for your convenience:

Performance
-----------

Since system UI fonts are pre-installed, the page renders faster while making fewer HTTP requests. You want your pages to download and render faster, don't you? Of course you do, even if you've come to realize that most SEO is bullshit.

Going Native
------------

Because your website/web app uses the same fonts as your users' operating systems, you're providing an integrated user experience (UX). This is especially important for web apps, but can be handy for websites, too.

Fine-Grained Control
--------------------

Rather than using the `"font" shorthand property <https://developer.mozilla.org/en-US/docs/Web/CSS/font>`_, setting the `"font-family" <https://developer.mozilla.org/en-US/docs/Web/CSS/font-family>`_ property of the "body" element defines a set of possible fonts for all elements on the page. We're still free to apply `"font-style" <https://developer.mozilla.org/en-US/docs/Web/CSS/font-style>`_, `"font-variant" <https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant>`_, `"font-weight" <https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight>`_, `"font-size" <https://developer.mozilla.org/en-US/docs/Web/CSS/font-size>`_, and `"line-height" <https://developer.mozilla.org/en-US/docs/Web/CSS/line-height>`_ properties to various `CSS selectors <https://developer.mozilla.org/en-US/docs/Glossary/CSS_Selector>`_ to style our text.

Drawbacks to using a system UI font stack
=========================================

While I think it makes sense to use system fonts, this approach isn't without its drawbacks. As `Ire Aderinokun points out <https://bitsofco.de/the-new-system-font-stack/>`_, maintenance can be an issue, and you might also run into naming conflicts. There's another drawback Ms. Aderinokun doesn't mention: they're all sans-serif.

Naming conflicts
----------------

With the exception of "-apple-system" and "BlinkMacSystemFont", current stack implementations specify fonts by name rather than by vendor-specific aliases. The "-apple-system" alias is defined by Apple, and allows Safari on OSX and iOS to use the `San Francisco fonts <https://developer.apple.com/fonts/>`_. "BlinkMacSystemFont" is Google Chrome's alias for these fonts.

If your user's browser falls back on "Segoe UI" because your user is viewing the site on Windows, one of three things can happen:

1. If "Segoe UI" is available, the web page gets rendered in Segoe UI.
2. If "Segoe UI" isn't available, the browser tries the next font in the stack.
3. If the user's "Segoe UI" is actually "Wingdings", the page looks like shit.

The third possibility is the one you don't want to happen. Also, don't try to be clever and make "system" the first font in the stack. They already tried that at Medium. `Hilarity ensued. <https://medium.design/system-shock-6b1dc6d6596f#.9i70uvkum>`_

Maintenance
-----------

Operating systems change, and part of that change involves changing the standard UI font. A few years ago, Microsoft changed the default Windows font from Tahoma to Segoe UI. More recently, Apple switched from Lucida Grande to San Francisco.

If web developers don't keep up, their font stacks will go stale. Their sites might use fonts that don't match their users' operating systems. Hell, a site with an ancient font stack might even resort to the dreaded "sans-serif" alias.

While it shouldn't be that difficult to update your stylesheets once or twice a year and push an update, that's still time better spent on other things. Unfortunately, we're stuck at the moment.

No Serif or Monospace Stacks for You
------------------------------------

You may have noticed that all of the fonts in the various system UI font stacks are all sans-serif fonts. I noticed this myself, and `submitted the following comment to CSS-Tricks's article <https://css-tricks.com/snippets/css/system-font-stack/#comment-1606237>`_:

    This makes a lot of sense and I plan to use this in my next website, but these are all sans-serif fonts. I can’t help but wonder if it’s possible to create similar stacks for system-default serif and monospace fonts. I might want to use the serif fonts on headings or blockquotes for emphasis, and apply monospace to the pre and code elements.

It might not be the worst comment ever posted (it isn't abusive, racist, or sexist enough), but I've seen better. Hell, I've posted better &mdash; just not on a smartphone at four in the morning while taking a leak.

Here is `Chris Coyier's reply <https://css-tricks.com/snippets/css/system-font-stack/#comment-1606238>`_:

    Is there any OS that uses a serif for a system font?

Mr. Coyier is right to ask this question. As far as I know, there isn't a single OS or X11 desktop environment that uses serif fonts as UI fonts. However, I've never worked on a computer that didn't come with at least one serif font pre-installed as part of the operating system or the operating system's `X Window System <https://www.x.org/wiki/>`_ packages. 

The same goes for monospace fonts. They're only used in terminal emulators and the Windows command prompt, but every OS has at least one.

Next Steps for System Standard Font Stacks
==========================================

The use of system UI font stacks is a relatively new trend, but I think it will continue because it makes sense. You can't beat the performance, and it's an excellent method for ensuring that your content remains readable regardless of device or browser.

However, system UI font stacks are currently a bit of a kludge_. Fixing the drawbacks inherent in this approach will encourage wide-spread adoption...

Fix 1: Standardization
----------------------

As system UI font stacks catch on, I hope web developers will lobby the World Wide Web Consortium (W3C_) to update the CSS standard. Manually updating the font-family stack isn't just only a burden on developers, albeit a relatively small one. 

It's also a performance hit users take with every page. Using current stacks, a browser must try fonts in sequence until it finds the first available font specified in the stack. In a worst-case scenario, a browser might attempt every font in the stack before resorting to "sans-serif".

If the W3C updated the CSS spec to include a "system-ui-font" alias, web developers could instead specify "font-family: system-ui-font, sans-serif;" instead of trying to specify every reasonably common environment's UI font by name/vendor alias in the right order. They could be confident that current browsers would use the operating system's standard UI font. Browsers that don't understand "system-ui-font" could still fall back on "sans-serif".

Fix 2: Expansion from a System UI Font Stack to System Standard Font Stacks
---------------------------------------------------------------------------

The first fix solves the need for maintenance on the developers' part and eliminates the risk of naming conflicts. However, the third drawback remains. While sans-serif fonts are better for low-resolution (100dpi or less) screens, displays with higher text resolution are becoming more common. 

Apple led the way with their Retina displays on the iPhone, but small high-resolution displays are slowly becoming more common in laptops and desktops outside Apple's ecosystem. If 4K or higher displays become sufficiently cheap and ubiquitous that 1080p replaces 1366x768 as the standard resolution for budget laptops, then improved HiDPI support may soon follow.

Once that happens, and text on screen gets rendered at resolutions approaching that of print, the readability edge that sans serif fonts enjoy over serif fonts may disappear. That doesn't mean that operating systems will use serif fonts instead of sans serif for UI. Instead, designers may have the option of rendering long passages of text in serif rather than sans serif without sacrificing readability on screens.

That means that a system UI font stack like those currently in use isn't enough. We need a set of **System Standard Font Stacks (SSFS)**: one for sans serif, one for serif, and one for monospace.

Despite my previous focus on HiDPI displays, serif and monospace SSFSes can still be useful today. Maybe you just want to emphasize headings and blockquotes by using serif fonts instead of sans serif. If you make liberal use of the "code" and "pre" elements, you might want these to render in a monospace font. If you want to provide "printer-friendly" versions of your pages, perhaps you'd rather print with a serif text instead of sans serif.

Regardless of your reason for not wanting to use sans serif, having system standard font stacks in serif and monospace is still a good idea for the same reasons the original sans serif stack is trending: improved performance, better integration with the viewer's device, and more creative control.

Basic Serif & Monospace System Standard Font Stacks
===================================================

With these possibilities in mind, I did some research and came up with serif and monospace stacks composed of fonts that should be available on the widest possible variety of devices.

With the original system UI font stack's example in mind, I've tried to arrange my stack from most specific to most generic. I doubt most Windows and Linux machines will have "Apple Garamond", and that is likewise true for Android devices.

Serif SSFS
----------

.. code:: css

    h1, h2, h3, h4, h5, h6, blockquote {  
        font-family: "Apple Garamond",
                     "Baskerville",
                     "Georgia",
                     "Times New Roman",
                     "Roboto Slab",
                     "Droid Serif",
                     "Times",
                     "Source Serif Pro",
                     serif,
                     "Apple Color Emoji",
                     "Segoe UI Emoji",
                     "Segoe UI Symbol";
    }

Monospace SSFS
--------------

.. code:: css

    pre, code {  
        font-family: "SF Mono",
                     "Monaco",
                     "Inconsolata",
                     "Hack",
                     "Fira Mono",
                     "Droid Sans Mono",
                     "Source Code Pro",
                     monospace;
    }

Notes and Caveats
-----------------

The Source Serif and Source Code Pro fonts (along with Source Sans Pro) are freely available from `Adobe Fonts on Github <https://github.com/adobe-fonts>`_. I include them as a last stop before sans-serif, serif, and monospace in my stacks because I use these fonts on GNU/Linux.

Speaking of Linux, "Times" (as opposed to Times New Roman) is a font I used to see packaged with X11.

While Mozilla created `Fira Mono to go with Fira Sans for Firefox OS <https://github.com/mozilla/Fira>`_, they didn't bother to create a serif variant. `Roboto Slab might be a reasonable substitute <https://fonts.google.com/specimen/Roboto+Slab>`_, but I have not been able to determine whether it comes pre-packaged with Android the way `Roboto <https://fonts.google.com/specimen/Roboto>`_ does.

I've included "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol" in the serif stack so that text rendered in serif still has a chance of showing emoji on devices possessing these fonts. I also specify them in my sans serif stack.

Any Questions?
==============

You're welcome to use my serif and monospace system-standard font stacks in your own development if you like. If you have any questions, or want to contact me, you can reach me by email_. If you decide to quote and link to this post in your own blog, I'd also like to hear from you.

.. _Jekyll: https://jekyllrb.com/
.. _Squarespace: https://squarespace.com/
.. _WordPress: https://wordpress.org/
.. _Medium: https://medium.com/
.. _Ghost: https://ghost.org/
.. _Github: http://github.com/
.. _kludge: https://en.wikipedia.org/wiki/Kludge
.. _W3C: https://www.w3.org/
.. _email: mailto:public@matthewgraybosch.com