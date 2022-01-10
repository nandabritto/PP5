function getvalues() {
  var selected = new Array();
  var chkbox = document.getElementById('id_selected_product')
  console.log(selected)
  
  var selchk = chkbox.getElementsByTagName('input');
  for (var i = 0; i < selchk.length; i++) {
    if (selchk[i].checked) {
      selected.push(selchk[i].value);
    }
  }
  if (selected.length > 0) {
    document.getElementById("displayvalues").innerHtml = selected;
  }
  
};

