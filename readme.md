# AGEsP-SDV

Agentic GenAI Service for Predictable Software-Defined Vehicle (SDV) Development.

## Problem

Software-Defined Vehicle (SDV) feature requirements are often high-level, ambiguous,
and difficult to convert into predictable, compliant, and testable vehicle software.

## Solution

AGEsP-SDV uses specialized Agentic GenAI components to transform SDV feature
requirements into structured, service-oriented software artifacts that are
extensible and suitable for downstream development and validation.

## Initial Agent Pipeline (PoC)

1. Requirement Agent ✅
2. Service Design Agent ✅
3. Code Generation Agent ✅

## Progress Log

### Session 1

* Project setup
* GitHub integration
* Initial agent architecture

### Session 2

* Requirement Agent v1 implemented
* Structured SDV service output defined
* Example input/output added

### Session 3

* Service Design Agent v1 implemented
* Requirement with Microservice mapping added
* Example microservice design output added

### Session 4

* Code Generation Agent v1 implemented
* Generated FastAPI microservice skeleton from service design output
* Added generated service folder

### Session 5
- Requirement Agent upgraded to local LLM-powered generation using Ollama
- Added JSON schema validation
- Added retry-on-invalid-output mechanism
- Integrated llama3.1 for SDV requirement extraction

## Current Status
- Requirement Agent v2 (LLM-powered) implemented
- Service Design Agent v1 implemented
- Code Generation Agent v1 implemented
- Local LLM integration via Ollama completed
- JSON schema validation added

## Next Steps
- Add multi-agent orchestration
- Implement Planner + Critic agents
- Improve code generation with API/data-contract awareness
- Add architecture diagram and workflow visualization