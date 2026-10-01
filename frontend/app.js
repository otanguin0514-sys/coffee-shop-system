* {
  box-sizing: border-box;
}

:root {
  --bg: #f7f1eb;
  --panel: #fffdfb;
  --panel-alt: #f0e5dc;
  --coffee: #51362a;
  --coffee-dark: #2d1a13;
  --accent: #c98d5f;
  --gold: #f3c56b;
  --text: #2d201d;
  --muted: #6a544d;
  --success: #3e8b5d;
  --danger: #a35b46;
  --shadow: 0 18px 40px rgba(57, 33, 23, 0.12);
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  font-family: "Inter", sans-serif;
  background: var(--bg);
  color: var(--text);
}

button, input, textarea {
  font: inherit;
}

a {
  text-decoration: none;
  color: inherit;
}

.container {
  width: min(1180px, calc(100% - 32px));
  margin: 0 auto;
}

.topbar {
  position: sticky;
  top: 0;
  z-index: 10;
  background: rgba(247, 241, 235, 0.88);
  border-bottom: 1px solid rgba(81, 54, 42, 0.08);
  backdrop-filter: blur(8px);
}

.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px 0;
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-mark {
  width: 42px;
  height: 42px;
  display: grid;
  place-items: center;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--coffee), var(--accent));
  color: white;
  font-family: "Cormorant Garamond", serif;
  font-size: 2rem;
  font-weight: 700;
}

.brand-name {
  margin: 0;
  font-weight: 700;
}

