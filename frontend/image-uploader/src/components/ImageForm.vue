<template>
  <div>
    <form class="image-form" @submit.prevent="uploadImage">
      <input
          id="description-input"
          type="text"
          maxlength="255"
          v-model="description"
          placeholder="Введите описание..."
          required
      >
       <label for="fileInput">
        {{ selectedFileName || 'Выбрать файл' }}
      </label>
      <input
        id="fileInput"
        class="file-input"
        type="file"
        @change="handleFileChange"
        accept="image/*"
      />
      <button type="submit">Отправить</button>

      <div class="error-message" v-if="errorMessage">
        {{ errorMessage }}
      </div>

    </form>


  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    fetchImg: {
      type: Function,
      required: true,
    },
  },
  data() {
    return {
      image: null,
      description: "",
      base64Image: null,
      errorMessage: null,
      selectedFileName: null,
    };
  },
  methods: {
    handleFileChange(event) {
      const file = event.target.files[0];

      if (file) {
        const reader = new FileReader();
        this.selectedFileName = file.name;

        reader.onload = (e) => {
          this.base64Image = e.target.result;
        };

        reader.readAsDataURL(file);
      } else {
        this.selectedFileName = null;
        this.base64Image = null;
      }
    },
    uploadImage() {
      if (!this.base64Image) {
        console.error("Изображение не выбрано");
        return;
      }
      axios.post("http://localhost:8000/api/images/", {
        image: this.base64Image,
        description: this.description,
      })
      .then(response => {
        console.log("Изображение успешно загружена", response.data);
        this.resetForm();
        this.fetchImg();
      })
      .catch(error => {
        console.error("Ошибка загрузки изображения", error);
        if (error.response && error.response.data && error.response.data.image) {
          this.errorMessage = error.response.data.image[0];
        } else {
          this.errorMessage = "Произошла ошибка при загрузке изображения";
        }
        this.resetForm()
        this.scheduleErrorMessageReset()
      });
    },
    resetForm() {
      this.image = null;
      this.description = "";
      this.base64Image = null;
      this.selectedFileName = null;
      document.getElementById("fileInput").value = null;
    },
    scheduleErrorMessageReset() {
      setTimeout(() => {
        this.errorMessage = null;
      }, 4000);
    }
  },
};
</script>

<style scoped>
.image-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
  margin-top: 30px;
  position: relative;
}

.error-message {
  position: absolute;
  bottom: -40px;
  width: 100%;
  display: flex;
  justify-content: center;
  color: red;
  margin: 10px auto;
  text-align: center;
}

.file-input {
  display: none;
}

#description-input {
  width: 90%;
  max-width: 500px;
  padding: 10px;
  margin-top: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-sizing: border-box;
  box-shadow: 0 0 20px lightgray;
}

#description-input:focus {
  border-color: transparent;
  outline: none;
}

</style>