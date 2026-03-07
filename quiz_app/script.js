// Dummy questions
const questions = [
            {
                question: "What does HTML stand for?",
                answers: [
                    { text: "Hyper Text Markup Language", correct: true },
                    { text: "Home Tool Markup Language", correct: false },
                    { text: "High Tech Main Language", correct: false }
                ]
            },
            {
                question: "Which language is used to style webpages?",
                answers: [
                    { text: "CSS", correct: true },
                    { text: "HTML", correct: false },
                    { text: "Python", correct: false }
                ]
            },
            {
                question: "Which language adds interactivity to webpages?",
                answers: [
                    { text: "JavaScript", correct: true },
                    { text: "CSS", correct: false },
                    { text: "HTML", correct: false }
                ]
            },
            {
                question: "Which JavaScript keyword is used to create a variable?",
                answers: [
                    { text: "let", correct: true },
                    { text: "button", correct: false },
                    { text: "style", correct: false }
                ]
            },
            {
                question: "Which method is used to select an element by ID?",
                answers: [
                    { text: "document.getElementById()", correct: true },
                    { text: "document.makeElement()", correct: false },
                    { text: "document.styleElement()", correct: false }
                ]
            }
        ];


// DOM - Document Object Model
// Elements
const questionEl = document.querySelector("#question")
const answerEl = document.querySelector("#answers")
const scoreEl = document.querySelector("#score")
const progressEl = document.querySelector("#progress")
const feedbackEl = document.querySelector("#feedback")
const finalScoreEl = document.querySelector("#final-score")
const resultBox = document.querySelector("#result-box")
const quizArea = document.querySelector(".quiz-area")
const themeBtn = document.querySelector("#theme-btn")
const nextBtn = document.querySelector("#next-btn")
const restartBtn = document.querySelector("#restart-btn")


let questionIndex = 0
let score = 0
questionEl.textContent = questions[questionIndex].question
function startQuiz() {
    questionIndex = 0
    score = 0
    scoreEl.textContent = "Score: 0"
    scoreEl.style.display = "block"
    quizArea.style.display = "block"
    resultBox.style.display = "none"
    showQuestions()
}

function showQuestions(){
    answerEl.innerHTML = ""
    feedbackEl.textContent = ""
    const currentQuestion = question[questionIndex]
    questionEl.textContent = currentQuestion
    progressEl.textContent = `Question ${questionIndex + 1} of ${questions.length}`
    // currentQuestion.answers.forEach(answer => {
    //     const button = document.createElement("button")
    //     button.textContent = answer.text
    //     button.classList.add("answer-btn")

    //     if (answer.correct) {
    //         button.dataset.correct

    //     }
    //     button.addEventListener("click", ()=> console.log("well done")
    //     )

    //     answerEl.appendChild(button)
    // });
}

startQuiz()
nextBtn.addEventListener("click", ()=> {
    questionIndex++
    questionEl.textContent = questions[questionIndex].question
})

restartBtn.addEventListener("click", ()=> {
    questionIndex = 0
    questionEl.textContent = questions[questionIndex].question
})