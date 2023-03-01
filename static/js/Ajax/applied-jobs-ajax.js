async function getNumber(id) {


    var elements = document.getElementsByClassName('pixel'); // get all elements

    for(var i = 0; i < elements.length; i++){
        elements[i].style.backgroundColor = "white";
    }

    post_id=id


    console.log("post__id="+post_id)
    let response = await fetch('',{

        method: "get",

        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": 'application/json',
            text: post_id,
        }

    }

    )

    let data = await response.json()
    var auth = data["auth"]
    var element = document.getElementById("detailsRow");

    if (element) {
        var display = element.style.display;

        if (display == "none") {
            element.style.display = "flex";
        }
    }
    const mobile = window.matchMedia('(max-width: 767px)');
    if(mobile.matches){

    }else{
        if(id != 0){
            var select = document.getElementById('select'+id)
            select.style.backgroundColor = "#E7F1FE";
        }

        if(id == 0){
            id=data["post_id"]
            var select = document.getElementById('select'+id)
            select.style.backgroundColor = "#E7F1FE";
        }
    }

    let textarea = document.getElementById('message');
    textarea.innerHTML=data["description"]


    var element = document.getElementById("job_title");
    element.innerHTML = data["title"]

    var city_jobs = document.getElementById("city")
    city_jobs.innerHTML = data["city_j"]+",  "+data["country"]

    var countApplicant = document.getElementById("countApplicant")

    if(data["appNo"]==0){
        countApplicant.innerHTML = data["appNo"]+" Applicants"
    }else if(data["appNo"]>=2){
        countApplicant.innerHTML = data["appNo"]+" Applicants"
    }
    else{
        countApplicant.innerHTML = data["appNo"]+" Applicant"
    }

    var start_date = document.getElementById("sDate");
    start_date.innerHTML = data["start_date"] +" - "+data["end_date"];


    var comp = document.getElementById("company")
    comp.innerHTML=data["company"]

        function getMonthDifference(startDate, endDate) {
          return (
            endDate.getMonth() -
            startDate.getMonth() +
            12 * (endDate.getFullYear() - startDate.getFullYear())
          );
        }

        var c= (getMonthDifference(
          new Date(data["SDate"]), new Date(data["EDate"]))
        );
        var total = (data["salary"]*data['hourPerWork'])*4*c;

        var tt  = Math.floor(total);
        if(data["country"]== "USA"){
        var salary = document.getElementById("salary")
        salary.innerHTML ="$"+ data ["salary"]+"/hour"
        document.getElementById("totsalary").innerHTML="$"+tt.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")+" total income";

        }else{
            var salary = document.getElementById("salary")
        salary.innerHTML ="€"+ data ["salary"]+"/hour"
        document.getElementById("totsalary").innerHTML="€"+tt.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")+" total income";

        }
    var typeOfWork = document.getElementById('typeOfWork')
    typeOfWork.innerHTML = data["typeOfWork"]+" "

    var hourPerWork = document.getElementById('hourPerWork')
    hourPerWork.innerHTML = " "+data['hourPerWork']+" hours/week"

    var housing = document.getElementById("housing")
    housing.innerHTML = "Housing "+data['housing']
    if(data["country"]=="USA"){
    var housingCost = document.getElementById("housingCost")
    housingCost.innerHTML = "$"+data["housingCost"]+"/week"
    }else{
        var housingCost = document.getElementById("housingCost")
    housingCost.innerHTML = "€"+data["housingCost"]+"/week"
    }
    var program = document.getElementById('program');
    program.innerHTML = data["program"];



    var programCost = document.getElementById("programCost")
    programCost.innerHTML = "Program Cost: €"+data["programCost"]

    var applyOn  = document.getElementById("applyon")
    applyOn.innerHTML = "Applied on: "+data["applied"]

    var firstMediaQuery = window.matchMedia('(min-width: 768px');
    const mediaQuery = window.matchMedia('(max-width: 767px)');
    var right_jobs_main_div = document.querySelector('.right-jobs-main-div');
    var jobs_left = document.querySelector('.jobs-left');
    var jobs_buttons = document.querySelector('.jobs-buttons');

    if (mediaQuery.matches) {
            right_jobs_main_div.style.display = "flex";
            jobs_left.style.display = "none";
            jobs_buttons.style.display = "none";
            if(id==0){
            var select = document.getElementById('select'+id)
            select.style.backgroundColor = "white";
            }
    }
    ;
}


    var nul = "";

    var firstMediaQuery = window.matchMedia('(min-width: 768px');
    const mediaQuery = window.matchMedia('(max-width: 767px)');
    var right_jobs_main_div = document.querySelector('.right-jobs-main-div');
    var jobs_left = document.querySelector('.jobs-left');
    var jobs_buttons = document.querySelector('.jobs-buttons');
    console.log("asd")
    if (mediaQuery.matches) {
            right_jobs_main_div.style.display = "none";
            jobs_left.style.display = "flex";
            jobs_buttons.style.display = "flex";

            var select = document.getElementById('select'+id)
            select.style.backgroundColor = "white";

    };


    window.onload = getNumber(nul);

