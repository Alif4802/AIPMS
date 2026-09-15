# Source Extraction

**Original file:** OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT.md  
**Original relative path:** 05_OFFICIAL_DESCO_POLICIES/OFFICIAL_POLICIES_ARCHITECTURE_EXTRACT.md  
**Source category:** OFFICIAL_POLICY (Precedence Rank 3)  
**Extraction method:** Direct companion mirror  
**Extraction date:** 2026-09-15  
**Number of pages/sheets/slides:** 908 lines of detailed policy analysis  
**Extraction completeness:** 100% complete  
**Notes:** Pre-compiled architectural extract synthesizing Service Rules 2017, Organogram 2018, Laptop Rules 2024, and Code of Conduct.

---

# DESCO AIPMS — Official Policies Architecture Extract

**Purpose:** Compact architecture-relevant extract from the official DESCO policy/organizational documents kept in `05_OFFICIAL_DESCO_POLICIES/`.

**Use:** Give Claude the policy facts and applicability boundaries needed for AIPMS architecture without loading the full scanned PDFs into Project Knowledge.

**Important:** This file is a working extract, not a replacement for the originals. If an exact clause, legal interpretation, disciplinary status, role applicability, or current organizational position matters, inspect the original document.

---

## 1. Source Set and Applicability

### 1.1 DESCO Service Rule 2017
Primary ordinary-employee source in this set for service conditions, conduct, discipline, promotion/increment context, penalties, inquiry, appeal, and confidentiality obligations.

Architecture use:
- employee conduct/compliance context;
- disciplinary-record lifecycle;
- confidentiality/access-control requirements;
- appraisal-to-increment/promotion context;
- AI scenario grounding where behavior directly demonstrates an official ACR metric.

Do **not** treat every Service Rule violation or disciplinary ground as an automatic low ACR score. A rule provision becomes appraisal evidence only when the actual authorized/finalized record and behavior are relevant to the specific ACR metric.

### 1.2 Organogram 2018
Official organizational-structure reference containing DESCO hierarchy, divisions, posts, operational role families, and later board-approved ICT/health setup notes included in the document.

Architecture use:
- realistic role/department context;
- organization and post taxonomy;
- integration/snapshot design;
- role-aware AI scenario examples.

Do **not** use the static organogram as the appraisal authority chain. Reporting/Countersigning/Certifying/Approving assignments are governed by the ACR/TOR/HRM process and must be resolved per appraisal case/cycle.

### 1.3 Official Laptop PC Use Rules 2024
Operational policy for allocation, use, custody, security, maintenance, and lifecycle of official laptops.

Architecture use:
- discipline/compliance context;
- asset/data-custody context;
- security-aware scenario grounding;
- supporting evidence for authorized-use and negligence cases.

This is an operational/device policy, not a general ACR scoring rubric.

### 1.4 DESCO Code of Conduct
**Limited applicability.** The supplied Code is titled for the Chairperson, Board members, and Chief Executive Officer/Managing Director, and its applicability section is directed to the Board-level governance population.

Architecture use:
- governance/conflict-of-interest context for covered senior actors;
- confidentiality, fair dealing, asset protection, and ethical-governance concepts where applicable.

Do **not** generalize this Code as the ordinary employee conduct policy. For normal employees, rely primarily on the DESCO Service Rule 2017 and other applicable employee policies.

---

# 2. DESCO Service Rule 2017 — Architecture-Relevant Extract

## 2.1 Promotion and Performance-Appraisal Link

The Service Rules establish that promotion should support competent personnel, morale, organizational needs, and fairness, and should be free from influence and bias. Promotion is tied to sanctioned vacancies/organizational requirements and the approved promotion process. The Administrative Department prepares the relevant merit list for competent-authority approval. The policy scope shown in the supplied rule applies up to CE/equivalent level.

