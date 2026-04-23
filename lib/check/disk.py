from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.check import Check
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['READYDATAOS-MIB']['diskEntry'], True),
)


class CheckDisk(Check):
    key = 'disk'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        snmp = get_snmp_client(asset, local_config, config)
        state = await snmpquery(snmp, QUERIES)
        for disk in state.get('diskEntry', []):
            disk['diskCapacity'] = int(disk['diskCapacity'])
        return state
