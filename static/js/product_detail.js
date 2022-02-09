function getvalues() {
  var selected = new Array();
  var chkbox = document.querySelectorAll("[id*='id_selected_product_']");
  console.log(selected);
  for (var i = 0; i < chkbox.length; i++) {
    if (chkbox[i].checked) {
      selected.push(chkbox[i].value);
    }
  }
  if (selected.length > 0) {
    document.getElementById("displayvalues").innerHTML = selected;
    return selected;
  }
}


// produt review save


