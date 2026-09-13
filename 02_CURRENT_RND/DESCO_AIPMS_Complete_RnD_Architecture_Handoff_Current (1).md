# DESCO AIPMS — Complete R&D & Architecture Handoff
## Clean-Slate Architecture Context After Metric Classification, Input Workflow, Scenario Simplification, and Appraisal-Integrity R&D

**Status:** Current working source-of-truth handoff for the next clean-slate architecture exercise  
**Audience:** Principal solution architect / Claude Pro browser project / internal R&D team  
**Primary purpose:** Consolidate the current DESCO AIPMS understanding before creating the new architecture from scratch  
**Important:** This document contains confirmed source facts, strong working design decisions, current R&D directions, and unresolved DESCO policy questions.

Where an official DESCO source conflicts with this document, the official source wins.

---

# 1. Why This New Handoff Exists

Earlier R&D and architecture work was done before several important concepts became clear.

Recent R&D has materially refined the design around:

- the official 25-metric Grade 1–11 ACR,
- the 10-domain AI-only context classification,
- scenario-library design,
- open-world handling of unseen scenarios,
- primary performance input,
- AI metric mapping,
- evidence accumulation,
- annual AI recommendation,
- initial pen picture generation,
- review feedback on the workflow,
- simplification of the scenario catalogue,
- and protection against malicious or biased human evaluators.

Therefore:

> **The next architecture should be designed from scratch using the current understanding.**

Do not restart the R&D from zero.  
Do restart the **software architecture** from zero.

Previous architecture/implementation work may later be used as historical reference, but it should not anchor the new design.

---

# 2. Source Precedence

For architecture work, interpret sources in this order:

```text
1. DESCO Revised AIPMS TOR
        ↓
2. Official DESCO ACR Forms
        ↓
3. Current DESCO-specific R&D decisions
        ↓
4. Current classification/workflow documents
        ↓
5. Pre-architecture analysis reports
        ↓
6. Scenario catalogues / examples
        ↓
7. Historical generic appraisal R&D
        ↓
8. Previous implementation architecture/code
```

### Conflict rule

- TOR and official ACR are authoritative.
- Current DESCO-specific R&D supersedes older generic appraisal R&D.
- Analysis documents can identify contradictions and recommend resolutions but cannot silently override official DESCO policy.
- AI-generated scenario examples or anchors must never be treated as official DESCO policy unless DESCO approves them.

---

# 3. Core Project Objective

Build an **AI-assisted performance management/appraisal system for DESCO** that:

- preserves DESCO's official appraisal instruments,
- collects performance evidence throughout the year,
- combines qualitative and approved structured/system evidence,
- maps evidence to official ACR metrics,
- recommends explainable metric-level scores,
- generates an initial evidence-backed pen picture,
- supports human review and higher appraisal authority,
- maintains complete auditability,
- supports on-prem/local AI,
- and remains operational even when AI is unavailable.

The AI is a **decision-support component**, not the institutional authority.

---

# 4. Official Grade 1–11 ACR Facts

The supplied official Grade 1–11 ACR contains:

- employee identity/year information,
- health examination section,
- biodata/employment/training information,
- Reporting Officer scoring,
- pen picture and recommendations,
- Countersigning Officer block,
- Certifying Officer block where applicable,
- Approving Officer block,
- official instructions.

## Official Grade 1–11 scoring

There are:

> **25 official criteria × integer 1–4**

Maximum = 100  
Minimum = 25

The Reporting Officer scores the 25 criteria separately.

The official total is a direct sum.

### Performance bands

- 95–100 — Extraordinary
- 85–94 — Excellent
- 75–84 — Good
- 60–74 — Satisfactory / current standard
- below 60 — below current standard

The current Grade 1–11 form does **not** define a weighted parameter model.

---

# 5. The 25 Official Grade 1–11 Metrics

1. Discipline — শৃঙ্খলা বোধ  
2. Judgment & Sense of Proportion — বিচার ও মাত্রাজ্ঞান  
3. Intelligence — বুদ্ধিমত্তা  
4. Energy & Initiative — উদ্যম ও উদ্যোগ  
5. Personality — ব্যক্তিত্ব  
6. Cooperation — সহযোগিতা  
7. Punctuality — সময়ানুবর্তিতা  
8. Reliability — নির্ভরযোগ্যতা  
9. Sense of Responsibility — দায়িত্ববোধ  
10. Interest in Work — কাজে আগ্রহ  
11. Promptness in Taking Action & Following Orders — ব্যবস্থা গ্রহণে ও আদেশ পালনে তৎপরতা  
12. Safety Awareness — নিরাপত্তা সচেতনতা  
13. Conduct with the Public — জনসাধারণের সাথে ব্যবহার  
14. Professional Knowledge — পেশাগত জ্ঞান  
15. Quality of Work — কাজের মান  
16. Quantity of Work — সম্পাদিত কাজের পরিমাণ  
17. Supervisory & Management Capability — তদারকি ও পরিচালনার সামর্থ্য  
18. Relationship with Colleagues — সহকর্মীদের সাথে সম্পর্ক  
19. Decision-Making Skill — সিদ্ধান্ত গ্রহণে দক্ষতা  
20. Ability to Implement Decisions — সিদ্ধান্ত বাস্তবায়নে সামর্থ্য  
21. Interest & Skill in Training Subordinates — অধীনস্থদের প্রশিক্ষণদানে আগ্রহ ও দক্ষতা  
22. Written Expression — প্রকাশ ক্ষমতা (লিখন)  
23. Verbal Expression — প্রকাশ ক্ষমতা (বাচনিক)  
24. Promptness in Writing/Countersigning ACRs — বার্ষিক গোপনীয় অনুবেদন লিখন ও প্রতিস্বাক্ষরকরণে তৎপরতা  
25. Devotion to Duty — কর্তব্যনিষ্ঠা  

### Non-negotiable rule

No architecture may silently:

