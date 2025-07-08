import boto3
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS IoT SiteWise client
sitewise = boto3.client('iotsitewise')

# Mapping of storage locations (e.g., A1–C3) to their respective asset IDs and property IDs in SiteWise
asset_map = {
    'A1': {'assetId': 'd5b83296-409a-4b05-a09a-fb2bb4ce9852', 'properties': {
        'id': '6f85f8bc-e85b-45d7-b999-5e6948e6b2ae',
        'type': '12b72c1a-aff6-4667-9a6c-f4f07a548f2b',
        'state': '64de9a70-58ee-4e01-9333-68cbc5b2d54a'}},
    # ... (remaining entries omitted for brevity; same structure for A2–C3)
    'C3': {'assetId': '81b62d80-3092-4499-8806-58e17ffd2634', 'properties': {
        'id': '6f85f8bc-e85b-45d7-b999-5e6948e6b2ae',
        'type': '12b72c1a-aff6-4667-9a6c-f4f07a548f2b',
        'state': '64de9a70-58ee-4e01-9333-68cbc5b2d54a'}}
}

def lambda_handler(event, context):
    logger.info("Lambda function invoked")
    logger.debug(f"Received event: {event}")

    # Extract timestamp and stockItems from incoming event
    time_in_seconds = event.get("ts")
    stock_items = event.get("stockItems", [])

    # Abort if timestamp is missing or stockItems array is empty
    if not isinstance(time_in_seconds, int) or not stock_items:
        logger.warning("Timestamp or stockItems missing or invalid. Aborting.")
        return

    entries = []

    # Process each stock item individually
    for item in stock_items:
        location = item.get("location")
        workpiece = item.get("workpiece", {})

        # Skip if location is missing or not found in asset_map
        if not location or location not in asset_map:
            logger.warning(f"Unknown or missing location: {location}")
            continue

        asset_id = asset_map[location]['assetId']
        properties = asset_map[location]['properties']

        # For each property (id, type, state), build a SiteWise entry
        for key in ['id', 'type', 'state']:
            raw_value = workpiece.get(key)
            value = raw_value if raw_value else "EMPTY"
            property_id = properties.get(key)

            # Skip if propertyId is missing
            if not property_id:
                logger.warning(f"Skipping: No propertyId for {location}:{key}")
                continue

            entry = {
                'entryId': f"{location}_{key}",
                'assetId': asset_id,
                'propertyId': property_id,
                'propertyValues': [
                    {
                        'value': {
                            'stringValue': str(value)
                        },
                        'timestamp': {
                            'timeInSeconds': time_in_seconds,
                            'offsetInNanos': 0
                        },
                        'quality': 'GOOD'
                    }
                ]
            }
            entries.append(entry)

    # Exit early if no valid entries found
    if not entries:
        logger.warning("No valid SiteWise entries generated.")
        return

    # Send entries to SiteWise in batches (max. 10 per request)
    BATCH_SIZE = 10
    for i in range(0, len(entries), BATCH_SIZE):
        batch = entries[i:i + BATCH_SIZE]
        try:
            response = sitewise.batch_put_asset_property_value(entries=batch)
            logger.info(f"{len(batch)} entries successfully sent to SiteWise.")

            # Log detailed errors if any were returned
            if 'errors' in response and response['errors']:
                for error in response['errors']:
                    logger.error(
                        f"Error for entryId={error['entryId']}: {error['errorMessage']} (Code: {error['errorCode']})"
                    )
            else:
                logger.info("All entries accepted without errors.")
        except Exception as e:
            logger.error(f"Exception occurred while writing batch to SiteWise: {e}")

