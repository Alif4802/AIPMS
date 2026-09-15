# Revised DESCO AIPMS Terms of Reference (TOR) — Full Text Extract

**Source Document:** `01_AUTHORITATIVE_SOURCES/2026-08-18 DESCO_AIPMS_TOR_Revised_2_Final (Autosaved).docx`  
**Version:** Revised 2 (10/18 August 2026)  
**Status:** Rank 1 Authoritative Source for DESCO AIPMS Architecture  

---

AI-Based Performance Management System (AIPMS)

Dhaka Electricity Supply PLC (DESCO)

Terms of Reference (TOR)

Revised Version

Original: 11 July 2026  |  Revised: 10 August 2026


# List of Acronyms



| Acronym | Full Form |
| --- | --- |
| 2FA | Two-Factor Authentication |
| ACR | Annual Confidential Report |
| AES-256 | Advanced Encryption Standard, 256-bit key length |
| AI | Artificial Intelligence |
| AIPMS | AI-Based Performance Management System |
| APA | Annual Performance Agreement |
| API | Application Programming Interface |
| APR | Annual Performance Report |
| BDT | Bangladeshi Taka |
| CEH | Certified Ethical Hacker |
| CI/CD | Continuous Integration / Continuous Deployment |
| CISSP | Certified Information Systems Security Professional |
| CSE | Computer Science and Engineering |
| CV | Curriculum Vitae |
| DESCO | Dhaka Electricity Supply PLC |
| ECG | Electrocardiogram |
| GoB | Government of Bangladesh |
| HLD | High-Level Design |
| HR | Human Resources |
| HRMS | Human Resource Management System |
| ICT | Information and Communication Technology |
| ISO/IEC 27001 | International Organization for Standardization / International Electro technical Commission — Information Security Management Systems standard |
| IT | Information Technology |
| KPI | Key Performance Indicator |
| ML | Machine Learning |
| MLOps | Machine Learning Operations |
| NID | National Identity (card/number) |
| PDF | Portable Document Format |
| PIU | Project Implementation Unit |
| PLC | Public Limited Company |
| PMP | Project Management Plan |
| PRINCE2 | PRojects IN Controlled Environments, version 2 (project management methodology) |
| QA | Quality Assurance |
| RBAC | Role-Based Access Control |
| REST / RESTful | Representational State Transfer (API architectural style) |
| SDD | Software Design Description |
| SIT | System Integration Testing |
| SRS | Software Requirements Specification |
| SSO | Single Sign-On |
| TLS | Transport Layer Security |
| ToT | Training of Trainers |
| TOR | Terms of Reference |
| UAT | User Acceptance Testing |
| UI | User Interface |
| VAT | Value Added Tax |



# 1. Background

Dhaka Electricity Supply PLC (DESCO) manages electricity distribution operations across several zones, circles, and divisions. DESCO requires a modern, transparent, data-driven mechanism to measure employee performance aligned with service delivery, customer satisfaction, revenue collection, fault response, project implementation, safety compliance, and digital transformation targets.

This initiative shall initially be implemented as a pilot project. During the pilot phase, the system shall operate independently, and the required data shall be entered manually or retrieved through available source-system APIs. Upon successful implementation, evaluation, and approval of the pilot project, DESCO may proceed with integration with the existing HRMS module to push finalized APR data.

To address these gaps, DESCO intends to implement an AI-based Performance Management and Digital Annual Performance Report (APR) System to transform the existing manual appraisal process into a structured, transparent, and evidence-based digital system.

The system shall digitize DESCO’s existing Annual Confidential Report (ACR)/Annual Performance Report (APR) process at the individual employee level, replicating — without altering unless separately approved by DESCO — the evaluation structure, criteria, and scoring scale of both ACR forms currently in use: the 20-criterion, 5-point-scale form for Grade 12–16 employees, and the 25-criterion, 4-point-scale form for Grade 1–11 employees.

The system shall enable reporting and supervising officers to record employees’ day-to-day achievements, contributions, performance deficiencies, and shortfalls throughout the appraisal period by data input. Based on these authorized inputs, relevant performance criteria, and available organizational data, the AI engine shall generate recommended performance marks and draft pen pictures for review, modification, and final approval by the designated reporting, countersigning, certifying (applicable in certain cases, per DESCO’s existing ACR guidelines), and approving authorities, consistent with DESCO’s existing multi-tier ACR approval hierarchy.

Where a reporting officer records a performance deficiency or shortfall, the system shall make this visible to the concerned employee at the time of entry (or at a configurable interval) and provide an opportunity for the employee to respond or improve before the item is carried into the final annual evaluation, consistent with DESCO’s existing ACR guidelines.

The system shall enforce the minimum-tenure rule from DESCO’s existing ACR guidelines: a reporting, countersigning, or certifying officer may evaluate an employee only where that officer has supervised the employee for a minimum of three (3) months during the appraisal period.

