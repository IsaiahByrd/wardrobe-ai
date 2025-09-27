<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FitDoctor.tech - Try Clothes On Virtually!</title>
    <!-- Link to your CSS file for styling -->
    <link rel="stylesheet" href="style.css">
    <!-- Optional: Favicon for your site -->
    <link rel="icon" href="favicon.ico" type="image/x-icon">
</head>
<body>
    <header>
        <div class="container">
            <a href="index.html" class="logo">FitDoctor.tech</a>
            <nav>
                <ul>
                    <li><a href="#how-it-works">How It Works</a></li>
                    <li><a href="#features">Features</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main>
        <section id="hero" class="hero-section">
            <div class="container">
                <h1>Experience Virtual Try-On Like Never Before!</h1>
                <p class="tagline">Upload your photo and any outfit. Our AI does the rest.</p>
                <button class="cta-button" onclick="document.getElementById('try-on-section').scrollIntoView({ behavior: 'smooth' });">Try It Now!</button>
            </div>
        </section>

        <section id="try-on-section" class="try-on-section">
            <div class="container">
                <h2>Your Virtual Fitting Room</h2>
                <p>Upload two images below to see the magic happen.</p>

                <div class="upload-area">
                    <div class="upload-card">
                        <h3>1. Your Photo</h3>
                        <div class="image-preview" id="person-image-preview">
                            <p>No image selected</p>
                            <!-- Image will be displayed here by JavaScript -->
                        </div>
                        <input type="file" id="person-image-upload" accept="image/*" class="file-input">
                        <label for="person-image-upload" class="upload-button">Upload Your Photo</label>
                        <p class="tip">Ensure good lighting and full body visible for best results.</p>
                    </div>

                    <div class="upload-card">
                        <h3>2. Clothing Photo</h3>
                        <div class="image-preview" id="clothing-image-preview">
                            <p>No image selected</p>
                            <!-- Image will be displayed here by JavaScript -->
                        </div>
                        <input type="file" id="clothing-image-upload" accept="image/*" class="file-input">
                        <label for="clothing-image-upload" class="upload-button">Upload Clothing Photo</label>
                        <p class="tip">Clothing should be clearly visible, ideally on a plain background.</p>
                    </div>
                </div>

                <button id="process-button" class="cta-button process-button" disabled>Generate Try-On</button>
                <p id="processing-status" class="status-message"></p>

                <div class="result-area">
                    <h3>Your Virtual Try-On Result</h3>
                    <div class="result-image-container" id="result-image-container">
                        <img src="placeholder-result.png" alt="Virtual try-on result" id="result-image">
                        <p id="result-placeholder">Your generated image will appear here.</p>
                    </div>
                    <button id="download-button" class="secondary-button" disabled>Download Result</button>
                </div>
            </div>
        </section>

        <section id="how-it-works" class="info-section">
            <div class="container">
                <h2>How FitDoctor.tech Works</h2>
                <div class="step-cards">
                    <div class="step-card">
                        <span class="step-number">1</span>
                        <h3>Upload Images</h3>
                        <p>Provide a clear photo of yourself and another of the clothing item you want to try.</p>
                    </div>
                    <div class="step-card">
                        <span class="step-number">2</span>
                        <h3>AI Processes</h3>
                        <p>Our advanced AI analyzes both images and seamlessly integrates the clothing onto your body.</p>
                    </div>
                    <div class="step-card">
                        <span class="step-number">3</span>
                        <h3>View & Download</h3>
                        <p>Instantly see your virtual try-on! Save and share your new look.</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="features" class="info-section alternate-bg">
            <div class="container">
                <h2>Why Choose FitDoctor.tech?</h2>
                <ul>
                    <li><strong>Realistic Try-Ons:</strong> Our AI ensures natural-looking results.</li>
                    <li><strong>Save Time & Effort:</strong> No more changing rooms or returns!</li>
                    <li><strong>Explore Styles:</strong> Experiment with countless outfits from home.</li>
                    <li><strong>Privacy Focused:</strong> Your images are processed securely and not stored indefinitely.</li>
                </ul>
            </div>
        </section>

        <section id="contact" class="contact-section">
            <div class="container">
                <h2>Get in Touch</h2>
                <p>Have questions or feedback? We'd love to hear from you!</p>
                <form action="#" method="POST" class="contact-form">
                    <input type="text" placeholder="Your Name" required>
                    <input type="email" placeholder="Your Email" required>
                    <textarea placeholder="Your Message" rows="5" required></textarea>
                    <button type="submit" class="cta-button">Send Message</button>
                </form>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 FitDoctor.tech. All rights reserved.</p>
            <div class="footer-links">
                <a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a>
            </div>
        </div>
    </footer>

    <!-- Link to your JavaScript file for interactivity -->
    <script src="script.js"></script>
</body>
</html>