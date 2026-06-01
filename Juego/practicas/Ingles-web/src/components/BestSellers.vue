<template>
    <section class="best-sellers">
        <div class="section-header">
            <h2 class="section-title">🏆 Best Sellers</h2>
            <button class="view-all">View All</button>
        </div>

        <div class="products-grid">
            <div v-for="product in bestSellers" :key="product.id" class="product-card">
                <div class="badge">{{ product.badge }}</div>

                <div class="product-image">
                    <img :src="product.image" :alt="product.name" />
                </div>

                <div class="product-info">
                    <span class="product-category">{{ product.category }}</span>
                    <h3 class="product-name">{{ product.name }}</h3>
                    <p class="product-author">{{ product.author }}</p>

                    <div class="rating">
                        <span class="stars">{{ renderStars(product.rating) }}</span>
                        <span class="review-count">({{ product.reviews }})</span>
                    </div>

                    <div class="price-row">
                        <span class="price">${{ product.price.toFixed(2) }}</span>
                        <span class="original-price" v-if="product.originalPrice">
                            ${{ product.originalPrice.toFixed(2) }}
                        </span>
                    </div>
                </div>

                <button class="add-to-cart" @click="addToCart(product)">
                    Add to Cart
                </button>
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref } from 'vue'

// 👇 Importá cada imagen así
import LOTR from '../assets/images/ELSDA.jpg'
import DUNE from '../assets/images/DUNE.jpg'
import KARAMAZOV from '../assets/images/Karamazov.webp'
import HOLMES from '../assets/images/Holmes.webp'

const emit = defineEmits(['add-to-cart'])

const bestSellers = ref([
    {
        id: 101,
        name: 'The Lord of the Rings: Trilogy',
        author: 'J.R.R. Tolkien',
        category: 'Fiction',
        image: LOTR,
        price: 89.99,
        originalPrice: 129.99,
        rating: 4.8,
        reviews: 2340,
        badge: '🔥 Hot',
    },
    {
        id: 102,
        name: 'Dune',
        author: 'Frank Herbert',
        category: 'Sci-Fi',
        image: DUNE,
        price: 24.99,
        originalPrice: 34.99,
        rating: 4.7,
        reviews: 1870,
        badge: '⭐ Top Rated',
    },
    {
        id: 103,
        name: 'Karamazov Brothers',
        author: 'Fyodor Dostoevsky',
        category: 'Classic',
        image: KARAMAZOV,
        price: 19.99,
        originalPrice: null,
        rating: 4.9,
        reviews: 4120,
        badge: '💎 Staff Pick',
    },
    {
        id: 104,
        name: 'Sherlock Holmes: The Complete Novels',
        author: 'Arthur Conan Doyle',
        category: 'Mystery',
        image: HOLMES,
        price: 34.99,
        originalPrice: 49.99,
        rating: 4.6,
        reviews: 983,
        badge: '🔥 Hot',
    },
])

function renderStars(rating) {
    const full = Math.floor(rating)
    const half = rating % 1 >= 0.5 ? 1 : 0
    const empty = 5 - full - half
    return '★'.repeat(full) + (half ? '½' : '') + '☆'.repeat(empty)
}

function addToCart(product) {
    emit('add-to-cart', product)
}
</script>

<style scoped>
.best-sellers {
    padding: 24px 16px;
    background-color: #fafafa;
}

.section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.section-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #1e1b4b;
}

.view-all {
    background: none;
    border: 2px solid #4f46e5;
    color: #4f46e5;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
}

.view-all:hover {
    background-color: #4f46e5;
    color: white;
}

.products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
}

.product-card {
    background: white;
    border-radius: 14px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    border: 1px solid #e5e7eb;
    position: relative;
    transition: all 0.2s ease;
}

.product-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.badge {
    position: absolute;
    top: 12px;
    left: 12px;
    background-color: #1e1b4b;
    color: white;
    font-size: 0.7rem;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 20px;
    z-index: 1;
}

.product-image {
    width: 100%;
    height: 200px;
    border-radius: 8px;
    overflow: hidden;
    background-color: #f3f4f6;
}

.product-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.3s ease;
}

.product-card:hover .product-image img {
    transform: scale(1.04);
}

.product-info {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.product-category {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
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

.rating {
    display: flex;
    align-items: center;
    gap: 4px;
    margin-top: 2px;
}

.stars {
    color: #f59e0b;
    font-size: 0.85rem;
}

.review-count {
    font-size: 0.75rem;
    color: #9ca3af;
}

.price-row {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 4px;
}

.price {
    font-size: 1.1rem;
    font-weight: 800;
    color: #4f46e5;
}

.original-price {
    font-size: 0.85rem;
    color: #9ca3af;
    text-decoration: line-through;
}

.add-to-cart {
    margin-top: auto;
    padding: 10px;
    background-color: #4f46e5;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.2s;
}

.add-to-cart:hover {
    background-color: #3730a3;
}
</style>