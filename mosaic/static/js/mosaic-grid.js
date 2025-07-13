// Calculate grid size and apply to mosaic grids
document.addEventListener('DOMContentLoaded', function() {
    const mosaicGrids = document.querySelectorAll('.mosaic-grid');
    
    function applyGridLayout() {
        mosaicGrids.forEach(function(grid) {
            const tiles = grid.children;
            const tileCount = tiles.length;
            
            if (tileCount === 0) return;
            
            // Check if mobile
            const isMobile = window.innerWidth <= 768;
            
            if (isMobile) {
                // Mobile: column layout
                grid.style.display = 'flex';
                grid.style.flexDirection = 'column';
                grid.style.gridTemplateColumns = '';
                grid.style.gridTemplateRows = '';
                grid.style.height = 'auto';
                grid.style.overflowY = 'auto';
            } else {
                // Desktop: grid layout
                const gridSize = Math.ceil(Math.sqrt(tileCount));
                
                grid.style.display = 'grid';
                grid.style.flexDirection = '';
                grid.style.gridTemplateColumns = `repeat(${gridSize}, 1fr)`;
                grid.style.gridTemplateRows = `repeat(${gridSize}, 1fr)`;
                grid.style.height = '100%';
                grid.style.minHeight = '400px';
                grid.style.overflowY = 'hidden';
            }
            
            grid.style.gap = '0px';
            grid.style.width = '100%';
            grid.style.padding = '0';
        });
    }
    
    // Apply on load
    applyGridLayout();
    
    // Apply on resize
    window.addEventListener('resize', applyGridLayout);
});