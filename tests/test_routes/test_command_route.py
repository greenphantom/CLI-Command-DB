"""Test script for unit testing all the command endpoints."""

from tests.test_routes.app_fixture import client


def test_get_cmds(client):
    """Tests the get route works correctly."""
    rv = client.get('commands')
    assert rv.status_code == 200
