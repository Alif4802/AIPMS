# DESCO AIPMS — Context Index

This repository contains the current source pack for DESCO AIPMS architecture work.

## Repository Structure

```text
DESCO_AIPMS/
├── CLAUDE.md
├── 00_CONTEXT_INDEX.md
├── 01_AUTHORITATIVE_SOURCES/
├── 02_OFFICIAL_DESCO_POLICIES/
├── 03_CURRENT_RND/
├── 04_CURRENT_AI_CONTEXT_DESIGN/
└── 05_PRE_ARCHITECTURE_ANALYSIS/
```

## 01_AUTHORITATIVE_SOURCES

Primary project and appraisal source documents.

Expected contents:

- Revised DESCO AIPMS TOR
- Official DESCO ACR — Grade 1–11
- Official DESCO ACR — Grade 12–16
- ACR Instructions / Office Order

Use these to establish official appraisal structure, scoring, hierarchy, workflow requirements, system scope, and contractual technical requirements.

## 02_OFFICIAL_DESCO_POLICIES

Supporting DESCO policy and organizational context.

Expected contents:

- DESCO Service Rule 2017
- DESCO Organogram 2018
- Laptop PC Use Rules 2024
- DESCO Code of Conduct

Important applicability note:

The DESCO Code of Conduct provided here applies to the Chairperson, Board members, and CEO/Managing Director. Do not generalize it as the ordinary employee conduct policy unless the same rule is independently supported by another applicable DESCO source.

Use the Organogram for realistic role/department context, not as a replacement for appraisal authority assignments.

## 03_CURRENT_RND

Current consolidated R&D handoff.

Expected contents:

- `DESCO_AIPMS_Complete_RnD_Architecture_Handoff_Current.md`

This captures the current validated working decisions, unresolved policy questions, evidence-model direction, AI boundaries, appraisal-integrity concerns, and architecture preparation decisions.

Treat it as current R&D guidance, subordinate to official DESCO sources.

## 04_CURRENT_AI_CONTEXT_DESIGN

Current AI evidence-mapping and workflow design.

Expected contents:

- Revised Classification & Workflow document
- Refined AI Context Catalogue V3 — Domains 1–3

Important rules:

- The 10 domains are AI context/routing constructs only.
- Official ACR metrics remain the appraisal outputs.
- Domains do not receive scores.
- Scenarios are open-world examples, not closed policy rules.
- Scenario polarity does not directly determine annual marks.
- Metric boundaries are important and should be preserved.

## 05_PRE_ARCHITECTURE_ANALYSIS

Current pre-HLD / pre-SDD analysis.

Expected contents:

- `DESCO_AIPMS_Architecture_RnD_Report.md`

Use this for identified contradictions, architecture risks, policy gaps, and first-principles analysis.

Do not treat recommendations in this document as official DESCO policy unless they are supported by higher-priority sources.

## Source Priority

When reasoning, use this precedence:

1. Revised DESCO AIPMS TOR
2. Official DESCO ACR forms and ACR instructions
3. Official DESCO policies and Service Rules
4. Current consolidated R&D handoff
5. Current classification/workflow and AI context catalogue
6. Pre-architecture analysis

If two sources conflict:

1. state the conflict explicitly;
2. cite or name the conflicting sources;
3. identify the architectural impact;
4. classify what requires DESCO clarification;
5. do not silently invent a resolution.

## Working Rule

Before making a major architecture decision, inspect the relevant source documents rather than relying only on summaries.

Keep these categories separate:

- **Confirmed source fact**
- **Current working decision**
- **Architecture recommendation**
- **DESCO policy decision / unresolved clarification**
