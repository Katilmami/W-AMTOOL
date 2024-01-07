from distutils.core import setup
import py2exe

setup(
    options={'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows=[{'script': 'mami.py'}],  # your_script.py, ana Python betiğinizin adını belirtin
    zipfile=None,
)
