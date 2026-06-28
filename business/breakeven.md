# breakeven.md  

## 1. Unit Economics (per **active** user / month)

| Cost Component | Assumptions | Monthly Cost (USD) |
|----------------|-------------|--------------------|
| **Compute** | • Avg. 100 k prompt‑completion tokens per user<br>• Benchmark runs on our own GPU fleet (≈ $0.05 per 1 k tokens) | **$5.00** |
| **Storage** | • 10 MB of raw logs & results per user<br>• S3 Standard $0.023/GB | **$0.002** |
| **Bandwidth** | • 20 MB inbound + outbound per user<br>• $0.02/GB egress (ingress free) | **$0.0004** |
| **Total Variable Cost** |  | **≈ $5.01** → round to **$5.00** per active user |

> **Note:** Variable cost is dominated by compute; storage & bandwidth are < 0.1 % of total and can be ignored for high‑level sizing.

---

## 2. Pricing Tiers  

| Tier | Monthly Price | Core Features | Token Quota (approx.) | Support |
|------|---------------|---------------|-----------------------|---------|
| **Free** | **$0** | • Dashboard with 1‑provider comparison<br>• 5 k tokens / month<br>• Community forum | 5 k | Community only |
| **Pro** | **$29** | • Up to 200 k tokens / mo<br>• Multi‑provider side‑by‑side charts<br>• Alerting on latency / cost drift<br>• Export CSV / JSON | 200 k | Email (24 h) |
| **Enterprise** | **$149** | • Unlimited tokens<br>• SLA‑backed uptime (99.9 %)<br>• Dedicated account manager<br>• On‑prem / VPC deployment option<br>• Custom integration & branding | Unlimited | 24/7 Phone & Slack |

*Pricing is deliberately positioned between existing “LLM‑ops” tools (e.g., PromptLayer $30/mo, LLM‑Eval $199/mo) to capture both indie developers and early‑stage AI teams.*

---

## 3. Customer‑Acquisition Cost (CAC)

| Channel | Typical Spend per New Customer | Rationale |
|---------|--------------------------------|-----------|
| Content / SEO (blog, tutorials) | **$120 – $180** | Low‑cost, long‑tail; conversion ~2 % |
| Paid Developer Ads (Twitter, Reddit, StackOverflow) | **$250 – $400** | Higher CPL but faster pipeline |
| Partnerships / Marketplace listings | **$80 – $150** | Co‑sell with cloud providers, low overhead |

**Overall CAC range:** **$150 – $350** per acquired paying user (average ≈ $250).

---

## 4. Lifetime Value (LTV)

*Assumptions*  

* Monthly churn = **5 %** (typical for developer‑focused SaaS) → average lifetime = 1/0.05 = **20 months**.  
* Customer mix (steady‑state): **70 % Pro**, **30 % Enterprise**.  

**Weighted ARPU**  

\[
ARPU = 0.7 \times 29 + 0.3 \times 149 = 20.3 + 44.7 = **\$65**\text{/mo}
\]

**LTV**  

\[
LTV = ARPU \times \frac{1}{\text{churn}} = 65 \times 20 = **\$1,300**
\]

Even with a higher churn scenario (8 % → 12.5 mo) LTV stays > $800, comfortably above the CAC ceiling.

---

## 5. Break‑Even Users (Monthly)

### 5.1 Fixed Monthly Overhead (staff + ops)

| Role | Headcount | Monthly Salary (USD) |
|------|-----------|----------------------|
| Backend Engineer | 2 | $12,000 each |
| Front‑end Engineer | 1 | $11,000 |
| DevSecOps / Infra | 1 | $9,000 |
| Product Manager | 1 | $10,000 |
| Marketing / Community | 1 | $5,000 |
| **Total Fixed** | — | **$47,000** |

### 5.2 Break‑Even Calculation  

*Revenue per user* = tier price – variable cost  

| Scenario | Avg. Revenue / User (USD) | Users Needed |
|----------|---------------------------|--------------|
| **All Pro** (price $29) | 29 – 5 = **$24** | 47,000 / 24 ≈ **1,958** |
| **All Enterprise** (price $149) | 149 – 5 = **$144** | 47,000 / 144 ≈ **327** |
| **Mixed (70 % Pro / 30 % Enterprise)** | 0.7×24 + 0.3×144 = **$58.8** | 47,000 / 58.8 ≈ **800** |

> **Break‑Even Users (target)**: **≈ 800 mixed‑tier customers** (or 1,960 Pro‑only). This is the point where monthly revenue covers all fixed + variable costs.

---

## 6. Path to **$10 K MRR**

| Target MRR | Required Users (by tier) | Example Mix |
|------------|---------------------------|-------------|
| **$10,000** | 345 × Pro (345 × $29 = $10,005) | 345 Pro |
| **$10,000** | 67 × Enterprise (67 × $149 = $9,983) | 67 Enterprise |
| **$10,000** | 200 × Pro + 20 × Enterprise (200×29 + 20×149 = $8,800 + $2,980 = $11,780) | 200 Pro + 20 Ent |
| **$10,000** | 500 × Free (no revenue) + 150 × Pro (150×29 = $4,350) + 30 × Enterprise (30×149 = $4,470) → **$8,820** (still short) → add 10 more Enterprise → **$10,310** | Hybrid free‑to‑pay funnel |

**Practical go‑to‑market plan**  

1. **Launch Free tier** → capture 2–3 k developers in 3 months (conversion 5 % → 100‑150 paying).  
2. **Convert 30 % of Free to Pro** via in‑app nudges → ~45 Pro users → $1.3 K MRR.  
3. **Target early‑stage AI teams** → 10 Enterprise pilots at $149 → $1.5 K MRR.  
4. **Scale content & paid ads** to add ~200 Pro users per quarter → reach $10 K MRR by month 6.

---

## 7. Summary of Key Numbers  

| Metric | Value |
|--------|-------|
| Variable cost per active user | **$5.00** |
| Pricing (Pro / Enterprise) | **$29** / **$149** per month |
| CAC (average) | **$250** |
| ARPU (mixed) | **$65** |
| LTV (5 % churn) | **$1,300** |
| Fixed monthly overhead | **$47,000** |
| Break‑even users (mixed) | **≈ 800** |
| Users for $10 K MRR (Pro only) | **345** |
| Users for $10 K MRR (Enterprise only) | **67** |

These figures provide a concrete financial foundation for the **model‑metrics** platform and guide the next steps in go‑to‑market, fundraising, and resource planning.