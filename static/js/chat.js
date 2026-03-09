new Chart(document.getElementById("roiChart"), {

type:"line",

data:{
labels:["Jan","Feb","Mar","Apr"],

datasets:[{
label:"ROI",
data:[100,150,220,300],
borderColor:"#4f6cff",
backgroundColor:"rgba(79,108,255,0.2)",
fill:true
}]
},

options:{
responsive:false
}

})