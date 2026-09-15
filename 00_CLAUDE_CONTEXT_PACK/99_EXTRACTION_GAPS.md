# Catalog of Extraction Gaps, Residual Scans, and Context Boundaries

**Document Purpose:** This document explicitly catalogs any gaps, partially extracted files, or external dependencies in `00_CLAUDE_CONTEXT_PACK/`. It ensures that Claude/LLM agents never guess unextracted text or assume the existence of documents not present in the repository.

---

## 1. Inventory of Extraction Completeness

| Target Source | Status in Context Pack | Extracted Content | Unextracted / Residual Content & Reason | Recommended Agent Action |
|---|---|---|---|---|
| **Revised DESCO AIPMS TOR** | **100% Complete** | All sections §1.0 to §10.1, deliverables, payment schedule, acronyms, and qualification tables. | None. Full verbatim text extracted. | Cite exact section numbers directly from `AUTHORITATIVE/TOR_FULL_EXTRACT.md`. |
| **Official Grade 1–11 ACR Form** | **100% Complete** | All 25 criteria, 1–4 scale, 5 performance bands, 12-item bio-data, 3-clause health report, 3-tier review blocks. | None. Full verbatim visual transcription across all 8 pages. | Rely directly on `AUTHORITATIVE/ACR_GRADE_1_11_FULL_EXTRACT.md`. |
| **Official Grade 12–16 ACR Form** | **100% Complete** | All 20 criteria, 1–5 scale, 5 performance bands, 11-item bio-data, health report, 3-tier review blocks. | None. Full verbatim visual transcription across all 8 pages. | Rely directly on `AUTHORITATIVE/ACR_GRADE_12_16_FULL_EXTRACT.md`. |
| **ACR Instructions / Office Order** | **100% Complete** | All 24 numbered clauses approved in Board Meeting 377 (07/04/2019) in Bengali original and English translation. | None. Full verbatim visual transcription. | Rely directly on `AUTHORITATIVE/ACR_INSTRUCTIONS_OFFICE_ORDER_FULL_EXTRACT.md`. |
| **DESCO Code of Conduct** | **100% Complete** | Clauses 1 to 9, Code for Independent Directors, Annexure-1 Affirmation Form across all 6 pages. | None. Full verbatim visual transcription. | Rely directly on `OFFICIAL_POLICIES/CODE_OF_CONDUCT_EXTRACT.md`. |
| **DESCO Laptop / PC Use Rules 2024** | **100% Complete** | Memo reference and all 20 numbered IT asset and cybersecurity clauses across all 3 pages. | None. Full verbatim visual transcription. | Rely directly on `OFFICIAL_POLICIES/LAPTOP_PC_USE_RULES_2024_EXTRACT.md`. |
| **DESCO Organogram 2018** | **100% Complete** | Structural hierarchy across all 15 pages extracted via PyMuPDF with page boundaries. | None. Vector text extracted. | Rely directly on `OFFICIAL_POLICIES/DESCO_ORGANOGRAM_2018_EXTRACT.md`. |
| **DESCO Service Rules 2017** | **Partial (Core Chapters)** | Complete Table of Contents (Chapters 1–9) and verbatim text for: <br>- §3.3 Promotion Rules<br>- §4.8 Annual Increment Rules<br>- §7.1–§7.12 Conduct & Discipline | Chapters 5 (Leave & Holidays), 6 (TA/DA Allowances), 8 (Retirement & Gratuity), and 9 (Misc) remain in the 63-page scanned PDF. These do not govern appraisal evaluation. | For general HR allowances, inspect original `05_OFFICIAL_DESCO_POLICIES/DESCO_Service_Rule_2017.pdf`. For appraisal rules, use `DESCO_SERVICE_RULES_2017_EXTRACT.md` and `OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT_COMPANION.md`. |

---

## 2. Specific Context & Knowledge Boundaries

### A. Earlier Architecture Phases ("PASS 1 Framing")
* **Status:** No standalone file named `PASS_1.docx` or `pass_1.pdf` exists in the repository root or subfolders.
* **Explanation:** "PASS 1" refers to an earlier conceptual architecture pass whose findings, limitations, and monolithic vs microservice tradeoffs were thoroughly critiqued and incorporated into [`04_PRE_ARCHITECTURE_ANALYSIS/DESCO_AIPMS_Architecture_RnD_Report.md`](file:///e:/AI_Appraisal%20&%20Assesment/04_PRE_ARCHITECTURE_ANALYSIS/DESCO_AIPMS_Architecture_RnD_Report.md) (and its extract [`PRE_ARCHITECTURE_ANALYSIS_REPORT_EXTRACT.md`](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/PREVIOUS_ANALYSIS/PRE_ARCHITECTURE_ANALYSIS_REPORT_EXTRACT.md)).
* **Rule for Claude:** Do not assume a standalone PASS 1 file is missing; its substantive content is preserved in the Pre-Architecture report.

### B. Legacy Populated ACR Dossiers
* **Status:** The repository contains the official blank statutory forms (`ACR Format.pdf` and `ACR ফর্ম (গ্রেড ১২-১৬).pdf`), but does **not** contain populated, historical ACR dossiers of real DESCO employees.
* **Explanation:** Employee appraisal records are confidential personnel records under DESCO Service Rules and Office Order Clause 18.
* **Rule for Claude:** When designing OCR data models, do not assume specific handwriting samples or actual employee IDs exist in the repo. Synthetic sample generation is required for OCR pipeline testing.

### C. External Enterprise Integration Schemas (ERP, SCADA, Active Directory)
* **Status:** The repository specifies the requirements to integrate with DESCO ERP, Biometric Attendance, Smart Metering/Billing, and Active Directory (TOR §3.1, §4.0; R&D Handoff §4). However, physical DDL schemas, API endpoint specs, and LDAP directory schemas are not stored in this repository.
* **Explanation:** These are client-side production schemas provided by DESCO IT during the Phase 1 Inception / Requirements Gathering stage.
* **Rule for Claude:** Treat external API endpoints as integration requirements with standard enterprise REST/SOAP/LDAP assumptions; do not invent proprietary DESCO ERP table schemas as confirmed facts.

---

## 3. Summary of Extraction Fidelity
No critical appraisal criteria, scoring formulas, evaluation bands, TOR clauses, or administrative instructions are missing. The primary contractual and assessment baseline is **100% verified and machine-readable**.
