# Secure Model Context Protocol (MCP) Pipeline for MITRE ATT&CK Threat Detection

This repository provides a secure, modular implementation of the **Model Context Protocol (MCP)** applied to **MITRE ATT&CK-based threat detection and response**. The notebook and microservices demonstrate how to integrate large language models (LLMs) with dynamic retrieval from MITRE techniques, threat logs, PDF reports, and incident histories—all while following robust coding and security practices.

---

## 📚 Key Features

- **MITRE-centric RAG Architecture**: Retrieve, map, and synthesize threat events, alerts, and logs against MITRE ATT&CK techniques at inference time.
- **Microservices via MCP**: Modular servers for memory (incident history), MITRE technique/context search, and orchestration.
- **Security Best Practices**: Includes authentication, strict input validation, logging, and supply chain safeguards.
- **Traceable Threat Explanation**: LLM answers are grounded in context and cite MITRE IDs, PDF pages, or log sources for auditability.

---

## 🛡️ Security Principles in the MITRE Pipeline

- **Separation of Duties**: Each MCP server is dedicated (memory, MITRE lookup, PDF/IOC search), reducing lateral movement risk.
- **Transport & Protocol Security**: JSON-RPC used to keep LLM/prompt logic separated from transport, minimizing prompt injection and tooling abuse.
- **Input Validation**: All server endpoints validate input data to prevent malformed queries and injection risks.
- **Forensic Logging**: Every event/query is timestamped and logged to enable incident response and auditing.
- **No Hardcoded Secrets**: All sensitive configuration is environment-managed.

---

## 🏗️ System Overview

```mermaid
graph TD;
    A[Analyst/LLM Client] -->|JSON-RPC| B[MCP Orchestrator];
    B -->|search_mitre| C[MITRE Vector Server];
    B -->|search_alerts| D[Alert Log Server];
    B -->|search_pdfs| E[PDF/IOC Server];
    B -->|insert_memory/fetch_memory| F[Incident Memory Server];
    C --> G[MITRE ATT&CK DB/CSV];
    D --> H[Security Events/Logs];
    E --> I[Threat Reports & PDFs];
