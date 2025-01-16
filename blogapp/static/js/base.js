// navbar-nav li:last-child 클릭시 logoutForm
document
  .querySelector(".navbar-nav li:last-child")
  .addEventListener("click", () => {
    document.querySelector("#logoutForm").submit();
  });
