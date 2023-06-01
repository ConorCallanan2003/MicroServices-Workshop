<template>
  <body>
    <main class="container">
        <h1 style="margin-bottom: 10px !important; ">View Products</h1> 
      <div>
        <div class="grid"> 
          <ItemComp v-for="(item, index) in responseData" :key="index" :name="item.name" :price="item.price" :description="item.description" :image="item.image"></ItemComp>
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
  data() {
    return {
      responseData: null
    };
  },
  methods: {
    fetchData() {
      fetch('http://localhost:2222/products')
        .then(response => {
          this.responseData = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  mounted() {
    this.fetchData();
  },
  components: {
    ItemComp
  },
}
</script>
