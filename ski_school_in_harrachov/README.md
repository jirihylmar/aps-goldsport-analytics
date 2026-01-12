# Classic Ski School - AI Search Visibility Analysis

**Client**: Classic Ski School Harrachov (classicskischool.cz)
**Project**: Google AI / Bing AI Visibility Optimization
**Status**: Technical fixes implemented, monitoring ongoing

---

## Project Structure

```
ski_school_in_harrachov/
├── README.md                              # This file - workflow instructions
├── BASELINE_VISIBILITY_MATRIX.md          # Main tracking document (EN)
├── BASELINE_VISIBILITY_MATRIX_cs.md       # Czech version
├── BASELINE_VISIBILITY_MATRIX_cs.html     # Czech HTML export (styled)
├── BASELINE_VISIBILITY_MATRIX_cs.pdf      # Czech PDF export
│
├── 2025-11-12/                            # Baseline measurement (Oct 22, 2025)
│   └── {query}/                           # PDF screenshots by search query
│
├── 2025-01-07/                            # Week 10 measurement (Jan 7, 2026)
│   └── {query}/                           # PDF screenshots by search query
│
└── archive/                               # Reference documents (completed)
    ├── VISIBILITY_ANALYSIS.md             # Detailed baseline analysis
    ├── VISIBILITY_ANALYSIS_CONDENSED.md   # Executive summary
    ├── TECHNICAL_FIXES_SEASON_2025-2026.md # Implementation checklist (done)
    └── FINAL_ACTION_PLAN.md               # Action plan document
```

---

## Measurement Workflow

### When to Run New Measurements

| Measurement | Date | Purpose |
|-------------|------|---------|
| Baseline | Oct 22, 2025 | Before technical fixes |
| Week 6 | Dec 2-6, 2025 | First check |
| Week 8 | Dec 16-20, 2025 | Mid-season check |
| **Week 10** | **Jan 7, 2026** | **Post-fix verification** |
| Week 12 | Feb 3-7, 2026 | Final measurement |

### Step 1: Capture New Search Results

Run the browser-search tool with these queries:

```bash
# English
browser-search "ski school in Harrachov" -b chrome -e google -m ask -l en --capture

# Czech
browser-search "lyžařská škola v Harrachově" -b chrome -e google -m ask -l cs --capture

# German
browser-search "Skischule in Harrachov" -b chrome -e google -m ask -l de --capture

# Polish
browser-search "szkoła narciarska w Harrachowie" -b chrome -e google -m ask -l pl --capture
```

Repeat for each engine: `google`, `bing`, `perplexity`, `duckduckgo`

Save PDFs to a new date folder: `YYYY-MM-DD/`

### Step 2: Analyze Results

For each PDF, record:
1. **Position**: Where does Classic Ski School appear? (#1, #2, #3, or NOT LISTED)
2. **Total schools**: How many schools are listed in AI response?
3. **Details shown**: Rating, reviews, address, phone, prices, features?
4. **Competitors**: Who is #1? Who else appears?

### Step 3: Update Reports

Update `BASELINE_VISIBILITY_MATRIX.md`:
1. Add new measurement section at top
2. Update "Current Status" table
3. Update target metrics checkboxes
4. Update document version and date

Update `BASELINE_VISIBILITY_MATRIX_cs.md`:
1. Same updates in Czech

Regenerate exports:
```bash
pandoc BASELINE_VISIBILITY_MATRIX_cs.md -o BASELINE_VISIBILITY_MATRIX_cs.html --standalone
pandoc BASELINE_VISIBILITY_MATRIX_cs.md -o BASELINE_VISIBILITY_MATRIX_cs.pdf --pdf-engine=xelatex -V mainfont="DejaVu Sans"
```

---

## Current Status (January 7, 2026)

### Results Summary

| Market | Baseline (Oct 2025) | Week 10 (Jan 2026) | Status |
|--------|--------------------|--------------------|--------|
| German Google AI | NOT LISTED | **#2 of 4** | FIXED |
| Polish Google AI | Weak mention | **#1 of 5** | FIXED |
| English Google AI | #2 of 6 | **#1 of 5** | IMPROVED |
| Czech Google AI | #1 of 4 | **#1 of 5** | MAINTAINED |

### Technical Fixes Implemented

- Meta title/description tags (DE, PL, EN, CS pages)
- Hreflang tags across all language versions
- Schema.org LocalBusiness markup
- Narrative content paragraphs for AI comprehension

### Remaining Actions

- [ ] Continue review generation campaign (current: 49, target: 55+)
- [ ] Week 12 final measurement (Feb 3-7, 2026)
- [ ] Final ROI report

---

## Key Metrics to Track

| Metric | Baseline | Current | Target |
|--------|----------|---------|--------|
| Google Reviews | 47 | 49 | 70+ |
| German Google AI | 0% | 100% | 100% |
| Polish Google AI | Weak | #1 | #1-2 |
| Rating | 4.8 | 4.8 | 4.7+ |

---

## Files Reference

| File | Purpose | Update Frequency |
|------|---------|------------------|
| `BASELINE_VISIBILITY_MATRIX.md` | Main tracking, EN | Each measurement |
| `BASELINE_VISIBILITY_MATRIX_cs.md` | Czech version | Each measurement |
| `TECHNICAL_FIXES_SEASON_2025-2026.md` | Implementation checklist | When fixes deployed |
| `VISIBILITY_ANALYSIS.md` | Detailed baseline | Reference only |
| `FINAL_ACTION_PLAN.md` | Strategic plan | Reference only |

---

**Last Updated**: January 7, 2026 (Week 10 Measurement)
**Next Update**: February 3-7, 2026 (Week 12 Final)