Where an evaluation contains an adverse remark, the system shall restrict disclosure to the concerned employee to the specific adverse portion only, consistent with DESCO’s existing confidentiality practice, rather than the complete report.

The system shall ensure:

- Complete digitization of DESCO’s existing APR process and appraisal forms, replacing the current dual-copy paper submission with a single digital record supported by a complete audit trail.
- Structured recording of employees’ day-to-day achievements, contributions, and shortfalls by their respective supervisors, by data input.
- AI-assisted generation of recommended APR marks based on recorded performance evidence, correctly applying the criteria set and scoring scale applicable to the employee’s grade tier.
- AI-assisted generation of objective and professionally worded pen pictures.
- Review, modification, approval, and override facilities for authorized officers.
- Preservation of human authority in all final appraisal decisions.
- Fair, consistent, transparent, and evidence-based performance evaluation.
Integration with DESCO’s existing source systems shall be limited to cases where a functional, accessible, and authorized API is available. Subject to API availability, the system will retrieve the following employee-related information:

- Promotion Effect on Personal Information
- Attendance records
- Training results and completion records
- Disciplinary actions and punishments awarded
- Awards, rewards, and recognition records
Where a source-system API is unavailable, the relevant data shall be entered manually by authorized users. During the pilot phase, the application shall only retrieve data and shall not push, write, modify, or update data in any existing DESCO system.

- Complete audit trails of performance inputs, AI-generated recommendations, modifications, approvals, and final evaluations.
- Real-time monitoring of appraisal progress, pending actions, and completion status.
- Improved employee accountability, motivation, professional development, and service delivery.

# 2. Objectives of the TOR

The primary objectives are:

- Align employee performance goals with DESCO’s Annual Confidential Report (ACR)/Annual Performance Agreement (APA) and management targets to ensure collective progress.
- Use AI and analytics to generate real-time insights, detect performance trends, and automatically calculate performance scores and grades in accordance with the applicable ACR scoring scale for each employee grade tier.
- Ensure fairness and transparency by reducing manual bias and using AI-based weighted evaluations.
- Boost efficiency and accountability with live dashboards, instant feedback, and automated reports that help management take timely actions.
- Promote a culture of continuous improvement and innovation through data-supported decision-making at the individual employee level.

# 3. Scope of Work


## 3.1 System Architecture Design

The core architectural principles guiding the development of the AIPMS include:

- Scalable and Modular Design: The system will be built using a micro-services architecture, which allows for greater flexibility, independent module updates, and the ability to scale specific functionalities as DESCO’s needs evolve.
- Intelligent AI Engine: At the heart of the system is an AI engine responsible for providing predictive scoring, performance forecasting, anomaly detection in evaluations, and data-driven recommendations.
- Secure, Role-Based Access: The system will incorporate modern authentication protocols, including Single Sign-On (SSO) and Two-Factor Authentication (2FA), to ensure users can only access data and functionalities appropriate to their roles.
- Mobile App Based Performance Input Module: Provides a mobile application for authorized management personnel, reporting officers, and supervisors. Enables recording of employees’ significant achievements, noteworthy contributions, performance shortfalls, and relevant observations during the APR year.
- Bilingual Interface: To ensure accessibility for all users across the organization, the system will fully support both Bangla and English interfaces for all modules and functionalities.

## 3.2 System Modules

The AI-Based Performance Management System (AIPMS) is designed as a modular, scalable, and interoperable platform to support DESCO’s individual-level performance management process, fully replicating the structure and scoring logic of the existing ACR/APR forms for Grade 1–11 and Grade 12–16 employees.


### 3.2.1 Core Performance Modules


### 3.2.1.1 Guiding Principles for Performance Evaluation

In designing and implementing the Performance Evaluation framework under AIPMS, the following guiding principles shall be adhered to:

- a) Grade-Tier-Specific KPI and Scoring Design: The system shall replicate, without alteration, the evaluation criteria and scoring scale defined in DESCO’s existing ACR forms for each grade tier — the 20-criterion, 5-point-scale form for Grade 12–16 employees, and the 25-criterion, 4-point-scale form for Grade 1–11 employees — including the associated performance bands (Extraordinary: 95–100; Excellent: 85–94; Good: 75–84; Satisfactory: 60–74; Below Satisfactory: below 60). Any future change to criteria or weightages shall require a change request approved by DESCO.
- b) Mitigation of Behavioral and Psychological Bias: Performance evaluations, particularly those conducted on an immediate or event-driven basis, may be susceptible to the influence of temporary emotional states or negative attitudes, which can compromise the objectivity of assessment. Accordingly, the system design and implementation shall incorporate appropriate controls and mechanisms to mitigate psychological and behavioral bias, ensuring balanced, evidence-based, and objective evaluation.
- c) Strategic Alignment through Evaluation Approach: The performance evaluation framework may adopt a Top-down Approach in preference to a Bottom-up Approach, in order to ensure alignment with organizational goals, strategic priorities, and institutional objectives, and to promote a result-oriented, transparent, and motivational performance assessment system.

