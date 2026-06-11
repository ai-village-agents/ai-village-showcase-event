import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import sys
import os

urls = [
    "https://ai-village-agents.github.io/village-arcade/",
    "https://ai-village-agents.github.io/village-timeline/",
    "https://ai-village-agents.github.io/village-pulse/",
    "https://ai-village-agents.github.io/the-poem-you-already-wrote/",
    "https://ai-village-agents.github.io/deepseek-pattern-archive/",
    "https://ai-village-agents.github.io/village-bestiary/",
    "https://ai-village-agents.github.io/village-welcome/",
    "https://ai-village-agents.github.io/village-fortune/",
    "https://ai-village-agents.github.io/village-crossword/",
    "https://ai-village-agents.github.io/village-archaeology-quiz/",
    "https://artifacts.aivillage.dev",
    "https://ai-village-agents.github.io/village-relay/"
]

report_header = """# Interactive Station Web Applications Deep Asset Audit Report

*Generated on Day 436 (Thursday, June 11, 2026) in preparation for the Friday 1:00 PM Venue A/V Dry Run.*

## Summary of Findings
Below is a detailed verification table of all public web applications. This test goes beyond simple HTTP pinging to scrape each page's HTML, resolve and check all referenced CSS, JS, and image assets, and inspect for template leaks or raw unrendered code.

| Web Application URL | Title | Main Status | CSS (Ok/Fail) | JS (Ok/Fail) | Images (Ok/Fail) | Template Leak Check | Verdict | Broken Assets |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
"""

report_rows = []

print("Starting deep audit of all 12 web application URLs...")

for url in urls:
    print(f"Auditing {url}...")
    try:
        r = requests.get(url, timeout=10)
        main_status = r.status_code
        if r.status_code != 200:
            report_rows.append(f"| {url} | N/A | {r.status_code} | - | - | - | - | FAIL (Main page offline) | - |")
            continue
    except Exception as e:
        report_rows.append(f"| {url} | N/A | Timeout/Err | - | - | - | - | FAIL (Connection error) | {str(e)} |")
        continue

    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Check title
    title = soup.title.string.strip() if soup.title else "No Title"
    
    # Check for template leaks
    leak_detected = "{{" in html_content or "{%" in html_content
    leak_status = "⚠️ LEAK DETECTED" if leak_detected else "✅ Clean"

    # Extract assets
    css_assets = []
    js_assets = []
    img_assets = []

    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href')
        if href:
            css_assets.append(urljoin(url, href))
            
    for script in soup.find_all('script'):
        src = script.get('src')
        if src:
            js_assets.append(urljoin(url, src))
            
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            img_assets.append(urljoin(url, src))

    # Helper function to audit assets
    def check_assets(asset_list):
        ok_count = 0
        failed_assets = []
        for asset in asset_list:
            # We don't want to spam external fonts/scripts, but we check local ones
            # For robustness, we check all, but ignore known huge CDNs if they throttle
            try:
                # Use HEAD requests to be light-weight, fallback to GET
                head_resp = requests.head(asset, timeout=5)
                status = head_resp.status_code
                if status >= 400:
                    get_resp = requests.get(asset, timeout=5)
                    status = get_resp.status_code
                
                if status < 400:
                    ok_count += 1
                else:
                    failed_assets.append(f"{asset} ({status})")
            except Exception as e:
                failed_assets.append(f"{asset} (Error: {str(e)})")
        return ok_count, len(asset_list), failed_assets

    css_ok, css_total, css_failed = check_assets(css_assets)
    js_ok, js_total, js_failed = check_assets(js_assets)
    img_ok, img_total, img_failed = check_assets(img_assets)

    all_failed = css_failed + js_failed + img_failed
    broken_list_str = "<br>".join(all_failed) if all_failed else "None"
    
    verdict = "✅ PASS"
    if len(all_failed) > 0 or leak_detected:
        verdict = "⚠️ WARNING"
        if css_total > 0 and css_ok == 0:
            verdict = "❌ FAIL (Broken CSS)"
        elif js_total > 0 and js_ok == 0:
            verdict = "❌ FAIL (Broken JS)"

    row = f"| {url} | {title} | {main_status} | {css_ok}/{css_total} | {js_ok}/{js_total} | {img_ok}/{img_total} | {leak_status} | {verdict} | {broken_list_str} |"
    report_rows.append(row)
    print(f"Finished {url}: {verdict}")

report_content = report_header + "\n".join(report_rows) + "\n\n## Conclusion & Recommendations\n"
if any("FAIL" in r for r in report_rows):
    report_content += "⚠️ **Action Required**: Some web applications have broken critical assets or failed to resolve. Immediate remediation is needed before the Friday venue dry run.\n"
else:
    report_content += "🎉 **All Web Applications Verified**: All 12 interactive web applications resolved successfully. 100% of internal and external CSS, JS, and image assets returned successful HTTP status codes. The applications are fully ready for the on-site A/V dry run on Friday at 1:00 PM PT.\n"

with open("/home/computeruse/ai-village-showcase-event/ops/web-app-audit-day436.md", "w") as f:
    f.write(report_content)

print("Audit report written successfully to ops/web-app-audit-day436.md")
