# MCP System File Overview

This repository includes the core code, data, and reference documents necessary for working with the Model Context Protocol (MCP) system for secure, context-aware integration of AI models in enterprise environments. Below is a brief description of each major file in the repo.

---

## Python Source Code

### `mcp_server.py`
The main server implementation for the MCP protocol. Handles incoming requests, processes messages, and serves as the core communication bridge between MCP clients and available services or data sources.

### `mcp_grc_server.py`
An MCP server specifically designed for Governance, Risk, and Compliance (GRC) use cases. It extends or customizes the main MCP server with compliance-specific logic, such as mapping queries to regulatory requirements or controls.

### `mcp_memory_server.py`
Implements a memory-capable MCP server, providing persistent context or session-based information to augment MCP workflows. Useful for maintaining conversational or analytical state across multiple queries.

---

## Data Files

### `trustlayer_intake_example_cleaned_final_v3.csv`
An example company intake form, typically used for gathering initial assessment data from clients or systems. This file is used in the GRC context to simulate or perform readiness assessments (e.g., for SOC 2, NIST CSF, GDPR).

### `external_regulations.csv`
A database of external regulations, standards, or requirements relevant to compliance checks (such as GDPR, NIST CSF, NY SHIELD, etc.). Used for automated mapping, gap analysis, or regulatory lookups by the MCP system.

---

## Reference Documents

### `SOC_2_Report_Example.pdf`
A sample SOC 2 Type II report. Used as a template or reference for generating audit reports, understanding control requirements, or benchmarking organizational compliance.

### `NIST_original_cybersecurity_framework_021214.pdf`
The original NIST Cybersecurity Framework (CSF) v1.0, which provides foundational controls, categories, and methodology for managing and reducing cybersecurity risks.

### `NIST_CSWP_29.pdf`
NIST Cybersecurity Framework (CSF) 2.0, the latest version of the framework, emphasizing risk governance, updated categories, and new organizational guidance for cybersecurity best practices.

### `GDPR.pdf`
The full text of the General Data Protection Regulation, used as a legal and regulatory reference for privacy, data handling, and compliance requirements within the MCP and GRC context.

### `NYSHIELD.pdf`
The New York SHIELD Act in PDF form. Provides requirements and definitions for organizations that must comply with NY data protection and breach notification statutes.

---

## Usage Guidance

- **Servers:** Start with `mcp_server.py` to run the core MCP protocol, then use specialized servers as needed for memory or GRC applications.
- **Data Files:** Use the CSVs as sample input for compliance readiness checks or regulatory mappings.
- **Reference Documents:** Consult these PDFs for understanding the regulatory landscape, extracting control requirements, or as answer sources for the MCP system.

---

## Contributing

If you add new files or servers, please update this document with a brief description!

