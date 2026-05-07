from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.check import Check
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['READYDATAOS-MIB']['volumeEntry'], True),
)


class CheckVolume(Check):
    key = 'volume'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        snmp = get_snmp_client(asset, local_config, config)
        state = await snmpquery(snmp, QUERIES)
        for vol in state.get('volumeEntry', []):
            free = vol['volumeFreeSpace']
            total = vol['volumeSize']
            vol['volumeUsedSpace'] = used = total - free
            vol['volumeUsedPercentage'] = 100 * used / total if total else None
            vol['volumeFreePercentage'] = 100 * free / total if total else None

        return state
