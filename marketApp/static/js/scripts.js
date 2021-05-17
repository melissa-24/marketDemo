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
    }),
    $('.showUpdateProdFrom').click(function(){
        $('.updateProdForm').animate({
            width: 'toggle'
        })
    }),
    $('.shopAddShopForm').click(function(){
        $('.addShopForm').animate({
            width: 'toggle'
        })
    }),
    $('.showAddCatForm').click(function(){
        $('.addCatForm').animate({
            width: 'toggle'
        })
    }),
    $('.showAllProducts').click(function(){
        $('.allProducts').animate({
            width: 'toggle'
        })
    }),
    $('.showAllShops').click(function(){
        $('.allShops').animate({
            width: 'toggle'
        })
    }),
    $('.showAllCats').click(function(){
        $('.allCats').animate({
            width: 'toggle'
        })
    })
})