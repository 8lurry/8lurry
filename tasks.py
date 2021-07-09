from atelier.invlib import setup_from_tasks
ns = setup_from_tasks(
    globals(), "whitewall",
    languages="en bn".split(),
    # tolerate_sphinx_warnings=True,
    locale_dir='whitewall/lib/whitewall/locale',
    revision_control_system='git',
    cleanable_files=['docs/api/whitewall.*'],
    demo_projects=['whitewall.projects.whitewall1'])
