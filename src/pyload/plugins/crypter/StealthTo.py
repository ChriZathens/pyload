# -*- coding: utf-8 -*-

from ..internal.deadcrypter import DeadCrypter


class StealthTo(DeadCrypter):
    __name__ = "StealthTo"
    __type__ = "crypter"
    __version__ = "0.25"
    __status__ = "stable"

    __pyload_version__ = "0.5"

    __pattern__ = r"http://(?:www\.)?stealth\.to/folder/.+"
    __config__ = [("enabled", "bool", "Activated", True)]

    __description__ = """Stealth.to decrypter plugin"""
    __license__ = "GPLv3"
    __authors__ = [("spoob", "spoob@pyload.net")]