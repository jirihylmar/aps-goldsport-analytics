'''
Example usage:
python3 /home/hylmarj/doc-digital-horizon-goldsport/help/ga_download/action_google_analytics_download.py \
--path-to-api-key=/home/hylmarj/aps-goldsport-booking/credentials/goldsport-default-project-37ba59256f71.json \
--project-property-id=365327832 \
--pages-paths=/home/hylmarj/doc-digital-horizon-goldsport/help/ga_download/pages.txt \
--start-date=2023-12-01 \
--output-path=/home/hylmarj/aps-goldsport-analytics/goldsport__ga_classicskischool_daily_metrix___gsp_dataset___hand_increment/method=hand_increment/source=goldsport/goldsport__ga_classicskischool_daily_metrix.tsv
'''

from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from datetime import datetime
import argparse
import logging
import sys
import os
import csv

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def get_analytics_data(session, start_date, end_date, property_id, page_paths):
    url = f"https://analyticsdata.googleapis.com/v1beta/properties/{property_id}:runReport"
    
    request_body = {
        "dateRanges": [
            {"startDate": start_date, "endDate": end_date}
        ],
        "metrics": [
            {"name": "sessions"},
            {"name": "activeUsers"},
            {"name": "newUsers"},
            {"name": "averageSessionDuration"}
        ],
        "dimensions": [
            {"name": "date"},
            {"name": "landingPage"}
        ],
        "dimensionFilter": {
            "orGroup": {
                "expressions": [
                    {
                        "filter": {
                            "fieldName": "landingPage",
                            "stringFilter": {"value": path}
                        }
                    } for path in page_paths
                ]
            }
        }
    }
    
    try:
        response = session.post(url, json=request_body, timeout=30.0)
        if response.status_code != 200:
            logger.error(f"Error response: {response.text}")
            return None
        return response.json()
    except Exception as e:
        logger.error(f"Request error: {str(e)}")
        return None

def transform_to_long_format(data):
    if not data or 'rows' not in data:
        logger.error("No data to transform")
        return None
        
    rows = []
    metric_names = ['Sessions', 'Active users', 'New users', 'Average engagement time per session']
    
    for row in data['rows']:
        date_str = row['dimensionValues'][0]['value']
        formatted_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
        date_obj = datetime.strptime(formatted_date, '%Y-%m-%d')
        year = date_obj.isocalendar()[0]
        week = date_obj.isocalendar()[1]
        landing_page = row['dimensionValues'][1]['value']
        metrics = row['metricValues']
        
        # Convert each metric to a separate row
        for metric_name, metric_value in zip(metric_names, metrics):
            # Convert to integer, rounding floating point values
            value = float(metric_value['value'])
            if metric_name == 'Average engagement time per session':
                value = int(round(value))  # Round to nearest integer
            else:
                value = int(value)  # Direct integer conversion for count metrics
            
            rows.append({
                'date': formatted_date,
                'year': year,
                'week': week,
                'code': landing_page,
                'type': metric_name,
                'value': value
            })
    
    # Sort by date, code (landing page), and type
    return sorted(rows, key=lambda x: (x['date'], x['code'], x['type']))

def save_to_tsv(rows, output_path):
    if not rows:
        logger.error("No data to save")
        return
        
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    fieldnames = ['date', 'year', 'week', 'code', 'type', 'value']
    
    with open(output_path, 'w', newline='') as tsvfile:
        writer = csv.DictWriter(tsvfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path-to-api-key', required=True)
    parser.add_argument('--project-property-id', required=True)
    parser.add_argument('--pages-paths', required=True)
    parser.add_argument('--start-date', required=True)
    parser.add_argument('--end-date', default=datetime.now().strftime('%Y-%m-%d'))
    parser.add_argument('--output-path', required=True, 
                      help='Output path with {} placeholder for timestamp')
    
    args = parser.parse_args()
    
    try:
        with open(args.pages_paths, 'r') as f:
            pages = [line.strip() for line in f if line.strip()]
        
        credentials = service_account.Credentials.from_service_account_file(
            args.path_to_api_key,
            scopes=['https://www.googleapis.com/auth/analytics.readonly']
        )
        
        session = AuthorizedSession(credentials)
        
        # Generate output path with timestamp
        #timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        #output_path = args.output_path.format(timestamp)
        output_path = args.output_path
        
        logger.info("Fetching analytics data...")
        data = get_analytics_data(session, args.start_date, args.end_date, 
                                args.project_property_id, pages)
        
        if data:
            transformed_data = transform_to_long_format(data)
            if transformed_data:
                save_to_tsv(transformed_data, output_path)
                logger.info(f"Data saved to: {output_path}")
        
    except Exception as e:
        logger.error(f"Error in main: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main()