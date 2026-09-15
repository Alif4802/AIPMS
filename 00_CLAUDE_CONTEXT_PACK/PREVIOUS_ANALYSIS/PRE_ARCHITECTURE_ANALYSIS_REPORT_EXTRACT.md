# Source Extraction

**Original file:** DESCO_AIPMS_Architecture_RnD_Report.md  
**Original relative path:** 04_PRE_ARCHITECTURE_ANALYSIS\DESCO_AIPMS_Architecture_RnD_Report.md  
**Source category:** PREVIOUS_ANALYSIS (Precedence Rank 6)  
**Extraction method:** Direct Markdown mirror  
**Extraction date:** 2026-09-15  
**Number of pages/sheets/slides:** 1322 lines  
**Extraction completeness:** 100% complete verbatim companion  
**Notes:** Pre-HLD / Pre-SDD Architecture R&D Report analyzing enterprise integration risks, system contradictions, and offline AI constraints.

---

# DESCO AIPMS — Architecture & R&D Analysis

**Status:** Pre-HLD / Pre-SDD architecture and R&D analysis
**Prepared from:** TOR (Revised 2, 10 Aug 2026), ACR Format (Pay-Grade 1–11 form, 8 pages), AI Appraisal & Assessment R&D Handoff
**Excluded by instruction:** all prior architecture documents, hardening plans, boilerplate and implementation decisions
**Output type:** analysis and recommendation. No implementation code. No boilerplate. No SDD/HLD.

---

## 0. Source Base and Its Limits

Three documents were treated as authoritative. Before any architecture is proposed, two facts about the source base itself must be stated, because both constrain how much of this report can be considered final.

**0.1 Only one of the two ACR forms was supplied.**
The provided `ACR Format` file contains 8 pages and is a single form: **এ.সি.আর ফরম (পে-গ্রেড ১-১১)** — the 25-criterion, 4-point-scale instrument. The TOR (§1, §3.2.1.1) states that a second instrument exists for Grade 12–16 with **20 criteria on a 5-point scale**. That form has not been provided. Consequently:

- The 20 criteria for Grade 12–16 are unknown.
- Whether the Grade 12–16 form uses the same performance bands is **inferred, not verified**. The TOR asserts the bands (95–100 / 85–94 / 75–84 / 60–74 / <60) generally; the bands table is visible only on the Grade 1–11 form.
- Whether the Grade 12–16 form has the same pen-picture, recommendation, health, bio-data and multi-tier signature structure is unknown.

This is a **hard blocker for requirements completeness**, not a detail. The architecture below is deliberately instrument-agnostic so that the second form can be onboarded as configuration rather than code, but the SRS cannot be closed without it.

**0.2 What the supplied ACR form actually contains.**
Recording this explicitly, because several TOR statements diverge from it.

| Page | Section | Filled by | Content |
|---|---|---|---|
| 1 | Cover | — | গোপনীয় marking; form tier (পে-গ্রেড ১-১১); year/period; name, designation, ID |
| 2 | স্বাস্থ্য পরীক্ষা প্রতিবেদন | Health Officer | Height, weight, eyesight, blood group, blood pressure, X-ray report, ECG report, medical classification, nature of health weakness/incapacity |
| 3 | জীবনবৃত্তান্ত | **Appraisee** | Name, designation, ID, marital status, current number of children, cadre name, date of joining current post, pay scale, current pay, education, training (domestic/foreign), foreign-language proficiency (speaking/reading/writing), full tenure of service under the reporting officer (from–to), and **item 12: brief work description for the period under consideration (5 slots ক–ঙ)** |
| 4 | মূল্যায়নের বিষয় | **Reporting Officer** | 25 criteria, each marked ✓ or initialled in one of four columns (৪ / ৩ / ২ / ১); মোট প্রাপ্ত নম্বর; band table (অসাধারণ 95–100, অত্যুত্তম 85–94, উত্তম 75–84, চলতি মান 60–74, চলতি মানের নিচে <60) |
| 5 | লেখচিত্র + সুপারিশ | **Reporting Officer** | Free-text pen picture; training/skill-development recommendation; promotion-eligibility category (4 mutually exclusive options, non-applicable ones struck out); other recommendation |
| 6 | Three comment blocks | Countersigning / Certifying / Approving officers | For each: comment (if any) + **"সামগ্রিক মূল্যায়নের ভিত্তিতে প্রদেয় মোট নম্বর"** — a single holistic total in a box + signature, name, designation, date |
| 7–8 | নির্দেশাবলী | — | 24 numbered instructions governing the whole process |

The 25 criteria on page 4 are: শৃঙ্খলা বোধ; বিচার ও মাত্রাজ্ঞান; বুদ্ধিমত্তা; উদ্দাম ও উদ্যোগ; ব্যক্তিত্ব; সহযোগিতা; সময়ানুবর্তিতা; নির্ভরযোগ্যতা; দায়িত্ববোধ; কাজে আগ্রহ; ব্যবস্থা গ্রহণে ও আদেশ পালনে তৎপরতা; নিরাপত্তা সচেতনতা; জনসাধারণের সাথে ব্যবহার; পেশাগত জ্ঞান; কাজের মান; সম্পাদিত কাজের পরিমাণ; তদারকি ও পরিচালনার সামর্থ্য; সহকর্মীদের সাথে সম্পর্ক; সিদ্ধান্ত গ্রহণে দক্ষতা; সিদ্ধান্ত বাস্তবায়নে সামর্থ্য; অধীনস্থদের প্রশিক্ষণদানে আগ্রহ ও দক্ষতা; প্রকাশ ক্ষমতা (লিখন); প্রকাশ ক্ষমতা (বাচনিক); বার্ষিক গোপনীয় অনুবেদন লিখন ও প্রতিস্বাক্ষরকরণে তৎপরতা; কর্তব্যনিষ্ঠা।

Three structural observations follow immediately and shape the entire design:

1. **The criteria are almost entirely trait/behavioural, not KPI/target-based.** Only a handful (সময়ানুবর্তিতা, সম্পাদিত কাজের পরিমাণ, বার্ষিক গোপনীয় অনুবেদন লিখন ও প্রতিস্বাক্ষরকরণে তৎপরতা) have any natural objective indicator. There are no targets, no weights, no variance analysis anywhere on the form. This collides head-on with the TOR's KPI-engine language (see §N).
2. **Arithmetic is closed and unweighted.** 25 criteria × max 4 = 100. 20 criteria × max 5 = 100. Both instruments max at exactly 100, which is almost certainly why they can share one band table. The total is a plain sum of integer ordinal marks. Note also that the **minimum** possible totals differ: 25 (Grade 1–11) versus 20 (Grade 12–16). The two scales are therefore *not* linearly comparable even though both cap at 100.
3. **Higher authorities do not re-score criteria.** The reporting officer produces 25 criterion marks. The countersigning, certifying and approving officers each produce **their own single holistic total** plus comments. There is no mechanism on the form by which an upper officer edits a criterion mark. This is the single most important structural fact for the workflow model, and it rules out the "one mutable score field" design the brief warned against — not merely as a design preference, but as a matter of form fidelity.

**0.3 The instructions carry binding business rules.** Pages 7–8 are not boilerplate. Rules extracted with direct architectural consequence:

- **Instr. 1** — one ACR per **calendar year** (পঞ্জিকা বৎসর) per officer.
- **Instr. 2** — special ACRs on higher-authority direction; the appraisee must have served **at least 3 months** under the reporting officer.
- **Instr. 3** — where there is an adverse remark, **only the relevant excerpt** is sent to the appraisee, not the report.
- **Instr. 4** — the ACR is never folded; inter-office transmission in a sealed envelope marked গোপনীয়.
- **Instr. 5** — the **HRM division determines** who the reporting, countersigning, certifying and approving officers are.
- **Instr. 6** — the immediate next higher officer initiates; the officer above the reporting officer countersigns; where applicable the officer above the countersigning officer certifies; **both must have সংশ্লিষ্টতা (connection) with the appraisee's work**.
- **Instr. 8–9** — the appraisee completes the bio-data section in **two copies**, signed and dated, and must confirm the personal particulars are complete and true.
- **Instr. 10** — the reporting officer must be objective, careful, must not evade with ambiguity or clever phrasing, and must avoid both exaggeration and gross under-evaluation.
- **Instr. 11** — **failures and weaknesses must be brought to the officer's notice as soon as they are observed, and an opportunity to correct must be given *before* the item is recorded in the ACR.**
- **Instr. 13** — the pen picture may carry an overall assessment and should briefly describe anything not reflected in parts 3 and 4.
- **Instr. 15** — an ACR is submitted for every officer who has served **at least 3 months** under the reporting officer.
- **Instr. 16, 19, 22** — each upper officer evaluates the lower officer's comments **in the light of personal observation**, writes their own opinion, and states a total on overall assessment.
- **Instr. 17, 20, 23** — if an upper officer believes a specific comment is wrong and should be cancelled, they record an appropriate alternative comment; where they fully disagree, they write their own opinion under their own heading.
- **Instr. 24** — after approval the form goes to the HRM division.

Instruction 11 is the sleeper requirement. It means **a negative observation is not admissible evidence until it has been disclosed to the employee and an opportunity to correct has passed.** That is an eligibility gate, and it must be enforced by the system rather than left to officer discipline.

---

## A. Requirements Model

Classification key:
**C** = Contractual / must implement · **BP** = Business policy (DESCO-owned, configurable) · **AR** = Architectural requirement · **TP** = Technology prescription · **AMB** = Ambiguous / requires DESCO clarification · **RISK** = Potential conflict or delivery risk

### A.1 Instrument fidelity

| ID | Requirement | Source | Class | Note |
|---|---|---|---|---|
| R-01 | Replicate both ACR instruments without alteration unless separately approved by DESCO | TOR §1, §3.2.1.1(a) | **C** | The strongest constraint in the TOR. Overrides any design impulse to "improve" the form. |
| R-02 | Grade 1–11 instrument: 25 criteria, 4-point scale (4/3/2/1) | ACR p.4; TOR §1 | **C** | Verified against the form. |
| R-03 | Grade 12–16 instrument: 20 criteria, 5-point scale | TOR §1, §3.2.1.1(a) | **C / AMB** | Form not supplied. Criteria unknown. Blocker. |
| R-04 | Performance bands 95–100 / 85–94 / 75–84 / 60–74 / <60 | ACR p.4; TOR §3.2.1.1(a) | **C** | Verified for Grade 1–11 only; asserted for both by TOR. |
| R-05 | Any future change to criteria or weightages requires a DESCO-approved change request | TOR §3.2.1.1(a) | **C / AR** | Implies the instrument must be a versioned first-class configuration artefact. |
| R-06 | Criterion marks are integers on a small ordinal scale; total is their sum | ACR p.4 | **C / AR** | Forbids surfacing continuous scores (e.g. 4.3) as official marks. |
| R-07 | Instrument selection is driven by pay grade | TOR §1 | **C / AMB** | Behaviour on mid-cycle grade change is unspecified. |
| R-08 | Support the recommendation section: training/skill development, promotion-eligibility category, other recommendation | ACR p.5; TOR §3.2.3.3 | **C** | Promotion category is 4 mutually exclusive options. |
| R-09 | Digitize the health examination fields (height, weight, eyesight, blood group, BP, X-ray, ECG, medical classification, nature of incapacity), completed by the Health Officer | ACR p.2; TOR §3.2.3.2(i) | **C** | Digitization only. Not an appraisal input. |
| R-10 | Ad-hoc health concern workflow | TOR §3.2.3.2(ii) | **AMB** | TOR itself marks this "scope to be confirmed". |
| R-11 | Employee bio-data self-completion including item 12 work description | ACR p.3; TOR §3.2.3.1 | **C** | The paper form already contains the self-input concept. |
| R-12 | Employee self-input is factual, **not** a self-rating or self-score | TOR §3.2.3.1 | **C / BP** | Architecturally: self-input can never write into a criterion mark field. |
| R-13 | Replace dual-copy paper submission with a single digital record + audit trail | TOR §1 | **C** | Supersedes ACR instr. 8 and 12 (two copies) — a deliberate, TOR-sanctioned deviation. Worth noting in the Inception Report. |

### A.2 Authority, workflow and eligibility

| ID | Requirement | Source | Class | Note |
|---|---|---|---|---|
| R-20 | Hierarchy: Reporting Officer → Countersigning Officer → Certifying Officer (conditional) → Approving Officer | TOR §3.2.3.3; ACR instr. 6, 18, 21 | **C** | Ordering confirmed by both sources. |
| R-21 | The certifying stage is conditional, applicable only in certain cases per DESCO's ACR guidelines | TOR §1, §3.2.3.3; ACR instr. 18 | **C / AMB** | The *condition* is never stated in either document. Must be obtained. |
| R-22 | HRM division determines the officers for each case | ACR instr. 5 | **BP / AR** | Authority chain is administratively assigned, not purely derived from the org chart. |
| R-23 | Reporting and countersigning officers must have work-connection (সংশ্লিষ্টতা) with the appraisee | ACR instr. 6 | **BP** | "Connection" is undefined and probably not machine-decidable. Treat as an attestation, not a computed check. |
| R-24 | Minimum 3-month supervision before an evaluation may be initiated | TOR §1, §3.2.1.2; ACR instr. 2, 15 | **C / AMB** | **The ACR ties the 3-month rule to the reporting officer (instr. 15) and to special ACRs (instr. 2). The TOR extends it to countersigning and certifying officers. That extension is a TOR interpretation, not an ACR rule.** Must be confirmed. |
| R-25 | Higher officers give a holistic total on overall assessment, not per-criterion marks | ACR p.6, instr. 16/19/22 | **C / AR** | Forbids the mutable-score model. |
| R-26 | An upper officer may record an alternative comment replacing a lower officer's specific comment, or state full disagreement under their own heading | ACR instr. 17, 20, 23 | **C / AR** | Requires comment supersession as an explicit, preserved relationship — never in-place edit. |
| R-27 | Human authority is preserved for all final decisions; AI output is for review, modification and approval | TOR §1, §3.2.3.3 | **C** | |
| R-28 | Complete audit trail of inputs, AI recommendations, modifications, approvals, final evaluations | TOR §1, §3.7(a) | **C / AR** | |
| R-29 | Real-time monitoring of appraisal progress, pending actions, completion status | TOR §1, §3.6 | **C** | |
| R-30 | How the final official score is determined from up to four independently recorded totals | — | **AMB** | **Neither document states this.** Highest-priority policy question. |

### A.3 Evidence, context and eligibility

| ID | Requirement | Source | Class | Note |
|---|---|---|---|---|
| R-40 | Continuous recording of achievements, contributions, shortfalls and observations throughout the appraisal period | TOR §1, §3.4 | **C** | This is the genuine novelty versus the paper process. |
| R-41 | A recorded deficiency must be made visible to the employee at entry (or at a configurable interval) with an opportunity to respond or improve **before** it enters the final evaluation | TOR §1; ACR instr. 11 | **C / AR** | Enforce as an admissibility gate on negative evidence. |
| R-42 | Only finalized and authorized disciplinary records may be considered | TOR §3.3.4 | **C / AR** | Lifecycle-state gate on evidence. |
| R-43 | Attendance, training, reward/recognition and compliance data feed the AI engine | TOR §3.3.1–3.3.5 | **C** | |
| R-44 | Evidence may be entered manually or retrieved by API where one exists | TOR §1, §3.3.5, §4 | **C** | |
| R-45 | Entries capture employee, date, category, description, remarks; support document/evidence upload; store with user identity and timestamps | TOR §3.4 | **C** | |
| R-46 | During the pilot, the system only reads from source systems; it must not write, modify or update any existing DESCO system | TOR §1 | **C / AR** | Strong integration constraint. Design for read-only now, write-capable later. |
| R-47 | Integration limited to: promotion effect on personal information, attendance, training results, disciplinary actions, awards/rewards | TOR §1, §4 | **C** | |
| R-48 | Health data must not influence performance evaluation | Implied: ACR separates p.2 from p.4; not stated in TOR | **BP / RISK** | **The TOR never explicitly forbids health data from reaching the AI engine.** This must be made an explicit rule, not an assumption. |

