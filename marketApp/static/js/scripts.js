$(document).ready(function() {
    $('.showShopForm').click(function(){
        $('.shopForm').animate( {
            width: 'toggle'
        })
    }),
    $('.showCatForm').click(function(){
        $('.catForm').animate( {
            width: 'toggle'
        })
    }),
    $('.showProdForm').click(function(){
        $('.prodForm').animate({
            width: 'toggle'
        })
    })
})