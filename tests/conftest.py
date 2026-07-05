"""Test configuration for Newsletter Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "newsletter-agent", "category": "Marketing"}
