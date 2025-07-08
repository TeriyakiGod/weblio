document.addEventListener('DOMContentLoaded', function() {
    const tiles = document.querySelectorAll('.tile-block');
    
    tiles.forEach(tile => {
        const images = tile.querySelectorAll('img');
        
        if (images.length > 1) {
            // Position all images initially
            images.forEach((img, index) => {
                if (index === 0) {
                    img.style.transform = 'translateX(0%)';
                    img.style.zIndex = '10';
                } else {
                    img.style.transform = 'translateX(100%)';
                    img.style.zIndex = '1';
                }
            });
            
            let currentImageIndex = 0;
            
            function switchImage() {
                const currentImage = images[currentImageIndex];
                const nextImageIndex = (currentImageIndex + 1) % images.length;
                const nextImage = images[nextImageIndex];
                
                // Animate current image out (slide right)
                currentImage.style.transform = 'translateX(-100%)';
                currentImage.style.zIndex = '1';
                
                // Animate next image in (slide from right)
                nextImage.style.transform = 'translateX(0%)';
                nextImage.style.zIndex = '10';
                
                currentImageIndex = nextImageIndex;
                
                // Reset the previous image position after transition
                setTimeout(() => {
                    const prevImageIndex = currentImageIndex === 0 ? images.length - 1 : currentImageIndex - 1;
                    images[prevImageIndex].style.transform = 'translateX(100%)';
                }, 1500); // Wait for transition to complete
                
                // Set random interval for next switch (3-7 seconds)
                const randomInterval = Math.random() * 4000 + 3000;
                setTimeout(switchImage, randomInterval);
            }
            
            // Start the switching after initial random delay
            const initialDelay = Math.random() * 3000 + 1000;
            setTimeout(switchImage, initialDelay);
        }
    });
});