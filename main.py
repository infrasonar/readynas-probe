from libprobe.probe import Probe
from lib.check.disk import check_disk
from lib.check.fan import check_fan
from lib.check.psu import check_psu
from lib.check.temperature import check_temperature
from lib.check.volume import check_volume
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'disk': check_disk,
        'fan': check_fan,
        'psu': check_psu,
        'temperature': check_temperature,
        'volume': check_volume,
    }

    probe = Probe("readynas", version, checks)

    probe.start()
