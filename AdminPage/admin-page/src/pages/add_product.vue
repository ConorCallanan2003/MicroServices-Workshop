<template>
  <body>
    <main class="container"> 
      <h1 style="margin-bottom: 10px !important;">Add Product</h1>
      <div> 
          <div class="grid">
            <label for="name">
              Item Name
              <input type="text" id="name" name="name" placeholder="Item Name" required>
            </label>
            <label for="image">
              Image (Emoji)
              <input type="text" id="image" name="image" placeholder="🏞️" required>
            </label>
          </div>
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
          <button @click="submitProduct">Submit</button>
      </div>
    </main>
  </body>
</template>

<style src="../css/pico.min.css">
</style>

<script>
export default {
  name: "AddProductPage",
  methods:  { 
    submitProduct() { 
      const nameField = document.getElementById('name');
      const imageField = document.getElementById('image');
      const quantityField = document.getElementById('quantity');
      const priceField = document.getElementById('name');
      const url = 'http://localhost:2222/products';
      const data = {
        name: nameField.value,
        image: imageField.value,
        quantity: quantityField.value,
        price: priceField.value
      };

      fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
        .then(response => response.json())
        .then(result => { 
          console.log(result);
        })
        .catch(error => {
          console.error('Error:', error);
        });
    }
  }
}
</script>
