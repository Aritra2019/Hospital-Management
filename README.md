<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hospital Management System</title>
</head>
<body>

<h1>Hospital Management System</h1>

<p>This is a basic Hospital Management System built using Python and Tkinter for the GUI. It allows users to manage patient information and prescriptions.</p>

<h2>How to Use</h2>
<p>Clone the repository and run the Python script:</p>
<pre><code>python Hospital_Management.py</code></pre>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li>Tkinter</li>
    <li>mysql-connector-python</li>
</ul>

<h2>Functionality</h2>
<p>The following buttons are available in the GUI and their respective functions:</p>
<ul>
    <li><strong>Prescription:</strong> Generates a prescription based on the input data and displays it in the text area on the right side of the interface. This is done by the <code>iprescription</code> function.</li>
    <li><strong>Prescription Data:</strong> Inserts the entered patient and prescription data into the database. This is handled by the <code>iprescriptionData</code> function.</li>
    <li><strong>Update:</strong> Updates the selected record in the database with the new data entered in the form fields. This is done by the <code>update_data</code> function.</li>
    <li><strong>Delete:</strong> Deletes the selected patient's record from the database based on the reference number. This functionality is provided by the <code>iDelete</code> function.</li>
    <li><strong>Clear:</strong> Clears all the input fields in the form, allowing the user to enter new data without interference from previous entries. This functionality needs to be implemented.</li>
    <li><strong>Exit:</strong> Closes the application. This functionality needs to be implemented.</li>
</ul>

<h2>Future Work</h2>
<p>Planned enhancements for the Hospital Management System:</p>
<ul>
    <li>Functionality for each button</li>
    <li>User authentication</li>
    <li>Enhanced data validation and error handling</li>
    <li>Exporting data to CSV or PDF formats</li>
    <!-- Add more planned enhancements -->
</ul>

<h2>Contributing</h2>
<p>Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
