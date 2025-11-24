# Website QR Code Generator

This script generates QR codes for your website that can be scanned from anywhere in the world to access your webpage.

## Features

- 🌍 **Global Access**: Generate QR codes for websites hosted online
- 🎨 **Logo Support**: Embed custom logos in your QR codes
- 🖼️ **High Quality**: Generates crisp PNG images
- 📱 **Mobile Friendly**: QR codes work with all smartphone cameras

## Quick Start

### Option 1: Easy Run (Windows)
Double-click `generate_qr.bat` and follow the prompts.

### Option 2: Manual Setup
1. Install Python dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

2. Run the script:
   ```powershell
   python qr_generator.py
   ```

3. Or provide URL directly:
   ```powershell
   python qr_generator.py https://your-website.com
   ```

## Hosting Your Website

To make your website accessible worldwide, you need to host it online. Here are some **FREE** options:

### 🎯 Recommended: GitHub Pages
1. Create a free account at [github.com](https://github.com)
2. Create a new repository
3. Upload your HTML files (`index.html`, `kamala_waters_shapefile_map.html`)
4. Go to Settings → Pages
5. Select "Deploy from a branch" and choose "main"
6. Your site will be at: `https://yourusername.github.io/repositoryname`

### Other Free Options:
- **Netlify**: Drag & drop deployment at [netlify.com](https://netlify.com)
- **Vercel**: Easy deployment at [vercel.com](https://vercel.com)
- **Firebase**: Google's hosting at [firebase.google.com](https://firebase.google.com)

## Usage Examples

### Basic QR Code
```powershell
python qr_generator.py https://mywebsite.com
```

### QR Code with Custom Logo
When prompted, provide the path to your logo image file.

### Custom Filename
The script will ask for a custom filename, or use the default `website_qr_code.png`.

## File Structure
```
Map/
├── index.html                          # Your main webpage
├── kamala_waters_shapefile_map.html    # Your map page
├── qr_generator.py                     # QR code generator script
├── requirements.txt                    # Python dependencies
├── generate_qr.bat                     # Easy run script for Windows
└── website_qr_code.png                 # Generated QR code (after running)
```

## How It Works

1. **Input**: You provide your website URL
2. **Generation**: Script creates a high-quality QR code
3. **Output**: PNG file ready for printing or sharing
4. **Scanning**: Anyone can scan the code with their phone camera
5. **Access**: Takes them directly to your website

## Tips

- 📏 **Print Size**: QR codes work best when at least 2x2 cm (0.8x0.8 inches)
- 🖼️ **Logo Size**: Keep logos small (script automatically resizes)
- 📱 **Testing**: Test your QR code with different phone cameras
- 🌐 **URL**: Use HTTPS URLs when possible for security

## Troubleshooting

### "Module not found" error
Install dependencies:
```powershell
pip install qrcode[pil] Pillow
```

### QR code doesn't work
- Ensure your website is hosted online (not local file)
- Check that URL is correct and accessible
- Try scanning with different QR code reader apps

### Script won't run
- Make sure Python is installed on your system
- Check that you're in the correct directory
- Try running with `python3` instead of `python`

---

**Need help?** The script provides interactive prompts and detailed error messages to guide you through the process.