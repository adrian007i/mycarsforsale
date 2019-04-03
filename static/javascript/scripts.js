$(document).ready(function(){
    $("#cars_profile div").mouseenter(function(){
        $(this).css("opacity",".7")
    });

    $("#cars_profile div").mouseleave(function(){
        $(this).css("opacity","1")
    });

});
