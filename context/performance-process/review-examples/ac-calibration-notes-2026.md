# AC's Calibration Notes 2026 (Voice Reference)

_AC's own Top 3 WHAT, Top 3 HOW and improvement-area wording for the six QA team members, as written on 2026-11-16. Kept as AC wrote them, including spelling and punctuation, so agents can copy his voice. Only changes: names replaced by aliases. No ratings or matrix positions were part of them. The filed, neutral versions are in each person's `team/<alias>.md` under "Calibration notes"._

## How To Use These

**Take from them**

- The voice: plain verbs, "he/she" talking about a colleague, one idea per bullet, the outcome stated.
- The pattern: a short bold-style lead-in sentence, then what was done and why it mattered ("Owner and architect of...", "Industrialised...", "Made Portal automation a possibility by...").
- Ticket IDs and named systems wherever AC has them, so each claim can be checked.
- HOW entries start with the behaviour, then give a concrete example.
- Improvement areas are short, numbered, and framed as what to do next.

**Leave behind**

- Nothing from the voice. This is the primary style reference for calibration and review drafting; the other-lead [examples](calibration-top3-examples.md) are for shape only.

**Still applies:** anything written into `team/` follows the [people-records writing standard](../../../team/README.md#writing-standard). Copy the voice, not any phrasing that labels a person.

## DA

**What**

Led front-end QA for the DK and CH rollouts: made sure the front-end test repo covered the new markets and managed the day to day QA for the go-lives. DK was later descoped as the business moved towards sunsetting the microsites.

Owned the front end test repo scope expanding coverage, adding enhancements, standardising between markets and ensuring appropriate AI workflows and skills were included.

Made Portal automation a possibility by leading member creation initiative working with other QA leads and the test manager to elicit requirements, scoping out how this could be achieved and creating a trail of work to deliver this

**How**

Raises issues with appropriate detail and clarity allowing other team members and deveopers to understand the root cause and fix them

Proactively looks for opportunities to expand our test coverage based on latest tech trends, best practice, and gaps issues seen on the web page (for example accessibility)

Takes on board technical challenge and is open to new technical approaches, not resistant to change and improvements, and supports others in having the same mindset

**Learning**

_Item 1 (engagement, communication style and adaptability) is not copied here: its wording labels the person, so only the neutral version in [da.md](../../../team/da.md) is kept._

2. Management - setting time aside time to focus on the development of direct reports, progression plans, objectives etc

## MP

**What**

Ensured QA standards did not drop when team went from two QA's to one. 110+ tickets were tested this year, about 40% of which were reopened. In August he covered five streams at once - CH race condition, Apple MPAN, deduction day in Pico, co-branded cards, session state

Got CH payments live and protected coverage as services moved into Pico. CH is live with good coverage. When some payment services moved into the Pico repo, he added tests confirming payment agreements and subscriptions are created after a join. He raised tickets for the remaining gaps (PAYTEAM-282/283/284), reaching 80% before microsite-sunset work took priority

Leveraged AI to accelerate and support the single QA model including mapping test migration across pipelines, brands and shards (PAYTEAM-82), work that would have taken hours manually, finding the root cause of PAYTEAM-292. Created a skill that suggests tests from a PR and checks them against his test plan.

**How**

Maintains high standards despite tight deadlines he kept to the agreed standards through tight deadlines and reduced capacity. Pushed back where appropriate.

Values knowledge sharing within the team, and is actively taking steps to close the gaps on documentation and how to do specific payments things (like how certain kafka messages work). Also, creates epics and stories to document gaps and to remind him to return to update in the future

Always looking to increase test coverage within his area. Investigating it, challenging it and improving it eg PAYTEAM-51, 61, 281, 282, 283, 284, 195, PAY-3588, 3571, 3921

**Learn**

1 Understanding the business outcomes, tailoring the level of testing needs to this and weighing it against "must fix now" vs "revisit later". Working with delivery and undestanding the bigger picture.

2. Longstanding in one team its good that steps have been taken to improve documentation in payments, turning this into a structured handover or cover plan would be beneficial. Also, openess to work in other areas would help him gain a bigger perspective

## TMW

**What**

Industrialised the Exerp release process improving it, removing some manual steps, adding more detailed instructions, added AI skills to speed it up etc. Most importantly, making sure we didn't have a single person managing it and creating a bottleneck for delivery.

Was the app team's only QA through a major release as the sole QA in apps. At this time, we had one of the biggest breaking change releases this year (moving to .NET 10) and she managed the defect and resolution process with product and the stakeholders, often having to fight for the member perspective to get resolutions and maintain quality.

Delivered some core appium improvements and journeys although never a full focus (and hampered by technical challenges), she created a plan to tackle appium and implemented some key improvements (browserstack reporting, class bookings and dashboard checks).

**How**

Looking out for her team members and helping cross team in WEB 3, particularly during the exerp upgrade process. Understanding the presure that was put on JFG and actively looking for ways to support him. From September this year, she supported JFG on the exerp release process, managing the last one entirely so he could focus on web 3.

Being a strong advocate for the member throughout testing, always reflecting on the user experience and making sure all issues found had that level of scrutiny. Spoke up in refinements for work and shifted left as much on potential issues and member experience gaps.

Showing determination to debug and find the root cause of issues on the app, partnering with the developers to push for deliver dev pages and wiremock solutions so that these edge case problems could be identified and resolved in QA (and not by live members).

## JS

**What**

Supported the pico launch in Switzerland - being heavily focused in QA for the Pico market launches, including CH and linked login work.

Presenting to key business stakeholders in London Head Office and on video calls regarding aspects of Pico feature/ functionality delivered e.g. Payload. Being a champion of the solution and ambassador for engineering.

Being a major SME and AI enabler on the front end tests creating an automation AI test agent to help generate tests / review tests for Playwright automation, always picking up PR's, creating appropriate tech enhancement tickets.

**How**

Proactively identifying risk and quality concerns. Flagging issues with the QA processes to the team and senior leaders, being proactive in raising problems at retros and ensuring the backlog of work is efficiently managed.

Supporting other teams and workstreams - not working in a silo'd manner, helping support other web teams, acting as an SME and onboarding new QA's onto the solution. For example: helping KB in web 2 and TMW onboard to web 2.

Member experience first thinking: going beyond the ticket and designs, digging into the usability and edge case scenarios. Questioning the reasoning behind choices made so design choices can be challenged.

**Learn**

Leadership training and awareness she wants to develop her mentoring/leadership skills. Wants to be more impactful.

More agentic AI usage/understanding she has expressed a desire to build more AI skills and look for ways this can help other teams (eg designing an agentic workflow to help review PRs).

## KB

**What**

Took over CoP testing and defined an automation approach: Moved to the Comms team and picked up all the testing in that area. Investigated automation and produced a proposal.

Protected a high-risk join journey with new automation: Added automation for segmented student journeys, an area where products had previously gone missing from the front end. This didn't cover duplicates, which was an issue fixed following an improvement after a P1, but this did mean we had good coverage for a new segmented approach in our pack.

Made AI enablement a key tenet of his role: focused on using AI to accelerate test case generation, in so much that all cases are AI generated. Added skills and guidance for better utilisation and used AI to build his own tools to enable faster and more efficient manual testing.

**How**

Detailed orientated - finds the hard to find issues: He found a major date issue in GCM UAT, and more recently raised an issue in the activity-data work. Has an SDET mindset and always works with developers to produce meaninful data to help them replicate and fix issues, to shorten the defect to fix loop.

Flexibility in supporting us where we need him: He was in the integration team, then the Comms team, then Web team 2 and now Apps! He is able to orientate in teams and deliver quickly.

Sound technical understanding to adapt to technology: Has a good understanding of our front end, backend, CEP, COP, GCM etc. Can pick up technical areas quickly and contribute to improving and growing automation in these areas.

**Improve**

1. Share what you build: Let other teams and engineering benefit from his tooling and insight, contribute to platform initiatives

2. Understanding the business outcomes its important to understand the level of testing needs to be tailored to the business and weighed against delivery. Undestand the bigger picture.

## JFG

**What**

Owner and architect of pico backend test repo which he mostly maintains. He has kept it up to date and changed it in response to feedback. The tests run against deployed preview environments, not only locally, so they catch problems that only appear once services talk to each other for real.

Became an SME for pico backend and portal end to end flows mentoring team members IY, TMW and LM on Braze, BGW, test data creation and account portal testing. Being the main point of contact in the QA team for account backend pico services.

Took over managing Exerp upgrades in our legacy backed end repos (BGW and Test Data) He was the person who led and managed the Exerp upgrades, including the BGW updates needed before microsite testing could start. TMW has subsequently picked up "owning" this, but it was his initial documentation and process that got this off the ground.

**How**

Shared what he knows so others can test Pico end to end: Always offers what he knows to others, runs demos/workshops/sessions to upskill others. Steps in to help testing when needed on E2E to help deliver on our sunset microsites mission.

Attention to detail very diligent when testing tickets, seeing data throughout the journey (particularly backend) and proving the seeding in databases is as expected. Asks the right questions to ensure he fully understands the remit of the ticket and ensure it is tested as thoroughly and comprehensively as possible.

Took responsibility beyond his own tickets: Understands that pico is a fully integrated ecosystem, and that whilst integration test coverage in account service is complete it is not in others (like basket). Created https://puregym.atlassian.net/browse/WEB-924 to identify gaps and had discussions with the team to agree scope.

**Imp**

1. Awareness - attending stand ups on time, being present and responsive in all calls (he does this mostly but lapses from time to time)

2. Visibility - making the case for his improvements to a wider auidence, be an advocate for his approach, be vocal on the change he wants
