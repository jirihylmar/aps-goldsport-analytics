# Goldsport Analytics

## Pipeline

Run the pipeline to download orders and transform phone numbers:

```bash
bash /home/hylmarj/doc-digital-horizon-goldsport/help/etls/run_goldsport_pipeline.sh
```

The pipeline:
1. Downloads orders from Goldsport export (http://kurzy.classicskischool.cz/export/export-tsv-2026.php)
2. Saves timestamped orders file + updates `orders-current-season.tsv`
3. Runs phone numbers ETL transformation
4. Updates `phone_numbers-current-season.csv`

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

All dashboards read from `*-current-season.*` files - no manual updates needed after running the pipeline.

## Deployment

```bash
cd ~/aps-goldsport-analytics
aws s3 sync --delete --profile JiHy__vsb__299 . s3://datite-ss1-infgsp-299025166536/staging-goldsport-analytics/
```

Trigger deployment manually after sync.
