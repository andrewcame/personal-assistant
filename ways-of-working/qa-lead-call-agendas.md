# Initial QA Lead Call Agendas

These agendas support the first discovery conversations with TMW, DA, and MP. They follow the 30-day plan: listen, understand, establish baselines, and build trust before making changes.

These are not formal performance reviews, objective-setting meetings, or technical deep dives. The aim is to understand each lead's experience, the team's health, current friction, and the support they need from the QA & Test Engineering Manager.

This is a temporary agenda for the initial conversations. After the calls, remove this file and retain only durable findings in the relevant team profiles, discovery notes, challenges, decisions, goals, or follow-ups.

## Shared Shape

Allow around 45-60 minutes. Keep the conversation natural rather than trying to ask every question.

### 1. Open The Conversation

- Explain that this is an initial listening conversation, not a formal goal-setting or performance meeting.
- Say that you want an honest view of what is working, what is difficult, and where you can be useful.
- Confirm that you will look for themes across conversations, without attributing every comment unnecessarily.

### 2. The Person And The Role

- What is giving you energy in the role at the moment?
- What do you most enjoy doing?
- What is frustrating you or taking more effort than it should?
- What would you like more or less of in your role?
- Where would you like to develop over the next 12-18 months?
- What support from me would make the biggest difference?

### 3. The Team And Ways Of Working

- How are your team and squad functioning at the moment?
- How has the current way of working landed with the QAs?
- Where does work flow well, and where does it queue or stall?
- How well do QA and engineering share ownership of quality?
- Where are communication or knowledge-sharing gaps between platforms or squads?
- What should I understand about your team before I start suggesting improvements?

### 4. Quality Health Baseline

Use this as a conversation, not a request for a report.

- Which automation do you trust, and which results do you treat cautiously?
- Where do environment, test data, builds, or deployment issues create the most friction?
- Where are the most important coverage gaps?
- How visible are test results and quality risks to the squad?
- What currently consumes time that does not feel like valuable QA work?
- Where could better developer involvement improve quality or reduce handoffs?

### 5. Close

- What is the one thing you would most like me to understand from this conversation?
- Is there anything you expected me to ask but have not?
- Who else should I speak to, and which forums should I join?
- What would make the next few weeks feel useful rather than disruptive?

Capture themes, not a transcript. Record operational actions in Notion and add only durable context to the person's profile or discovery notes.

---

## App Lead: TMW

### Conversation Aim

Understand how the Mobile App team is operating, what is affecting confidence in mobile delivery and automation, and how TMW wants to lead and develop the platform. Do not begin with Appium versus Maestro; first understand the underlying pain and capability needs.

### Prompts

- How are you finding the Mobile App lead role at the moment?
- What is working well in the mobile team, and what feels harder than it should?
- How are iOS and Android work differing in terms of testing, environments, devices, and release confidence?
- Which parts of the current Appium framework do the team trust, and where does it create friction?
- Are there problems that belong to the MAUI app, the framework, the test data, the devices, or the CI pipeline?
- How are automation decisions discussed with developers? Where is shared ownership strong or weak?
- How is JFG being supported and developed within the team?
- Where do you want to grow as a Lead QA: technical direction, people leadership, stakeholder influence, or something else?
- What would help you feel more confident setting the mobile quality direction?
- What should I understand about the existing mobile automation work before getting involved?

### Listen For

- Whether framework friction is technical, capability-related, confidence-related, or an ownership issue.
- Whether mobile automation is treated as a shared engineering asset or primarily a QA responsibility.
- Whether the team has a clear path from mobile test failures to root cause.
- How much time is lost to device availability, MAUI behaviour, overlays, builds, environments, or flaky tests.
- Evidence of Level 7 leadership: mentoring, creating space for others, influencing standards, and connecting mobile practice to wider QA direction.

### Relevant Context

- [Challenge 01 - Mobile Automation Strategy](../challenges/01-mobile-automation-strategy.md)
- Mobile App is a core platform responsibility in the role and includes iOS and Android .NET MAUI coverage.

