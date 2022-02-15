var hideable_shipping_form = $('.hideable_shipping_form');
var hideable_billing_form = $('.hideable_billing_form');
var hideable_user_default_billing = $('.hideable_user_default_billing');

var use_default_shipping = document.querySelector("input[name=use_default_shipping]");
var use_default_billing = document.querySelector("input[name=use_default_billing]");
var same_billing_address = document.querySelector("input[name=same_billing_address]");

if(use_default_shipping){
use_default_shipping.addEventListener('change', function() {
  if (this.checked) {
    hideable_shipping_form.hide();
  } else {
    hideable_shipping_form.show();
  }
})}

if(use_default_billing){
use_default_billing.addEventListener('change', function() {
  if (this.checked) {
    hideable_billing_form.hide();
  } else {
    hideable_billing_form.show();
  }
})}

same_billing_address.addEventListener('change', function() {
    if (this.checked) {
      hideable_billing_form.hide();
      hideable_user_default_billing.hide();
    } else {
      hideable_billing_form.show();
      hideable_user_default_billing.hide();
    }
  })
  