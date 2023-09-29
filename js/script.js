const out = document.getElementById("sadness");
const btn = document.getElementById("btnsub");
let sharedData=null;

function sendDataToPython(data) {
  $.ajax({
    type: "POST",
    url: "http://127.0.0.1:5000/process_data",
    contentType: "application/json",
    data: JSON.stringify(data),
    success: function(result) {
      sharedData=JSON.stringify(result);
      console.log(sharedData);
      localStorage.setItem("result", sharedData);
    },
  });

}


function ding() {
  const name = document.getElementById("username").value;
  const passw = document.getElementById("passw").value;
  
  const data = { name, passw };

  sendDataToPython(data);
}

document.addEventListener('DOMContentLoaded', function() {
  btn.addEventListener('click', ding);
});
