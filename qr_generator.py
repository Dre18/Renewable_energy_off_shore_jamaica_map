#!/usr/bin/env python3
"""
QR Code Generator for Website
This script generates a QR code that links to your website.
When scanned, users can view your webpage from anywhere in the world.
"""

import qrcode
from PIL import Image
import os
import sys
from urllib.parse import urlparse

def generate_qr_code(url, filename="website_qr_code.png", logo_path=None):
    """
    Generate a QR code for the given URL
    
    Args:
        url (str): The website URL to encode in the QR code
        filename (str): Output filename for the QR code image
        logo_path (str): Optional path to a logo image to embed in the QR code
    
    Returns:
        str: Path to the generated QR code file
    """
    
    # Validate URL
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        parsed_url = urlparse(url)
        if not parsed_url.netloc:
            raise ValueError("Invalid URL format")
    except Exception as e:
        print(f"Error: Invalid URL format - {e}")
        return None
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for logo embedding
        box_size=10,  # Size of each box in pixels
        border=4,  # Size of the border (minimum is 4)
    )
    
    # Add URL data to QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # Add logo if provided
    if logo_path and os.path.exists(logo_path):
        try:
            # Open logo image
            logo = Image.open(logo_path)
            
            # Calculate logo size (10% of QR code size)
            qr_width, qr_height = qr_img.size
            logo_size = min(qr_width, qr_height) // 10
            
            # Resize logo
            logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
            
            # Calculate position to center the logo
            logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
            
            # Paste logo onto QR code
            qr_img.paste(logo, logo_pos)
            
        except Exception as e:
            print(f"Warning: Could not add logo - {e}")
    
    # Save QR code
    output_path = os.path.join(os.getcwd(), filename)
    qr_img.save(output_path, "PNG", optimize=True)
    
    return output_path

def generate_hosting_instructions():
    """Generate instructions for hosting the website"""
    instructions = """
    
=== HOSTING OPTIONS FOR GLOBAL ACCESS ===

To make your website accessible worldwide, you have several free options:

1. GITHUB PAGES (Recommended - Free)
   - Create a GitHub account at github.com
   - Create a new repository
   - Upload your HTML files (index.html, kamala_waters_shapefile_map.html)
   - Go to Settings > Pages
   - Select "Deploy from a branch" and choose "main"
   - Your site will be available at: https://dre18.github.io/Renewable_energy_off_shore_jamaica_map

2. NETLIFY (Free tier available)
   - Go to netlify.com
   - Drag and drop your project folder
   - Get instant URL like: https://random-name.netlify.app

3. VERCEL (Free tier available)
   - Go to vercel.com
   - Import your project from GitHub or upload directly
   - Get URL like: https://your-project.vercel.app

4. FIREBASE HOSTING (Google - Free tier)
   - Go to firebase.google.com
   - Create a project and enable hosting
   - Use Firebase CLI to deploy

Once hosted, use the live URL in this script to generate your QR code!
    """
    return instructions

def main():
    """Main function to run the QR code generator"""
    print("🗺️  Website QR Code Generator")
    print("=" * 40)
    
    # Check if running with command line arguments
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        # Interactive mode
        print("\nTo make your website globally accessible, you need to host it online.")
        print("See the hosting instructions below.")
        
        url = input("\nEnter your website URL (or press Enter for local testing): ").strip()
        
        if not url:
            # Default to local file for testing
            current_dir = os.path.dirname(os.path.abspath(__file__))
            index_path = os.path.join(current_dir, "index.html")
            map_path = os.path.join(current_dir, "kamala_waters_shapefile_map.html")
            
            if os.path.exists(index_path):
                url = f"file:///{index_path.replace(os.sep, '/')}"
                print(f"Using local file: {url}")
                print("⚠️  Note: This will only work on your computer. For global access, host online!")
            else:
                print("No URL provided and no local index.html found.")
                print(generate_hosting_instructions())
                return
    
    # Ask for custom filename
    filename = input("Enter QR code filename (press Enter for 'website_qr_code.png'): ").strip()
    if not filename:
        filename = "website_qr_code.png"
    
    if not filename.endswith(('.png', '.jpg', '.jpeg')):
        filename += '.png'
    
    # Ask for logo
    logo_path = input("Enter logo image path (optional, press Enter to skip): ").strip()
    if logo_path and not os.path.exists(logo_path):
        print(f"Logo file not found: {logo_path}")
        logo_path = None
    
    print(f"\nGenerating QR code for: {url}")
    
    # Generate QR code
    output_path = generate_qr_code(url, filename, logo_path)
    
    if output_path:
        print(f"✅ QR code generated successfully!")
        print(f"📁 Saved as: {output_path}")
        print(f"📱 Scan this QR code to access your website from anywhere!")
        
        if url.startswith('file://'):
            print(generate_hosting_instructions())
    else:
        print("❌ Failed to generate QR code")

if __name__ == "__main__":
    main()