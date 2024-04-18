r"""
  _____                    ______
 |  __ \                  |  ____|
 | |  | |_   _ _ __   __ _| |__ ___  _ __ _ __ ___
 | |  | | | | | '_ \ / _` |  __/ _ \| '__| '_ ` _ \
 | |__| | |_| | | | | (_| | | | (_) | |  | | | | | |
 |_____/ \__, |_| |_|\__,_|_|  \___/|_|  |_| |_| |_|
          __/ |
         |___/
"""

import django

__title__ = "DynaForm"
__version__ = "0.1.0"
__author__ = "Loghman Barari"
__license__ = "BSD 3-Clause"
__copyright__ = "Copyright 2022-Present Loghman Barari"

# Version synonym
VERSION = __version__

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = "iso-8859-1"

# Default datetime input and output formats
ISO_8601 = "iso-8601"


if django.VERSION < (3, 2):
    default_app_config = "dynaform.apps.DynaFormConfig"
