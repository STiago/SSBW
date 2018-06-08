$('#likes_up').click(function(){
  var catid;
  catid = $(this).attr("data-catid");
  window.print(catid);
  $.get('/recipes_dashboard/like_category/', {category_id: catid}, function(data){
             $('#output').html(data);
             $('#likes_up').hide();
  });
});
