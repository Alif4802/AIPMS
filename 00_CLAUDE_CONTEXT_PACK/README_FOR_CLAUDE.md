# Claude Master Entry Point & Navigation Guide
**Context Pack Directory:** `00_CLAUDE_CONTEXT_PACK/`  
**Purpose:** Machine-readable mirror and index for LLM reasoning without runtime PDF/DOCX dependencies.

---

## 1. Mandatory Reading & Governance Protocol

When reasoning, answering questions, or designing for the DESCO AIPMS project, Claude/LLM agents **must** adhere to the following reading order and authority rules:

1. **Start with [`CLAUDE.md`](file:///e:/AI_Appraisal%20&%20Assesment/CLAUDE.md)**: Read the operational guardrails, non-negotiable architectural mandates, and core domain rules first.
2. **Read [`00_CONTEXT_INDEX.md`](file:///e:/AI_Appraisal%20&%20Assesment/00_CONTEXT_INDEX.md)**: Understand the document ecosystem, authoritative precedence, and repository layout.
3. **Use this Context Pack only as a readable representation/index**: The extracts in this directory exist so you do not need to parse binary PDF/DOCX/XLSX at runtime.
4. **Original project documents remain authoritative**: The files in `01_AUTHORITATIVE_SOURCES/`, `05_OFFICIAL_DESCO_POLICIES/`, etc., are the ground truth.
5. **Never let a derived summary override an authoritative source**: If a secondary analysis or downstream summary conflicts with a primary source extract, the primary source wins.
6. **Where an extract conflicts with its original, original wins**: The extracts are faithful transcriptions; any transcription discrepancy must yield to the original binary source.
7. **Do not treat R&D recommendations as DESCO policy**: Proposals in `02_CURRENT_RND/` or `04_PRE_ARCHITECTURE_ANALYSIS/` are technical research and engineering options, not official DESCO board-approved policies.
8. **Do not treat architecture proposals as confirmed requirements**: Unless explicitly mandated by the Revised TOR or an Official Office Order, architectural proposals are working hypotheses subject to review.
9. **Strictly preserve provenance distinctions**: You must explicitly distinguish between:
   - **Confirmed Institutional Fact** (e.g. DESCO is an autonomous power utility, organogram hierarchy, board orders)
   - **Contractual TOR Requirement** (e.g. clause 3.2.1 AI evaluation, clause 3.2.2 OCR, clause 4 security, clause 5 timeline)
   - **Official Policy** (e.g. Service Rules 2017, Code of Conduct, Laptop Rules 2024, ACR Office Order 2019)
   - **Current R&D Decision** (e.g. 5-engine evaluation pipeline, hybrid on-prem architecture in `02_CURRENT_RND/`)
   - **Architecture Recommendation** (e.g. event-driven workflow engine, database schema suggestions)
   - **Provisional Assumption** (e.g. estimated annual appraisal load of ~2,000 employees)
   - **Unresolved Clarification** (e.g. missing ACR forms for non-technical support staff, precise LDAP schema attributes)
10. **Check Source Map before claiming unavailability**: Before stating that a document, clause, or policy is missing or unavailable, consult [`01_SOURCE_PRIORITY_AND_MAP.md`](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/01_SOURCE_PRIORITY_AND_MAP.md) and its extracted companion.

---

## 2. Directory Navigation Map

```
00_CLAUDE_CONTEXT_PACK/
├── README_FOR_CLAUDE.md                    <-- This file (Master Entry Point)
├── 00_REPOSITORY_MANIFEST.md               <-- Complete inventory of all repo files, sizes, types, & status
├── 01_SOURCE_PRIORITY_AND_MAP.md           <-- 6-level precedence hierarchy & logical-to-physical mappings
├── 02_PRIMARY_SOURCE_VERIFICATION.md       <-- Exact status of critical primary source extractions
├── 03_DOCUMENT_RELATIONSHIP_MAP.md         <-- Downstream interpretation & provenance tracking
├── 99_EXTRACTION_GAPS.md                   <-- Explicit catalog of unextracted scans, gaps, or caveats
│
├── AUTHORITATIVE/                          <-- Primary contractual & official evaluation standards
│   ├── TOR_FULL_EXTRACT.md                 <-- Full text of Revised TOR with exact section numbers
│   ├── ACR_GRADE_1_11_FULL_EXTRACT.md      <-- Full extract of Officer ACR (All 25 criteria, 1-4 scale, 5 bands)
│   ├── ACR_GRADE_12_16_FULL_EXTRACT.md     <-- Full extract of Staff ACR (All 20 criteria, 1-5 scale, 5 bands)
│   └── ACR_INSTRUCTIONS_OFFICE_ORDER_FULL_EXTRACT.md <-- 24 official administrative instructions (Board 2019)
│
├── OFFICIAL_POLICIES/                      <-- Official company rules, conduct, and organogram
│   ├── DESCO_SERVICE_RULES_2017_EXTRACT.md <-- TOC Chapters 1-9, promotion (§3.3), increments, conduct/discipline (§7)
│   ├── DESCO_ORGANOGRAM_2018_EXTRACT.md    <-- 15-page structural hierarchy & division breakdown
│   ├── CODE_OF_CONDUCT_EXTRACT.md          <-- 6 pages of official corporate conduct & director obligations
│   ├── LAPTOP_PC_USE_RULES_2024_EXTRACT.md <-- 20 official IT security & asset management clauses
│   └── OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT_COMPANION.md <-- Synthesized architectural policy extract
│
├── CURRENT_RND/                            <-- Active engineering & pipeline specifications
│   └── COMPLETE_RND_ARCHITECTURE_HANDOFF_EXTRACT.md <-- Consolidated R&D handoff & 5-engine evaluation pipeline
│
├── CURRENT_WORKING_DESIGN/                 <-- Granular metric models & workflow definitions
│   ├── AI_CONTEXT_CATALOGUE_V3_DOMAINS_1_TO_3_EXTRACT.md <-- 131 paragraphs & 26 tables of evaluation metrics
│   └── CLASSIFICATION_AND_WORKFLOW_REVISED_EXTRACT.md    <-- OCR routing, review workflow & verification
│
├── PREVIOUS_ANALYSIS/                      <-- Pre-architecture gap analysis & institutional studies
│   └── PRE_ARCHITECTURE_ANALYSIS_REPORT_EXTRACT.md <-- Detailed foundational review of institutional readiness
│
└── REFERENCES/                             <-- Core rules & meta navigation
    ├── CLAUDE_CORE_RULES_EXTRACT.md        <-- Mirror of project operational instructions (CLAUDE.md)
    └── CONTEXT_INDEX_MAP_EXTRACT.md        <-- Mirror of repository context map (00_CONTEXT_INDEX.md)
```

---

## 3. Quick Links to Critical Primary Sources

For authoritative answers to appraisal criteria, scoring, legal procedures, or contractual TOR scope, navigate directly to:
- [Revised TOR Full Extract](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/TOR_FULL_EXTRACT.md)
- [Grade 1–11 ACR Form Full Extract](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_GRADE_1_11_FULL_EXTRACT.md)
- [Grade 12–16 ACR Form Full Extract](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_GRADE_12_16_FULL_EXTRACT.md)
- [ACR Instructions / Office Order Full Extract](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_INSTRUCTIONS_OFFICE_ORDER_FULL_EXTRACT.md)
- [Service Rules 2017 Extract](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/DESCO_SERVICE_RULES_2017_EXTRACT.md)
- [Code of Conduct Extract](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/CODE_OF_CONDUCT_EXTRACT.md)
- [Laptop & PC Use Rules 2024 Extract](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/LAPTOP_PC_USE_RULES_2024_EXTRACT.md)
