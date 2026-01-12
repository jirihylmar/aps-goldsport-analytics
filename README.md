# Goldsport Analytics

## How It Works

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        AUTOMATED FLOW (Daily)                          │
│                                                                         │
│  GitHub Actions (6:00 AM UTC)                                          │
│       │                                                                 │
│       ▼                                                                 │
│  Download orders from Goldsport ──► Transform phone numbers            │
│       │                                                                 │
│       ▼                                                                 │
│  Commit & push to GitHub ──► Triggers Amplify build ──► Live website   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                         MANUAL FLOW (Local)                            │
│                                                                         │
│  1. git pull                    # Get latest data from GitHub          │
│  2. bash etls/run_goldsport_pipeline.sh   # Run pipeline locally       │
│  3. git add . && git commit && git push   # Push changes               │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Important:** GitHub Actions runs the pipeline daily and commits changes. To get the latest data locally, always `git pull` first.

## Pipeline

Run manually (optional - GitHub Actions runs daily):

```bash
cd ~/aps-goldsport-analytics
git pull                                    # Get latest changes first!
bash etls/run_goldsport_pipeline.sh         # Run pipeline
git add . && git commit -m "Update" && git push
```

The pipeline:
1. Downloads orders from Goldsport export
2. Saves timestamped orders file + updates `orders-current-season.tsv`
3. Runs phone numbers ETL transformation
4. Updates `phone_numbers-current-season.csv`

## GitHub Actions

Workflow: `.github/workflows/daily-pipeline.yml`

**Triggers:**
- Daily at 6:00 AM UTC (7:00 AM CET)
- On every push to `main` branch
- Manual trigger via GitHub Actions UI

**What it does:**
1. Checks out repository
2. Runs the pipeline (download + transform)
3. Cleans up duplicate files
4. Commits and pushes changes back to GitHub
5. Push triggers Amplify deployment automatically

### Billing & Limits

GitHub Actions is **free** for public repos. For private repos:

| Resource | Free Tier |
|----------|-----------|
| Minutes/month | 2,000 |
| Storage | 500 MB |
| Concurrent jobs | 20 |

**This project usage:** ~1 run/day × ~2 min = **~60 min/month** (3% of free tier)

**Who pays:** Repository owner's GitHub account. Check usage: https://github.com/settings/billing

## Data Files

### Orders
- `goldsport__orders___gsp_dataset___hand_increment/method=hand_increment/source=goldsport/`
  - `orders-YYYY-MM-DD-HHMMSS.tsv` - timestamped exports
  - `orders-current-season.tsv` - latest export (used by dashboards)

### Phone Numbers
- `goldsport__phone_numbers___gsp_dataset___hand_increment/method=hand_increment/source=goldsport/`
  - `phone_numbers_YYYY-MM-DD_YYYY-MM-DD.csv` - timestamped transforms
  - `phone_numbers-current-season.csv` - latest transform (used by dashboards)

## Dashboards

| File | Description |
|------|-------------|
| `orders__graph_cumulative_sums.html` | Cumulative orders/revenue comparison across seasons |
| `orders__graph_cumulative.html` | Orders by category (Kids, Skis, Snowboard) |
| `orders_phone_numbers__graph_cumulative_sums.html` | Phone numbers analysis by country |

All dashboards read from `*-current-season.*` files - automatically updated.

## Deployment

**Automatic:** Push to `main` → Amplify builds and deploys

**Manual S3 sync (if needed):**
```bash
cd ~/aps-goldsport-analytics
aws s3 sync --delete --profile JiHy__vsb__299 . s3://datite-ss1-infgsp-299025166536/staging-goldsport-analytics/
```

## Domain Setup

**Status:** AWAITING DNS UPDATE

### Required DNS Records

Update these CNAME records at your DNS provider:

| Host | Type | Value |
|------|------|-------|
| `analytics.classicskischool.cz` | CNAME | `d2p2xogu6e4rk4.cloudfront.net` |
| `www.analytics.classicskischool.cz` | CNAME | `d2p2xogu6e4rk4.cloudfront.net` |

### SSL Certificate Verification (if needed)

| Host | Type | Value |
|------|------|-------|
| `_95365be9da8d7c6e26cb0397f63007a4.analytics.classicskischool.cz` | CNAME | `_2ad80b54a90bc94a965cdff4e29949a8.zfyfvmchrl.acm-validations.aws.` |

### Troubleshooting

**403 Error / SSL Security Warning:**
- DNS records not updated yet → Update CNAME records above
- SSL certificate pending → Add certificate verification record
- DNS propagation delay → Wait 10-30 minutes after DNS update

**Check domain status:**
```bash
aws amplify get-domain-association --app-id drz9yi5cw9kfv --domain-name analytics.classicskischool.cz --profile JiHy__vsb__299
```

**Expected status progression:**
1. `CREATING` → Setting up
2. `AWAITING_APP_CNAME` → Update DNS records
3. `PENDING_VERIFICATION` → Waiting for SSL cert
4. `AVAILABLE` → Ready!

## URLs

- **Live:** https://www.analytics.classicskischool.cz
- **Amplify default:** https://main.drz9yi5cw9kfv.amplifyapp.com
- **GitHub:** https://github.com/jirihylmar/aps-goldsport-analytics
- **Amplify Console:** App ID `drz9yi5cw9kfv`

## Access

Page is protected via Amplify Basic Auth:

| | |
|---|---|
| **Username** | `master@goldsport.cz` |
| **Password** | `Goldsport2025` |
