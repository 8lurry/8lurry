.. doctest docs/specs/db.rst
.. _whitewall.specs.db:

================================
Database structure of Whitewall
================================

This document describes the database structure.

.. contents::
  :local:


.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('whitewall.projects.whitewall1.settings.doctests')
>>> from lino.api.doctest import *


>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_db_overview())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
17 apps: lino, staticfiles, about, jinja, bootstrap3, extjs, printing, system, users, lets, whitewall, export_excel, office, tinymce, weasyprint, appypod, sessions.
9 models:
=========================== ============================ ========= =======
 Name                        Default table                #fields   #rows
--------------------------- ---------------------------- --------- -------
 lets.Demand                 lets.Demands                 3         3
 lets.Offer                  lets.Offers                  4         5
 lets.Place                  lets.Places                  4         4
 lets.Product                lets.Products                4         6
 sessions.Session            users.Sessions               3         ...
 system.SiteConfig           system.SiteConfigs           3         0
 tinymce.TextFieldTemplate   tinymce.TextFieldTemplates   5         2
 users.Authority             users.Authorities            3         0
 users.User                  users.AllUsers               19        11
=========================== ============================ ========= =======
<BLANKLINE>
