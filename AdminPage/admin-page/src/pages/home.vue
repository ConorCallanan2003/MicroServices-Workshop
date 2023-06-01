<template>
  <body>
   <main class="container max-size">
      <nav>
        <ul>
          <li><strong>Welcome Admin!</strong></li>
        </ul>
        <ul>
          <li>
            <a href="/add_product">Add a Product</a> 
          </li>
          <li>
            <a href="/view_products">View Products</a> 
          </li>
        </ul>
      </nav>
      <router-view></router-view> 
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