- delete,
- rename,
- merge,
- replace,
- reweight,
- normalize away,
- or generate parent scores instead of

these 25 official Grade 1–11 outputs.

---

# 6. Grade 12–16 Remains a Requirements Gap

The TOR states a separate Grade 12–16 instrument exists with:

> **20 criteria × 5-point scale**

The actual Grade 12–16 ACR form has not yet been supplied.

Therefore the following are unknown until the real form is obtained:

- actual 20 criteria,
- applicability rules,
- exact form sections,
- pen-picture structure,
- authority/signature structure,
- any special instructions,
- and whether all Grade 1–11 workflow assumptions carry over.

### Architecture consequence

The architecture should support multiple appraisal instruments/configurations.

However:

> **The SRS/HLD cannot be considered fully closed until the official Grade 12–16 form is obtained.**

Do not invent its criteria.

---

# 7. Current 10-Domain AI Context Classification

The 10 domains are **not official DESCO criteria**.

They are used only inside the AI reasoning/context layer to:

- reduce reasoning space,
- organize scenario guidance,
- route evidence,
- provide cleaner metric context,
- improve mapping consistency.

They receive **no score**.

---

## Domain 1 — Discipline & Punctuality

Official metrics:

1. Discipline  
7. Punctuality

Strict scope:

- rule compliance,
- orderly/professional conduct,
- attendance/time discipline.

Office confidentiality/security rules may belong here when they are fundamentally compliance/conduct matters.

---

## Domain 2 — Reliability & Responsibility

Official metrics:

8. Reliability  
9. Sense of Responsibility  
25. Devotion to Duty

Strict scope:

- dependability,
- ownership,
- accountability,
- duty continuity,
- sustained commitment.

Do not automatically map one event to all three.

---

## Domain 3 — Work Motivation & Initiative

Official metrics:

4. Energy & Initiative  
10. Interest in Work  
11. Promptness in Taking Action & Following Orders

Strict scope:

- self-starting action,
- engagement,
- motivation,
- timely response to lawful/authorized instructions.

Self-motivation toward achieving assigned goals may be scenario context but is **not** a new official criterion.

---

## Domain 4 — Judgment & Cognitive Ability

Official metrics:

2. Judgment & Sense of Proportion  
3. Intelligence

Strict scope:

- reasoning,
- analytical understanding,
- situational comprehension,
- sound judgment.

For technical employees, technical comprehension can be evidence of cognitive ability, but technical/job knowledge itself remains Metric 14.

---

## Domain 5 — Decision & Execution Capability

Official metrics:

19. Decision-Making Skill  
20. Ability to Implement Decisions

Strict scope:

- selecting a course of action,
- and carrying that decision through.

Team-leading/coordination situations may provide evidence, but formal supervisory/management ability remains Metric 17.

---

## Domain 6 — Professional Competence & Productivity

Official metrics:

14. Professional Knowledge  
15. Quality of Work  
16. Quantity of Work

Strict scope:

- technical/job know-how,
- correctness and quality,
- actual work output/productivity.

---

## Domain 7 — Workplace Behaviour & Team Relations

Official metrics:

5. Personality  
6. Cooperation  
18. Relationship with Colleagues

Strict scope:

- professional behavior,
- cooperation,
- team interaction,
- internal working relationships.

Do not use this as a catch-all for communication skills.

---

## Domain 8 — Communication & Public Interaction

Official metrics:

13. Conduct with the Public  
22. Written Expression  
23. Verbal Expression

Strict scope:

- stakeholder/public conduct,
- written communication,
- verbal communication.

Internal teamwork should remain distinct.

---

## Domain 9 — Supervisory Leadership & Staff Development

Official metrics:

17. Supervisory & Management Capability  
21. Interest & Skill in Training Subordinates  
24. Promptness in Writing/Countersigning ACRs

Strict scope:

- supervision,
- people management,
- developing subordinates,
- appraisal responsibilities.

Role applicability must follow DESCO policy.

---

## Domain 10 — Safety Awareness

Official metric:

12. Safety Awareness

Strict scope:

- physical/workplace safety,
- operational safety,
- emergency readiness,
- disaster-prevention awareness where relevant.

Confidentiality/information secrecy is not automatically treated as Safety Awareness.

---

# 8. Parent-Domain Rule

Correct hierarchy:

```text
10 AI Context Domains
        ↓
25 Official DESCO Metrics
        ↓
Metric-Specific Evidence
        ↓
AI Recommendation for Each Metric
```

Incorrect hierarchy:

```text
10 Parent Scores
        ↓
Automatically Derived Child Scores
```

Example:

```text
Professional Competence & Productivity
    ├── Professional Knowledge → 4
    ├── Quality of Work         → 3
    └── Quantity of Work        → 2
```

The parent domain never receives a score.

---

# 9. Metric Contamination Is a Major Risk

A single positive event must not become evidence for every vaguely related metric.

Example:

> “Employee worked very hard to complete an urgent task.”

A weak system might incorrectly map that to:

- Initiative
- Responsibility
- Reliability
- Devotion to Duty
- Interest in Work
- Quality
- Quantity
- Decision Making

This would inflate the appraisal.

Preferred evidence-link model:

```text
PRIMARY relevance
SECONDARY relevance
NOT RELEVANT
```

Only sufficiently relevant links should become appraisal evidence.

---

# 10. Scenario Library — Current Philosophy

The scenario catalogue is **not a closed rulebook**.

It is an AI context/example library.

The system must continue to work when an event is not already listed.

Preferred reasoning hierarchy:

```text
Parent Domain Definition
        ↓
Official Metric Definition
        ↓
Scenario Examples
        ↓
Boundary / Exclusion Guidance
```

The first two provide the conceptual foundation.

Scenarios improve consistency.

---

# 11. Open-World Handling of New / Unlisted Scenarios

Preferred logic:

