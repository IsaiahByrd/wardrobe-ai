import os
import time
from pathlib import Path
from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from virtual_tryon import run_virtual_tryon

# Initialize FastAPI app
app = FastAPI(title="Wardrobe AI", description="Virtual Try-On API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get paths
BACKEND_DIR = Path(__file__).parent
FRONTEND_DIR = BACKEND_DIR.parent / "frontend"

# Mount static files from frontend directory
app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    """Serve the main page (index.html as the home page)"""
    try:
        with open(FRONTEND_DIR / "index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Home page not found")

@app.get("/features", response_class=HTMLResponse)
async def features():
    """Serve the features page"""
    try:
        with open(FRONTEND_DIR / "features.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Features page not found")

@app.get("/try-on", response_class=HTMLResponse)
async def try_on_page():
    """Serve the virtual try-on page"""
    try:
        with open(FRONTEND_DIR / "index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Try-on page not found")

@app.get("/htmlpage", response_class=HTMLResponse)
async def htmlpage():
    """Serve the htmlpage (currently empty)"""
    try:
        with open(FRONTEND_DIR / "htmlpage.html", "r", encoding="utf-8") as f:
            content = f.read()
            if not content.strip():
                # If empty, redirect to main page
                return HTMLResponse(content='<script>window.location.href="/";</script>')
            return HTMLResponse(content=content)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Page not found")

@app.post("/api/virtual-tryon")
async def virtual_tryon_api(
    person_image: UploadFile = File(...),
    clothing_image: UploadFile = File(...)
):
    """API endpoint for virtual try-on functionality"""
    try:
        # Save uploaded files temporarily
        person_image_path = BACKEND_DIR / "image1.jpeg"
        clothing_image_path = BACKEND_DIR / "image2.webp"
        
        # Save person image
        with open(person_image_path, "wb") as f:
            content = await person_image.read()
            f.write(content)
        
        # Save clothing image  
        with open(clothing_image_path, "wb") as f:
            content = await clothing_image.read()
            f.write(content)
        
        # Run the virtual try-on process
        run_virtual_tryon()
        
        # Check if result image was generated
        result_image_path = BACKEND_DIR / "virtual_try_on_result.png"
        if result_image_path.exists():
            # Add timestamp to prevent browser caching
            timestamp = int(time.time())
            return {
                "status": "success", 
                "message": "Virtual try-on completed successfully",
                "result_image_url": f"/api/result-image?t={timestamp}"
            }
        else:
            raise HTTPException(status_code=500, detail="Failed to generate result image")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Virtual try-on failed: {str(e)}")

@app.get("/api/result-image")
async def get_result_image():
    """Serve the generated virtual try-on result image"""
    result_image_path = BACKEND_DIR / "virtual_try_on_result.png"
    if result_image_path.exists():
        return FileResponse(
            result_image_path, 
            media_type="image/png",
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0"
            }
        )
    else:
        raise HTTPException(status_code=404, detail="Result image not found")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "Wardrobe AI server is running"}

if __name__ == "__main__":
    # Run the server
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
