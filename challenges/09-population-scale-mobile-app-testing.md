---
id: CH-09
type: challenge
status: open
horizon: later
updated: 2026-10-16
pillars: [P4, P8]
focus: [automation]
jd: [JD-05]
goals: []
links: [CH-01]
people: []
---

# Challenge 09 — Population-Scale Mobile App Testing And Low-Incidence Defects

---

## Context

Current Mobile App testing is primarily functional and singular. A tester may exercise a feature across only three or four locally available devices, proving that individual functions and selected journeys work under a small number of known conditions.

The Appium pipeline adds repeatable automated coverage, but its suites do not currently run at enough volume, frequency, or behavioural diversity to reproduce defects that affect only a small proportion of members. A defect affecting 8% of the member base can therefore remain difficult to observe in testing even though it has a meaningful production impact.

Members collectively exercise the app at production scale and in more varied ways than the current test model. They bring different devices, operating-system versions, account histories, membership states, data combinations, journey sequences, timings, retries, interruptions, and patterns of repeated use. This creates population-level failure modes that may not appear when a tester proves each function once against stable data and a small device set.

This concern is related to [Challenge 01 — Mobile Automation Strategy](01-mobile-automation-strategy.md), but is distinct from the choice or mechanics of an automation framework. Appium, Maestro, or another tool could all execute tests without resolving the underlying problem if execution remains low-volume, uses narrow behavioural patterns, and repeatedly exercises the same data and member states.

## Challenge

How do we build a Mobile App test strategy that can detect low-incidence defects before members encounter them, by exercising the app at sufficient scale and across representative patterns of usage, data regeneration, and state variation?

The strategy needs to move beyond proving that isolated functions work and create evidence that member journeys remain reliable across:

- a representative range of devices and operating-system versions
- varied member, membership, gym, payment, and account states
- regenerated or deliberately mutated test data rather than repeatedly reused stable records
- different journey sequences, timings, retries, interruptions, and repeat usage
- enough executions to make defects affecting a small percentage of members observable
- combinations of app, API, integration, environment, and data conditions that may produce intermittent failures

## Questions To Explore

### Scale And Detection

- What execution volume is needed to give a reasonable chance of detecting a defect that affects 8% of members?
- How often should priority journeys run to expose intermittent or state-dependent failures?
- Which journeys justify population-style repeated execution rather than a single pass per build or release?
- How should pass rates, intermittent failures, and failure clusters be reported so that low-incidence signals are not dismissed as test noise?

### Representative Usage Patterns

- Which production usage patterns differ most from the clean, linear journeys used in functional testing?
- What combinations of retries, abandoned journeys, backgrounding, network interruption, repeated actions, and return visits should be represented?
- Can production telemetry identify the device, operating-system, account-state, and journey patterns associated with escaped defects?
- How should privacy-safe production evidence inform the test population without copying sensitive member data?

### Data Regeneration And State Variation

- Which member and membership states must be generated for each run rather than maintained as a small pool of fixed test accounts?
- How can test data be created, mutated, expired, and reset reliably across the app and its dependent systems?
- Which defects depend on account history or state transitions that a newly created member cannot reproduce?
- Can scenario generation vary data while retaining enough control to diagnose and replay a failure?

### Devices, Environments, And Execution Model

- What role should local devices, managed device farms, simulators or emulators, and controlled physical-device estates each play?
- Which environment constraints currently prevent higher-volume or parallel execution?
- Can the pipeline run representative scenarios concurrently without test-data collisions or shared-state interference?
- How do we separate genuine low-incidence product failures from device-farm, environment, or automation instability?

### Evidence And Prioritisation

- Which recent member-reported defects passed functional testing but would have been detectable through greater scale or variation?
- What defect incidence, member impact, and journey criticality should trigger investment in population-scale coverage?
- What is the smallest proof of concept that can show whether repeated, varied execution finds failures missed by the current approach?
- How should findings feed back into lower test layers, observability, and product design rather than remain only as larger Appium suites?

## Initial Position

Passing a function on a few devices is necessary evidence, but it is not evidence that the app will behave reliably across the member population. The strategy should retain focused functional testing while adding a population-oriented layer for the journeys where low-incidence failure has meaningful member or business impact.

The first step should not be to multiply the same tests unchanged. Repetition will add limited value if every run uses the same member state, data, sequence, and timing. A useful proof of concept should combine controlled variation with enough executions to expose intermittent behaviour, while preserving the seed, data, device, state, and journey trace needed to reproduce a failure.

Production telemetry and escaped-defect evidence should guide scenario selection. The aim is not to reproduce the entire member base in test, but to identify representative cohorts and high-risk state combinations, then use repeated execution to make uncommon failures visible before release.

## 2026-10-16 Update — Ideas Triage

_From the Ideas triage on 2026-10-16 ([ideas log](../state/ideas-log.md))._

- Current app issues keep unearthing defects that have always been there; each fix reveals another. They are hard to find in QA because testing is functional rather than like the app is used.
- Question: how can we test on prod, alpha and beta builds?

## Roadmap

| ID | Step | Owner | Depends on | Status |
|----|------|-------|------------|--------|
| CH-09.1 | Analyse a recent low-incidence escaped app defect | AC | — | later |
| CH-09.2 | Define PoC journey, member states and variations | AC | CH-09.1 | later |
| CH-09.3 | Set execution count and frequency for target incidence | AC | CH-09.2 | later |
| CH-09.4 | Confirm per-run data generation and replay evidence | AC | CH-09.2 | later |
| CH-09.5 | Run PoC through the existing Appium pipeline | AC | CH-09.3, CH-09.4, INI-02.6 | later |

## Status & Next Action

**Status:** Open — captured on 2026-09-24. Current functional and Appium coverage does not yet provide evidence at the volume or behavioural diversity needed to detect low-incidence member defects.

**Next action:**

1. Select a recent escaped Mobile App defect, ideally one affecting a known minority such as 8% of members, and identify the conditions associated with it.
2. Define one critical journey and a small set of representative member states, data variations, device profiles, and behavioural variations for a proof of concept.
3. Establish the execution count and frequency needed to make the target incidence reasonably observable.
4. Confirm how each run will generate or mutate data and record enough evidence to replay failures.
5. Run the proof of concept through the existing Appium pipeline before deciding whether framework, environment, device-farm, or infrastructure changes are required.

**Watch for:**

- Higher test counts being treated as sufficient without meaningful state or behaviour variation.
- Fixed test accounts masking defects caused by account history, regeneration, or state transitions.
- Intermittent product failures being classified as automation noise without investigation.
- Device and environment diversity being increased without enough diagnostics to reproduce failures.
- Framework discussions displacing the more fundamental question of representative scale and usage.

## Related

- [Challenge 01 — Mobile Automation Strategy (Appium vs Maestro)](01-mobile-automation-strategy.md) — addresses framework direction, ownership, and layered automation; this challenge addresses execution scale, representative population behaviour, varied state and data, and low-incidence defect detection.