<template>
    <section class="search-bar">
        <input v-model="query" type="text" placeholder="Search for products..." @keyup.enter="handleSearch" />
        <button @click="handleSearch">Search</button>
    </section>
</template>

<script setup>
import { ref } from 'vue'

const query = ref('')

const emit = defineEmits(['search'])

function handleSearch() {
    if (query.value.trim()) {
        emit('search', query.value.trim())
    }
}
</script>

<style scoped>
.search-bar {
    display: flex;
    gap: 8px;
    padding: 16px;
}

.search-bar input {
    flex: 1;
    padding: 10px 14px;
    border: 1px solid #ccc;
    border-radius: 6px;
    font-size: 1rem;
    outline: none;
    transition: border-color 0.2s;
}

.search-bar input:focus {
    border-color: #4f46e5;
}

.search-bar button {
    padding: 10px 20px;
    background-color: #4f46e5;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.2s;
}

.search-bar button:hover {
    background-color: #3730a3;
}
</style>