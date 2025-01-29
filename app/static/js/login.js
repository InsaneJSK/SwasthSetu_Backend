document.addEventListener("DOMContentLoaded", function () {
  const formTitle = document.getElementById("form-title");
  const extraFields = document.getElementById("extra-fields");
  const loginForm = document.getElementById("login-form");
  const toggleText = document.getElementById("toggle-text"); // Updated to get the toggle text container

  let isSignUp = false;

  function toggleForm() {
    isSignUp = !isSignUp;

    if (isSignUp) {
      formTitle.textContent = "Sign Up";
      extraFields.classList.remove("hidden");
      toggleText.innerHTML = `Have an account? <a href="#" id="toggle-link">Sign In</a>`;
    } else {
      formTitle.textContent = "Sign In";
      extraFields.classList.add("hidden");
      toggleText.innerHTML = `Don't have an account? <a href="#" id="toggle-link">Sign Up</a>`;
    }

    document
      .getElementById("toggle-link")
      .addEventListener("click", function (event) {
        event.preventDefault();
        toggleForm();
      });
  }

  document
    .getElementById("toggle-link")
    .addEventListener("click", function (event) {
      event.preventDefault();
      toggleForm();
    });

  loginForm.addEventListener("submit", function (event) {
    event.preventDefault();
    alert(isSignUp ? "Sign Up Successful!" : "Sign In Successful!");
  });
});
