document.getElementById('quiz-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const quizData = Object.fromEntries(formData.entries());

    fetch('/api/quiz', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(quizData),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const resultMessage = document.getElementById('result-message');
        if (data.matchResult) {
            resultMessage.innerText = `Match found! You are suited for: ${data.predictedJob}`;
        } else {
            let recommendations = data.recommendedJobs.join(', ') || 'No recommendations available';
            resultMessage.innerText = `No match for your selected job. Recommended jobs: ${recommendations}`;
        }
        document.getElementById('result-container').style.display = 'block';
    })
    .catch(error => console.error('Error:', error));
});

function restartQuiz() {
    document.getElementById('quiz-form').reset();
    document.getElementById('result-container').style.display = 'none';
}
