<template>
    <section class="featured-products">
        <div class="section-header">
            <h2 class="section-title">✨ Featured Products</h2>
            <div class="filter-tabs">
                <button v-for="tab in tabs" :key="tab" class="tab" :class="{ active: activeTab === tab }"
                    @click="activeTab = tab">
                    {{ tab }}
                </button>
            </div>
        </div>

        <div class="products-grid">
            <div v-for="product in filteredProducts" :key="product.id" class="product-card">
                <div class="image-wrapper">
                    <img :src="product.image" :alt="product.name" class="product-image" />
                    <button class="wishlist-btn" :class="{ active: wishlist.includes(product.id) }"
                        @click="toggleWishlist(product.id)">
                        {{ wishlist.includes(product.id) ? '❤️' : '🤍' }}
                    </button>
                    <div class="discount-tag" v-if="product.discount">
                        -{{ product.discount }}%
                    </div>
                </div>

                <div class="product-info">
                    <span class="product-category">{{ product.category }}</span>
                    <h3 class="product-name">{{ product.name }}</h3>
                    <p class="product-author">{{ product.author }}</p>
                    <p class="product-desc">{{ product.description }}</p>

                    <div class="rating">
                        <span class="stars">{{ renderStars(product.rating) }}</span>
                        <span class="review-count">({{ product.reviews }})</span>
                    </div>

                    <div class="price-row">
                        <div class="prices">
                            <span class="price">${{ product.price.toFixed(2) }}</span>
                            <span class="original-price" v-if="product.originalPrice">
                                ${{ product.originalPrice.toFixed(2) }}
                            </span>
                        </div>
                        <button class="cart-btn" @click="addToCart(product)">
                            🛒
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <p v-if="filteredProducts.length === 0" class="empty-state">
            No books found in this category.
        </p>
    </section>
</template>

<script setup>
import { ref, computed } from 'vue'

// 👇 Importá tus imágenes acá
import CAMPANAS from '../assets/images/Campanas.webp'
import FOUNDATION from '../assets/images/Foundation.webp'
import Rayuela from '../assets/images/Rayuela.webp'
import MOBYDICK from '../assets/images/MobyDick.jpg'
import THE_WITCHER from '../assets/images/Witcher.jpg'
import PLATERO from '../assets/images/Platero.jpg'


const emit = defineEmits(['add-to-cart'])

const activeTab = ref('All')
const wishlist = ref([])

const tabs = ['All', 'Fiction', 'Sci-Fi', 'Non-Fiction', 'Classic']

const products = ref([
    {
        id: 201,
        name: 'For whom the bell tolls',
        author: 'Ernest Hemingway',
        category: 'Fiction',
        image: CAMPANAS,
        description: 'A novel about the Spanish Civil War and its impact on the characters.',
        price: 24.99,
        originalPrice: 34.99,
        discount: 28,
        rating: 4.8,
        reviews: 3210,
    },
    {
        id: 202,
        name: 'Foundation',
        author: 'Isaac Asimov',
        category: 'Sci-Fi',
        image: FOUNDATION,
        description: 'The collapse of a galactic empire and those who seek to shorten the dark age.',
        price: 19.99,
        originalPrice: null,
        discount: null,
        rating: 4.6,
        reviews: 1870,
    },
    {
        id: 203,
        name: 'Rayuela',
        author: 'Julio Cortázar',
        category: 'Fiction',
        image: Rayuela,
        description: 'A groundbreaking novel that challenges traditional narrative structures.',
        price: 22.99,
        originalPrice: 32.99,
        discount: 30,
        rating: 4.7,
        reviews: 5430,
    },
    {
        id: 204,
        name: 'Moby Dick',
        author: 'Herman Melville',
        category: 'Classic',
        image: MOBYDICK,
        description: 'The epic tale of Captain Ahab and his obsession with the great white whale.',
        price: 18.99,
        originalPrice: null,
        discount: null,
        rating: 4.9,
        reviews: 7820,
    },
    {
        id: 205,
        name: 'The Witcher',
        author: 'Andrzej Sapkowski',
        category: 'Fantasy',
        image: THE_WITCHER,
        description: 'The adventures of Geralt of Rivia, a monster hunter in a fantasy world.',
        price: 89.99,
        originalPrice: 122.99,
        discount: 26,
        rating: 4.5,
        reviews: 1240,
    },
    {
        id: 206,
        name: 'Platero y yo',
        author: 'Juan Ramón Jiménez',
        category: 'Classic',
        image: PLATERO,
        description: 'A touching story of a boy and his donkey in the Spanish countryside.',
        price: 15.99,
        originalPrice: 18.99,
        discount: 31,
        rating: 4.8,
        reviews: 9100,
    },
])

