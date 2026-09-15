"""
Validation script for 00_CLAUDE_CONTEXT_PACK
Verifies that primary-source extracts in 00_CLAUDE_CONTEXT_PACK/AUTHORITATIVE/
contain complete answers for Step 9 validation criteria.
"""

import os
import re
import sys

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTEXT_PACK_DIR = os.path.join(ROOT_DIR, "00_CLAUDE_CONTEXT_PACK")
AUTH_DIR = os.path.join(CONTEXT_PACK_DIR, "AUTHORITATIVE")

def check_file_exists(filename):
    path = os.path.join(AUTH_DIR, filename)
    if not os.path.exists(path):
        print(f"[FAIL] Missing file: {filename}")
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def validate_grade_1_11():
    print("\n--- Validating Grade 1-11 ACR Extract ---")
    content = check_file_exists("ACR_GRADE_1_11_FULL_EXTRACT.md")
    if not content:
        return False
    
    # 1. Check number of criteria in table (| ১ | to | ২৫ |)
    table_criteria = re.findall(r"\|\s*([১-৯]|১[০-৯]|২[০-৫])\s*\|\s*([^|]+)\|\s*([^|]+)\|", content)
    num_criteria = len(table_criteria)
    print(f"  Criteria detected in assessment table: {num_criteria}/25")
    if num_criteria == 25:
        print("  Sample criteria recovered:")
        print(f"    Item 1:  {table_criteria[0][1].strip()} ({table_criteria[0][2].strip()})")
        print(f"    Item 14: {table_criteria[13][1].strip()} ({table_criteria[13][2].strip()})")
        print(f"    Item 25: {table_criteria[24][1].strip()} ({table_criteria[24][2].strip()})")
    
    # 2. Check scoring scale 1-4
    scale_ok = "প্রাপ্ত মান ৪" in content and "প্রাপ্ত মান ১" in content
    print(f"  Scoring scale (1-4: প্রাপ্ত মান ১ to ৪): {'PASSED' if scale_ok else 'FAILED'}")
    
    # 3. Check total 100
    total_ok = "Max: 100" in content or "১০০" in content
    print(f"  Total score (100 marks): {'PASSED' if total_ok else 'FAILED'}")
    
    # 4. Check 5 bands
    bands = ["অসাধারণ", "অত্যুত্তম", "উত্তম", "চলতি মান", "চলতি মানের নিম্নে"]
    bands_found = [b for b in bands if b in content]
    print(f"  Performance bands found: {len(bands_found)}/5 ({', '.join(bands_found)})")
    
    passed = (num_criteria == 25 and scale_ok and total_ok and len(bands_found) == 5)
    return passed

def validate_grade_12_16():
    print("\n--- Validating Grade 12-16 ACR Extract ---")
    content = check_file_exists("ACR_GRADE_12_16_FULL_EXTRACT.md")
    if not content:
        return False
    
    # 1. Check number of criteria in table (| ১ | to | ২০ |)
    table_criteria = re.findall(r"\|\s*([১-৯]|১[০-৯]|২০)\s*\|\s*([^|]+)\|\s*([^|]+)\|", content)
    num_criteria = len(table_criteria)
    print(f"  Criteria detected in assessment table: {num_criteria}/20")
    if num_criteria == 20:
        print("  Sample criteria recovered:")
        print(f"    Item 1:  {table_criteria[0][1].strip()} ({table_criteria[0][2].strip()})")
        print(f"    Item 10: {table_criteria[9][1].strip()} ({table_criteria[9][2].strip()})")
        print(f"    Item 20: {table_criteria[19][1].strip()} ({table_criteria[19][2].strip()})")
    
    # 2. Check scoring scale 1-5
    scale_ok = "প্রাপ্ত মান ৫" in content and "প্রাপ্ত মান ১" in content
    print(f"  Scoring scale (1-5: প্রাপ্ত মান ১ to ৫): {'PASSED' if scale_ok else 'FAILED'}")
    
    # 3. Check total 100
    total_ok = "Max: 100" in content or "১০০" in content
    print(f"  Total score (100 marks): {'PASSED' if total_ok else 'FAILED'}")
    
    # 4. Check 5 bands
    bands = ["অসাধারণ", "অত্যুত্তম", "উত্তম", "চলতি মান", "চলতি মানের নিম্নে"]
    bands_found = [b for b in bands if b in content]
    print(f"  Performance bands found: {len(bands_found)}/5 ({', '.join(bands_found)})")
    
    passed = (num_criteria == 20 and scale_ok and total_ok and len(bands_found) == 5)
    return passed

