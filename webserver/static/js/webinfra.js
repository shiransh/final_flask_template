function display_stream() {
    if (!!window.EventSource) {
        var source = new EventSource('/example_stream/');
        source.onmessage = function(e) {
            $("#data").text(e.data);
            document.getElementById("random_int").innerHTML = e.data;
        }
    }
}