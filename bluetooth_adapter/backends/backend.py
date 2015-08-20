import logging


log = logging.getLogger(__name__)
ERROR = "Not implemented on abstract base class"


class BLEBackend(object):
    """Abstract base class representing a Bluetooth adapter backend."""

    def __repr__(self):
        log.error(ERROR)
        raise NotImplementedError()

    def start(self):
        log.error(ERROR)
        raise NotImplementedError()

    def stop(self):
        log.error(ERROR)
        raise NotImplementedError()

    def scan(self):
        log.error(ERROR)
        raise NotImplementedError()

    def list_bonds(self):
        log.error(ERROR)
        raise NotImplementedError()

    def remove_bond(self, bond):
        log.error(ERROR)
        raise NotImplementedError()

    def clear_bonds(self, bond):
        log.error(ERROR)
        raise NotImplementedError()

    def connect(self, address):
        log.error(ERROR)
        raise NotImplementedError()

    def get_rssi(self, address, from_connection=False):
        log.error(ERROR)
        raise NotImplementedError()

    def encrypt(self):
        log.error(ERROR)
        raise NotImplementedError()

    def bond(self):
        log.error(ERROR)
        raise NotImplementedError()

    def attribute_read(self, attribute):
        log.error(ERROR)
        raise NotImplementedError()

    def attribute_write(self, attribute, value):
        log.error(ERROR)
        raise NotImplementedError()

    def subscribe(self, characteristic, notification, indication, callback):
        log.error(ERROR)
        raise NotImplementedError()