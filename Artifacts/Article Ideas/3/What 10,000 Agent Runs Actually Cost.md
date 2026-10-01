# What 10,000 Agent Runs Actually Cost

You're three weeks into running your agent workflow in production. The hosted bill came in at $3,003. Your CFO asks what it would cost to move to your own AWS account. You do some quick math — compute, storage, a managed Postgres — and quote $3,500. Three weeks later, the real invoice arrives: $7,200. The missing $3,700 wasn't a billing error. It was the things that don't show up on a vendor pricing page.

That's the question this article answers: what does 10,000 agent runs a month actually cost, once you count everything? The short version is that hosted and self-hosted infrastructure are roughly even on paper — about $3,000 to $4,000. The moment you add operational labor, retry taxes, and human review queues, self-hosted costs nearly twice as much. Here's where every dollar goes, what the pricing pages hide, and how to tell which number applies to your team.

---

## The hosted stack: $3,003, and it's not just the compute

Hosted platforms bundle the infrastructure and absorb the operational labor. That $3,003 invoice covers the agent runtime, the workflow engine, state storage, tracing, and the hidden cost of things going wrong — a number built from pricing pages and workload assumptions, not an audited production invoice.

The agent runtime — the time your model spends actually thinking — is the easiest line to understand. At roughly twenty minutes of active execution per run, 10,000 runs a month comes to about $133 in runtime fees.

The workflow engine — the thing that makes sure your long-running processes survive a server restart — adds a base platform cost. Then there's state storage (the database that remembers what your agent did last week), tracing (the dashboard that shows you why it failed), and the human review queue. If twenty percent of runs need a person to approve the output before it touches a customer, and each review takes three minutes, that's $600 a month at a $60-per-hour review rate.

Both stacks share a vulnerability that no pricing page models: the cost of things going wrong. Complex workflows retry about fifteen percent of the time. When a step fails and retries, you're not just paying for the second attempt — you're paying for the model call again, the tool call again, and the side effect again. At a twenty percent step-failure rate — a figure from one workload model, not a universal law — the pricing page's "per run" estimate becomes 1.37 times more expensive. That's roughly $360 a month in retry costs for this workload, and it's the kind of line item that never appears on the vendor's website.

The hosted advantage is zero operational full-time equivalents. When the checkpoint storage fills up or the durable timer stops firing, the vendor's team fixes it. You don't add headcount.

**The practical takeaway:** The $3,003 invoice is real, but it assumes your failure rate is low and your human-review queue is manageable. Push either number up and the bill climbs fast.

---

## The self-hosted trap: $3,500 in cloud invoices, $2,000–$6,000 in engineer salaries

Self-hosted infrastructure looks cheaper on paper because the raw compute comes in slightly under the hosted equivalent — roughly $3,500 to $4,000 a month for the same workload, again from a cost model rather than a production audit.

You're paying for the cloud infrastructure that runs the workflow engine, the action fees that scale with execution volume, the self-managed database for state, and the tracing stack you host yourself. Add it up and the cloud invoice is narrower than the hosted bill, not wider.

But here's the thing about self-hosted: the cloud invoice is only half the story.

Someone needs to patch the operating system, rotate secrets, debug checkpoint corruption, and answer the 2 AM page when the durable timer stops firing. That's not a part-time job — it's between a quarter and one full-time equivalent, depending on how many workloads share the cluster and how much chaos they produce. At fully-loaded engineering salaries, that's $2,000 to $6,000 a month. Suddenly the $3,500 infrastructure bill becomes a $5,500 to $10,000 monthly cost — and that's before the first production incident.

The same incident that costs a hosted platform nothing in headcount becomes a Thursday night for your team.

**The practical takeaway:** Self-hosted only makes financial sense if you already have a platform engineering team and can spread their cost across multiple products. If you're hiring that person specifically for this workload, hosted just won.

---

## The hidden multipliers: idempotency, retries, and the $72,000 overnight

