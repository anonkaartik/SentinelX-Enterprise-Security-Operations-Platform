function updateTime(){

    const now=new Date();

    const options={
        weekday:"short",
        day:"2-digit",
        month:"short",
        year:"numeric",
        hour:"2-digit",
        minute:"2-digit",
        second:"2-digit"
    };

    document.getElementById("datetime").innerHTML=
        now.toLocaleString("en-IN",options);

}

updateTime();

setInterval(updateTime,1000);