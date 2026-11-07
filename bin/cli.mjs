#!/usr/bin/env node
import { OmniMaximusEngine } from '../src/engine.mjs';

const engine = new OmniMaximusEngine();
const command = process.argv[2] || 'audit';

console.log(`
\x1b[36m================================================================\x1b[0m
\x1b[1m\x1b[33m 🛡️ OMNI-MAXIMUS v18.0 — Autonomous Adversarial SRE & AppSec\x1b[0m
\x1b[36m================================================================\x1b[0m
\x1b[90m Zero-Sycophancy Axiom | 6 Deterministic Hard Gates | 100-Pt Rubric\x1b[0m
`);

if (command === 'install') {
  const isGlobal = process.argv.includes('--global');
  try {
    const res = engine.installSkill(isGlobal ? 'global' : 'workspace');
    console.log(`\x1b[32m✔ Skill installed successfully!\x1b[0m`);
    console.log(`  Target: \x1b[35m${res.installedPath}\x1b[0m`);
    console.log(`  Trigger with: \x1b[33m/omni-maximus\x1b[0m in your AI coding agent\n`);
  } catch (err) {
    console.error(`\x1b[31m✖ Installation failed: ${err.message}\x1b[0m`);
    process.exit(1);
  }
} else if (command === 'scorecard') {
  console.log(engine.getScorecard());
} else {
  // Default: audit
  console.log(`\x1b[1mRunning Gate 0: Supply Chain & Sentinel Verification...\x1b[0m`);
  const audit = engine.auditSupplyChain();
  console.log(`  Lockfiles: \x1b[32m${audit.lockfiles.join(', ') || 'NONE'}\x1b[0m`);
  if (audit.wildcardDeps.length > 0) {
    console.log(`  \x1b[31m✖ Wildcard dependencies detected:\x1b[0m`, audit.wildcardDeps);
  } else {
    console.log(`  \x1b[32m✔ Dependency pinning verified (No wildcards)\x1b[0m`);
  }
  console.log(`  Status: \x1b[32m${audit.status}\x1b[0m\n`);

  console.log(`\x1b[90mTip: Run \x1b[33mnpx @achatainga/omni-maximus install\x1b[90m to install the skill for Antigravity / Claude Code / Cursor.\x1b[0m\n`);
}
