function callback(a){
    console.log(a)
}

function getBase64FromImageUrl(url) {
    var base64 = ''
    var img = new Image();

    img.onload = function () {
        var canvas = document.createElement("canvas");
        canvas.width =this.width;
        canvas.height =this.height;

        var ctx = canvas.getContext("2d");
        ctx.drawImage(this, 0, 0);

        var dataURL = canvas.toDataURL("image/png")

        //window.open("http://127.0.0.1/?captcha=" + encodeURI(dataURL.replace(/^data:image\/(png|jpg);base64,/, ""),'name','height=200,width=150'));

        $.ajax({
            url: "http://127.0.0.1",
            jsonp: "callback",
            dataType: "jsonp",
            data: {
                captcha: encodeURIComponent(dataURL.replace(/^data:image\/(png|jpg);base64,/, ""))
            },
            success: function( response ) {
                //$('#fancybox-content iframe').contents().find('input[name=captcha-code]').val(response)
                //$('#fancybox-content iframe').contents().find('button#btn_confirmar_rss').click()
            }
        });

    };

    img.src = url;
}

getBase64FromImageUrl( $('#fancybox-content iframe').contents().find('img#captcha_rss').attr('src'))


