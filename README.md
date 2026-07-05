# Newsletter Agent

[![CI](https://github.com/kogunlowo123/newsletter-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/newsletter-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Marketing | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Newsletter creation agent that curates content, writes editorial sections, manages subscriber preferences, personalizes editions, and tracks readership engagement.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `curate_content` | Curate relevant content for a newsletter edition |
| `write_editorial` | Write editorial commentary for curated content items |
| `build_edition` | Build a complete newsletter edition from components |
| `manage_preferences` | Manage subscriber content preferences and frequency |
| `track_readership` | Track newsletter readership and engagement metrics |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/newsletter/create` | Create or generate |
| `POST` | `/api/v1/newsletter/analyze` | Analyze performance |
| `POST` | `/api/v1/newsletter/optimize` | Optimize |
| `POST` | `/api/v1/newsletter/schedule` | Schedule |
| `POST` | `/api/v1/newsletter/report` | Generate report |

## Features

- Newsletter
- Analytics
- Optimization

## Integrations

- Hubspot Marketing
- Marketo
- Mailchimp
- Google Analytics
- Meta Ads

## Architecture

```
newsletter-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── newsletter_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Marketing Platform + LLM + Analytics**

---

Built as part of the Enterprise AI Agent Platform.
