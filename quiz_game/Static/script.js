/* // static/quiz_game/script.js

document.addEventListener('DOMContentLoaded', function () {
    const quizForm = document.getElementById('quizForm');
    const nextButton = document.getElementById('nextButton');
    const questions = document.querySelectorAll('.question');
    let currentQuestionIndex = 0;
    let score = 0;

    // Hide all questions except the first one
    questions.forEach(function (question, index) {
        if (index !== currentQuestionIndex) {
            question.style.display = 'none';
        }
    });

    nextButton.addEventListener('click', function () {
        // Get the selected option
        const selectedOption = document.querySelector(`input[name="question${questions[currentQuestionIndex].dataset.questionId}"]:checked`);
        if (selectedOption) {
            // Update score if the selected option is correct
            if (selectedOption.dataset.isCorrect === 'true') {
                score += 100;
            }
            // Display the next question
            questions[currentQuestionIndex].style.display = 'none';
            currentQuestionIndex++;
            if (currentQuestionIndex < questions.length) {
                questions[currentQuestionIndex].style.display = 'block';
            } else {
                // Submit the quiz if all questions have been answered
                quizForm.submit();
            }
        } else {
            alert('Please select an option.');
        }
    });
}); */
document.addEventListener('DOMContentLoaded', function () {
    const quizForm = document.getElementById('quizForm');
    const nextButton = document.getElementById('nextButton');
    const questions = document.querySelectorAll('.question');
    let currentQuestionIndex = 0;
    let score = 0;

    // Hide all questions except the first one
    questions.forEach(function (question, index) {
        if (index !== currentQuestionIndex) {
            question.style.display = 'none';
        }
    });

    nextButton.addEventListener('click', function () {
        // Get the selected option
        const selectedOption = document.querySelector(`input[name="question${questions[currentQuestionIndex].dataset.questionId}"]:checked`);
        if (selectedOption) {
            // Update score if the selected option is correct
            if (selectedOption.dataset.isCorrect === 'true') {
                score += 100;
            }
            // Display the next question
            questions[currentQuestionIndex].style.display = 'none';
            currentQuestionIndex++;
            if (currentQuestionIndex < questions.length) {
                questions[currentQuestionIndex].style.display = 'block';
            } else {
                // Submit the quiz if all questions have been answered
                quizForm.submit();
            }
        } else {
            alert('Please select an option.');
        }
    });
});

// script.js
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        const username = form.querySelector('#id_username').value.trim();
        const email = form.querySelector('#id_email').value.trim();
        const password1 = form.querySelector('#id_password1').value;
        const password2 = form.querySelector('#id_password2').value;

        if (username === '' || email === '' || password1 === '' || password2 === '') {
            event.preventDefault(); // Prevent form submission
            alert('All fields are required.');
            return;
        }

        if (password1 !== password2) {
            event.preventDefault(); // Prevent form submission
            alert('Passwords do not match.');
            return;
        }

        if (password1.length < 8) {
            event.preventDefault(); // Prevent form submission
            alert('Password must be at least 8 characters long.');
            return;
        }
    });
});