```text
New performance event
        ↓
Close match to known scenario?
        │
   ┌────┴────┐
   │         │
  YES        NO
   │         │
Use known    Reason from:
scenario     - domain definition
context      - official metric definition
             - boundaries/exclusions
             - approved behavioral guidance
   │         │
   └────┬────┘
        ↓
AI proposes mapping
        ↓
Human confirms/corrects
```

Possible outcomes:

### A. Clearly covered by an existing metric
Map normally.

### B. Mapping is uncertain
Require human review.

### C. No meaningful ACR relevance
Do not force a mapping.

### D. Raises a new policy issue
Do not let AI invent policy; escalate for DESCO clarification.

---

# 12. Scenario Library Governance

Potential lifecycle:

```text
Initial Approved Context Library
        ↓
Real Usage
        ↓
Novel / Unmatched Cases
        ↓
Human Review
        ↓
Recurring and Useful?
        │
       YES
        ↓
Add as New Approved Example
        ↓
Version the Context Library
```

Assessments should preserve which context-library version was used.

---

# 13. Scenario Catalogue Simplification — Revised Direction

The first scenario catalogue became too complicated.

It included:

- scenario IDs,
- Scenario Family column,
- Evidence Direction column,
- Strong Positive / Positive / Negative / Strong Negative labels,
- DESCO-style example,
- AI Mapping / Boundary Note column.

Recent review concluded that this is unnecessarily complex.

### Revised per-metric catalogue structure

Each official metric should use:

```text
Metric Name

Short Definition
    ↓

Positive Scenarios
| Scenario | DESCO-Style Example |

Negative Scenarios
| Scenario | DESCO-Style Example |

Boundary / Do Not Confuse With
• exclusion / distinction
• exclusion / distinction
• common confusion
```

### Remove from the human-review document

- manual scenario IDs,
- Scenario Family terminology,
- Evidence Direction column,
- Strong Positive/Strong Negative labels,
- repeated AI Mapping column,
- repeated row-level boundary notes.

Useful boundary knowledge should be consolidated at the **metric level**.

---

# 14. Scenario Deduplication Principle

Do not create many rows merely because the workplace situation differs.

Bad pattern:

- on-time office attendance,
- on-time training attendance,
- on-time meeting attendance,
- on-time field inspection,
- on-time customer appointment.

Better:

> **Reports for scheduled duties and commitments on time**

Example may list office, meeting, training, field duty, shift or customer appointment.

### Why this is better

The AI should learn the **behavioral concept**, not memorize every workplace variant.

---

# 15. Scenario Count

Do not force an equal number of scenarios per metric.

Guideline only:

- approximately 6–10 distinct positive scenarios,
- approximately 6–10 distinct negative scenarios,
- approximately 3–6 important boundaries/exclusions.

Narrow metrics may need fewer.

Broad metrics may need more.

The final count should be driven by **distinct behavioral patterns**, not an arbitrary quota.

---

# 16. Important Similar-Metric Boundaries

These distinctions should be explicitly encoded in the metric context.

## Discipline vs Punctuality

- Discipline = compliance with rules/procedures/proper conduct.
- Punctuality = reporting/attending at the scheduled time.

## Reliability vs Responsibility

- Reliability = whether others can consistently depend on the employee.
- Responsibility = whether the employee takes ownership/accountability.

## Responsibility vs Devotion to Duty

- Responsibility = ownership of specific responsibilities.
- Devotion to Duty = sustained seriousness and commitment toward official duty over time.

## Initiative vs Interest in Work

- Initiative = proactively taking useful action.
- Interest in Work = engagement, curiosity, learning interest and attention toward work.

## Initiative vs Promptness

- Initiative = proactive action, often without waiting for instruction.
- Promptness = taking action without unnecessary delay after an instruction/requirement exists.

## Punctuality vs Promptness

- Punctuality = being present/reporting at the expected time.
- Promptness = speed of initiating action.

These boundaries should reduce evidence duplication and metric contamination.

---

# 17. Revised Primary Performance Input Workflow

Recent review feedback changed the earlier workflow.

### Removed

The previous **Hybrid Input** option has been removed.

### Current input modes

There are now two main modes:

---

## A. Quick Input

The primary inputter writes what happened naturally.

Example:

> “Employee handled the feeder fault well, identified the issue quickly and coordinated the field team.”

Flow:

```text
Quick Input
    ↓
AI proposes primary domain
    ↓
Human confirms/corrects domain
    ↓
Metric mapping proceeds
```

---

## B. Guided Input

The inputter selects:

- one of the 10 domains,
- optionally a common scenario,
- then describes the actual event.

Flow:

```text
Guided Input
    ↓
Selected domain confirmed
    ↓
Scenario/context retrieved
    ↓
Metric mapping proceeds
```

---

# 18. Primary Domain Checkpoint

The revised workflow adds an explicit **Primary Domain Checkpoint**.

The purpose is to prevent the AI from searching all 25 metrics without structure.

For Quick Input:

```text
Natural-language event
    ↓
AI suggests primary domain
    ↓
Human confirms/corrects
```

For Guided Input:

```text
User-selected domain
    ↓
Human confirmation
```

The confirmed domain becomes the **normal mapping boundary**.

---

# 19. Cross-Domain Mapping

Selecting a primary domain must not trap the event incorrectly.

If strong evidence clearly points to another domain:

```text
Primary domain
    ↓
AI detects strong cross-domain relevance
    ↓
Cross-domain flag
    ↓
Human explicitly confirms/adds the extra metric
```

The AI should not silently attach the event to many unrelated metrics.

---

# 20. Minimum Event Input — Working Candidate

A performance event may contain:

- employee,
- event date / period,
- primary domain,
- scenario (optional),
- free-text description,
- outcome / impact,
- supporting evidence/reference,
- record nature,
- optional repetition/frequency context.

Possible record nature:

- achievement,
- positive observation,
- shortfall/deficiency,
- factual/general record.

Avoid making the form an unofficial scoring matrix.

Do not force fields such as:

- severity 1–5,
- complexity 1–5,
- importance 1–5,
- hidden behavior score 1–4,

