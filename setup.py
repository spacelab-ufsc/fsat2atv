#!/usr/bin/env python

#
#  setup.py
#  
#  Copyright The FloripaSat-2A Telemetry Viewer Contributors.
#  
#  This file is part of FloripaSat-2A Telemetry Viewer.
#
#  FloripaSat-2A Telemetry Viewer is free software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#  
#  FloripaSat-2A Telemetry Viewer is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public
#  License along with FloripaSat-2A Telemetry Viewer; if not, see
#  <http://www.gnu.org/licenses/>.
#  
#

import setuptools
import os

from sphinx.setup_command import BuildDoc

exec(open('fsat2atv/version.py').read())

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name                            = "floripasat2a_telemetry_viewer",
    version                         = __version__,
    author                          = "Gabriel Mariano Marcelino",
    author_email                    = "gabriel.mm8@gmail.com",
    maintainer                      = "Gabriel Mariano Marcelino",
    maintainer_email                = "gabriel.mm8@gmail.com",
    url                             = "https://github.com/spacelab-ufsc/fsat2atv",
    license                         = "GPLv3",
    description                     = "FloripaSat-2A Telemetry Viewer",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    platforms                       = ["Linux"],
    classifiers                     = [
        "Development Status :: 4 - Beta",
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research"
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Communications :: Ham Radio",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        ],
    download_url                    = "https://github.com/spacelab-ufsc/fsat2atv/releases",
    packages                        = setuptools.find_packages(),
    install_requires                = ['gi'],
    entry_points                    = {
        'gui_scripts': [
            'golds-ufsc-tv = fsat2atv.__main__:main'
            ]
        },
    data_files                      = [
        ('share/icons/', ['fsat2atv/data/img/fsat2atv_256x256.png']),
        ('share/applications/', ['fsat2atv.desktop']),
        ('share/fsat2atv/', ['fsat2atv/data/ui/fsat2atv.glade']),
        ('share/fsat2atv/', ['fsat2atv/data/img/spacelab-logo-full-400x200.png']),
        ],
    cmdclass                        = {'build_sphinx': BuildDoc},
)
