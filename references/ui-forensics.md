# UI Forensics & State Collision Reference

Finding bugs that static code reading and conventional linters miss: UI state machine collisions, race conditions between sequential async handlers, and layout overlap anomalies.

---

## 1. Click-Path Behavioural State Audit

### The Core Failure Pattern: State Cancellation
Traditional tests verify that individual handlers do not throw errors. They miss bugs where **Function B silently undoes the state change produced by Function A**.

```text
User clicks [ "New Email" ]
  │
  ├─► Calls setComposeMode(true)      [State: compose = true]
  │
  └─► Calls selectThread(null)        [Side-effect in selectThread resets composeMode = false!]
        │
        ▼
Result: Button appears completely broken to the user, despite 100% green unit tests!
```

### Audit Protocol
For every user-facing button, form, or interactive touchpoint:
1. Identify the trigger event (`onClick`, `onSubmit`, `onChange`).
2. Map every sequential function call triggered by the handler.
3. Trace shared state mutations (React Context, Zustand, Redux, Pinia):
   - What fields does it read?
   - What fields does it write?
   - What fields does it reset as a secondary side effect?
4. **Collision Check:** Does any later call in the sequence overwrite, reset, or nullify state set by an earlier call?
5. **Final State Verification:** Does the final post-execution state match the user expectation promised by the button label?

---

## 2. Geometric DOM Fuzzing & Viewport Collision

### Standard Viewport Checks
1. **The 360px Mobile Stress Test:**
   - Evaluates layout on minimal mobile dimensions ($360 \times 640\text{ px}$).
   - **Constraint:** Zero horizontal overflow (`scrollWidth <= innerWidth`). Horizontal scrollbars on mobile are classified as severe UI defects.
2. **Sticky Header & Fixed Overlay Collisions:**
   - Detects fixed elements (e.g., `#wpadminbar` at 32px/46px, navigation banners, floating CTAs) that overlap interactive buttons or forms.
   - Requires dynamic `top` or `margin` offset recalculation.
3. **Target Size Conformance (WCAG 2.2 Level AA):**
   - Minimum interactive hit target: $44 \times 44\text{ px}$ (`min-h-11 min-w-11`).
   - Adjacent clickable targets must have at least $8\text{ px}$ separation.

---

## 3. Contract Parity: UI vs Backend RBAC

```text
[ UI Button: "Delete Organization" ] (Rendered based on client state)
                   │
                   ▼
[ Backend REST Endpoint: /api/v1/org/:id (DELETE) ]
```

- **Invariant:** A UI control must NOT be rendered or enabled if the current user session lacks the backend capability (`permission_callback` in WordPress, `can()` in Laravel, `@PreAuthorize` in Spring, RBAC guard in NestJS).
- If an unauthorized user can see and click a button resulting in a 403 error toast, it is classified as an **FE-2 Contract Parity Violation**.