unless a future DESCO-approved methodology explicitly requires them.

---

# 21. Primary Inputter Should Not Give Event-Level ACR Scores

The first person should judge:

> **What happened?**

They should not normally judge:

> **What annual 1–4 score does this one event deserve?**

Why:

If every event receives a 1–4 mark, the system immediately invents another scoring methodology:

```text
Event 1 = 4
Event 2 = 2
Event 3 = 4

Average = ?
```

DESCO's official ACR does not currently define incident-score averaging.

Therefore:

> **Event capture and annual appraisal scoring must remain separate.**

---

# 22. Event-Level Evidence Profile — New Explicit Layer

Review feedback showed that the path from event to annual score needed a clearer intermediate layer.

Each confirmed event/metric link should preserve structured evidence metadata such as:

- relevance:
  - Primary
  - Secondary
- evidence direction:
  - Supporting
  - Contrary
  - Contextual / Neutral
- source/evidence reference,
- outcome/impact,
- date/period,
- repetition/frequency context,
- verification/provenance state.

This is **not an employee score**.

It is the structured evidence profile used later for annual reasoning.

---

# 23. One Event Must Be Stored Once

A real-world event should not be duplicated simply because it supports more than one official metric.

Correct:

```text
Evidence Event E-014
    ├── Professional Knowledge [PRIMARY]
    ├── Decision Making        [PRIMARY]
    └── Initiative             [SECONDARY]
```

Incorrect:

```text
E-014A
E-014B
E-014C
```

as if three separate incidents happened.

---

# 24. Human Confirmation of Mapping

AI proposes mapping.

The officer should be able to:

- accept,
- remove,
- add,
- correct,
- or hold an uncertain case for review.

The confirmed mapping then becomes part of the appraisal evidence set.

This creates useful future data:

```text
AI proposed mapping
        ↓
Human final mapping
```

which can later be used to evaluate/improve the model.

---

# 25. Evidence Sources Across the Appraisal Period

Annual assessment should use multiple permitted evidence sources.

## A. Supervisor / Reporting Officer Inputs

- achievements,
- observations,
- contributions,
- shortfalls,
- work events.

## B. Approved Structured/System Facts

Potential examples:

- attendance,
- training,
- rewards/recognition,
- finalized disciplinary/compliance records,
- authorized KPI/task facts,
- customer/service data,
- project/operational data,
- other approved source-system facts.

## C. Employee Self-Input

Employee self-input should be factual:

- achievement,
- work completed,
- supporting evidence.

It should **not** become:

- self-rating,
- self-score,
- self-assigned ACR marks.

---

# 26. Build 25 Separate Official Metric Evidence Sets

The system should aggregate confirmed evidence per official metric.

Example:

```text
Metric 14 — Professional Knowledge

Supporting:
E-017
E-043
E-061

Contrary:
E-052

Context:
Training T-006
```

Each official metric has its own evidence set.

The parent domain never creates a shared score.

Sibling metrics do not automatically inherit the same evidence.

---

# 27. AI Assessment at Appraisal Time

At appraisal time:

```text
Metric Evidence Set
        +
Official Metric Definition
        +
Parent-Domain Context
        +
Relevant Scenario Examples
        +
Boundary / Exclusion Guidance
        +
Approved Behavioral Anchors
        ↓
AI Metric Assessment
```

Possible output:

```json
{
  "metric": "Professional Knowledge",
  "recommendedMark": 3,
  "reason": "Repeated evidence demonstrates strong job knowledge...",
  "supportingEvidence": ["E-017", "E-043", "E-061"],
  "contraryEvidence": ["E-052"],
  "evidenceSufficiency": "ADEQUATE"
}
```

AI should be allowed to return:

```text
INSUFFICIENT_EVIDENCE
```

rather than forcing a score.

---

# 28. 1–4 Behavioral Anchors Are Still an Open Critical Issue

A metric name alone is not enough for AI to defensibly distinguish:

- 1
- 2
- 3
- 4

The system likely requires:

- DESCO-approved scoring descriptors/behavioral anchors,
- or another formally validated evidence-to-score methodology.

### Critical rule

Do **not** invent official anchors and present them as DESCO policy.

Anchor design/approval is a policy/governance workstream.

---

# 29. Evidence Sufficiency Is Still Open

The system needs a formal policy for when enough evidence exists to recommend a mark.

Possible factors:

- amount of evidence,
- time coverage,
- source reliability,
- consistency,
- supporting vs contrary evidence,
- objective/system evidence,
- role applicability,
- repeated vs isolated behavior.

No final threshold has been frozen yet.

---

# 30. Reporting Officer Role

The AI recommendation remains advisory.

For each metric, the Reporting Officer should be able to review:

- AI recommendation,
- rationale,
- supporting evidence,
- contrary evidence,
- evidence sufficiency,
- mapping history if relevant.

The Reporting Officer remains responsible for the official metric score.

---

# 31. Human-First vs AI-First Score Presentation Is Still Open

## Option A — AI-First

```text
AI recommendation
    ↓
Officer sees it
    ↓
Officer accepts/changes
```

Risk:

- AI anchoring.

## Option B — Human-First / Blind-First

```text
Officer gives provisional judgment
    ↓
AI recommendation revealed
    ↓
Officer confirms/changes final mark
```

Potential advantages:

- reduces anchoring,
- preserves evaluator independence,
- allows measurement of:
  - original human judgment,
  - AI recommendation,
  - final human judgment.

No final choice is frozen.

---

# 32. Initial Pen Picture

The initial pen picture should be generated **after structured metric assessment**.

Preferred sequence:

```text
Performance Records
    ↓
Evidence Mapping
    ↓
25 Metric Evidence Sets
    ↓
25 AI Metric Assessments
    ↓
Reporting Officer Review
    ↓
AI Drafts Initial Pen Picture
```

The draft may use:

- reviewed metric assessments,
- major achievements,
- meaningful shortfalls,
- strengths,
- development areas,
- evidence-backed patterns,
- historical context where policy permits.