**Architecture consequence**
- AIPMS may provide finalized appraisal outputs as an input to promotion-related decisions/reports.
- Do not make AIPMS itself invent promotion eligibility formulas or automatically promote employees unless a separately approved DESCO rule explicitly defines that automation.
- Preserve the finalized appraisal result and source period so downstream promotion decisions can be audited.

**Source:** Service Rule 2017, promotion-policy section around printed pp. 14–16.

## 2.2 Annual Increment / Pay Raise

The Service Rules state that annual increment/pay raise is based on the **rating of the performance appraisal**. The rule also contains service-status conditions affecting increment eligibility and permits competent authority to grant advance increment(s) for outstanding performance/merit in appropriate cases.

**Architecture consequence**
- Final appraisal ratings can have material employment consequences; scoring and finalization require strong auditability.
- Preserve which approved appraisal result was used for any downstream increment action.
- Do not invent increment thresholds, formulas, exceptions, or approval rules not explicitly supplied.

**Source:** Service Rule 2017 §4.8, printed p. 16 onward.

---

## 2.3 Fidelity, Secrecy and Confidential Information

Employees must maintain strict secrecy regarding company affairs and must not communicate company information obtained through their duties to unauthorized persons except where required for proper discharge of duties. A fidelity/secrecy declaration is required before joining.

**Architecture consequence**
- ACR/appraisal data must be treated as confidential institutional information.
- Apply least-privilege access, role/case-scoped authorization, secure audit trails, and controlled disclosure.
- Do not expose full appraisal records merely because a user belongs to the same department or has a senior title.
- AI prompts, logs, exports, analytics, and support tools must follow the same confidentiality boundary.

**Source:** Service Rule 2017 §7.1, printed p. 25.

---

## 2.4 Required Employee Conduct

Service Rule §7.2 requires employees to:
- conform to DESCO rules;
- remain aligned with company vision, mission, policies, and goals;
- demonstrate and participate in performance improvement;
- observe, comply with, and obey lawful orders/directions consistent with law, company rules, and the relevant person’s authority/jurisdiction;
- serve the company and discharge assigned duties faithfully, honestly, and diligently;
- use best efforts to promote the company’s interests;
- maintain proper decorum, courtesy, and appropriate workplace conduct;
- maintain secrecy regarding company affairs.

**AIPMS use**
These provisions may provide behavioral context for ACR metrics such as Discipline, Reliability, Sense of Responsibility, Devotion to Duty, Cooperation, Conduct with the Public, and related metrics **only where the actual event directly demonstrates that metric**.

Do not map a rule citation to an ACR metric automatically.

**Source:** Service Rule 2017 §7.2(a), printed p. 25.

---

## 2.5 Important Prohibited/Restricted Conduct

The supplied rules restrict, among other matters:
- unauthorized political association/activity;
- absence from duty or leaving station without permission;
- unauthorized public/media statements concerning company matters;
- outside employment or part-time work without appropriate approval;
- engaging in trade/business without approval;
- certain processions/demonstrations and conduct inconsistent with service obligations;
- gifts/concessions and financial dealings that may create improper influence/conflict;
- other prohibited activities defined by the rules.

**Architecture consequence**
- These are compliance/disciplinary concepts, not standalone ACR scoring rules.
- If such information enters AIPMS, store the official status and provenance rather than a free-text accusation.
- Pending or disputed matters must remain distinguishable from finalized findings.

**Source:** Service Rule 2017 §7.2(b)–(d), printed p. 26.

---

## 2.6 Grounds for Penalty

The Service Rules list grounds including:
- negligence in duties;
- inefficiency/loss of efficiency;
- misconduct;
- corruption or knowingly facilitating corruption;
- willful insubordination/disobedience;
- theft, fraud, or dishonesty involving DESCO business/property;
- habitual breach of rules/regulations;
- riotous/disorderly behavior;
- falsifying, tampering with, damaging, or causing loss of official records;
- false information regarding personal particulars/qualifications or suppression of material facts;
- malingering, slowing down work, undue delay in performance of duty, refusal/negligence to carry out reasonable orders, or related service failures.

