// Generate the Phantom Theater OG image by cropping the committed hero WebP to 1200x630.
//
// We previously rendered tools/og-phantom-theater.html via puppeteer, but the
// puppeteer + Chrome-for-Testing stack on the author's machine times out on
// every Page.captureScreenshot call (irrespective of content). Cropping the
// source image with `sips` is reliable and produces a strong result — the
// night facade with the sign centered. Social platforms render the title and
// description from <meta> tags, so a text overlay isn't needed.
//
// Source: the committed 1200x900 hero WebP. No external assets required, so
// any contributor can regenerate this image from a clean clone.
//
// Run: node tools/capture-og-phantom-theater.mjs
import { execSync } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';
import { existsSync, mkdtempSync, copyFileSync, rmSync } from 'fs';
import { tmpdir } from 'os';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SRC = path.join(__dirname, '..', 'images', 'phantom-theater', 'IMG_5112-hero@1200.webp');
const OUT = path.join(__dirname, '..', 'images', 'og', 'og-phantom-theater.png');

if (!existsSync(SRC)) {
  console.error(`Source WebP missing: ${SRC}`);
  process.exit(1);
}

const tmp = mkdtempSync(path.join(tmpdir(), 'og-phantom-'));
const work = path.join(tmp, 'work.png');

try {
  // Convert WebP -> PNG (sips on macOS 12+ reads WebP).
  execSync(`sips -s format png "${SRC}" --out "${work}"`, { stdio: 'pipe' });
  // Source is 1200x900 (4:3). Crop to 1200x630 (1.91:1, OG ratio) centered.
  execSync(`sips -c 630 1200 "${work}"`, { stdio: 'pipe' });
  copyFileSync(work, OUT);
  console.log(`Captured: ${OUT}`);
} finally {
  rmSync(tmp, { recursive: true, force: true });
}
