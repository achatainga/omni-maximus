"""
Generate 4 high-resolution promotional screenshots for OMNI-MAXIMUS Agensi listing.
"""
import os
import asyncio
from playwright.async_api import async_playwright

SCREENSHOTS = [
    {
        "title": "OMNI-MAXIMUS — The 6 Deterministic Hard Gates Pipeline",
        "tag": "GATE 0 - GATE 2 PIPELINE",
        "content": """
<div style="font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 1.6; color: #e2e8f0;">
  <div style="color: #a855f7; font-weight: bold; margin-bottom: 12px;">🛡️ OMNI-MAXIMUS v18.0 — ADVERSARIAL SRE & APPSEC AUDIT</div>
  
  <div style="background: rgba(168, 85, 247, 0.1); border-left: 3px solid #a855f7; padding: 10px 14px; margin-bottom: 16px; border-radius: 4px;">
    <span style="color: #c084fc; font-weight: bold;">[GATE 0: SUPPLY CHAIN & SENTINEL NIH SHIELD]</span><br/>
    • Lockfiles: <span style="color: #4ade80;">VERIFIED (package-lock.json, composer.lock)</span><br/>
    • Secrets Scan: <span style="color: #4ade80;">ZERO HARDCODED TOKENS DETECTED</span><br/>
    • Sentinel NIH: <span style="color: #fbbf24;">BLOCKED: Handcrafted XOR cipher in auth/token.ts (Enforcing crypto.subtle)</span>
  </div>

  <div style="background: rgba(59, 130, 246, 0.1); border-left: 3px solid #3b82f6; padding: 10px 14px; margin-bottom: 16px; border-radius: 4px;">
    <span style="color: #60a5fa; font-weight: bold;">[GATE 1: AST ATTACK SURFACE INVENTORY]</span><br/>
    • Surface Mapped: <strong>24 Public Endpoints</strong> (18 REST, 3 Webhooks, 3 Cron Workers)<br/>
    • Top Centrality Nodes: <span style="color: #93c5fd;">OrderController, WalletService, DispatchPipeline</span><br/>
    • Sinks Reached: 4 Database Mutations, 2 External Payment Gateways, 1 Shell Execution
  </div>

  <div style="color: #f59e0b; font-weight: bold;">[GATE 2: SRE PHYSICAL LIMITS VERIFICATION]</div>
  <div style="color: #94a3b8; font-size: 12px;">Scanning for memory bloat (>8KB chunks), unbounded queries, and race conditions...</div>
</div>
        """
    },
    {
        "title": "SRE Chaos Engineering: 10x Concurrency & Physical Bounds",
        "tag": "GATE 2: PHYSICAL LIMITS (SEV-1..7)",
        "content": """
<div style="font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 1.6; color: #e2e8f0;">
  <div style="color: #ef4444; font-weight: bold; margin-bottom: 10px;">⚠️ SEV-2 DETECTED: CONCURRENCY DOUBLE-SPEND IN WALLET SERVICE</div>
  
  <div style="background: #1e1e2e; border: 1px solid #313244; padding: 12px; border-radius: 6px; margin-bottom: 14px;">
    <div style="color: #f38ba8;">// VULNERABLE CODE AT src/services/wallet.ts:42</div>
    <div style="color: #cdd6f4;">const user = await db.users.findUnique({ where: { id } });</div>
    <div style="color: #f38ba8; text-decoration: line-through;">if (user.balance >= amount) { await db.users.update(...); } // RACE CONDITION</div>
  </div>

  <div style="background: rgba(34, 197, 94, 0.1); border-left: 3px solid #22c55e; padding: 10px 14px; margin-bottom: 14px; border-radius: 4px;">
    <div style="color: #4ade80; font-weight: bold;">🛡️ OMNI-MAXIMUS SRE DEFENSE: COMPARE-AND-SWAP (CAS) ATOMIC LOCK</div>
    <div style="color: #86efac; font-size: 12px; margin-top: 4px;">
      Applied atomic condition: <code>UPDATE users SET balance = balance - :amt WHERE id = :id AND balance >= :amt</code><br/>
      Concurrency 10x Stress Test: <strong>10 simultaneous requests executed -> 1 Succeeded, 9 Correctly Rejected with 409 Conflict</strong>.
    </div>
  </div>

  <div style="color: #38bdf8; font-size: 12px;">
    • DB Query Limits: <span style="color: #4ade80;">Enforced LIMIT 50 on all list endpoints (Prevents connection pool starvation)</span><br/>
    • Heap Stream Quotas: <span style="color: #4ade80;">Payloads > 64KB piped in 8192-byte chunks</span>
  </div>
</div>
        """
    },
    {
        "title": "Zero False Positives: Autonomous PoC Exploit Synthesizer",
        "tag": "GATE 4: MANDATORY POC FALSIFICATION",
        "content": """
<div style="font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 1.6; color: #e2e8f0;">
  <div style="color: #a855f7; font-weight: bold; margin-bottom: 10px;">⚡ &lt;falsation_audit&gt; BLOCK: EXECUTABLE PROOF-OF-CONCEPT</div>
  
  <div style="background: #0f172a; border: 1px solid #1e293b; padding: 12px; border-radius: 6px; margin-bottom: 14px;">
    <div style="color: #38bdf8; font-weight: bold;">1. TAINT CHECK:</div>
    <div style="color: #94a3b8; font-size: 12px;">Client-controlled JSON property 'order_id' reaches raw SQL query at line 118 without int-casting or permission check.</div>

    <div style="color: #38bdf8; font-weight: bold; margin-top: 8px;">2. EXECUTABLE EXPLOIT VECTOR:</div>
    <div style="background: #020617; padding: 8px; border-radius: 4px; color: #f43f5e; font-size: 12px;">
      curl -s -X POST https://api.prod/orders/cancel \\<br/>
      &nbsp;&nbsp;-H "Content-Type: application/json" \\<br/>
      &nbsp;&nbsp;-d '{"order_id": "999 OR 1=1"}'
    </div>

    <div style="color: #38bdf8; font-weight: bold; margin-top: 8px;">3. RUNTIME VERDICT:</div>
    <div style="color: #f43f5e; font-weight: bold;">CONFIRMED VULNERABILITY (P0) — Replicable exploit verified.</div>
  </div>

  <div style="background: rgba(168, 85, 247, 0.15); border: 1px solid rgba(168, 85, 247, 0.3); padding: 8px 12px; border-radius: 4px; font-size: 12px; color: #d8b4fe;">
    <strong>Guaranteed Anti-Hallucination:</strong> If an alert cannot be reproduced with a real payload, OMNI-MAXIMUS discards it as a False Positive. No wasted developer hours.
  </div>
</div>
        """
    },
    {
        "title": "UI Forensics, State Collision & Resilience Certification",
        "tag": "GATE 3 & 5: DUAL-BRAIN CERTIFICATION",
        "content": """
<div style="font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 1.6; color: #e2e8f0;">
  <div style="display: flex; gap: 12px; margin-bottom: 14px;">
    <div style="flex: 1; background: rgba(56, 189, 248, 0.1); border: 1px solid #0284c7; padding: 10px; border-radius: 4px;">
      <div style="color: #38bdf8; font-weight: bold;">UI CLICK-PATH AUDIT</div>
      <div style="font-size: 11px; color: #bae6fd; margin-top: 4px;">
        • State Cancellation: <span style="color: #4ade80;">ZERO CONFLICTS</span><br/>
        • 360px Viewport: <span style="color: #4ade80;">NO HORIZONTAL OVERFLOW</span><br/>
        • WCAG 2.2 AA Contrast: <span style="color: #4ade80;">PASS (5.2:1)</span><br/>
        • Touch Targets: <span style="color: #4ade80;">>= 44x44px</span>
      </div>
    </div>
    
    <div style="flex: 1; background: rgba(168, 85, 247, 0.1); border: 1px solid #7e22ce; padding: 10px; border-radius: 4px;">
      <div style="color: #c084fc; font-weight: bold;">SANTA METHOD VERIFICATION</div>
      <div style="font-size: 11px; color: #e9d5ff; margin-top: 4px;">
        • Generator Agent: <span style="color: #4ade80;">Patch Generated</span><br/>
        • Independent Reviewer: <span style="color: #4ade80;">PASSED</span><br/>
        • 4-Voice Council: <span style="color: #4ade80;">CONSENSUS REACHED</span><br/>
        • Convergence Loop: <span style="color: #4ade80;">1 Iteration</span>
      </div>
    </div>
  </div>

  <div style="background: #0f172a; border: 2px solid #22c55e; padding: 12px; border-radius: 6px;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
      <span style="color: #4ade80; font-weight: bold; font-size: 14px;">🛡️ OMNI-MAXIMUS RESILIENCE SCORECARD: 98 / 100</span>
      <span style="background: #166534; color: #dcfce7; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: bold;">CERTIFIED PROD-READY</span>
    </div>
    <div style="color: #94a3b8; font-size: 11px; margin-top: 6px;">
      AppSec: 25/25 | Concurrency: 20/20 | SRE Limits: 20/20 | UI State: 19/20 | Supply Chain: 14/15
    </div>
  </div>
</div>
        """
    }
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      width: 1280px;
      height: 720px;
      background: radial-gradient(circle at 50% 20%, #1e1138 0%, #0c0818 60%, #05030a 100%);
      color: #f8fafc;
      font-family: 'Inter', sans-serif;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 40px;
      overflow: hidden;
    }}
    .window {{
      width: 1160px;
      height: 640px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(168, 85, 247, 0.4);
      border-radius: 16px;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.9), 0 0 50px rgba(168, 85, 247, 0.2);
      display: flex;
      flex-direction: column;
      backdrop-filter: blur(20px);
      overflow: hidden;
    }}
    .window-header {{
      height: 48px;
      background: rgba(30, 41, 59, 0.6);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      padding: 0 16px;
      gap: 12px;
    }}
    .dots {{ display: flex; gap: 8px; }}
    .dot {{ width: 12px; height: 12px; border-radius: 50%; }}
    .dot.red {{ background: #ff5f56; }}
    .dot.yellow {{ background: #ffbd2e; }}
    .dot.green {{ background: #27c93f; }}
    .window-title {{
      font-size: 13px;
      color: #94a3b8;
      font-weight: 600;
      letter-spacing: 0.5px;
      flex: 1;
      text-align: center;
    }}
    .badge {{
      background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%);
      color: white;
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 20px;
      letter-spacing: 0.8px;
    }}
    .window-body {{
      flex: 1;
      padding: 28px 36px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .headline {{
      margin-bottom: 16px;
    }}
    .headline h1 {{
      font-size: 24px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.5px;
    }}
    .headline p {{
      font-size: 13px;
      color: #cbd5e1;
      margin-top: 4px;
    }}
    .terminal-box {{
      background: #020617;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 10px;
      padding: 20px;
      flex: 1;
      box-shadow: inset 0 2px 8px rgba(0,0,0,0.6);
    }}
  </style>
</head>
<body>
  <div class="window">
    <div class="window-header">
      <div class="dots">
        <div class="dot red"></div>
        <div class="dot yellow"></div>
        <div class="dot green"></div>
      </div>
      <div class="window-title">OMNI-MAXIMUS Enterprise • Autonomous Adversarial SRE & AppSec Engine</div>
      <div class="badge">{tag}</div>
    </div>
    <div class="window-body">
      <div class="headline">
        <h1>{title}</h1>
        <p>Zero-Sycophancy Verification Layer for Claude Code, Cursor, Windsurf & Antigravity</p>
      </div>
      <div class="terminal-box">
        {content}
      </div>
    </div>
  </div>
</body>
</html>
"""

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 720})

        desktop = os.path.expanduser("~/Desktop")

        for idx, item in enumerate(SCREENSHOTS, 1):
            html = HTML_TEMPLATE.format(
                tag=item["tag"],
                title=item["title"],
                content=item["content"]
            )
            await page.set_content(html)
            await page.wait_for_timeout(300)

            local_path = f"C:/code/omni-maximus/screenshots/screenshot-{idx}.png"
            desktop_path = os.path.join(desktop, f"omni-maximus-screenshot-{idx}.png")

            await page.screenshot(path=local_path)
            await page.screenshot(path=desktop_path)
            print(f"Generated Screenshot {idx}: {desktop_path}")

        await browser.close()
        print("All 4 screenshots generated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
