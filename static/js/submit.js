document.addEventListener('DOMContentLoaded', function () {
    // Wait for the DOM to be fully loaded

    // Get the form element
    var form = document.getElementById('optionForm');

    // Variable to store the OneDrive link
    var oneDriveLink = '';

    // Add a submit event listener to the form
    form.addEventListener('submit', function (event) {
      // Prevent the default form submission
      event.preventDefault();

      // Get the selected values from the Source and Destination dropdowns
      var sourceValue = document.getElementById('Source').value;
      var destinationValue = document.getElementById('Destination').value;

      // Show an alert with the submitted options
      alert("Submitted Source: " + sourceValue + "\nSubmitted Destination: " + destinationValue);

      // Set the default OneDrive link
      var newOneDriveLink = '';

      // Use an if-else loop to conditionally set the OneDrive link
      if (sourceValue == destinationValue) {
        alert("ERROR: Submitted Source and Destination Cannot be Same.");
        // Don't proceed further if source and destination are the same
        return;
      }else if (sourceValue === 'CSAMCR-02' && destinationValue === 'CSAMCR-01') {
        newOneDriveLink = 'https://onedrive.live.com/embed?resid=6E1F01B08891AA1%21349&authkey=!ACDFLMyoYd3R4RE&em=2';
      }else if (sourceValue === 'CSDSCR-02' && destinationValue === 'CSAMCR-04') {
        newOneDriveLink = 'https://onedrive.live.com/embed?resid=6E1F01B08891AA1%21351&authkey=!AKzobjW2zb5vijo&em=2';
      }else if (sourceValue === 'CSDSCR-02' && destinationValue === 'CSDSCR-03') {
        newOneDriveLink = 'https://onedrive.live.com/embed?resid=6E1F01B08891AA1%21350&authkey=!ANl4CRegQN31Qi4&em=2';
      }else if (sourceValue === 'CSDSCR-02' && destinationValue === 'LAB-02') {
        newOneDriveLink = 'https://onedrive.live.com/embed?resid=6E1F01B08891AA1%21352&authkey=!AOmrg40qWjArDug&em=2';
      }else if (sourceValue === 'CSDSCR-02' && destinationValue === 'LAB-03') {
        newOneDriveLink = 'https://onedrive.live.com/embed?resid=6E1F01B08891AA1%21354&authkey=!AJU35olxfWC_eck&em=2';
      }else if (sourceValue === 'CSDSCR-02' && destinationValue === 'LAB-01') {
        newOneDriveLink = 'https://onedrive.live.com/embed?resid=6E1F01B08891AA1%21353&authkey=!AMzjTrZHBnlVAV0&em=2';
      }else if (sourceValue === 'CSDSCR-02' && destinationValue === 'CSDSCR-01') {
        newOneDriveLink = 'https://onedrive.live.com/embed?resid=6E1F01B08891AA1%21355&authkey=!AIwW33_dh9cgI90&em=2';
      }

      // Update the iframe source with the new OneDrive link
      document.getElementById('viewer').src = newOneDriveLink;

      // Show the viewer container
      document.getElementById('viewer-container').style.display = 'block';
    });
  });
