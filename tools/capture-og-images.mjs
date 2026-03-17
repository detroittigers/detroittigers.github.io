import puppeteer from 'puppeteer';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(__dirname, 'og-image-generator.html');
const outDir = path.join(__dirname, '..', 'images', 'og');

const cards = [
  { selector: '.og-strategy', filename: 'og-strategy-guide.png' },
  { selector: '.og-crowd', filename: 'og-crowd-calendar.png' },
  { selector: '.og-spring', filename: 'og-spring-break.png' },
  { selector: '.og-home', filename: 'og-home.png' },
  { selector: '.og-queue', filename: 'og-mine-cart-madness.png' },
  { selector: '.og-generic', filename: 'og-default.png' },
];

const browser = await puppeteer.launch({ headless: true });
const page = await browser.newPage();
await page.setViewport({ width: 1400, height: 4000, deviceScaleFactor: 2 });
await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0' });

// Wait for fonts to load
await page.evaluate(() => document.fonts.ready);
await new Promise(r => setTimeout(r, 1000));

for (const card of cards) {
  const el = await page.$(card.selector);
  if (!el) {
    console.error(`Could not find ${card.selector}`);
    continue;
  }
  const outPath = path.join(outDir, card.filename);
  await el.screenshot({ path: outPath, type: 'png' });
  console.log(`Captured: ${card.filename}`);
}

await browser.close();
console.log(`\nDone! ${cards.length} images saved to ${outDir}`);
