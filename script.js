async function login() {

    const password = document.getElementById("masterPassword").value;

    const response = await fetch("http://127.0.0.1:5000/login", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            password: password
        })
    });

    const data = await response.json();

    if (data.success) {

        window.location.href = "dashboard.html";

    } else {

        document.getElementById("error").innerText = "Wrong Password";
    }
}