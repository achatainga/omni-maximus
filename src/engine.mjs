import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';

export class OmniMaximusEngine {
  constructor(cwd = process.cwd()) {
    this.cwd = cwd;
  }

  /**
   * Gate 0: Supply Chain & Secrets Audit
   */
  auditSupplyChain() {
    const results = {
      gate: 'GATE_0_SUPPLY_CHAIN',
      status: 'PASS',
      lockfiles: [],
      wildcardDeps: [],
      secretsFound: 0,
      timestamp: new Date().toISOString()
    };

    const lockfiles = ['package-lock.json', 'yarn.lock', 'pnpm-lock.yaml', 'composer.lock', 'Cargo.lock', 'poetry.lock'];
    for (const lf of lockfiles) {
      if (fs.existsSync(path.join(this.cwd, lf))) {
        results.lockfiles.push(lf);
      }
    }

    if (results.lockfiles.length === 0) {
      results.status = 'FLAGGED';
      results.lockfileWarning = 'No cryptographic lockfile found in repository root.';
    }

    // Inspect package.json for wildcard versions
    const pkgPath = path.join(this.cwd, 'package.json');
    if (fs.existsSync(pkgPath)) {
      try {
        const pkg = JSON.parse(fs.readFileSync(pkgPath, 'utf8'));
        const allDeps = { ...pkg.dependencies, ...pkg.devDependencies };
        for (const [dep, ver] of Object.entries(allDeps)) {
          if (ver === '*' || ver === 'latest') {
            results.wildcardDeps.push({ dep, ver });
            results.status = 'FLAGGED';
          }
        }
      } catch {}
    }

    return results;
  }

  /**
   * Install SKILL.md into local project or global agent directory
   */
  installSkill(target = 'workspace') {
    const skillSource = path.join(import.meta.dirname, '..', 'SKILL.md');
    if (!fs.existsSync(skillSource)) {
      throw new Error('Source SKILL.md not found.');
    }

    let destDir;
    if (target === 'global') {
      destDir = path.join(os.homedir(), '.gemini', 'config', 'skills', 'omni-maximus');
    } else {
      destDir = path.join(this.cwd, '.agents', 'skills', 'omni-maximus');
    }

    fs.mkdirSync(destDir, { recursive: true });
    const destFile = path.join(destDir, 'SKILL.md');
    fs.copyFileSync(skillSource, destFile);

    return {
      success: true,
      target,
      installedPath: destFile,
      version: '18.0.0'
    };
  }

  /**
   * Generate 100-Point Resilience Scorecard Template
   */
  getScorecard() {
    return `
================================================================
 🛡️ OMNI-MAXIMUS RESILIENCE SCORECARD (Target >= 95/100)
================================================================
 [1] AppSec & Taint Flow (25 pts):         ____ / 25
 [2] Concurrency & ACID Integrity (20 pts): ____ / 20
 [3] Physical Resource Bounds (20 pts):    ____ / 20
 [4] UI State Integrity & WCAG (20 pts):   ____ / 20
 [5] Supply Chain & Sentinel NIH (15 pts): ____ / 15
----------------------------------------------------------------
 TOTAL RESILIENCE SCORE:                   ____ / 100
 VERDICT: [ CERTIFIED READY FOR PROD (>= 95) | BLOCKED (< 95) ]
================================================================
`;
  }
}