---

## Payments Lead: MP

### Conversation Aim

Understand how the Payments team experiences quality risk, how payment testing supports business confidence, and what MP needs to lead the specialist domain effectively. Keep the focus on people, operating friction, and confidence rather than a payment architecture review.

### Prompts

- How are you finding the Payments lead role and the current team dynamic?
- Which payment journeys or failure modes create the most pressure for the team?
- What does "safe to release" mean for Payments from your perspective?
- How confident are you in coverage across payment partners, retries, failures, refunds, reconciliation, and member/account states?
- Where do environments or test data make payment testing difficult or unrealistic?
- How well do Finance, payment partners, Commercial, and delivery teams understand the quality risks you are managing?
- Where does the team get involved in requirements and acceptance criteria, and where does QA still receive work too late?
- What information would help you communicate payment confidence more clearly to engineering and business stakeholders?
- How are you developing the people around you, and where would you value support as a people leader?
- What would make the biggest positive difference to the Payments team's effectiveness over the next few months?

### Listen For

- Whether the team can distinguish product defects, partner failures, data problems, environment problems, and test problems.
- Whether business-critical payment coverage is visible and understood outside QA.
- Where payment domain knowledge is concentrated and whether succession or knowledge-sharing risk exists.
- Whether MP has enough influence upstream to shape quality and testability before delivery.
- Evidence of Level 7 leadership: coaching, cross-team influence, technical quality standards, and practical ownership of delivery risk.

### Relevant Context

- Payments is explicitly business-critical in the role: Finance, payment partners, Commercial, and market teams need useful quality visibility.
- Relevant role pillars: Business-Critical Journey Protection, Stakeholder Confidence & Visibility, Quality Ownership & Culture, and Test Infrastructure, Environments & Data.

---

## Web Lead: DA

### Conversation Aim

Understand how the Website platform is operating across Web Teams 1 and 2 and the Commercial squad, how QA supports high-velocity web delivery, and how DA is developing JS and KB. Keep the conversation about experience and operating health rather than an automation repo deep dive.

### Prompts

- How are you finding the Website lead role across the different teams you support?
- Where is the website delivery model working well, and where does it create friction?
- How consistent are quality expectations across Web Teams 1 and 2 and the Commercial squad?
- Which web automation results do you trust, and where do intermittent or environment-related failures reduce confidence?
- How are preview environments affecting testing, especially for backend-dependent or cross-service changes?
- How easy is it to get representative test data for member journeys, markets, and commercial flows?
- How early are you involved in feature discovery, scoping, acceptance criteria, and edge cases?
- How are JS and KB being supported and developed within the Website team?
- Where could knowledge-sharing across Website, Mobile, and Payments help the team?
- What would you most like me to improve or protect as the QA & Test Engineering Manager?

### Listen For

- Whether the same quality bar is experienced across the Website teams and Commercial squad.
- Whether preview reliability, test data, backend coverage, or CI feedback is the main source of friction.
- Whether automation coverage reflects business-critical journeys and international market variation.
- Whether DA is carrying too much coordination or platform knowledge personally.
- Evidence of Level 7 leadership: growing other people, improving shared practices, influencing engineering ways of working, and making quality risks visible.

### Relevant Context

- Website is an Astro-powered platform supporting Web Teams 1 and 2 and the Commercial squad.
- Relevant role pillars: Automation Trust & Reliability, Delivery Confidence & Flow, Business-Critical Journey Protection, Knowledge Sharing & Quality Practice, and People Capability, Progression & Succession.

---

## After All Three Calls

Compare themes without attributing comments unnecessarily.

- What frustrations appear across all three platforms?
- Which problems are platform-specific and which are systemic?
- Where do the leads need clearer ownership, better support, or more capacity?
- Which signals should feed the automation, environment/data, and delivery baselines?
- What should be explored next with the wider QA team, Platform/DevEx, SRE, Configuration, or business stakeholders?
- Which apparent easy wins are supported by more than one source, and which still need evidence?
