from setuptools import setup, find_packages

# Set version
with open('VERSION', 'r') as f:
    __version__ = f.read().strip()

SHORT_DESCRIPTION = 'A MQTT-Eventghost wrapper.'

# Use the README.md as the long description
with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

requirements = [
    'paho-mqtt',
]

testing_requirements = [
    'coveralls',
    'pep8',
    'pylint',
    'pytest',
    'pytest-cov',
]


setup(
    name='silent_eg',
    version=__version__,
    url='https://github.com/SilentFrogNet/silent_eg',
    author='Ilario Dal Grande',
    author_email='info@silentfrog.net',
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license='GPLv3',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=requirements,
    dependency_links=[
    ],
    extras_require={
        'testing': testing_requirements,
        # 'readline': ['gnureadline'],
        # 'windows': ['pyreadline'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows 10',
        'Environment :: Console',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: System :: Shells',
        'Topic :: System :: System Shells',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    # entry_points='''
    #     [console_scripts]
    #     sho=app:cli
    # ''',
)
