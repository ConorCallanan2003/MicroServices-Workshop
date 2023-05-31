import { createRouter, createWebHistory } from 'vue-router';

// Import your components
import HomePage from './pages/home.vue';
import AddProductPage from './pages/add_product.vue';
import ViewProductPage from './pages/view_products.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/add_product', component: AddProductPage },
  { path: '/view_products', component: ViewProductPage }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
