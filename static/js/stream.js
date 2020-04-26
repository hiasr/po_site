$("document").ready(function(){
    $('form').on('submit', function(event) {
        event.preventDefault();
         var checkBox1 = document.getElementById("switch1");
         var checkBox2 = document.getElementById("switch2");
        $.ajax({
            data: {
                motor : checkBox1.checked,
                angle : $('#angle').val(),
                speed : $('#speed').val(),
                direction : checkBox2.checked
            },
            type: 'POST',
            url: '/stream'
        })

    });

});
