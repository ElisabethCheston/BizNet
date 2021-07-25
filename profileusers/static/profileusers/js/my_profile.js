console.log('hello world')


const toFollowModalBody = document.getElementById('to-follow-modal')
const spinnerBox = document.getElementById('spinner-box')
const toFollowBtn = document.getElementById('to-follow-btn')
let toFollowLoad = false


console.log(toFollowModalBody)
console.log(spinnerBox)

toFollowBtn.addEventListener('click', () => {
    $.ajax({
        type: 'GET',
        url: '/profileusers/profile_data/',
        success: function(response){
            if(!toFollowLoad) {
                console.log(response);
                const pfData = response.pf_data;
                console.log(pfData);
                setTimeout(() => {
                    spinnerBox.classList.add('not-visible');
                    pfData.forEach(el=>{ 
                        toFollowModalBody.innerHTML += `
                        <div class="row mb-2 align-items-center">
                            <div class="col-2">
                                <img class="avatar" src="${el.avatar}" alt="${el.user}">

                            </div>
                            <div class="col-3">
                            <div class="text-muted">${el.user}</div>

                            </div>
                            <div class="col text-right">
                            <button class="btn btn-sm btn-success">Follow Me</button>                                

                            </div>
                        </div>
                    `;
                    });
                }, 2000);
            }
            toFollowLoad = true;
        },
        error: function(error) {
            console.log(error);
        }
    });
});

