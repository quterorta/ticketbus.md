// window.onload = function () {
//     document.body.classList.add('loaded_hiding');
//     window.setTimeout(function () {
//         document.body.classList.add('loaded');
//         document.body.classList.remove('loaded_hiding');
//     }, 1000);
// }

 $(document).ready(function(){
    var preloader = document.getElementById('preloader')
    preloader.style.display = 'none';

    $("#order_ticket_form").submit(function(e) {
        var form = this;
        e.preventDefault();
        preloader.style.display = 'block';
        document.body.style.overflow = 'hidden';
        setTimeout(function () {
            form.submit();
        }, 4500);
    });
});