### 3.2.1.2 KPI Engine & Performance Framework Module

- Configures individual KPIs aligned with APA and corporate strategy, applying the criteria set and scoring scale applicable to the employee’s grade tier.
- Manages KPI templates, weight distribution, and evaluation cycles.
- Supports monthly, quarterly, and annual KPI calculation.
- Enables target vs. actual variance analysis and year-to-year comparison.
- Validates that a reporting, countersigning, or certifying officer has supervised the employee for a minimum of three (3) months before permitting an evaluation to be initiated, per DESCO’s ACR guidelines.

### 3.2.1.3 Individual Level Performance Module

- KPIs and corresponding weightages shall be defined based on individual job descriptions to ensure role-specific, objective, and measurable performance evaluation.
- Manages employee KPIs, competencies, and behavioral indicators.
- Integrates attendance, task completion, disciplinary, and training data.
- Supports supervisor evaluation and structured self-input of achievements (see Section 3.2.3.1).
- Automates ACR/APR generation following DESCO’s existing formats for both grade tiers.

### 3.2.2 AI-Driven Performance & Analytics Modules


### 3.2.2.1 AI Performance Scoring & Analytics Module

- Provides AI-based rating recommendations and consistency checks, correctly applying the criteria and scale for the employee’s grade tier.
- Performs past vs. current performance analysis and peer comparison (department/division-wise, as an aggregation of individual scores).
- Includes predictive analytics for attrition risk, training needs, and future performance.
- Anomaly detection for irregular ratings.

### 3.2.2.2 Core AI & Data Analytics Features

The system must include:

- Bias Detection & Fairness: Statistical tests (regression, disparity metrics) and ML fairness metrics (demographic parity, disparate impact, equal opportunity); rule-based and model-based anomaly detection for evaluator behavior (leniency, severity, recency, halo); per-evaluator bias scores and flagged cases with supporting evidence.
- Scoring & Predictive Models: AI weight computation fusing KPI data, sentiment, past performance, attendance, and training history into composite scores; predictive models to forecast next-period performance or risk of underperformance; confidence estimates and calibrated probabilities.
- Explainability & Bias Dashboard: A dedicated interface, available to authorized HR, evaluators, and auditors, exposing the rationale behind each AI-recommended score and pen picture (contributing factors and their relative weight), alongside aggregate fairness and bias metrics across evaluators, departments, and grade tiers, consistent with the validation requirements of Section 3.8(b) and delivered per Section 6.2.
- Security & Privacy: Data encryption (Name, NID, Birth Certificate) in transit and at rest, role-based access, and audit logging; support for pseudonymization/anonymization in training pipelines where required; compliance with Government of Bangladesh (GoB) data protection norms and DESCO’s applicable information security policy.

### 3.2.3 Evaluation & Feedback Modules


### 3.2.3.1 Employee Self-Input Module

- Enables employees to enter their achievements and work completed during the appraisal period, as structured factual input rather than a self-rating or self-score.
- Supports document and evidence upload.
- Promotes transparency and ownership in the appraisal process.

### 3.2.3.2 Employee’s Health Assessment Module

The module shall support two related but distinct functions:

- (i) Annual Health Examination Digitization — digitizes the fields currently captured on the ACR form: height, weight, eyesight, blood group, blood pressure, X-ray report, ECG report, medical classification, and nature of any health weakness/incapacity, to be completed by the designated Health Officer as part of the annual ACR cycle.
- (ii) Ad-hoc Health Concern Workflow (scope to be confirmed) — allows employees, supervisors, or authorized HR personnel to raise a health-related concern, assign a DESCO-appointed doctor, record the assessment, and maintain findings in the employee’s confidential health record, with role-based access and audit trail. This is additional functionality beyond base ACR digitization and shall be confirmed with DESCO as in-scope or out-of-scope for the pilot.

### 3.2.3.3 Supervisor & Reviewer Evaluation Module

- Allows supervisors and reviewers to provide qualitative and quantitative feedback.
- Integrates AI-based consistency checks to ensure fairness.
- Supports a configurable, conditional approval workflow matching DESCO’s existing hierarchy: Reporting Officer → Countersigning Officer → Certifying Officer (applicable in certain cases only, per DESCO’s ACR guidelines) → Approving Officer.
- Where an evaluation includes an adverse remark, restricts disclosure to the employee to the specific adverse portion only.
- Supports the recommendation section matching the existing ACR form, including training/skill-development recommendations and promotion-eligibility categorization (eligible / not yet eligible / at maximum eligibility limit / recently promoted, pending further review).

## 3.3 Training, Reward, Attendance & Compliance Data Modules


### 3.3.1 Training Data Module

- Enables authorized users to enter employees’ training information for the relevant APR year.
- Retrieves training data through API integration where the source system provides an API.
- Maintains records of training programs attended, completed, or pending during the appraisal period.
- Provides verified training data to the AI engine for generating recommended APR marks and draft pen pictures.