The Reporting Officer edits/accepts the draft.

---

# 33. Higher Authority Workflow Is Not Yet Fully Reworked

The current R&D focus has been:

- primary performance input,
- AI evidence mapping,
- Reporting Officer initial assessment,
- initial pen picture.

Higher authority workflow remains a separate architecture workstream.

Important existing source fact:

The Grade 1–11 ACR contains distinct:

- Reporting Officer assessment,
- Countersigning Officer total/comment,
- Certifying Officer total/comment where applicable,
- Approving Officer total/comment.

Higher authorities do not simply rewrite the 25 criterion marks on the paper form.

The next architecture must preserve form fidelity and explicitly model this hierarchy.

---

# 34. New Major Architecture Concern — Malicious or Biased Evaluator

A new R&D question has been added:

> What if the primary evaluator or next authority intentionally evaluates an employee badly?

The architecture must not assume every human evaluator is honest or unbiased.

Potential abuses include:

- false negative observations,
- exaggerated adverse comments,
- selective recording of failures,
- omission of achievements,
- intentional low scoring,
- retaliation,
- collusion between evaluators,
- unexplained score deviation,
- tampering with historical evidence,
- conflict of interest.

The architecture should make malicious evaluation:

> **harder, visible, attributable, and reviewable.**

---

# 35. Appraisal Integrity Principle

The system should **not prevent a human officer from giving a low mark**.

Sometimes a low mark is correct.

Instead:

> **The system should prevent an unsupported low mark from passing through invisibly.**

This preserves human authority while increasing accountability.

---

# 36. Evidence Provenance

Every performance record should preserve provenance.

Possible evidence/source classification:

```text
SYSTEM VERIFIED
OFFICIAL RECORD
DOCUMENT SUPPORTED
SUPERVISOR OBSERVATION
EMPLOYEE SELF-REPORTED
DISPUTED
UNVERIFIED
```

These are trust/provenance states, **not employee-performance scores**.

AI should reason differently about:

```text
3 unsupported negative remarks from one supervisor
```

versus:

```text
3 negative events supported by official records
```

Exact weighting/treatment requires DESCO policy.

Architecture must preserve the distinction.

---

# 37. Adverse Event Lifecycle

Negative/adverse input should not simply appear at year-end without context.

Preferred conceptual flow:

```text
Adverse Performance Event
        ↓
Recorded During Appraisal Period
        ↓
Evidence / Source Attached
        ↓
Employee Notified Where Policy Requires
        ↓
Employee Response
        ↓
Corrective Opportunity / Follow-Up
        ↓
Final Status Preserved
```

Example:

```text
March:
Punctuality issue recorded

Employee notified

April–December:
No recurrence
```

AI should see:

- initial adverse event,
- employee response,
- corrective action,
- sustained improvement.

Not only the original negative event.

---

# 38. Employee Response Without Employee Veto

An employee should not be able to delete adverse feedback.

Instead:

```text
Officer Observation
        +
Employee Response
        +
Supporting Evidence
        +
Final Review State
```

All remain visible in the audit trail.

This allows the higher authority and AI to see both sides.

---

# 39. Immutable / Append-Only Decision History

Confirmed evidence and appraisal decisions should behave conceptually as append-only records.

Correction should occur through:

```text
Original Record
    ↓
Correction / Response / Superseding Record
```

not by silently rewriting history.

Similarly:

```text
AI recommended 3
Reporting Officer entered 1
Reason entered
Next authority reviewed
```

All stages should remain attributable.

---

# 40. Score Justification Gate

If a human score materially differs from AI/evidence patterns, the system may require stronger explanation.

Example:

```text
AI Recommendation = 3
Officer Score      = 3
→ normal workflow

AI Recommendation = 3
Officer Score      = 2
→ short reason may be required

AI Recommendation = 4
Officer Score      = 1
→ major deviation flag
→ reason + evidence required
→ higher review
```

This does **not** mean AI is always correct.

It means large unexplained divergence becomes reviewable.

---

# 41. Human–AI Deviation Analysis

The system should be capable of comparing:

- AI recommendation,
- human score,
- evidence pattern,
- evidence sufficiency.

Possible output:

```text
Human score:       1
AI recommendation: 3
Evidence pattern:  mostly positive
Status:            significant unexplained deviation
```

The system should not automatically overwrite the human mark.

Instead it should:

> flag for review.

---

# 42. Historical Anomaly Detection

Historical appraisal data may be useful as an **integrity signal**, not as a current-score determinant.

Example:

```text
2024 = 86
2025 = 88
2026 = 52
```

The system should not say:

> "Employee scored well before, so 2026 must be high."

It may say:

> "Significant year-to-year deviation detected; verify whether sufficient current evidence explains the change."

Historical consistency should support review, not score inheritance.

---

# 43. Evaluator Calibration / Pattern Analytics

The architecture should preserve enough data to later identify unusual evaluator behavior.

Possible indicators:

- evaluator average significantly lower/higher than peers,
- unusually high override rate against AI,
- frequent large downward deviations,
- evaluator almost never increases scores,
- unusually high adverse-record frequency,
- one employee being treated very differently from peers without evidence.

These are:

> **review signals, not proof of malicious intent.**

The system must never label an evaluator malicious automatically.

---

# 44. Anti-Selective-Evidence Design

A biased supervisor may not submit false negatives.

They may simply hide positives.

Therefore annual assessment should not depend only on narrative supervisor input.

The snapshot should also include all authorized data available from:

- attendance,
- training,
- awards,
- official task/KPI records where approved,
- customer-service data,
- project/operational data,
- finalized disciplinary records,
- employee factual achievements,
- other approved systems.

This reduces the ability of one evaluator to define the full reality.

---

# 45. Conflict-of-Interest Support

Architecture should be capable of representing evaluator conflicts such as:

- family/personal relationship,
- active grievance,
- disciplinary dispute,
- direct organizational conflict,
- same person occupying incompatible appraisal stages,
- other DESCO-defined conflict conditions.

