<template>
  <body>
    <main class="container">
        <h1 style="margin-bottom: 10px !important; ">View Products</h1> 
      <div>
        <div class="grid">
          <ItemComp name="iPhone" price="100" description="Great product" image="🍾"></ItemComp>
          <ItemComp name="iPhone" price="100" description="Great product" image="🍾"></ItemComp>
          <ItemComp name="iPhone" price="100" description="Great product" image="🍾"></ItemComp>
          <ItemComp name="iPhone" price="100" description="Great product" image="🍾"></ItemComp>
          <ItemComp name="iPhone" price="100" description="Great product" image="🍾"></ItemComp>
        </div>
      </div>
    </main>
  </body>
</template>

<style src="../css/pico.min.css">
</style>

<script>
import ItemComp from '../components/ItemComp.vue';
export default {
  name: "ViewProductsPage",
  components: {
    ItemComp
  },
}
</script>
