const jobTitles = [
    "Software Developer", "Web Developer", "Mobile Developer", "Data Analyst",
    "Data Scientist", "System Administrator", "Network Engineer", "IT Support Specialist",
    "Cybersecurity Analyst", "Database Administrator", "Cloud Architect", "DevOps Engineer",
    "IT Project Manager", "Business Intelligence Analyst", "IT Consultant", "UX/UI Designer",
    "QA Engineer", "Machine Learning Engineer", "Artificial Intelligence Engineer", "Technical Writer"
];

function filterSuggestions() {
    const input = document.getElementById("job").value.trim().toLowerCase();
    const suggestionsContainer = document.getElementById("suggestions-container");
    suggestionsContainer.innerHTML = "";

    if (!input) {
        suggestionsContainer.style.display = "none";
        return;
    }

    const matches = jobTitles.filter(title => title.toLowerCase().includes(input));

    if (matches.length > 0) {
        suggestionsContainer.style.display = "block";
        matches.forEach(title => {
            const suggestionItem = document.createElement("div");
            suggestionItem.className = "suggestion-item";
            suggestionItem.textContent = title;
            suggestionItem.onclick = () => selectSuggestion(title);
            suggestionsContainer.appendChild(suggestionItem);
        });
    } else {
        suggestionsContainer.style.display = "none";
    }
}

function selectSuggestion(title) {
    document.getElementById("job").value = title;
    document.getElementById("suggestions-container").style.display = "none";
}

function goBack() {
    alert("No previous page implemented yet.");
}
