<script>
export default {
  props: {
    id: String,
    name: String,
    description: String,
    price: Number,
    image: String
  },
}
</script>

<template>
  <body>
    <div class="grid">
      <article style="padding-top: 16px !important;">
        <h3 style="margin: 0px !important;">{{ name }}</h3>
        <p style="margin:0px !important;">{{ description }}</p>
        <p style="margin:0px !important;">{{ image }}</p>
        <footer style="padding: 10px; margin-top: 0px;">Price: €{{ price }}</footer>
      </article>
    </div>
  </body>
</template>

<style src="../css/pico.min.css">
</style>