**Architecture consequence**
- These grounds are useful for classifying official disciplinary/compliance data.
- They must **not** be converted directly into ACR marks.
- A technical mistake, quality issue, delay, negligence allegation, or efficiency concern must be interpreted against the actual evidence and correct ACR metric boundary.
- The TOR rule that only finalized and authorized disciplinary records may be considered for APR assessment remains controlling for AIPMS assessment use.

**Source:** Service Rule 2017 §7.3, printed p. 27.

---

## 2.7 Penalty Types

The rules provide penalties such as:
- censure/warning;
- withholding increment or promotion for a specified period;
- reduction/relegation;
- recovery of loss caused to the company;
- reduction to lower post/grade where applicable;
- termination/discharge/dismissal.

**Architecture consequence**
The disciplinary model should not store only a generic `disciplinary=true/false`. Preserve at least:
- case/reference;
- allegation/ground;
- current procedural state;
- competent authority;
- decision date;
- penalty type;
- effective date;
- appeal state/result;
- finality/authorization status;
- supporting official reference.

**Source:** Service Rule 2017 §7.4, printed pp. 27–28.

---

## 2.8 Suspension, Inquiry and Due Process

The rules provide for suspension pending inquiry/proceedings and formal inquiry procedures. Relevant controls include:
- written communication of charges/allegations;
- opportunity for the employee to explain/respond;
- inquiry by competent authority/committee where applicable;
- hearing/investigation procedures before final orders in applicable cases;
- written communication of decisions.

**Architecture consequence**
AIPMS must distinguish:
`ALLEGED / CHARGED / UNDER_INQUIRY / DECIDED / PENALTY_IMPOSED / UNDER_APPEAL / FINAL` or equivalent states.

Do not treat:
- allegation,
- show-cause,
- pending inquiry,
- suspension,
- or non-final case

as equivalent to a finalized disciplinary finding.

Where disciplinary data is imported through API, import the source status and finality rather than inferring it.

**Source:** Service Rule 2017 §§7.6–7.8, printed pp. 28–29.

---

## 2.9 Summary Proceedings

The rules allow summary proceedings for specified categories such as habitual late attendance, leaving duty without permission, willful misrepresentation/suppression of fact, certain misbehavior, unnecessary delay in disposal of files/records, and absence without permission beyond the specified period.

**Architecture consequence**
- A summary-proceeding event still needs an official procedural/finality state before being used as finalized disciplinary evidence.
- Attendance or delay facts may independently exist as objective/system evidence, but the disciplinary **finding** and the underlying raw fact are different evidence objects and must not be conflated.

**Source:** Service Rule 2017 §7.9, printed p. 29.

---

## 2.10 Appeal and Reinstatement

The Service Rules provide an appeal process against penalties, including procedural requirements/time limits, and provide for authority review of the case record. They also cover reinstatement following dismissal/removal/suspension outcomes.

**Architecture consequence**
- A disciplinary decision can change after appeal/review.
- Imported compliance evidence should support supersession/versioning rather than destructive overwrite.
- Preserve both the original decision and later appeal/reinstatement outcome.
- If an appraisal used a disciplinary record that is later reversed/modified, the audit trail must show what information was valid/available at the time.

**Source:** Service Rule 2017 §§7.10–7.11, printed pp. 29–30.

---

# 3. Organogram — Architecture-Relevant Extract

## 3.1 Top-Level Structure

The supplied organogram shows a hierarchy broadly containing:
- Board of Directors;
- Managing Director;
- Executive Director — Administration & HR;
- Executive Director — Procurement;
- Executive Director — Engineering;
- Executive Director — Operation;
- Executive Director — Finance & Accounts;
- Company Secretary;
- Internal Audit;
- Monitoring Cell;
- major Chief Engineer / General Manager structures beneath these functions.