Potential model concept:

```text
EvaluatorConflict
ConflictType
DeclaredBy
ReviewedBy
Resolution
```

Whether specific conflicts trigger reassignment or higher scrutiny is DESCO policy.

---

# 46. Appraisal Integrity Layer — Conceptual Capability

The system should include a business capability conceptually like:

```text
             APPRAISAL INTEGRITY LAYER

┌──────────────────────────────────────┐
│ Evidence Provenance                  │
├──────────────────────────────────────┤
│ Adverse-Event Control                │
├──────────────────────────────────────┤
│ Employee Response / Dispute Context  │
├──────────────────────────────────────┤
│ Human–AI Deviation Analysis          │
├──────────────────────────────────────┤
│ Historical Consistency Signals       │
├──────────────────────────────────────┤
│ Evaluator Calibration Analytics      │
├──────────────────────────────────────┤
│ Conflict-of-Interest Controls        │
├──────────────────────────────────────┤
│ Immutable Audit Trail                │
└──────────────────────────────────────┘
```

This does not necessarily need to become a separate microservice.

It is a required **business capability**.

---

# 47. Proportional Integrity Controls

Do not create unnecessary bureaucracy.

Possible approach:

```text
Normal score supported by evidence
→ no extra explanation

Moderate deviation
→ short reason

Major deviation
→ reason + evidence required

Adverse / very low assessment
→ stronger justification and review
```

This keeps the workflow usable while protecting against abuse.

---

# 48. AI Must Not Become "Judge of the Judge"

Incorrect approach:

```text
Human Score
    ↓
AI decides whether human is fair
```

Preferred:

```text
AI Recommendation
Human Recommendation
Evidence Pattern
Objective Facts
Historical Pattern
Evaluator Pattern
        ↓
Consistency / Anomaly Indicators
        ↓
Authorized Human Review
```

AI detects potential inconsistency.

It should not make accusations.

Preferred language:

> "Significant unexplained deviation; review required."

Not:

> "The supervisor is malicious."

---

# 49. Three-Layer Protection Against Malicious Evaluation

## Prevention

Make manipulation harder:

- multiple evidence sources,
- provenance,
- no arbitrary event score,
- employee response,
- conflict checks,
- verified/official evidence.

## Detection

Detect unusual patterns:

- human-vs-evidence discrepancy,
- human-vs-AI discrepancy,
- historical anomaly,
- evaluator-pattern anomaly,
- selective-input pattern.

## Accountability

Preserve:

- who entered the evidence,
- when,
- what evidence existed,
- what AI recommended,
- what the human decided,
- why a deviation occurred,
- who reviewed it,
- and what the final decision was.

---

# 50. Sensitive Data Boundary

Health/personal information from the ACR should not automatically be fed into scoring AI.

A clean architecture should separate:

- institutional/profile data needed for workflow,
- scoring-relevant evidence,
- sensitive health/private data,
- restricted information.

The AI assessment input should be sanitized and policy-controlled.

---

# 51. Deterministic vs AI Responsibilities

Strong working principle:

## Deterministic Business System Owns

- institutional truth,
- employees,
- roles/authority,
- appraisal periods,
- official evidence records,
- workflow state,
- official scores,
- arithmetic totals,
- performance band conversion,
- access control,
- audit,
- provenance,
- conflict state,
- evidence/version references,
- integrity flags,
- final human decisions.

## AI Owns / Performs

- natural-language interpretation,
- domain recognition,
- scenario matching,
- metric mapping suggestions,
- evidence summarization,
- supporting/contrary pattern analysis,
- metric score recommendations,
- rationale generation,
- pen-picture drafting,
- anomaly explanation/support where permitted.

AI should never own institutional truth.

---

# 52. Current Likely Technical Split — Not Yet Frozen

Current likely direction:

```text
Frontend
    ↓
Java / Spring Boot Business Core
    ↓
Python AI / ML Service
```

Possible ownership:

### Java / Spring Business Core

- users/employees,
- organization/authority,
- performance events,
- evidence,
- appraisal lifecycle,
- official scores,
- audit,
- snapshots,
- integrity controls,
- notifications,
- policy version references,
- source-system integration.

### Python AI Service

- natural-language interpretation,
- AI context retrieval,
- domain/metric mapping,
- AI assessment,
- local-model inference,
- structured outputs,
- pen-picture generation,
- model/prompt/context version execution.

Preferred boundary:

> Python should not directly own or mutate the core business database.

Java should send a sanitized/versioned input snapshot to the AI layer.

### Important

This split must be **re-evaluated from first principles** during architecture design.

Do not keep it only because earlier R&D suggested it.

---

# 53. AI Must Be Advisory and Replaceable

The business system should remain usable if AI is unavailable.

AI should not be:

- source of official truth,
- only holder of evidence,
- mandatory for every workflow step,
- source of institutional policy,
- impossible to replace.

Architecture should support:

- provider/model abstraction where practical,
- on-prem/local model serving,
- model/version tracking,
- prompt/template version tracking,
- context-library version tracking,
- structured validated outputs,
- graceful AI failure,
- reproducibility.

---

# 54. Immutable Evaluation Snapshot

At appraisal time, create a sealed/versioned evaluation input representing:

- employee/appraisal context,
- eligible evidence,
- source/provenance state,
- confirmed metric mappings,
- domain/metric definitions,
- scenario/context library version,
- behavioral-anchor/policy version,
- model version,
- prompt/template version.

Purpose:

- auditability,
- dispute resolution,
- later reproduction,
- model comparison,
- legal/grievance defense,
- validation.

Exact implementation remains an architecture decision.

---

# 55. AI Context Library — Preferred Logical Components

Future AI reasoning context should likely contain:

```text
10 Parent Domain Definitions
        │
        ├── 25 Official Metric Definitions
        ├── Inclusion Guidance
        ├── Boundary / Exclusion Guidance
        ├── Approved Behavioral Anchors
        ├── Positive Scenario Examples
        ├── Negative Scenario Examples
        ├── Common Confusions
        └── Role-Specific Context Examples
```

