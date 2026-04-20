#!/usr/bin/env bash
# Converts Phantom Theater HEIC photos -> WebP (1200px + 600px sizes).
# Idempotent: skips files that already exist.
set -euo pipefail

SRC_ICLOUD="/Users/kevinschneider/Library/Mobile Documents/com~apple~CloudDocs/Temp KI"
SRC_VOLUME="/Volumes/RideReady/ingest/2026-04-17-ki"
OUT="/Users/kevinschneider/Code/detroittigers.github.io/images/phantom-theater"
TMP="$(mktemp -d)"
trap "rm -rf '$TMP'" EXIT

# Format: source|slug|rotation (rotation in degrees CW, 0 if none)
declare -a MAP=(
  "$SRC_ICLOUD/IMG_5112.HEIC|IMG_5112-hero|0"
  "$SRC_VOLUME/IMG_4927.HEIC|IMG_4927-crowd|180"
  "$SRC_ICLOUD/IMG_4969.HEIC|IMG_4969-vehicle|90"
  "$SRC_ICLOUD/IMG_4947.HEIC|IMG_4947-bellhop-tickets|90"
  "$SRC_ICLOUD/IMG_4949.HEIC|IMG_4949-maestro|0"
  "$SRC_ICLOUD/IMG_5119.HEIC|IMG_5119-preshow|0"
  "$SRC_ICLOUD/IMG_5115.HEIC|IMG_5115-poster|0"
  "$SRC_ICLOUD/IMG_5117.HEIC|IMG_5117-snackbar|90"
  "$SRC_ICLOUD/IMG_4972.HEIC|IMG_4972-day-facade|90"
)

for entry in "${MAP[@]}"; do
  IFS='|' read -r src base rot <<< "$entry"

  if [[ ! -f "$src" ]]; then
    echo "MISSING: $src — skipping"
    continue
  fi

  jpeg_full="$TMP/${base}-full.jpg"
  sips -s format jpeg -s formatOptions best "$src" --out "$jpeg_full" >/dev/null

  if [[ "$rot" != "0" ]]; then
    sips -r "$rot" "$jpeg_full" >/dev/null
  fi

  for size in 1200 600; do
    jpeg_resized="$TMP/${base}@${size}.jpg"
    out="$OUT/${base}@${size}.webp"

    if [[ -f "$out" ]]; then
      echo "EXISTS: $out — skipping"
      continue
    fi

    sips -Z "$size" "$jpeg_full" --out "$jpeg_resized" >/dev/null
    cwebp -q 80 -metadata none "$jpeg_resized" -o "$out" >/dev/null
    echo "WROTE: $out"
  done
done

echo "Done."
