// const ctx = document.getElementById('featureChart').getContext('2d');
// const featureChart = new Chart(ctx, {
//     type: 'bar',
//     data: {
//         labels: ['Age', 'Sex', 'CP', 'Trestbps', 'Chol', 'FBS', 'RestECG', 'Thalach', 'Exang', 'Oldpeak', 'Slope', 'CA', 'Thal'],
//         datasets: [{
//             label: 'Feature Contributions',
//             data: feature_contributions,
//             backgroundColor: 'rgba(75, 192, 192, 0.2)',
//             borderColor: 'rgba(75, 192, 192, 1)',
//             borderWidth: 1
//         }]
//     },
//     options: {
//         responsive: true,
//         scales: {
//             y: {
//                 beginAtZero: true
//             }
//         }
//     }
// });

const ctx = document.getElementById('featureChart').getContext('2d');
    const featureChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Age', 'Sex', 'CP', 'Trestbps', 'Chol', 'FBS', 'RestECG', 'Thalach', 'Exang', 'Oldpeak', 'Slope', 'CA', 'Thal'],
            datasets: [{
                label: 'Feature Contributions',
                data: {{ feature_contributions | safe }},
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                     beginAtZero: true
                }
            }
        }
    });