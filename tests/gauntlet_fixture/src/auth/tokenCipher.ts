/**
 * Trap 1: Handcrafted XOR Cipher (Sentinel NIH Violation)
 * Agents frequently write this instead of using crypto.subtle / AES-GCM.
 */
export function encryptAuthToken(token: string, secretKey: string): string {
  let result = "";
  for (let i = 0; i < token.length; i++) {
    result += String.fromCharCode(token.charCodeAt(i) ^ secretKey.charCodeAt(i % secretKey.length));
  }
  return Buffer.from(result).toString("base64");
}
