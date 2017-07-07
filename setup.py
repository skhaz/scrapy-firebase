from distutils.core import setup


setup(
    name='scrapy-firebase',
    version='0.0.1',
    license='Apache License, Version 2.0',
    description='Pipeline to Firebase for Scrapy.',
    author='Rodrigo Delduca',
    author_email='rodrigodelduca@gmail.com',
    url='https://github.com/skhaz/scrapy-firebase',
    keywords="scrapy firebase",
    py_modules=['scrapy_firebase'],
    platforms=['Any'],
    install_requires=[
        'Scrapy >= 1.4.0',
        'firebase-admin >= 2.1.0'
    ],
    classifiers=[
        'Development Status :: 0 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
