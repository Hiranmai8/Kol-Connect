// Wallet System

document.addEventListener("DOMContentLoaded", function(){

const walletTable = document.getElementById("walletTable");

let transactions = [
{date:"2025-01-10",type:"Payment Received",amount:300,status:"Completed"},
{date:"2025-01-12",type:"Withdrawal",amount:-100,status:"Pending"},
{date:"2025-01-18",type:"Payment Received",amount:500,status:"Completed"}
];

renderWallet();


function renderWallet(){

if(!walletTable) return;

walletTable.innerHTML = "";

transactions.forEach(t=>{

const row = document.createElement("tr");

row.innerHTML = `
<td>${t.date}</td>
<td>${t.type}</td>
<td>$${t.amount}</td>
<td>${t.status}</td>
`;

walletTable.appendChild(row);

});

}

});