Major operational/functional families visible in the organogram include:
- Administration & HR;
- HRM / Personnel Management;
- Training & Development;
- Security;
- Estate & Legal Affairs;
- Procurement / Inspection & Testing / Material Planning / Stores;
- Development & Projects;
- Planning & Design;
- S&D Operation — East and West;
- individual Sales & Distribution Divisions;
- Network Operation;
- Grid Operation / System Protection / Energy Audit / SCADA;
- ICT;
- Finance & Accounts;
- Company Secretary / Regulatory Affairs / Board Affairs / Public Relations;
- Health Service.

**Source:** Organogram 2018, overview pp. 2–3 and detailed pages.

---

## 3.2 Administration / HR Context

The Administration structure includes HRM and Personnel Management, Training & Development, security, logistics/general services, estate/legal functions, and supporting administrative roles.

**AIPMS relevance**
- HRM is a key organizational actor for employee/appraisal administration.
- Employee/post/assignment data should be sourced from the authoritative HR/organization source where available.
- Training evidence and personnel context may originate from different administrative functions and should retain provenance.

**Source:** Organogram, Administration/HR detail around p. 5.

---

## 3.3 Procurement / Material / Store Context

The organogram contains:
- Procurement;
- Procurement Inspection & Testing;
- Material Planning;
- Central Store/Sub-store;
- Clearing & Movement.

**AIPMS relevance**
Use these as role-context families for examples involving:
- process compliance;
- inspection/testing;
- custody;
- record accuracy;
- procurement timeliness;
- material/store responsibility.

Do not create special scoring rules merely because a user belongs to Procurement.

**Source:** Organogram, procurement detail around p. 6.

---

## 3.4 Development / Projects and Planning / Design

Development & Projects includes project units, electrical/civil work, development and meter-workshop functions. Planning & Design includes system planning, design/specification, and project planning.

**AIPMS relevance**
Useful role context for:
- project delivery;
- technical judgment;
- quality/quantity of work;
- decision/implementation;
- coordination;
- professional knowledge.

Role context changes what evidence looks like; it does **not** change the meaning or official scoring scale of the ACR metric.

**Source:** Organogram, pp. 7–8.

---

## 3.5 Sales & Distribution Operations

The organogram shows East/West S&D zones and detailed S&D divisions containing operational and service functions such as:
- system operation;
- commercial operation;
- customer service;
- new connection;
- line maintenance;
- MV substation work;
- revenue;
- metering/monitoring;
- sub-control-center functions;
- complaint handling;
- shift/field roles;
- supporting records/billing functions.

**AIPMS relevance**
Important role context for:
- punctuality/roster behavior;
- prompt response;
- public/customer conduct;
- safety;
- reliability;
- responsibility;
- technical/professional competence;
- work quantity/quality.

Shift/roster requirements should be interpreted from actual authorized duty schedules, not inferred merely from job title.

**Source:** Organogram, S&D overview/details around pp. 9–11.

---

## 3.6 Network Operation / Grid / Safety-Critical Context

The Network Operation structure includes:
- grid operation;
- grid O&M;
- system protection;
- SCADA;
- MV substation maintenance;
- meter testing/repair;
- energy-audit-related functions;
- hardware/software maintenance roles;
- shift-based operational roles.

**AIPMS relevance**
This is important role context for:
- Safety Awareness;
- Promptness;
- Reliability;
- Professional Knowledge;
- Quality of Work;
- Decision/Execution;
- emergency/fault response.

Do not equate generic cybersecurity or asset-care behavior with the official **Safety Awareness** metric unless the actual role/event is genuinely safety-related.

**Source:** Organogram, Network Operation around p. 12.

---

## 3.7 ICT Context

The ICT structure includes:
- MIS & Software;
- MIS/eServices/business analysis/coordination;
- software architecture, analysis, development, integration, testing, deployment, maintenance/support, and database design/development;
- network architecture, monitoring, maintenance, system support, and cybersecurity;
- data-center monitoring/maintenance/database administration;
- system automation;
- GIS, AMI, SCADA, prepaid and smart-meter technologies;
- call-center/support functions.

