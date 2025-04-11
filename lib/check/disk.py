from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['READYDATAOS-MIB']['diskEntry'], True),
)


async def check_disk(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)
    for disk in state.get('diskEntry', []):
        disk['diskCapacity'] = int(disk['diskCapacity'])
    return state
