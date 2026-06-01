<template>
    <section class="categories">
        <h2 class="section-title">Books by Category</h2>
        <div class="categories-grid">
            <div v-for="category in categories" :key="category.id" class="category-card"
                @click="selectCategory(category)" :class="{ active: selectedCategory === category.id }">
                <span class="category-icon">{{ category.icon }}</span>
                <span class="category-name">{{ category.name }}</span>
                <span class="category-count">{{ category.productCount }} items</span>
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['category-selected'])

const selectedCategory = ref(null)

const categories = ref([
    { id: 1, name: 'Fiction', icon: '🤖', productCount: 142 },
    { id: 2, name: 'Suspense', icon: '⁉️', productCount: 389 },
    { id: 3, name: 'Mystery', icon: '🔍', productCount: 215 },
    { id: 4, name: 'Science Fiction', icon: '🚀', productCount: 98 },
    { id: 5, name: 'Sports', icon: '⚽', productCount: 176 },
    { id: 6, name: 'Self-Help', icon: '💡', productCount: 63 },
    { id: 7, name: 'Beauty', icon: '💄', productCount: 204 },
    { id: 8, name: 'Police', icon: '🕵️', productCount: 57 },
])

function selectCategory(category) {
    selectedCategory.value = category.id
    emit('category-selected', category)
}
</script>

<style scoped>
.categories {
    padding: 24px 16px;
}

.section-title {
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 16px;
    color: #1e1b4b;
}

.categories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
    gap: 12px;
}

.category-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    padding: 16px 10px;
    border: 2px solid #e5e7eb;
    border-radius: 12px;
    cursor: pointer;
    transition: all 0.2s ease;
    background-color: #fff;
    text-align: center;
}

.category-card:hover {
    border-color: #4f46e5;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.15);
}

.category-card.active {
    border-color: #4f46e5;
    background-color: #eef2ff;
}

.category-icon {
    font-size: 2rem;
}

.category-name {
    font-size: 0.85rem;
    font-weight: 600;
    color: #374151;
}

.category-count {
    font-size: 0.75rem;
    color: #9ca3af;
}
</style>