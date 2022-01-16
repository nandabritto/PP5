var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var boxId = this.dataset.box
        var action = this.dataset.action
        console.log('boxId:', boxId, 'action:', action)

        console.log('USER:', user)
        if (user == 'AnonymousUser') {
            console.log('Not logged in')
        } else {
            updateUserOder(boxId, action)
        }
    })
}


function updateUserOrder(boxId, action) {
    console.log('User is logged in, sending data...')

    const request = new Request(
        '/cart/update_cart/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            mode: 'same-origin' // Do not send CSRF token to another domain.
        },
        JSON.stringify({
            'boxId': boxId,
            'action': action
        })
    );

    fetch(request).then(function (response) {
        return response.json;
    });
    fetch(request).then(function (data) {
        console.log('data', data);
    });

}