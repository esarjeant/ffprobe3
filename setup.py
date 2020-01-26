#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='ffprobe3-esarjeant',
    version='0.1.3',
    description="""
    Original Project: ffprobe3 (https://github.com/DheerendraRathor/ffprobe3)

    A wrapper around ffprobe command to extract metadata from media files.

    This project which is maintained by Eric Sarjeant is a Python 3 port of original ffprobe3 which is itself a fork
    of ffprobe.
    """,
    author='Simon Hargreaves',
    author_email='simon@simon-hargreaves.com',
    maintainer='Eric Sarjeant',
    maintainer_email='eric@sarjeant.us',
    url='https://github.com/esarjeant/ffprobe3',
    packages=['ffprobe3'],
    keywords='ffmpeg, ffprobe, mpeg, mp4',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Natural Language :: English',
        'Topic :: Multimedia :: Video',
        'Topic :: Software Development :: Libraries'
    ])
