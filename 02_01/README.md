# Model Context Protocol (MCP) — Hands-on Introduction

Welcome to the hands-on lab for the **Model Context Protocol (MCP)**!  
This notebook introduces MCP—a secure, standardized protocol that allows AI models to interact safely and contextually with enterprise systems. MCP is critical for cybersecurity teams and GRC professionals seeking to automate, audit, and defend organizational workflows with AI.

---

## What is the Model Context Protocol (MCP)?

**MCP** is an open, message-based protocol (often implemented over JSON-RPC) that securely connects AI systems to enterprise tools and data—*with full context and governance*.

It allows you to:
- Standardize and secure tool invocation by AI models (e.g., accessing logs, running compliance checks, fetching policies)
- Audit and control AI model actions and data access
- Enhance blue team automation, real-time compliance, and robust defense against prompt injection or tool misuse

---

## Who is this for?

- **Cybersecurity defenders and blue teams:** Automate detection, response, and compliance.
- **GRC (Governance, Risk, and Compliance) professionals:** Implement real-time controls, automate audits, and manage risk across complex environments.
- **Developers & architects:** Understand secure, modular AI system design.

---

## What's in this Notebook?

You’ll explore:
- **MCP Architecture & Roles**: Host, client, server breakdown
- **JSON-RPC Communication**: Standardized, auditable messaging
- **Tooling**: Example code for an MCP server, memory server, and GRC workflows
- **Security**: Real-world risks, security controls, and safe design
- **Practical labs**: Try out core MCP requests and responses

Each code block is fully annotated. If you run the notebook, you’ll see live outputs and be able to modify parameters for experimentation.

---

## Notebook Sections and Code Explanations

### 1. MCP Architecture: Hosts, Clients, and Servers
- **Host**: Orchestrates the system (e.g., a security platform or chatbot).
- **Client**: Manages connection and communication with MCP servers.
- **Server**: Wraps a data source, tool, or capability—exposing them in a secure, standardized way.

_Example: The notebook will show how a GRC policy database or ticketing tool becomes accessible to an AI agent through an MCP server, all via auditable APIs._

---

### 2. JSON-RPC: The Messaging Protocol
- MCP messages use JSON-RPC 2.0:  
  - Every action is a request or response (with clear method names, parameters, and unique IDs).
  - All interactions are traceable—crucial for compliance and incident investigation.
- **Sample Request/Response:**  
  The notebook provides example payloads (e.g., requesting a compliance check or fetching evidence).

---

### 3. MCP Memory Server Example
- **Purpose**: Demonstrates a minimal MCP server (FastAPI + in-memory store) for session-based memory or logs.
- **Key Code:**
  - `@app.post("/mcp")`: Accepts JSON-RPC requests to insert or fetch memory for a session
  - `@app.get("/debug/memory")`: Lets you see the full in-memory audit/log (great for debugging!)

**Educational Focus**: See how session data and user actions can be securely logged and retrieved—an essential piece for both blue teams and GRC auditing.

---

### 4. GRC Use Case: Real-World Scenario
- The notebook walks through how MCP servers can power use cases like:
  - Checking whether a business unit is subject to new regulations (e.g., DORA, GDPR, NY SHIELD)
  - Auditing evidence across multiple sources
  - Automating documentation and compliance reporting

---

### 5. Security Best Practices
- **Risks addressed:** Tool poisoning, prompt injection, unauthorized tool invocation
- **Controls:**  
  - Context enforcement (never act outside approved context)
  - Strong authentication & authorization on servers
  - Auditable logging
  - Secure deployment guidance (e.g., running MCP servers in isolated containers, integrating with SIEM/SOAR for alerts)

---

### 6. Hands-on: Run & Extend
- Run each cell and observe outputs
- Modify server code to add your own methods or security checks
- Try integrating with a different tool (e.g., a ticketing system, log archive, or regulatory policy database)

---

## How to Use This Notebook

1. **Setup**  
   - Install Python 3.9+, FastAPI, and Uvicorn if running locally  
     ```
     pip install fastapi uvicorn
     ```
2. **Run the example MCP memory server**  
   - Open a terminal:
     ```
     uvicorn mcp_memory_server:app --reload
     ```
3. **Run notebook cells**  
   - Experiment with JSON-RPC requests using `requests` library or Postman

---

## Key Files (If Provided)
- **`mcp_memory_server.py`**: Example MCP-compliant memory server (audit log store)
- **`full_mcp_notebook.ipynb`**: This interactive walkthrough and code samples
- **Additional scripts**: (e.g., `mcp_grc_server.py`) may provide real-world tool integration or GRC workflows

---

## Further Reading & References

- **Model Context Protocol (MCP)**: [Project documentation](https://github.com/modelcontext/protocol) (if public)
- **NIST Cybersecurity Framework 2.0**: Learn about standard security and compliance controls ([NIST CSF](https://www.nist.gov/cyberframework))
- **NY SHIELD Act**, **GDPR**, **SOC 2**: Explore the compliance landscape referenced in the use cases

---

## Questions?  
Experiment, modify, and reach out via LinkedIn Learning Q&A for support.  
We encourage you to adapt the code to your organization's tools, data sources, and regulatory environment!

---

# Start exploring and secure your AI workflows with MCP!