Both stacks share a vulnerability that no pricing page models: the cost of things going wrong in production.

A five percent failure rate adds fifteen to thirty percent to your bill because every retry re-executes model calls, tool calls, and side effects. The retry tax alone runs $600 to $900 a month for a complex workload. And one documented case from 2026 shows an agent retry loop running overnight and generating $72,000 in charges before anyone noticed — the kind of outlier that cost models don't capture.

Idempotency is the guardrail. If your agent generates a stable idempotency key before it charges the customer's card or updates the record, a network timeout becomes a safe retry instead of a duplicate transaction. Without it, an 800 millisecond network blip can turn a $100 purchase into a $200 purchase — and a manageable month into a catastrophe.

Hosted platforms also have a structural advantage with human approval workflows. A thirty-day approval gate doesn't cost extra infrastructure because the vendor handles the waiting. Self-hosted, you're paying for the database rows, the queue processor, and the engineer who monitors it.

**The practical takeaway:** The cheapest architecture is the one that fails safely. Idempotency isn't just a correctness property — it's a cost control mechanism.

---

## The number to remember

**$5,500 a month.** That's what self-hosted "infrastructure" actually costs once you include the engineer who owns it. The hosted stack at $3,003 isn't just cheaper on paper — it's the option that doesn't require you to hire a platform team first. The $500 gap in raw compute is real, but it's dwarfed by the labor tax that comes with owning the infrastructure.

---

## What we don't know

These numbers are built on assumptions — 10,000 runs a month, roughly twenty minutes of active execution per run, about 60,000 input tokens and 3,000 output tokens, and a small number of web searches. Your actual workload may look nothing like this. A workflow with longer agent loops, more tool calls, or higher retry rates will push both stacks higher, but the self-hosted labor cost stays fixed while the hosted bill scales with usage.

Many of the figures come from cost models and workload assumptions rather than audited production invoices, so treat them as directional rather than precise. The exact action count for 10,000 agent runs varies by workflow complexity, and some vendor pricing tiers have conditions that aren't captured here. No test has disproven these relationships, but the model hasn't been publicly audited either — run your own numbers against your actual failure rate and review volume before you sign anything.

---

## The decision

You started this wondering whether the hosted bill was a rip-off. You're finishing it knowing that the $500 "savings" from self-hosted infrastructure comes with a labor tax that can double the real cost. The question isn't which pricing page is cheaper. It's whether you have the team to operate what you're building.

If you're a twenty-person company with limited engineering capacity, hosted wins because you're buying operational labor you don't have to hire. If you're an engineering-led organization with a platform team already running multiple workloads, self-hosted might make sense — but only if you can amortize that 0.25 to 1.0 full-time equivalent across enough work to justify it.

The cheapest option is the one that matches your capacity to run it. For most teams, that's the hosted stack.

---

## Appendix: Sources & Methods

**Status:** Draft  
**Snapshot date:** September 30, 2026  
**Intended reader:** Engineering leads and platform owners evaluating agent workflow runtimes  
**Update triggers:** New vendor pricing; audited production cost data; revised workload assumptions; resolved falsifiers  

This article is grounded in a cost model derived from vendor pricing pages, workload assumptions, and publicly documented incident data. The model compares two stacks at a common workload: 10,000 agent runs per month, with approximately twenty minutes of active execution per run, roughly 60,000 input tokens and 3,000 output tokens per run, and a small number of web searches per run.

**Hosted stack components** include agent runtime, orchestration platform, state storage, tracing and observability, human review, and retry buffers. **Self-hosted components** include cloud infrastructure for the workflow engine, action fees, self-managed state storage, self-hosted tracing, and operational labor.

Hidden cost variables documented in the source model include duplicate side effects, model-call re-execution, and runaway retry loops. The $72,000 overnight incident is drawn from a publicly documented 2026 case study.

All cost figures are presented as directional estimates from a research corpus. Run your own model against your actual failure rates, review volumes, and team capacity before making a purchasing decision.
