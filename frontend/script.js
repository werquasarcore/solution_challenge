const BASE_URL = "http://127.0.0.1:8000/api";

// Add Report
function addReport() {
    fetch(BASE_URL + "/reports/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            title: document.getElementById("title").value,
            description: "Test",
            location: document.getElementById("location").value,
            category: "general",
            urgency: 5,
            severity: 4,
            people_affected: 10
        })
    })
    .then(res => res.json())
    .then(() => alert("Report Added"));
}

// Add Volunteer
function addVolunteer() {
    fetch(BASE_URL + "/volunteers/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            name: document.getElementById("name").value,
            skill: document.getElementById("skill").value,
            location: "Area A",
            available: true
        })
    })
    .then(res => res.json())
    .then(() => alert("Volunteer Added"));
}

// Chatbot
function askBot() {
    fetch(BASE_URL + "/chatbot/ask/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            question: document.getElementById("question").value
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("answer").innerText = data.answer;
    });
}

// Load Reports
function loadReports() {
    fetch(BASE_URL + "/reports/")
    .then(res => res.json())
    .then(data => {
        let html = "";
        data.forEach(r => {
            html += `<p>${r.title} - ${r.location}</p>`;
        });
        document.getElementById("reports").innerHTML = html;
    });
}