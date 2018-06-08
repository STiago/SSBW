$('#save_recipe').click(function(){
  var catid;
  catid = $(this).attr("data-catid");
  window.print(catid);
  $.get('/recipes_dashboard/save_recipe/', {category_id: catid}, function(data){
             $('#save_recipe').hide();
  });
});