### A.4 AI, analytics and validation

| ID | Requirement | Source | Class | Note |
|---|---|---|---|---|
| R-60 | AI generates recommended APR marks applying the correct tier rubric | TOR §1, §3.2.2.1 | **C** | |
| R-61 | AI generates draft pen pictures | TOR §1, §3.2.2.1 | **C / AMB** | The ACR pen picture is written by the reporting officer only. The TOR implies drafts for all four authorities. Clarify. |
| R-62 | AI consistency checks | TOR §3.2.2.1, §3.2.3.3 | **C** | Best served by rules, not a model. |
| R-63 | Past-vs-current analysis and peer comparison | TOR §3.2.2.1 | **C / RISK** | Requires historical data that does not exist at pilot start. |
| R-64 | Predictive analytics: attrition risk, training needs, future performance | TOR §3.2.2.1 | **C / RISK** | Not statistically supportable from one pilot cycle. See §G.4. |
| R-65 | Anomaly detection for irregular ratings | TOR §3.2.2.1, §3.2.2.2 | **C** | Statistical, not LLM. |
| R-66 | Bias detection: regression, disparity metrics, demographic parity, disparate impact, equal opportunity; evaluator behaviour models (leniency, severity, recency, halo); per-evaluator bias scores | TOR §3.2.2.2 | **C / RISK** | Several named metrics are undefined without protected attributes and/or ground-truth labels. See §I.5. |
| R-67 | Explainability & Bias Dashboard exposing rationale and contributing factors with relative weight | TOR §3.2.2.2, §6.2 | **C / AR** | Achievable by construction for deterministic components; requires structured, citation-bearing AI output for the rest. |
| R-68 | AI accuracy/agreement benchmarking per grade tier against a minimum threshold agreed with DESCO before Go-Live | TOR §3.8(b) | **C / AMB** | Threshold not set. Benchmark corpus does not exist. |
| R-69 | Robustness testing on incomplete/missing/edge-case data | TOR §3.8(b) | **C / AR** | Requires the AI to be able to return "no recommendation". |
| R-70 | Human-override rate and pattern monitoring | TOR §3.8(b) | **C / AR** | Only meaningful if the AI recommendation is recorded before the human mark. See §O.1. |
| R-71 | Rubric/weight changes trigger model revalidation before redeployment | TOR §3.8(c) | **C / AR** | Implies a dependency graph between rubric version and model validation certificate. |
| R-72 | Model versions tracked with rollback capability | TOR §3.8(c), §6.2 | **C / AR** | |
| R-73 | Deliver labelled/annotated datasets and annotation guidelines | TOR §6.3 | **C / RISK** | There is no historical labelled ACR corpus. See §N. |
| R-74 | Deliver trained models and MLOps setup (CI/CD, model registry, monitoring) | TOR §6.2 | **C** | |

### A.5 Security, platform and delivery

| ID | Requirement | Source | Class | Note |
|---|---|---|---|---|
| R-80 | RBAC with granular permissions | TOR §3.7(a), §5.2 | **C** | Role alone is insufficient; see §I.1. |
| R-81 | Field-level redaction so only the adverse excerpt reaches the employee | TOR §1, §3.2.3.3, §3.7(a); ACR instr. 3 | **C / AR** | |
| R-82 | AES-256 at rest for Name, NID, and Birth Certificate / Birth Date; TLS 1.2+ in transit | TOR §3.2.2.2, §5.2 | **C / AMB** | The two clauses disagree on the third field. Encrypting `Name` has severe operational consequences. |
| R-83 | Two-factor authentication; SSO | TOR §3.1, §5.2 | **C** | |
| R-84 | Alignment with ISO/IEC 27001 practices | TOR §5.2, §6.1 | **C / AMB** | "Compliance" vs "alignment" — a vendor cannot confer certification on DESCO. |
| R-85 | Bilingual Bangla/English across all modules | TOR §3.1 | **C** | Includes AI-generated narrative. Significant NLP risk. |
| R-86 | On-premise deployment with cloud flexibility | TOR §5.1 | **C** | Constrains all AI options. |
| R-87 | Microservices architecture | TOR §3.1 | **TP / RISK** | See §J. |
| R-88 | Java Spring Boot / React / Oracle or PostgreSQL / Python + TensorFlow / REST | TOR §5.1 | **TP** | See §J.1. |
| R-89 | Mobile application for performance input, with installable builds and full source | TOR §3.4, §6.2 | **C** | |
| R-90 | Full IP, source code, documentation and AI models vest in DESCO on acceptance | TOR §9 | **C** | Constrains model licensing choices — see ADR-14. |
| R-91 | 6-month implementation, 6-month support, phase-tied payments | TOR §7.1, §10 | **C / RISK** | The two tables disagree on percentages. See §N. |

---

## B. Core Domain Model

### B.1 Bounded contexts

The system is not one model. Nine contexts, chosen so that the confidentiality and eligibility boundaries fall on *deployment* boundaries rather than on code conventions.

```
┌──────────────────────────────────────────────────────────────────┐
│  ORGANISATION & AUTHORITY   │  APPRAISAL INSTRUMENT & CYCLE      │
│  effective-dated org, posts,│  versioned form definitions,       │
│  supervision, authority     │  criteria, scales, bands, anchors  │
│  chains                     │  applicability, policy versions    │
├─────────────────────────────┼────────────────────────────────────┤
│  FACT & CONTEXT             │  EVIDENCE ELIGIBILITY              │
│  immutable raw facts,       │  the only path from facts to any   │
│  observations, org context, │  evaluation input. Enforced as a   │
│  provenance, corrections    │  boundary, not a filter.           │
├─────────────────────────────┼────────────────────────────────────┤
│  EVALUATION                 │  DECISION & WORKFLOW               │
│  deterministic scoring,     │  append-only staged decisions,     │
│  AI recommendation runs,    │  returns, supersessions, final     │
│  input snapshots            │  authority resolution              │
├─────────────────────────────┼────────────────────────────────────┤
│  DISCLOSURE                 │  ANALYTICS & FAIRNESS              │
│  what each subject may see, │  rater effects, anomalies,         │
│  adverse-excerpt packets    │  aggregates, cell suppression      │
├─────────────────────────────┴────────────────────────────────────┤
│  CONFIDENTIAL HEALTH RECORD  — separate schema, separate keys,    │
│  separate credentials, structurally unreachable from EVALUATION   │
└───────────────────────────────────────────────────────────────────┘
                    AUDIT & GOVERNANCE spans all
```

### B.2 Aggregates and why they exist

**`AppraisalInstrument` (versioned)** — the machine-readable form. Holds `CriterionDefinition[]` (code, Bangla/English label, ordinal position), `ScaleDefinition` (allowed values, direction, semantic labels), `BandDefinition[]`, `ApplicabilityRule[]`, and `EvaluationStrategy` per criterion. Exists because R-05 makes the form a change-controlled artefact and R-03 requires a second instrument to be onboarded without code change. **An instrument version is frozen per cycle**; a mid-cycle rubric change never applies to in-flight cases.

**`BehaviouralAnchor` (versioned, child of criterion)** — the descriptive definition of what a 4, 3, 2 or 1 means for a given criterion. *These do not exist on the paper form.* The ACR gives bare numeric columns and relies on the officer's judgement. Writing anchors is therefore **net-new institutional content that DESCO must author and approve** — it is not a technical deliverable the vendor can invent. This is flagged as a policy decision (M-07) and, arguably, as a hidden scope item in the TOR.

**`AppraisalCycle`** — period, tier applicability, instrument versions in force, policy version set, open/close dates, and the state of the cycle. Anchors the calendar-year rule (ACR instr. 1) and the fiscal/calendar ambiguity (N-04).

**`AppraisalCase`** — one employee, one cycle, one instrument version. The process root. Holds the resolved `AuthorityChain`, the current stage, and references to the bio-data submission, evidence snapshots, evaluation runs, decisions and disclosure packets. It does **not** hold a `score` field. That absence is deliberate and load-bearing.

**`AuthorityChain` + `AuthorityAssignment`** — the assigned officers for a case, snapshotted at cycle open, each assignment carrying role, actor, assigning HRM user, effective period, eligibility evaluation result and attestation of work-connection (R-22, R-23). Changes create new assignment versions with explicit downstream invalidation, never silent replacement.

**`RawFact`** — an atomic, immutable, typed record of something that happened, carrying `occurredAt`, `recordedAt`, `provenance`, `verificationState` and a payload. Attendance events, training completions, disciplinary outcomes, awards, complaint resolutions, task/project outcomes. Never carries a judgement or a score.

**`Observation`** — a human-authored narrative record about an employee: an achievement, a contribution, a shortfall, a supervisor note. Immutable; corrections supersede. Carries `authorRole`, `category`, `occurredAt`, `recordedAt`, attachments, and — critically — `disclosureState` and `responseWindow` for negative observations (R-41).

**`ContextFact`** — a condition, not an event about a person: severe-weather advisory, office closure, emergency duty order, festival period, system outage, approved leave block, organisational restructure. Recorded **once at organisation or org-unit level** with a validity interval, and joined to a person's facts by time and org-unit at evaluation time. This is the mechanism that prevents scenario explosion (§C).

**`EvidenceEligibilityPolicy` (versioned)** — for a given criterion, which fact types, observation categories and context types are admissible, with what recency window, what minimum verification state, and what disclosure precondition. Owned by DESCO, expressed as configuration, evaluated at the boundary.

**`EvidenceItem`** — deliberately **not** a stored aggregate. It is a *derived projection*: `(RawFact | Observation) × Criterion × EligibilityPolicyVersion → EvidenceItem`. The same attendance record is strong evidence for সময়ানুবর্তিতা, weak context for কর্তব্যনিষ্ঠা, and inadmissible for ব্যক্তিত্ব. Storing evidence as a first-class row forces you either to duplicate it per criterion or to pretend it is criterion-neutral. Deriving it keeps one fact and many admissible readings.

**`DerivedIndicator`** — a deterministic, reproducible metric computed from raw facts over a period: punctuality rate, absence-without-leave count, training completion ratio, complaint resolution rate, ACR-submission timeliness. Named separately from evidence because indicators are *calculated*, versioned by formula, and are the only legitimate basis for OBJECTIVE criteria.

**`EvaluationInputSnapshot`** — a content-addressed, immutable bundle: the set of fact versions, observation versions, context versions, derived indicator values, instrument version, anchor version, eligibility policy version and scoring policy version that a given evaluation saw. **This is the central artefact of the entire architecture.** It is what makes an appraisal reproducible three years later in front of an auditor or a grievance panel, and it is what TOR §3.8 and §6.2 implicitly require without naming.

**`EvaluationRun`** — one execution against a snapshot. Records deterministic results, AI recommendations, model descriptor (name, version, weights hash, quantisation, provider), prompt template version, latency, and full prompt/response for audit. Runs are additive; a re-run never overwrites.

**`CriterionRecommendation`** — per criterion: recommended ordinal mark **or** `INSUFFICIENT_EVIDENCE`, confidence, evidence strength, justification text, and a mandatory list of cited evidence references. A recommendation with no citations is invalid by construction.

**`StageDecision`** — immutable, append-only. The workflow's only writable surface. Detailed in §E.

**`DisclosurePacket`** — the computed, versioned answer to "what may this subject see about this case, right now". Generated by policy, persisted, and auditable — never assembled ad hoc in a controller or hidden in the UI.

**`HealthAssessment`** — segregated aggregate, separate schema and credentials. Linked to the case by identifier only.

**`BioDataSubmission`** — the appraisee's page-3 content, including item-12 work descriptions, with attestation of truth (ACR instr. 9), signature and timestamp.

**`Recommendation`** — training/skill recommendation, promotion-eligibility category (single-select of four), other recommendation. Authored by the reporting officer.

### B.3 Assessment of the concept names proposed in the brief

| Proposed | Verdict | Reasoning |
|---|---|---|
| `PerformanceEvent` | **Reject as a separate type** | Splits into `RawFact` (system/objective) and `Observation` (human narrative). They have completely different provenance, reliability, correction and disclosure semantics. One type would carry a permanently confusing nullable half. |
| `EvidenceItem` | **Keep, but demote to a derived projection** | See above. This is the most consequential naming change. |
| `ContextFact` / `ContextEvent` | **Keep, merge into `ContextFact`** | The distinction between a fact and an event dissolves once everything carries a validity interval. |
| `EvidenceEligibilityPolicy` | **Keep, promote to first-class and to a deployment boundary** | Too important to be a service method. |
| `EvidenceSignal` | **Rename to `DerivedIndicator`** | "Signal" invites the reading that it is an input to a model. It is a calculated number with a versioned formula, which is a stronger and more auditable claim. |
| `MetricEvaluationPolicy` | **Rename to `CriterionEvaluationPolicy`** | "Metric" is imported from the TOR's KPI framing and does not exist in the ACR vocabulary. Aligning names to the ACR keeps the team honest about what the instrument actually is. |
| `BehavioralAnchor` | **Keep, and flag as missing institutional content** | Essential, and absent from the source form. |
| `EventSignificance` | **Reject as a stored field** | If a data-entry user can mark their own observation "highly significant", you have handed them a weighting dial and created a manipulation surface. Significance must be *computed* at evaluation time from context, corroboration, recurrence and policy. |
| `EvidenceTimeline` | **Keep as a read model, not an aggregate** | It is a projection over facts, observations and context. Making it an aggregate would create a second source of truth. |
| `EvaluationInputSnapshot` | **Keep, and elevate to the architectural centrepiece** | Strongest of the proposed names. |
| `AssessmentAuthorityChain` | **Keep, rename `AppraisalAuthorityChain`** | "Appraisal" matches the ACR domain; "assessment" is the reusable-platform word and should stay in the platform layer if a platform layer is ever built. |
| `AuthorityAssignment` | **Keep** | |
| `AppraisalStage` | **Keep, but split** | `Stage` (enum: REPORTING, COUNTERSIGNING, CERTIFYING, APPROVING) and `StageInstance` (stage + attempt sequence), because returns produce repeat attempts that must all be preserved. |
| `AppraisalDecision` | **Rename `StageDecision`** | Emphasises that the decision belongs to a stage attempt, not to the case. |
| `DecisionLedger` | **Keep** | Accurate: append-only, ordered, non-destructive. |
| `ReviewerEligibilityPolicy` | **Keep** | |

Two concepts the brief did not propose and the domain requires:

- **`DisclosurePacket`** — because adverse-remark redaction (R-81, ACR instr. 3) is a domain decision with an audit trail, not a presentation concern.
- **`Correction` / supersession chains** — because ACR instr. 17/20/23 require an upper officer to *replace* a lower officer's comment while the original must remain in the record.

---

## C. Evidence & Context Architecture

### C.1 The scenario-explosion problem, stated precisely

The failure mode to avoid is a system in which someone eventually writes:

```
if (weatherSevere && attendanceOnTime) punctualityBonus += 1;
```

