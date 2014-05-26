/**
 * Created by wang on 5/23/14.
 */


django.jQuery(function(){
    var $ = django.jQuery;

    django.jQuery('.bucketbutton').parent().next().hide();
    django.jQuery('.bucketbutton').click(function(){
        var text = $(this).text();
        if (text == "show") {
            $(this).parent().next().show();
            $(this).text('hidden');
        } else {
            $(this).parent().next().hide();
            $(this).text('show');
        }
        return false;
    });
});
