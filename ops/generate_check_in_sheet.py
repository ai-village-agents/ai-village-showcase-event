#!/usr/bin/env python3
import csv
import sys
import os
import subprocess

def main():
    # Define default filepaths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "ops", "rsvp-backup-tracker-template.csv")
    html_out = os.path.join(base_dir, "print-assets", "check-in-sheet-populated.html")
    pdf_out = os.path.join(base_dir, "print-assets", "check-in-sheet-populated.pdf")

    # Accept CLI arguments if provided
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
    if len(sys.argv) > 2:
        html_out = sys.argv[2]
    if len(sys.argv) > 3:
        pdf_out = sys.argv[3]

    print(f"Reading guest list from: {csv_path}")
    
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}", file=sys.stderr)
        sys.exit(1)

    guests = []
    try:
        with open(csv_path, mode="r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get("name", "").strip()
                # Skip example or empty rows
                if not name or name.lower() == "example person":
                    continue
                
                # Check rsvp status - only include confirmed/going
                status = row.get("rsvp_status", "").strip().lower()
                if status not in ["", "going", "confirmed", "yes"]:
                    continue

                # Compile clean notes from dietary and accessibility needs
                diet = row.get("dietary_restrictions", "").strip()
                access = row.get("accessibility_needs", "").strip()
                other_notes = row.get("notes", "").strip()
                
                notes_list = []
                if diet and diet.lower() != "none":
                    notes_list.append(f"Diet: {diet}")
                if access and access.lower() != "none":
                    notes_list.append(f"Access: {access}")
                if other_notes:
                    notes_list.append(other_notes)
                
                notes = "; ".join(notes_list)
                guests.append({"name": name, "notes": notes})
    except Exception as e:
        print(f"Error reading CSV: {e}", file=sys.stderr)
        sys.exit(1)

    # Sort guests alphabetically (case-insensitive)
    guests.sort(key=lambda g: g["name"].lower())
    
    # If no guests, keep at least one blank row so the sheet is printable
    if not guests:
        guests = [{"name": "", "notes": ""}]

    total_guests = len(guests)
    rows_per_page = 20
    # Calculate how many pages we need for guests (minimum 1 page)
    guest_pages = max(1, (total_guests + rows_per_page - 1) // rows_per_page)
    total_pages = guest_pages + 1  # Guest pages + 1 walk-ins/guide page

    html_content = []
    html_content.append("""<!doctype html>
<html><head><meta charset="utf-8"><title>AI Village Showcase Check-in Packet</title>
<style>
@page { size: letter; margin: 0.42in; }
body { font-family: Arial, Helvetica, sans-serif; color: #111827; font-size: 10.5px; }
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }
.topline { display: flex; justify-content: space-between; border-bottom: 2px solid #111827; padding-bottom: 5px; margin-bottom: 8px; font-size: 10px; }
h1 { font-size: 18px; margin: 0 0 4px; }
h1 span { font-size: 10.5px; font-weight: 400; color: #4b5563; }
h2 { font-size: 13px; margin: 12px 0 4px; }
p.note { margin: 0 0 7px; color: #374151; }
table { width: 100%; border-collapse: collapse; table-layout: fixed; }
th, td { border: 1px solid #6b7280; padding: 4px 5px; height: 20px; vertical-align: middle; }
th { background: #eef2ff; font-size: 9.5px; text-align: left; }
th:first-child, td.num { width: 24px; text-align: right; }
th:nth-child(2), td:nth-child(2) { width: 34%; }
th:nth-child(3), th:nth-child(4), th:nth-child(5), td.box { width: 54px; text-align: center; font-size: 12px; }
ol { margin-top: 6px; padding-left: 18px; columns: 2; column-gap: 28px; }
li { margin-bottom: 3px; }
code { font-size: 9.5px; }
</style></head><body>""")

    for p in range(guest_pages):
        start_idx = p * rows_per_page
        end_idx = min(start_idx + rows_per_page, total_guests)
        
        page_num = p + 1
        html_content.append(f"""
<section class="page">
  <div class="topline"><div><strong>AI Village Showcase & Human×AI Field Day</strong></div><div>Sat Jun 13, 2026 · The Fold · Doors 7:00 PM</div></div>
  <h1>RSVP Check-in Sheet <span>page {page_num} / {total_pages} · rows {start_idx + 1}-{start_idx + rows_per_page}</span></h1>
  <p class="note">At the door: check arrived, hand name tag, hand one Prompt Card, and mention the Demo Prompt Bowl by the stage.</p>
  <table><tr><th>#</th><th>Name (from RSVP export)</th><th>Arrived</th><th>Name tag</th><th>Prompt card</th><th>Notes</th></tr>""")

        for i in range(rows_per_page):
            curr_idx = start_idx + i
            num_label = curr_idx + 1
            if curr_idx < total_guests:
                g = guests[curr_idx]
                name = g["name"]
                notes = g["notes"]
            else:
                name = ""
                notes = ""
            
            html_content.append(f"<tr><td class='num'>{num_label}</td><td>{name}</td><td class='box'>☐</td><td class='box'>☐</td><td class='box'>☐</td><td>{notes}</td></tr>")
        
        html_content.append("</table>\n</section>")

    # Walk-ins page (last page)
    html_content.append(f"""
<section class="page">
  <div class="topline"><div><strong>AI Village Showcase & Human×AI Field Day</strong></div><div>Sat Jun 13, 2026 · The Fold · Doors 7:00 PM</div></div>
  <h1>Walk-ins / Last-minute Additions <span>page {total_pages} / {total_pages}</span></h1>
  <p class="note">If guest is not on RSVP list, add them here. If near cap 100 or any safety concern, check with Larissa before admitting.</p>
  <table><tr><th>#</th><th>Name</th><th>Arrived</th><th>Name tag</th><th>Prompt card</th><th>How they heard about event</th></tr>""")

    for i in range(1, 21):
        html_content.append(f"<tr><td class='num'>{i}</td><td></td><td class='box'>☐</td><td class='box'>☐</td><td class='box'>☐</td><td></td></tr>")

    html_content.append("""</table>
  <h2>Check-in helper quick guide</h2>
  <ol>
    <li>Greet warmly: “Welcome to the AI Village Showcase!”</li>
    <li>Find their RSVP name and check them off.</li>
    <li>Hand them a name tag and pen.</li>
    <li>Give one Prompt Card from <code>program/door-prompt-cards.md</code>; mention they can drop it in the Demo Prompt Bowl by the stage — the agents may build one live.</li>
    <li>Point them toward snacks/drinks, the welcome projection, and station area.</li>
    <li>Leaving early requires no action.</li>
  </ol>
</section>
</body></html>""")

    # Write HTML file
    try:
        with open(html_out, "w", encoding="utf-8") as f:
            f.write("\n".join(html_content))
        print(f"Generated HTML check-in sheet at: {html_out}")
    except Exception as e:
        print(f"Error writing HTML: {e}", file=sys.stderr)
        sys.exit(1)

    # Render HTML to PDF using weasyprint
    try:
        print(f"Rendering PDF check-in sheet to: {pdf_out}")
        subprocess.run(["weasyprint", html_out, pdf_out], check=True)
        print("PDF compilation successful!")
    except Exception as e:
        print(f"Error compiling PDF: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
