.. _whitewall.install:

Installing Whitewall
=====================

- Install Lino (the framework) as documented in
  :ref:`lino.dev.install`

- Go to your :xfile:`repositories` directory and download also a copy
  of the *Whitewall* repository::

    cd ~/repositories
    git clone https://github.com/lino-framework/whitewall
    
- Use pip to install this as editable package::

    pip install -e whitewall

- Create a local Lino project as explained in
  :ref:`lino.tutorial.hello`.

- Change your project's :xfile:`settings.py` file so that it looks as
  follows:

  .. literalinclude:: settings.py

  The first line is Python way to specify encoding (:pep:`263`).
  That's needed because of the non-ascii **ì** of "Lino Noi" in
  line 3.

