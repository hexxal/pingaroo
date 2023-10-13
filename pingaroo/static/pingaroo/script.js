var chartElements = document.querySelectorAll('.chart');

fetch('http://localhost:8000/api/foo/')
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        chartElements.forEach(function (chartElement, index) {
            var author = data[index];
            if (author) {
                var options = {
                    series: author.results.series,
                    chart: {
                        type: 'line',
                        animations: { enabled: false },
                        toolbar: { show: false },
                        background: 'transparent',
                        foreColor: '#fff',
                        height: '80%',
                        width: '100%',
                    },
                    dataLabels: { enabled: false },
                    stroke: { curve: 'smooth' },
                    grid: {
                        show: false, // Toggle for debugging
                    },
                    xaxis: {
                        labels: { show: false },
                    },
                    yaxis: {
                        labels: { show: false },
                        min: 0,
                        max: 400,
                        tickAmount: 3,
                    },
                    theme: {
                        mode: 'dark',
                        palette: 'palette2'
                    },
                    padding: { top: 0, right: 0, bottom: 0, left: 0 },
                };
                var chart = new ApexCharts(chartElement, options);
                chart.render();
            }
        });
    });

// var options = {
//     series: [{
//         data: [218, 242, 241, 264, 180, 170, 168, 172, 154]
//     }],
//     chart: {
//         type: 'line',
//         animations: { enabled: false },
//         toolbar: { show: false },
//         background: 'transparent',
//         foreColor: '#fff',
//         height: '100%',
//     },
//     dataLabels: { enabled: false },
//     stroke: { curve: 'smooth' },
//     grid: {
//         show: false, // Toggle for debugging
//     },
//     xaxis: {
//         labels: { show: false },
//     },
//     yaxis: {
//         labels: { show: false },
//         min: 100,
//         max: 400,
//         tickAmount: 3,
//     },
//     theme: {
//         mode: 'dark',
//         palette: 'palette2'
//     },
//     padding: { top: 0, right: 0, bottom: 0, left: 0 }, // Remove all padding
// };

// var chart = new ApexCharts(document.querySelector("#chart"), options);
// chart.render();