/**
 * Trap 2: Concurrency 10x Race Condition (SEV-2)
 * Reading balance, checking, and updating without a lock or atomic CAS.
 */
export async function deductCredits(db: any, userId: string, amount: number): Promise<boolean> {
  const account = await db.query("SELECT credits FROM user_accounts WHERE user_id = $1", [userId]);
  
  if (account.rows[0].credits >= amount) {
    // Simulating async network delay between read and write
    await new Promise((r) => setTimeout(r, 50));
    
    await db.query("UPDATE user_accounts SET credits = credits - $1 WHERE user_id = $2", [amount, userId]);
    return true;
  }
  return false;
}
