<template>
  <div id="app">
    <ImageForm :fetchImg="fetchImages"/>
    <ImageList :images="images" :deleteImage="deleteImage" />
  </div>
</template>

<script>
import axios from "axios";
import ImageForm from "@/components/ImageForm.vue";
import ImageList from "@/components/ImageList.vue";

export default {
  components: {
    ImageForm,
    ImageList,
  },
  data() {
    return {
      images: [],
    };
  },
  methods: {
    fetchImages() {
      axios.get("http://localhost:8000/api/images/")
        .then((response) => {
          this.images = response.data;
        })
        .catch((error) => {
          console.error("Ошибка при получении изображений:", error);
        });
    },
    deleteImage(imageId) {
      axios.delete(`http://localhost:8000/api/images/${imageId}/`)
        .then(() => {
          this.fetchImages();
        })
        .catch((error) => {
          console.error("Ошибка при удалении изображения:", error);
        });
    },

  },
  created() {
    this.fetchImages();
  },
};
</script>

<style>
app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

button, label {
  margin-top: 15px;
  cursor: pointer;
  padding: 10px 15px;
  font-size: 16px;
  color: #fff;
  background-color: #007bff;
  border: 1px solid #007bff;
  border-radius: 4px;
  transition: 0.2s;
}

button:hover, label:hover {
  scale: 1.05;
  box-shadow: 0 0 15px grey;
}

</style>
