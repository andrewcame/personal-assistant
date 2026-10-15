---
id: CH-05
type: challenge
status: resolved
horizon: none
updated: 2026-10-15
pillars: [P1]
focus: [people]
goals: []
links: []
people: [TMW, DA, MP, KB, JS, JFG, LM]
---

# Challenge 05 — QA Growth Headroom, Stagnation, And Talent Pipeline

---

## Context

The QA department has an established 8-level grading structure under the QA Rating Model:

- **Level 1 / 2:** Graduate & Junior QA Engineer (QA-1, QA-2) — entry-level pipeline
- **Level 3 / 4:** QA Engineer & QA Engineer II (QA-3, QA-4) — core practitioners (e.g., JS, JFG)
- **Level 5 / 6:** Senior QA Engineer & Senior QA Engineer II (QA-5, QA-6) — specialist senior practitioners (e.g., KB at Level 6)
- **Level 7:** Lead QA Engineer (QA-7) — domain/platform quality owners (as at 2026-10-08: TMW in Website (Web Team 2), DA in Website, MP in Payments; TMW moved from App, so App no longer has a Level 7 owner — see [team roster](../team/README.md))
- **Level 8:** Staff QA Engineer (QA-8) — the deepest quality engineering anchor within a platform, owning the hardest automation and quality architecture problems while multiplying capability across the function

The current team distribution presents structural career bottlenecks at both the top and bottom of the department pyramid:

1. **Ceiling for Lead QAs (Level 7):**
   - The three Lead QAs each own a distinct domain within the Pico estate (Mobile App, Website, Payments).
   - The only upward progression path for them is **Staff QA Engineer (Level 8)**, but the Staff specification describes a change in impact rather than simply a larger platform remit: the Staff engineer owns the hardest problems, sets the quality ceiling, builds reusable utilities and infrastructure, mentors Leads and senior engineers, and may line-manage a small number of practitioners.
   - Stepping from Level 7 to Level 8 is a substantial leap: requiring Level 5 (Strategise) in Technical, Collaboration, and AI, Level 4 (Manage) in Leadership, and Level 3 (Mentor) in People Management.
   - Without clear platform-level problems with multiplier potential and explicit cross-team opportunities through the QA chapter, reaching Staff level is difficult to evidence, leaving Leads feeling capped.

2. **Lead Bottleneck for Senior II (Level 6):**
   - For a Senior QA Engineer II (KB), the immediate next step is **Lead QA Engineer (Level 7)**.
   - Because the three domain Lead positions are already occupied, there is no obvious vacant Lead post unless an existing Lead steps up to Staff, moves laterally, or exits.
   - Without an alternative technical lead/specialist route that doesn't require displacing an incumbent or taking on people management, this creates a dead end for high-performing seniors.

3. **Missing Junior Pipeline (Levels 1–2):**
   - The department currently has no Graduate (Level 1) or Junior (Level 2) engineers.
   - Without an entry-level talent pipeline, there is no natural backfill mechanism when engineers progress or move on, making recruitment reactive and expensive.

4. **Longstanding Tenures & Stagnation Risks:**
   - Most QA engineers in the organisation are longstanding and have been static in their current roles and bands for extended periods.
   - Prolonged stagnation creates pent-up expectations for promotion. When engineers seek progression simultaneously in a top-heavy, bottlenecked structure, it creates friction between individual career ambitions and organisational capacity.

---

## Challenge

As the QA & Test Engineering Manager, how do I:

- Create meaningful progression pathways and growth headroom for longstanding engineers without manufacturing artificial promotions or title inflation
- Define clear, achievable criteria for Lead QAs (Level 7) to build and demonstrate Staff-level (Level 8) impact across engineering
- Provide viable next steps for Senior QA II (Level 6) practitioners that avoid structural dead ends, exploring both domain lead and senior individual contributor / technical specialist tracks
- Re-energise and motivate static, longstanding team members who feel their career progression has stalled
- Establish a healthy bottom-up talent pipeline (Graduate/Junior) that supports succession planning, cost efficiency, and team sustainability

---

## Questions To Explore

### Headroom And Staff Level (Level 7 → Level 8)
- What platform-level problems are sufficiently difficult and valuable to provide a legitimate Staff QA scope?
- Can a Lead demonstrate Staff impact by setting the quality ceiling for their platform, building reusable utilities or infrastructure, and making other QAs and engineers faster and more confident?
- Which opportunities should extend beyond the platform through the QA chapter, cross-team collaboration, shared standards, and mentoring of other Leads or senior engineers?
- How much day-to-day platform ownership and line management should remain with a Staff QA, and what should transfer to the Manager or Lead roles?
- Is there room in the organisation for one or more Staff QA roles, and what business justification is required?

### Senior II Progression & Role Design (Level 6 → Level 7)
- Does Level 7 (Lead QA Engineer) require the full combination of platform ownership, line management, test architecture, and squad quality voice described in the role spec, or can a specialist technical lead track exist under the framework?
- How do we support KB's progression toward Lead without requiring an existing Lead to vacate their post?
- How do we support JS's stated aspiration toward a supportive Lead QA Engineer role when she does not want the QA manager role?
- Can domain scope be shared, rotated, or expanded (e.g., cross-cutting E2E / integration leadership, preview tooling) to create legitimate Lead-level scope without inventing a title?
- What observable evidence would demonstrate that DA is operating at Staff level, including active Website/Web 3 ownership, cross-platform influence, and function-wide quality improvement?

