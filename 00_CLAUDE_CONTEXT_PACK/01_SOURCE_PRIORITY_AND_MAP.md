# DESCO AIPMS — Source Priority & Repository Map

**Document Role:** Authoritative source precedence hierarchy and complete mapping from logical knowledge sources to physical repository paths and Claude-readable extract companions.  
**Precedence Authority:** Derived directly from [CLAUDE.md](file:///e:/AI_Appraisal%20&%20Assesment/CLAUDE.md) §Source Priority and [00_CONTEXT_INDEX.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CONTEXT_INDEX.md) §4.

---

## 1. Source Precedence Hierarchy

When evaluating requirements, designing architecture, or resolving ambiguities, all AI models, Claude agents, and solution architects **MUST** strictly adhere to this rank ordering:

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│ [RANK 1] Revised DESCO AIPMS Terms of Reference (TOR)                           │
│          Contractual requirements, scope of work, technical modules, milestones   │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │ overrules
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│ [RANK 2] Official DESCO ACR Forms & ACR Instructions (Office Order)              │
│          Official appraisal criteria, scoring scales, performance bands, rules   │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │ overrules
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│ [RANK 3] Official DESCO Policies & Service Rules 2017                            │
│          Service conditions, conduct, disciplinary proceedings, asset rules       │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │ overrules
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│ [RANK 4] Current Consolidated R&D Handoff                                        │
│          Clean-slate architecture baseline, validated R&D decisions              │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │ overrules
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│ [RANK 5] Current Working Design Documents                                        │
│          AI Context Catalogue (Domains 1–3), Revised Classification & Workflow  │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │ overrules
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│ [RANK 6] Pre-Architecture Analysis Reports                                       │
│          Early risk identification, system contradictions, offline AI feasibility│
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Complete Logical Source to Physical Extract Mapping

### Rank 1: Authoritative Contractual Source

#### Logical Source: Revised DESCO AIPMS TOR (Terms of Reference)
- **Authority / Role:** Contractual project scope, core functional modules, AI advisory boundaries, integration constraints, security standards, deliverables, and payment schedule.
- **Actual Repository Path:**
  `01_AUTHORITATIVE_SOURCES/2026-08-18 DESCO_AIPMS_TOR_Revised_2_Final (Autosaved).docx`
- **Machine-Readable Extract Companion:**
  [TOR_FULL_EXTRACT.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/TOR_FULL_EXTRACT.md)
- **Status & Completeness:** 100% complete. Exact section numbers (Sections 1 to 10.1) and all tables preserved verbatim.

---

### Rank 2: Official Appraisal Instruments & Instructions

#### Logical Source: Official Grade 1–11 ACR Form (Officers)
- **Authority / Role:** Official annual appraisal schema for Pay Grades 1 to 11. Prescribes the 25 official performance metrics scored on a 1–4 scale across Parts 1 through 5.
- **Actual Repository Path:**
  `01_AUTHORITATIVE_SOURCES/ACR Format.pdf`
- **Machine-Readable Extract Companion:**
  [ACR_GRADE_1_11_FULL_EXTRACT.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_GRADE_1_11_FULL_EXTRACT.md)
- **Status & Completeness:** 100% complete. Transcribed from 150 DPI page renders. Covers cover, medical report, 12-item bio-data, all 25 assessment criteria, 1–4 scale, 5 performance bands, pen picture, recommendations, and multi-tier review blocks.

#### Logical Source: Official Grade 12–16 ACR Form (Staff)
- **Authority / Role:** Official annual appraisal schema for Pay Grades 12 to 16. Prescribes the 20 official performance metrics scored on a 1–5 scale across Parts 1 through 5.
- **Actual Repository Path:**
  `01_AUTHORITATIVE_SOURCES/ACR ফর্ম (গ্রেড ১২-১৬).pdf`
- **Machine-Readable Extract Companion:**
  [ACR_GRADE_12_16_FULL_EXTRACT.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_GRADE_12_16_FULL_EXTRACT.md)
- **Status & Completeness:** 100% complete. Transcribed from 150 DPI page renders. Covers cover, medical report, 11-item staff bio-data, all 20 assessment criteria, 1–5 scale, 5 performance bands, pen picture, recommendations, and multi-tier review blocks.

#### Logical Source: Official ACR Instructions / Office Order
- **Authority / Role:** Prescribes appraisal periodicity, the 3-month minimum supervision rule, adverse remark notification procedure, confidentiality sealing, and 4-tier reporting roles. Approved in 377th Board Meeting (07 April 2019).
- **Actual Repository Paths:**
  - Scanned Document: `01_AUTHORITATIVE_SOURCES/ACR_Instructions_Office_Order_Document.pdf`
  - Printout Stub: `01_AUTHORITATIVE_SOURCES/ACR_Instructions_Office_Order.pdf`
- **Machine-Readable Extract Companion:**
  [ACR_INSTRUCTIONS_OFFICE_ORDER_FULL_EXTRACT.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_INSTRUCTIONS_OFFICE_ORDER_FULL_EXTRACT.md)
- **Status & Completeness:** 100% complete. All 24 clauses transcribed verbatim in original Bengali with faithful English translations.

---

### Rank 3: Official DESCO Policies & Service Rules

#### Logical Source: DESCO Service Rules 2017
- **Authority / Role:** Employment manual governing recruitment, promotion policies (§3.3), annual increment link (§4.8), general conduct (§7.2), disciplinary penalties (§7.4), and inquiry procedure (§7.7).
- **Actual Repository Path:**
  `05_OFFICIAL_DESCO_POLICIES/DESCO_Service_Rule_2017.pdf`
- **Machine-Readable Extract Companion:**
  [DESCO_SERVICE_RULES_2017_EXTRACT.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/DESCO_SERVICE_RULES_2017_EXTRACT.md)
- **Status & Completeness:** Comprehensive institutional extract containing complete Table of Contents across Chapters 1–9, Verbatim Conduct & Disciplinary provisions, and Promotion/Increment rules.

#### Logical Source: DESCO Organogram 2018
- **Authority / Role:** Official company hierarchy, divisional structure, post taxonomy, and administrative levels.
- **Actual Repository Path:**
  `05_OFFICIAL_DESCO_POLICIES/DESCO_Organogram_2018.pdf`
- **Machine-Readable Extract Companion:**
  [DESCO_ORGANOGRAM_2018_EXTRACT.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/DESCO_ORGANOGRAM_2018_EXTRACT.md)
- **Status & Completeness:** 100% complete text extract across all 15 pages with explicit page boundaries.

#### Logical Source: Official Laptop PC Use Rules 2024
- **Authority / Role:** Institutional policy on device custody, authorized usage, cybersecurity controls (Active Directory, Windows Defender), password secrecy, and negligence liability.
- **Actual Repository Path:**
  `05_OFFICIAL_DESCO_POLICIES/Laptop_PC_Use_Rules_2024.pdf`
- **Machine-Readable Extract Companion:**
  [LAPTOP_PC_USE_RULES_2024_EXTRACT.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/LAPTOP_PC_USE_RULES_2024_EXTRACT.md)
- **Status & Completeness:** 100% complete. Transcribed across all 3 pages, including the administrative notice and all 20 operational clauses.

#### Logical Source: DESCO Code of Conduct
- **Authority / Role:** Ethical guidelines under BSEC Corporate Governance Code 2018. Strictly limited to Chairperson, Board Members, and CEO/Managing Director.
- **Actual Repository Path:**
  `05_OFFICIAL_DESCO_POLICIES/Code_of_ConductCode_of_Conduct.pdf`
- **Machine-Readable Extract Companion:**
  [CODE_OF_CONDUCT_EXTRACT.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/CODE_OF_CONDUCT_EXTRACT.md)
- **Status & Completeness:** 100% complete verbatim transcription of all 6 pages (Clauses 1–9, Independent Director code, and Annexure-1).

#### Logical Source: Official Policies Architecture Extract
- **Authority / Role:** Pre-compiled policy synthesis prepared for AI model ingestion.
- **Actual Repository Path:**
  `05_OFFICIAL_DESCO_POLICIES/OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT.md`
- **Machine-Readable Extract Companion:**
  [OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT_COMPANION.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT_COMPANION.md)
- **Status & Completeness:** 100% complete direct text mirror.

---

### Rank 4: Current Consolidated R&D Handoff

#### Logical Source: Complete R&D Architecture Handoff (Current Reference)
- **Authority / Role:** Current clean-slate architecture baseline consolidating metric classifications, open-world handling, pen-picture generation, and appraisal integrity rules.
- **Actual Repository Path:**
  `02_CURRENT_RND/DESCO_AIPMS_Complete_RnD_Architecture_Handoff_Current (1).md`
- **Machine-Readable Extract Companion:**
  [COMPLETE_RND_ARCHITECTURE_HANDOFF_EXTRACT.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/CURRENT_RND/COMPLETE_RND_ARCHITECTURE_HANDOFF_EXTRACT.md)
- **Status & Completeness:** 100% complete direct text mirror.

---

### Rank 5: Current Working Design Documents

#### Logical Source: Refined AI Context Catalogue V3 (Domains 1 to 3)
- **Authority / Role:** Open-world scenario examples, behavioral indicators, and boundary definitions mapping to official ACR metrics. (Internal AI routing construct only; does not score).
- **Actual Repository Path:**
  `03_CURRENT_WORKING_DESIGN/DESCO_AIPMS_AI_Context_Catalogue_V3_Domains_1_to_3 (2).docx`
- **Machine-Readable Extract Companion:**
  [AI_CONTEXT_CATALOGUE_V3_DOMAINS_1_TO_3_EXTRACT.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/CURRENT_WORKING_DESIGN/AI_CONTEXT_CATALOGUE_V3_DOMAINS_1_TO_3_EXTRACT.md)
- **Status & Completeness:** 100% complete. Extracted via python-docx, preserving all 131 paragraphs and 26 tables.

#### Logical Source: Revised Classification & Input Workflow
- **Authority / Role:** Defines evidence accumulation lifecycles, operational input workflows, notification triggers, and multi-stage appraisal reviews.
- **Actual Repository Path:**
  `03_CURRENT_WORKING_DESIGN/DESCO_AIPMS_Classification_and_Workflow_REVISED_after_review.pdf`
- **Machine-Readable Extract Companion:**
  [CLASSIFICATION_AND_WORKFLOW_REVISED_EXTRACT.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/CURRENT_WORKING_DESIGN/CLASSIFICATION_AND_WORKFLOW_REVISED_EXTRACT.md)
- **Status & Completeness:** 100% complete text extract across all 3 pages.

---

### Rank 6: Pre-Architecture Analysis Reports

#### Logical Source: Pre-Architecture R&D Report
- **Authority / Role:** Analysis of enterprise integration risks, system contradictions, offline AI constraints, and edge cases.
- **Actual Repository Path:**
  `04_PRE_ARCHITECTURE_ANALYSIS/DESCO_AIPMS_Architecture_RnD_Report.md`
- **Machine-Readable Extract Companion:**
  [PRE_ARCHITECTURE_ANALYSIS_REPORT_EXTRACT.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/PREVIOUS_ANALYSIS/PRE_ARCHITECTURE_ANALYSIS_REPORT_EXTRACT.md)
- **Status & Completeness:** 100% complete direct text mirror.

---

### Governance & Operating Instructions

#### Logical Source: Claude Operating Manual
- **Actual Repository Path:** `CLAUDE.md`
- **Extract Companion:** [CLAUDE_CORE_RULES_EXTRACT.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/REFERENCES/CLAUDE_CORE_RULES_EXTRACT.md)

#### Logical Source: Master Context Index & Workspace Guide
- **Actual Repository Path:** `00_CONTEXT_INDEX.md`
- **Extract Companion:** [CONTEXT_INDEX_MAP_EXTRACT.md](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/REFERENCES/CONTEXT_INDEX_MAP_EXTRACT.md)
