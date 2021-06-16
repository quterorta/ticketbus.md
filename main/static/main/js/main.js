function swapValues(){
    var tmp = document.getElementById("order_ticket_form_city_start_trip").value;
    document.getElementById("order_ticket_form_city_start_trip").value = document.getElementById("order_ticket_form_city_end_trip").value;
    document.getElementById("order_ticket_form_city_end_trip").value = tmp;
}

$("#order_ticket_form_date_trip").on('click', function () {
    $(this).siblings('[type="date"]').removeClass('hidden').focus().click();
});

function scrollToSearchResult() {

    var input_date_field = document.getElementById("order_ticket_form_date_trip");

    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
        input_date_field.setAttribute('readonly', 'readonly');
    } else {
        input_date_field.removeAttribute('readonly');
    }

    var search_result = document.getElementById("search_result");
    var non_search_result = document.getElementById("non_search_result");
    if (!search_result) {
        non_search_result.scrollIntoView({block: "center", behavior: "smooth"});
    } else {
        search_result.scrollIntoView({block: "start", behavior: "smooth"});
    }
}