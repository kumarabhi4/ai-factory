"""
Custom MCP Server - Temperature Conversion & Unit Converter
Built during AWS Workshop: Everyday Productivity Accelerators
"""

from mcp.server import FastMCP
from typing import Dict
from datetime import datetime

# Initialize MCP server
mcp = FastMCP("Temperature Conversion Server")

@mcp.tool(description="Convert Fahrenheit to Celsius")
def fahrenheit_to_celsius(temp_f: str) -> Dict:
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        temp_f: Temperature in Fahrenheit (as string)
    
    Returns:
        Dictionary with converted temperature
    """
    try:
        # Parse the temperature
        fahrenheit = float(temp_f.strip())
        
        # Convert to Celsius
        celsius = (fahrenheit - 32) * 5/9
        
        return {
            "success": True,
            "fahrenheit": fahrenheit,
            "celsius": round(celsius, 2),
            "message": f"{fahrenheit}°F = {round(celsius, 2)}°C",
            "timestamp": datetime.now().isoformat()
        }
        
    except ValueError:
        return {
            "success": False,
            "error": "Invalid temperature format. Please provide a number.",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

@mcp.tool(description="Convert Celsius to Fahrenheit")
def celsius_to_fahrenheit(temp_c: str) -> Dict:
    """Convert temperature from Celsius to Fahrenheit."""
    try:
        celsius = float(temp_c.strip())
        fahrenheit = (celsius * 9/5) + 32
        
        return {
            "success": True,
            "celsius": celsius,
            "fahrenheit": round(fahrenheit, 2),
            "message": f"{celsius}°C = {round(fahrenheit, 2)}°F",
            "timestamp": datetime.now().isoformat()
        }
        
    except ValueError:
        return {
            "success": False,
            "error": "Invalid temperature format. Please provide a number.",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

@mcp.tool(description="Convert distance units (miles to kilometers)")
def miles_to_kilometers(miles: str) -> Dict:
    """Convert miles to kilometers."""
    try:
        miles_val = float(miles.strip())
        kilometers = miles_val * 1.60934
        
        return {
            "success": True,
            "miles": miles_val,
            "kilometers": round(kilometers, 2),
            "message": f"{miles_val} miles = {round(kilometers, 2)} km",
            "timestamp": datetime.now().isoformat()
        }
        
    except ValueError:
        return {
            "success": False,
            "error": "Invalid distance format. Please provide a number.",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

@mcp.tool(description="Convert weight units (pounds to kilograms)")
def pounds_to_kilograms(pounds: str) -> Dict:
    """Convert pounds to kilograms."""
    try:
        pounds_val = float(pounds.strip())
        kilograms = pounds_val * 0.453592
        
        return {
            "success": True,
            "pounds": pounds_val,
            "kilograms": round(kilograms, 2),
            "message": f"{pounds_val} lbs = {round(kilograms, 2)} kg",
            "timestamp": datetime.now().isoformat()
        }
        
    except ValueError:
        return {
            "success": False,
            "error": "Invalid weight format. Please provide a number.",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

if __name__ == "__main__":
    print(f"🚀 Starting {mcp.name}...")
    mcp.run(transport="stdio")