$(".ckbCheckAll").click(function () {
    $(".checkbox").prop('checked', $(this).prop('checked'));
});

$(".checkbox").change(function(){
    if (!$(this).prop("checked")){
        $(".ckbCheckAll").prop("checked",false);
    }
});



function doSearch()
		{
			var tableReg = document.getElementById('all_table');
			var searchText = document.getElementById('searchTerm').value.toLowerCase();
			var cellsOfRow="";
			var found=false;
			var compareWith="";

			for (var i = 1; i < tableReg.rows.length; i++)
			{
				cellsOfRow = tableReg.rows[i].getElementsByTagName('td');
				found = false;
				for (var j = 0; j < cellsOfRow.length && !found; j++)
				{
					compareWith = cellsOfRow[j].innerHTML.toLowerCase();
					if (searchText.length == 0 || (compareWith.indexOf(searchText) > -1))
					{
						found = true;
					}
				}
				if(found)
				{
					tableReg.rows[i].style.display = '';
				} else {
					tableReg.rows[i].style.display = 'none';
				}
			}
		}

function doColSearch(colname){
    var index_row = colname.substr(-1);
    var tableReg = document.getElementById('all_table');
    var searchText = document.getElementById(colname).value.toLowerCase();
    var cellsOfRow="";
    var found=false;
    var compareWith="";

    for (var i = 1; i < tableReg.rows.length; i++){
      cellsOfRow = tableReg.rows[i].getElementsByTagName('td');
      found = false;
      compareWith = cellsOfRow[index_row].innerHTML.toLowerCase();
      if (searchText.length == 0 || (compareWith.indexOf(searchText) > -1)){
        found = true;
      }
      if(found){
        tableReg.rows[i].style.display = '';
      } else {
        tableReg.rows[i].style.display = 'none';
      }
      tableReg.rows[tableReg.rows.length-1].style.display = '';
    }
}


$(".accordion-tit").click(function(){

   var contains=$(this).next(".accordion-content");

   if(contains.css("display")=="none"){ //open
      contains.slideDown(250);
      $(this).addClass("open");
   }
   else{
      contains.slideUp(250);
      $(this).removeClass("open");
  }

});
