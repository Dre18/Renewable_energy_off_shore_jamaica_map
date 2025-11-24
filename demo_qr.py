#!/usr/bin/env python3
"""
Demo script to generate a QR code for your website
"""

import qrcode
from PIL import Image
import os

def create_demo_qr():
    """Create a demo QR code"""
    
    # For demo purposes - replace with your actual hosted URL
    demo_url = "https://yourusername.github.io/your-map-project"
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(demo_url)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR code
    img.save("demo_qr_code.png")
    
    print(f"✅ Demo QR code created: demo_qr_code.png")
    print(f"🔗 URL encoded: {demo_url}")
    print(f"📱 Replace the URL in this script with your actual website URL!")

if __name__ == "__main__":
    create_demo_qr()