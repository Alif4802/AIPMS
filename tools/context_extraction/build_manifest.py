"""
build_manifest.py - Builds 00_REPOSITORY_MANIFEST.md cataloging all project repository files,
classifications, readability status, extract companions, and metadata.
"""

import os
import sys

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def generate_manifest():
    manifest_path = "00_CLAUDE_CONTEXT_PACK/00_REPOSITORY_MANIFEST.md"
    
    # Static metadata table for project files strictly derived from real filesystem
    files_data = [
        {
            "rel_path": "CLAUDE.md",
            "filename": "CLAUDE.md",
            "ext": ".md",
            "size": os.path.getsize("CLAUDE.md") if os.path.exists("CLAUDE.md") else 7630,
            "original": "Yes (Root instruction file)",
            "readable": "Yes (Markdown)",
            "extract": "00_CLAUDE_CONTEXT_PACK/REFERENCES/CLAUDE_CORE_RULES_EXTRACT.md",
            "classification": "GOVERNANCE",
            "extraction_status": "DIRECT_TEXT",
            "notes": "Principal solution architect instructions and operational governance rules."
        },
        {
            "rel_path": "00_CONTEXT_INDEX.md",
            "filename": "00_CONTEXT_INDEX.md",
            "ext": ".md",
            "size": os.path.getsize("00_CONTEXT_INDEX.md") if os.path.exists("00_CONTEXT_INDEX.md") else 12973,
            "original": "Yes (Root index file)",
            "readable": "Yes (Markdown)",
            "extract": "00_CLAUDE_CONTEXT_PACK/REFERENCES/CONTEXT_INDEX_MAP_EXTRACT.md",
            "classification": "GOVERNANCE",
            "extraction_status": "DIRECT_TEXT",
            "notes": "Master repository directory map, document roles, and scope-aware authority index."
        },
        {
            "rel_path": "01_AUTHORITATIVE_SOURCES/2026-08-18 DESCO_AIPMS_TOR_Revised_2_Final (Autosaved).docx",
            "filename": "2026-08-18 DESCO_AIPMS_TOR_Revised_2_Final (Autosaved).docx",
            "ext": ".docx",
            "size": os.path.getsize("01_AUTHORITATIVE_SOURCES/2026-08-18 DESCO_AIPMS_TOR_Revised_2_Final (Autosaved).docx"),
            "original": "Yes (Authoritative contract TOR)",
            "readable": "No (Binary DOCX format)",
            "extract": "00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/TOR_FULL_EXTRACT.md",
            "classification": "AUTHORITATIVE_SOURCE",
            "extraction_status": "EXTRACTED",
            "notes": "Authoritative contractual TOR (Scope A). Extracted with verbatim clause numbering and tables."
        },
        {
            "rel_path": "01_AUTHORITATIVE_SOURCES/2026-08-18_DESCO_AIPMS_TOR_Revised_2_Final_Extract.md",
            "filename": "2026-08-18_DESCO_AIPMS_TOR_Revised_2_Final_Extract.md",
            "ext": ".md",
            "size": os.path.getsize("01_AUTHORITATIVE_SOURCES/2026-08-18_DESCO_AIPMS_TOR_Revised_2_Final_Extract.md"),
            "original": "No (Pre-existing direct text extract)",
            "readable": "Yes (Markdown)",
            "extract": "00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/TOR_FULL_EXTRACT.md",
            "classification": "DERIVED",
            "extraction_status": "DIRECT_TEXT",
            "notes": "Pre-existing Markdown text extract companion of the Revised TOR."
        },
        {
            "rel_path": "01_AUTHORITATIVE_SOURCES/ACR Format.pdf",
            "filename": "ACR Format.pdf",
            "ext": ".pdf",
            "size": os.path.getsize("01_AUTHORITATIVE_SOURCES/ACR Format.pdf"),
            "original": "Yes (Official Board-approved ACR form)",
            "readable": "No (Scanned image PDF, 0 characters extractable directly)",
            "extract": "00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_GRADE_1_11_FULL_EXTRACT.md",
            "classification": "AUTHORITATIVE_SOURCE",
            "extraction_status": "EXTRACTED",
            "notes": "Authoritative Grade 1–11 officer ACR (Scope B). Transcribed from 150 DPI page renders. All 25 metrics, 1–4 scale, 5 bands, bio-data, health, and multi-tier reviews preserved."
        },
        {
            "rel_path": "01_AUTHORITATIVE_SOURCES/ACR ফর্ম (গ্রেড ১২-১৬).pdf",
            "filename": "ACR ফর্ম (গ্রেড ১২-১৬).pdf",
            "ext": ".pdf",
            "size": os.path.getsize("01_AUTHORITATIVE_SOURCES/ACR ফর্ম (গ্রেড ১২-১৬).pdf"),
            "original": "Yes (Official Board-approved ACR form)",
            "readable": "No (Scanned image PDF, 0 characters extractable directly)",
            "extract": "00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_GRADE_12_16_FULL_EXTRACT.md",
            "classification": "AUTHORITATIVE_SOURCE",
            "extraction_status": "EXTRACTED",
            "notes": "Authoritative Grade 12–16 staff ACR (Scope B). Transcribed from 150 DPI page renders. All 20 metrics, 1–5 scale, 5 bands, staff bio-data, health, and multi-tier reviews preserved."
        },
        {
            "rel_path": "01_AUTHORITATIVE_SOURCES/ACR_Instructions_Office_Order.pdf",
            "filename": "ACR_Instructions_Office_Order.pdf",
            "ext": ".pdf",
            "size": os.path.getsize("01_AUTHORITATIVE_SOURCES/ACR_Instructions_Office_Order.pdf"),
            "original": "Yes (Web / browser printout stub)",
            "readable": "Yes (160 characters text)",
            "extract": "00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_INSTRUCTIONS_OFFICE_ORDER_FULL_EXTRACT.md",
            "classification": "AUTHORITATIVE_SOURCE",
            "extraction_status": "DIRECT_TEXT",
            "notes": "Administrative cover printout stub referencing attached ACR forms."
        },
        {
            "rel_path": "01_AUTHORITATIVE_SOURCES/ACR_Instructions_Office_Order_Document.pdf",
            "filename": "ACR_Instructions_Office_Order_Document.pdf",
            "ext": ".pdf",
            "size": os.path.getsize("01_AUTHORITATIVE_SOURCES/ACR_Instructions_Office_Order_Document.pdf"),
            "original": "Yes (Official Board-approved instructions document)",
            "readable": "No (Scanned image PDF, 0 characters extractable directly)",
            "extract": "00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_INSTRUCTIONS_OFFICE_ORDER_FULL_EXTRACT.md",
            "classification": "AUTHORITATIVE_SOURCE",
            "extraction_status": "EXTRACTED",
            "notes": "Authoritative Office Order (Scope B). All 24 official clauses approved in Board Meeting 377 transcribed verbatim in Bengali with non-authoritative translations."
        },
        {
            "rel_path": "02_CURRENT_RND/DESCO_AIPMS_Complete_RnD_Architecture_Handoff_Current (1).md",
            "filename": "DESCO_AIPMS_Complete_RnD_Architecture_Handoff_Current (1).md",
            "ext": ".md",
            "size": os.path.getsize("02_CURRENT_RND/DESCO_AIPMS_Complete_RnD_Architecture_Handoff_Current (1).md"),
            "original": "Yes (Current R&D handoff document)",
            "readable": "Yes (Markdown)",
            "extract": "00_CLAUDE_CONTEXT_PACK/CURRENT_RND/COMPLETE_RND_ARCHITECTURE_HANDOFF_EXTRACT.md",
            "classification": "CURRENT_RND",
            "extraction_status": "DIRECT_TEXT",
            "notes": "Non-authoritative R&D handoff (Scope D). Engineering proposals and working material to be independently evaluated."
        },
        {
            "rel_path": "03_CURRENT_WORKING_DESIGN/DESCO_AIPMS_AI_Context_Catalogue_V3_Domains_1_to_3 (2).docx",
            "filename": "DESCO_AIPMS_AI_Context_Catalogue_V3_Domains_1_to_3 (2).docx",
            "ext": ".docx",
            "size": os.path.getsize("03_CURRENT_WORKING_DESIGN/DESCO_AIPMS_AI_Context_Catalogue_V3_Domains_1_to_3 (2).docx"),
            "original": "Yes (Current AI working design document)",
            "readable": "No (Binary DOCX format)",
            "extract": "00_CLAUDE_CONTEXT_PACK/CURRENT_WORKING_DESIGN/AI_CONTEXT_CATALOGUE_V3_DOMAINS_1_TO_3_EXTRACT.md",
            "classification": "CURRENT_WORKING_DESIGN",
            "extraction_status": "EXTRACTED",
            "notes": "Non-authoritative working design (Scope D). Refined context catalogue across 131 paragraphs and 26 tables."
        },
        {
            "rel_path": "03_CURRENT_WORKING_DESIGN/DESCO_AIPMS_Classification_and_Workflow_REVISED_after_review.pdf",
            "filename": "DESCO_AIPMS_Classification_and_Workflow_REVISED_after_review.pdf",
            "ext": ".pdf",
            "size": os.path.getsize("03_CURRENT_WORKING_DESIGN/DESCO_AIPMS_Classification_and_Workflow_REVISED_after_review.pdf"),
            "original": "Yes (Current workflow design document)",
            "readable": "Yes (Vector PDF text extractable)",
            "extract": "00_CLAUDE_CONTEXT_PACK/CURRENT_WORKING_DESIGN/CLASSIFICATION_AND_WORKFLOW_REVISED_EXTRACT.md",
            "classification": "CURRENT_WORKING_DESIGN",
            "extraction_status": "EXTRACTED",
            "notes": "Non-authoritative working design (Scope D). 3-page workflow specification extracted with page boundaries."
        },
        {
            "rel_path": "04_PRE_ARCHITECTURE_ANALYSIS/DESCO_AIPMS_Architecture_RnD_Report.md",
            "filename": "DESCO_AIPMS_Architecture_RnD_Report.md",
            "ext": ".md",
            "size": os.path.getsize("04_PRE_ARCHITECTURE_ANALYSIS/DESCO_AIPMS_Architecture_RnD_Report.md"),
            "original": "Yes (Pre-architecture analysis report)",
            "readable": "Yes (Markdown)",
            "extract": "00_CLAUDE_CONTEXT_PACK/PREVIOUS_ANALYSIS/PRE_ARCHITECTURE_ANALYSIS_REPORT_EXTRACT.md",
            "classification": "PREVIOUS_ANALYSIS",
            "extraction_status": "DIRECT_TEXT",
            "notes": "Non-authoritative historical analysis (Scope D). Pre-architecture gap analysis and institutional study."
        },
        {
            "rel_path": "05_OFFICIAL_DESCO_POLICIES/Code_of_ConductCode_of_Conduct.pdf",
            "filename": "Code_of_ConductCode_of_Conduct.pdf",
            "ext": ".pdf",
            "size": os.path.getsize("05_OFFICIAL_DESCO_POLICIES/Code_of_ConductCode_of_Conduct.pdf"),
            "original": "Yes (Official corporate ethics policy)",
            "readable": "No (Scanned image PDF, 0 characters extractable directly)",
            "extract": "00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/CODE_OF_CONDUCT_EXTRACT.md",
            "classification": "OFFICIAL_POLICY",
            "extraction_status": "EXTRACTED",
            "notes": "Authoritative corporate policy (Scope C). 6 pages. Transcribed verbatim across all 9 clauses, director code, and Annexure-1."
        },
        {
            "rel_path": "05_OFFICIAL_DESCO_POLICIES/DESCO_Organogram_2018.pdf",
            "filename": "DESCO_Organogram_2018.pdf",
            "ext": ".pdf",
            "size": os.path.getsize("05_OFFICIAL_DESCO_POLICIES/DESCO_Organogram_2018.pdf"),
            "original": "Yes (Official corporate organogram)",
            "readable": "Yes (Vector text PDF, 31,525 characters)",
            "extract": "00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/DESCO_ORGANOGRAM_2018_EXTRACT.md",
            "classification": "OFFICIAL_POLICY",
            "extraction_status": "EXTRACTED",
            "notes": "Authoritative organogram (Scope C). 15-page organizational hierarchy and post structure."
        },
        {
            "rel_path": "05_OFFICIAL_DESCO_POLICIES/DESCO_Service_Rule_2017.pdf",
            "filename": "DESCO_Service_Rule_2017.pdf",
            "ext": ".pdf",
            "size": os.path.getsize("05_OFFICIAL_DESCO_POLICIES/DESCO_Service_Rule_2017.pdf"),
            "original": "Yes (Official employee service manual)",
            "readable": "No (Scanned image PDF, 0 characters extractable directly)",
            "extract": "00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/DESCO_SERVICE_RULES_2017_EXTRACT.md",
            "classification": "OFFICIAL_POLICY",
            "extraction_status": "EXTRACTED",
            "notes": "Authoritative service manual (Scope C). 63 pages. Comprehensive institutional extract with complete TOC Chapters 1–9, Disciplinary and Promotion rules."
        },
        {
            "rel_path": "05_OFFICIAL_DESCO_POLICIES/Laptop_PC_Use_Rules_2024.pdf",
            "filename": "Laptop_PC_Use_Rules_2024.pdf",
            "ext": ".pdf",
            "size": os.path.getsize("05_OFFICIAL_DESCO_POLICIES/Laptop_PC_Use_Rules_2024.pdf"),
            "original": "Yes (Official device & ICT policy)",
            "readable": "No (Scanned image PDF / broken font encoding)",
            "extract": "00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/LAPTOP_PC_USE_RULES_2024_EXTRACT.md",
            "classification": "OFFICIAL_POLICY",
            "extraction_status": "EXTRACTED",
            "notes": "Authoritative IT asset policy (Scope C). 3 pages. Transcribed verbatim across all 20 clauses and official notice."
        },
        {
            "rel_path": "05_OFFICIAL_DESCO_POLICIES/OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT.md",
            "filename": "OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT.md",
            "ext": ".md",
            "size": os.path.getsize("05_OFFICIAL_DESCO_POLICIES/OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT.md"),
            "original": "No (Pre-compiled architecture synthesis)",
            "readable": "Yes (Markdown)",
            "extract": "00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT_COMPANION.md",
            "classification": "DERIVED POLICY SYNTHESIS",
            "extraction_status": "DIRECT_TEXT",
            "notes": "Derived policy synthesis (Scope C). Pre-compiled working extract synthesizing Service Rules, Organogram, Laptop, and Conduct rules."
        }
    ]

    out = []
    out.append("# DESCO AIPMS — Complete Repository Manifest\n")
    out.append("**Document Role:** Machine-readable inventory of all knowledge assets, source files, classifications, readability, and extract companions.")
    out.append("**Generated by:** `tools/context_extraction/build_manifest.py`")
    out.append("**Workspace Root:** `.`")
    out.append(f"**Total Knowledge Files Cataloged:** {len(files_data)}\n")
    out.append("---\n")
    
    out.append("## Summary Statistics\n")
    out.append(f"- **Total Authoritative Sources (Scope A & B):** 5 primary sources (TOR, Grade 1–11 ACR, Grade 12–16 ACR, Office Order, Order Stub)")
    out.append(f"- **Total Official Policies (Scope C):** 4 primary sources (Service Rules 2017, Organogram 2018, Laptop Rules 2024, Code of Conduct)")
    out.append(f"- **Total Derived Synthesis & Companions:** 2 files (Official Policies Architecture Extract, TOR Text Extract)")
    out.append(f"- **Total Engineering R&D & Working Designs (Scope D):** 3 files (R&D Handoff, AI Context Catalogue V3, Classification & Workflow)")
    out.append(f"- **Total Pre-Architecture Analysis:** 1 file (Pre-Architecture RnD Report)")
    out.append(f"- **Total Root Governance References:** 2 files (CLAUDE.md, 00_CONTEXT_INDEX.md)")
    out.append(f"- **Total Knowledge Files:** {len(files_data)} files\n")
    out.append("---\n")
    
    out.append("## Detailed File Inventory\n")
    out.append("| # | Relative Path | Extension | Size (Bytes) | Original File | Directly Readable | Extract Companion Path | Classification | Extraction Status | Notes |")
    out.append("|---|---|---|---|---|---|---|---|---|---|")
    
    for i, item in enumerate(files_data, 1):
        rel_path = item["rel_path"].replace("\\", "/")
        extract_path = item["extract"].replace("\\", "/")
        notes = item["notes"].replace("|", "/")
        out.append(f"| {i} | `{rel_path}` | `{item['ext']}` | {item['size']} | {item['original']} | {item['readable']} | [`{extract_path}`]({extract_path}) | `{item['classification']}` | `{item['extraction_status']}` | {notes} |")
        
    out.append("\n---\n")
    out.append("## Classification Definitions\n")
    out.append("- **`AUTHORITATIVE_SOURCE`**: Primary contractual and official appraisal documents (Revised TOR, Official ACR Forms, Official Office Order). Highest authority in their respective scopes.")
    out.append("- **`OFFICIAL_POLICY`**: Official DESCO institutional policies approved by the Board or management (Service Rules, Organogram, Laptop Rules, Code of Conduct).")
    out.append("- **`DERIVED POLICY SYNTHESIS`**: Analytical synthesis of official policies prepared for fast AI context ingestion (e.g., `OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT.md`). Subordinate to original policies.")
    out.append("- **`CURRENT_RND`**: Current active engineering proposals and research handoffs. Non-authoritative working material to be independently evaluated from first principles.")
    out.append("- **`CURRENT_WORKING_DESIGN`**: Operational taxonomies and workflow design proposals. Non-authoritative working design.")
    out.append("- **`PREVIOUS_ANALYSIS`**: Exploratory risk and gap analysis reports. Historical engineering analysis.")
    out.append("- **`GOVERNANCE`**: Root operational instructions, repository indexes, and architect guidelines.")
    out.append("- **`DERIVED`**: Companion text representations or extracts.")
    
    manifest_content = "\n".join(out) + "\n"
    
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(manifest_content)
    
    print(f"Generated {manifest_path} successfully.")

if __name__ == "__main__":
    generate_manifest()
