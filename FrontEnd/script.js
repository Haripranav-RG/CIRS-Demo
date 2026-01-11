document.getElementById("registerForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const fullName = document.getElementById("full_name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm_password").value;

    // ✅ Password match validation
    if (password !== confirmPassword) {
        alert("Passwords do not match");
        return;
    }

    // Payload matching backend schema
    const payload = {
        full_name: fullName,
        email: email,
        phone: phone || null,
        password: password
    };

    try {                          

        const response = await fetch("http://127.0.0.1:8000/users/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (!response.ok) {
            alert(data.detail || "Registration failed");
            return;
        }

        alert("Account created successfully!");
        console.log("Success:", data);

        // Optional redirect later
        // window.location.href = "/login.html";

    } catch (error) {
        console.error("Error:", error);
        alert("Unable to connect to server");
    }
});
