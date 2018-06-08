$('#likes_up').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    nameid = $(this).attr("data-name");
    alert( "+1 Like to : " + nameid);
    $.post("like_category", {category_id: catid}, function(data){
       $('#output').html(data);
       $('#likes_up').hide();
       alert( "Done.");
   });
});
