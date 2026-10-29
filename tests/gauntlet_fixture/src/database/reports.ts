/**
 * Trap 3: Unbounded Database Query (SEV-5)
 * Querying unbounded logs without a LIMIT clause or pagination.
 */
export async function getAuditReport(db: any, tenantId: string): Promise<any[]> {
  const result = await db.query(
    "SELECT id, action, payload, created_at FROM audit_logs WHERE tenant_id = $1 ORDER BY created_at DESC",
    [tenantId]
  );
  return result.rows;
}
