document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.weather-background');
    const condition = container.dataset.condition;
    
    const backgrounds = {
        'Overcast': 'url(/static/img/overcast.jpg)',
        'Clear': 'url(/static/img/sunny.jpg)',
        'Clouds': 'url(/static/img/cloudy.jpg)',
        'Rain': 'url(/static/img/rainy.jpg)'
    };
    
    if (backgrounds[condition]) {
        container.style.backgroundImage = backgrounds[condition];
        container.style.transition = 'background-image 0.5s ease';
    }
});