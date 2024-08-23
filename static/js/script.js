function submitCode() {
    const code = document.getElementById('code').value;
    
    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `code=${encodeURIComponent(code)}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `
            <p>Score: ${data.score}%</p>
            <p>Passed Tests: ${data.passed_tests}/${data.total_tests}</p>
        `;
    })
    .catch(error => {
        document.getElementById('result').innerHTML = `
            <p style="color: red;">An error occurred: ${error.message}</p>
        `;
    });
}
