const studentRecords = [
  { id: 1, name: "Shiva", additionalInfo: "Destroyer of evil" },
  { id: 2, name: "Vishnu", additionalInfo: "Preserver of the universe" },
  { id: 3, name: "Durga", additionalInfo: "Goddess of power and strength" },
  { id: 4, name: "Ganesha", additionalInfo: "Remover of obstacles" },
  { id: 5, name: "Krishna", additionalInfo: "God of compassion and love" },
  { id: 6, name: "Saraswati", additionalInfo: "Goddess of knowledge and arts" },
  { id: 7, name: "Lakshmi", additionalInfo: "Goddess of wealth and prosperity" },
  { id: 8, name: "Hanuman", additionalInfo: "Symbol of devotion and courage" },
  { id: 9, name: "Kali", additionalInfo: "Goddess of time and death" },
  { id: 10, name: "Brahma", additionalInfo: "Creator of the universe" }
];

function showSearchForm() {
  document.getElementById("searchForm").style.display = "block";
  document.getElementById("deleteForm").style.display = "none";
  document.getElementById("insertForm").style.display = "none";
  document.getElementById("records").style.display = "none";
}

function showDeleteForm() {
  document.getElementById("searchForm").style.display = "none";
  document.getElementById("deleteForm").style.display = "block";
  document.getElementById("insertForm").style.display = "none";
  document.getElementById("records").style.display = "none";
}

function showInsertForm() {
  document.getElementById("searchForm").style.display = "none";
  document.getElementById("deleteForm").style.display = "none";
  document.getElementById("insertForm").style.display = "block";
  document.getElementById("records").style.display = "none";
}



function deleteRecord() {
  const deleteId = parseInt(document.getElementById("deleteId").value);
  const index = studentRecords.findIndex(record => record.id === deleteId);
  if (index !== -1) {
    studentRecords.splice(index, 1);
    alert(`Student record with ID ${deleteId} deleted.`);
  } else {
    alert("No student record found for the provided ID.");
  }
}


function insertRecord() {
  const insertId = parseInt(document.getElementById("insertId").value);
  const insertName = document.getElementById("insertName").value;
  const insertInfo = document.getElementById("insertInfo").value;

  // Check if the ID already exists
  const existingRecord = studentRecords.find(record => record.id === insertId);
  if (existingRecord) {
    alert("A record with the provided ID already exists. Please enter a unique ID.");
    return;
  }

  // Insert the record
  studentRecords.push({ id: insertId, name: insertName, additionalInfo: insertInfo });
  alert("Student record inserted successfully.");
}

function displayRecords() {
  const tableBody = document.querySelector("#records tbody");
  tableBody.innerHTML = "";
  studentRecords.forEach(record => {
    const row = document.createElement("tr");
    row.innerHTML = `<td>${record.id}</td><td>${record.name}</td><td>${record.additionalInfo}</td>`;
    tableBody.appendChild(row);
  });
  document.getElementById("searchForm").style.display = "none";
  document.getElementById("deleteForm").style.display = "none";
  document.getElementById("insertForm").style.display = "none";
  document.getElementById("records").style.display = "table";
}

function deleteRecord() {
  const deleteId = parseInt(document.getElementById("deleteId").value);
  console.log("Delete ID:", deleteId);
  const index = studentRecords.findIndex(record => record.id === deleteId);
  console.log("Index:", index);
  if (index !== -1) {
    studentRecords.splice(index, 1);
    alert(`Student record with ID ${deleteId} deleted.`);
  } else {
    alert("No student record found for the provided ID.");
  }
}

function displayRecords() {
  const tableBody = document.querySelector("#records tbody");
  tableBody.innerHTML = "";
  studentRecords.forEach(record => {
    const row = document.createElement("tr");
    row.innerHTML = `<td>${record.id}</td><td>${record.name}</td><td>${record.additionalInfo}</td>`;
    tableBody.appendChild(row);
  });
  document.getElementById("searchForm").style.display = "none";
  document.getElementById("deleteForm").style.display = "none";
  document.getElementById("records").style.display = "table";
}