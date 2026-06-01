<template>
    <section class="customer-reviews">
        <div class="section-header">
            <h2 class="section-title">💬 Customer Reviews</h2>
            <div class="overall-rating">
                <span class="big-score">{{ overallRating }}</span>
                <div class="rating-details">
                    <span class="stars">{{ renderStars(overallRating) }}</span>
                    <span class="total-reviews">{{ reviews.length }} reviews</span>
                </div>
            </div>
        </div>

        <!-- Rating breakdown -->
        <div class="rating-breakdown">
            <div v-for="n in [5, 4, 3, 2, 1]" :key="n" class="breakdown-row">
                <span class="breakdown-label">{{ n }} ★</span>
                <div class="breakdown-bar">
                    <div class="breakdown-fill" :style="{ width: getPercentage(n) + '%' }" :class="`fill-${n}`"></div>
                </div>
                <span class="breakdown-count">{{ countByStars(n) }}</span>
            </div>
        </div>

        <!-- Reviews list -->
        <div class="reviews-list">
            <div v-for="review in visibleReviews" :key="review.id" class="review-card">
                <div class="review-header">
                    <div class="reviewer-info">
                        <div class="avatar">{{ review.avatar }}</div>
                        <div>
                            <p class="reviewer-name">{{ review.name }}</p>
                            <p class="review-date">{{ review.date }}</p>
                        </div>
                    </div>
                    <div class="review-rating">
                        <span class="stars">{{ renderStars(review.rating) }}</span>
                        <span class="verified" v-if="review.verified">✅ Verified</span>
                    </div>
                </div>

                <p class="review-product">Re: <strong>{{ review.product }}</strong></p>
                <p class="review-text">{{ review.text }}</p>

                <div class="review-footer">
                    <button class="helpful-btn" :class="{ liked: likedReviews.includes(review.id) }"
                        @click="toggleHelpful(review.id)">
                        👍 Helpful ({{ review.helpful + (likedReviews.includes(review.id) ? 1 : 0) }})
                    </button>
                </div>
            </div>
        </div>

        <!-- Show more -->
        <div class="show-more-wrapper" v-if="reviews.length > visibleCount">
            <button class="show-more-btn" @click="visibleCount += 3">
                Load More Reviews ↓
            </button>
        </div>
    </section>
</template>

<script setup>
import { ref, computed } from 'vue'

const visibleCount = ref(3)
const likedReviews = ref([])

const reviews = ref([
    {
        id: 301,
        name: 'Sarah M.',
        avatar: '👩',
        date: 'May 18, 2025',
        rating: 5,
        product: 'The Lord of the Rings: Trilogy Box Set',
        text: 'Absolutely love this trilogy! Dont know how to describe the epicness.',
        helpful: 42,
        verified: true,
    },
    {
        id: 302,
        name: 'James T.',
        avatar: '👨',
        date: 'May 10, 2025',
        rating: 4,
        product: 'Karamazov Brothers',
        text: 'A masterpiece of literature. The psychological depth and philosophical themes are unparalleled.',
        helpful: 28,
        verified: true,
    },
    {
        id: 303,
        name: 'Lucia R.',
        avatar: '👩‍🦱',
        date: 'April 30, 2025',
        rating: 5,
        product: 'Sherlock Holmes: Complete Collection',
        text: 'Now i can become a detective like Sherlock! The stories are thrilling and the writing is brilliant. A must-have for mystery lovers.',
        helpful: 17,
        verified: false,
    },
    {
        id: 304,
        name: 'Carlos D.',
        avatar: '🧔',
        date: 'April 22, 2025',
        rating: 3,
        product: 'Dune',
        text: 'The world-building is incredible but the pacing was a bit slow for me. Still, a classic worth reading.',
        helpful: 9,
        verified: true,
    },
    {
        id: 305,
        name: 'Nina K.',
        avatar: '👩‍🦰',
        date: 'April 15, 2025',
        rating: 5,
        product: 'Rayuela',
        text: 'A groundbreaking novel that challenges traditional narrative structures. It was a bit confusing at first but once you get into it, its a rewarding experience.',
        helpful: 56,
        verified: true,
    },
    {
        id: 306,
        name: 'Tom W.',
        avatar: '👦',
        date: 'April 8, 2025',
        rating: 4,
        product: 'The Witcher',
        text: 'A novel so good,that we can see on videogame and series.',
        helpful: 13,
        verified: false,
    },
])

