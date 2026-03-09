// Campaign Management

document.addEventListener("DOMContentLoaded", () => {

const campaignForm = document.getElementById("campaignForm");
const campaignList = document.getElementById("campaignList");

let campaigns = [];

// Create Campaign
if(campaignForm){

campaignForm.addEventListener("submit", function(e){
e.preventDefault();

const title = document.getElementById("title").value;
const budget = document.getElementById("budget").value;
const deadline = document.getElementById("deadline").value;

if(title === "" || budget === ""){
alert("Please fill required fields");
return;
}

const campaign = {
title,
budget,
deadline,
status:"Active"
};

campaigns.push(campaign);

renderCampaigns();

campaignForm.reset();

});

}

// Render Campaign Cards
function renderCampaigns(){

if(!campaignList) return;

campaignList.innerHTML = "";

if(campaigns.length === 0){

campaignList.innerHTML = `
<div class="empty">
No campaigns created yet
</div>
`;

return;
}

campaigns.forEach((campaign,index)=>{

const card = document.createElement("div");

card.className = "campaign-card";

card.innerHTML = `
<h3>${campaign.title}</h3>
<p><b>Budget:</b> $${campaign.budget}</p>
<p><b>Deadline:</b> ${campaign.deadline}</p>
<p><b>Status:</b> ${campaign.status}</p>

<button onclick="deleteCampaign(${index})">
Delete
</button>
`;

campaignList.appendChild(card);

});

}

window.deleteCampaign = function(index){

campaigns.splice(index,1);
renderCampaigns();

}

});