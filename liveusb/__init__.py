# -*- coding: utf-8 -*-
#
# Copyright © 2008  Red Hat, Inc. All rights reserved.
#
# This copyrighted material is made available to anyone wishing to use, modify,
# copy, or redistribute it subject to the terms and conditions of the GNU
# General Public License v.2.  This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY expressed or implied, including the
# implied warranties of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.  You should have
# received a copy of the GNU General Public License along with this program; if
# not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth
# Floor, Boston, MA 02110-1301, USA. Any Red Hat trademarks that are
# incorporated in the source code or documentation are not subject to the GNU
# General Public License and may only be used or replicated with the express
# permission of Red Hat, Inc.
#
# Author(s): Luke Macken <lmacken@redhat.com>

import os
import sys
import gettext
import locale

if sys.platform == 'win32':
    import gettext_windows
    gettext_windows.setup_env()

if os.path.exists('locale'):
    translation = gettext.translation('liveusb-creator', 'locale', fallback=True)
else:
    translation = gettext.translation('liveusb-creator', '/usr/share/locale',
                                      fallback=True)
_ = translation.ugettext

def utf8_gettext(string):
    " Translate string, converting it to a UTF-8 encoded bytestring "
    return _(string).encode('utf8')


class LiveUSBError(Exception):
    """ A generic error message that is thrown by the LiveUSBCreator """

    def __init__(self, fullMessage, shortMessage=""):
        self.args = [fullMessage]
        if shortMessage != "":
            self.short = shortMessage
        else:
            self.short = fullMessage

if sys.platform == "win32":
    from liveusb.creator import WindowsLiveUSBCreator as LiveUSBCreator
elif sys.platform.startswith("linux"):
    from liveusb.creator import LinuxLiveUSBCreator as LiveUSBCreator
elif sys.platform == "darwin":
    from liveusb.creator import MacOsLiveUSBCreator as LiveUSBCreator
else:
    from liveusb.creator import LiveUSBCreator as LiveUSBCreator

__all__ = ("LiveUSBCreator", "LiveUSBError", "LiveUSBWindow", "_", "utf8_gettext")
