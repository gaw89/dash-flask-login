from setuptools import setup
import io
from dash_flask_login import __version__

setup(
    name='dash_flask_login',
    version=__version__,  # noqa: F821
    author='Gideon Whitehead',
    author_email='gideon.whitehead@uphs.upenn.edu',
    packages=['dash_flask_login'],
    package_data={'': ['dash_flask_login/templates/*.html']},
    license='MIT',
    description='Integration of Dash with Flask-Login',
    long_description=io.open('README.md', encoding='utf-8').read(),
    install_requires=[
        'Flask>=0.12',
        'flask-compress',
        'flask-seasurf',
        'plotly',
        'dash>=0.18.3',
        'jinja2==2.10',
        'flask_login==0.4.1'
    ],
    include_package_data=True,
    url='https://github.com/gaw89/dash-flask-login',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
