$(document).ready(function()
{
    console.log( "ready!" );
    $("#optAvc").hide();


    $('#chkBox').click(function() 
    {
	    var $this = $(this);
	    // $this will contain a reference to the checkbox   
	    if ($this.is(':checked')) {
	       console.log( "visible!" );
		   $("#optAvc").show();
	    } else {
	       console.log( "pas visible!" );
		   $("#optAvc").hide();
	    }
	});
});
