// Generate the Phantom Theater OG image by cropping the hero photo to 1200x630.
//
// We previously rendered tools/og-phantom-theater.html via puppeteer, but the
// puppeteer + Node 25 + Chrome-for-Testing stack on this machine times out on
// every Page.captureScreenshot call. Cropping the source HEIC directly via
// `sips` is reliable and produces a strong image — the night facade with the
// sign centered. Social platforms render the title and description from meta
// tags, so a text overlay isn't needed.
//
// Run: node tools/capture-og-phantom-theater.mjs
import { execSync } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';
import { existsSync, mkdtempSync, copyFileSync, rmSync } from 'fs';
import { tmpdir } from 'os';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SRC = '/Users/kevinschneider/Library/Mobile Documents/com~apple~CloudDocs/Temp KI/IMG_5112.HEIC';
const OUT = path.join(__dirname, '..', 'images', 'og', 'og-phantom-theater.png');

if (!existsSync(SRC)) {
  console.error(`Source HEIC missing: ${SRC}`);
  process.exit(1);
}

const tmp = mkdtempSync(path.join(tmpdir(), 'og-phantom-'));
const work = path.join(tmp, 'work.png');

try {
  execSync(`sips -s format png "${SRC}" --out "${work}"`, { stdio: 'pipe' });
  // Source is 5712x4284 (4:3). Crop to 5712x2991 (1.91:1) centered, then resample to 1200x630.
  execSync(`sips -c 2991 5712 "${work}"`, { stdio: 'pipe' });
  execSync(`sips --resampleHeightWidth 630 1200 "${work}"`, { stdio: 'pipe' });
  copyFileSync(work, OUT);
  console.log(`Captured: ${OUT}`);
} finally {
  rmSync(tmp, { recursive: true, force: true });
}
