<template>
  <div>
    <ul class="image-list">
      <li class="image-item" v-for="image in images" :key="image.id">
        <hr />
        <img :src="image.image" :alt="image.description" />
        <p class="description">{{ image.description }}</p>
        <p>Добавлено: {{ convertDateTime(image.created_at) }}</p>
        <button @click="deleteImage(image.id)">Удалить</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    images: {
      type: Array,
      required: true,
    },
    deleteImage: {
      type: Function,
      required: true,
    },
  },
  methods: {
    convertDateTime(utcDateTime) {
      const date = new Date(utcDateTime)
      return date.toLocaleString()
    }
  },
};
</script>

<style scoped>
.image-list {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.image-item {
  margin: 10px;
  text-align: center;
}

img {
  max-width: 90%;
  height: auto;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 5px;
  margin-top: 40px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  text-align: center;
  margin-bottom: 20px;
}

.description {
  overflow-wrap: anywhere;
}

hr {
  border: 0;
  height: 1px;
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #333, rgba(0, 0, 0, 0));
  margin: 20px auto;
  width: 100%;
}
</style>