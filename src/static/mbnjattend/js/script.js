function enableBrowseFunction(){
  var e = document.getElementById("method");
  var strUser = e.options[e.selectedIndex].text;

  if (strUser == "Config Memo") {
      $('#browseBtn').prop('disabled', false);
  }
  else {
      $('#browseBtn').prop('disabled', true);
  }
}
function selectSat(){
  var e = $('#sc').children("option:selected").text();
  //var httpstr = "/cmauto/?satname=" + e;
  var httpstr = "/mbnjattend/" + e;
  window.location.href = httpstr;
}
function getSatName(){
  var e = window.location.href;
  var satname = e.split("/")[4];
  var pk = e.split("/")[5];
  var httpstr = "/cmauto/" + satname + "/" + pk + "/newchange";
  window.location.href = httpstr;
}
function genOTO(){
  var e = window.location.href;
  var satname = e.split("/")[4];
  var pk = e.split("/")[5];
  var httpstr = "/cmauto/" + satname + "/" + pk + "/genoto";
  window.location.href = httpstr;
}
