import concurrent.futures
from .campaign_generator import generate_campaign

def handle_batch_request(body):
    platforms = body.get("platforms", ["LinkedIn"])
    result_dict = {}

    # Crucial: Parallel Threading to prevent API Gateway timeouts
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(platforms)) as executor:
        future_to_platform = {
            executor.submit(generate_campaign, body, platform): platform 
            for platform in platforms
        }
        
        for future in concurrent.futures.as_completed(future_to_platform):
            platform = future_to_platform[future]
            try:
                result_dict[platform] = future.result()
            except Exception as exc:
                result_dict[platform] = {"error": str(exc)}

    return {
        "campaign_title": body["idea"],
        "platforms_generated": len(platforms),
        "results": result_dict
    }