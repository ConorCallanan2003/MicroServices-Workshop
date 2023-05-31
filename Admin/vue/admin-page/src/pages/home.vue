<template>
  <body>
   <main class="container">
      <div class="container">
        <h1>Welcome Admin!</h1>
        <button @click="navigateToAddProduct">Add a Product</button> 
        <button @click="navigateToViewProducts">View Products</button> 
        <router-view></router-view>
      </div>
    </main>
  </body>
</template>

<style src="../css/pico.min.css" ref="stylesheet">

</style>

<script>
export default {
  name: "HomePage",
  methods: {
    navigateToAddProduct() {
      this.$router.push('/add_product');
    },
    navigateToViewProducts() {
      this.$router.push('/view_products')
    }
  }
}
</script>