### 3.3.2 Reward & Recognition Data Module

- Enables authorized users to enter employees’ rewards, recognitions, commendations, and notable achievements for the relevant APR year.
- Retrieves reward and recognition data through API integration where the source system provides an API.
- Maintains records of awards, incentives, commendations, and other official recognition received during the appraisal period.
- Provides verified reward and recognition data to the AI engine for generating recommended APR marks and draft pen pictures.

### 3.3.3 Attendance Data Module

- Enables authorized users to enter employees’ attendance information for the relevant APR year.
- Retrieves attendance data through API integration where the source attendance system provides an API.
- Maintains relevant attendance information, including presence, absence, late attendance, leave, and other approved attendance-related records.
- Provides verified attendance data to the AI engine for generating recommended APR marks and draft pen pictures.

### 3.3.4 Compliance & Discipline Data Module

- Enables authorized users to enter employees’ compliance and disciplinary information for the relevant APR year.
- Retrieves compliance and disciplinary data through API integration where the source system provides an API.
- Maintains records of warnings, disciplinary actions, compliance issues, penalties, and final decisions taken during the appraisal period.
- Only finalized and authorized disciplinary records shall be considered for APR assessment.
- Provides verified compliance and disciplinary data to the AI engine for generating recommended APR marks and draft pen pictures.

### 3.3.5 Common Data Processing Requirement

Data under these modules shall be collected either through authorized manual data entry or through API integration, subject to the availability of APIs in the respective source systems. The AI engine shall analyze the available training, reward and recognition, attendance, compliance, disciplinary, achievement, and shortfall data to generate recommended APR marks and draft pen pictures for review and approval by the authorized officers.


## 3.4 Mobile App-Based Performance Input Module

- Provides a mobile application for authorized management personnel, reporting officers, and supervisors.
- Enables recording of employees’ significant achievements, noteworthy contributions, performance shortfalls, and relevant observations during the APR year.
- Captures employee details, date, category, description, and remarks for each entry.
- Supports uploading relevant documents or supporting evidence, where applicable.
- Securely stores all recorded information with user identification and timestamps.
- Uses the recorded data as input for AI-assisted generation of recommended APR marks and draft pen pictures.
- Allows authorized officers to review, modify, and approve AI-generated marks and pen pictures.
- Maintains a complete audit trail of data entry, modification, review, and approval activities.

## 3.5 Data Workflow & Communication


### 3.5.1 Document & Workflow Automation Module

- Generates ACR/APR forms, evaluation reports, promotion summaries, and training analysis.
- Provides configurable approval workflows.

### 3.5.2 Notification & Communication Module

- Multi-channel notifications (SMS, email, portal alerts).
- Automated reminders for deadlines, pending approvals, and performance meetings.
- Template-driven communication with rule-based triggers.

## 3.6 Dashboard & Reporting Modules


### a. Real-Time Dashboard Module

Role-based dashboards for:

- Employees
- Reporting Officers / Evaluators
- Countersigning Officers
- Certifying Officers
- Approving Officers
- HR
- Top Management
Features include KPI trends, heat maps, forecasts, and drill-down analytics on individual performance data, aggregated by department where required for reporting purposes only (see 3.6(c)).


### b. Executive & HR Reporting Module

Provides senior management and HR with consolidated, analytical, and decision-support reports derived from individual performance data aggregated at department and organization level for reporting purposes.

- Organization-wide and departmental performance summaries, derived by aggregating individual employee scores (not independently configured departmental/organizational KPIs).
- Departmental and individual performance comparison, ranking, and distribution reports.
- AI-generated fairness, bias, and anomaly audit reports.
- Promotion, increment, incentive, and training-need analysis reports.
- Standardized and ad-hoc reports exportable in PDF and Excel formats.
- Role-based access control, data confidentiality, and full audit trail.

### c. Departmental Performance Aggregation Dashboard

- Displays department-wise aggregation of individual employee KPI achievement (not a separately configured departmental KPI).
- Drill-down from department to division/section/unit to individual employee level.
- AI-generated insights, alerts, and performance forecasts based on aggregated individual data.
- Monitoring of evaluation progress, attendance, and compliance indicators.
- Standardized reports with export facilities (PDF/Excel).
- Role-based access control and management.

### d. Employee Self-Service Dashboard

- Access to personal KPIs, ratings, comments, and training history.
- Visual insights on strengths, weaknesses, and AI-driven improvement suggestions.
- Display of individual KPI targets, weightages, and achievement status for the active evaluation cycle.
- Visual performance indicators (scorecards, progress bars, trend lines).
- Comparison of current performance against previous evaluation periods.
- Color-coded alerts for underperforming or high-achievement areas.

## 3.7 Security, Governance & Administration


### a. Security, Access Control & Audit Module