**AIPMS relevance**
Use as role context for:
- Professional Knowledge;
- Quality of Work;
- Judgment;
- Decision/Implementation;
- Responsibility;
- Discipline/compliance where access/change/security rules are actually involved;
- service/support promptness and reliability.

Cybersecurity competence can support Professional Knowledge/Quality where relevant. A security-policy breach can support Discipline/Responsibility where relevant. Neither should be automatically mapped to Safety Awareness.

The organogram also contains later Board-approved ICT setup notes; therefore treat organizational structure as effective-dated/changeable rather than immutable configuration.

**Source:** Organogram, ICT detail around p. 13.

---

## 3.8 Finance & Accounts Context

The Finance & Accounts structure contains functions such as:
- banking/cash management;
- investment and bank reconciliation;
- financial management/budget;
- salary/allowance, CPF and gratuity;
- corporate accounts;
- S&D accounts;
- VAT/tax and plant accounts.

**AIPMS relevance**
Role-context examples may involve:
- accuracy;
- timeliness;
- confidentiality;
- compliance;
- financial responsibility;
- documentation;
- reliability.

Do not use financial-role membership itself as evidence; only actual work/evidence is assessable.

**Source:** Organogram, Finance & Accounts around p. 14.

---

## 3.9 Health Service Context

The organogram includes a DESCO health-service setup with roles including:
- Senior Medical Officer;
- Medical Officer;
- Medical Assistants;
- Nurses;
- supporting staff.

**AIPMS relevance**
- Confirms a distinct health-service organizational role family.
- Health records should be treated as specially restricted information.
- Health staff roles may be relevant to the ACR health-assessment workflow, but the ACR/TOR remain the authority for what health data is captured and who may act on it.

Do not use health information as performance evidence merely because it exists in the organization.

**Source:** Organogram, health-service detail around p. 15.

---

## 3.10 Organogram Boundary Rules for Architecture

1. **Do not hard-code the organogram.** DESCO organizational structures change.
2. Model posts, units, reporting relationships, and role assignments as effective-dated data/configuration or consume them from an authoritative HR/organization source.
3. Preserve organizational snapshots needed to reproduce historical appraisals.
4. Do not assume department hierarchy equals appraisal authority.
5. Do not infer ACR applicability purely from a job title/post listed in the organogram.
6. Use role families to improve AI context/scenario interpretation, not to create separate unofficial ACR criteria.
7. Outsourced/support roles appear in the organogram; whether a particular employee/population is in AIPMS/ACR scope must come from authoritative appraisal policy, not from the organogram alone.

---

# 4. Official Laptop PC Use Rules 2024 — Architecture-Relevant Extract

## 4.1 Policy Purpose and Applicability

The notice states that official laptops are provided to support official-work simplification, transparency, accountability, digital service improvement, and good governance. Allocation is directed to specified officer levels/functions and is intended to expand across eligible DESCO offices.

**Architecture consequence**
Treat device-policy applicability as role/asset-specific. Do not assume every employee is governed by every laptop-specific rule.

**Source:** Laptop PC Use Rules notice, 28 Aug 2024, p. 1.

---

## 4.2 Asset Registration and Custody

The rules require controlled allocation and asset/register maintenance for official laptops, with identifying/assignment information maintained by the relevant office/department. Transfer/change of assignment must be reflected through the responsible administrative process.

**Architecture consequence**
Where device misuse/custody appears as appraisal evidence, capture:
- asset/reference;
- assigned user;
- relevant period;
- applicable policy;
- incident/evidence;
- official verification state.

Do not rely on vague statements such as “did not take care of laptop.”

**Source:** Laptop PC Use Rules, pp. 1–2.

---

## 4.3 Authorized Use

Official laptops are for official purposes and are subject to DESCO administrative/ICT rules. Unauthorized software/hardware changes or unapproved use are restricted.

