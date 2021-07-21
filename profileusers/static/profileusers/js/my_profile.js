console.log('hello world')


const toFollowModalBody = document.getElementById('to-follow-modal')
const spinnerBox = document.getElementById('spinner-box')

console.log(toFollowModalBody)
console.log(spinnerBox)


$.ajax({
    type: 'GET',
    url: '/profileusers/profile_data/',
    success: function(response){
        console.log(response)
        const pfData = response.pf_data
        console.log(pfData)
        setTimeout(()=>{
            spinnerBox.classList.add('not-visible')
            pfData.forEach(el=>{
                toFollowModalBody.innerHTML += `
                <div>hellow <b> world </b></div>
                `
            })
        }, 2000)
    },
    error: function(error) {
        console.log(error)
    }
})