Role-specific scenario context may include:

- office/admin,
- technical/engineering,
- S&D/network,
- field operations,
- outage/fault response,
- ICT,
- project work,
- customer service,
- team coordination,
- supervisory work,
- safety/emergency/disaster response.

The official metric set remains the same.

---

# 56. Role Applicability Problem

Metrics such as:

- Supervisory & Management Capability,
- Training Subordinates,
- Writing/Countersigning ACRs

may not naturally apply to every Grade 1–11 employee.

The existing official form does not provide a simple N/A mechanism.

The system must not silently:

- drop these criteria,
- rescale totals,
- insert neutral scores,

without DESCO approval.

This is a policy issue.

Architecture should support future applicability rules, but the default must preserve the official instrument until DESCO decides otherwise.

---

# 57. KPI vs ACR Remains a Policy Contradiction

The TOR includes KPI/target-management requirements.

The official Grade 1–11 ACR is a 25-criterion unweighted 1–4 instrument.

Therefore KPI data should not silently become another official scoring system inside the ACR.

Current recommendation:

> Treat KPI/target data as authorized evidence for relevant ACR metrics and/or as a separate management analytics layer, unless DESCO explicitly approves a new scoring model.

Claude should flag this for formal DESCO resolution.

---

# 58. Historical Data / Future ML Direction

Human-approved appraisal history is potentially valuable future training data.

Useful future dataset:

```text
Employee / Role
        +
Evidence Snapshot
        +
AI Recommendation
        +
Human Initial Score
        +
Human Final Score
        +
Override Reason
        +
Final Pen Picture
```

This can support:

- model benchmarking,
- calibration,
- fine-tuning,
- evaluator-pattern analysis,
- classical ML experiments,
- fairness studies.

Fine-tuning should not begin until sufficient high-quality approved data exists.

---

# 59. Local / On-Prem AI Direction

DESCO requires strong control over data.

Current R&D direction favors local/on-prem model serving.

Candidate open-weight model families should be selected through benchmarking, not naming preference alone.

Benchmark dimensions should include:

- Bangla understanding,
- English understanding,
- Bangla/English mixed administrative text,
- ordinal reasoning,
- metric mapping,
- evidence grounding,
- structured JSON reliability,
- hallucination,
- pen-picture quality,
- latency,
- GPU fit,
- on-prem operability.

Keep the model replaceable.

---

# 60. Claude Pro Browser Is the Architecture Owner

Claude Pro in the browser will be used as the principal architecture model.

Do **not** rely on Claude inside Antigravity for the architecture.

### Claude Pro Browser Role

- first-principles architecture analysis,
- domain modeling,
- architecture decisions,
- ADRs,
- HLD,
- evidence architecture,
- appraisal-integrity architecture,
- AI boundary design,
- architecture challenge/review.

### ChatGPT Role

- R&D partner,
- challenge assumptions,
- source-pack preparation,
- decision comparison,
- review Claude output,
- refine prompts.

### Antigravity + Gemini/Flash Role

- implementation,
- coding,
- module construction,
- migrations,
- tests,
- frontend,
- implementation fixes.

Claude Pro should not be wasted on repetitive CRUD/boilerplate coding.

---

# 61. Recommended Claude Project Context Files

## Mandatory / Core

1. Revised DESCO AIPMS TOR
2. Official Grade 1–11 ACR
3. This complete current R&D handoff
4. Current 10-domain classification/workflow PDF
5. DESCO pre-architecture R&D/analysis report

## Strongly Useful

6. Simplified scenario catalogue for Domains 1–3
7. Review/critique material if useful
8. Any official DESCO Service Rules
9. Code of Conduct
10. HR/appraisal policy
11. organizational/reporting hierarchy
12. Grade 12–16 ACR when obtained

## Historical Reference Only

- earlier generic appraisal R&D,
- old HLD,
- old DB schema,
- old API design,
- old boilerplate architecture,
- previous implementation plans.

These should be labeled:

> **Historical reference only — not authoritative.**

---

# 62. Do Not Give Claude These as Primary Authority

Avoid treating these as source-of-truth:

- old implementation code,
- old database schema,
- old endpoint list,
- generic 5-point appraisal ideas,
- old parameter weighting models,
- old boilerplate technology decisions,
- unapproved scenario examples,
- AI-generated 1–4 anchors,
- previous architecture assumptions.

---

# 63. Clean-Slate Architecture Process

Recommended architecture sequence:

```text
PASS 1
First-Principles Architecture Reasoning
        ↓
PASS 2
Architecture Decisions / ADRs
        ↓
PASS 3
High-Level Architecture
        ↓
PASS 4
Detailed Domain / Data / Integration Design
        ↓
PASS 5
Implementation Planning
        ↓
Implementation
```

Do not start with database tables or endpoint lists.

---

# 64. Architecture Pass 1 Should Focus On

Claude should identify:

- business domains,
- actors,
- institutional truths,
- ownership of each data type,
- official appraisal instruments,
- performance-event lifecycle,
- evidence lifecycle,
- mapping lifecycle,
- annual evaluation lifecycle,
- higher-authority lifecycle,
- appraisal-integrity controls,
- AI vs deterministic responsibilities,
- source-system integrations,
- data-sensitivity boundaries,
- audit/reproducibility,
- conflict-of-interest handling,
- adverse-event handling,
- failure modes,
- unresolved policy questions,
- contradictions in TOR/ACR,
- deployment constraints,
- model-serving constraints.

---

# 65. Architecture Pass 1 Should NOT Produce

Do not ask yet for:

- full DB schema,
- complete API list,
- every frontend screen,
- final microservice count,
- exhaustive infrastructure manifests,
- final model choice,
- final 1–4 anchors,
- implementation code.

These come after architecture reasoning is reviewed.

---