**AIPMS mapping boundary**
- explicit authorized-use/rule breach may be relevant to **Discipline**;
- custody/care negligence may be more directly relevant to **Sense of Responsibility**;
- technical inability to operate a system may instead concern **Professional Knowledge**;
- do not map all laptop incidents to multiple metrics automatically.

---

## 4.4 Software and Security Controls

The rules require/expect controls including:
- ICT oversight/approval regarding software installation/use;
- licensed/authorized security software;
- Windows Defender Firewall and Real-Time Protection or equivalent protective controls to remain enabled;
- secure/updated operating environment;
- avoiding unauthorized or unsafe software/hardware practices.

**Architecture consequence**
Use these rules as source-grounding for role-relevant compliance/security scenarios. They do not create an ACR cybersecurity metric.

**Source:** Laptop PC Use Rules, p. 3.

---

## 4.5 Password and Credential Protection

Users are required to protect the laptop with a password and must not share credentials/passwords with others.

**Architecture consequence**
Credential-sharing incidents can be relevant to Discipline/Responsibility when verified and applicable. AIPMS itself should also enforce strong identity controls and avoid shared accounts.

**Source:** Laptop PC Use Rules, p. 3.

---

## 4.6 File Protection, Backup and Safe Internet Use

The rules require users to protect important files, maintain appropriate backup where needed, and exercise caution when browsing the internet, using email, or downloading files/software.

**Architecture consequence**
- Data-loss/security events need provenance and context.
- Separate malicious/unauthorized behavior from accidental technical error.
- Do not convert every security incident into poor performance without determining role, control, causation, and official finding.

**Source:** Laptop PC Use Rules, p. 3.

---

## 4.7 Fault, Loss, Theft and Reporting Responsibility

The policy requires timely reporting/handling of device problems and imposes responsibility on the assigned user for proper use, preservation, and security. Loss/theft/damage is subject to formal reporting and responsibility rules.

**Architecture consequence**
Relevant evidence should preserve:
- when the incident occurred;
- when it was reported;
- whether the user followed required reporting/escalation;
- official investigation/finding;
- recovery/correction outcome.

A reported incident is not automatically negligence. The finding and surrounding facts matter.

**Source:** Laptop PC Use Rules, p. 3.

---

## 4.8 Device Lifecycle

The rules address useful life, maintenance/repair, custody, and disposal/unserviceable handling through the relevant DESCO process.

**Architecture consequence**
Asset lifecycle belongs to the source asset/administrative system. AIPMS should normally reference verified asset/compliance events rather than become the authoritative asset-management system.

---

# 5. DESCO Code of Conduct — Limited Senior-Governance Extract

## 5.1 Applicability Boundary

The supplied Code of Conduct is specifically framed for DESCO Board-level governance, including the Chairperson, Board members, and CEO/Managing Director. Its objectives include transparency, integrity, accountability, ethical conduct, and corporate governance.

**Critical AIPMS rule**
Do **not** cite this Code as the general conduct standard for all DESCO employees.

For ordinary employee behavior, use the Service Rule 2017 and other employee-applicable policies.

**Source:** Code of Conduct, p. 1.

---

## 5.2 Regulatory Compliance and Ethical Conduct

For covered actors, the Code requires compliance with applicable laws/rules/regulations and high standards of integrity, honesty, and ethical conduct.

**AIPMS relevance**
Useful for governance controls involving covered senior actors, but not a substitute for ordinary employee appraisal definitions.

**Source:** Code of Conduct, p. 2.

---

## 5.3 Conflict of Interest

The Code requires covered directors to avoid conflicts between personal interests and company interests and to refrain from participation/voting where a conflict exists.

**Architecture consequence**
AIPMS should be capable of representing conflict-of-interest restrictions/recusal for decision-makers if DESCO adopts such controls for the appraisal process. The supplied Code directly supports this principle only for its covered population.

Do not silently apply Board-specific recusal rules to all evaluators as established DESCO policy; raise broader evaluator-conflict rules as a governance decision if needed.

