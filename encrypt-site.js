#!/usr/bin/env node
/**
 * Post-build script: encrypt all HTML files in the mdBook output directory.
 *
 * Usage:
 *   BOOK_PASSWORD=secret node encrypt-site.js
 *
 * Requires: pagecrypt (npm install -D pagecrypt)
 */

import { readdir } from "node:fs/promises";
import { join } from "node:path";
import { encrypt } from "pagecrypt";

const SITE_DIR = "output/site";

const password = (process.env.BOOK_PASSWORD ?? "").trim();
if (!password) {
  console.error("Error: BOOK_PASSWORD environment variable is not set or is empty.");
  process.exit(1);
}

async function findHtmlFiles(dir) {
  const entries = await readdir(dir, { withFileTypes: true, recursive: true });
  return entries
    .filter((e) => e.isFile() && e.name.endsWith(".html"))
    .map((e) => join(e.parentPath ?? e.path, e.name));
}

const files = await findHtmlFiles(SITE_DIR);
console.log(`Encrypting ${files.length} HTML files in ${SITE_DIR}/...`);

for (const file of files) {
  await encrypt(file, file, password);
}

console.log("Done — all pages are now password-protected.");
