var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var box_id = this.dataset.box
        var action = this.dataset.action
        console.log('box_id:', box_id, 'action:', action)

        console.log('USER:', user)
        if (user == 'AnonymousUser') {
            console.log('Not logged in')
        } else {
            updateUserOrder(box_id, action)
        }
    })
}


function updateUserOrder(box_id, action, prod_selected_ids=getvalues()) {
    console.log('User is logged in, sending data...')

    var url = '/cart/update_cart/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
                'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'box_id': box_id, 'action':action, 'prod_selected_ids':prod_selected_ids})
    })

    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data',data)
        location.reload()
    })
}


















//     const request = new Request(
//         '/cart/update_cart/', {
//             method: 'POST',
//             headers: {
//                 'Content-Type':'application/json',
//                 'X-CSRFToken': csrftoken
//             },
            
//             body: JSON.stringify({
//                 'box_id': box_id,
//                 'action': action
//             })
//         },
        
//     );

//     fetch(request).then(function (response) {
//         return response.json();
//     });
//     fetch(request).then(function (data) {
//         console.log('data', data);
//     });

// }