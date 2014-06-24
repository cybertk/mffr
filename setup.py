from distutils.core import setup

setup(
    name='mffr',
    version='1.0.0',
    author='Quanlong He',
    author_email='kyan.ql.he@gmail.com',
    scripts=['bin/mffr'],
    packages=[
        'chromium_tools'],
    url='https://github.com/cybertk/mffr',
    license='BSD-style License, see LICENSE.txt',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development ",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",

    ],
    keywords='replace find mutli-file substitude files',
    description='Fast multi-file find and replace',
)
