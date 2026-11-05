# Full Review Example

## Goals

### 1. New Skill - Appium

Post MAUI, transition automation over to Appium starting with the MX Account site migration.

Comments

This objective has been completed:

- **Learning -** I learned Appium through paired delivery of the MVP with x, who provided technical guidance and framework design support. To reinforce each of the concepts we covered during implementation, I utilized AI/Copilot to summarise content and provide further reading (updating my own personal notes).
- **Delivery -** we designed and implemented the Appium MVP framework to cover the basic authentication flows and some basic scaffolding for the Bookings and Account journeys. The maintainable POM/component approach was aligned to MAUI/XAML patterns to allow future expansion. QA improvements were added via improved error handling and feedback mechanisms in the tests.
- **Documentation -** I helped peer review framework documentation produced by x.
- **Metrics** - During the MVP I created a simple Excel model to monitor completion against the legacy pack. I also added in all legacy tests into code in an "ignored" state so we could see the numbers move over time in real time in the pack. Although we expected tests to change during migration, this supported the original "like for like migration" goal (although I'm aware the plan has changed now).

I've set myself to "star" for this objective as (in my view) producing this MVP, parallel to sprint work, was crucial to get buy in to progress Appium as a project and demonstrate the value gained by doing so.

### 2. Tech objective - fill MX knowledge gaps by March25

Obtain exerp handovers to fill MX knowledge gaps, so that you can become a SME by mid-March25.

This objective has been completed.

- I carried out multiple structured handover sessions with x to close my remaining Exerp blind spots, specifically around class bookings, Kiosk/POS cash drawer behavior and clip cards.
- I have established ongoing contact with x, x and x in the config team, so am confident that I can reach out to them on any specific domain questions that arise that I can't answer.
- Going forward, I always push for config involvement in tickets (where appropriate) to ensure we know how to set things up in test prior to a ticket hitting QA (for example - premium classes).

*Note: although the objective is complete, I continue to build on this knowledge in my new team, and the Exerp/PICO exposure has strengthened my overall technical toolkit*

## Values

### 1. Focus on the Detail

*Some examples of how I feel I have displayed this:*

- Improved reliability in the Xamarin UI test suite by identifying redundant logic (e.g. achievement badges) and added intelligent retries (in pipeline/code), significantly reducing deployment delays. This was seen as a "win" in speeding up delivery as before it would often take a day of retries to get a green UI test run.
- Paired with developers on detailed issue investigations whenever I find issues that need a closer look. For example, reproducing android-specific crashes and working collaboratively to solve this (often working in addition to other sprint work).
- Always ensuring a high quality of test commentary, comments and "this is how you need to test this" information on tickets. This ensured traceability and allows other engineers to review if they need to do a similar test in the future.
- When onboarding to the apps team, worked with another engineer to update and validate the team setup instructions (Mac, simulators, local tooling), ensuring documentation was accurate and removing a major friction point for new engineers. *This is still a WIP but something that is greatly improved vs the previous version.*

### 2. Play to Win

- Drove the Appium MVP delivery, pairing with RW alongside the sprint work and pushing the MVP through to completion.
- Championed a shift-left mindset in both Apps and Web, encouraging earlier QA involvement in refinements, development and during PR reviews to reduce rework and improve first-time quality.
- Jumped on issues found in App testing, working with the developers to recreate so that they can identify a fix more efficiently.
- Leveraged new reporting tools in the apps team (Firebase and Android studio) to flag repeated errors and oops codes seen and understand what causes these to occur, ultimately creating a better bug report.

### 3. Stand Shoulder to Shoulder

Some examples of how I feel I have displayed this

- Provided day-to-day leadership and mentoring to x and support to x, acting as the on-the-ground QA representative (or "lead") prior to x joining.
- Coordinated with my former Apps team on premium classes whilst working in Web. This helped align cross-team understanding and ensured they could progress their feature development in parallel to web/backend work.
- Supported Product by producing functional videos, answering SME questions, and joining calls to explain key features of the account area, helping them work with design to build the new account are designs.
- Supported PICO testing during go-live, offering my knowledge and experience to help test some edge cases and contribute to a more confident go live. Also, proactively and guiding the E2E tester with SME knowledge particularly around Braze.
- Helped JFG in the MX Web refinements by giving a more rounded QA perspective, particularly from my time in apps in regards to premium classes.
- Be a trusted advisor and SME in areas I have experience in, who can people can always reach out to. Be willing to explain concepts to improve others understandings and support other teams when needed.

### 4. Make a Difference

*Some examples of how I feel I have displayed this:*

- Played a key role in the Apps team, quickly becoming a trusted voice whose QA perspective influenced planning, retro, and delivery discussions (by asking the right questions in these discussions).
- Took full ownership of the Appium journey — not just learning it, but helping make it real after years of stalled attempts — demonstrating initiative and determination.
- Increased confidence and capability within the wider QA group by mentoring others, both in Apps/Web (x and x) and in QA meetings. Encouraged a culture of continuous learning and improvement by pushing for cross team QA standards and tooling.
- Transitioned into Web, delivering value from the off and showing a strong desire to understand and contribute to the team.

## Forward Focus

- Deepen my understanding of the PICO ecosystem and related technologies including GitHub Actions, GraphQL, Kafka, SuperGraph, and Astro, to effectively support and contribute to Web team initiatives and automation.
- Continue improving my coding skills in C# — building on my Appium experience with concepts like inheritance and dependency injection — and advance my JavaScript/TypeScript proficiency to support the upcoming Playwright implementation for the new Account area.
- Grow my technical debugging and automation engineering capabilities on my path to becoming a strong SDET, with an eventual aspiration to contribute as a junior developer.
- Develop expertise in load testing, specifically with K6, to prepare for taking a more active QA ownership role in performance and reliability testing as this area shifts from development-led to QA-led.