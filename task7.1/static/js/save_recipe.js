$('#save_recipe').click(function(){
  var catid;
  catid = $(this).attr("data-catid");
  window.print(catid);
});
