I Became a Programmer to Avoid Grunt Work, Dammit
#################################################

:date: 2017-02-03 21:46
:category: Just Tech Things
:summary: I don't mind working hard, but I hate doing repetitive, tedious work. Especially when it involves cleaning up after somebody else's mistakes.
:tags: web development, front end, bootstrap, div soup, accessibility, a11y, rant
:slug: became-programmer-avoid-grunt-work-dammit

It's about a quarter to ten on a Friday night, and I'm still here at my day job working on accessibility fixes for a public facing page so that the app we're building for a government client will be compliant with Section 508 of the Americans with Disabilities Act.

Why? Because web accessibility is *not* something you fuck around with unless you want to get sued. Also, because this shit is actually *important*. It shouldn't matter what sort of disabilities you've got. **Every website should work for everybody, goddammit.**

To ignore web accessibility is to engage in the sort of rank ableism that is best left to brogrammers fresh out of college who have never faced adversity and need to be pimp-slapped across the face by the reality of unemployment and poverty.

The problem is that I must go through the page and wire up every last donkey-molesting coprophagic form input element to its respective label, so that it looks something like this:

.. code:: html

    <div class="row form-group">
        <div class="col-sm-3">
            <label for="exampleFormInput"  
                    aria-label="This is a form input element.">  
                    Form Input Element
            </label>
        </div>
        <div class="col-sm-9">
            <input id="exampleFormInput"  
                    type="text"  
                    size="255" />
        </div>
    </div>

Naturally, it's a Bootstrap app so it's ``<div>`` soup. And because *none* of the inputs were wired to labels, I've got to go through a hundred of the damned things and wire up every one of them by hand. This is the sort of `grunt work <http://idioms.thefreedictionary.com/grunt+work>`_ I became a programmer to *avoid* doing.

Actually, the sort of grunt work I wanted to escape also involved...

* scraping baby barf off of floors
* erasing the attempts of homeless people with untreated mental illness at fecal fingerpainting in the public bathrooms
* not going postal every Christmas because of the shitty muzak and parents dragging their kids into the store when they're tired, cranky, and have an acute (but not at all cute) case of the mommylookits

However, it's still the sort of grunt work that should be automated or delegated to a junior developer, but a junior dev who doesn't grok the importance of accessibility already fucked up this page. That leaves automation, which means I'd have to find a HTML parser library that can cope with the proprietary controls I'm actually using instead of ``<label>`` and ``<input>``. Either that, or start `figuring out how to parse HTML with regular expressions <https://blog.codinghorror.com/parsing-html-the-cthulhu-way/>`_.

If the Coding Horror post I just linked is any indication, *that way lies madness*. The problem is that I'm not sane. I'm just high-functioning.

Though I probably could have wired up a dozen fields in the fifteen minutes I spent on this post, so maybe I'm *not* high-functioning. Maybe I've finally lost it. In which case you're all *fucked* once I start working on *Blackened Phoenix* again.