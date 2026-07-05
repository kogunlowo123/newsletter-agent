"""Newsletter Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_curate_content():
    """Test Curate relevant content for a newsletter edition."""
    tools = AgentTools()
    result = await tools.curate_content(topic_areas="test", sources="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_write_editorial():
    """Test Write editorial commentary for curated content items."""
    tools = AgentTools()
    result = await tools.write_editorial(content_items="test", voice="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_build_edition():
    """Test Build a complete newsletter edition from components."""
    tools = AgentTools()
    result = await tools.build_edition(sections="test", template="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_manage_preferences():
    """Test Manage subscriber content preferences and frequency."""
    tools = AgentTools()
    result = await tools.manage_preferences(subscriber_id="test", preferences="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.newsletter_agent_agent import NewsletterAgentAgent
    agent = NewsletterAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
