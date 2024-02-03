document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("resetPasswordForm");
    const newPasswordInput = document.getElementById("newPassword");
    const confirmPasswordInput = document.getElementById("confirmPassword");
    const message = document.getElementById("message");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const newPassword = newPasswordInput.value;
        const confirmPassword = confirmPasswordInput.value;

        if (newPassword !== confirmPassword) {
            message.textContent = "Passwords do not match. Please try again.";
            message.style.color = "#d9534f";
        } else {
            // Passwords match - you can implement your password update logic here
            message.textContent = "Password has been reset successfully.";
            message.style.color = "green";
            newPasswordInput.value = "";
            confirmPasswordInput.value = "";
        }

        // Apply the fade-in animation to the message
        message.classList.remove("hidden");

        // After a few seconds, apply the fade-out animation to the message
        setTimeout(function() {
            message.style.animation = "fadeOut 0.3s forwards";
        }, 3000); // Delay for 3 seconds
    });
});
