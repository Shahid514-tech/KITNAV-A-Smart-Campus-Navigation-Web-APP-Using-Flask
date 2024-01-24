function submitForm() {
    // Get the selected options
    var source = document.getElementById('Source').value;
    var destination = document.getElementById('Destination').value;

    // Check if source and destination are the same
    if (source === destination) {
        return;  // Don't proceed further if source and destination are the same
    }
    // Create an object with the data
    var data = {
        source: source,
        destination: destination
    };

    // Create a new XMLHttpRequest object
    var xhr = new XMLHttpRequest();

    // Configure it: POST-request for the /submit_options endpoint
    xhr.open('POST', '/submit_options', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    // Convert the data object to a JSON string
    var jsonData = JSON.stringify(data);

    // Send the request with the JSON data
    xhr.send(jsonData);

    // Optional: Handle the response from the server
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log(xhr.responseText);
        }
    };
}