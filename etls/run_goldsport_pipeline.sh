#!/bin/bash
# Goldsport Orders Download, Phone Numbers ETL, and Google Analytics Pipeline
# Downloads orders, transforms phone numbers, and fetches GA data

set -e

# Get script directory for relative paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(dirname "${SCRIPT_DIR}")"

# Configuration - Orders
ORDERS_DIR="${BASE_DIR}/goldsport__orders___gsp_dataset___hand_increment/method=hand_increment/source=goldsport"
PHONE_NUMBERS_DIR="${BASE_DIR}/goldsport__phone_numbers___gsp_dataset___hand_increment/method=hand_increment/source=goldsport"
EXPORT_URL="http://kurzy.classicskischool.cz/export/export-tsv-2026.php"
ETL_SCRIPT="${SCRIPT_DIR}/etl__phone_numbers.py"
CURRENT_SEASON_ORDERS="${ORDERS_DIR}/orders-current-season.tsv"
CURRENT_SEASON_PHONES="${PHONE_NUMBERS_DIR}/phone_numbers-current-season.csv"

# Configuration - Google Analytics
GA_DIR="${BASE_DIR}/goldsport__ga_classicskischool_daily_metrix___gsp_dataset___hand_increment/method=hand_increment/source=goldsport"
GA_SCRIPT="${SCRIPT_DIR}/ga_download/action_google_analytics_download.py"
GA_CREDENTIALS="${SCRIPT_DIR}/ga_download/goldsport-default-project-bb5fc04659f5.json"
GA_PAGES="${SCRIPT_DIR}/ga_download/pages.txt"
GA_PROPERTY_ID="365327832"
GA_START_DATE="2025-12-01"
CURRENT_SEASON_GA="${GA_DIR}/ga_classicskischool-current-season.tsv"

# Generate timestamp for filename
TIMESTAMP=$(date +"%Y-%m-%d-%H%M%S")
OUTPUT_FILE="${ORDERS_DIR}/orders-${TIMESTAMP}.tsv"

echo "=== Goldsport Pipeline Started ==="
echo "Timestamp: ${TIMESTAMP}"

# Step 1: Trigger export
echo ""
echo "Step 1: Triggering export..."
curl -s "${EXPORT_URL}" > /dev/null

# Step 2: Download the TSV file
echo "Step 2: Downloading orders..."
curl -s "${EXPORT_URL}?action=download" -o "${OUTPUT_FILE}"

# Verify download
LINE_COUNT=$(wc -l < "${OUTPUT_FILE}")
echo "Downloaded: ${OUTPUT_FILE}"
echo "Lines: ${LINE_COUNT}"

if [ "$LINE_COUNT" -lt 2 ]; then
    echo "ERROR: Download failed or file is empty"
    exit 1
fi

# Step 3: Update current season orders file
echo ""
echo "Step 3: Updating current season orders file..."
cp "${OUTPUT_FILE}" "${CURRENT_SEASON_ORDERS}"
echo "Updated: ${CURRENT_SEASON_ORDERS}"

# Step 4: Run phone numbers ETL
echo ""
echo "Step 4: Running phone numbers transformation..."
python3 "${ETL_SCRIPT}" "${OUTPUT_FILE}"

# Step 5: Update current season phone numbers file
echo ""
echo "Step 5: Updating current season phone numbers file..."
LATEST_PHONES=$(ls -t "${PHONE_NUMBERS_DIR}"/phone_numbers_2*.csv 2>/dev/null | head -1)
if [ -n "${LATEST_PHONES}" ]; then
    cp "${LATEST_PHONES}" "${CURRENT_SEASON_PHONES}"
    echo "Updated: ${CURRENT_SEASON_PHONES}"
else
    echo "WARNING: No phone numbers file found to copy"
fi

# Step 6: Download Google Analytics data
echo ""
echo "Step 6: Downloading Google Analytics data..."
GA_OUTPUT_FILE="${GA_DIR}/ga_classicskischool-${TIMESTAMP}.tsv"

if [ -f "${GA_CREDENTIALS}" ]; then
    python3 "${GA_SCRIPT}" \
        --path-to-api-key="${GA_CREDENTIALS}" \
        --project-property-id="${GA_PROPERTY_ID}" \
        --pages-paths="${GA_PAGES}" \
        --start-date="${GA_START_DATE}" \
        --output-path="${GA_OUTPUT_FILE}"

    GA_LINE_COUNT=$(wc -l < "${GA_OUTPUT_FILE}")
    echo "Downloaded: ${GA_OUTPUT_FILE}"
    echo "Lines: ${GA_LINE_COUNT}"

    # Step 7: Update current season GA file
    echo ""
    echo "Step 7: Updating current season GA file..."
    cp "${GA_OUTPUT_FILE}" "${CURRENT_SEASON_GA}"
    echo "Updated: ${CURRENT_SEASON_GA}"
else
    echo "WARNING: GA credentials not found at ${GA_CREDENTIALS}"
    echo "Skipping Google Analytics download"
fi

echo ""
echo "=== Pipeline Complete ==="
