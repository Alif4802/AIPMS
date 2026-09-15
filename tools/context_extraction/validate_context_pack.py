"""
Deterministic validation script for DESCO AIPMS Simplified Clean Context Pack.
Validates the 13 post-cleanup repository integrity conditions:
 1. Original authoritative documents exist.
 2. Original R&D documents exist.
 3. Original working-design documents exist.
 4. Original policy documents exist.
 5. Scanned/binary sources have readable Markdown extracts in 00_CLAUDE_CONTEXT_PACK/.
 6. ACR extracts contain all 25 (Grade 1–11) and 20 (Grade 12–16) criteria.
 7. Office Order extract contains all 24 administrative clauses.
 8. TOR extract contains all 10 sections and acronyms.
 9. Core governance files exist (CLAUDE.md, 00_CONTEXT_INDEX.md, README_FOR_CLAUDE.md).
 10. No path in governance/navigation files points to a deleted file.
 11. No duplicate mirrors or empty directories remain in 00_CLAUDE_CONTEXT_PACK/.
 12. Temporary scratch/ directory is removed.
 13. Zero modifications to original source file content.
"""

import os
import re
import subprocess
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTEXT_PACK_DIR = os.path.join(ROOT_DIR, "00_CLAUDE_CONTEXT_PACK")

def read_file(rel_path):
    full_path = os.path.join(ROOT_DIR, rel_path)
    if not os.path.exists(full_path):
        return None
    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()

def test_1_to_4_original_sources_exist():
    print("Test 1-4: Validating original documents exist across all domains...")
    required_originals = [
        "01_AUTHORITATIVE_SOURCES/2026-08-18 DESCO_AIPMS_TOR_Revised_2_Final (Autosaved).docx",
        "01_AUTHORITATIVE_SOURCES/ACR Format.pdf",
        "01_AUTHORITATIVE_SOURCES/ACR ফর্ম (গ্রেড ১২-১৬).pdf",
        "01_AUTHORITATIVE_SOURCES/ACR_Instructions_Office_Order_Document.pdf",
        "02_CURRENT_RND/DESCO_AIPMS_Complete_RnD_Architecture_Handoff_Current (1).md",
        "03_CURRENT_WORKING_DESIGN/DESCO_AIPMS_AI_Context_Catalogue_V3_Domains_1_to_3 (2).docx",
        "03_CURRENT_WORKING_DESIGN/DESCO_AIPMS_Classification_and_Workflow_REVISED_after_review.pdf",
        "04_PRE_ARCHITECTURE_ANALYSIS/DESCO_AIPMS_Architecture_RnD_Report.md",
        "05_OFFICIAL_DESCO_POLICIES/Code_of_ConductCode_of_Conduct.pdf",
        "05_OFFICIAL_DESCO_POLICIES/DESCO_Organogram_2018.pdf",
        "05_OFFICIAL_DESCO_POLICIES/DESCO_Service_Rule_2017.pdf",
        "05_OFFICIAL_DESCO_POLICIES/Laptop_PC_Use_Rules_2024.pdf",
        "05_OFFICIAL_DESCO_POLICIES/OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT.md"
    ]
    all_ok = True
    for p in required_originals:
        full_p = os.path.join(ROOT_DIR, p)
        if not os.path.exists(full_p):
            print(f"  [FAIL] Missing original: {p}")
            all_ok = False
    if all_ok:
        print(f"  [PASS] All {len(required_originals)} original source documents exist.")
    return all_ok

def test_5_extracts_exist():
    print("Test 5: Validating required machine-readable extracts in 00_CLAUDE_CONTEXT_PACK...")
    required_extracts = [
        "00_CLAUDE_CONTEXT_PACK/README_FOR_CLAUDE.md",
        "00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/TOR_FULL_EXTRACT.md",
        "00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_GRADE_1_11_FULL_EXTRACT.md",
        "00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_GRADE_12_16_FULL_EXTRACT.md",
        "00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/ACR_INSTRUCTIONS_OFFICE_ORDER_FULL_EXTRACT.md",
        "00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/DESCO_SERVICE_RULES_2017_EXTRACT.md",
        "00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/DESCO_ORGANOGRAM_2018_EXTRACT.md",
        "00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/CODE_OF_CONDUCT_EXTRACT.md",
        "00_CLAUDE_CONTEXT_PACK/OFFICIAL_POLICIES/LAPTOP_PC_USE_RULES_2024_EXTRACT.md",
        "00_CLAUDE_CONTEXT_PACK/CURRENT_WORKING_DESIGN/AI_CONTEXT_CATALOGUE_V3_DOMAINS_1_TO_3_EXTRACT.md",
        "00_CLAUDE_CONTEXT_PACK/CURRENT_WORKING_DESIGN/CLASSIFICATION_AND_WORKFLOW_REVISED_EXTRACT.md"
    ]
    all_ok = True
    for p in required_extracts:
        full_p = os.path.join(ROOT_DIR, p)
        if not os.path.exists(full_p):
            print(f"  [FAIL] Missing extract: {p}")
            all_ok = False
    if all_ok:
        print(f"  [PASS] All {len(required_extracts)} required machine-readable extracts verified.")
    return all_ok

