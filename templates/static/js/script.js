const category = document.getElementById("category");
const product = document.getElementById("product");
const output = document.querySelector(".output");
const form = document.querySelector("form");

const orderFoodCategories = () => {
  const selectedType = category.value;
  const options = product.options;

  for (let i = 0; i < options.length; i++) {
    const option = options[i];

    if (option.classList.contains(`c${selectedType}`)) {
      option.style.display = "inherit";
    } else {
      option.style.display = "none";
    }
  }
};

orderFoodCategories(); // on load

category.addEventListener("change", () => {
  orderFoodCategories();
});

document.addEventListener("DOMContentLoaded", function () {
  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const selectedIndex = product.selectedIndex;
    const selectedOption = product.options[selectedIndex].className;
    const selectedType = category.value;

    if (selectedOption != `c${selectedType}`) {

      output.innerHTML = "Product-Category Incompatibility";
      
    } else {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "", true);

      xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
          if (xhr.status === 200) {
            var data = JSON.parse(xhr.responseText);
            if (data.success) {
              output.innerHTML = data.msg;
            } else {
              output.innerHTML = "Request Error";
            }
          }
        }
      };

      xhr.send(new URLSearchParams(new FormData(this)).toString());
    }
  });
});
