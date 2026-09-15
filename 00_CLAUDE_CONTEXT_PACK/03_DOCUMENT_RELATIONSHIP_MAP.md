# Document Relationship & Provenance Map

**Purpose:** This document records the structural, analytical, and operational relationships among all repository files. It enables Claude and human engineers to strictly distinguish **primary authoritative sources** from **downstream technical interpretations, R&D proposals, and architectural recommendations**.

---

## 1. High-Level Document Lineage

```
[ LEVEL 1: PRIMARY CONTRACTUAL & REGULATORY SOURCES ]
  ├── Revised DESCO AIPMS TOR (2026-08-18)
  ├── Official Grade 1–11 ACR Form (25 Criteria, 1–4 Scale)
  ├── Official Grade 12–16 ACR Form (20 Criteria, 1–5 Scale)
  └── ACR Instructions / Office Order (24 Board Clauses)
          │
          ├── (interprets & refines AI requirements)
          ▼
[ LEVEL 2: OFFICIAL INSTITUTIONAL POLICIES ]
  ├── DESCO Service Rules 2017 (Promotion, Increments, Discipline)
  ├── DESCO Organogram 2018 (Divisional Hierarchy & Reporting)
  ├── DESCO Code of Conduct (Integrity, Confidentiality)
  └── Laptop & PC Use Rules 2024 (ICT & Data Custody)
          │
          ├── (synthesizes legal & operational rules)
          ▼
[ LEVEL 3: POLICY SYNTHESIS ]
  └── OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT.md
          │
          ├── (informs engineering scope)
          ▼
[ LEVEL 4: CURRENT R&D DECISION & ARCHITECTURE HANDOFF ]
  └── AIPMS_COMPLETE_RND_ARCHITECTURE_HANDOFF.md
      (5-engine pipeline, hybrid deployment, auditability)
          │
          ├── (operationalizes into granular metric models)
          ▼
[ LEVEL 5: CURRENT WORKING DESIGN & CATALOGUES ]
  ├── AI Context Catalogue V3 (Domains 1–3 metric breakdown)
  └── Classification & Workflow Revised (OCR & routing flow)
          │
          ├── (built upon earlier foundational studies)
          ▼
[ LEVEL 6: PREVIOUS ANALYSIS & CONCEPTUAL FRAMING ]
  ├── DESCO AIPMS Architecture RnD Report (Pre-Architecture gap analysis)
  └── PASS 1 Architecture Framing (Early conceptual pass)
```

---

## 2. Granular Source-to-Interpretation Mappings

### A. Contractual TOR Provenance

* **Primary Source:**
  `01_AUTHORITATIVE_SOURCES/TOR/2026-08-18 DESCO_AIPMS_TOR_Revised_2_Final (Autosaved).docx`  
  *(Extract: `00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/TOR_FULL_EXTRACT.md`)*
* **Downstream Flow:**
  * **Interpreted by Current R&D Handoff** (`02_CURRENT_RND/AIPMS_COMPLETE_RND_ARCHITECTURE_HANDOFF.md`): Translates TOR §3.2.1 (AI evaluation) and §3.2.2 (OCR digitization) into a concrete 5-engine evaluation pipeline and hybrid on-premises architecture.
  * **Analyzed by Pre-Architecture Analysis** (`04_PRE_ARCHITECTURE_ANALYSIS/DESCO_AIPMS_Architecture_RnD_Report.md`): Identifies institutional gaps between legacy paper workflows and TOR requirements.
  * **Referenced by PASS 1 Architecture Framing**: Grounded early system component definitions against TOR scope.
* **Interpretation Guardrail:**
  * *TOR Requirement* = Legally binding contractual deliverable.
  * *R&D Pipeline* = Recommended technical implementation of that deliverable. If R&D recommends a specific model or library not stated in the TOR, that remains an engineering proposal, not a TOR requirement.

---

### B. Official ACR Evaluation Instruments & Office Order Provenance

* **Primary Sources:**
  1. `01_AUTHORITATIVE_SOURCES/ACR_FORMS_AND_INSTRUCTIONS/ACR Format.pdf` *(Extract: `AUTHORITATIVE/ACR_GRADE_1_11_FULL_EXTRACT.md`)*
  2. `01_AUTHORITATIVE_SOURCES/ACR_FORMS_AND_INSTRUCTIONS/ACR ফর্ম (গ্রেড ১২-১৬).pdf` *(Extract: `AUTHORITATIVE/ACR_GRADE_12_16_FULL_EXTRACT.md`)*
  3. `01_AUTHORITATIVE_SOURCES/ACR_FORMS_AND_INSTRUCTIONS/ACR_Instructions_Office_Order_Document.pdf` *(Extract: `AUTHORITATIVE/ACR_INSTRUCTIONS_OFFICE_ORDER_FULL_EXTRACT.md`)*
