// Function to check password length
function check() {
    let pass = document.getElementById("password").value;
    if (pass.length < 6 || pass.length > 16) {
        alert("Enter a valid password (6-16 characters).");
        return false;
    }
    return true;
 }
 
 // Function to handle the registration
 function register() {
     // First, check the password length
     if (!check()) {
         return;  // If password is invalid, stop the registration
     }
 
     let firstName = document.getElementById("fname").value; // Get name
     let email = document.getElementById("email").value;    // Get email
     let password = document.getElementById("password").value; // Get password
     let confirmPassword = document.getElementById("confirm-password").value; // Get confirm password
 
     // Check if name, email, password, and confirm password are entered
     if (!firstName || !email || !password || !confirmPassword) {
         alert("Please fill in all fields.");
         return;  // If any field is missing, stop the registration
     }
 
     // Check if password and confirm password match
     if (password !== confirmPassword) {
         alert("Passwords do not match.");
         return;  // If passwords don't match, stop the registration
     }
 
     // You can now submit the data to the backend (using Fetch or Ajax)
     // Example POST request using Fetch to send data to Flask backend
     let data = {
         first_name: firstName,
         email: email,
         password: password
     };
 
     // Send the data to the Flask backend
     fetch('/register', {
         method: 'POST',
         headers: {
             'Content-Type': 'application/json',
         },
         body: JSON.stringify(data)
     })
     .then(response => response.json())
     .then(data => {
         if (data.success) {
             alert("Registration successful!");
             // Redirect to login page or landing page after successful registration
             window.location.href = "/login";  // Redirect to login page
         } else {
             alert("Error: " + data.message);
         }
     })
     .catch(error => {
         console.error('Error:', error);
         alert("Failed to register. Please try again later.");
     });
 
     // Clear the form fields after submission
     document.getElementById("fname").value = "";
     document.getElementById("email").value = "";
     document.getElementById("password").value = "";
     document.getElementById("confirm-password").value = "";
 }// Function to check password length
function check() {
    let pass = document.getElementById("password").value;
    if (pass.length < 6 || pass.length > 16) {
        alert("Enter a valid password (6-16 characters).");
        return false;
    }
    return true;
}

function register() {
    // First, check the password length
    if (!check()) {
        return;  // If password is invalid, stop the registration
    }

    // Collect form data
    let firstName = document.getElementById("fname").value;  // Get first name
    let email = document.getElementById("email").value;      // Get email
    let password = document.getElementById("password").value; // Get password
    let confirmPassword = document.getElementById("confirm-password").value; // Get confirm password

    // Validate fields
    if (!firstName || !email || !password || !confirmPassword) {
        alert("Please fill in all fields.");
        return;
    }

    // Check if password and confirm password match
    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return;
    }

    // Create data object to send to the backend
    let data = {
        first_name: firstName,
        email: email,
        password: password
    };

    // Send data to the backend via fetch
    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Registration successful!");
            // Optionally, you can redirect the user to the login page
            // window.location.href = "/login"; 
        } else {
            alert("Error: " + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Failed to register. Please try again later.");
    });

    // Clear the form fields after submission
    document.getElementById("fname").value = "";
    document.getElementById("email").value = "";
    document.getElementById("password").value = "";
    document.getElementById("confirm-password").value = "";
}

 