Once that line exists, DESCO owns an unbounded backlog: what about a transport strike? A road closure on one route only? An employee already on approved leave during the storm? Field staff whose duty station *is* the storm? Every new real-world situation becomes a code change, a release, a regression risk, and — worst of all — an undocumented change to an official appraisal rule.

The generalisable insight is that the explosion is not in the number of *situations*; it is in the number of *(situation × criterion × policy)* combinations. Attack it by refusing to let those three ever be entangled in one record.

### C.2 Three-layer separation

```
LAYER 1 — FACTS (what happened)
  RawFact        : typed, atomic, provenance-bearing, no judgement
  Observation    : human narrative, authored, no score
       │  neither knows which criterion it will serve
       ▼
LAYER 2 — CONTEXT (under what conditions)
  ContextFact    : org-level or unit-level condition with a validity interval
       │  recorded once, joined by (time ∩ org-unit ∩ employee assignment)
       ▼
LAYER 3 — INTERPRETATION (what it means here)
  EvidenceEligibilityPolicy  : is this admissible for this criterion at all?
  CriterionEvaluationPolicy  : how does it count, and how does context modulate it?
  BehaviouralAnchor          : what does a mark of 4 / 3 / 2 / 1 look like?
       │  all three are versioned configuration owned by DESCO
       ▼
  DerivedIndicator  →  EvidenceItem (derived)  →  EvaluationInputSnapshot
```

**The storm example resolved.** There is no storm rule anywhere in the code.

1. A `PresenceFact(employee, date, onTime)` is recorded by the attendance adapter. It knows nothing about weather.
2. A `ContextFact(type=SEVERE_WEATHER_ADVISORY, scope=DHAKA_NORTH_ZONE, validity=[date, date])` is recorded once by an authorised HR/administration user (or ingested from an official advisory). It knows nothing about any individual.
3. At evaluation time, the সময়ানুবর্তিতা `CriterionEvaluationPolicy` — a versioned, DESCO-approved configuration record — states something of the form: *attendance on days carrying an org-wide disruption context is counted with elevated significance weight w, capped at n days per cycle.*
4. The AI never invents this. The deterministic indicator computes it. The AI may *narrate* it in the pen picture, citing both the presence fact and the context fact.

Add a new situation type — a transport strike, a national mourning day, a substation emergency — and you add a `ContextFact` type and, if DESCO decides it should matter, one policy line. No code. No release. And there is a change-controlled record of exactly when the rule changed and who approved it, which is precisely what an appraisal grievance will one day demand.

### C.3 Evidence quality, not just evidence presence

Every derived `EvidenceItem` carries an `EvidenceQualityProfile`:

| Dimension | Meaning | Source |
|---|---|---|
| Provenance class | SYSTEM_INTEGRATED · SYSTEM_MANUAL · OFFICER_OBSERVED · SELF_REPORTED · DOCUMENT_ATTACHED | Structural |
| Verification state | UNVERIFIED · CORROBORATED · OFFICIALLY_FINALISED | Workflow |
| Corroboration count | Independent facts supporting the same claim | Computed |
| Recency | Distance from cycle end | Computed |
| Recording lag | `recordedAt − occurredAt` | Computed |
| Relevance | Policy-declared strength for this criterion | Policy |
| Disclosure state | For negative items: DISCLOSED / RESPONSE_WINDOW_OPEN / ADMISSIBLE | Workflow |

Two of these deserve emphasis because they are anti-manipulation controls rather than quality measures. **Recording lag** exposes the classic pattern of negative evidence being entered in bulk shortly before cycle close. **Disclosure state** enforces ACR instruction 11: a shortfall that was never shown to the employee is inadmissible, full stop, regardless of how true it is.

Self-reported evidence carries the lowest default reliability and — this is a policy parameter, not a hard rule — should have a bounded maximum influence on any criterion mark. Otherwise the employee self-input module becomes a volume game.

### C.4 Patterns, not incidents

"Isolated incident versus persistent behaviour" must never be an LLM judgement, because the LLM sees a bag of text and has no reliable sense of base rates. It is a deterministic computation over the `EvidenceTimeline` read model:

- occurrence count within the cycle and within rolling windows
- recurrence after a documented corrective conversation (a strong signal, and one that only exists because of the instr. 11 disclosure workflow)
- trend direction across quarters
- dispersion and consistency
- comparison to the employee's own prior cycles (available from cycle 2 onward)

The AI receives the *computed pattern summary* plus the specific cited items, never a raw dump of the year's records. This is also the main defence against context-window dilution and against the model latching onto whichever incident happened to be described most vividly.

### C.5 Contradictory and missing evidence

**Contradictory.** Do not let anything resolve a contradiction silently — not the AI, and not a scoring rule. Detect it (`EvidenceConflict` between, say, a supervisor observation of poor reliability and a finalised award for the same period), lower the confidence, surface both items side by side to the reporting officer, and require adjudication. The officer's adjudication is itself an `Observation` with reasons, and it enters the record.

**Missing.** `INSUFFICIENT_EVIDENCE` must be a first-class recommendation outcome, not a low score. This is a direct requirement of TOR §3.8(b) robustness testing, and it is also the honest engineering answer: a model that always produces a number will produce a number for an employee about whom nothing was recorded. The system's response should be to block AI recommendation for that criterion, require the officer to mark it manually with a written justification, and count the case in an evidence-coverage report that HRM can act on.

**Positive-only bias.** Expect the opposite failure too: officers who record achievements and never record shortfalls, producing a year of uniformly positive evidence. The coverage report should track negative-evidence rate per evaluator alongside positive, and treat a zero rate as a data-quality flag rather than as good news.

---

## D. Scoring Architecture

### D.1 Non-negotiable arithmetic constraints

Before any evaluation strategy is chosen, four constraints come straight off the form and cannot be traded away:

1. **The official mark is an integer on a 4-point or 5-point ordinal scale.** Internal computation may be continuous; the recommendation *surfaced to an officer* must be an integer plus, optionally, a boundary-proximity indicator ("close to 3"). The R&D handoff document's illustrative `"suggestedScore": 4.3` is correct for a generic platform and **wrong for DESCO**.
2. **The total is an unweighted sum.** 25 × 4 = 100; 20 × 5 = 100. There are no weights on the form. Any weighting alters the instrument and requires a DESCO change request (R-05).
3. **Band assignment is a pure function of the total.** Deterministic, testable, no model involvement.
4. **The two tiers are not linearly comparable.** Tier 1–11 ranges 25–100; tier 12–16 ranges 20–100. A mark of 3 is 75% of scale on one instrument and 60% on the other. Cross-tier aggregation must operate on totals and bands, never on raw criterion marks.

Constraint 2 has an important architectural consequence: **build the weighting capability, ship it neutral.** `CriterionWeight` exists in the instrument model, defaults to 1.0 uniformly, and is change-controlled. If DESCO later approves weighted evaluation, it is a configuration change with a revalidation trigger (R-71), not a re-architecture.

### D.2 Evaluation strategies per criterion

| Strategy | Definition | AI role | Example (Grade 1–11) |
|---|---|---|---|
| **OBJECTIVE** | Mark derived deterministically from `DerivedIndicator` values via a versioned mapping | **None in the number.** May narrate. | সময়ানুবর্তিতা from punctuality rate; বার্ষিক গোপনীয় অনুবেদন লিখন ও প্রতিস্বাক্ষরকরণে তৎপরতা from the system's own ACR submission timeliness |
| **HYBRID** | An objective indicator establishes a prior mark; qualitative evidence may adjust it within a bounded, policy-set deviation | Proposes an adjustment **within the cap**, with citations | সম্পাদিত কাজের পরিমাণ; নিরাপত্তা সচেতনতা; জনসাধারণের সাথে ব্যবহার |
| **QUALITATIVE** | No reliable objective indicator exists; judgement against behavioural anchors and cited evidence | Proposes a mark with justification and low prior confidence | ব্যক্তিত্ব; বিচার ও মাত্রাজ্ঞান; বুদ্ধিমত্তা |
| **DERIVED** | Computed from other criteria or indicators; no independent evidence collection | None | Reserved; not currently mapped to any ACR criterion |
| **COMPOSITE** | Internally decomposed into sub-dimensions for reasoning support only | Reasons over sub-dimensions; output is still one integer | কাজের মান decomposed into achievement / quality / consistency / impact |

Two cautions on COMPOSITE. First, the four dimensions from the R&D handoff (achievement 30 / quality 25 / consistency 20 / impact 25) are a *reasoning scaffold*, not a scoring mechanism — the ACR has no sub-dimensions, so composite decomposition must never change the official mark's arithmetic. Second, decomposition is the right place to spend AI reasoning tokens; the aggregation back to an integer should be deterministic.

**The bounded-deviation cap is the most important guardrail in this section.** For HYBRID criteria, policy sets a maximum distance between the deterministic prior and the AI-proposed mark (e.g. ±1 scale point). It prevents a persuasive narrative from overturning a hard indicator, it makes the AI's contribution auditable ("the indicator said 3, the AI proposed 4, here is why"), and it gives DESCO a single dial to tighten or loosen AI influence per criterion without touching code.

### D.3 How a raw fact becomes a mark

```
RawFact / Observation
   │
   ├─ EvidenceEligibilityPolicy(criterion, version)  ──► admissible? provenance ok?
   │                                                     disclosure precondition met?
   │                                                     lifecycle state finalised?
   ▼
EvidenceItem (derived, criterion-scoped, quality-profiled)
   │
   ├─ ContextFact join (time ∩ org-unit)
   ├─ DerivedIndicator computation (deterministic, versioned formula)
   ├─ Pattern computation (frequency, recurrence, trend, consistency)
   ▼
EvaluationInputSnapshot  ── content-addressed, immutable ──┐
   │                                                        │
   ├─ OBJECTIVE   → deterministic mapping ────────────┐     │
   ├─ HYBRID      → prior + capped AI adjustment ─────┤     │ every
   ├─ QUALITATIVE → AI vs anchors, citations required ┤     │ downstream
   ▼                                                  ▼     │ artefact
CriterionRecommendation[]  (integer | INSUFFICIENT_EVIDENCE)│ references
   │                        + confidence + evidenceStrength │ this
   │                        + justification + citations[]   │ snapshot id
   ▼                                                        │
Reporting Officer records the OFFICIAL mark ────────────────┘
   │  (may accept, modify, or reject the recommendation; reason captured)
   ▼
Total = Σ official marks    →    Band = f(total)    [both deterministic]
```

Note where the boundary sits: the AI produces a `CriterionRecommendation`; the *officer* produces the `CriterionMark`. These are separate records with separate lifecycles. At no point does an AI output flow into the official mark without a human write. That is R-27 enforced structurally rather than by convention.

### D.4 What the AI must not decide

Fixed list, enforced by type system and by service boundaries rather than by prompt instructions:

- the official criterion mark (only an officer writes it);
- the total or the band (deterministic);
- whether an evidence item is admissible (eligibility policy);
- whether the 3-month rule is satisfied (deterministic);
- the promotion-eligibility category (human-only; see M-14);
- anything involving health data (structurally unreachable);
- who the authority officers are.

### D.5 The applicability problem

Criteria 17 (তদারকি ও পরিচালনার সামর্থ্য), 21 (অধীনস্থদের প্রশিক্ষণদানে আগ্রহ ও দক্ষতা) and 24 (বার্ষিক গোপনীয় অনুবেদন লিখন ও প্রতিস্বাক্ষরকরণে তৎপরতা) presuppose that the appraisee supervises others and writes ACRs. A Grade 1–11 employee with no subordinates cannot meaningfully be scored on them — yet the form provides no N/A column and the total is out of 100.

In paper practice this is almost certainly absorbed by officers awarding a middling mark. Digitising it forces the question into the open, and there are only three honest answers:

- **(a) Score as-is** — preserve current practice exactly. Zero instrument change. Accepts that three criteria are noise for non-supervisory staff.
- **(b) N/A + pro-rata rescaling** — mark inapplicable criteria N/A and rescale the achieved total to 100. More defensible, but it **changes the instrument** and therefore requires a DESCO change request under R-05, and it makes totals across employees subtly non-comparable.
- **(c) N/A + fixed neutral mark** — a hidden version of (a) with extra steps. Not recommended.

Architecture supports all three via `ApplicabilityRule` + `NormalizationPolicy`. **Default must be (a)**, because R-01 says replicate without alteration. This is a policy decision (M-08), not a design choice, and it should be raised in Phase 1 rather than discovered in UAT.

---

## E. Appraisal Authority & Decision Workflow

### E.1 The structural fact that drives the model

The ACR form does not have one score. It has **up to four independently recorded assessments**:

| Stage | What is recorded | Granularity |
|---|---|---|
| Reporting Officer | 25 (or 20) criterion marks + arithmetic total + pen picture + recommendations | Per criterion |
| Countersigning Officer | Comment (if any) + **one holistic total** | Aggregate only |
| Certifying Officer (conditional) | Comment (if any) + **one holistic total** | Aggregate only |
| Approving Officer | Comment (if any) + **one holistic total** | Aggregate only |

An upper officer's total is explicitly described as being given *"সামগ্রিক মূল্যায়নের ভিত্তিতে"* — on the basis of overall assessment. It is their own judgement, informed by the lower officer's work (instr. 16/19/22), not an edit of it. It need not equal the reporting officer's arithmetic sum, and nothing on the form says it must.

Therefore: **`AppraisalCase` has no `score` field, and no stage ever writes to a field another stage wrote to.** The workflow is an append-only ledger of independent, attributable assessments. This is not a purity argument — it is form fidelity.

### E.2 The decision ledger

```
StageInstance(caseId, stage, attemptSeq, openedAt, assignedActor, status)
     │  1..n
     ▼
StageDecision  ── immutable, append-only, hash-chained ──
     actorId, authorityRole, decisionType, decidedAt
     criterionMarks[]          (REPORTING stage only)
     holisticTotal             (upper stages only)
     comments[]
     penPicture                (REPORTING stage only — per ACR p.5)
     recommendation            (REPORTING stage only — per ACR p.5)
     evaluationRunId           (which AI output was on screen)
     evidenceSnapshotId        (exactly what evidence was visible)
     instrumentVersion, policyVersionSet
     supersedes[]              (CommentSupersession references)
     reason                    (mandatory for MODIFY / RETURN / REJECT)
     previousDecisionHash
```

`decisionType ∈ { CONCUR, MODIFY, RETURN, REQUEST_CLARIFICATION, REJECT, APPROVE_FINAL }`.

- **CONCUR** — agrees; for upper stages still records their own total (the form requires it).
- **MODIFY** — records a differing holistic total and/or an alternative comment; reason mandatory.
- **RETURN** — sends the case back to a lower stage. Does not delete anything; opens a new `StageInstance` with `attemptSeq + 1`. Every attempt survives in the ledger.
- **REQUEST_CLARIFICATION** — a non-returning query, typically to the appraisee or to HRM, that pauses the stage clock.
- **REJECT** — only where DESCO policy permits; neither source document establishes a rejection right, so this must be confirmed (M-11) and is disabled by default.
- **APPROVE_FINAL** — terminal; freezes the case and triggers HRM transmission (instr. 24).

**Comment supersession (instr. 17/20/23).** When an upper officer decides a lower officer's specific comment is wrong and should be cancelled, the system records `CommentSupersession(targetCommentId, replacementText, supersedingActor, reason)`. The original comment is never deleted or edited. The rendered ACR shows the superseding comment in the upper officer's block, exactly as the paper form does, while the audit view shows both. Where the officer *fully* disagrees, they write under their own heading — a plain comment on their own decision, no supersession link.

### E.3 Final score resolution

