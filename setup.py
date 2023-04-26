import sys
from io import open

from setuptools import find_packages, setup


extras_require = {
    'dev': [
        'django',
        'django_mock_queries',
        'pylint',
        'pytest-pylint',
        'pytest',
        'pytest-cov',
        'pytest-watch',
        'tox'
    ],
    'code-quality': [
        'isort',
        'bandit',
        'xenon',
    ],
}


def get_version():
    version = '0.0'
    for arg in sys.argv:
        if arg.startswith('--version'):
            version = arg.split("=")[1]
            sys.argv.remove(arg)
            break

    return version if version[0] != 'v' else version[1:]


setup(
    name='django-admin-inline-paginator',
    version=get_version(),
    description='The "Django Admin Inline Paginator" is simple way to paginate your inline in django admin',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Shinneider Libanio da Silva',
    author_email='shinneider-libanio@hotmail.com',
    url='https://github.com/shinneider/django-admin-inline-paginator',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    python_requires=">=3.3",
    extras_require=extras_require,
    install_requires=[
        'django',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
