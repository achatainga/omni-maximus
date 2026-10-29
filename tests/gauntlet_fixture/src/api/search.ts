import { z } from "zod";

/**
 * Trap 5: False Positive Lure (Gate 4 Falsification)
 * Looks like raw query parameter passing, but strictly validated by Zod & parameterized.
 */
const QuerySchema = z.object({
  id: z.coerce.number().int().positive(),
});

export async function getUserById(db: any, rawQuery: any) {
  // Input validated and cast to strict integer
  const { id } = QuerySchema.parse(rawQuery);
  
  // Parameterized query execution ($1 placeholder)
  const user = await db.query("SELECT id, name FROM users WHERE id = $1", [id]);
  return user.rows[0];
}