**Source:** Code of Conduct, p. 2.

---

## 5.4 Fair Dealing

Covered actors are expected to deal fairly with stakeholders/employees and discharge duties fairly and impartially.

**AIPMS relevance**
Supports governance/fairness expectations for covered senior decision-makers. It does not establish a universal employee ACR scoring rule.

**Source:** Code of Conduct, p. 3.

---

## 5.5 Confidential Information

The Code requires confidentiality of sensitive company/stakeholder information except where disclosure is authorized or legally required and prohibits using confidential information for personal advantage/profit.

**Architecture consequence**
Reinforces:
- restricted appraisal access;
- controlled exports;
- confidential AI/prompt handling;
- audit logging;
- no unauthorized secondary use of employee/appraisal information.

For ordinary employees, the same confidentiality requirement should be grounded primarily in Service Rule §7.1/§7.2.

**Source:** Code of Conduct, p. 3.

---

## 5.6 Company Assets

Covered actors must protect company assets/property and ensure use for legitimate company purposes.

**AIPMS relevance**
Governance context only for covered actors; ordinary-employee asset conduct should be grounded in the Service Rules and applicable operational policies such as the Laptop Rules.

**Source:** Code of Conduct, p. 3.

---

## 5.7 Disclosure, Strategic Governance and Meetings

The Code includes:
- disclosure of material interests;
- strategic-planning responsibilities;
- informed/independent judgment;
- meeting participation obligations;
- additional expectations for independent directors;
- reporting unethical behavior/fraud;
- protection of company/shareholder/employee interests.

**Architecture relevance**
These items may inform governance workflows for covered senior officers. Do not turn them into general employee ACR metrics.

**Source:** Code of Conduct, pp. 3–5.

---

## 5.8 Certification and Change

Covered directors submit periodic/annual compliance certification. The Board may amend the Code. The supplied Code states an effective date of 17 October 2019.

**Architecture consequence**
Policies and governance rules should be versioned/effective-dated rather than assumed permanent.

**Source:** Code of Conduct, pp. 5–6.

---

# 6. Cross-Document Architecture Rules for AIPMS

The following are the main architecture conclusions supported by the official policy set.

## 6.1 Policy Applicability Must Be Explicit

Every policy-derived evidence item should be able to answer:
- Which policy/version applied?
- To which employee/role did it apply?
- On what date?
- What actual behavior/record demonstrates relevance?
- Was the fact verified/finalized?
- Which ACR metric, if any, does the behavior directly support?

A policy mention alone is not evidence.

---

## 6.2 Separate Raw Facts from Disciplinary Findings

Example:

`Late attendance record`
is not the same object as
`disciplinary finding for habitual late attendance`.

Both may exist, but they have different:
- provenance;
- procedural status;
- meaning;
- admissibility;
- correction/appeal lifecycle.

AIPMS must not double-count them simply because they refer to the same underlying event.

---

## 6.3 Preserve Procedural Finality

Compliance/disciplinary records require status/finality. At minimum, architecture must be able to distinguish:
- reported/alleged;
- under review/inquiry;
- decision issued;
- penalty imposed;
- appealed/reviewed;
- final;
- reversed/superseded/reinstated.

For APR assessment, follow the TOR rule: **only finalized and authorized disciplinary records are eligible as disciplinary evidence.**

---

## 6.4 Preserve Corrections, Appeals and Supersession

Do not destructively replace an old decision with a new one.

Preserve:
- original record;
- correction/appeal/review;
- revised outcome;
- timestamps;
- authority;
- reason;
- which version was available to each appraisal decision.

---

## 6.5 Confidentiality Is Structural, Not Cosmetic

Confidentiality requirements imply:
- least-privilege access;
- role + case/stage/assignment-aware authorization;
- server-side redaction;
- access auditing;
- controlled document export;
- secure AI-context assembly;
- restricted logs;
- no reliance on frontend hiding alone.

---

## 6.6 Organization Structure Is Effective-Dated Context

