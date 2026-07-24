// Engineering Calculator JavaScript

document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");
    const operation = document.querySelector("select[name='operation']");
    const num1 = document.querySelector("input[name='num1']");
    const num2 = document.querySelector("input[name='num2']");

    // Hide second number for square root
    function toggleSecondInput() {
        if (operation.value === "sqrt") {
            num2.parentElement.style.display = "none";
            num2.removeAttribute("required");
            num2.value = "";
        } else {
            num2.parentElement.style.display = "block";
            num2.setAttribute("required", "required");
        }
    }

    toggleSecondInput();

    operation.addEventListener("change", toggleSecondInput);

    // Input validation
    form.addEventListener("submit", function (e) {

        if (num1.value.trim() === "") {
            alert("Please enter the first number.");
            num1.focus();
            e.preventDefault();
            return;
        }

        if (operation.value !== "sqrt" && num2.value.trim() === "") {
            alert("Please enter the second number.");
            num2.focus();
            e.preventDefault();
            return;
        }

        if (operation.value === "divide" && Number(num2.value) === 0) {
            alert("Division by zero is not allowed.");
            e.preventDefault();
            return;
        }

        if (operation.value === "log") {

            if (Number(num1.value) <= 0 || Number(num2.value) <= 0 || Number(num2.value) === 1) {
                alert("Logarithm requires:\n\n• Number > 0\n• Base > 0\n• Base ≠ 1");
                e.preventDefault();
                return;
            }
        }

        // Loading animation
        const button = document.querySelector("button");

        button.innerHTML = `
            <span class="spinner-border spinner-border-sm"></span>
            Calculating...
        `;

        button.disabled = true;
    });

});