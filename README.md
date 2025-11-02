<h1 align="center">
    FLORIPASAT-2A TELEMETRY VIEWER
    <br>
</h1>

<h4 align="center">Telemetry visualizer software for the FloripaSat-2A mission.</h4>

<p align="center">
    <a href="https://github.com/spacelab-ufsc/fsat2atv">
        <img src="https://img.shields.io/badge/status-development-green?style=for-the-badge">
    </a>
    <a href="https://github.com/spacelab-ufsc/fsat2atv/releases">
        <img alt="GitHub commits since latest release (by date)" src="https://img.shields.io/github/commits-since/spacelab-ufsc/fsat2atv/latest?style=for-the-badge">
    </a>
    <a href="https://github.com/spacelab-ufsc/fsat2atv/blob/main/LICENSE">
        <img src="https://img.shields.io/badge/license-GPL3-yellow?style=for-the-badge">
    </a>
</p>

<p align="center">
    <a href="#overview">Overview</a> •
    <a href="#dependencies">Dependencies</a> •
    <a href="#installing">Installing</a> •
    <a href="#documentation">Documentation</a> •
    <a href="#license">License</a>
</p>

# Overview

The FloripaSat-2A Telemetry Viewer (FSat2ATV) is a software to visualize and manage the telemetry data transmitted by the FloripaSat-2A satellite.

Below, there is an image of the main window of the software:

<img src="docs/img/main-window.png" width=""/>

# Dependencies

* [PyGObject](https://pypi.org/project/PyGObject/)

## Installation on Ubuntu

```sudo apt install python3 python3-gi```

## Installation on Fedora

```sudo dnf install python3 python3-gobject```

# Installing

```python setup.py install```

# Documentation

## Dependencies

* Sphinx
* sphinx-redactor-theme

## Building the Documentation

```make html```

# License

This project is licensed under GPLv3 license.
