<template>
  <div class="app">
    <header class="app-header">
      <h1 class="app-title">Bookmark Qwerty123</h1>
      <div class="cart-icon" @click="showCart = !showCart">
        🛒
        <span class="cart-count" v-if="cartItems.length">{{ cartItems.length }}</span>
      </div>
    </header>

    <!-- Cart notification -->
    <transition name="slide-down">
      <div class="cart-toast" v-if="lastAdded">
        ✅ <strong>{{ lastAdded.name }}</strong> added to cart!
      </div>
    </transition>

    <main class="app-main">
      <SearchBar @search="handleSearch" />

      <CategoriesSection @category-selected="handleCategorySelected" />

      <BestSellers @add-to-cart="handleAddToCart" />

      <FeaturedProducts @add-to-cart="handleAddToCart" />

      <CustomerReviews />
    </main>

    <footer class="app-footer">
      <p>© 2025 Bookmark Qwerty123. All rights reserved.</p>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import SearchBar from './components/SearchBar.vue'
import CategoriesSection from './components/CategoriesSection.vue'
import BestSellers from './components/BestSellers.vue'
import FeaturedProducts from './components/FeaturedProducts.vue'
import CustomerReviews from './components/CustomerReviews.vue'

const cartItems = ref([])
const lastAdded = ref(null)
const showCart = ref(false)
let toastTimer = null

function handleAddToCart(product) {
  cartItems.value.push(product)
  lastAdded.value = product

  // Auto-hide toast after 2.5s
  clearTimeout(toastTimer)
  toastTimer = setTimeout(() => {
    lastAdded.value = null
  }, 2500)
}

function handleSearch(query) {
  console.log('Search:', query)
  // Conectar con lógica de filtrado global acá
}

function handleCategorySelected(category) {
  console.log('Category selected:', category)
  // Conectar con lógica de filtrado global acá
}
</script>

<style scoped>
.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--color-bg);
}

.app-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background-color: var(--color-surface);
  border-bottom: 1px solid var(--color-border);
  padding: 14px 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.app-title {
  font-family: var(--font-display);
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--color-primary);
  letter-spacing: -0.03em;
}

.cart-icon {
  font-size: 1.5rem;
  cursor: pointer;
  position: relative;
  padding: 4px;
  transition: transform 0.2s;
}

.cart-icon:hover {
  transform: scale(1.1);
}

.cart-count {
  position: absolute;
  top: -4px;
  right: -6px;
  background-color: var(--color-danger);
  color: white;
  font-size: 0.65rem;
  font-weight: 800;
  border-radius: 50%;
  width: 18px;
  height: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cart-toast {
  position: fixed;
  top: 72px;
  right: 20px;
  z-index: 200;
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
  border-left: 4px solid var(--color-success);
  padding: 12px 20px;
  border-radius: 10px;
  font-size: 0.88rem;
  color: var(--color-text);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.1);
}

.app-main {
  flex: 1;
  max-width: 1280px;
  width: 100%;
  margin: 0 auto;
  padding: 16px 0 40px;
}

.app-footer {
  background-color: var(--color-surface);
  border-top: 1px solid var(--color-border);
  text-align: center;
  padding: 20px;
  font-size: 0.82rem;
  color: var(--color-text-muted);
}

/* Toast animation */
.slide-down-enter-active,
.slide-down-leave-active {
  transition: all 0.3s ease;
}

.slide-down-enter-from,
.slide-down-leave-to {
  opacity: 0;
  transform: translateY(-12px);
}
</style>