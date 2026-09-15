# DESCO AIPMS — Master Context Index & Repository Map

**Document Role:** Master Workspace Inventory & Navigation Index  
**Workspace Root:** `.` (DESCO AIPMS Project Root)  

---

## 1. Repository Directory Structure

```text
.
├── CLAUDE.md                                                       <-- Principal architect instructions & governance
├── 00_CONTEXT_INDEX.md                                             <-- This file (Master inventory & map)
│
├── 00_CLAUDE_CONTEXT_PACK/                                         <-- Machine-readable text extracts of binary/scanned files
│   ├── README_FOR_CLAUDE.md                                        <-- Master entry point for LLMs
│   │
│   ├── AUTHORITATIVE/                                              <-- Primary contractual & official appraisal extracts
│   │   ├── TOR_FULL_EXTRACT.md                                     <-- Revised TOR complete extract
│   │   ├── ACR_GRADE_1_11_FULL_EXTRACT.md                          <-- Officer ACR (25 criteria, 1–4 scale)
│   │   ├── ACR_GRADE_12_16_FULL_EXTRACT.md                         <-- Staff ACR (20 criteria, 1–5 scale)
│   │   └── ACR_INSTRUCTIONS_OFFICE_ORDER_FULL_EXTRACT.md          <-- 24 official administrative instructions (Board 377)
│   │
│   ├── OFFICIAL_POLICIES/                                          <-- Official institutional policy extracts
│   │   ├── DESCO_SERVICE_RULES_2017_EXTRACT.md                     <-- Service conditions, promotion, increments, discipline
│   │   ├── DESCO_ORGANOGRAM_2018_EXTRACT.md                        <-- Department & division hierarchy
│   │   ├── CODE_OF_CONDUCT_EXTRACT.md                             <-- Corporate conduct & director ethics
│   │   └── LAPTOP_PC_USE_RULES_2024_EXTRACT.md                     <-- IT asset custody & data security
│   │
│   └── CURRENT_WORKING_DESIGN/                                     <-- Working design extracts
│       ├── AI_CONTEXT_CATALOGUE_V3_DOMAINS_1_TO_3_EXTRACT.md      <-- Evidence indicator catalogue extract
│       └── CLASSIFICATION_AND_WORKFLOW_REVISED_EXTRACT.md         <-- Classification & review workflow extract
│
├── 01_AUTHORITATIVE_SOURCES/                                       <-- Authoritative original documents
│   ├── 2026-08-18 DESCO_AIPMS_TOR_Revised_2_Final (Autosaved).docx <-- Authoritative Revised TOR
│   ├── ACR Format.pdf                                              <-- Official Officer ACR Form (Grade 1–11)
│   ├── ACR ফর্ম (গ্রেড ১২-১৬).pdf                                 <-- Official Staff ACR Form (Grade 12–16)
│   └── ACR_Instructions_Office_Order_Document.pdf                  <-- Official ACR Office Order (Board 377)
│
├── 02_CURRENT_RND/                                                 <-- Non-authoritative engineering research
│   └── DESCO_AIPMS_Complete_RnD_Architecture_Handoff_Current (1).md<-- Current R&D working material to be evaluated
│
├── 03_CURRENT_WORKING_DESIGN/                                      <-- Non-authoritative working designs
│   ├── DESCO_AIPMS_AI_Context_Catalogue_V3_Domains_1_to_3 (2).docx<-- Working design: evidence indicators
│   └── DESCO_AIPMS_Classification_and_Workflow_REVISED_after_review.pdf <-- Working design: review routing flows
│
├── 04_PRE_ARCHITECTURE_ANALYSIS/                                   <-- Historical pre-architecture analysis
│   └── DESCO_AIPMS_Architecture_RnD_Report.md                      <-- Exploratory risk and gap analysis report
│
├── 05_OFFICIAL_DESCO_POLICIES/                                     <-- Official company policies & governance
│   ├── Code_of_ConductCode_of_Conduct.pdf                          <-- Official DESCO Code of Conduct
│   ├── DESCO_Organogram_2018.pdf                                   <-- Official DESCO Organogram (2018)
│   ├── DESCO_Service_Rule_2017.pdf                                 <-- Official DESCO Service Rules 2017
│   ├── Laptop_PC_Use_Rules_2024.pdf                                <-- Official Laptop & PC Use Rules 2024
│   └── OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT.md                   <-- Derived policy synthesis extract
│
└── tools/context_extraction/                                       <-- Development extraction utilities
    ├── extract_docx.py                                             <-- Programmatic DOCX extractor
    ├── extract_pdf.py                                              <-- Programmatic vector PDF extractor
    ├── build_manifest.py                                           <-- Manifest generation utility
    └── validate_context_pack.py                                    <-- Primary-source validation suite
```

---

## 2. Document Locations & Authority Scopes

### A. Authoritative Originals (`01_AUTHORITATIVE_SOURCES/`)
Primary contractual, legal, and institutional source documents:
- **Revised TOR (`.docx`):** Primary authority for contractual scope, deliverables, technical obligations, and milestones.
- **ACR Forms & Instructions (`.pdf`):** Primary authority for Grade 1–11 (25 criteria, 1–4 scale) and Grade 12–16 (20 criteria, 1–5 scale) official appraisal instruments, scoring scales, performance bands, 3-month supervision rule, and administrative procedures.

### B. Machine-Readable Extracts (`00_CLAUDE_CONTEXT_PACK/`)
Text companions provided strictly for LLM readability of binary DOCX and scanned PDF files. If an extract diverges from its physical source document, the original physical source governs.

### C. Official Company Policies (`05_OFFICIAL_DESCO_POLICIES/`)
Corporate governance and employment rules:
- **DESCO Service Rules 2017:** Primary authority for employment terms, promotion (§3.3), annual increment link (§4.8), and disciplinary due process (Chapter 7).
- **DESCO Organogram 2018:** Corporate organizational structure.
- **DESCO Code of Conduct:** Corporate ethics and governance boundaries. Applicability is limited to the Chairperson, Board Members and CEO/Managing Director as stated by the source. Do not apply it to ordinary employees unless another official source independently establishes the same rule.
- **Laptop & PC Use Rules 2024:** ICT equipment custody and cybersecurity standards.
- **OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT.md:** Architecture-relevant synthesis of Layer B policies.

### D. Engineering R&D & Working Designs (`02_CURRENT_RND/`, `03_CURRENT_WORKING_DESIGN/`, `04_PRE_ARCHITECTURE_ANALYSIS/`)
**Non-Authoritative Research & Working Material:**
- All proposals, pipeline architectures, context catalogues, workflow diagrams, and historical reports in these directories represent prior hypotheses and exploratory engineering work.
- They are subordinate to authoritative sources (Scopes A, B, and C) and must be independently evaluated from first principles. They do not represent approved architecture decisions.

---

## 3. Scope-Aware Authority Model

1. **Contractual Requirements & Scope:** Primary authority is the **Revised TOR**.
2. **Appraisal Instruments & Procedures:** Primary authority is the **Official ACR Forms & Office Order (BM 377)**.
3. **Institutional Governance & Service Rules:** Primary authority is **DESCO Service Rules 2017 & Official Policies**.
4. **Engineering & Research Material:** R&D handoffs, working designs, and pre-architecture reports are **non-authoritative research inputs**.

### Conflict Handling Protocol
If two primary authorities appear to conflict within overlapping scope, classify the issue as a `CROSS-SOURCE CONTRACTUAL/POLICY CONFLICT` and require explicit reconciliation. Lower-level R&D or working designs can never override primary sources.
