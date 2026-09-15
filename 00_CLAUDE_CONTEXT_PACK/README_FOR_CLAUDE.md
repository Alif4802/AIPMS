# Claude Master Entry Point & Navigation Guide

**Context Pack Location:** `00_CLAUDE_CONTEXT_PACK/`  
**Purpose:** Machine-readable text extracts of scanned and binary documents to facilitate LLM reasoning without runtime binary parsing dependencies.

---

## Mandatory Reading & Authority Order

When reasoning, answering questions, or designing for the DESCO AIPMS project, adhere to the following sequence and principles:

1. **Read [`CLAUDE.md`](file:///e:/AI_Appraisal%20&%20Assesment/CLAUDE.md) first:** Understand operational governance, solution architect role, and scope-aware authority rules.
2. **Read [`00_CONTEXT_INDEX.md`](file:///e:/AI_Appraisal%20&%20Assesment/00_CONTEXT_INDEX.md):** Review repository structure, document roles, and authority boundaries.
3. **Read [`AUTHORITATIVE/`](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/) extracts:**
   - [`TOR_FULL_EXTRACT.md`](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/TOR_FULL_EXTRACT.md) — Contractual scope and requirements
   - [`ACR_GRADE_1_11_FULL_EXTRACT.md`](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_GRADE_1_11_FULL_EXTRACT.md) — Official Officer appraisal criteria (25 criteria, 1–4 scale)
   - [`ACR_GRADE_12_16_FULL_EXTRACT.md`](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_GRADE_12_16_FULL_EXTRACT.md) — Official Staff appraisal criteria (20 criteria, 1–5 scale)
   - [`ACR_INSTRUCTIONS_OFFICE_ORDER_FULL_EXTRACT.md`](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_INSTRUCTIONS_OFFICE_ORDER_FULL_EXTRACT.md) — 24 official administrative instructions (Board 377)
4. **Read [`OFFICIAL_POLICIES/`](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/) extracts:**
   - [`DESCO_SERVICE_RULES_2017_EXTRACT.md`](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/DESCO_SERVICE_RULES_2017_EXTRACT.md) — Service conditions, promotion, increments, discipline (Ch. 7)
   - [`DESCO_ORGANOGRAM_2018_EXTRACT.md`](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/DESCO_ORGANOGRAM_2018_EXTRACT.md) — Corporate organizational structure
   - [`CODE_OF_CONDUCT_EXTRACT.md`](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/CODE_OF_CONDUCT_EXTRACT.md) — Governance & ethics (limited to Board/MD unless independently established)
   - [`LAPTOP_PC_USE_RULES_2024_EXTRACT.md`](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/LAPTOP_PC_USE_RULES_2024_EXTRACT.md) — IT asset custody & data security
5. **Then read original R&D, working-design, and previous-analysis files:**
   - [`02_CURRENT_RND/DESCO_AIPMS_Complete_RnD_Architecture_Handoff_Current (1).md`](file:///e:/AI_Appraisal%20&%20Assesment/02_CURRENT_RND/DESCO_AIPMS_Complete_RnD_Architecture_Handoff_Current%20(1).md)
   - [`03_CURRENT_WORKING_DESIGN/`](file:///e:/AI_Appraisal%20&%20Assesment/03_CURRENT_WORKING_DESIGN/) (and its text extracts under [`00_CLAUDE_CONTEXT_PACK/CURRENT_WORKING_DESIGN/`](file:///e:/AI_Appraisal%20&%20Assesment/00_CLAUDE_CONTEXT_PACK/CURRENT_WORKING_DESIGN/))
   - [`04_PRE_ARCHITECTURE_ANALYSIS/DESCO_AIPMS_Architecture_RnD_Report.md`](file:///e:/AI_Appraisal%20&%20Assesment/04_PRE_ARCHITECTURE_ANALYSIS/DESCO_AIPMS_Architecture_RnD_Report.md)
   - [`05_OFFICIAL_DESCO_POLICIES/OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT.md`](file:///e:/AI_Appraisal%20&%20Assesment/05_OFFICIAL_DESCO_POLICIES/OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT.md)
6. **Existing R&D is non-authoritative:** Earlier research, pipeline ideas, and metric mappings are working hypotheses that must be independently evaluated from first principles.
7. **Originals win over extracts:** Physical source documents in `01_AUTHORITATIVE_SOURCES/` and `05_OFFICIAL_DESCO_POLICIES/` are the ground truth. Extracts exist strictly for LLM readability.