- Role-Based Access Control (RBAC) with granular permissions.
- Field-level redaction control, ensuring only the relevant adverse-remark excerpt (not the full report) is disclosed to an employee, where applicable.
- Data security with AES-256 encryption (Name, NID, and Birth Certificate information) at rest and TLS 1.2+ in transit.
- Complete audit logs of user actions, AI decisions, overrides, and configurations.

### b. Configuration & System Administration Module

- Manages KPI templates, scoring formulas, evaluation cycles, and AI thresholds.
- Controls organizational hierarchy, user roles, and system parameters.
- Provides centralized system governance and operational control.

## 3.8 Software and AI Model Testing & Validation

The vendor shall design, execute, and document a structured testing and validation program covering both conventional software quality assurance and AI-model-specific validation, prior to each Go-Live and on an ongoing basis during the pilot.


### a. Software Testing

- Functional testing of all modules against the SRS, explicitly covering both ACR grade-tier rubrics (the 20-criterion/5-point scale for Grade 12–16 and the 25-criterion/4-point scale for Grade 1–11).
- Non-functional testing: performance/load testing under a concurrent-user load representative of DESCO’s workforce; security testing (vulnerability assessment/penetration testing aligned with Section 5.2); and usability testing of the bilingual (Bangla/English) and mobile-responsive interfaces.
- System Integration Testing (SIT): verifying integration between core modules (KPI engine, AI scoring, self-input, health, supervisor/reviewer, dashboards) and, where applicable, with source-system APIs (Section 4).
- User Acceptance Testing (UAT): conducted jointly by DESCO’s designated HR and ICT personnel with vendor support (Section 7.2), using test cases that explicitly exercise both grade-tier rubrics, the conditional certifying-officer step, the minimum 3-month tenure validation, and adverse-remark redaction (Section 3.2.3.3).
- Regression testing prior to each release or configuration change, including changes to KPI criteria or weightages.

### b. AI Model Testing & Validation

- Accuracy & Agreement Validation: benchmarking AI-recommended scores against manually calculated scores on a representative historical or shadow sample, evaluated separately for each grade tier, against a minimum agreement/accuracy threshold to be agreed with DESCO prior to pilot Go-Live.
- Bias & Fairness Testing: validating the bias-detection features described in Section 3.2.2.2 using recognized fairness metrics (e.g., demographic parity, disparate impact) across evaluators and departments, prior to and periodically throughout the pilot.
- Explainability Validation: confirming that the Explainability & Bias Dashboard (Section 3.2.2.2) produces clear, human-interpretable justifications for each AI-recommended score and draft pen picture.
- Robustness Testing: testing model behavior against incomplete, missing, or edge-case input data (e.g., an employee with no recorded training history, or exactly 3 months’ tenure) to confirm graceful handling rather than erroneous or unexplained scores.
- Human-Override Monitoring: tracking the rate and pattern of cases where reporting, countersigning, certifying, or approving officers override or materially modify an AI-recommended score or pen picture during the pilot, as an input to model tuning and to DESCO’s pilot evaluation.

### c. Model Revalidation & Change Control

- Any change to KPI criteria, weightages, or grade-tier rubrics (Section 3.2.1.1) shall trigger revalidation of the affected AI model(s) before redeployment.
- Model versions shall be tracked under the MLOps setup (Section 6.2), with the ability to roll back to a prior validated version.

### d. Acceptance Criteria for Go-Live

- All Critical and High severity defects identified during SIT/UAT shall be resolved and re-tested prior to Go-Live; Medium/Low severity defects may be deferred into the post-handover support period (Section 7.6) subject to DESCO’s written agreement.
- UAT sign-off shall be obtained jointly from DESCO’s HR and ICT teams, evidenced in the Test Plan, Test Cases, and SIT/UAT Sign-off Report (Section 6.1), as a precondition for release of Payment Milestone 3 (Section 10).

# 4. Integration Requirements

Integration with DESCO’s existing source systems shall be limited to cases where a functional and accessible API is available. Subject to API availability, the system may retrieve the following employee-related data:

- Promotion Effect on Personal Information
- Attendance records
- Training results and completion records
- Disciplinary actions and punishments awarded
- Awards, rewards, and recognition records
Where a source-system API is unavailable, the relevant data shall be entered manually by authorized users.


# 5. Technical Requirements


## 5.1 Technology Stack

- Web-based platform
- Mobile-responsive UI
- Backend: Java Spring Boot
- Frontend: React
- Database: Oracle/PostgreSQL
- AI/ML engine: Python, TensorFlow
- API: RESTful API
- On-premise deployment (with Cloud/On-premise deployment flexibility)

## 5.2 Security

- Compliance with ISO/IEC 27001 information security management practices.
- Role-based access control (RBAC).
- Data encryption (AES-256) for sensitive personal fields (Name, NID, Birth Date) at rest and in transit.
- Audit trails.
- Two-factor authentication.

# 6. Deliverables