### Mitigating Stagnation & Reigniting Growth
- How do we assess the competency baselines of longstanding engineers against the Growth Framework objectively?
- Where engineers have plateaued in pay or band, what non-promotional growth levers (e.g., high-visibility projects, new technology exploration, mentoring, chapter leadership) can renew motivation?
- How do we manage expectations transparently so team members understand that promotion requires sustained evidence of next-level behaviours, not just time served?
- What leadership development options, such as a leadership cohort, are available to practitioners who want to lead through support and influence rather than line management?
- How should promotion expectations be communicated transparently against the competency framework and agreed evidence?
- What evidence should JFG provide for Senior QA progression beyond strong backend technical capability, particularly in communication, meeting participation, and front-end ownership?

### Talent Pipeline & Succession
- What is the business case for introducing Junior / Graduate QA roles (Levels 1–2) into squads?
- How could bringing in junior engineers free up senior capacity for higher-leverage architecture and enablement work?
- How do we balance squad delivery velocity with the coaching and onboarding capacity required for junior engineers?

---

## Initial Position

Progression must be grounded in observable impact and demonstrated competency against the Growth Framework, never awarded merely as a reward for tenure. However, a management model that leaves talented people feeling stuck in dead ends will inevitably lead to disengagement or attrition.

We must address both ends of the pyramid:
1. **Clarify the Staff QA (Level 8) pathway:** Define difficult platform problems with multiplier potential (e.g., Pico test architecture, staging resilience, agentic AI testing, shared test infrastructure) that give Level 7 Leads a legitimate canvas to build Staff-level evidence. Staff scope should be anchored in deep platform accountability and measurable leverage, then extended through chapter influence and mentoring, rather than defined only as vague function-wide seniority.
2. **Clarify Lead QA (Level 7) expectations:** Use the Lead specification as the baseline: platform test architecture, line management, upstream quality influence, AI adoption, test debt and NFR ownership, flow discipline, and shared quality ownership. Differentiate those expectations from Staff-level multiplier impact so strong Senior IIs (Level 6) have a credible path to Level 7 that does not depend on unseating peers.
3. **Build the case for entry-level hiring:** Advocate for Junior/Graduate QA roles to rebalance the pyramid, establish succession pathways, and allow senior engineers to develop coaching and mentoring competencies.
4. **Honest, growth-focused 1:1 conversations:** Use the initial discovery and 30-day baseline period to understand each engineer's personal aspirations, reset expectations objectively against the competency rubric, and co-design tailored development plans.

---

## 2026-10-15 Resolved For Now

- KB's move to App lead opens his growth route. Other QAs have routes to Senior within their current teams.
- The remaining headroom question is the Staff QA route for the two Website Lead QAs (TMW, DA). If one reaches Staff, they step up and the other leads Web; if both do, Web concerns are split between them.
- Priorities and team shape may change in 2027, so this is resolved for now. Individual progression continues through objectives and development plans ([IMP-08](../improvements/08-2026-objectives-calibration-and-eoy-reviews.md)); reopen at 2027 planning if needed.

## Roadmap

| ID | Step | Owner | Depends on | Status |
|----|------|-------|------------|--------|
| CH-05.1 | Review each QA's competency profile in 1:1s | AC | — | dropped |
| CH-05.2 | Deep-dive each Lead QA area, including growth review | AC | — | dropped |
| CH-05.3 | Define Staff QA (Level 8) expectations and evidence | AC | — | dropped |
| CH-05.4 | Define Senior QA II progression options with engineering leadership | AC | — | dropped |
| CH-05.5 | Agree a Staff QA evidence plan with DA | AC | CH-05.3 | dropped |
| CH-05.6 | Explore Junior/Graduate QA headcount with GL | AC | — | dropped |

## Status & Next Action

**Status:** Resolved for now 2026-10-15. _Previously:_ Open — Identified as a structural team health and retention risk during initial baseline phase.

**Next action:**
1. Review each QA engineer's current competency profile against the QA Rating Model during the initial 1:1 discovery conversations.
2. Draft a clear definition of what "Staff QA Engineer (Level 8)" entails at PureGym and what cross-domain evidence is required.
3. Define the progression options for Senior QA II (Level 6) in collaboration with engineering leadership.
4. Explore headcount strategy with the Director to determine feasibility of adding Junior/Graduate QA roles in future budget cycles.
5. Deep dive with each QA Lead on their functional and technical area (output: a Miro covering both layers), including a growth framework review of where each lead sits — agreed at the first QA Lead Sync (2026-09-07).
6. Define a Staff QA evidence plan for DA and review it through observable Website, Web 3, cross-platform, and quality-improvement outcomes rather than title or self-assessment alone.
7. Review JFG's Senior QA evidence with TMW and DA, balancing backend specialism with visibility, communication, and growing front-end capability.
8. Decide whether cross-platform E2E capacity should be retained, replaced, or redistributed when LM's contractor engagement ends, and use the transition to establish a repeatable knowledge-transfer model.

**Watch for:**
- Disengagement or frustration from longstanding engineers who feel their career has plateaued
- Pressure to promote based on length of service rather than demonstrated competency against the next band
- Resistance from Leads if junior engineers are perceived as a drain on delivery velocity rather than an investment
- Unhealthy competition between peers if advancement opportunities are perceived as zero-sum
