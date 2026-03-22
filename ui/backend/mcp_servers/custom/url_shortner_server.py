"""
Custom MCP Server - URL Shortener & Text Utilities
Built during AWS Workshop: Everyday Productivity Accelerators
"""

from mcp.server import FastMCP
from typing import Dict
from datetime import datetime
import hashlib
import json
import os

# Initialize MCP server
mcp = FastMCP("URL Shortener & Text Utilities")

# Storage file for URLs (in production, use a database)
STORAGE_FILE = "url_storage.json"

def load_url_storage() -> Dict:
    """Load URL storage from file"""
    if os.path.exists(STORAGE_FILE):
        try:
            with open(STORAGE_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {"urls": {}, "stats": {}}

def save_url_storage(storage: Dict):
    """Save URL storage to file"""
    try:
        with open(STORAGE_FILE, 'w') as f:
            json.dump(storage, f, indent=2)
    except Exception as e:
        print(f"Error saving storage: {e}")

@mcp.tool(description="Shorten a long URL into a compact format")
def shorten_url(url: str, custom_code: str = None) -> Dict:
    """Shorten a URL and store it for later retrieval."""
    try:
        # Validate URL format
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        storage = load_url_storage()
        
        # Generate short code
        if custom_code:
            short_code = custom_code
        else:
            # Create hash from URL + timestamp
            content = f"{url}{datetime.now().isoformat()}"
            hash_object = hashlib.md5(content.encode())
            short_code = hash_object.hexdigest()[:8]
        
        # Store the URL
        storage["urls"][short_code] = {
            "original_url": url,
            "created_at": datetime.now().isoformat(),
            "clicks": 0
        }
        
        save_url_storage(storage)
        
        return {
            "success": True,
            "short_code": short_code,
            "short_url": f"short.ly/{short_code}",
            "original_url": url,
            "message": f"URL shortened successfully! Code: {short_code}"
        }
        
    except Exception as e:
        return {"success": False, "error": str(e)}

@mcp.tool(description="Expand a shortened URL to get the original URL")
def expand_url(short_code: str) -> Dict:
    """Expand a shortened URL code to get the original URL."""
    try:
        storage = load_url_storage()
        
        if short_code not in storage["urls"]:
            return {
                "success": False,
                "error": f"Short code '{short_code}' not found"
            }
        
        url_data = storage["urls"][short_code]
        url_data["clicks"] += 1  # Track usage
        save_url_storage(storage)
        
        return {
            "success": True,
            "original_url": url_data["original_url"],
            "clicks": url_data["clicks"]
        }
        
    except Exception as e:
        return {"success": False, "error": str(e)}

@mcp.tool(description="Get statistics for all shortened URLs")
def get_url_stats() -> Dict:
    """Get statistics for all shortened URLs."""
    try:
        storage = load_url_storage()
        
        if not storage["urls"]:
            return {"success": True, "message": "No URLs shortened yet"}
        
        total_clicks = sum(data["clicks"] for data in storage["urls"].values())
        
        return {
            "success": True,
            "total_urls": len(storage["urls"]),
            "total_clicks": total_clicks
        }
        
    except Exception as e:
        return {"success": False, "error": str(e)}

@mcp.tool(description="Count words, characters, and lines in text")
def analyze_text(text: str) -> Dict:
    """Analyze text to count words, characters, lines, and other statistics."""
    try:
        lines = text.split('\n')
        words = text.split()
        
        return {
            "success": True,
            "statistics": {
                "characters": len(text),
                "characters_no_spaces": len(text.replace(' ', '')),
                "words": len(words),
                "lines": len(lines)
            }
        }
        
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    print(f"🚀 Starting {mcp.name}...")
    mcp.run(transport="stdio")