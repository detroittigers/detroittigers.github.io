import os

# Mapping: Legacy Subpath -> New Target URL (Absolute)
REDIRECTS = {
    "epic-universe/2025-holiday-strategy": "https://rideready.app/parks/epic-universe/2025-holiday-strategy/",
    "epic-universe/mlk-day-weekend-2026": "https://rideready.app/parks/epic-universe/mlk-day-weekend-2026/",
    "epic-universe/presidents-day-weekend-2026": "https://rideready.app/parks/epic-universe/presidents-day-weekend-2026/"
}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url={target_url}">
    <script>window.location.href = "{target_url}" + window.location.search;</script>
    <title>Redirecting...</title>
    <!-- Canonical & OG for Link Previews -->
    <link rel="canonical" href="{target_url}">
    <meta property="og:url" content="{target_url}">
    <meta property="og:title" content="Page Moved - Ride Ready">
    <meta property="og:description" content="This guide has moved to a new location. Redirecting you now.">
    <!-- Basic Image Fallback if available, otherwise generic -->
    <meta property="og:image" content="https://rideready.app/images/logo.png">
</head>
<body>
    <p>Moved to <a href="{target_url}">{target_url}</a></p>
</body>
</html>
"""

def generate_redirects():
    for legacy_path, target_url in REDIRECTS.items():
        # Ensure directory exists
        if not os.path.exists(legacy_path):
            os.makedirs(legacy_path)
            print(f"Created directory: {legacy_path}")
        
        # Write index.html
        file_path = os.path.join(legacy_path, "index.html")
        content = TEMPLATE.format(target_url=target_url)
        
        with open(file_path, "w") as f:
            f.write(content)
        
        print(f"Generated redirect at: {file_path} -> {target_url}")

if __name__ == "__main__":
    generate_redirects()