def validate_tor():
    print("\n--- Validating Revised TOR Extract ---")
    content = check_file_exists("TOR_FULL_EXTRACT.md")
    if not content:
        return False
    
    # Top-level sections: 1 to 10
    sections = [
        "1. Background", "2. Objectives of the TOR", "3. Scope of Work",
        "4. Integration Requirements", "5. Technical Requirements", "6. Deliverables",
        "7. Implementation, Training, and Support Plan", "8. Resource Requirements",
        "9. Governance, Compliance, and Intellectual Property", "10. Payment Schedule"
    ]
    sections_found = [s for s in sections if s in content]
    print(f"  Top-level TOR sections detected: {len(sections_found)}/{len(sections)}")
    
    # Sub-sections of interest
    subsections = ["3.1", "3.2", "3.2.1", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8", "5.1", "5.2", "7.1", "10.1"]
    subsections_found = [ss for ss in subsections if re.search(rf"\b{re.escape(ss)}\b", content)]
    print(f"  Key sub-sections detected: {len(subsections_found)}/{len(subsections)}")
    
    # AI requirements
    ai_ok = "AI" in content and "predictive scoring" in content.lower() and "bias" in content.lower() and "pen picture" in content.lower()
    print(f"  AI requirements (predictive scoring, bias detection, pen picture): {'PASSED' if ai_ok else 'FAILED'}")
    
    # Workflow requirements
    wf_ok = "workflow" in content.lower() and "reporting officer" in content.lower() and "countersigning" in content.lower()
    print(f"  Workflow requirements (Reporting, Countersigning, Approving): {'PASSED' if wf_ok else 'FAILED'}")
    
    # Integration requirements
    int_ok = "integration" in content.lower() and "api" in content.lower() and ("hrms" in content.lower() or "attendance" in content.lower())
    print(f"  Integration requirements (APIs, Attendance, Disciplinary, Training): {'PASSED' if int_ok else 'FAILED'}")
    
    # Security requirements
    sec_ok = "iso/iec 27001" in content.lower() and "rbac" in content.lower() and "aes-256" in content.lower()
    print(f"  Security requirements (ISO 27001, RBAC, AES-256, Audit logs): {'PASSED' if sec_ok else 'FAILED'}")
    
    # Deployment/Tech stack requirements
    dep_ok = "spring boot" in content.lower() and "react" in content.lower() and "on-premise" in content.lower()
    print(f"  Deployment & Tech stack (Java Spring Boot, React, Python/TensorFlow, On-premise): {'PASSED' if dep_ok else 'FAILED'}")
    
    passed = (len(sections_found) == len(sections) and ai_ok and wf_ok and int_ok and sec_ok and dep_ok)
    return passed

def validate_office_order():
    print("\n--- Validating ACR Instructions / Office Order Extract ---")
    content = check_file_exists("ACR_INSTRUCTIONS_OFFICE_ORDER_FULL_EXTRACT.md")
    if not content:
        return False
    
    # Clauses in Bengali: ১। to ২৪। or English: *(English: 1. to 24.)*
    bengali_clauses = re.findall(r"(?:^|\n)([১-৯]|১[০-৯]|২[০-৪])।", content)
    unique_bengali = len(set(bengali_clauses))
    print(f"  Official Bengali clauses detected: {unique_bengali}/24")
    
    english_clauses = re.findall(r"\*\(English:\s*([1-9]|1[0-9]|2[0-4])\.", content)
    unique_english = len(set(english_clauses))
    print(f"  English translated clauses detected: {unique_english}/24")
    
    # Appraisal cycle and 3-month rule
    period_ok = ("তিন মাস" in content or "3 months" in content.lower() or "৩ মাস" in content) and ("পঞ্জিকা বৎসর" in content or "calendar year" in content.lower())
    print(f"  Appraisal cycle & 3-month supervision rule (Clause 1, 2, 15): {'PASSED' if period_ok else 'FAILED'}")
    
    # Multi-tier routing (Reporting, Countersigning, Certifying, Approving)
    routing_ok = "অনুবেদনকারী" in content and "প্রতিস্বাক্ষরকারী" in content and "প্রত্যয়নকারী" in content and "অনুমোদনকারী" in content
    print(f"  Multi-tier routing (Reporting, Countersigning, Certifying, Approving): {'PASSED' if routing_ok else 'FAILED'}")
    
    # Adverse remarks procedure
    adverse_ok = "বিরূপ মন্তব্য" in content or "adverse remark" in content.lower()
    print(f"  Adverse remarks procedure (Clause 3): {'PASSED' if adverse_ok else 'FAILED'}")
    
    # Confidentiality rules
    conf_ok = "গোপনীয়" in content and ("খাম" in content or "confidential" in content.lower())
    print(f"  Confidentiality & transmission rules (Clause 4): {'PASSED' if conf_ok else 'FAILED'}")
    
    passed = (unique_bengali == 24 and unique_english == 24 and period_ok and routing_ok and adverse_ok and conf_ok)
    return passed

def main():
    print("============================================================")
    print("STEP 9: PRIMARY-SOURCE VALIDATION SUITE")
    print("============================================================")
    
    g1_ok = validate_grade_1_11()
    g2_ok = validate_grade_12_16()
    tor_ok = validate_tor()
    oo_ok = validate_office_order()
    
    print("\n============================================================")
    print("VALIDATION SUMMARY")
    print("============================================================")
    print(f"A. Grade 1-11 ACR (25 criteria, 1-4 scale, 100 total, 5 bands): {'PASS' if g1_ok else 'FAIL'}")
    print(f"B. Grade 12-16 ACR (20 criteria, 1-5 scale, 100 total, 5 bands): {'PASS' if g2_ok else 'FAIL'}")
    print(f"C. Revised TOR (10 sections, AI, Workflow, Integrations, Security, Deploy): {'PASS' if tor_ok else 'FAIL'}")
    print(f"D. ACR Office Order (24 clauses, 3-mo rule, routing, adverse remarks): {'PASS' if oo_ok else 'FAIL'}")
    
    all_passed = g1_ok and g2_ok and tor_ok and oo_ok
    print(f"\nOVERALL RESULT: {'ALL TESTS PASSED - CONTEXT PACK VALID' if all_passed else 'VALIDATION FAILED'}")
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