**Neither the TOR nor the ACR states how the official final score is determined** when up to four totals exist. This is the highest-priority open question in the entire project (M-01), because it determines what appears on every dashboard, every report and every promotion file.

Candidate policies, all implementable, none decidable by the vendor:

| Policy | Description | Plausibility |
|---|---|---|
| `HIGHEST_AUTHORITY_TOTAL` | The approving officer's total is the official score | Most likely, matches bureaucratic norm |
| `LAST_RECORDED_TOTAL` | The total from the terminal stage actually reached | Handles cases where no certifying stage occurred |
| `REPORTING_TOTAL_WITH_ENDORSEMENT` | The reporting officer's sum stands unless explicitly overridden | Possible, but hard to reconcile with the form giving upper officers a total box |
| `AVERAGE` / weighted | Averaging the totals | Unlikely; no basis in the form |

Architecture: `FinalScoreResolutionPolicy` is versioned configuration, and the resolved final score is stored as a **computed, attributed result** (`resolvedFrom: stageDecisionId, policyVersion`) rather than as a bare number. If DESCO changes the policy later, historical cases keep their original resolution and the change is visible.

### E.4 Divergence, escalation and manipulation controls

The ACR expects reasoned disagreement (instr. 16–17). The TOR requires anomaly detection (R-65) and override monitoring (R-70). Together they justify:

- **`DivergenceRule`** — when `|upperTotal − reportingTotal|` exceeds a policy threshold, require an expanded written justification and optionally notify HRM. Note this is an *architectural capability*; whether DESCO wants a threshold, and what it is, is a policy decision (M-12).
- **Band-crossing divergence** — a divergence that moves the employee across a band boundary is materially more consequential than one that does not, and is worth flagging separately.
- **Segregation of duties** — the same actor cannot occupy two stages of one case; cannot appraise themselves; and mutual-appraisal pairs (A appraises B while B appraises A in the same cycle) should be detected and reported to HRM. None of these are stated in the source documents; all are standard control expectations and should be proposed to DESCO explicitly rather than implemented silently.
- **Evidence freeze at submission** — when the reporting officer submits, the `EvidenceSnapshot` is sealed. Evidence added afterwards is visible to upper officers as *post-submission additions*, clearly separated, and cannot retroactively alter what the reporting officer saw.
- **Late-entry detection** — high recording lag on negative observations near cycle close is flagged (§C.3).
- **Chain-change invalidation** — if HRM changes an authority assignment mid-case, decisions already taken by the removed officer remain in the ledger, and downstream stages are explicitly re-opened with a recorded reason. No silent reassignment.

### E.5 Stage state machine

```
        ┌──────────────────┐
        │ CYCLE_OPEN       │
        └────────┬─────────┘
                 ▼
        ┌──────────────────┐   employee attests bio-data (instr. 8–9)
        │ BIODATA_PENDING  │───────────────────────────────┐
        └────────┬─────────┘                               │
                 ▼                                          │
        ┌──────────────────┐  eligibility check (3-month,   │
        │ REPORTING        │  work-connection attestation)  │
        └───┬──────────┬───┘                                │
   RETURN ◄─┘          ▼ submit → EVIDENCE SNAPSHOT SEALED  │
        ┌──────────────────┐                                │
        │ COUNTERSIGNING   │──── RETURN ────────────────────┘
        └───┬──────────┬───┘
            │          ▼ (conditional — condition undefined, M-05)
            │  ┌──────────────────┐
            │  │ CERTIFYING       │──── RETURN ───┐
            │  └────────┬─────────┘               │
            ▼           ▼                          │
        ┌──────────────────┐                       │
        │ APPROVING        │──── RETURN ───────────┘
        └────────┬─────────┘
                 ▼ APPROVE_FINAL
        ┌──────────────────┐
        │ FINALISED        │ → HRM transmission (instr. 24), disclosure
        └──────────────────┘   packets computed, case frozen
```

Two edge states the source documents do not address and the design must anticipate: an officer who **transfers, retires or dies mid-cycle** before signing (requires a succession/delegation policy — M-13), and a case where **no officer is eligible** under the 3-month rule (M-04).

---

## F. Temporal Supervision Model

### F.1 Why this needs bitemporality

An appraisal is a legal-ish artefact that may be challenged years later. If a 2029 reorganisation retroactively rewrites who reported to whom in 2027, every 2027 appraisal becomes indefensible. So the organisation and authority context is stored **bitemporally**: `validFrom/validTo` (when the arrangement was in force in the world) and `recordedFrom/recordedTo` (when the system was told about it). Nothing else in the system needs bitemporality; this does.

### F.2 Entities

```
OrgUnit(version)          ── effective-dated; supports restructure, rename, merge
Position(version)         ── effective-dated; belongs to an OrgUnit version
EmploymentAssignment      ── employee ↔ position ↔ orgUnit, [validFrom, validTo)
                             carries payGrade, so grade history is queryable
SupervisionRelationship   ── employee ↔ supervisor, [validFrom, validTo),
                             type ∈ { SUBSTANTIVE, ACTING, IN_CHARGE, ADDITIONAL }
AuthorityAssignment       ── HRM-assigned officers per case (see B.2)
```

`SupervisionPeriod` is **derived**, not stored as truth: for a given (employee, officer, cycle) it is computed by interval intersection of the supervision relationships with the cycle window, minus policy-defined exclusions.

```
cycle window:        |════════════ 1 Jan ─────────────────── 31 Dec ═══════|
employee at Unit A:  |════════ Jan–Apr ════|
employee at Unit B:                        |═══════ May–Dec ═══════════════|
supervisor X (A):    |════════ Jan–Apr ════|                → 120 days
supervisor Y (B):                          |═══ May–Aug ═══|  → 123 days
supervisor Z (B, acting):                                  |═ Sep–Dec ═|  → 122 days
long leave:                       |══ Mar ══|                → exclusion?
```

### F.3 Reviewer eligibility as versioned policy

The 3-month rule sounds simple and is not. Every one of these is unspecified by both source documents:

| Question | Options | Source position |
|---|---|---|
| Is it 3 calendar months or 90 days? | Either | Unspecified |
| Contiguous or cumulative across separate stints? | Either | Unspecified |
| Does approved leave count toward the officer's supervision period? | Either | Unspecified |
| Does deputation / training absence count? | Either | Unspecified |
| Does ACTING or IN_CHARGE supervision count? | Either | Unspecified |
| Does the rule apply to countersigning and certifying officers? | Yes per TOR; ACR only states it for the reporting officer | **TOR extends beyond the ACR** |
| Which officer writes the report when several are eligible? | Longest tenure / most recent / HRM decides | Unspecified; ACR instr. 5 suggests HRM decides |
| What happens when nobody is eligible? | Skip cycle / HRM-nominated officer / abbreviated report | Unspecified |

`ReviewerEligibilityPolicy` therefore carries all of these as versioned parameters, and the eligibility evaluation result is **persisted with the assignment** — so the record shows not just that an officer was eligible but under which policy version and on what computed evidence.

Note the honest position on R-24: the TOR's extension of the 3-month rule to countersigning and certifying officers may well reflect actual DESCO practice, but it is not in the ACR text supplied. It should be confirmed rather than implemented as though it were established (M-03).

### F.4 Partial-period handling — capability versus policy

**Architectural capability (build):** `PartialPeriodAssessment` — a reporting-stage decision scoped to a sub-period, with its own evidence snapshot and its own criterion marks; plus `PartialPeriodAggregationPolicy` with strategies `SOLE_LONGEST_TENURE`, `SEPARATE_REPORTS`, `DAY_WEIGHTED_AGGREGATE`.

**DESCO policy (do not invent):** which strategy applies, and whether multiple partial reports are even permissible given that the ACR is a single annual form per employee. The form's page 3 does say *"…থেকে …পর্যন্ত কালের জন্য বার্ষিক অনুবেদন"* — for the period from X to Y — which suggests partial periods are contemplated. That is suggestive, not conclusive.

**Default until confirmed:** `SOLE_LONGEST_TENURE` with a single report, because it is the minimal-change reading of a single-form-per-year process. Ship it configurable, flag it in the Inception Report, and do not let it quietly harden into an undocumented rule.

### F.5 Mid-cycle grade change

If an employee is promoted from Grade 12 to Grade 11 during the cycle, the applicable instrument changes from the 20-criterion/5-point form to the 25-criterion/4-point form. Candidate policies: grade held at cycle end; grade held for the majority of the cycle; grade at cycle start; two partial reports on two instruments. All are implementable; none is stated. The TOR's own integration list includes "Promotion Effect on Personal Information", which shows DESCO is aware of promotions moving through the system but says nothing about instrument selection. This is M-09 and it will be hit in the very first cycle.

---

## G. AI/ML Architecture

### G.1 Decomposition — the TOR's "AI" is seven different problems

The TOR uses "AI" as a single word for capabilities with almost nothing in common. Treating them as one system is the fastest route to a fragile, unexplainable deliverable. Decomposed:

| # | Capability | TOR ref | Correct problem class | Recommended approach for the pilot |
|---|---|---|---|---|
| 1 | Recommended criterion marks | §1, §3.2.2.1 | Ordinal classification against a rubric | Deterministic for OBJECTIVE; LLM-with-anchors + structured output for QUALITATIVE/HYBRID, capped |
| 2 | Draft pen picture | §1, §3.2.2.1 | Constrained natural-language generation | LLM, generated **from structured evaluation output only**, with mandatory citations |
| 3 | Consistency checks | §3.2.2.1, §3.2.3.3 | Rule evaluation | Deterministic rules. **Not** a model. |
| 4 | Anomaly detection in ratings | §3.2.2.1, §3.2.2.2 | Statistical outlier / rater-effect analysis | Mixed-effects or many-facet Rasch rater models; robust z-scores; isolation forest for multivariate cases |
| 5 | Bias & fairness analytics | §3.2.2.2 | Statistical hypothesis testing + audit | Rater-effect analysis + counterfactual probes; see §I.5 for what is and is not applicable |
| 6 | Predictive analytics (attrition, future performance, training need) | §3.2.2.1 | Supervised learning / survival analysis | **Not deliverable in the pilot.** Provision the pipeline; do not ship a model. See G.4. |
| 7 | Explainability | §3.2.2.2, §6.2 | Mostly *construction*, not post-hoc XAI | Deterministic components explain themselves; LLM emits structured rationale + citations. SHAP only where a real ML model exists. |

The single most useful reframing here: **most of what the TOR calls AI is arithmetic and statistics.** The genuinely generative part is narrow — one recommendation task and one drafting task. Concentrating LLM usage there and refusing it everywhere else is what makes the system explainable, testable and defensible.

### G.2 Criterion mark recommendation

The task is: given an anchored rubric, a bounded set of admissible, quality-profiled evidence, computed patterns, and organisational context, propose an integer on a 4- or 5-point scale with a justification and citations.

**Why not supervised ML at pilot start:** there is no labelled corpus. Historical ACRs are paper, confidential, and — even if digitised — carry marks without the evidence that produced them, which makes them useless as training pairs. Cold start is absolute.

**Why an LLM is nonetheless defensible here:** the task is anchored comparison over short, curated text, not open-ended reasoning. With behavioural anchors, a bounded evidence set, structured output and a deviation cap, the model's discretion is narrow and every output is checkable against its own citations.

**Design constraints that make it safe:**
- Input is the `EvaluationInputSnapshot` only — never a live database query, never health data, never demographic fields.
- One criterion per call. Cross-criterion reasoning invites halo effects, which is precisely what §3.2.2.2 asks the system to detect in humans.
- Structured output, schema-validated. Reject and retry on schema failure; never regex-parse prose.
- Mandatory citations: every justification sentence maps to evidence identifiers present in the snapshot. Post-generation, verify programmatically that every cited identifier exists. Uncited claims are a hard validation failure, not a warning.
- `INSUFFICIENT_EVIDENCE` is always a permitted output.
- Temperature at or near zero, fixed seed where the runtime allows, for reproducibility.

**Path to classical ML (year 2+):** once several thousand `(snapshot → officer's final mark)` pairs accumulate, HYBRID criteria with mostly tabular features become good candidates for ordinal logistic regression or gradient-boosted ordinal models — which are cheaper, faster, fully explainable via coefficients or SHAP, and far easier to revalidate under §3.8(c). This is a realistic and attractive future state and the architecture should not foreclose it: keep features materialised, keep snapshots, keep labels.

### G.3 Pen picture generation

Generate **after** structured evaluation, never in parallel with it, and never from raw evidence text. Input: final or proposed criterion marks, band, computed patterns, top-cited evidence items, and the officer's own notes. Output: a draft with per-sentence evidence citations.

Risks and controls:

| Risk | Control |
|---|---|
| Hallucinated events | Citation-constrained generation + automated citation verification + officer sign-off. A pen picture is never auto-filed. |
| Bangla fluency and register failure | The ACR pen picture is written in formal administrative Bangla. This is a genuine capability question for any candidate model and must be benchmarked, not assumed (§P.3). Fallback: template-assisted drafting with AI-suggested phrases. |
| Inconsistency with the marks | Automated check: sentiment/valence of the narrative against the band; flag mismatches (a "চলতি মানের নিচে" total with a glowing pen picture). |
| Leaking adverse detail into a disclosable artefact | Pen picture is subject to the same `DisclosurePolicy` as everything else. |
| Homogenised, templated prose across an entire department | Track n-gram overlap across generated pen pictures per evaluator; high overlap is a quality flag and, incidentally, an early warning of rubber-stamping. |

One clarification is needed: the ACR gives the pen picture (লেখচিত্র) to the reporting officer alone. The TOR implies AI-drafted pen pictures for review by all four authorities. Upper officers write *comments*, not pen pictures. The system should draft the pen picture for the reporting officer and, at most, offer comment-drafting assistance to upper officers — subject to DESCO confirmation (M-15).

### G.4 Predictive analytics — the honest assessment

TOR §3.2.2.1 requires "predictive analytics for attrition risk, training needs, and future performance". In a **pilot covering a single appraisal cycle**, this is not deliverable as a validated model, for reasons that are statistical rather than technical:

- **Attrition prediction** needs labelled separation events over multiple years, with censoring handled properly (it is a survival-analysis problem, not a classification one). One cycle provides no outcome labels at all.
- **Future performance prediction** needs at least two prior cycles per employee to establish any autocorrelation. At pilot Go-Live there are zero digital prior cycles.
- **Training-need identification** is the one tractable member of the group, because it can be done descriptively: low marks on criteria with mapped training programmes, cross-referenced against training records. That is a rules-and-reporting feature, not a predictive model, and it should be delivered as such.

There is also a governance problem independent of the statistics. An attrition-risk score attached to a named employee inside a performance system can influence promotion, posting and development decisions; it is a prediction, not evidence, and the ACR framework has no place for it. Feeding it back into appraisal would be both circular and unfair.

**Recommendation:** deliver descriptive and trend analytics in the pilot; architecturally provision the predictive pipeline (feature materialisation, model registry, monitoring) so it is a data problem and not a rebuild; and raise §3.2.2.1 with DESCO as a scope/timeline conflict requiring either deferral to a post-pilot phase or explicit acknowledgement that pilot-phase predictive output is illustrative and non-operational. **Do not silently ship an unvalidated attrition model to satisfy a checklist.**

### G.5 Anomaly and rater-effect detection

Purely statistical, run as scheduled batch jobs, no LLM:

