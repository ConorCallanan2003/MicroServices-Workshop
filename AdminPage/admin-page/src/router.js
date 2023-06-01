import { createRouter, createWebHistory } from 'vue-router';

// Import your components
import AddProductPage from './pages/add_product.vue';
import ViewProductPage from './pages/view_products.vue';

const routes = [
  { path: '/add_product', component: AddProductPage },
  { path: '/view_products', component: ViewProductPage }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
