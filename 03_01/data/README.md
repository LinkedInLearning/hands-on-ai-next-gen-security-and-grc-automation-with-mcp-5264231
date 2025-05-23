---

##  Data File Details

### `mitreembed_master_Chroma.csv`
- Contains: MITRE ATT&CK techniques, their descriptions, IDs, references, and relationships.
- Used to map alerts to standardized adversary behaviors.

### `master_detections.csv`
- Contains: Detection rule name, description, logic, tags, references, false positive guidance, and more.
- All fields are combined into a single document for vector search to maximize match quality.

### `CISA_combo_features_new.csv`
- Contains: CISA advisories, threat actor campaigns, vulnerabilities, mitigation strategies, dates, and related metadata.
- Used to provide up-to-date threat intelligence context for each query.
