from eth_tester.constants import (
    UINT256_MAX,
    UINT256_MIN,
)


def test_eth_getBalance(rpc_client):
    accounts = rpc_client('eth_accounts')
    for account in accounts:
        balance = rpc_client('eth_getBalance', params=[account, 'latest'])
        assert balance >= UINT256_MIN
        assert balance <= UINT256_MAX
