$('#delete_image').click(function(){
    var catid;
    catid = $(this).attr("data-del");
    alert( "Do you want to delete: " + catid + "?");
});
