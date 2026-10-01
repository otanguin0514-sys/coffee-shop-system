const API_BASE = '/api';
const cart = [];
let selectedRating = 0;

const money = new Intl.NumberFormat('en-US', {
  style: 'currency',
  currency: 'USD'
});

async function fetchJson(url, options = {}) {
  const response = await fetch(url, {
    headers: { 'Content-Type': 'application/json', ...(options.headers || {}) },
    ...options,
  });
  const data = await response.json();
  if (!response.ok) throw new Error(data.detail || 'Request failed');
  return data;
}

function formatMoney(value) {
  return money.format(Number(value || 0));
}

async function loadProducts() {
  try {
    const products = await fetchJson(`${API_BASE}/products/`);
    renderProducts(products);
  } catch (err) {
    console.error(err);
  }
}

function renderProducts(products) {
  const menuGrid = document.getElementById('menuGrid');
  menuGrid.innerHTML = products.map((p) => `
    <article class="menu-item">
      <div class="menu-top">
        <div>
          <h3>${p.name}</h3>
        </div>
        <span class="badge">Popular</span>
      </div>
      <p>${p.description || 'Crafted with care and high-quality ingredients.'}</p>
      <div class="meta-row">
        <span class="price">${formatMoney(p.price)}</span>
        <button class="add-button" data-id="${p.id}">+</button>
      </div>
    </article>
  `).join('');

  document.querySelectorAll('.add-button').forEach((button) => {
    button.addEventListener('click', () => addToCart(Number(button.dataset.id)));
  });
}

function addToCart(productId) {
  const existing = cart.find((item) => item.id === productId);
  if (existing) {
    existing.quantity += 1;
  } else {
    cart.push({ id: productId, quantity: 1 });
  }
  renderCart();
}

async function renderCart() {
  const cartItems = document.getElementById('cartItems');
  const subtotalEl = document.getElementById('subtotal');
  const serviceFeeEl = document.getElementById('serviceFee');
  const totalEl = document.getElementById('total');

  if (cart.length === 0) {
    cartItems.innerHTML = '<div class="empty-cart">Your cart is empty. Add a coffee to begin.</div>';
    subtotalEl.textContent = '$0.00';
    serviceFeeEl.textContent = '$0.00';
    totalEl.textContent = '$0.00';
    document.getElementById('cartCount').textContent = '0';
    return;
  }

  const productMap = new Map((await fetchJson(`${API_BASE}/products/`)).map((p) => [p.id, p]));
  const items = cart.map((entry) => {
    const product = productMap.get(entry.id);
    return { ...product, quantity: entry.quantity };
  });

  cartItems.innerHTML = items.map((item) => `
    <div class="cart-item">
      <div>
        <div class="cart-item-name">${item.name}</div>
        <div class="cart-item-meta">${formatMoney(item.price)} each</div>
      </div>
      <div class="qty-control">
        <button class="minus-btn" data-id="${item.id}">-</button>
        <span>${item.quantity}</span>
        <button class="plus-btn" data-id="${item.id}">+</button>
      </div>
    </div>
  `).join('');

  document.querySelectorAll('.minus-btn').forEach((button) => {
    button.addEventListener('click', () => updateCartQty(Number(button.dataset.id), -1));
  });
  document.querySelectorAll('.plus-btn').forEach((button) => {
    button.addEventListener('click', () => updateCartQty(Number(button.dataset.id), 1));
  });

  const subtotal = items.reduce((sum, item) => sum + Number(item.price) * item.quantity, 0);
  const serviceFee = subtotal * 0.08;
  const total = subtotal + serviceFee;

  subtotalEl.textContent = formatMoney(subtotal);
  serviceFeeEl.textContent = formatMoney(serviceFee);
  totalEl.textContent = formatMoney(total);
  document.getElementById('cartCount').textContent = String(items.reduce((sum, item) => sum + item.quantity, 0));
}

function updateCartQty(productId, change) {
  const item = cart.find((entry) => entry.id === productId);
  if (!item) return;

  item.quantity += change;
  if (item.quantity <= 0) {
    const idx = cart.findIndex((entry) => entry.id === productId);
    cart.splice(idx, 1);
  }
  renderCart();
}

