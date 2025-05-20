document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.weather-background');
    const condition = container.dataset.condition;
    
    const backgrounds = {
        'Thunderstorm': 'url(/static/img/thunderstorm.png)',
        'Clear': 'url(/static/img/clear.png)',
        'Clouds': 'url(/static/img/clouds.png)',
        'Rain': 'url(/static/img/rain.png)',
        'Drizzle': 'url(/static/img/drizzle.png)',
    };
    
    if (backgrounds[condition]) {
        container.style.backgroundImage = backgrounds[condition];
        container.style.transition = 'background-image 0.5s ease';
    }
});