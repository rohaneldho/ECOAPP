const urlParams = new URLSearchParams(window.location.search);
const name = urlParams.get('username');
var passw;

if (name) {
    document.getElementById('outputName').textContent = name;
}
var tc,pc,nop;
const receivedData = JSON.parse(localStorage.getItem("result"));
console.log(receivedData);
if (receivedData) {
  passw=receivedData["password"];
    tc=receivedData["TC"];
    document.getElementById('totalTrees').innerHTML = tc;
    pc=receivedData["PC"];
    document.getElementById('totalPlastic').innerHTML = pc;
    nop=receivedData["NOP"];
    document.getElementById('totalPoints').innerHTML = nop;

} else {
    console.log('No data received.');
}
function tf(){
  tc+=1;
  nop+=20;
  document.getElementById('totalTrees').innerHTML = tc;
  document.getElementById('totalPoints').innerHTML = nop;

}
function pf(){
  pc+=1;
  nop+=5;
  document.getElementById('totalPlastic').innerHTML = pc;
  document.getElementById('totalPoints').innerHTML = nop;
}
function save(){
  const data ={name,passw,tc,pc,nop};
  console.log(data);
  $.ajax({
    type: "POST",
    url: "http://127.0.0.1:5000/saving_data",
    contentType: "application/json",
    data: JSON.stringify(data),
    success: function(result) {
      sharedData=JSON.stringify(result);

      console.log(sharedData);
    },
  });
}