| Effect | Detection |
|---|---|
| Leniency / severity | Evaluator mean deviation from the grand mean, adjusted for the composition of their appraisee pool (grade, unit, tenure) |
| Central tendency | Variance compression toward the scale midpoint |
| Range restriction | Within-evaluator standard deviation across criteria and across appraisees |
| Halo | Inter-criterion correlation within an evaluator, compared to the population correlation structure |
| Recency | Correlation between marks and the temporal distribution of the cited evidence |
| Score inflation over cycles | Year-over-year band distribution drift per evaluator and per unit |
| Evidence–mark mismatch | High marks with thin or negative cited evidence; low marks with strong positive evidence |
| Post-hoc justification | Evidence recorded after the mark was provisionally entered |

The principled model for separating true performance from rater harshness is a **many-facet Rasch model** or a mixed-effects model with evaluator and appraisee random effects. Both require adequate sample size and crossing (evaluators sharing appraisees, or appraisees sharing evaluators) — in a strictly hierarchical org this crossing may be sparse, which limits identifiability. This is a real R&D question (§P.6), not a solved one, and the pilot should start with simpler robust z-score and distributional methods while the data structure is assessed.

**Presentation matters as much as detection.** A per-evaluator bias score (required by §3.2.2.2) is a sensitive personnel signal about the *evaluator*. It should be visible to HRM and audit, delivered with confidence intervals and sample sizes, and never presented as a verdict. A leniency flag on an officer with four appraisees is noise.

### G.6 Fine-tuning — when it is and is not justified

**Not justified at pilot.** Reasons, in order of weight:

1. No training data. Fine-tuning on nothing is not possible; fine-tuning on a few hundred examples produces overfitting dressed as domain adaptation.
2. No evaluation set. Without a held-out, human-approved benchmark you cannot demonstrate that fine-tuning improved anything — and TOR §3.8(b) requires exactly that demonstration.
3. Revalidation burden. §3.8(c) triggers revalidation on rubric change; a fine-tuned model bakes the rubric into weights, so every rubric tweak invalidates the model. A prompt-and-anchor approach keeps the rubric as data, where it belongs.
4. On-prem GPU cost for training, unbudgeted in the TOR.
5. IP: TOR §9 vests all AI models in DESCO. Fine-tuned derivatives of open-weight models carry licence terms that must be checked against that clause before any weights are touched (see ADR-14).

**Justified later, and for a narrower purpose than usually imagined.** After several thousand human-approved `(evidence → final mark → justification)` records exist, a LoRA/QLoRA adaptation of an open-weight model becomes reasonable — primarily to improve **Bangla administrative register, structured-output reliability and format adherence**, and secondarily to calibrate to DESCO's mark distribution. It is not a route to "teaching the model DESCO's judgement"; that framing overstates what fine-tuning does and understates the human authority the TOR insists on.

### G.7 On-premise inference — the largest unpriced risk

TOR §5.1 mandates on-premise deployment. TOR §5.1 also names Python/TensorFlow. Neither the TOR nor the payment schedule mentions GPU infrastructure, who supplies it, or what capacity is required. The options:

| Option | Viability | Notes |
|---|---|---|
| Self-hosted open-weight model (Qwen / Llama / Mistral class) on DESCO GPUs | **Recommended, conditional** | Satisfies on-prem and confidentiality. Requires GPU procurement decision in Phase 1. Serving via vLLM/TGI, not TensorFlow. |
| CPU-only small model | Not viable for Bangla narrative quality | Might suffice for structured classification; will not produce acceptable pen pictures |
| External hosted API (Gemini, Claude, GPT) | **Likely non-compliant** | ACR content is গোপনীয়; sending it off-premise conflicts with §5.1 and with GoB data-protection expectations under §3.2.2.2 |
| Hybrid: on-prem for production, hosted API for development only, on synthetic data | Viable and useful | Requires an explicit rule that no real ACR content leaves the premises |

**This must be resolved in Phase 1.** A pilot that reaches Month 5 without GPU capacity has no AI engine, and no amount of architecture recovers that. It belongs in the Inception Report as a named dependency on DESCO (M-19).

### G.8 Model lifecycle and abstraction

```
AiEvaluationService  (domain — knows nothing about providers)
        │
        ▼
AiGateway  ── provider abstraction, structured-output contract,
              schema validation, retry, timeout, circuit-break
        │
   ┌────┴──────────────┬──────────────────┐
   ▼                   ▼                  ▼
Self-hosted        Hosted API        Deterministic
open-weight        (dev/synthetic     stub (test /
(vLLM/TGI)          only)              fallback)
```

Every `EvaluationRun` records: model name, version, weights hash, quantisation, provider, prompt template version, anchor version, rubric version, eligibility policy version, scoring policy version, temperature, seed. Rollback means pinning a previous version set and re-running against retained snapshots.

**Revalidation dependency graph (R-71).** A `ModelValidationCertificate` is issued against a specific `(model version, prompt version, anchor version, rubric version)` tuple. Changing any element invalidates the certificate, and an invalid certificate blocks deployment to production. This turns §3.8(c) from a promise into a mechanism.

The R&D handoff's direction — Spring AI as the abstraction layer — is sound for the Java stack and is retained (ADR-11), with the caveat that a Python inference service sits behind it rather than inside it.

---

## H. Data & Integration Architecture

### H.1 Integration posture

TOR §1 is unambiguous: during the pilot the system **only retrieves**; it must not push, write, modify or update data in any existing DESCO system. Architecturally this is a gift — read-only integration is dramatically simpler — but it must be enforced rather than intended. Recommendation: integration credentials are provisioned read-only at the source system, adapters expose no write methods, and this is stated in the Information Security & Compliance Report (§6.1) as a verified control rather than a design claim.

Post-pilot HRMS write-back (pushing finalised APR data) is anticipated by TOR §1 and should be provisioned as an outbound port with no implementation, so that enabling it is a delivery, not a redesign.

### H.2 Adapter model

```
Source system  ──►  IntegrationAdapter (versioned)  ──►  RawFactRecord
                       │
                       └─ provenance: sourceSystem, sourceRecordId, adapterVersion,
                          fetchedAt, sourceAsOf, payloadHash, credentialIdentity
```

Every retrieved record carries provenance. `payloadHash` supports idempotent re-fetch and change detection. `sourceAsOf` distinguishes "the source's view of the world" from "when we asked", which matters when a disciplinary case is finalised retroactively.

Where no API exists, the same `RawFactRecord` shape is produced by manual entry with `provenanceClass = SYSTEM_MANUAL`, `enteredBy`, and optionally a verification workflow. **The downstream evaluation code must not know or care which path a fact arrived by** — only the eligibility policy consults provenance class, and it does so explicitly.

### H.3 Corrections and staleness

Facts are immutable. A correction creates a new version and marks the prior version superseded, retaining both. Consequence: any `EvaluationInputSnapshot` referencing a superseded fact version becomes **stale**, and any `EvaluationRun` or `StageDecision` referencing that snapshot is flagged. The system does not silently re-run; it surfaces "the evidence underlying this decision has since been corrected" to HRM and to the relevant stage, and lets policy decide whether the case reopens. This is one of the more likely real-world sequences (a disciplinary finding overturned on appeal after the ACR was written) and it deserves an explicit path rather than an exception.

### H.4 Snapshots as the backbone

To restate, because it carries the most weight of anything in this report: **every AI recommendation and every human decision references a content-addressed, immutable snapshot of exactly what was visible at that moment.** Without it:

- override-rate monitoring (R-70) is uninterpretable;
- accuracy benchmarking (R-68) is unreproducible;
- explainability (R-67) degrades to a narrative claim;
- model rollback (R-72) cannot be evaluated against past cases;
- a grievance three years later cannot be answered.

With it, all five are mechanical. Snapshots will grow; budget for retention, compression and a cold-storage tier from the outset rather than discovering the growth curve in year two.

### H.5 Document and attachment handling

Evidence uploads (TOR §3.2.3.1, §3.4) require: virus scanning at ingest, content-hash addressing, an immutable object store, access control inherited from the case's disclosure policy, and size/type limits. Attachments are referenced by hash in snapshots, never copied into them. OCR/text extraction of attachments for AI consumption is a **separate, explicit, policy-gated step** — a scanned document dropped into a prompt is an uncontrolled data path and, for confidential HR documents, a genuine leakage risk.

### H.6 Reference data and the bilingual requirement

Every domain label — criteria, bands, decision types, categories, notification templates, AI-facing anchor text — is bilingual reference data (R-85). Two non-obvious consequences:

1. **Anchors must exist in both languages and must mean the same thing.** A Bangla anchor and its English translation that diverge in strictness will produce different AI recommendations depending on prompt language. Anchor translation is a validation item, not a localisation chore.
2. **Prompt language is a versioned configuration parameter**, and any change to it invalidates the model validation certificate (§G.8). Whether the AI reasons in Bangla, in English, or in English over Bangla evidence is an empirical question to be settled by benchmark (§P.3), not by preference.

---

## I. Security, Privacy, Fairness & Governance Architecture

### I.1 Authorisation: RBAC is necessary and insufficient

TOR §3.7(a) specifies RBAC with granular permissions. Role alone cannot express the actual rule, which is relational and temporal: *this officer may see this case because they are the assigned countersigning officer for this case in this cycle, and only while the case is at or past their stage.*

Recommended model: **RBAC for coarse capability, ABAC/policy-based for every case-scoped decision.** An authorisation request evaluates `(subject, action, resource, case, stage, effectiveDate, authorityChain)`. Consequences worth stating:

- A department head is *not* automatically entitled to see appraisals in their department — only the cases where they occupy an assigned authority role. The ACR's confidentiality model is chain-based, not hierarchy-based.
- An officer's access to a case does not begin before their stage opens. A countersigning officer browsing the reporting officer's draft before submission undermines the independence the form assumes.
- HRM has broad but audited access (instr. 5, 24), and every HRM access to a case body should be logged as an access event, not merely permitted.

### I.2 Disclosure and adverse remarks

`DisclosurePolicy` is a domain service producing a persisted `DisclosurePacket`. The default disclosure to an appraisee, under ACR instr. 3 and 4 and the গোপনীয় classification, is **nothing** — with three exceptions:

1. their own bio-data submission and self-input;
2. shortfalls disclosed under instruction 11 during the cycle, with the response opportunity;
3. the **specific adverse excerpt** where an adverse remark exists and disclosure is ordered.

Redaction is computed server-side and the packet is what the API returns. The client never receives the full record and hides part of it — that pattern is a breach waiting for a browser dev-tools session.

**This collides directly with TOR §3.6(d)**, "Employee Self-Service Dashboard — access to personal KPIs, ratings, comments". Ratings and comments are exactly what the ACR keeps confidential. See N-06; this must be resolved before UAT, and the resolution is a DESCO policy decision with legal implications, not a UI preference.

### I.3 Sensitive data segregation

Three categories require structural, not procedural, separation:

**Health data (ACR p.2).** Separate schema, separate encryption key, separate database credentials held only by the health module. The evidence eligibility layer has no code path and no credential to reach it. This is deliberately stronger than a configuration flag: *the AI service must be structurally incapable of receiving health data*, so that a prompt-construction bug cannot become a medical-data disclosure. Note that the TOR never explicitly prohibits health data from influencing scoring (R-48) — the prohibition should be stated in the SRS and confirmed by DESCO (M-16).

**Demographic and family data (ACR p.3: marital status, number of children).** Captured on the form, therefore stored. **Never eligible evidence, never a model feature, never present in a prompt.** If these fields reach an LLM prompt, the system acquires a live discrimination pathway and no amount of downstream fairness testing will fully characterise it. Enforce by an allow-list on prompt construction — the prompt builder assembles from a whitelisted projection, never from a general employee record.

**AI prompt and response logs.** Required for audit and validation (§3.8), and they contain full confidential appraisal content. They inherit the ACR's classification, encryption, access control and retention policy. A common and serious mistake is to treat model logs as ordinary application telemetry and ship them to a general observability stack.

### I.4 Encryption

TOR §5.2 requires AES-256 at rest for Name, NID and Birth Date (§3.2.2.2 says Birth Certificate — see N-09). Practical position:

- **NID, birth date, birth-certificate number:** field-level AES-256 with envelope encryption and a proper key hierarchy. Straightforward.
- **Name:** encrypting names at rest breaks search, sort, pagination, reporting, and any join on name. Options: deterministic encryption (weakens security, enables equality search), a blind index / searchable-encryption scheme (adds complexity), or negotiating the requirement down to database-level TDE plus strict access control for the name field. **Recommendation: raise it as a clarification (N-09) rather than silently implementing something that will not survive UAT performance testing.**
- Transport: TLS 1.3 preferred, 1.2 as the floor per §5.2.
- Full-disk/TDE for the whole database as a baseline in addition to field-level encryption.

### I.5 Fairness — what applies and what does not

The TOR (§3.2.2.2) names demographic parity, disparate impact and equal opportunity. These are not interchangeable, and two of the three are problematic here. Taking them seriously rather than implementing them decoratively:

**Demographic parity** (equal score distributions across protected groups) presumes that true performance is identically distributed across groups within each comparison set. In an employee-appraisal context that presumption is unjustified, and *enforcing* parity would require adjusting individual marks by group membership — which contradicts the TOR's own evidence-based principle and is very likely unlawful. **Use as a monitoring signal that triggers human investigation. Never as a constraint, never as an auto-correction, never as a target.**

**Disparate impact** (e.g. the four-fifths rule) is more defensible, but only when applied to *consequential outcomes* — band distribution, promotion-eligibility recommendation rates — and only with proper stratification by grade, job family and tenure. Unstratified, it will fire constantly for reasons that have nothing to do with bias (an all-male field-operations unit will differ from a mixed head-office unit for occupational reasons).

**Equal opportunity / equalised odds** require ground-truth labels of true performance. **No such label exists.** The officer's final mark is not ground truth — it is the very thing under audit. This should be stated plainly to DESCO: the metric cannot be computed as defined, and any dashboard claiming to show it would be showing something else.

**The additional problem nobody has raised yet:** all three metrics require protected attributes. AIPMS may hold sex; it almost certainly does not hold religion or ethnicity, and it should not infer them from names or NID. **Collecting protected attributes purely to run fairness tests is itself a policy and legal decision** (M-17) with its own risks. There is a real tension here — you cannot measure disparity across attributes you deliberately do not hold — and it should be surfaced to DESCO rather than resolved by a developer.

**What is well-founded, and should be the core of the fairness programme:**

| Method | Why it works here |
|---|---|
| **Rater-effect analysis** (§G.5) | Needs no protected attributes. Directly targets the unfairness that actually dominates appraisal systems: inconsistent evaluators. |
| **Evidence-grounding audit** | Measures whether marks are supported by cited evidence. A mark unsupported by evidence is the operational definition of arbitrary. |
| **AI–human divergence analysis** | Where the AI and officers systematically disagree, stratified by unit and grade, is diagnostically rich regardless of protected attributes. |
| **Counterfactual perturbation probes** | **The strongest concrete recommendation in this section.** Offline, on synthetic or de-identified cases, swap names (including gender-typical and religion-typical names), pronouns and unit labels while holding evidence identical, and measure recommendation drift. Any non-zero drift is direct evidence of model bias — and it requires **no production collection of protected attributes at all.** Run it as a gated pre-deployment test and periodically thereafter. |
| **Small-cell suppression** | Prevents fairness dashboards from becoming a re-identification vector in small units. |

### I.6 Governance artefacts

