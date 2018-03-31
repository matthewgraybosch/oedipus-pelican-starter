CSS Frameworks Considered Harmful
#################################

:date: 2018-03-12 08:27
:category: Just Tech Things
:tags: css, framework, bootstrap, foundation, bulma, grid, flexbox, diy, technical debt, web, development, developer, front end
:summary: Any web developer who chooses to use a CSS framework in the absence of pressure from management is going to regret it once I take over their project and find out where they live.
:slug: css-frameworks-considered-harmful


Any web developer who chooses to use a CSS framework in the absence of pressure from management is going to regret it once `I take over their project and find out where they live <http://wiki.c2.com/?CodeForTheMaintainer>`_.

I don't care if you're using Bootstrap, Foundation, Bulma, or some other framework. Chances are it's overkill and you don't need it. Sure, it might make things easier at first, but you're introducing technical debt that some other poor schmuck must pay down by doing the following:

* Frameworks use shitty, non-semantic markup. Seriously, why are we still using nested divs for *everything* in HTML5? And `whose bright goddamn idea was it <https://fontawesome.com/>`_ to use the ``<i>`` tag for icons?
* Framework CSS selectors get way too specific. Good luck customizing individual elements.
* Frameworks provide shit you probably don't need. I'm building a static personal website here; I don't *need* modal popup messages in six different colors.
* Frameworks make the web boring. You know damn well that every website built with Bootstrap looks like every *other* fucking website built with Bootstrap no matter how hard you work to hide it.

Check out `this article by Belén Albeza <https://hacks.mozilla.org/2016/04/you-might-not-need-a-css-framework/>` _ if you don't believe me. They even provide simple examples of alternatives using Flexbox and CSS Grid.

I've got an idea: how about you grow a fucking spine, develop some design sense, learn something about aesthetics, and take the time to craft your own semantic markup and just enough CSS to do the job. This `motherfucking website <http://motherfuckingwebsite.com>`_ doesn't even use CSS. This `other motherfucker <http://bettermotherfuckingwebsite.com>`_ only uses seven lines. They both work just fine for their purpose.

PS
==

Any framework that provides its own grid system instead of using CSS Grid
needs to die in a fire. I don't give a damn if IE doesn't fully support
CSS Grid yet, because I understand concepts like `graceful degradation
<https://developer.mozilla.org/en-US/docs/Glossary/Graceful_degradation>`_.

PPS
=== 

If your website isn't readable with `lynx <http://lynx.invisible-island.net/>`_ and it isn't a single-page app that provides information inside ``<noscript>`` tags, then your website is a worthless piece of shit and so are you.