def test_6_acr_criteria_intact():
    print("Test 6: Validating ACR evaluation criteria completeness...")
    g1 = read_file(os.path.join("00_CLAUDE_CONTEXT_PACK", "AUTHORITATIVE", "ACR_GRADE_1_11_FULL_EXTRACT.md"))
    g2 = read_file(os.path.join("00_CLAUDE_CONTEXT_PACK", "AUTHORITATIVE", "ACR_GRADE_12_16_FULL_EXTRACT.md"))
    
    g1_c = len(set(re.findall(r"\|\s*([১-৯]|১[০-৯]|২[০-৫])\s*\|", g1)))
    g2_c = len(set(re.findall(r"\|\s*([১-৯]|১[০-৯]|২০)\s*\|", g2)))
    
    ok = (g1_c == 25 and g2_c == 20)
    if ok:
        print("  [PASS] Grade 1–11 contains all 25 criteria; Grade 12–16 contains all 20 criteria.")
    else:
        print(f"  [FAIL] Criteria counts: Grade 1-11: {g1_c}/25, Grade 12-16: {g2_c}/20")
    return ok

def test_7_office_order_clauses():
    print("Test 7: Validating 24 Office Order clauses...")
    oo = read_file(os.path.join("00_CLAUDE_CONTEXT_PACK", "AUTHORITATIVE", "ACR_INSTRUCTIONS_OFFICE_ORDER_FULL_EXTRACT.md"))
    bengali_clauses = len(set(re.findall(r"(?:^|\n)([১-৯]|১[০-৯]|২[০-৪])।", oo)))
    english_clauses = len(set(re.findall(r"\*\(Non-Authoritative Working Translation:\s*([1-9]|1[0-9]|2[0-4])\.", oo)))
    ok = (bengali_clauses == 24 and english_clauses == 24)
    if ok:
        print("  [PASS] All 24 Bengali administrative clauses and 24 English translations present.")
    else:
        print(f"  [FAIL] Clauses: Bengali {bengali_clauses}/24, English {english_clauses}/24")
    return ok

def test_8_tor_extract_intact():
    print("Test 8: Validating Revised TOR extract integrity...")
    tor = read_file(os.path.join("00_CLAUDE_CONTEXT_PACK", "AUTHORITATIVE", "TOR_FULL_EXTRACT.md"))
    sections = [
        "1. Background", "2. Objectives of the TOR", "3. Scope of Work",
        "4. Integration Requirements", "5. Technical Requirements", "6. Deliverables",
        "7. Implementation, Training, and Support Plan", "8. Resource Requirements",
        "9. Governance, Compliance, and Intellectual Property", "10. Payment Schedule"
    ]
    found = [s for s in sections if s in tor]
    ok = (len(found) == 10 and "List of Acronyms" in tor)
    if ok:
        print("  [PASS] All 10 TOR sections and Acronyms table present.")
    else:
        print(f"  [FAIL] Sections found: {len(found)}/10")
    return ok

def test_9_governance_files_exist():
    print("Test 9: Validating root governance and navigation files exist...")
    gov_files = ["CLAUDE.md", "00_CONTEXT_INDEX.md", "00_CLAUDE_CONTEXT_PACK/README_FOR_CLAUDE.md"]
    all_ok = True
    for gf in gov_files:
        if not os.path.exists(os.path.join(ROOT_DIR, gf)):
            print(f"  [FAIL] Missing governance file: {gf}")
            all_ok = False
    if all_ok:
        print("  [PASS] CLAUDE.md, 00_CONTEXT_INDEX.md, and README_FOR_CLAUDE.md exist.")
    return all_ok

