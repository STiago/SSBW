$('.likes_up').click(function(){
    var catid = $(this).attr("data-catid");
    var button = $(this);
    var like_url = "/recipes_dashboard/like_category/" + catid;

    /*$.put(like_url, {}, function(responseData){
       var count = button.parent().find('.likes_up_count');
       $(count).html(responseData);
       button.hide();
   });*/
   
    $.get("/recipes_dashboard/like_category/", {category_id: catid}, function(responseData){
       var count = button.parent().find('.likes_up_count');
       $(count).html(responseData);
       button.hide();
   });
});
