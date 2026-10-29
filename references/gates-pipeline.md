# The 6 Deterministic Hard Gates Pipeline

OMNI-MAXIMUS enforces a zero-bypass verification sequence. Every code review, feature branch, or pre-production check must pass each gate sequentially.

---

## Gate 0: Supply Chain & Sentinel NIH Shield

```text
Input: Dependency manifests (package.json, composer.json, Cargo.lock, requirements.txt, .env.example)
Objective: Ensure zero unauthorized dependencies and zero handcrafted security wheels.
```

### Verification Criteria
1. **Lockfile Enforcement:** If dependencies are listed in a manifest, an exact lockfile (`package-lock.json`, `composer.lock`, etc.) must exist and be committed. Wildcards (`*`, `latest`, `^99.0.0`) are classified as P0 Supply Chain risks.
2. **Secrets Detection:** Regex and entropy scan for unencrypted API tokens, private keys, database passwords, and test JWT secrets in production paths.
3. **Sentinel NIH (Not-Invented-Here) Filter:** Detects and blocks:
   - Handcrafted cryptography (e.g., custom XOR ciphers, manual AES implementations, homebrew PRNGs).
   - Custom JWT/Bearer token parsers (must use audited standard libraries like `jsonwebtoken`, `jose`, or `firebase/php-jwt`).
   - Artisanal regex parsers for structured syntax (HTML, SQL, email) susceptible to ReDoS (Regular Expression Denial of Service).

---

## Gate 1: AST Cartography & Attack Surface Mapping

```text
Input: Repository root
Objective: Map every external entry point and establish data-flow boundaries to critical sinks.
```

### Verification Criteria
1. **Surface Inventory:** Systematically identify all:
   - Public HTTP/REST/GraphQL endpoints.
   - Webhook listeners.
   - Background job consumers & cron tasks.
   - CLI commands & administrative scripts.
2. **Sink Mapping:** For each entry point, trace the AST call graph to determine if it can reach:
   - File system I/O (uploads, temp files, shell execution).
   - Database mutation layer (`INSERT`, `UPDATE`, `DELETE`, raw queries).
   - Financial / inventory transactions (credits, balance, checkout).
   - External third-party APIs (payment gateways, notification providers).

---

## Gate 2: SRE Physical Limits & Taint Matrix (SEV-1 to SEV-7)

```text
Input: Code blocks on the attack surface (-15 to +15 lines around data sinks)
Objective: Audit against physical computer limits (RAM heap, socket file descriptors, DB pool, lock contention).
```

### Verification Criteria
1. **SEV-1 (Taint & Uploads):** Magic-byte MIME checking, cryptographically randomized filenames (SHA-256), non-executable permissions.
2. **SEV-2 (Concurrency 10x):** Mutex distributed locking, optimistic CAS with retry counters, or pessimistic row locking (`SELECT FOR UPDATE`) on shared balances/stock.
3. **SEV-3 (I/O & Descriptors):** Mandatory cleanup of file handles and temp descriptors in `finally` blocks or language-native RAII.
4. **SEV-4 (Cascading Timeouts):** Hard timeout ($\le 1500$ ms) and circuit breaker pattern on all outbound network connections.
5. **SEV-5 (Unbounded DB Queries):** Explicit `LIMIT` clause on all bulk/list queries. Elimination of $N+1$ query loops via eager loading.
6. **SEV-6 (Memory Heap Quotas):** Payloads $> 64$ KB must be streamed in chunks $\le 8192$ bytes.
7. **SEV-7 (Timing Attacks):** Constant-time comparison (`timingSafeEqual`) on tokens, hashes, and secrets.

---

## Gate 3: UI Forensics & State Collision

```text
Input: Frontend components, state stores (React, Vue, Zustand, Redux), DOM layouts
Objective: Catch UI race conditions, conflicting state setters, and accessibility violations.
```

### Verification Criteria
1. **Click-Path State Audit:** Trace every button click through its state-setter chain to detect silent cancellations (Function B resetting state set by Function A).
2. **DOM Geometry Collision:** Verify touch targets $\ge 44 \times 44$ px, sticky header offsets (e.g., `#wpadminbar`), and zero horizontal overflow on 360px mobile viewports.
3. **Accessibility (WCAG 2.2 AA):** Minimum contrast of 4.5:1 (regular text) and 3:1 (large text/controls).
4. **RBAC Parity:** Visible UI elements must have identical authorization checks on their backing REST endpoints.

---

## Gate 4: Mandatory PoC Falsification

```text
Input: Potential vulnerability candidates from Gates 0-3
Objective: Prove the vulnerability with an executable exploit or discard it as a false positive.
```

### Verification Criteria
Every confirmed issue must provide the `<falsation_audit>` block with:
- The exact curl command, HTTP body, or concurrency script.
- The expected vs actual response demonstrating breach or failure.
- If no exploit can be formulated due to mitigating middleware or typing, the alert is declared a **FALSE POSITIVE**.

---

## Gate 5: Surgical Remediation & Santa Method Convergence

```text
Input: Confirmed issues with reproducible PoC
Objective: Apply minimal surgical diff and verify via dual independent reviewers.
```

### Verification Criteria
1. **Two-Phase Write:** Diff preview $\rightarrow$ Test pass $\rightarrow$ Final application.
2. **Santa Method (Check It Twice):** A secondary independent reviewer evaluates the patch against the 100-Point Scorecard. The patch is accepted only when score is $\ge 95/100$.
