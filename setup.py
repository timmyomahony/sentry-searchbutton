from setuptools import setup, find_packages

install_requires = [
    'sentry>=5.0.0',
]

setup(
    name='sentry-searchbutton',
    version='0.1.0',
    author="Timmy O'Mahony",
    author_email='me@timmyomahony.com',
    url='http://github.com/timmyomahony/sentry-seachbutton',
    description='A Sentry extension that introduces a search button for errors',
    long_description=__doc__,
    license='BSD',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
       'sentry.plugins': [
            'searchbutton = sentry_searchbutton.plugin:SearchButton'
        ],
        'sentry.apps': [
            'searchbutton = sentry_searchbutton'
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
