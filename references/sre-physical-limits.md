# SRE Physical Limits & Chaos Engineering Standards

Computers operate under the unyielding laws of physics: CPU clock cycles, memory bus bandwidth, socket descriptor tables, and disk I/O queue depths. Code that ignores these limits fails under stress.

OMNI-MAXIMUS enforces the following concrete thresholds across all backend codebases:

---

## 1. Physical Threshold Matrix

| Resource Domain | Physical Failure Mode | Hard Rule / Threshold | Architectural Requirement |
| :--- | :--- | :--- | :--- |
| **Database Pool** | Connection starvation under 100 req/s | All collection queries MUST have explicit `LIMIT` ($\le 100$). | Indexed pagination; no `SELECT *` without limit; eager-load relations. |
| **Heap Memory** | Out-Of-Memory (OOM) kill under file upload | Buffers $> 64$ KB must be processed as streams ($\le 8192$ bytes/chunk). | Stream piping (`fs.createReadStream`, `php://input` in chunks). |
| **Socket Descriptors** | File descriptor leak (`EMFILE: too many open files`) | Explicit timeout on all HTTP clients $\le 1500$ ms. | Connection pooling with keep-alive and strict max sockets quota. |
| **Shared State & Balances** | Double-spending / stock overselling | Concurrency 10x MUST use ACID transactions or CAS locks. | `SELECT ... FOR UPDATE` or atomic `UPDATE tbl SET bal = bal - x WHERE id = y AND bal >= x`. |
| **File System I/O** | Disk inode exhaustion / lingering temp files | Temporary files must be created in volatile storage (`/dev/shm` or OS temp). | Guaranteed deletion in `finally` / shutdown hooks. |
| **Authentication CPU** | ReDoS / Timing side-channel attack | Constant-time string equality; bounded regex execution. | `crypto.timingSafeEqual`; reject nested regex quantifiers `(a+)+`. |

---

## 2. Concurrency 10x Simulation Pattern

When evaluating high-traffic endpoints (checkout, debit, balance update, ticket booking), OMNI-MAXIMUS applies the **10x Concurrent Burst Model**:

```text
Request 1  ───► [Read Balance: $100] ───► [Deduct $100] ───► [Save: $0]
Request 2  ───► [Read Balance: $100] ───► [Deduct $100] ───► [Save: -$100 (CORRUPT)]
```

### Required Defense: Compare-And-Swap (CAS) or Row Locking

```sql
-- Pessimistic Row Lock:
BEGIN TRANSACTION;
SELECT balance FROM accounts WHERE user_id = 42 FOR UPDATE;
-- Verify balance >= 100;
UPDATE accounts SET balance = balance - 100 WHERE user_id = 42;
COMMIT;
```

Or Optimistic Compare-And-Swap:

```sql
UPDATE accounts 
SET balance = balance - 100, version = version + 1 
WHERE user_id = 42 AND balance >= 100 AND version = :current_version;
```

---

## 3. The Circuit Breaker & Timeout Standard

Any external API call (e.g., Stripe, SendGrid, OpenAI, Webhooks) that does not specify a timeout is a **Severity 4 (Cascading Collapse)** risk.

- **Maximum Allowed Timeout:** $1,500\text{ ms}$ for synchronous user-facing requests.
- **Background Worker Timeout:** $10,000\text{ ms}$ with exponential backoff and jitter.
- **Fallback Requirement:** Every external dependency must have a defined fallback state (cached response, circuit trip, or queued job) when degraded.
