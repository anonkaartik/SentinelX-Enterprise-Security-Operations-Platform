const ctx=document.getElementById("threatChart");

if(ctx){

new Chart(ctx,{
type:"line",
data:{
labels:["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
datasets:[{
label:"Threats",
data:[18,32,27,45,38,55,41],
tension:.4
}]
},
options:{
responsive:true,
plugins:{
legend:{
display:false
}
}
}
});

}

function updateTime(){

const now=new Date();

document.getElementById("datetime").innerHTML=
now.toLocaleString("en-IN");

}

updateTime();

setInterval(updateTime,1000);