This section outlines all the tangible items that will be delivered to DESCO upon the successful completion of the project. A Project Implementation Unit (PIU) from DESCO will take over the Deliverables as per scope of TOR. Each deliverable is mapped to the phase in which it is produced (Section 7.1) and, where applicable, to the corresponding payment milestone (Section 10).


## 6.1 Documentation

- Inception Report and Project Management Plan (PMP): Detailing the final project scope, plan, and schedule. [Phase 1]
- System Requirement Specification (SRS): A comprehensive document outlining all functional and non-functional requirements. [Phase 2]
- System Design Document (High-Level Design and Software Design Description): The complete technical architecture and design specifications. [Phase 2]
- KPI Framework Documentation: A guide to the configured KPIs, evaluation criteria, and scoring logic for both ACR grade tiers (Grade 1–11 and Grade 12–16). [Phase 2]
- Test Plan, Test Cases, and SIT/UAT Sign-off Report: Documenting System Integration Testing and User Acceptance Testing conducted jointly with DESCO’s HR and ICT teams, and formal sign-off prior to Go-Live, per the testing and validation requirements of Section 3.8 and the training arrangements in Section 7.2. [Phase 3]
- Information Security & Compliance Report: Documenting implementation of RBAC, AES-256 field-level encryption, audit-trail configuration, and alignment with ISO/IEC 27001 (or the agreed equivalent standard) per Section 5.2. [Phase 3]
- AI Model Validation Report: Documenting accuracy/agreement results, bias and fairness testing, explainability validation, and robustness testing for the AI scoring engine, per Section 3.8(b). [Phase 3]
- User Manual & Admin Manual: Detailed guides for end-users, supervisors/evaluators, and system administrators, covering both the web platform and the mobile application. [Phase 3–4]

## 6.2 Software and Source Code

- Fully Developed System: The production-ready AIPMS web platform, tested and deployed on DESCO’s main server. [Phase 3]
- Mobile Application: The production-ready mobile application for performance data input (Section 3.4), including installable builds and complete source code. [Phase 4]
- Complete Source Code: The full, unencumbered source code for all system modules (web and mobile), delivered as part of project handover per Section 7.3. [Phase 3–4]
- UI Mockups & Prototypes: All design assets, user interface mockups, and interactive prototypes created during the development process. [Phase 2–3]
- Deployment & Configuration Scripts: All scripts required for system deployment and maintenance. [Phase 3]
- AI Assets:
- Trained Models: The production-ready machine learning models for predictive scoring and related source code.
- Explainability & Bias Dashboard: A functional dashboard for auditing AI-driven decisions and monitoring fairness metrics.
- MLOps Setup: The complete CI/CD pipelines, model registry, and monitoring framework for managing the AI model lifecycle.

## 6.3 Data Assets

- Labeled and Annotated Datasets: The complete datasets used for training, validating, and testing the AI models. [Phase 3]
- Annotation Guidelines: The documentation outlining the procedures and standards used for data labeling. [Phase 3]

## 6.4 Training & Handover Deliverables

- Training Curriculum & Materials: Course content and materials for the Training of Trainers (ToT) and hands-on end-user training tracks described in Section 7.2. [Phase 5]
- Video Tutorials: Recorded, bilingual (Bangla/English) walkthroughs covering core user journeys (self-input, evaluation, approval workflow, dashboards). [Phase 5]
- Training Attendance & Completion Records: Records confirming participation and completion for all trained personnel. [Phase 5]
- Handover Report: Confirming transfer to DESCO’s ICT and HR teams of all source code, technical documentation, AI models, and reproducible model-retraining recipes, per Section 7.3. [Phase 5]
Where a deliverable in this section is also listed as a payment milestone in Section 10, submission and DESCO’s acceptance of that deliverable is a precondition for release of the corresponding payment.


# 7. Implementation, Training, and Support Plan

A successful implementation extends beyond the deployment of technology; it requires a comprehensive plan for training, knowledge transfer, and ongoing support to ensure widespread user adoption and long-term project success.


## 7.1 Phase-wise Implementation Plan (6 Months)

The system shall be implemented in the following phases, targeting Go-Live and completion of training within 6 months of contract signing. The post-handover support period (Section 7.6) runs separately, commencing after handover (Phase 5), so that the total project duration — implementation plus support — fits within 12 months.