async function loadReviews() {
  try {
    const reviews = await fetchJson(`${API_BASE}/reviews/shop/1`);
    renderReviews(reviews);
    document.getElementById('reviewCount').textContent = String(reviews.length);
    const total = reviews.reduce((sum, review) => sum + review.rating, 0);
    const avg = reviews.length ? (total / reviews.length).toFixed(1) : '0.0';
    document.getElementById('shopRating').textContent = avg;
  } catch (err) {
    console.error('Review load failed', err);
    renderReviews([]);
  }
}

function renderReviews(reviews) {
  const reviewList = document.getElementById('reviewList');
  if (!reviews.length) {
    reviewList.innerHTML = '<div class="review-item"><p>No reviews yet. Be the first to share your experience.</p></div>';
    return;
  }

  reviewList.innerHTML = reviews.map((r) => `
    <article class="review-item">
      <div class="review-header">
        <strong>${r.user}</strong>
        <span class="review-stars">${'★'.repeat(r.rating)}${'☆'.repeat(5 - r.rating)}</span>
      </div>
      <p>${r.comment}</p>
    </article>
  `).join('');
}

async function loadInventory() {
  try {
    const inventory = await fetchJson(`${API_BASE}/inventory/`);
    const lowCount = inventory.filter((item) => item.stock_level <= item.reorder_level).length;
    document.getElementById('inventoryAlerts').textContent = String(lowCount);

    const inventoryGrid = document.getElementById('inventoryGrid');
    inventoryGrid.innerHTML = inventory.map((item) => `
      <div class="inventory-item">
        <span class="inventory-status ${item.stock_level <= item.reorder_level ? 'low' : 'good'}">
          ${item.stock_level <= item.reorder_level ? 'Low stock' : 'In stock'}
        </span>
        <strong>${item.product_name}</strong>
        <span>${item.stock_level} ${item.unit} remaining</span>
      </div>
    `).join('');
  } catch (err) {
    console.error(err);
  }
}

function attachRatingStars() {
  document.querySelectorAll('.star-button').forEach((button) => {
    button.addEventListener('click', () => {
      selectedRating = Number(button.dataset.value);
      for (const star of document.querySelectorAll('.star-button')) {
        star.classList.toggle('active', Number(star.dataset.value) <= selectedRating);
      }
    });
  });
}

document.getElementById('reviewForm').addEventListener('submit', async (event) => {
  event.preventDefault();
  const name = document.getElementById('customerName').value.trim();
  const comment = document.getElementById('reviewComment').value.trim();

  if (!name || !comment || selectedRating === 0) {
    alert('Please enter your name, rating, and review comment.');
    return;
  }

  try {
    const payload = {
      rating: selectedRating,
      title: 'Customer Experience',
      comment,
      shop_id: 1,
      product_id: null
    };

    await fetchJson(`${API_BASE}/reviews/`, {
      method: 'POST',
      body: JSON.stringify(payload),
      headers: { Authorization: `Bearer demo-token` }
    });

    event.target.reset();
    selectedRating = 0;
    document.querySelectorAll('.star-button').forEach((star) => star.classList.remove('active'));
    loadReviews();
  } catch (err) {
    alert('Unable to submit review: ' + err.message);
  }
});

async function checkout() {
  const items = cart.map((entry) => ({ product_id: entry.id, quantity: entry.quantity }));
  if (!items.length) {
    alert('Add at least one item to your cart before placing an order.');
    return;
  }

  try {
    await fetchJson(`${API_BASE}/orders/`, {
      method: 'POST',
      body: JSON.stringify({ items, payment_method: 'card', notes: 'Coffee shop order' }),
      headers: { Authorization: `Bearer demo-token` }
    });
    cart.length = 0;
    renderCart();
    alert('Order placed successfully!');
  } catch (err) {
    alert(err.message);
  }
}

document.getElementById('checkoutBtn').addEventListener('click', checkout);
document.getElementById('authButton').addEventListener('click', () => alert('Demo mode: login is ready in the Python backend.'));

attachRatingStars();
loadProducts();
renderCart();
loadReviews();
loadInventory();