- **`ModelValidationCertificate`** — gates deployment; invalidated by version changes (§G.8).
- **`PolicyChangeRecord`** — every change to eligibility, scoring, evaluation, disclosure or resolution policy carries an approver, an effective date and a rationale. Policies are effective-dated so historical cases resolve under the policy that was in force.
- **Immutable audit log** — append-only, hash-chained, covering authentication, authorisation decisions (including denials), evidence creation and correction, snapshot sealing, AI runs, stage decisions, disclosure packet generation, policy changes, exports and all HRM access to case bodies.
- **ISO/IEC 27001** — the TOR alternates between "compliance with" (§5.2) and "alignment with" (§6.1). A vendor can implement aligned controls and document them; it cannot deliver DESCO a certification. This should be clarified in the contract rather than in the Compliance Report (N-10).

### I.7 Multi-tenancy — a caution

The R&D handoff frames a reusable platform across DESCO, teachers and students. The **DESCO pilot is single-tenant** and should be built that way. The prudent middle path: keep tenancy-relevant boundaries clean (no cross-case global state, tenant-scopable identifiers, policy resolution already parameterised) so that a future multi-tenant version is a refactor rather than a rewrite — but build **zero** tenant provisioning, tenant administration or tenant isolation features in the pilot. Speculative multi-tenancy in a six-month on-prem government pilot is a schedule risk with no pilot-phase payoff, and TOR §9 vests the IP in DESCO regardless.

---

## J. Deployment Architecture Options

### J.1 First: analysing the TOR's technology prescriptions

TOR §5.1 is a bulleted list under "Technical Requirements". TOR §3.1 describes microservices under "core architectural principles". Neither is in a contract clause that says "the vendor shall not deviate", but both are TOR text, and TOR text is what the evaluation committee reads. The correct posture is neither blind compliance nor silent deviation: **comply where compliance costs nothing, and where it does cost something, record the deviation and its rationale in the Inception Report for DESCO's written acceptance in Phase 1.**

| Prescription | Contractual? | Better alternative? | Deviation needs approval? | Position |
|---|---|---|---|---|
| Java Spring Boot backend | Stated as a requirement | No — it is a genuinely good fit for on-prem enterprise workflow systems, and it matches the R&D handoff's own direction | Yes | **Comply.** |
| React frontend | Stated | No | Yes | **Comply.** |
| Oracle **or** PostgreSQL | Stated as a choice | PostgreSQL: cost, JSONB for evidence payloads, pgvector optionality, on-prem friendliness. Oracle if DESCO ICT standardises on it for support reasons | No — the TOR offers both | **Recommend PostgreSQL; defer to DESCO ICT standards (M-20).** Keep persistence adapters isolated either way. |
| REST APIs | Stated | No | Yes | **Comply.** |
| On-premise (cloud flexible) | Stated, and reinforced by confidentiality | No | Yes, and unlikely to be granted | **Comply.** Drives §G.7. |
| **Python + TensorFlow** for AI/ML | Stated | **Yes.** Python: comply. TensorFlow: for LLM inference the ecosystem is vLLM/TGI/PyTorch; for the statistical layer it is statsmodels/scikit-learn. TensorFlow is not the natural tool for either workload described | Yes — flag it | **Comply with Python; request that "TensorFlow" be read as "a Python ML stack appropriate to the workload", documented in the Inception Report (N-11).** Do not simply ignore a named technology in a government TOR. |
| **Microservices** | Stated as a principle, with stated goals: flexibility, independent module updates, targeted scaling | **Yes, in part** — see below | Yes — flag it | **Propose the hybrid (Option 3) as satisfying the stated goals, with written acknowledgement.** |

The microservices clause deserves careful reading. The TOR does not ask for microservices as an end; it says the system "will be built using a micro-services architecture, **which allows for** greater flexibility, independent module updates, and the ability to scale specific functionalities". The stated purposes are flexibility, independent updates and targeted scaling. Those are the requirements. Microservices is the TOR's proposed means to them, and a hybrid meets all three for the components that actually differ in scaling profile — which is the AI plane, not the appraisal workflow.

### J.2 The three options

#### Option 1 — Modular monolith + embedded AI calls

Single Spring Boot deployable with strong internal module boundaries; AI accessed as an outbound HTTP call to a provider.

| | |
|---|---|
| **Benefits** | Fastest to build and deploy. One transaction boundary — and this system has genuinely transactional invariants (seal snapshot + record decision + generate disclosure packet). Trivial on-prem footprint. Easiest to secure, back up, and hand over. Best fit for a 6-month window. |
| **Risks** | AI workload (GPU, long latency, Python runtime) does not belong inside a Java request thread. Independent model versioning and rollback (R-72) become awkward. Data-eligibility enforcement is a code convention rather than a network boundary. Scaling the AI plane means scaling everything. |
| **Operational complexity** | Lowest. One artefact, one runbook. |
| **TOR compliance** | Weak against §3.1 as literally written. |
| **Pilot suitability** | High. |
| **Long-term** | Adequate but constrains the AI roadmap. |

#### Option 2 — Full microservices per TOR §3.1

Separate services for identity, organisation, instrument, evidence, evaluation, workflow, disclosure, analytics, notification, mobile BFF, integration, each independently deployed.

| | |
|---|---|
| **Benefits** | Literal TOR compliance. Independent scaling and deployment of every module. Clean team parallelisation if the team were large. |
| **Risks** | **Severe for this project.** The core invariants are cross-cutting: a stage decision must atomically seal a snapshot, write to the ledger and recompute disclosure. Distributing that means sagas, compensations and eventual consistency in a system whose central promise is auditability — the worst possible domain in which to introduce "the audit log is eventually consistent". On-prem service mesh, distributed tracing, per-service secrets and certificate rotation all become DESCO ICT's problem at handover. A ten-role team building twelve services in five months will spend its time on infrastructure, not on the appraisal domain. |
| **Operational complexity** | Highest, and it is transferred to DESCO at handover (§7.3) with 12 days of knowledge transfer. |
| **TOR compliance** | Full. |
| **Pilot suitability** | **Low. This is the single most likely cause of schedule failure.** |
| **Long-term** | Good only if DESCO ICT has, or will acquire, a microservices operations capability. That is a DESCO question, not a vendor assumption. |

#### Option 3 — Hybrid: modular core + separated AI/analytics plane (**recommended**)

```
┌───────────────────────────────────────────────────────────┐
│  React SPA (bilingual)          Mobile app (input module)  │
└──────────────────────┬─────────────────────┬───────────────┘
                       ▼                     ▼
              ┌──────────────────────────────────┐
              │  API Gateway / BFF               │  SSO, 2FA, rate limit
              └────────────────┬─────────────────┘
                               ▼
   ┌────────────────────────────────────────────────────────┐
   │  APPRAISAL CORE  (Spring Boot, modular monolith)        │
   │  ┌────────────┬────────────┬────────────┬────────────┐  │
   │  │ org &      │ instrument │ evidence & │ workflow & │  │
   │  │ authority  │ & policy   │ context    │ ledger     │  │
   │  ├────────────┼────────────┼────────────┼────────────┤  │
   │  │ evaluation │ disclosure │ integration│ audit      │  │
   │  │ orchestr.  │            │ adapters   │            │  │
   │  └────────────┴────────────┴────────────┴────────────┘  │
   │            ONE transaction boundary for invariants       │
   └───────┬───────────────────────────┬─────────────────────┘
           │  EvaluationInputSnapshot  │  materialised features
           │  (eligibility-filtered,   │
           │   whitelisted projection) │
           ▼                           ▼
   ┌──────────────────┐      ┌──────────────────────────┐
   │ AI INFERENCE     │      │ ANALYTICS / ML BATCH     │
   │ SERVICE (Python) │      │ SERVICE (Python)         │
   │ • LLM serving    │      │ • rater-effect models    │
   │ • structured out │      │ • anomaly detection      │
   │ • citation check │      │ • fairness probes        │
   │ • GPU-bound      │      │ • trend/descriptive      │
   └──────────────────┘      └──────────────────────────┘
           │                           │
           └─────────┬─────────────────┘
                     ▼
   ┌──────────────────────────────────────────────────────┐
   │ PostgreSQL (or Oracle)   │  HEALTH SCHEMA — separate  │
   │ appraisal, evidence,     │  credentials, separate key,│
   │ ledger, snapshots, audit │  unreachable from AI plane │
   └──────────────────────────────────────────────────────┘
   Object store (attachments, content-addressed, scanned)
```

| | |
|---|---|
| **Benefits** | Keeps the transactional core transactional, where auditability demands it. Separates the two components that genuinely differ — GPU-bound synchronous inference and long-running batch analytics — by runtime, language, scaling profile and failure mode. Makes the evidence-eligibility boundary a **network boundary**, which is the strongest available enforcement of §I.3. Enables independent AI model versioning and rollback (R-71, R-72) without redeploying the appraisal system. Modest, transferable operational footprint: three deployables plus a database. |
| **Risks** | Inference service availability must be handled gracefully — the appraisal workflow must remain fully usable with AI unavailable (this is a feature, not a fallback: the ACR process worked on paper). Contract between core and AI plane must be versioned. Two runtimes to operate. |
| **Operational complexity** | Moderate, and realistically transferable in the 12-day handover window. |
| **TOR compliance** | Substantially satisfies §3.1's stated goals; requires a documented interpretation note accepted in Phase 1. |
| **Pilot suitability** | **High.** |
| **Long-term** | **Best of the three.** Individual core modules can be extracted into services later if load or team structure warrants — the module boundaries are already drawn. |

### J.3 Why the boundary falls where it does

The split is principled, not fashionable. The AI plane is separated because it differs on **every** axis that justifies a service boundary: language runtime (Python vs Java), hardware (GPU vs CPU), latency profile (seconds vs milliseconds), failure semantics (degradable vs not), release cadence (model versions vs application versions), and — most importantly — **security posture**, since a separate service with a separate credential and a whitelisted input contract is the enforcement mechanism for evidence eligibility and health-data segregation.

Conversely, splitting the appraisal core would place a network boundary in the middle of invariants that must hold atomically. That is a boundary drawn against the domain rather than along it.

---

## K. Recommended Architecture

### K.1 The recommendation in one page

**Deployment:** Option 3 — modular monolith appraisal core (Java/Spring Boot), plus a separated Python AI inference service and a Python analytics/batch service, on PostgreSQL, deployed on-premise, with a segregated health schema. Documented in the Inception Report as the interpretation of TOR §3.1, for DESCO's written acceptance.

**Domain:** No mutable score. An append-only `DecisionLedger` of immutable `StageDecision`s. Instruments, anchors, eligibility policies, evaluation policies and disclosure policies are all **versioned configuration owned by DESCO**, not code.

**Evidence:** Three-layer separation — immutable facts, org-level context with validity intervals, versioned interpretation policy. `EvidenceItem` is derived per criterion, never stored criterion-neutral. Negative evidence is inadmissible until disclosed under ACR instruction 11.

**Scoring:** Deterministic wherever the ACR permits. OBJECTIVE criteria never touch a model. HYBRID criteria use a deterministic prior with a policy-capped AI adjustment. QUALITATIVE criteria use anchored LLM recommendation with mandatory citations and a permitted `INSUFFICIENT_EVIDENCE` outcome. Totals and bands are pure functions. Weights exist in the model and ship uniform.

**AI:** Narrow and deep rather than broad and shallow. LLM confined to two tasks — anchored criterion recommendation and pen-picture drafting — both citation-constrained, both structured-output, both against a sealed snapshot. Everything else the TOR calls AI is deterministic rules or classical statistics. No fine-tuning in the pilot. No predictive attrition model in the pilot.

**Authority:** Bitemporal organisation and supervision data; HRM-assigned authority chains snapshotted per case; eligibility computed and persisted with its policy version; four independently recorded assessments, with final-score resolution as an explicit, versioned, DESCO-set policy.

**Security:** ABAC over RBAC for case-scoped access; server-side disclosure packets; structurally segregated health data; whitelisted prompt projection that cannot reach demographic or health fields; hash-chained audit log; encrypted sensitive fields with the `Name` requirement raised for clarification.

**Fairness:** Rater-effect analysis and counterfactual perturbation probes as the substantive programme; the TOR's named group-fairness metrics implemented as monitoring signals with documented, honest limitations rather than as decorative dashboard tiles.

### K.2 The five architectural pillars, ranked

If everything else were compromised under schedule pressure, these five are the ones that must survive, because each is prohibitively expensive to retrofit:

1. **`EvaluationInputSnapshot`** — reproducibility. Without it, nothing else in the audit, validation or fairness story is real.
2. **Append-only decision ledger** — form fidelity and defensibility.
3. **Evidence eligibility as a network boundary** — the only durable protection for health and demographic data.
4. **Versioned, DESCO-owned policy configuration** — the answer to scenario explosion and to R-05.
5. **Bitemporal organisation and authority data** — the answer to "who was my officer in 2027?" asked in 2030.

### K.3 Phasing against the TOR's six months

Realistic sequencing, mapped to TOR §7.1, with the honest observation that Phase 3 as written (build everything, SIT, UAT and Go-Live in Months 3–5) is compressed:

| TOR Phase | Architecture work | Risk note |
|---|---|---|
| Phase 1 (M1) | Obtain the Grade 12–16 form. Resolve the M-register questions, especially M-01 (final score), M-05 (certifying condition), M-19 (GPU). Author the deviation notes for §3.1 and §5.1. Confirm health module scope. | **Everything downstream depends on this month.** |
| Phase 2 (M2–3) | Instrument model, anchors authored **by DESCO**, policy model, domain model, snapshot design, authority/temporal model, disclosure design, API contracts, AI evaluation design. | Anchor authoring is the hidden critical path (M-07). |
| Phase 3 (M3–5) | Core build, integration adapters, deterministic scoring, AI inference service, evidence workflow, ledger, dashboards, SIT/UAT. | Deterministic scoring and workflow must be complete and UAT-ready even if AI is degraded — build the system so it is usable with AI off. |
| Phase 4 (M3–5) | Mobile input module against the same evidence APIs. | Reuses the core; no separate domain. |
| Phase 5 (M5–6) | Training, handover, documentation. | Three-deployable footprint is transferable in 12 days; twelve microservices would not be. |
| Phase 6 (M6–12) | Support, first real cycle observation, override-rate and rater-effect data collection, model recalibration. | This is when the data needed for §G.2's ML path and §G.6's fine-tuning path begins to exist. |

A design decision that follows from this table and deserves stating on its own: **the system must be fully operable with the AI plane disabled.** The appraisal process is legally and organisationally complete without AI — that is how it runs on paper today. Making AI an enhancement rather than a dependency de-risks Go-Live, satisfies the graceful-degradation expectation of §3.8(b), and gives DESCO a fallback that does not involve reverting to paper.

---

## L. Architecture Decision Register

Decisions that can responsibly be made now, on technical grounds, without DESCO input.

