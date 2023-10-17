
const allNodesButtonText = document.querySelector("#all_nodes_button span h4");
const isoNodesButtonText = document.querySelector("#iso_nodes_button span h6");
const node_button = document.getElementById("get_node_button");
const iso_node_div = document.getElementById("iso_nodes_div");
const all_node_div = document.getElementById("all_nodes_div");


document.getElementById('iso_nodes_button').addEventListener("click", () => {
    console.log(iso_node_div)
  toggleButtonText();
});

function toggleButtonText() {
  const tempText = allNodesButtonText.textContent;
  allNodesButtonText.textContent = isoNodesButtonText.textContent;

  isoNodesButtonText.textContent = tempText;

  if (iso_node_div.style.display === "none") {
    iso_node_div.style.display = "block";
    all_node_div.style.display = "none";
  } else {
    iso_node_div.style.display = "none";
    all_node_div.style.display = "block";
  }
}
