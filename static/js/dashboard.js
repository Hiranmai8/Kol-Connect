// Revenue Chart

const revenueChart = new Chart(
document.getElementById('revenueChart'),
{
type: 'bar',
data: {
labels: ['Sep','Oct','Nov','Dec','Jan','Feb'],
datasets: [{
label: 'Revenue',
data: [1200,2000,1600,3000,2500,3800],
}]
}
}
);

// Engagement Chart

const engagementChart = new Chart(
document.getElementById('engagementChart'),
{
type: 'line',
data: {
labels: ['Sep','Oct','Nov','Dec','Jan','Feb'],
datasets: [{
label: 'Engagement %',
data: [3.2,3.8,4.1,3.9,4.5,5.2],
}]
}
}
);
// BAR CHART

const barCtx = document.getElementById('barChart');

new Chart(barCtx,{
type:'bar',
data:{
labels:['Sep','Oct','Nov','Dec','Jan','Feb'],
datasets:[{
label:'Budget',
data:[4500,8000,6500,12000,9000,15000],
backgroundColor:'#4f6cff'
}]
},
options:{
responsive:true
}
});


// PIE CHART

const pieCtx = document.getElementById('pieChart');

new Chart(pieCtx,{
type:'pie',
data:{
labels:['Instagram','YouTube','TikTok','X'],
datasets:[{
data:[45,30,20,5],
backgroundColor:[
'#4f6cff',
'#ff9f43',
'#1dd1a1',
'#576574'
]
}]
}
});