const filteredProducts = computed(() => {
    if (activeTab.value === 'All') return products.value
    return products.value.filter(p => p.category === activeTab.value)
})

function renderStars(rating) {
    const full = Math.floor(rating)
    const half = rating % 1 >= 0.5 ? 1 : 0
    const empty = 5 - full - half
    return '★'.repeat(full) + (half ? '½' : '') + '☆'.repeat(empty)
}

function toggleWishlist(id) {
    const index = wishlist.value.indexOf(id)
    if (index === -1) {
        wishlist.value.push(id)
    } else {
        wishlist.value.splice(index, 1)
    }
}

function addToCart(product) {
    emit('add-to-cart', product)
}
</script>

<style scoped>
.featured-products {
    padding: 24px 16px;
}

.section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 20px;
}

.section-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #1e1b4b;
}

.filter-tabs {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

.tab {
    padding: 6px 16px;
    border-radius: 20px;
    border: 2px solid #e5e7eb;
    background: white;
    font-size: 0.82rem;
    font-weight: 600;
    color: #6b7280;
    cursor: pointer;
    transition: all 0.2s;
}

.tab:hover {
    border-color: #4f46e5;
    color: #4f46e5;
}

.tab.active {
    background-color: #4f46e5;
    border-color: #4f46e5;
    color: white;
}

.products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 20px;
}

.product-card {
    background: white;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    overflow: hidden;
    transition: all 0.2s ease;
    display: flex;
    flex-direction: column;
}

.product-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
}

.image-wrapper {
    position: relative;
    width: 100%;
    height: 220px;
    overflow: hidden;
    background-color: #f3f4f6;
}

.product-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.3s ease;
}

.product-card:hover .product-image {
    transform: scale(1.04);
}

.wishlist-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    background: white;
    border: none;
    border-radius: 50%;
    width: 32px;
    height: 32px;
    font-size: 1rem;
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: transform 0.2s;
}

.wishlist-btn:hover {
    transform: scale(1.15);
}

.discount-tag {
    position: absolute;
    top: 10px;
    left: 10px;
    background-color: #ef4444;
    color: white;
    font-size: 0.72rem;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 20px;
}

.product-info {
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 5px;
    flex: 1;
}

.product-category {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #9ca3af;
    font-weight: 600;
}

.product-name {
    font-size: 0.95rem;
    font-weight: 700;
    color: #111827;
    line-height: 1.3;
}

.product-author {
    font-size: 0.8rem;
    color: #6b7280;
    font-style: italic;
}

.product-desc {
    font-size: 0.8rem;
    color: #6b7280;
    line-height: 1.4;
    margin: 2px 0;
}

.rating {
    display: flex;
    align-items: center;
    gap: 4px;
}

.stars {
    color: #f59e0b;
    font-size: 0.82rem;
}

.review-count {
    font-size: 0.72rem;
    color: #9ca3af;
}

.price-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 6px;
}

.prices {
    display: flex;
    align-items: center;
    gap: 6px;
}

.price {
    font-size: 1.1rem;
    font-weight: 800;
    color: #4f46e5;
}

.original-price {
    font-size: 0.82rem;
    color: #9ca3af;
    text-decoration: line-through;
}

.cart-btn {
    background-color: #eef2ff;
    border: none;
    border-radius: 8px;
    padding: 8px 10px;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.2s;
}

.cart-btn:hover {
    background-color: #4f46e5;
}

.empty-state {
    text-align: center;
    color: #9ca3af;
    padding: 40px 0;
    font-size: 0.95rem;
}
</style>