| ID | Decision | Rationale | Reversibility |
|---|---|---|---|
| ADR-01 | `AppraisalCase` has **no** mutable score field | ACR p.6 records up to four independent assessments; a mutable field would be form-infidelity, not just poor design | Low — foundational |
| ADR-02 | Stage decisions are immutable and append-only, hash-chained | R-28 auditability; ACR instr. 17/20/23 supersession semantics | Low |
| ADR-03 | Comment supersession is modelled as a link, never an edit | ACR instr. 17/20/23 require both texts to survive | Low |
| ADR-04 | `EvaluationInputSnapshot` is content-addressed, immutable, and referenced by every AI run and every decision | R-67, R-68, R-70, R-72 all become mechanical; grievance defensibility | Low — the backbone |
| ADR-05 | `EvidenceItem` is a derived projection, not a stored entity | One fact, many criterion-scoped readings; avoids duplication and criterion-neutral pretence | Medium |
| ADR-06 | Context is recorded once at org/unit level with a validity interval and joined at evaluation time | Prevents scenario explosion (§C.2) | Low |
| ADR-07 | `EventSignificance` is computed by policy, never stored as user input | Removes a manipulation surface | Medium |
| ADR-08 | Instruments, anchors, eligibility, evaluation, disclosure and resolution policies are versioned configuration, effective-dated | R-05, R-71; historical cases resolve under the policy in force | Low |
| ADR-09 | Instrument version is frozen per cycle; mid-cycle changes apply to the next cycle only | Prevents in-flight cases changing rules under officers | Low |
| ADR-10 | AI output is never written directly to an official mark; officer write is a separate record | R-27 enforced structurally | Low |
| ADR-11 | Provider-abstracted AI gateway (Spring AI in the Java core, Python inference service behind it), with model/prompt/anchor/rubric versions recorded per run | R-72, §G.8; keeps the model replaceable | Low |
| ADR-12 | Structured, schema-validated AI output with mandatory, programmatically verified citations; free-form prose is never parsed for scores | Hallucination control; §G.3 | Low |
| ADR-13 | `INSUFFICIENT_EVIDENCE` is a first-class AI outcome; the AI may decline to recommend | R-69 robustness | Low |
| ADR-14 | Any open-weight model licence is verified against TOR §9 (full IP vesting in DESCO) **before** it is adopted | Contractual exposure on model deliverables | Low — do this in Phase 1 |
| ADR-15 | No fine-tuning in the pilot | §G.6: no data, no eval set, revalidation burden, unbudgeted GPU | High — revisit after cycle 1 |
| ADR-16 | Health data lives in a separate schema with separate credentials, structurally unreachable from the AI plane | §I.3; stronger than a configuration flag | Low |
| ADR-17 | Prompt construction uses a whitelisted projection; demographic and family fields are never in the whitelist | §I.3; removes a discrimination pathway by construction | Low |
| ADR-18 | ABAC/policy-based authorisation over case-scoped resources, layered on RBAC | Access depends on the authority chain and stage, which a role cannot express | Medium |
| ADR-19 | Disclosure packets are computed and persisted server-side; the client never receives redacted-but-present data | R-81; client-side hiding is not redaction | Low |
| ADR-20 | Bitemporal storage for organisation, position, assignment and supervision data | Historical defensibility of authority chains | Low |
| ADR-21 | Facts are immutable; corrections supersede and mark dependent snapshots stale | §H.3; handles overturned disciplinary findings | Low |
| ADR-22 | Deployment: modular monolith core + separate Python AI inference and analytics services | §J.3; boundary drawn along the domain, not against it | Medium |
| ADR-23 | The system is fully operable with the AI plane disabled | Go-Live de-risking; §K.3 | Low |
| ADR-24 | Weighting capability exists in the instrument model, ships uniform at 1.0 | R-05: capability without instrument alteration | Low |
| ADR-25 | Cross-tier aggregation operates on totals and bands only, never on raw criterion marks | §D.1 constraint 4: the ordinal scales are not comparable | Low |
| ADR-26 | Attachments are content-addressed in an object store, virus-scanned at ingest, referenced by hash in snapshots; OCR-to-prompt is a separate policy-gated step | §H.5 | Low |
| ADR-27 | Pilot is single-tenant; tenancy-relevant boundaries kept clean but no tenant features built | §I.7 | Medium |
| ADR-28 | PostgreSQL recommended (TOR permits it); persistence adapters isolated so Oracle remains available | §J.1 | Medium — subject to M-20 |

---

## M. DESCO Policy Decision Register

Questions that **must not** be answered by developers. Each carries what it blocks and what the system will do if no answer arrives — a default that is deliberately the most conservative reading, and which must be flagged as provisional rather than allowed to harden.

