from setuptools import setup

import io
exec(open('dash-flask-login/version.py').read())

setup(
    name='dash_flask_login',
    version=__version__,  # noqa: F821
    author='Gideon Whitehead',
    author_email='gideon.whitehead@uphs.upenn.edu',
    packages=['dash_flask_login'],
    license='MIT',
    description='Integration of Dash with Flask-Login',
    long_description=io.open('README.md', encoding='utf-8').read(),
    install_requires=[
        'Flask>=0.12',
        'flask-compress',
        'flask-seasurf',
        'plotly',
        'dash>=0.18.3'
    ],
    include_package_data=True,
    url='https://github.com/gaw89/dash-flask-login',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Dash/Flask',
        'Intended Audience :: Dash Developers/Users',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