| Phase | Focus | Timeline | Key Activities | Milestone / Payment |
| --- | --- | --- | --- | --- |
| Phase 1 | Inception & Requirement Finalization | Month 1 | Kickoff meeting; stakeholder consultation; validation of both ACR grade-tier forms and business rules (tenure check, redaction, conditional certifying step); confirmation of Health Module scope. | Inception Report & PMP approved (10%) |
| Phase 2 | Design | Month 2–3 | SRS, HLD, SDD; non-functional prototype; KPI/scoring-rubric mapping for both grade tiers; approval-workflow and dashboard design. | SRS/HLD/SDD approved (10%) |
| Phase 3 | Core Development, Testing & Pilot | Month 3–5 | Build KPI engine, AI scoring & analytics, self-input, health, supervisor/reviewer, dashboard, and security modules; SIT/UAT; piloting of HR & Training Modules; Go-Live on main server. | UAT complete; pilot Go-Live (40%) |
| Phase 4 | Mobile Application (parallel) | Month 3–5 | Design, build, and test the mobile application for performance data input. | Mobile app delivered (15%) |
| Phase 5 | Training & Rollout | Month 5–6 | 1. Training of Trainers (10 personnel, 03 days); <br>2. Hands-on training for HR-associated personnel (10 personnel, 05 days, run in parallel with ToT); video tutorials and materials; feedback incorporation;<br>3. Technology and knowledge handover (10 personnel, 12 days). | Training complete; system handed over (20%) |
| Phase 6 | Post-Handover Support | Month 6–12, 6 months (outside the 6-month implementation window) | Quarterly maintenance and support following successful handover (Phase 5), source-code submission, and acceptance by DESCO; DESCO may extend based on pilot-evaluation outcome. | Payable quarterly (5%) |



## 7.2 System Training and Knowledge Transfer

A tailored training program shall be conducted for distinct user groups to ensure all personnel are proficient in using the new system:

- HR and IT Administrators: In-depth training on system configuration, administration, security management, and report generation. This will be Training of Trainers (ToT): 10 DESCO personnel for 03 days.
- General Employees and Supervisors: Practical, hands-on training focused on navigating the user interface, setting KPIs, conducting self-input of achievements, and providing feedback. 10 DESCO personnel associated with HR, conducted in a minimum of single batches for 05 days.
- ICT Personnel: Specialized technical training covering the system’s architecture, development framework, database structure, deployment procedures, source code, AI ML model related knowledge base  and maintenance protocols.
Training shall be conducted in phases following successful development of the system, sequenced after User Acceptance Testing (UAT) is complete (see Section 7.1, Phase 3). The training plan shall consider participants’ ICT literacy, professional expertise, organizational requirements, and convenience.

User Acceptance Testing is a separate activity from training and shall be conducted jointly by DESCO’s designated HR and ICT personnel, with vendor support, prior to Go-Live, to confirm the system meets the requirements set out in this TOR before final acceptance.


## 7.3 Knowledge Transfer and Handover

A complete and transparent handover process is a critical project milestone. This includes the transfer of all project assets to DESCO’s ICT and HR teams, ensuring they are fully equipped to manage and evolve the system independently. The handover will include all source code, technical documentation, AI models, and the reproducible training recipes required to retrain or update the models in the future, for 10 DESCO personnel over 12 days.


## 7.4 Training Cost Responsibilities

All training-related expenses shall be borne by the selected firm. The expenses shall include:

- Food and refreshments
- Training materials
- Remuneration of Trainees

## 7.5 Training Venue

Training venue will be provided by DESCO.


## 7.6 Technical Support

A 06 (Six) Month period of post-deployment technical support shall commence immediately following successful handover of the system (Phase 5, Section 7.1), to ensure smooth system operation and address any issues arising during the pilot. Given the pilot nature of this project, DESCO may, at its discretion, extend the support period based on the outcome of the pilot evaluation.


# 8. Resource Requirements

To ensure the successful execution of this project, the vendor shall deploy a cross-functional team of qualified experts. The minimum academic qualification, minimum relevant experience, and key skills/certifications expected for each role are set out below. The vendor shall name specific individuals against each role in its technical proposal, along with CVs demonstrating compliance with these criteria; DESCO reserves the right to interview or request substitution of any proposed team member.