def test_10_no_broken_references():
    print("Test 10: Checking that governance files do not point to deleted files...")
    deleted_patterns = [
        "00_REPOSITORY_MANIFEST.md",
        "01_SOURCE_PRIORITY_AND_MAP.md",
        "02_PRIMARY_SOURCE_VERIFICATION.md",
        "03_DOCUMENT_RELATIONSHIP_MAP.md",
        "99_EXTRACTION_GAPS.md",
        "CONTEXT_READINESS_REPORT.md",
        "CLAUDE_CORE_RULES_EXTRACT.md",
        "CONTEXT_INDEX_MAP_EXTRACT.md",
        "COMPLETE_RND_ARCHITECTURE_HANDOFF_EXTRACT.md",
        "PRE_ARCHITECTURE_ANALYSIS_REPORT_EXTRACT.md",
        "OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT_COMPANION.md",
        "EXTRACTION_OBSERVATIONS.md",
        "2026-08-18_DESCO_AIPMS_TOR_Revised_2_Final_Extract.md",
        "ACR_Instructions_Office_Order.pdf"
    ]
    files_to_check = [
        "CLAUDE.md",
        "00_CONTEXT_INDEX.md",
        "00_CLAUDE_CONTEXT_PACK/README_FOR_CLAUDE.md"
    ]
    all_ok = True
    for gf in files_to_check:
        content = read_file(gf)
        if content:
            for dp in deleted_patterns:
                if dp in content:
                    print(f"  [FAIL] Reference to deleted file '{dp}' in {gf}")
                    all_ok = False
    if all_ok:
        print("  [PASS] No references to deleted files found in governance/navigation.")
    return all_ok

def test_11_no_empty_dirs_or_mirrors():
    print("Test 11: Validating no empty dirs or unwanted mirrors in 00_CLAUDE_CONTEXT_PACK...")
    unwanted_dirs = ["REFERENCES", "CURRENT_RND", "PREVIOUS_ANALYSIS", "DERIVED_NOTES"]
    all_ok = True
    for ud in unwanted_dirs:
        p = os.path.join(CONTEXT_PACK_DIR, ud)
        if os.path.exists(p):
            print(f"  [FAIL] Unwanted directory still exists: {ud}")
            all_ok = False
    
    # Check for empty directories
    for root, dirs, files in os.walk(CONTEXT_PACK_DIR):
        if not dirs and not files:
            print(f"  [FAIL] Empty directory found: {root}")
            all_ok = False
    if all_ok:
        print("  [PASS] No unwanted mirrors or empty directories in 00_CLAUDE_CONTEXT_PACK.")
    return all_ok

def test_12_scratch_removed():
    print("Test 12: Validating scratch/ directory is removed...")
    scratch_p = os.path.join(ROOT_DIR, "scratch")
    if os.path.exists(scratch_p):
        print("  [FAIL] scratch/ directory still exists!")
        return False
    print("  [PASS] scratch/ directory has been removed.")
    return True

def test_13_original_files_untouched():
    print("Test 13: Verifying zero modifications to original source file contents...")
    # Check git status for modifications on remaining original files
    res = subprocess.run(["git", "status", "--porcelain", "02_CURRENT_RND", "03_CURRENT_WORKING_DESIGN", "04_PRE_ARCHITECTURE_ANALYSIS", "05_OFFICIAL_DESCO_POLICIES"], cwd=ROOT_DIR, capture_output=True, text=True)
    mods = [line for line in res.stdout.splitlines() if line.startswith(" M") or line.startswith("M ")]
    if len(mods) == 0:
        print("  [PASS] Original R&D, working design, and policy sources remain completely untouched.")
        return True
    else:
        print(f"  [FAIL] Modified files: {mods}")
        return False

def main():
    print("============================================================")
    print("VALIDATION: DESCO AIPMS SIMPLIFIED REPOSITORY INTEGRITY")
    print("============================================================")
    results = [
        test_1_to_4_original_sources_exist(),
        test_5_extracts_exist(),
        test_6_acr_criteria_intact(),
        test_7_office_order_clauses(),
        test_8_tor_extract_intact(),
        test_9_governance_files_exist(),
        test_10_no_broken_references(),
        test_11_no_empty_dirs_or_mirrors(),
        test_12_scratch_removed(),
        test_13_original_files_untouched()
    ]
    all_passed = all(results)
    print("\n============================================================")
    print(f"FINAL RESULT: {'ALL CHECKS PASSED (10/10 TEST SUITES)' if all_passed else 'VALIDATION FAILED'}")
    print("============================================================")
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
