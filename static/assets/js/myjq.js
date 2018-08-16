$(document).ready(function() {

    $(".hide-desktop").click(function() {
        $(this).css("display", "none");
        $(".show-desktop").css("display", "inline-block");
        $("#lab-container").css("width", "92.8%");
        $("#display").css("display", "none");
    });

    $(".show-desktop").click(function() {
        $(this).css("display", "none");
        $(".hide-desktop").css("display", "inline-block");
        $("#lab-container").css("width", "30%");
        $("#display").css("display", "inline-block");
    });


    $(".hide-tools").click(function() {
        $(this).css("display", "none");
        $(".show-tools").css("display", "inline-block");
        $("#tools").css("right", "-140px");
    });

    $(".show-tools").click(function() {
        $(this).css("display", "none");
        $(".hide-tools").css("display", "inline-block");
        $("#tools").css("right", "0px");
    });


    $(".close").click(function()
    {
        $(".labdoc-msg").css("display", "none");
    });

    //$("#btn_css").click(function () {
    //    $("h1,h2,p").addClass("blue");
    //    $("div").addClass("important");
    //});

    //$("#btn_attr").click(function () {

        //  $("#btn_css").attr("height","100px");
        //   $("#btn_css").attr("width","200px");

        /* $("#btn_css").attr({
             "height":"20px",
             "width":"10px"
         });*/

    //    $("#btn_css").css("height", "100px");
    //    $("#btn_css").css("width", "200px");
    //});


});