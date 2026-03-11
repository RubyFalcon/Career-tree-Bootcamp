// Dummy questions
let questions = [];

async function loadQuestions() {
  try {
    const response = await fetch("./questions.json");
    questions = await response.json();
    startQuiz();
  } catch (error) {
    questionEl.textContent = "Failed to load quiz questions.";
    console.log(error);
  }
}

// DOM - Document Object Model
// Elements
const questionEl = document.querySelector("#question");
const answerEl = document.querySelector("#answers");
const scoreEl = document.querySelector("#score");
const progressEl = document.querySelector("#progress");
const feedbackEl = document.querySelector("#feedback");
const finalScoreEl = document.querySelector("#final-score");
const resultBox = document.querySelector("#result-box");
const quizArea = document.querySelector(".quiz-area");
const themeBtn = document.querySelector("#theme-btn");
const nextBtn = document.querySelector("#next-btn");
const restartBtn = document.querySelector("#restart-btn");

let questionIndex = 0;
let score = 0;
// questionEl.textContent = questions[questionIndex].question
function startQuiz() {
  questionIndex = 0;
  score = 0;
  scoreEl.textContent = `Score : ${score}`;
  scoreEl.style.display = "block";
  quizArea.style.display = "block";
  resultBox.style.display = "none";
  showQuestions();
}

function shuffleArray(array) {
    return array.sort(() => Math.random() - 0.5)
}

function showQuestions() {
  answerEl.innerHTML = "";
  feedbackEl.textContent = "";
  const currentQuestion = questions[questionIndex];
  const shuffledAnswers = shuffleArray([...currentQuestion.answers])
  questionEl.textContent = currentQuestion.question;
  progressEl.textContent = `Question ${questionIndex + 1} of ${questions.length}`;

  shuffledAnswers.forEach( answer => {
    const button = document.createElement("button");
    button.textContent = answer.text;
    button.classList.add("answer-btn");

    if (answer.correct) {
      button.dataset.correct = "true";
    }
    button.addEventListener("click", selectAnswer);
    answerEl.appendChild(button);
  });
}

function selectAnswer(event) {
  const selectedButton = event.target;
  const isCorrect = selectedButton.dataset.correct === "true";
  if (isCorrect) {
    feedbackEl.textContent = "Correct";
    score++;
    scoreEl.textContent = `Score: ${score}`;
  } else {
    feedbackEl.textContent = "Wrong answer";
  }
  const allButtons = answerEl.querySelectorAll("button");
  allButtons.forEach(function (button) {
    if (button.dataset.correct === "true") {
      button.classList.add("correct");
    } else {
      button.classList.add("incorrect");
    }
    button.disabled = true;
  });
}

function nextQuestion() {
  questionIndex++;
  if (questionIndex < questions.length) {
    showQuestions();
  } else {
    showResult();
  }
}

function showResult() {
  quizArea.style.display = "none";
  resultBox.style.display = "block";
  finalScoreEl.textContent = `You scored ${score} out of ${questions.length}.`;
}

nextBtn.addEventListener("click", nextQuestion);
restartBtn.addEventListener("click", startQuiz);

themeBtn.addEventListener("click", function () {
  document.body.classList.toggle("dark-mode");
});

loadQuestions();
