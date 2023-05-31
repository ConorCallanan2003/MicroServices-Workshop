import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from './components/home.vue';
import AddProduct from './components/add_product.vue';

Vue.use(VueRouter);

const routes = [

  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/add_product',
    name: 'AddProduct',
    component: AddProduct
  }
];

const router = new VueRouter(
  {
    mode: 'history',
    routes
  }
);

export default router;