.brand span {
  color: var(--muted);
  font-size: 0.76rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.nav-links {
  display: flex;
  gap: 28px;
  color: var(--muted);
  font-weight: 500;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.primary-button, .secondary-button, .checkout-button, .filter-pill {
  border: none;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.primary-button, .checkout-button {
  background: linear-gradient(135deg, var(--coffee), var(--coffee-dark));
  color: white;
  padding: 0.9rem 1.3rem;
  border-radius: 999px;
  font-weight: 600;
  box-shadow: 0 12px 30px rgba(81, 54, 42, 0.2);
}

.secondary-button {
  background: var(--panel);
  color: var(--coffee);
  border: 1px solid rgba(81, 54, 42, 0.15);
  padding: 0.9rem 1.3rem;
  border-radius: 999px;
  font-weight: 600;
}

.cart-button {
  position: relative;
  border: none;
  background: rgba(81, 54, 42, 0.06);
  border-radius: 999px;
  width: 48px;
  height: 48px;
  cursor: pointer;
}

.cart-count {
  position: absolute;
  top: -6px;
  right: -4px;
  background: var(--accent);
  color: white;
  border-radius: 999px;
  width: 20px;
  height: 20px;
  display: grid;
  place-items: center;
  font-size: 0.72rem;
  font-weight: 700;
}

.hero {
  padding: 64px 0 44px;
}

.hero-inner {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 28px;
  align-items: center;
}

.eyebrow {
  display: inline-block;
  color: var(--accent);
  font-size: 0.78rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  font-weight: 700;
  margin-bottom: 14px;
}

.hero-copy h1,
.section-heading h2,
.review-form-card h3 {
  margin: 0;
  color: var(--coffee-dark);
  font-family: "Cormorant Garamond", serif;
}

.hero-copy h1 {
  font-size: clamp(3rem, 5vw, 5rem);
  line-height: 0.9;
  letter-spacing: -0.04em;
}

.hero-copy p {
  max-width: 560px;
  font-size: 1.05rem;
  line-height: 1.8;
  color: var(--muted);
  margin: 18px 0 30px;
}

.hero-actions {
  display: flex;
  gap: 16px;
  margin-bottom: 30px;
}

.hero-metrics {
  display: flex;
  gap: 28px;
  flex-wrap: wrap;
}

.hero-metrics div {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.hero-metrics strong {
  font-size: 1.35rem;
  color: var(--coffee-dark);
}

.hero-metrics span {
  color: var(--muted);
  font-size: 0.82rem;
}

.hero-card {
  background: linear-gradient(180deg, rgba(255,255,255,0.58), rgba(244, 224, 210, 0.7));
  border: 1px solid rgba(81, 54, 42, 0.08);
  border-radius: 30px;
  box-shadow: var(--shadow);
  padding: 28px;
}

.coffee-art {
  position: relative;
  height: 230px;
  background: radial-gradient(circle at 50% 36%, #f4dcc0, #d9a97f 55%, #b1754f 80%, #714d38 100%);
  border-radius: 22px;
  overflow: hidden;
  margin-bottom: 20px;
}

.cup {
  position: absolute;
  width: 180px;
  height: 110px;
  background: rgba(255, 250, 247, 0.92);
  border-radius: 0 0 24px 24px;
  left: 50%;
  top: 56%;
  transform: translate(-50%, -50%);
  border-top: 12px solid rgba(106, 84, 77, 0.15);
  box-shadow: inset 0 -18px 0 rgba(231, 191, 154, 0.6);
}

.cup::before {
  content: "";
  position: absolute;
  width: 120px;
  height: 28px;
  background: rgba(235, 207, 182, 0.9);
  border-radius: 50%;
  left: 50%;
  top: -12px;
  transform: translateX(-50%);
}

.cup::after {
  content: "";
  position: absolute;
  width: 28px;
  height: 70px;
  border: 10px solid rgba(255, 255, 255, 0.8);
  border-left: none;
  border-radius: 0 18px 18px 0;
  right: -28px;
  top: 18px;
}

.steam {
  position: absolute;
  width: 16px;
  height: 80px;
  background: linear-gradient(180deg, rgba(255,255,255,0.65), rgba(255,255,255,0));
  border-radius: 999px;
  left: 50%;
  top: 16%;
  filter: blur(2px);
  animation: steam 4s infinite ease-in-out;
}

.steam-one { margin-left: -50px; }
.steam-two { margin-left: 10px; animation-delay: 0.8s; }
.steam-three { margin-left: 70px; animation-delay: 1.6s; }

@keyframes steam {
  0% { transform: translateY(0) scaleY(0.95); opacity: 0.4; }
  50% { transform: translateY(-18px) scaleY(1); opacity: 0.8; }
  100% { transform: translateY(-36px) scaleY(1.08); opacity: 0; }
}

.promo-tag {
  display: inline-flex;
  background: rgba(255, 255, 255, 0.7);
  color: var(--accent);
  padding: 0.45rem 0.75rem;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.hero-card h3 {
  margin: 14px 0 10px;
  font-size: 2rem;
  color: var(--coffee-dark);
}

.promo-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: var(--muted);
}

.promo-row strong {
  color: var(--coffee-dark);
  font-size: 1.3rem;
}

.stats {
  padding: 20px 0 10px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 18px;
}

.stat-card {
  background: rgba(255,255,255,0.7);
  border: 1px solid rgba(81, 54, 42, 0.08);
  border-radius: 20px;
  padding: 24px 20px;
  box-shadow: 0 10px 25px rgba(73, 49, 39, 0.06);
}

.stat-card strong {
  display: block;
  margin-top: 10px;
  font-size: clamp(1.7rem, 2vw, 2.3rem);
  color: var(--coffee-dark);
}

.stat-label {
  color: var(--muted);
  font-size: 0.8rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-weight: 700;
}

.stat-card small {
  display: block;
  margin-top: 8px;
  color: var(--muted);
}

.shop-layout {
  display: grid;
  grid-template-columns: 1.4fr 0.7fr;
  gap: 26px;
  padding: 52px 0 20px;
}

.menu-panel, .cart-panel, .review-block, .review-form-card {
  background: rgba(255,255,255,0.65);
  border: 1px solid rgba(81, 54, 42, 0.08);
  border-radius: 28px;
  box-shadow: 0 14px 36px rgba(73, 49, 39, 0.06);
}

.menu-panel, .cart-panel, .review-block, .review-form-card {
  padding: 24px;
}

.section-heading {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 22px;
}

.section-heading h2 {
  font-size: clamp(2.2rem, 4vw, 3rem);
  color: var(--coffee-dark);
}

.menu-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}

.menu-item {
  background: var(--panel);
  border: 1px solid rgba(81, 54, 42, 0.08);
  border-radius: 22px;
  padding: 18px;
}

.menu-top {
  display: flex;
  justify-content: space-between;
  gap: 12px;
}

.menu-item h3 {
  margin: 0;
  color: var(--coffee-dark);
  font-size: 1.3rem;
}

.badge {
  background: rgba(243, 197, 107, 0.22);
  color: var(--coffee);
  border-radius: 999px;
  font-size: 0.7rem;
  padding: 0.4rem 0.55rem;
  font-weight: 700;
  white-space: nowrap;
}

.menu-item p {
  margin: 12px 0 18px;
  color: var(--muted);
  line-height: 1.6;
  min-height: 52px;
}

.meta-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}

.price {
  font-weight: 700;
  color: var(--coffee-dark);
  font-size: 1.3rem;
}

.add-button {
  border: none;
  background: var(--coffee);
  color: white;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  font-size: 1.4rem;
  cursor: pointer;
}

.cart-panel {
  position: sticky;
  top: 92px;
  height: fit-content;
}

.cart-items {
  display: flex;
  flex-direction: column;
  gap: 14px;
  min-height: 150px;
}

.empty-cart {
  border: 1px dashed rgba(81, 54, 42, 0.2);
  border-radius: 16px;
  background: rgba(81, 54, 42, 0.02);
  padding: 22px 14px;
  color: var(--muted);
  text-align: center;
}

.cart-item {
  background: rgba(81, 54, 42, 0.03);
  border-radius: 16px;
  padding: 12px 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.cart-item-name {
  font-weight: 600;
  color: var(--coffee-dark);
}

.cart-item-meta {
  color: var(--muted);
  font-size: 0.82rem;
}

.qty-control {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255,255,255,0.78);
  border-radius: 999px;
  padding: 4px 8px;
}

.qty-control button {
  width: 22px;
  height: 22px;
  border: none;
  border-radius: 50%;
  background: var(--panel-alt);
  color: var(--coffee-dark);
  cursor: pointer;
}

.summary-box {
  border-top: 1px solid rgba(81, 54, 42, 0.1);
  padding-top: 16px;
  margin-top: 18px;
}

.summary-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  color: var(--muted);
}

.summary-row.total {
  font-size: 1.1rem;
  color: var(--coffee-dark);
  margin-top: 18px;
  padding-top: 12px;
  border-top: 1px solid rgba(81, 54, 42, 0.12);
}

.checkout-button {
  width: 100%;
  margin-top: 16px;
}

.reviews-section {
  padding: 52px 0 24px;
}

.reviews-layout {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 26px;
}

.review-list {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.review-item {
  background: rgba(255,255,255,0.68);
  border: 1px solid rgba(81, 54, 42, 0.08);
  border-radius: 18px;
  padding: 18px;
}

.review-header {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 8px;
}

.review-header strong {
  color: var(--coffee-dark);
}

.review-stars {
  color: var(--gold);
  letter-spacing: 0.1em;
}

.review-item p {
  margin: 0;
  line-height: 1.7;
  color: var(--muted);
}

#reviewForm {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

#reviewForm label {
  display: flex;
  flex-direction: column;
  gap: 8px;
  color: var(--coffee-dark);
  font-weight: 600;
}

#reviewForm input,
#reviewForm textarea {
  border: 1px solid rgba(81, 54, 42, 0.12);
  border-radius: 14px;
  padding: 0.9rem 1rem;
  background: rgba(255,255,255,0.7);
  color: var(--text);
}

.stars {
  display: flex;
  gap: 8px;
}

.star-button {
  font-size: 1.8rem;
  background: transparent;
  border: none;
  color: #d0c8c4;
  cursor: pointer;
}

.star-button.active {
  color: var(--gold);
}

.full-width {
  width: 100%;
}

.inventory-section {
  margin: 18px auto 60px;
  padding: 24px;
  background: rgba(255,255,255,0.65);
  border: 1px solid rgba(81, 54, 42, 0.08);
  border-radius: 28px;
  box-shadow: 0 14px 36px rgba(73, 49, 39, 0.06);
}

.inventory-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 16px;
}

