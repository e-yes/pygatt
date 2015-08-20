import click

from bluetooth_adapter import BluetoothAdapter
from bluetooth_adapter.backends import BackendEnum


def main():
    click.secho("Creating BluetoothAdapter", fg='green')
    adapter = BluetoothAdapter(BackendEnum.bgapi)
    click.secho("Enabling adapter", fg='green')
    adapter.enable()

    click.secho("Disabling adapter", fg='green')
    adapter.disable()


if __name__ == '__main__':
    main()