| Role | Minimum Academic Qualification | Minimum Relevant Experience | Key Skills / Certifications (Preferred) |
| --- | --- | --- | --- |
| Project Manager | Bachelor's degree in CSE/Software Engineering/IT or Business Administration (Master's preferred) | Minimum 8 years in IT project management, including at least 3 years managing enterprise HR/ERP or public-sector software implementations | PMP or PRINCE2 certification preferred; experience coordinating multi-vendor/stakeholder government ICT projects |
| System Architect | Bachelor's degree in CSE/Software Engineering (Master's preferred) | Minimum 10 years in software architecture and design, including at least 3 years designing micro-services/cloud-based enterprise systems | Experience architecting large-scale, multi-role, workflow-driven systems; cloud/on-premise deployment experience |
| HR Domain Specialist | Bachelor's/Master's degree in Human Resource Management or related field | Minimum 5 years of experience in HR systems or performance-appraisal processes, preferably including grade-tiered appraisal/ACR-APR type systems | Familiarity with public-sector or utility-sector HR practices in Bangladesh preferred; experience translating HR policy into system business rules |
| AI/ML Specialist(s) | Bachelor's/Master's degree in Computer Science, Data Science, or Artificial Intelligence | Minimum 5 years of hands-on machine learning model development, including experience with predictive analytics and bias/fairness detection in ML models | Proficiency in Python and TensorFlow (or equivalent); experience building explainable/auditable AI systems |
| Backend Developer(s) | Bachelor's degree in CSE or related field | Minimum 4 years of backend development experience using Java Spring Boot or an equivalent enterprise framework | RESTful API design and development; experience with role-based access control and audit-logging implementation |
| Frontend Developer(s) | Bachelor's degree in CSE or related field | Minimum 3 years of frontend development experience using React/Next.js or an equivalent modern framework | Experience building bilingual (Bangla/English) and mobile-responsive interfaces preferred |
| Database Administrator / Data Engineer | Bachelor's degree in CSE or related field | Minimum 4 years of database administration/data engineering experience, including PostgreSQL | Experience implementing field-level encryption (e.g., AES-256) and secure data-migration practices |
| Information Security Specialist | Bachelor's/Master's degree in Computer Science or Cybersecurity | Minimum 4 years of information security experience | Experience with ISO/IEC 27001 (or equivalent) implementation, RBAC design, and encryption/audit-trail systems; relevant security certification (e.g., CISSP, CEH) preferred |
| QA & Test Engineer(s) | Bachelor's degree in CSE or related field | Minimum 3 years of software QA/testing experience, including coordination of User Acceptance Testing (UAT) | Experience with automated testing frameworks and defect-tracking tools |
| Training & Change Management Specialist | Bachelor's/Master's degree in a relevant field | Minimum 4 years of experience delivering enterprise software training and organizational change management, preferably for HR system rollouts | Strong facilitation skills in both Bangla and English; experience developing training materials and video tutorials |


This team structure ensures that all aspects of the project — from technical architecture and AI development to HR-domain accuracy, security, and user adoption — are managed by appropriately qualified and experienced personnel. Roles may be combined where a single individual demonstrably meets the qualification and experience criteria for more than one role, subject to DESCO’s approval.


# 9. Governance, Compliance, and Intellectual Property

This project will be executed in strict accordance with all relevant legal and regulatory frameworks governing public sector ICT projects in Bangladesh. The highest standards of governance and compliance shall be upheld throughout the project lifecycle.

The following commitments will be formally observed:

- Regulatory Adherence: The project will maintain full compliance with the Government of Bangladesh’s national ICT policy and any other applicable regulations.
- Data Protection: The system will be designed and operated in accordance with all applicable data protection regulations to safeguard sensitive employee information.
- Intellectual Property: Upon project completion and final acceptance, all intellectual property rights for the developed system — including the complete source code, documentation, and AI models — will be fully and exclusively vested in Dhaka Electricity Supply PLC (DESCO).

# 10. Payment Schedule

The payment milestones below correspond directly to the phases defined in the Phase-wise Implementation Plan (Section 7.1), so that each payment is tied to a specific, verifiable phase completion rather than a standalone date.



| SL | Deliverables/Reports | Phase (Sec. 7.1) | Time of Submission/Demonstration | Payment |
| --- | --- | --- | --- | --- |
| 1 | Inception Report and Project Management Plan | Phase 1 | After 1 month from the date of contract signing | 10% |
| 2 | Software Requirements Specification (SRS), Non-functional Prototype, High-Level Design (HLD), and Software Design Description (SDD) | Phase 2 | Within 2 months after approval of the Inception Report and Project Management Plan (by end of Month 3) | 10% |
| 3 | Core module development, System Integration Testing (SIT), User Acceptance Testing (UAT) sign-off jointly by DESCO’s HR and ICT teams (see Section 7.2), piloting of the HR and Training Modules, and Go-Live on the main server | Phase 3 | Within 2 months after approval of the SRS & SDD (by end of Month 5) | 35% |
| 4 | Development and delivery of the Mobile Application | Phase 4 | Within 2 months after approval of the SRS & SDD (by end of Month 5) | 15% |
| 5 | Training for key stakeholders, Training of Trainers (ToT), hands-on training, video tutorials, training materials, and feedback incorporation | Phase 5 | Within 1 month after project Go-Live (by end of Month 6) | 20% |
| 6 | Maintenance and support services for 06 months following successful system handover, source-code submission, and acceptance by DESCO | Phase 6 | Payable after maintenance and support period (by end of Month 12) | 10% |
|  | Total |  |  | 100% |



## 10.1 Method of Payment

All payments shall be made in Bangladeshi Taka (BDT) upon completion, submission, validation, and acceptance of the respective deliverables, subject to:

- Submission and acceptance of the Inception Report, SRS, SDD, developed software, SIT/UAT sign-off, training deliverables, and successful Go-Live.
- Validation and approval by DESCO’s designated Project Implementation Unit (PIU).
- Deployment of the project team in accordance with the qualification and experience criteria set out in Section 8, or substitutes approved in writing by DESCO.
- Deduction of applicable VAT and taxes in accordance with prevailing laws and regulations.
Where DESCO extends the post-deployment technical support period beyond the 06 months referred to in Section 7.6, payment terms for the extended period shall be agreed separately between DESCO and the vendor.
