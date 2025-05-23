# MCP for MITRE ATT&CK Threat Detection

This repository provides a modern, modular framework for mapping real-world security detections and alerts to MITRE ATT&CK techniques, leveraging Retrieval-Augmented Generation (RAG) and the Model Context Protocol (MCP). The goal is to empower blue teamers and security analysts with rapid, auditable context for any detection or incident—using modern AI and open standards.

---

##  MITRE Use Case: Real-Time Threat Detection Contextualization

**Problem:**  
Security operations teams receive thousands of alerts and detections per day. Most are noisy or ambiguous—lacking context, mapping, or clear recommendations.  

**Solution:**  
This project lets you submit any alert, log message, or detection rule (e.g., SIGMA/Splunk) and instantly map it to the most relevant:
- **MITRE ATT&CK techniques**  
- **Detection rules and logic**  
- **CISA advisories and threat intelligence**  
- All results are searchable, explainable, and auditable for compliance and analyst workflows.

---

##  System Components

### Code Files

| File                         | Purpose                                                                |
|------------------------------|------------------------------------------------------------------------|
| `upload_to_chromadb.py`      | Loads all relevant CSV data into ChromaDB vector databases with context |
| `mcp_mitre_server.py`        | FastAPI server: exposes `/mcp` endpoint for semantic search (MITRE, Detections, CISA) |
| `mcp_memory_server.py`       | FastAPI server: stores/retrieves analyst session history               |
| `notebook/mitre_mcp_demo.ipynb` | Jupyter Notebook: main client and analyst workflow demo               |
| `requirements.txt`           | Python dependencies                                                    |

---

### Data Files

| File                         | Description                                                  |
|------------------------------|--------------------------------------------------------------|
| `mitreembed_master_Chroma.csv` | MITRE ATT&CK techniques, TTPs, descriptions, and metadata   |
| `master_detections.csv`      | Detection rules (e.g., SIGMA, Splunk), with logic and tags   |
| `CISA_combo_features_new.csv`| CISA advisories, CVEs, threat context, and mitigation info   |

- **Each detection rule is embedded with full context:** title, logic, tags, authors, and more—enabling accurate, explainable matching.
- **CISA and MITRE data provide regulatory, tactical, and threat context for each query.**

---

##  How It Works

1. **Upload CSVs to ChromaDB:**  
   Run `upload_to_chromadb.py` to vectorize and store MITRE, detections, and CISA datasets.

2. **Start the Servers:**  
   - Run `python mcp_mitre_server.py` for search and retrieval (port 8003 by default)
   - Run `python mcp_memory_server.py` for session history (port 8001)

3. **Analyze Alerts in the Notebook:**  
   - Use the Jupyter notebook to submit any alert, detection, or log.
   - The system queries each data source for the most relevant context (semantic search).
   - Optionally, synthesize a blue-team-ready answer with OpenAI or another LLM.
   - Log the Q&A to memory for traceability.

4. **Review History:**  
   - Analyst conversation history is stored in memory server—browsable at `/debug/memory`.

---

## 🛠️ Example Analyst Workflow

- Submit:  
  `"Hijack Legit RDP Session to Move Laterally"`
- System returns:
  - **Top MITRE techniques** (e.g., T1563.002)
  - **Relevant detection rules** with title, tags, and description
  - **CISA advisories** for the related threat/technique
- OpenAI (or another LLM) can synthesize a recommended action plan for the SOC analyst.
- The full session is logged for future audits.



---

## Quick Start

```bash
pip install -r requirements.txt
python upload_to_chromadb.py         # Index the data
python mcp_mitre_server.py           # Run search server (port 8003)
python mcp_memory_server.py          # Run memory/history server (port 8001)
