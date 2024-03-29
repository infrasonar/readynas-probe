from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..utils import get_data

QUERIES = (
    MIB_INDEX['READYDATAOS-MIB']['diskEntry'],
)


async def check_disk(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    state = await get_data(asset, asset_config, check_config, QUERIES)
    for disk in state.get('diskEntry', []):
        disk['diskCapacity'] = int(disk['diskCapacity'])
    return state