| ID | Question | Blocks | Provisional default | Priority |
|---|---|---|---|---|
| **M-01** | **How is the official final score determined when the reporting officer's total and up to three holistic totals differ?** | Every dashboard, report, promotion file, and the entire reporting layer | `HIGHEST_AUTHORITY_TOTAL` (approving officer) | **Critical — Phase 1** |
| **M-02** | Provide the **Grade 12–16 ACR form** (20 criteria, 5-point scale) and confirm whether it shares the same bands, pen picture, recommendation, health and bio-data structure | Instrument configuration for half the workforce; SRS closure; §3.8 tier-specific testing | Cannot proceed | **Critical — Phase 1** |
| **M-03** | Does the 3-month supervision rule apply to countersigning and certifying officers, or only to the reporting officer? (The ACR states it for the reporting officer; the TOR extends it) | Reviewer eligibility policy; workflow gating | Apply to reporting officer only, per ACR text | **Critical — Phase 1** |
| **M-04** | What happens when **no officer meets the 3-month threshold** (multiple transfers)? | Case initiation; exception workflow | HRM exception route with recorded justification | High |
| **M-05** | **Under exactly what conditions does the Certifying Officer stage apply?** Neither document states the condition | Workflow branching; UAT test cases (§3.8 names this explicitly) | Stage present only when HRM assigns a certifying officer | **Critical — Phase 1** |
| **M-06** | Is the appraisal period the **calendar year** (per ACR instr. 1) or the fiscal/APA year (July–June, implied by the TOR's APA references)? | Cycle definition; every integration date range | Calendar year, per ACR instr. 1 | **Critical — Phase 1** |
| **M-07** | **Who authors and approves the behavioural anchors** for each criterion at each scale point? They do not exist on the paper form | AI recommendation quality; evaluator consistency; §3.8(b) validation | Cannot proceed without DESCO-authored anchors | **Critical — Phase 2 critical path** |
| **M-08** | How are criteria that presuppose supervisory duties (17, 21, 24) handled for non-supervisory staff? | Scoring; total comparability | Score as-is, preserving current practice (R-01) | High |
| **M-09** | Which instrument applies when an employee's **grade changes mid-cycle**? | Instrument selection; will occur in cycle 1 | Grade held at cycle end | High |
| **M-10** | When several officers are eligible, **who writes the report**, and are partial-period reports permitted? | Partial-period aggregation policy | Sole report by longest-tenure eligible officer | High |
| **M-11** | May an upper authority **reject** a report outright, or only return it for revision? | Workflow decision types | Return only; reject disabled | Medium |
| **M-12** | Should **score divergence** between stages trigger mandatory justification or escalation, and at what threshold? | Divergence rules; anomaly alerting | Justification required on band-crossing divergence; no auto-escalation | Medium |
| **M-13** | What happens when an assigned officer **transfers, retires or dies** mid-cycle before signing? | Succession/delegation policy; deadlock prevention | HRM reassigns with recorded reason; prior decisions preserved | High |
| **M-14** | May AI recommend the **promotion-eligibility category**, or is it human-only? | AI scope | Human-only | High |
| **M-15** | Should AI draft **comments for upper authorities**, given that only the reporting officer writes the pen picture on the form? | AI scope at stages 2–4 | Pen picture for reporting officer only; no AI comment drafting upstream | Medium |
| **M-16** | Confirm explicitly that **health data must never influence performance evaluation** — the TOR does not say so | Eligibility policy; a foundational rule | Health data strictly excluded | **Critical — Phase 1** |
| **M-17** | Will DESCO **collect protected attributes** for fairness testing, and under what legal basis? Without them, several TOR-named metrics cannot be computed | §3.2.2.2 fairness deliverables; §6.1 AI Model Validation Report | No collection; rely on rater-effect analysis and counterfactual probes | **Critical — Phase 1** |
| **M-18** | What is the **minimum agreement/accuracy threshold** for AI recommendations, and what benchmark corpus will it be measured against? TOR §3.8(b) requires this to be agreed pre-Go-Live | Go-Live acceptance | Cannot be set unilaterally | **Critical — Phase 1** |
| **M-19** | Who provides **GPU infrastructure** for on-premise LLM inference, at what capacity, and by when? | The entire AI capability | Cannot proceed; hard dependency | **Critical — Phase 1** |
| **M-20** | Oracle or PostgreSQL — does DESCO ICT have a database standard for on-prem systems it must support post-handover? | Persistence choice | PostgreSQL | High |
| **M-21** | Is the **ad-hoc health concern workflow** (TOR §3.2.3.2(ii)) in scope for the pilot? The TOR itself defers this | Scope; effort estimate | Out of scope | High |
| **M-22** | What may an employee see on the **self-service dashboard**? TOR §3.6(d) implies ratings and comments; the ACR keeps them confidential | Disclosure policy; a legal exposure | Own bio-data, own self-input, disclosed shortfalls, adverse excerpts only | **Critical — before UAT** |
| **M-23** | Confirm the interpretation of the **"minimum three months"** — calendar months or 90 days; contiguous or cumulative; does approved leave, deputation, or acting supervision count? | Eligibility computation | 90 cumulative days; acting counts; leave counts | High |
| **M-24** | Which **shortfall-disclosure interval** applies under TOR §1's "at entry or at a configurable interval", and how long is the employee's response window? | Evidence admissibility timing (ACR instr. 11) | Disclosure at entry; 14-day response window | High |
| **M-25** | Confirm the encryption scope for **`Name`** — field-level AES-256 will break search, sort and reporting | Data model; performance UAT | Raise as clarification (N-09) | High |
| **M-26** | Does DESCO have any **digitised historical ACR data**? If not, TOR §6.3 (labelled/annotated datasets) and §3.2.2.1 (past-vs-current analysis) cannot be met in the pilot | Deliverables §6.3; analytics scope | Assume none; renegotiate §6.3 | **Critical — Phase 1** |
| **M-27** | Are **segregation-of-duties rules** (no self-appraisal, no dual-stage occupancy, mutual-appraisal detection) acceptable additions? They are standard controls but not in the source documents | Control implementation | Implement and disclose in the Inception Report | Medium |
| **M-28** | What is the **records retention period** for ACRs, evidence, snapshots and AI prompt/response logs? | Storage planning; audit policy | Follow DESCO records policy once supplied | Medium |

---

## N. TOR Contradictions, Ambiguities and Technically Risky Requirements

Raised without reinterpretation. Each is stated as the TOR states it, followed by the problem.

### N-01. KPI framework versus ACR fidelity — the flagship contradiction

TOR §1 and §3.2.1.1(a) require replication of the ACR instruments **without alteration**. TOR §3.2.1.2 requires a KPI engine that "manages KPI templates, **weight distribution**, and evaluation cycles", supports "monthly, quarterly, and annual KPI calculation" and "target vs. actual variance analysis". TOR §3.2.1.3 requires that "KPIs and corresponding weightages shall be defined based on individual job descriptions".

**The supplied ACR form has no KPIs, no targets, no weights and no variance analysis.** Its 25 criteria are overwhelmingly behavioural traits (ব্যক্তিত্ব, বুদ্ধিমত্তা, বিচার ও মাত্রাজ্ঞান), each worth an equal maximum of 4 points. These two sets of requirements cannot both be satisfied inside the official ACR score. Either the KPI layer is **supplementary and non-scoring** (a management-information layer alongside the ACR), or it **alters the instrument** and requires a change request under §3.2.1.1(a).

**Recommended resolution:** treat KPI/target data as evidence feeding ACR criterion recommendations and as a separate management dashboard, not as a parallel scoring system. Requires DESCO confirmation.

### N-02. Payment percentages differ between §7.1 and §10

| Phase | §7.1 milestone column | §10 payment column |
|---|---|---|
| Phase 3 (UAT / pilot Go-Live) | **40%** | **35%** |
| Phase 6 (post-handover support) | **5%**, "payable quarterly" | **10%**, "payable after maintenance and support period (by end of Month 12)" |

Both tables total 100%, so this is not an arithmetic slip in one place — the two schedules are genuinely different documents. It also affects **when** the support payment falls due (quarterly instalments versus a single end-of-period payment). This is a contractual defect that must be corrected before signature.

### N-03. Predictive analytics required in a single-cycle pilot

§3.2.2.1 requires predictive analytics for attrition risk, training needs and future performance; §3.2.2.1 also requires past-vs-current performance analysis. §6.3 requires delivery of "labelled and annotated datasets used for training, validating and testing the AI models". §7.1 gives a six-month implementation covering one appraisal cycle at most.

Attrition and future-performance prediction require multi-year labelled outcomes; past-vs-current analysis requires at least one prior digital cycle. **Neither exists at pilot Go-Live**, and §6.3's dataset deliverable presupposes a labelled corpus that does not exist. Unless DESCO holds digitised historical ACR data (M-26), these requirements are not satisfiable as written and should be deferred or redefined as descriptive analytics.

### N-04. Calendar year versus APA/fiscal year

ACR instruction 1 states one report per **calendar year** (পঞ্জিকা বৎসর). TOR §2 requires alignment with the **APA**, which in Bangladeshi public-sector practice runs on the fiscal year (July–June), and the TOR refers throughout to the "APR year" without defining it. Cycle boundaries determine every evidence date range and every integration query. Must be fixed (M-06).

### N-05. APA and ACR are conflated

TOR §2 speaks of aligning employee goals with "DESCO's Annual Confidential Report (ACR)/Annual Performance Agreement (APA)". These are different instruments at different levels: the APA is an organisation-level agreement with government; the ACR is an individual confidential report. Treating them as interchangeable obscures whether individual criteria are meant to cascade from organisational APA targets — which, again, the ACR form provides no mechanism for.

### N-06. Employee self-service dashboard versus ACR confidentiality

TOR §3.6(d) requires an "Employee Self-Service Dashboard" with "access to personal KPIs, **ratings, comments**, and training history", plus "visual insights on strengths, weaknesses" and comparison against previous evaluation periods.

TOR §1, §3.2.3.3 and §3.7(a) — and ACR instruction 3 — restrict employee visibility to the **specific adverse excerpt only**, and the entire form is marked গোপনীয়.

These are directly contradictory. This is not a UI question; it is a confidentiality-policy question with legal implications, and it will surface in UAT if not resolved in Phase 1 (M-22).

### N-07. AI pen pictures for authorities who do not write pen pictures

TOR §1 requires AI-drafted pen pictures "for review, modification, and final approval by the designated reporting, countersigning, certifying and approving authorities". On the ACR form, the pen picture (লেখচিত্র, p.5) is written by the **reporting officer only**; upper authorities write comments and a holistic total. Clarify what artefact the AI is expected to draft at each stage (M-15).

### N-08. The 3-month rule extended beyond its source

TOR §1 and §3.2.1.2 state that a "reporting, countersigning, or certifying officer may evaluate an employee only where that officer has supervised the employee for a minimum of three (3) months". The ACR states the 3-month requirement for the **reporting officer** (instruction 15) and for **special ACRs** (instruction 2). It does not state it for countersigning or certifying officers. The TOR's extension may reflect real DESCO practice, but it is an extrapolation from the supplied source and should be confirmed rather than implemented as established policy (M-03).

### N-09. Encryption scope is internally inconsistent and operationally problematic

§3.2.2.2 specifies encryption of "Name, NID, Birth Certificate". §5.2 specifies "Name, NID, Birth Date". The third field differs. Separately, **field-level AES-256 encryption of `Name`** breaks search, sort, pagination, reporting and joins across the entire application — in a system whose primary navigation is by employee name. This will fail usability and performance UAT. Requires clarification and probably a deterministic-encryption or TDE-plus-access-control alternative (M-25).

### N-10. ISO/IEC 27001 "compliance" versus "alignment"

§5.2 requires "compliance with ISO/IEC 27001 information security management practices"; §6.1 requires a report documenting "alignment with ISO/IEC 27001 (or the agreed equivalent standard)". ISO 27001 certifies an *organisation's* management system; a vendor can implement and evidence aligned controls but cannot deliver DESCO a certification. The contract should say which is meant.

### N-11. Python/TensorFlow prescription does not match the workload

§5.1 prescribes "AI/ML engine: Python, TensorFlow". The AI workload described in the TOR is (a) LLM-based recommendation and narrative generation, for which the serving ecosystem is vLLM/TGI/PyTorch, and (b) statistical rater-effect and fairness analysis, for which the tools are statsmodels and scikit-learn. TensorFlow is the natural choice for neither. Python is entirely appropriate. Recommend a documented reading of "Python/TensorFlow" as "a Python ML stack appropriate to the workload" (§J.1).

### N-12. Microservices versus a six-month on-premise pilot

§3.1 prescribes microservices. §7.1 allows five months to design, build, integrate, test and Go-Live, on-premise, with §7.3 handing operations to DESCO ICT in a 12-day knowledge transfer. Microservices distribute the very invariants (snapshot sealing, ledger append, disclosure recomputation) whose atomicity underpins auditability, and transfer substantial operational burden to DESCO. See §J for the analysis and the recommended hybrid.

### N-13. Fairness metrics that cannot be computed as defined

§3.2.2.2 names demographic parity, disparate impact and equal opportunity. Demographic parity and disparate impact require protected attributes that AIPMS may not hold and that DESCO may not be permitted to collect for this purpose (M-17). Equal opportunity additionally requires a ground-truth performance label, which does not exist — the officer's mark is the object of audit, not a ground truth. See §I.5 for what can be delivered honestly instead.

### N-14. Peer comparison as an input to rating recommendation

§3.2.2.1 requires "peer comparison (department/division-wise, as an aggregation of individual scores)" within the AI Performance Scoring module. If peer position influences an individual's *recommended mark*, the system silently imports forced-distribution logic that the ACR does not contain — each employee is scored against criteria, not against colleagues. Peer comparison should be a **reporting** feature, explicitly excluded from recommendation inputs. Requires confirmation.

### N-15. Design and development phases overlap

§7.1 places Phase 2 (SRS/HLD/SDD) in Months 2–3 and Phase 3 (core development) in Months 3–5; §10 milestone 3 is due "within 2 months after approval of the SRS & SDD". Development therefore begins in the same month design is approved, at best. This is survivable with disciplined phasing but should be acknowledged as a compressed schedule rather than treated as slack.

### N-16. Certifying-officer condition is never stated

§1, §3.2.3.3 and §3.8 all refer to the certifying stage as "applicable in certain cases, per DESCO's existing ACR guidelines". Neither the TOR nor the supplied ACR states what those cases are. §3.8 explicitly requires UAT test cases exercising "the conditional certifying-officer step" — which cannot be written without the condition (M-05).

### N-17. Structural and minor issues

- **§3.1** lists "Mobile App Based Performance Input Module" as a *core architectural principle* alongside scalability and security. It is a module (and is properly specified at §3.4).
- **§7.2** states hands-on training will be "conducted in a minimum of single batches", which is not parseable as a requirement.
- **§7.2** requires specialised ICT training but, unlike the other two tracks, specifies no headcount or duration.
- **ACR p.3 item 5** asks for "ক্যাডারের নাম" (cadre name) — a civil-service concept inherited from the government template. DESCO is a PLC; this field may be permanently empty. Confirm whether to render, hide or repurpose it.
- **§6.2** requires deployment "on DESCO's main server" while §1 states the pilot "shall operate independently". Confirm the deployment target and isolation expectations.
- **§3.2.2.2** requires compliance with "GoB data protection norms" without naming an instrument. Bangladesh's data-protection legislation has been in flux; the applicable instrument should be named so controls can be designed against it rather than against a moving target.
- **TOR §1** replaces the ACR's dual-copy paper process (instructions 8 and 12) with a single digital record. This is a sanctioned and sensible deviation, but it is a deviation from the source instrument and should be recorded as such.

---

## O. Major Failure Modes

Ordered by expected damage, with the architectural control that addresses each.

### O-1. Rubber-stamping (automation bias)

**Scenario.** Officers accept AI recommendations wholesale. Within two cycles, the "AI-assisted" system is the de facto decision-maker, human authority is nominal, and TOR §1's central guarantee is hollow.

**Why it happens.** Accepting a pre-filled number is faster than justifying a different one, particularly for 25 criteria across dozens of appraisees under deadline.

**Controls.** Override-rate monitoring per evaluator with alerting on near-total concurrence (R-70). Mandatory justification when accepting a recommendation flagged `LOW_CONFIDENCE` or `INSUFFICIENT_EVIDENCE`. Evidence-coverage gating so a recommendation cannot exist without cited evidence.

**The deeper design tension, unresolved.** Override statistics are only meaningful if the AI recommendation precedes the human mark — but showing the recommendation first *creates* the anchoring it is meant to measure. Proposed answer: a configurable **blind-first mode**, where the officer records a provisional mark before the AI reveal, both are retained, and divergence between provisional and final marks becomes a direct measure of AI influence. This needs empirical validation during the pilot (§P.1) and is one of the more interesting R&D questions the project offers.

### O-2. Evidence starvation

**Scenario.** Officers do not record achievements or shortfalls during the year. At cycle close, the AI has almost nothing, produces low-confidence recommendations or `INSUFFICIENT_EVIDENCE` across the board, and the system delivers less than paper did while costing more.

**Why it happens.** Continuous evidence recording (TOR §3.4) is the genuine behavioural change the project depends on, and behavioural change is the part no architecture can guarantee.

**Controls.** Evidence-coverage dashboards for HRM by unit and evaluator; mid-cycle reminders (§3.5.2); the mobile app specifically designed for 30-second entry; a hard rule that criteria without evidence require manual marks with written justification; and coverage reported as a pilot-evaluation metric in its own right. **This should be stated to DESCO as a joint risk, not a vendor deliverable** — it is the difference between a system that works and one that is technically complete and practically empty.

### O-3. Retaliatory or back-dated negative evidence

**Scenario.** An officer records a year's worth of shortfalls in the last fortnight, or back-dates entries after a dispute.

**Controls.** Recording-lag detection (§C.3); the ACR instruction 11 admissibility gate — undisclosed negative evidence simply cannot enter the evaluation; evidence-snapshot sealing at submission; and late-entry patterns surfaced in the anomaly report.

### O-4. Hallucinated pen pictures

**Scenario.** A generated pen picture describes an achievement that never happened, an officer signs it under time pressure, and it enters a permanent personnel record.

**Controls.** Generation from structured evaluation output only, never from raw text; mandatory citations with programmatic verification that every cited identifier exists in the snapshot; narrative–band consistency checks; and drafts that are never auto-filed. Note that citation verification checks *existence*, not *faithfulness* — a model can cite a real item and still misdescribe it. Human sign-off remains the real control, which is why the draft must be short enough to actually read.

### O-5. Confidentiality breach via analytics

**Scenario.** A departmental dashboard for a unit of three makes individual scores trivially inferable, defeating the entire গোপনীয় classification through aggregation.

**Controls.** Minimum-cell-size suppression on every aggregate view; suppression of complementary cells that permit differencing; disclosure packets computed server-side; ABAC scoping so hierarchy alone does not confer visibility.

### O-6. Silent policy drift

**Scenario.** Someone adjusts an eligibility rule or an anchor mid-cycle. Cases evaluated before and after the change are scored under different rules, with nothing in the record showing it.

**Controls.** Instrument versions frozen per cycle (ADR-09); all policies effective-dated with a `PolicyChangeRecord` requiring an approver and rationale; every snapshot recording the policy version set that produced it; and revalidation of affected models triggered by rubric change (R-71).

### O-7. AI plane unavailable at Go-Live

**Scenario.** GPU procurement slips, or on-prem inference underperforms, and Month 5 arrives with no working AI engine.

**Controls.** ADR-23 — the system is fully operable with AI disabled. Go-Live can proceed on the deterministic and workflow capability, which is already a substantial improvement on paper. The AI plane is a separately deployable service that can be enabled when infrastructure is ready. This single decision converts the project's largest external dependency (M-19) from a Go-Live blocker into a feature flag.

### O-8. Bangla output quality failure

**Scenario.** Generated pen pictures are grammatically correct but register-wrong — informal where the ACR demands formal administrative Bangla — and officers rewrite every one, so the feature saves no time.

**Controls.** Benchmark candidate models on real Bangla administrative prose before selection (§P.3); template-assisted drafting fallback; measure edit distance between draft and final as a live quality metric during the pilot.

### O-9. Corrected evidence invalidating completed appraisals

**Scenario.** A disciplinary finding used in an appraisal is overturned on appeal three months after the ACR is approved.

**Controls.** Supersession marks dependent snapshots stale; affected decisions are flagged rather than silently re-run; an explicit HRM-triggered reopening path exists. Whether reopening is permitted at all is a DESCO policy question that should be added to the Phase 1 agenda.

### O-10. Authority chain deadlock

**Scenario.** The approving officer retires in Month 11; cases sit unsignable; the cycle cannot close.

**Controls.** Succession/delegation policy (M-13); ageing alerts on stage instances; HRM reassignment that preserves prior decisions in the ledger and records the reason.

### O-11. Snapshot storage growth

**Scenario.** Snapshots, prompt logs and model responses grow faster than projected; storage becomes a cost and performance problem in year two.

**Controls.** Content-addressing deduplicates identical fact versions across snapshots; a retention and cold-storage tier designed from the start; compression of prompt/response payloads; retention policy aligned to DESCO records policy (M-28).

### O-12. Cross-tier comparison producing nonsense

**Scenario.** A dashboard averages criterion marks across both instruments; a 3 on the 4-point scale and a 3 on the 5-point scale are treated as equivalent; rankings are quietly wrong.

**Controls.** ADR-25 — cross-tier aggregation on totals and bands only. Enforce with a type distinction between `CriterionMark` and `NormalisedTotal` so the mistake is a compile error rather than a reporting bug.

### O-13. Litigation or grievance three years later

**Scenario.** An employee challenges a 2027 appraisal in 2030. The evidence has been corrected, the org chart has changed twice, the model has been replaced, and the anchors have been revised.

**Controls.** This is the scenario the whole architecture is built for: bitemporal authority data answers *who* was the officer; the sealed snapshot answers *what* they saw; the versioned policy set answers *under what rules*; the model descriptor answers *which model recommended what*; and the append-only ledger answers *who decided what and why*. If any one of the five pillars in §K.2 was dropped, this scenario has no good answer.

---

## P. Open R&D Questions

These require investigation before HLD/SDD can be considered sound. They are research questions, not design gaps — each has multiple defensible answers and the right one is empirical.

**P-1. Blind-first versus AI-first presentation.** Does showing the AI recommendation before the officer's judgement measurably anchor the mark, and by how much? Does blind-first materially slow evaluators? Design a controlled comparison within the pilot, since this determines whether override rate (R-70) means anything at all.

**P-2. Minimum evidence volume for a defensible recommendation.** Below what quantity and quality of cited evidence does a criterion recommendation stop being better than a coin flip? Needed to set the `INSUFFICIENT_EVIDENCE` threshold per criterion type rather than by intuition.

**P-3. Bangla LLM benchmark.** Construct a Bangladesh-specific evaluation set covering (a) anchored ordinal judgement over Bangla evidence, (b) formal administrative Bangla generation in ACR register, (c) structured JSON reliability with Bangla content, (d) hallucination and citation faithfulness. Benchmark Qwen, Llama and Mistral class models at deployable sizes. **Also test whether reasoning in English over Bangla evidence outperforms reasoning in Bangla** — a non-obvious question with real quality and cost implications.

**P-4. Confidence calibration.** Does model-reported confidence correlate with actual agreement with officers? Almost certainly not out of the box. Establish a calibration method (temperature scaling, isotonic regression on shadow-run data) so that "low confidence" triggers review for the right cases.

**P-5. Anchor authoring methodology.** The ACR has no behavioural anchors. How should DESCO author them — expert panel, retrospective derivation from historical marks, iterative refinement during the pilot? How is inter-anchor consistency validated across 25 (and 20) criteria and two languages? This is on the Phase 2 critical path and has no vendor-side answer.

**P-6. Rater-effect model identifiability.** In a strictly hierarchical organisation, evaluators may not share appraisees, which limits the crossing needed to separate rater severity from true performance. Assess DESCO's actual supervision graph before committing to a many-facet Rasch or mixed-effects approach; determine minimum sample sizes and whether unit-level anchoring is required.

**P-7. Counterfactual probe design.** Which perturbations (name, gender-typical name, religion-typical name, unit, grade, pronoun) and what drift magnitude constitutes a failure? Needs a defined probe suite and pass thresholds before it can gate deployment (§I.5).

**P-8. Deviation cap calibration for HYBRID criteria.** Is ±1 scale point the right cap? Should it vary by criterion or by evidence strength? Determine empirically from shadow runs rather than by assumption.

**P-9. Context significance policy design.** How should a `ContextFact` modulate an indicator without creating a gaming surface? If officers can create context facts, they can manufacture mitigation. Investigate who may author which context types, and whether org-level contexts should be restricted to HRM/administration.

**P-10. Cross-tier normalisation for organisational reporting.** Given ranges of 25–100 and 20–100 and non-comparable ordinal marks, what is the defensible way to report organisation-wide performance across both instruments? Band distribution is safe; anything finer needs justification.

**P-11. Prompt and context budget.** For an employee with a year of dense evidence, what is the selection strategy — top-k by relevance, temporal stratification, pattern summary plus exemplars? Selection is itself an interpretive act and must be deterministic, versioned and auditable, since two different selections produce two different recommendations from the same evidence.

**P-12. Path to classical ML.** After how many approved `(snapshot → final mark)` pairs does an ordinal model become competitive with the LLM on HYBRID criteria? Estimate sample requirements now so that feature materialisation is designed to support it, not retrofitted.

**P-13. Effect of the coarse ordinal scale on band stability.** With 25 criteria at 4 points each, every criterion is worth 1% of the total and bands are 10 points wide. Analyse how sensitive band assignment is to plausible mark variation, and whether that sensitivity is materially different on the 20×5 instrument. Relevant to how much precision the AI recommendation actually needs.

---

## Q. Summary of Immediate Next Steps

Before any HLD, SDD or implementation planning:

1. **Obtain the Grade 12–16 ACR form** (M-02). Requirements cannot be closed without it.
2. **Convene a Phase 1 policy session with DESCO** covering the eleven Critical items in the M-register — above all M-01 (final score resolution), M-05 (certifying condition), M-06 (cycle year), M-07 (anchors), M-16 (health exclusion), M-18 (accuracy threshold), M-19 (GPU), M-22 (employee visibility) and M-26 (historical data).
3. **Table the N-register in writing** as TOR clarification requests — particularly N-01 (KPI vs ACR), N-02 (payment discrepancy), N-03 (predictive analytics), N-06 (self-service dashboard) and N-13 (fairness metrics). Deviations from §3.1 and §5.1 should be recorded in the Inception Report for written acceptance, not implemented silently.
4. **Confirm the anchor-authoring plan and owner** (P-5). This is the Phase 2 critical path and it belongs to DESCO, not the vendor.
5. **Run the Bangla model benchmark** (P-3) in parallel with Phase 1, so that the GPU capacity question (M-19) can be answered with a specific model and size rather than a guess.

Only then should the domain model, API contracts and AI evaluation design proceed to HLD/SDD.

---

*Prepared as pre-design architecture and R&D analysis. No implementation code, boilerplate, HLD or SDD is included, and no prior architecture work has been carried forward.*
