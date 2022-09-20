function ajaxFunction() {
    var ajaxRequest;

    try {
        ajaxRequest = new XMLHttpRequest();
    } catch (e) {
        
    try {
        ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {

    try {
        ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
    } catch (e) {

            alert("Your Browser broke!");
            return false;
            }
        }
    }
}

function validateUserId(){
    ajaxFunction();

    ajaxRequest.onreadystatechange = processRequest;


if (!target) target = document.getElementById('userid');
var url = 'validate?id=' + escape(target.value);

ajaxRequest.open('GET', url, true);
ajaxRequest.send(null);
}