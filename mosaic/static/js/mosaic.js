document.addEventListener('DOMContentLoaded', function() {
    const tiles = document.querySelectorAll('.tile-block');
    
    tiles.forEach(tile => {
        const images = tile.querySelectorAll('img');
        const transition = tile.dataset.transition || 'fade';
        
        if (images.length > 1) {
            // Special handling for flip transitions - flip the entire tile
            if (transition.startsWith('flip')) {
                setupFlipTransition(tile, images, transition);
            } else {
                setupImageTransition(tile, images, transition);
            }
        }
    });
    
    function setupImageTransition(tile, images, transition) {
        // Hide all images except the first
        images.forEach((img, index) => {
            if (index === 0) {
                img.style.opacity = '1';
                img.style.zIndex = '10';
            } else {
                setInitialState(img, transition);
                img.style.zIndex = '1';
            }
        });
        
        let currentImageIndex = 0;
        
        function switchImage() {
            const currentImage = images[currentImageIndex];
            const nextImageIndex = (currentImageIndex + 1) % images.length;
            const nextImage = images[nextImageIndex];
            
            // Set z-index for proper layering
            nextImage.style.zIndex = '10';
            currentImage.style.zIndex = '1';
            
            // Animate based on transition type
            animateTransition(currentImage, nextImage, transition).then(() => {
                // Reset the previous image after animation
                setInitialState(currentImage, transition);
            });
            
            currentImageIndex = nextImageIndex;
            
            // Schedule next transition
            const randomInterval = Math.random() * 4000 + 3000;
            setTimeout(switchImage, randomInterval);
        }
        
        // Start the transitions after initial delay
        const initialDelay = Math.random() * 3000 + 1000;
        setTimeout(switchImage, initialDelay);
    }
    
    function setupFlipTransition(tile, images, transition) {
        // Show only the first image initially
        images.forEach((img, index) => {
            if (index === 0) {
                img.style.opacity = '1';
            } else {
                img.style.opacity = '0';
            }
        });
        
        let currentImageIndex = 0;
        
        function flipTile() {
            const nextImageIndex = (currentImageIndex + 1) % images.length;
            const currentImage = images[currentImageIndex];
            const nextImage = images[nextImageIndex];
            
            // Get flip direction
            const flipDirection = getFlipDirection(transition);
            
            // Handle diagonal flip specially
            if (transition === 'flip-diagonal') {
                anime.timeline()
                    .add({
                        targets: tile,
                        rotateX: 90,
                        rotateY: 90,
                        duration: 750,
                        easing: 'easeInOutCubic',
                        complete: () => {
                            currentImage.style.opacity = '0';
                            nextImage.style.opacity = '1';
                        }
                    })
                    .add({
                        targets: tile,
                        rotateX: 0,
                        rotateY: 0,
                        duration: 750,
                        easing: 'easeInOutCubic'
                    });
            } else {
                // Regular flip - simple and clean
                anime.timeline()
                    .add({
                        targets: tile,
                        [flipDirection.axis]: flipDirection.half,
                        duration: 750,
                        easing: 'easeInOutCubic',
                        complete: () => {
                            // At the halfway point, swap images
                            currentImage.style.opacity = '0';
                            nextImage.style.opacity = '1';
                        }
                    })
                    .add({
                        targets: tile,
                        [flipDirection.axis]: 0,
                        duration: 750,
                        easing: 'easeInOutCubic'
                    });
            }
            
            currentImageIndex = nextImageIndex;
            
            // Schedule next flip
            const randomInterval = Math.random() * 4000 + 3000;
            setTimeout(flipTile, randomInterval);
        }
        
        // Start flipping after initial delay
        const initialDelay = Math.random() * 3000 + 1000;
        setTimeout(flipTile, initialDelay);
    }
    
    function getFlipDirection(transition) {
        switch (transition) {
            case 'flip':
            case 'flip-x':
                return { axis: 'rotateY', half: 90 };
            case 'flip-y':
                return { axis: 'rotateX', half: 90 };
            case 'flip-diagonal':
                return { axis: 'rotateY', half: 90 };
            case 'flip-random':
                const randomFlips = [
                    { axis: 'rotateY', half: 90 },
                    { axis: 'rotateX', half: 90 }
                ];
                return randomFlips[Math.floor(Math.random() * randomFlips.length)];
            default:
                return { axis: 'rotateY', half: 90 };
        }
    }
    
    function setInitialState(img, transition) {
        // Stop any existing animations and reset
        anime.remove(img);
        img.style.opacity = '1';
        img.style.transform = '';
        
        switch (transition) {
            case 'fade':
                img.style.opacity = '0';
                break;
            case 'slide-left':
                anime.set(img, { translateX: '100%' });
                break;
            case 'slide-right':
                anime.set(img, { translateX: '-100%' });
                break;
            case 'slide-up':
                anime.set(img, { translateY: '100%' });
                break;
            case 'slide-down':
                anime.set(img, { translateY: '-100%' });
                break;
            case 'zoom':
                anime.set(img, { scale: 0 });
                break;
            case 'flip':
            case 'flip-x':
                anime.set(img, { rotateY: 90 });
                break;
            case 'flip-y':
                anime.set(img, { rotateX: 90 });
                break;
        }
    }
    
    function animateTransition(currentImage, nextImage, transition) {
        const duration = 1500;
        const exitEasing = 'easeInCubic';  // Faster start for exiting
        const enterEasing = 'easeOutCubic'; // Slower start for entering
        
        return new Promise((resolve) => {
            switch (transition) {
                case 'fade':
                    anime.timeline()
                        .add({
                            targets: currentImage,
                            opacity: 0,
                            duration: duration,
                            easing: 'easeInOutQuad',
                        })
                        .add({
                            targets: nextImage,
                            opacity: 1,
                            duration: duration,
                            easing: 'easeInOutQuad',
                            complete: resolve
                        }, 0);
                    break;
                    
                case 'slide-left':
                    anime.timeline()
                        .add({
                            targets: currentImage,
                            translateX: '-100%',
                            duration: duration,
                            easing: 'easeInOutCubic'
                        })
                        .add({
                            targets: nextImage,
                            translateX: '0%',
                            duration: duration,
                            easing: 'easeInOutCubic',
                            complete: resolve
                        }, 0);
                    break;
                    
                case 'slide-right':
                    anime.timeline()
                        .add({
                            targets: currentImage,
                            translateX: '100%',
                            duration: duration,
                            easing: 'easeInOutCubic'
                        })
                        .add({
                            targets: nextImage,
                            translateX: '0%',
                            duration: duration,
                            easing: 'easeInOutCubic',
                            complete: resolve
                        }, 0);
                    break;
                    
                case 'slide-up':
                    anime.timeline()
                        .add({
                            targets: currentImage,
                            translateY: '-100%',
                            duration: duration,
                            easing: 'easeInOutCubic'
                        })
                        .add({
                            targets: nextImage,
                            translateY: '0%',
                            duration: duration,
                            easing: 'easeInOutCubic',
                            complete: resolve
                        }, 0);
                    break;
                    
                case 'slide-down':
                    anime.timeline()
                        .add({
                            targets: currentImage,
                            translateY: '100%',
                            duration: duration,
                            easing: 'easeInOutCubic'
                        })
                        .add({
                            targets: nextImage,
                            translateY: '0%',
                            duration: duration,
                            easing: 'easeInOutCubic',
                            complete: resolve
                        }, 0);
                    break;
                    
                case 'flip-x':
                    anime.timeline()
                        .add({
                            targets: currentImage,
                            rotateY: 90,
                            duration: duration / 2,
                            easing: exitEasing
                        })
                        .add({
                            targets: nextImage,
                            rotateY: [-90, 0],
                            duration: duration / 2,
                            easing: enterEasing,
                            complete: resolve
                        });
                    break;
                    
                case 'flip-y':
                    anime.timeline()
                        .add({
                            targets: currentImage,
                            rotateX: 90,
                            duration: duration / 2,
                            easing: exitEasing
                        })
                        .add({
                            targets: nextImage,
                            rotateX: [-90, 0],
                            duration: duration / 2,
                            easing: enterEasing,
                            complete: resolve
                        });
                    break;
                
                default:
                    // Fallback to fade
                    return animateTransition(currentImage, nextImage, 'fade');
            }
        });
    }
});