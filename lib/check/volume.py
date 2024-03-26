from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..utils import get_data

QUERIES = (
    MIB_INDEX['READYDATAOS-MIB']['volumeEntry'],
)


async def check_volume(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    state = await get_data(asset, asset_config, check_config, QUERIES)
    for vol in state.get('volumeEntry', []):
        free = vol['volumeFreeSpace']
        total = vol['volumeSize']
        vol['volumeUsedSpace'] = used = total - free
        vol['volumeUsedPercentage'] = 100 * used / total if total else None
        vol['volumeFreePercentage'] = 100 * free / total if total else None

    return state