# 66. Critical Open DESCO Policy Questions

The following must remain explicit until resolved:

1. Grade 12–16 official form/criteria.
2. Official 1–4 behavioral anchors for Grade 1–11.
3. Evidence sufficiency threshold.
4. Role applicability for metrics 17, 21, 24.
5. Human-first vs AI-first recommendation presentation.
6. Treatment of repeated vs isolated incidents.
7. Treatment of contradictory evidence.
8. Source/provenance weighting.
9. Employee response/dispute process.
10. Required notification for adverse observations.
11. Human-AI score-deviation threshold.
12. When deviation requires mandatory justification.
13. Evaluator calibration review policy.
14. Conflict-of-interest rules.
15. KPI relationship to official ACR.
16. Historical data availability.
17. Records retention.
18. Final-score resolution across appraisal authorities.
19. Exact certifying-stage conditions.
20. Employee visibility into appraisal evidence.
21. Scenario/context-library governance.
22. Authorized source systems.
23. Acceptable AI accuracy/validation targets.
24. GPU / infrastructure constraints.
25. Final local-model selection.

---

# 67. Strong Current Working Decisions

The following are the strongest current design decisions:

- Grade 1–11 official output remains 25 metrics × 1–4.
- 10 parent domains are AI context only.
- Parent domains do not receive scores.
- Scenario catalogue is open-world, not exhaustive.
- Scenario catalogue should be simple and concept-based.
- Primary input does not assign annual 1–4 marks to events.
- Current input modes are Quick Input and Guided Input.
- Hybrid Input has been removed.
- Quick Input AI-proposes a primary domain; human confirms.
- Guided Input uses a selected domain; human confirms.
- Confirmed domain becomes the normal mapping boundary.
- Cross-domain mapping requires explicit human confirmation.
- One event is stored once.
- One event may link to multiple official metrics where directly relevant.
- Each link has an evidence profile.
- Evidence accumulates over the appraisal period.
- 25 separate official metric evidence sets are built.
- AI recommends 1–4 only at appraisal time.
- AI recommendation must include explanation/evidence.
- AI may return insufficient evidence.
- Reporting Officer remains responsible for the official score.
- Pen picture is generated after structured metric assessment.
- Negative/adverse evidence must preserve provenance and response history.
- Human evaluator bias/malice must be mitigated through integrity controls.
- AI cannot declare a human evaluator malicious.
- Large unexplained score deviations should be reviewable.
- Audit trail should be append-only/attributable.
- AI must be replaceable and advisory.
- Institutional truth belongs to the deterministic business system.

---

# 68. Current Open Architecture Questions

These are architecture questions, not yet decisions:

- modular monolith vs service split,
- exact Java/Python deployment boundary,
- sync vs async AI workflows,
- event sourcing vs append-only audit records,
- snapshot storage format,
- evidence relation schema,
- vector/RAG requirement,
- context-retrieval design,
- prompt orchestration,
- model gateway design,
- model failover,
- evaluator analytics architecture,
- historical anomaly-engine design,
- dispute workflow,
- source integration patterns,
- notification architecture,
- policy/version modeling,
- immutable vs mutable domain data boundaries.

Claude should derive these from requirements, not inherit previous answers.

---

# 69. Architecture Anti-Patterns to Avoid

Do not build:

### A. Event = Score

```text
One event
    ↓
1–4 score
```

### B. Parent Domain = Score

```text
Domain score
    ↓
child scores
```

### C. Scenario List = Closed Rules

```text
No scenario match
    ↓
cannot evaluate
```

### D. AI = Institutional Authority

```text
AI gives score
    ↓
official score automatically accepted
```

### E. Supervisor Narrative = Entire Reality

```text
Supervisor wrote it
    ↓
treated as indisputable truth
```

### F. History = Current Score

```text
Last year high
    ↓
this year must be high
```

### G. AI = Bias Judge

```text
AI disagrees
    ↓
supervisor declared malicious
```

### H. Silent Data Overwrite

```text
Negative record edited
    ↓
old history disappears
```

---

# 70. One-Sentence Architecture Philosophy

> **Build DESCO AIPMS as a deterministic, auditable institutional appraisal system that preserves the official ACR, collects and verifies year-round evidence, uses AI only to organize evidence and recommend explainable metric-level assessments, keeps authorized humans accountable for final decisions, and includes explicit controls against unsupported, biased, or malicious appraisal behavior.**

---

# 71. Recommended Immediate Next Step

Before implementation:

1. Assemble the Claude Pro Project source pack.
2. Add the Revised TOR.
3. Add the official Grade 1–11 ACR.
4. Add this handoff.
5. Add the current classification/workflow PDF.
6. Add the pre-architecture analysis report.
7. Add the refined Domain 1–3 scenario catalogue once complete.
8. Start **Clean-Slate Architecture Pass 1**.
9. Review Claude's output critically before ADR/HLD.
10. Only after architecture decisions stabilize should detailed schema/API design begin.

---

# 72. Recommended Claude Architecture Role

Claude should be instructed:

> You are the principal solution architect for DESCO AIPMS.  
> This is a clean-slate architecture exercise.  
> You are not the implementation agent.  
> Derive the architecture from the supplied authoritative sources and the current R&D handoff.  
> Preserve DESCO's official ACR framework.  
> Treat the 10-domain classification as an internal AI context model, not a new appraisal instrument.  
> Treat scenario libraries as open-world examples, not exhaustive rules.  
> Do not invent DESCO policy.  
> Explicitly distinguish source facts, approved decisions, working hypotheses, and unresolved policy questions.  
> Design for human accountability, evaluator-bias resistance, evidence provenance, explainability, auditability, reproducibility, local/on-prem deployment, and AI replaceability.  
> Do not inherit old implementation architecture merely because it exists.  
> Do not jump directly to database tables, endpoints, or implementation code before completing first-principles architecture reasoning.

---

# End of Handoff

This document should be treated as the current R&D bridge into the new architecture exercise.
