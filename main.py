from libprobe.probe import Probe
from lib.check.disk import CheckDisk
from lib.check.fan import CheckFan
from lib.check.psu import CheckPsu
from lib.check.system import CheckSystem
from lib.check.temperature import CheckTemperature
from lib.check.volume import CheckVolume
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckDisk,
        CheckFan,
        CheckPsu,
        CheckSystem,
        CheckTemperature,
        CheckVolume,
    )

    probe = Probe("readynas", version, checks)

    probe.start()
