$("document").ready(function(){
    $('form').on('submit', function(event) {
        event.preventDefault();
        $.ajax({
            data: {
                rijst : $("#rijst").val(),
                mais : $('#mais').val(),
                linzen : $('#linzen').val()
            },
            type: 'POST',
            url: '/process'
        })
        if ($("#rijst").val()<0 || $("#linzen").val()<0 || $("#mais").val()<0) {
        $("#warning").text("Please enter only positive integers.");
        }
        else if ($("#rijst").val()>100 || $("#linzen").val()>100 || $("#mais").val()>100) {
            $("#warning").text("You can't order more than 100 grams of one item.");
        }
        else if ($("#rijst").val()==0 && $("#linzen").val()==0 && $("#mais").val()==0) {
            $("#warning").text("You put nothing to order!");
        }
        else {
            $("#warning").text("Order succesful!")
        }
        $("#mais").val("0");
        $("#linzen").val("0");
        $("#rijst").val("0")
    });

});
