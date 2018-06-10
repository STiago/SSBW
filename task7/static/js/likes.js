$('.likes_up').click(function(){
    var catid = $(this).attr("data-catid-up");
    var button = $(this);
    var like_url = "/recipes_dashboard/like_up/" + catid +"/";

    $.post(like_url, {}, function(responseData){
       var count = button.parent().find('.likes_up_count');
       $(count).html(responseData);
       button.hide();
   });
});

$('.likes_down').click(function(){
    var catid = $(this).attr("data-catid-down");
    var button = $(this);
    var like_url = "/recipes_dashboard/like_down/" + catid +"/";

    $.post(like_url, {}, function(responseData){
       var count = button.parent().find('.likes_down_count');
       $(count).html(responseData);
       button.hide();
   });
});
