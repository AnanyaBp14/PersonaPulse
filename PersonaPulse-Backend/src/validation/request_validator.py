REQUIRED_FIELDS = ["idea", "platforms", "audience", "tone", "language"]

def validate_request(body):
    if not isinstance(body.get("platforms"), list):
        return False, "'platforms' must be a list."
    
    for field in REQUIRED_FIELDS:
        if field not in body:
            return False, f"Missing required field: {field}"
            
    if len(body["platforms"]) > 5:
        return False, "Maximum 5 platforms allowed per batch."
        
    return True, None