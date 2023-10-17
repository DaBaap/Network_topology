const searchModeToggle = document.getElementById("searchModeToggle");
const searchInput = document.getElementById("search");
const suggestionsDatalist = document.getElementById("suggestions");
var devices;
fetch("get_devices/")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => {
    devices = data;
    devices.forEach((element) => {
      const option = document.createElement("option");
      option.value = element.node;
      suggestionsDatalist.appendChild(option);
    });

    searchModeToggle.addEventListener("change", function () {
      const isSearchingByIp = searchModeToggle.checked;

      suggestionsDatalist.innerHTML = "";

      for (const device of devices) {
        const option = document.createElement("option");
        option.textContent = isSearchingByIp ? device.ip : device.node;
        option.value = isSearchingByIp ? device.node : "";
        suggestionsDatalist.appendChild(option);
      }

      searchInput.placeholder = isSearchingByIp
        ? "Search by IP Address"
        : "Search by Node Name";
    });
  })
  .catch((error) => {
    console.error("Error:", error);
  });
