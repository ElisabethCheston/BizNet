console.log('hello world')

const toFollowModalBody = document.getElementById('to-follow-modal')
const spinnerBox = document.getElementById('spinner-box')

console.log(toFollowModalBody)
console.log(spinnerBox)

$.ajaxt({
    type: 'GET',
    url: 'profileusers/profile_data',
    success: function (response) {
        console.log(response)
    },
    error: function(error) {
        console.log(error)
    }
})
