document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("forgotPasswordForm");
    const emailInput = document.getElementById("email");
    const message = document.getElementById("message");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const email = emailInput.value;

        if (isValidEmail(email)) {
            // Simulating a password reset link sent to the email address
            message.textContent = "Password reset link sent to your email.";
            message.style.color = "green";
            emailInput.value = "";
        } else {
            message.textContent = "Please enter a valid email address.";
            message.style.color = "#d9534f";
        }

        // Apply the fade-in animation to the message
        message.classList.remove("hidden");

        // After a few seconds, apply the fade-out animation to the message
        setTimeout(function() {
            message.style.animation = "fadeOut 0.3s forwards";
        }, 3000); // Delay for 3 seconds
    });

    function isValidEmail(email) {
        // You can add email validation logic here
        // This is a simple example; consider using a regular expression for a more robust check
        return email.includes("@") && email.includes(".");
    }
});
