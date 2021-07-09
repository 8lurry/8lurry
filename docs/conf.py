# -*- coding: utf-8 -*-
from lino.sphinxcontrib import configure
configure(globals(), 'whitewall.projects.whitewall1.settings.doctests')

extensions += ['lino.sphinxcontrib.help_texts_extractor']
help_texts_builder_targets = {
    'whitewall.': 'whitewall.lib.whitewall'
}

project = "Whitewall"
copyright = '2016-2021 Rumma & Ko Ltd'

html_title = "Whitewall"
# html_context.update(public_url='https://whitewall.lino-framework.org')