const visibleReviews = computed(() => reviews.value.slice(0, visibleCount.value))

const overallRating = computed(() => {
    const avg = reviews.value.reduce((sum, r) => sum + r.rating, 0) / reviews.value.length
    return avg.toFixed(1)
})

function countByStars(n) {
    return reviews.value.filter(r => Math.floor(r.rating) === n).length
}

function getPercentage(n) {
    return Math.round((countByStars(n) / reviews.value.length) * 100)
}

function renderStars(rating) {
    const full = Math.floor(rating)
    const half = rating % 1 >= 0.5 ? 1 : 0
    const empty = 5 - full - half
    return '★'.repeat(full) + (half ? '½' : '') + '☆'.repeat(empty)
}

function toggleHelpful(id) {
    const index = likedReviews.value.indexOf(id)
    if (index === -1) {
        likedReviews.value.push(id)
    } else {
        likedReviews.value.splice(index, 1)
    }
}
</script>

<style scoped>
.customer-reviews {
    padding: 24px 16px;
    background-color: #fafafa;
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

.overall-rating {
    display: flex;
    align-items: center;
    gap: 10px;
}

.big-score {
    font-size: 2.8rem;
    font-weight: 900;
    color: #1e1b4b;
    line-height: 1;
}

.rating-details {
    display: flex;
    flex-direction: column;
    gap: 2px;
}

.stars {
    color: #f59e0b;
    font-size: 0.9rem;
}

.total-reviews {
    font-size: 0.78rem;
    color: #9ca3af;
}

/* Breakdown */
.rating-breakdown {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 24px;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.breakdown-row {
    display: flex;
    align-items: center;
    gap: 10px;
}

.breakdown-label {
    font-size: 0.82rem;
    font-weight: 600;
    color: #374151;
    width: 28px;
    text-align: right;
}

.breakdown-bar {
    flex: 1;
    height: 8px;
    background-color: #f3f4f6;
    border-radius: 99px;
    overflow: hidden;
}

.breakdown-fill {
    height: 100%;
    border-radius: 99px;
    transition: width 0.6s ease;
}

.fill-5 {
    background-color: #22c55e;
}

.fill-4 {
    background-color: #84cc16;
}

.fill-3 {
    background-color: #f59e0b;
}

.fill-2 {
    background-color: #f97316;
}

.fill-1 {
    background-color: #ef4444;
}

.breakdown-count {
    font-size: 0.78rem;
    color: #9ca3af;
    width: 16px;
}

/* Reviews */
.reviews-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.review-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 18px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    transition: box-shadow 0.2s;
}

.review-card:hover {
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.07);
}

.review-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 8px;
}

.reviewer-info {
    display: flex;
    align-items: center;
    gap: 10px;
}

.avatar {
    font-size: 2rem;
    background: #eef2ff;
    border-radius: 50%;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.reviewer-name {
    font-size: 0.9rem;
    font-weight: 700;
    color: #111827;
}

.review-date {
    font-size: 0.75rem;
    color: #9ca3af;
}

.review-rating {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 3px;
}

.verified {
    font-size: 0.72rem;
    color: #16a34a;
    font-weight: 600;
}

.review-product {
    font-size: 0.8rem;
    color: #6b7280;
}

.review-text {
    font-size: 0.88rem;
    color: #374151;
    line-height: 1.6;
}

.review-footer {
    display: flex;
    justify-content: flex-end;
}

.helpful-btn {
    background: none;
    border: 1px solid #e5e7eb;
    border-radius: 20px;
    padding: 5px 14px;
    font-size: 0.8rem;
    color: #6b7280;
    cursor: pointer;
    transition: all 0.2s;
}

.helpful-btn:hover {
    border-color: #4f46e5;
    color: #4f46e5;
}

.helpful-btn.liked {
    background-color: #eef2ff;
    border-color: #4f46e5;
    color: #4f46e5;
    font-weight: 600;
}

/* Show more */
.show-more-wrapper {
    display: flex;
    justify-content: center;
    margin-top: 24px;
}

.show-more-btn {
    padding: 10px 32px;
    border: 2px solid #4f46e5;
    background: white;
    color: #4f46e5;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
}

.show-more-btn:hover {
    background-color: #4f46e5;
    color: white;
}
</style>