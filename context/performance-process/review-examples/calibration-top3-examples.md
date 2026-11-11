# Top 3 WHAT / HOW Examples From Another Department Lead

_Shared by another department lead on 2026-11-11 as examples of Top 3 WHAT and Top 3 HOW entries for the calibration template. They describe engineers outside QA and carry no names. Used by calibration-prep and Review Writer for the **shape** of an entry, not its voice._

## How To Use These

**Take from them**

- Three entries each for WHAT and HOW, one per line.
- Ticket IDs in brackets so every claim can be checked.
- The system or service named, and the result stated ("eliminating DLQs", "unblocking legacy microsite decommissioning").
- Each HOW entry names a value-style theme, then gives a concrete example.

**Leave behind**

- The mechanical, verb-led opening ("Spearheaded", "Engineered", "Architected") and the repeated "title - description" pattern.
- Stacked labels and buzzwords ("high-throughput", "operational excellence", "systems thinking").
- Packing several claims into one sentence.

**AC's preference:** AC finds these quite factual and wants his own entries a little warmer and less mechanical. Keep the specifics, ticket IDs and outcomes, but write like a person talking about a colleague's work. Plain verbs, one idea per sentence, no buzzword labels. Entries for the QA team still follow the [people-records standard](../../../team/README.md#writing-standard): dated, observable and neutral.

## Example 1

**WHAT**

1. Decoupled membership events from legacy order events (WEB-922) - Spearheaded re-architecture of membership events (MembershipPurchased, MembershipUpdated) away from multi-line order events, preventing out-of-order state overwrites, eliminating DLQs, and enabling safe event replay.
2. Delivered Staff & Personal Trainer ingestion pipeline (WEB-774, WEB-829, WEB-842) - Engineered full-stack data pipeline from Exerp to Pico GraphQL schema to calculate and expose Staff and PT flags, including a complete historical backfill across all accounts.
3. Implemented Cancellation & Retention Braze pipeline (WEB-566, MXPO-168, MXPO-94) - Added MEMBER_RETAINED telemetry into Braze, established Avro schemas for failure scenarios, and added TransactionId for end-to-end distributed tracing.

**HOW**

1. Systems thinking & root-cause resolution - Investigated and resolved complex cross-system race conditions (e.g., PersonDetailsChanged/SuspensionStatusChanged arriving before PersonCreatedDone), systematically draining recurrent DLQ backlogs.
2. Proactive operational excellence - Drove down alert noise and improved reliability by remediating PII data in Exerp Adapter logs, building automated stale-transaction cron jobs, and fixing data-mapping integrity bugs causing duplicate accounts.
3. Autonomous, high-throughput delivery - Trusted to take vague, legacy, multi-system problems to robust permanent solutions while shipping at high velocity across pico, exerp-adapter, account-service, exerp-extractor, and braze-adapter.

## Example 2

**WHAT**

1. Delivered the Legacy Gateway translation layer in Pico (WEB-893) - Implemented GraphQL account management features (Key Fob, Bolt-ons, Change Plan, Membership Freeze) translating into Business Gateway calls with RFC 7807 problem parsing, typed errors, and integration test coverage, unblocking legacy microsite decommissioning.
2. Architected the Retention Offer rules engine (WEB-509, WEB-453) - Led the technical spike and implemented backend eligibility engine for `ReceiveMembershipRetentionOffer`, codifying rules around add-ons, price changes, corporate/Vitality membership, and pending freezes, plus an ADR on subscription price change sourcing.
3. Built the greenfield Access Service for international QR gate access (MXPO-74, MXPO-259, MXPO-267) - Created a new Pico microservice for Denmark and Switzerland, integrating with Exerp v6 `accessGate` with custom error handling for boolean-only gate responses.

**HOW**

1. Cross-system architectural initiative - Entrusted with high-ambiguity spikes (price change sourcing ADR, member status migration mapping, Braze SDK in Astro) and delivered across Pico, Business Gateway, CAPI, and Identity Server boundaries.
2. Operational hygiene & reliability ownership - Resolved captive DbContext connection leak in Identity Server, redacted PII in Exerp Adapter logs, and stabilized out-of-order Kafka events with automated retries.
3. Developer enablement & AI leadership - Built the `KafkaSender.Cli` developer tooling and configurable Exerp Extractor batch utilities; ran the AI chapter for ~5 months, evaluating LLMs and demoing new AI capabilities.

## Illustration: Same Facts, Warmer Voice

_Illustrative rewrite of Example 1, WHAT 1, using only the facts above. Aim for this register in AC's own entries._

> Moved membership events (MembershipPurchased, MembershipUpdated) off the old multi-line order events (WEB-922). Updates no longer overwrite newer state when they arrive out of order, the dead-letter queues stopped filling up, and events can now be replayed safely.
