fetch("/api/shop")
.then(res => res.json())
.then(data => {

  const paid = document.getElementById("paid");
  const free = document.getElementById("free");

  window.MAIN = data.links.main;
  window.LIKE = data.links.like_group;
  window.JWT = data.links.jwt_bot;

  data.paid_products.forEach(p => {
    const b = document.createElement("button");
    b.innerText = `${p.name} — ${p.price}`;
    b.onclick = openMain;
    paid.appendChild(b);
  });

  data.free_products.forEach(p => {
    const b = document.createElement("button");
    b.innerText = p.name;

    if (p.type === "like_group") b.onclick = () => window.open(LIKE);
    else if (p.type === "jwt_bot") b.onclick = () => window.open(JWT);
    else b.onclick = openMain;

    free.appendChild(b);
  });
});

function openMain() {
  window.open(window.MAIN);
}