The organogram is useful context, but DESCO changes organization structures and posts.

Architecture should preserve:
- current organizational relationship;
- effective period;
- historical snapshot/value needed for an old appraisal;
- actual appraisal-authority assignment separately.

Do not hard-code a 2018/2020 structure into business logic.

---

## 6.7 Role Context Must Not Change Official Metric Meaning

The same official ACR metric can look different by role.

Example:
- ICT: authorized change/access process;
- Procurement: procurement/inspection process;
- S&D: operating/customer-service procedure;
- Finance: financial control/documentation;
- Network Operation: operational/safety procedure.

Use role context to interpret evidence, not to create unofficial role-specific scoring scales.

---

## 6.8 Security/Confidentiality Is Not Automatically Safety Awareness

Information security, credential protection, confidentiality, and authorized-device use are generally better grounded in:
- Discipline;
- Sense of Responsibility;
- Professional Knowledge/Quality where role competence is involved.

Map to **Safety Awareness** only where the actual role/event concerns physical/operational/workplace safety or another clearly safety-relevant context.

---

## 6.9 Policy Violations Do Not Automatically Produce Scores

Do not implement:
`policy violation -> metric -> fixed mark`

Instead:
`verified event/record -> applicability + context + metric relevance -> annual evidence set -> AI recommendation/human appraisal`

The official ACR scale remains authoritative.

---

## 6.10 Appraisal Outputs Can Have Material Employment Consequences

Because performance appraisal is connected in the Service Rules to annual increment/pay raise and can contribute to promotion decisions, AIPMS must preserve:
- final result;
- evaluator/authority;
- applicable instrument;
- evidence snapshot;
- approval/finalization;
- audit trail;
- later correction/supersession where permitted.

---

# 7. What This Extract Does NOT Establish

Do not infer the following from these four policy documents alone:

- exact ACR Reporting/Countersigning/Certifying/Approving assignments;
- exact ACR disclosure rights;
- exact 1–4 or 1–5 behavioral anchors;
- event-level scores;
- automatic marks for misconduct;
- general evaluator conflict-of-interest rules for all staff;
- exact promotion/increment formula from ACR total;
- employee eligibility for Grade 1–11 vs Grade 12–16 solely from organogram title;
- whether every listed/outsourced role participates in AIPMS;
- health data eligibility for performance scoring;
- current live organizational reporting lines after later reorganizations.

For those questions, use the higher-priority ACR/TOR/ACR Instructions and seek DESCO clarification where the official source pack is silent or contradictory.

---

# 8. Source Register

1. **DESCO Service Rule 2017**
   - Promotion policy / service conditions: relevant sections around printed pp. 14–17.
   - General Conduct & Discipline: Chapter VII, §§7.1–7.12, printed pp. 25–31.

2. **DESCO Organogram 2018**
   - Organization overview and detailed functional structures, pp. 2–15.
   - Includes later board-approved ICT/health setup notes within the supplied document.

3. **দাপ্তরিক ল্যাপটপ পিসি ব্যবহার ও সংরক্ষণের নিয়মাবলী (2024)**
   - DESCO Administration Division notice dated 28 August 2024.
   - Official laptop allocation/use/security/custody/lifecycle requirements.

4. **DESCO Code of Conduct**
   - Board/Chairperson/CEO-MD governance code.
   - Regulatory compliance, ethics, conflict of interest, fair dealing, confidentiality, assets, governance duties, certification.
   - Effective 17 October 2019.

---

## Final Usage Rule for Claude

Use this extract as **supporting official-policy context**, not as the highest project authority.

When a policy point materially affects architecture or appraisal logic:
1. check whether the TOR/ACR/ACR Instructions impose a more specific rule;
2. preserve the policy’s applicability scope;
3. distinguish raw fact, allegation, disciplinary finding, and finalized record;
4. do not invent a score or policy outcome;
5. consult the original policy PDF when exact wording or legal interpretation matters.
