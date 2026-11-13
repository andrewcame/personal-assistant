---
id: IMP-10
tag: BrowserStack
type: improvement
status: in-progress
horizon: now
updated: 2026-11-13
pillars: [P4, P9]
focus: [automation, productivity]
jd: [JD-05]
goals: []
links: [CH-09, CH-13]
people: [AE]
---

# Improvement 10 — BrowserStack Renewal And Mobile Device Strategy

## Context

- The BrowserStack licence is due for renewal on **22 November 2026** (confirmed by AC on 2026-11-05). The account-manager call was held on 2026-10-19.
- Remote device reliability has contributed to mobile automation noise (see the 2026-09-16 evidence in the closed [Challenge 01](../challenges/01-mobile-automation-strategy.md)).
- The device platform choice affects how far mobile automation can go: the [Jira initiative brief](../context/jira-initiatives/02-appium-ai-led-first-pass.md) (Appium first pass) and [CH-09](../challenges/09-population-scale-mobile-app-testing.md) (mobile coverage).

## Objective

- **Now:** renew at a lower cost for 22 November 2026, matched to actual usage.
- **Later:** review alternatives (other managed device clouds, a controlled local device estate) and choose the platform that best unlocks reliable, scalable mobile automation.

## Related

- Goal(s): [2026 goals](../goals/2026.md) — provisional
- Role pillar(s): P4 Automation Trust & Reliability · P9 AI-Enabled Testing & Innovation
- Originating recommendation: self (2026-10-15)
- Originating challenge(s): [CH-01](../challenges/01-mobile-automation-strategy.md) (device-farm reliability), [CH-09](../challenges/09-population-scale-mobile-app-testing.md)

## Actions & Progress

### 2026-10-15

- Opened. Account-manager call booked as the first port of call.

### 2026-10-16 (ideas triage)

_From the Ideas triage on 2026-10-16 ([ideas log](../state/ideas-log.md))._

- **Speed:** is there a reason BrowserStack is slow? Are there better alternatives (feeds IMP-10.4)?
- **Exploratory testing:** consider Firebase Test Lab or other exploratory test tools.
- **Requirement to check:** QR code testing via BrowserStack camera image injection with Appium ([BrowserStack docs](https://www.browserstack.com/docs/app-automate/appium/advanced-features/camera-image-injection?fw-lang=c-sharp)).

### 2026-10-19 (renewal call)

- Account-manager call held; the Notion card is closed.
- BrowserStack offered additional features during the call.
- BrowserStack will send: (a) what our current plan includes, including features; (b) the plans we could move to, up or down.
- BrowserStack shared a link to its SDK documentation, but the link can no longer be found. To be re-requested and assessed as an Appium test improvement (IMP-10.6, links CH-09).

### 2026-11-05 (renewal date confirmed)

- AC confirmed the renewal date as **22 November 2026**. Agree the lower-cost plan before renewal; the access review remains a follow-up after approval.

### 2026-11-04 (Platform Technical Lead discovery)

Source: [2026-11-04 Platform Technical Lead](../context/discovery-calls/2026-11-04-platform-technical-lead-staging-reporting.md).

- **Pain point raised:** device testing and beta testing on BrowserStack is painful because external web views need a login through Cloudflare access, and the access client is not installed on BrowserStack devices.
- **Offer from AE:** Platform can whitelist the BrowserStack IP addresses if QA supplies them, so the web views load without the login. Added IMP-10.8 (get the IPs from BrowserStack, then ask AE).
- Feeds the device-reliability baseline (IMP-10.3) and the Appium work in CH-09 (population-scale mobile testing).

### 2026-11-10 (2027 direction preview)

Source: [Leadership Direction, 2026-11-10](../context/leadership-direction.md); tracked in [CH-13](../challenges/13-2027-business-direction-transition.md).

- Web and app technology is expected to move to a third party in 2027, so a long commitment is hard to justify. BrowserStack only sells yearly plans, so the monthly rolling option is off the table. If Web and App go to white label, automation has no product to test and BrowserStack isn't needed; the call is yearly or nothing, made after the director's white-label scope (Thu 12 Nov) and the Friday catch-up (13 Nov). IMP-10.2 updated; its card was renamed to match.
- The longer-term device strategy steps (IMP-10.3 to IMP-10.6) stay in Later, parked until CH-13 shows who owns mobile automation in 2027.

### 2026-11-13 (Friday catch-up; found Done in the weekly review, Flow 6)

- AC asked BrowserStack to cancel the subscription because it is no longer used, following the 13 Nov catch-up: web, app and join move to white label ([CH-13](../challenges/13-2027-business-direction-transition.md)), so there is no product left for the device cloud to test. This replaces the monthly rolling plan idea.
- Cards "Decide yearly BrowserStack or nothing, after the director meeting", "Review my BrowserStack access post “approval”" and "Ask platform to whitelist BrowserStack IPs" are Done. IMP-10.2, IMP-10.7 and IMP-10.8 marked done. New step IMP-10.9 (confirm the cancellation lands before 22 Nov) and card added.
- IMP-10.3 to IMP-10.6 are no longer needed; to be closed with the record once the cancellation is confirmed (outcome to be asked then).

## Roadmap

| ID       | Step                                                                                                                                    | Owner | Depends on         | Status | Card                                                   |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------|-------|--------------------|--------|--------------------------------------------------------|
| IMP-10.1 | Hold renewal call with the BrowserStack account manager                                                                                 | AC    | —                  | done   | —                                                      |
| IMP-10.2 | Decide yearly BrowserStack or nothing, after the director's white-label scope (Thu 12 Nov) and the Friday catch-up; BrowserStack sells yearly only | AC    | IMP-10.1           | done   | Decide yearly BrowserStack or nothing, after the director meeting |
| IMP-10.3 | Baseline device-related failures in mobile automation                                                                                   | AC    | —                  | later  | —                                                      |
| IMP-10.4 | Review alternatives: other device clouds and a local device estate                                                                      | AC    | IMP-10.2, IMP-10.3 | later  | —                                                      |
| IMP-10.5 | Choose the platform that best unlocks mobile automation                                                                                 | AC    | IMP-10.4, CH-09.9  | later  | —                                                      |
| IMP-10.6 | Re-request the SDK documentation; assess it as an Appium test improvement (with camera image injection)                                 | AC    | IMP-10.1           | later  | —                                                      |
| IMP-10.7 | Review my BrowserStack access after approval                                                                                            | AC    | —                  | done   | Review my BrowserStack access post “approval”          |
| IMP-10.8 | Get the BrowserStack IP addresses and ask AE to whitelist them so external web views load on devices                                    | AC    | —                  | done   | Ask platform to whitelist BrowserStack IPs             |
| IMP-10.9 | Confirm the BrowserStack cancellation is processed before the 22 Nov renewal                                                            | AC    | IMP-10.2           | doing  | Confirm BrowserStack cancellation before the 22 Nov renewal |

## Status & Next Action

**Status:** In progress

**Next action:** Confirm the cancellation request is processed before renewal on **22 November 2026**, then close the record.

## Outcome

- Completed:
- Logged achievement:
