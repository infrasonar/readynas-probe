from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..utils import get_data

QUERIES = (
    MIB_INDEX['READYDATAOS-MIB']['fanEntry'],
)


async def check_fan(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    state = await get_data(asset, asset_config, check_config, QUERIES)
    return state