.inventory-item {
  background: rgba(255,255,255,0.72);
  border-radius: 18px;
  border: 1px solid rgba(81, 54, 42, 0.08);
  padding: 18px;
}

.inventory-status {
  display: inline-block;
  padding: 0.42rem 0.7rem;
  border-radius: 999px;
  font-size: 0.74rem;
  font-weight: 700;
  margin-bottom: 10px;
}

.inventory-status.good {
  background: rgba(62, 139, 93, 0.12);
  color: var(--success);
}

.inventory-status.low {
  background: rgba(163, 91, 70, 0.12);
  color: var(--danger);
}

.inventory-item strong {
  display: block;
  font-size: 1.15rem;
  margin-bottom: 10px;
  color: var(--coffee-dark);
}

.inventory-item span {
  color: var(--muted);
}

.site-footer {
  background: var(--coffee-dark);
  color: rgba(255,255,255,0.8);
  padding: 28px 0;
}

.footer-inner {
  display: flex;
  justify-content: space-between;
  gap: 18px;
  align-items: center;
}

@media (max-width: 980px) {
  .hero-inner, .shop-layout, .reviews-layout {
    grid-template-columns: 1fr;
  }

  .stats-grid, .inventory-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 680px) {
  .nav {
    flex-wrap: wrap;
    justify-content: center;
    gap: 16px;
  }

  .nav-links {
    order: 3;
    width: 100%;
    justify-content: center;
    flex-wrap: wrap;
  }

  .menu-grid, .stats-grid, .inventory-grid {
    grid-template-columns: 1fr;
  }

  .hero-metrics {
    gap: 12px 18px;
  }

  .hero-actions {
    flex-direction: column;
    align-items: stretch;
  }

  .footer-inner {
    flex-direction: column;
    align-items: flex-start;
  }
}