* **Downstream Flow:**
  * **Reflected in AI Context Catalogue V3** (`03_CURRENT_WORKING_DESIGN/AI_Context_Catalogue_V3_Domains_1-3.docx`): Maps each official ACR criterion (25 for officers, 20 for staff) to specific organizational evidence sources, ERP databases, SCADA logs, and self-appraisal submissions.
  * **Reflected in Classification & Workflow** (`03_CURRENT_WORKING_DESIGN/Classification and AIPMS Workflow Revised.pdf`): Adapts the 3-tier reporting officer flow (Reporting Officer -> Countersigning Officer -> Approving Authority) from the forms and Office Order into an automated digital routing pipeline with OCR document ingestion.
  * **Reflected in R&D Handoff**: Embedded within Domain Engine 1 (Objective KPIs) and Domain Engine 2 (Behavioral Competencies).
* **Interpretation Guardrail:**
  * *Official Form* = Fixed statutory appraisal rubric with exact criteria names, weights, and scoring thresholds.
  * *AI Context Catalogue* = Feature-engineering mapping connecting data sources to the rubric. The catalogue must conform to the form, never the reverse.

---

### C. DESCO Institutional Policies Provenance

* **Primary Sources:**
  1. `05_OFFICIAL_DESCO_POLICIES/DESCO_Service_Rule_2017.pdf` *(Extract: `OFFICIAL_POLICIES/DESCO_SERVICE_RULES_2017_EXTRACT.md`)*
  2. `05_OFFICIAL_DESCO_POLICIES/Code_of_ConductCode_of_Conduct.pdf` *(Extract: `OFFICIAL_POLICIES/CODE_OF_CONDUCT_EXTRACT.md`)*
  3. `05_OFFICIAL_DESCO_POLICIES/Laptop_PC_Use_Rules_2024.pdf` *(Extract: `OFFICIAL_POLICIES/LAPTOP_PC_USE_RULES_2024_EXTRACT.md`)*
  4. `05_OFFICIAL_DESCO_POLICIES/DESCO Organogram- 2018 (Final)-1.pdf` *(Extract: `OFFICIAL_POLICIES/DESCO_ORGANOGRAM_2018_EXTRACT.md`)*
* **Downstream Flow:**
  * **Synthesized into Architectural Constraints** (`05_OFFICIAL_DESCO_POLICIES/OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT.md`): Summarizes disciplinary trigger thresholds (Service Rules Chapter 7), role conflict restrictions (Code of Conduct), IT security mandates (Laptop Rules), and reporting lines (Organogram).
  * **Informs System Security & Governance in R&D Handoff**: Drives the Role-Based Access Control (RBAC) model, data residency mandates, and audit trail retention requirements.
* **Interpretation Guardrail:**
  * *DESCO Policy* = Non-negotiable enterprise compliance boundary.
  * *AIPMS Architecture* = System mechanism that enforces compliance. The system cannot create new disciplinary penalties or alter reporting lines established by the board.

---

## 3. Provenance Differentiation Matrix

To avoid confusing source facts with engineering proposals, use this table when citing repository knowledge:

| Information Type | Example In Repository | Authority Level | Can Claude Modify or Propose Changes? |
|---|---|---|---|
| **Contractual Obligation** | TOR Clause 3.2.1 (AI scoring, confidence score, explainability) | Inviolable | **NO.** Must be satisfied as written. |
| **Official Statutory Rubric** | 25 criteria for Grade 1–11; 20 criteria for Grade 12–16 | Inviolable | **NO.** System must evaluate against official criteria. |
| **Administrative Procedure** | 3-month reporting rule, adverse remark review (Office Order) | Inviolable | **NO.** Workflow must honor official rules. |
| **Corporate Policy** | Laptop custody, password rules, conflict of interest disclosure | Inviolable | **NO.** System security must conform to policy. |
| **Current R&D Recommendation** | 5-engine evaluation pipeline, local LLM deployment, FastAPI backend | Technical Recommendation | **YES, with justification.** Engineering design is subject to architecture iteration. |
| **Working Design Specification** | Feature weights and metric indicators in Context Catalogue V3 | Working Design | **YES.** Can be refined during detailed system design. |
| **Pre-Architecture Assessment** | Gap analysis of legacy records, OCR risk evaluations | Historical Analysis | Contextual only. Informs risks and assumptions. |
| **Provisional Assumption** | Estimated 2,000 active employees, specific GPU hardware specs | Assumption | Subject to formal validation with DESCO IT/HR. |
