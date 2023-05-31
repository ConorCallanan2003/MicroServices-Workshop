<template>
  <body>
    <main class="container">
       
        <h1 style="margin-bottom: 10px !important;">Add Product</h1>
      <!--img href="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.syncfusion.com%2Fblogs%2Fpost%2F12-tips-to-make-charts-more-aesthetic.aspx&psig=AOvVaw1aYNiPeo6FKuN8vvsKqnvE&ust=1685614980652000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCNjgiaOrn_8CFQAAAAAdAAAAABAQ"></img-->
      
      <div>
        <label for="name">
          Item Name
          <input type="text" id="name" name="name" placeholder="Item Name" required>
        </label>
        <div class="grid">
          <label for="quantity">
            Item Quantity
            <input type="number" id="quantity" name="quantity" placeholder="Item Quantity" required>
          </label> 
          <label for="price">
            Item Price
            <input type="number" id="price" name="price" placeholder="Item Price" required>
          </label>
        </div>
        <input type="submit">
      </div>
    </main>
  </body>
</template>

<style src="../css/pico.min.css">
</style>

<script>
export default {
  name: "AddProductPage"
}
</script>
