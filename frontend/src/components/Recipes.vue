<template>
  <div class="container">
    <!-- Add new recipe -->
    <div class="row">
      <div class="col-sm-12">
        <h1>Recipes</h1>
        <hr>
        <alert :message="message" v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.recipe-modal>
          Add Recipe
        </button>
        <br><br>
      </div>
    </div>
    <!-- Recipe cards -->
    <div class="row">
      <div class="card col-sm-3" v-for="recipe in recipes" v-bind:key="recipe.id">
        <div class="card-content">
          <h4 class="name">{{ recipe.name }} - {{ recipe.minutes }}</h4>
          <p class="name">{{ recipe.instructions }}</p>
        </div>
        <button
                type="button"
                class="btn btn-warning btn-sm"
                v-b-modal.recipe-update-modal
                @click="editRecipe(recipe)">
            Update
        </button>
        <button
                type="button"
                class="btn btn-danger btn-sm"
                @click="onDeleteRecipe(recipe)">
            Delete
        </button>
      </div>
    </div>
    <!-- Add recipe modal -->
    <b-modal ref="addRecipeModal"
             id="recipe-modal"
             title="Add a new recipe"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group"
                      label="Name:"
                      label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addRecipeForm.name"
                        required
                        placeholder="Simmered Kabocha">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-ingredients-group"
                      label="Ingredients:"
                      label-for="form-ingredients-input">
          <b-form-input id="form-ingredients-input"
                        type="text"
                        v-model="addRecipeForm.ingredients"
                        required
                        placeholder="dashi, kabocha, mirin, soy sauce, sugar">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-instructions-group"
                      label="Instructions:"
                      label-for="form-instructions-input">
          <b-form-input id="form-instructions-input"
                        type="text"
                        v-model="addRecipeForm.instructions"
                        required
                        placeholder="Mix and cover 1 inch kabocha pieces. Simmer 25 minutes.">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-minutes-group"
                      label="Minutes:"
                      label-for="form-minutes-input">
          <b-form-input id="form-minutes-input"
                          type="int"
                          v-model="addRecipeForm.minutes"
                          required
                          placeholder="35">
          </b-form-input>
        </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <!-- Update recipe modal -->
    <b-modal ref="editRecipeModal"
            id="recipe-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-name-edit-group"
                  label="Name:"
                  label-for="form-name-edit-input">
          <b-form-input id="form-name-edit-input"
                        type="text"
                        v-model="editRecipeForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-ingredients-edit-group"
                  label="Ingredients:"
                  label-for="form-ingredients-edit-input">
          <b-form-input id="form-ingredients-edit-input"
                        type="text"
                        v-model="editRecipeForm.ingredients"
                        required
                        placeholder="Enter ingredients">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-instructions-edit-group"
                  label="Instructions:"
                  label-for="form-instructions-edit-input">
          <b-form-input id="form-instructions-edit-input"
                        type="text"
                        v-model="editRecipeForm.instructions"
                        required
                        placeholder="Enter instructions">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-minutes-edit-group"
                  label="Minutes:"
                  label-for="form-minutes-edit-input">
          <b-form-input id="form-minutes-edit-input"
                        type="text"
                        v-model="editRecipeForm.minutes"
                        required
                        placeholder="Enter minutes">
          </b-form-input>
        </b-form-group>
      <b-button type="submit" variant="primary">Update</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert';

export default {
  data() {
    return {
      recipes: [],
      addRecipeForm: {
        name: '',
        ingredients: '',
        instructions: '',
        minutes: '',
      },
      editRecipeForm: {
        id: '',
        name: '',
        ingredients: '',
        instructions: '',
        minutes: '',
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getRecipes() {
      const path = 'http://localhost:5000/api/recipes/';
      axios.get(path)
        .then((res) => {
          this.recipes = res.data.recipes;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addRecipe(payload) {
      const path = 'http://localhost:5000/api/recipes/';
      axios.post(path, payload)
        .then(() => {
          this.getRecipes();
          this.message = 'Recipe added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getRecipes();
        });
    },
    removeRecipe(recipeID) {
      const path = `http://localhost:5000/api/recipes/${recipeID}`;
      axios.delete(path)
        .then(() => {
          this.getRecipes();
          this.message = 'Recipe deleted!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getRecipes();
        });
    },
    updateRecipe(payload, recipeID) {
      const path = `http://localhost:5000/api/recipes/${recipeID}`;
      axios.put(path, payload)
        .then(() => {
          this.getRecipes();
          this.message = 'Recipe updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getRecipes();
        });
    },
    editRecipe(recipe) {
      this.editRecipeForm = recipe;
    },
    initForm() {
      this.addRecipeForm.name = '';
      this.addRecipeForm.ingredients = '';
      this.addRecipeForm.instructions = '';
      this.addRecipeForm.minutes = '';
      this.editRecipeForm.id = '';
      this.editRecipeForm.name = '';
      this.editRecipeForm.ingredients = '';
      this.editRecipeForm.instructions = '';
      this.editRecipeForm.minutes = '';
    },
    onDeleteRecipe(recipe) {
      this.removeRecipe(recipe.id);
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addRecipeModal.hide();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editRecipeModal.hide();
      this.initForm();
      this.getRecipes();
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addRecipeModal.hide();
      const payload = {
        name: this.addRecipeForm.name,
        instructions: this.addRecipeForm.instructions,
        ingredients: this.addRecipeForm.ingredients,
        minutes: this.addRecipeForm.minutes,
      };
      this.addRecipe(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editRecipeModal.hide();
      const payload = {
        id: this.editRecipeForm.id,
        name: this.editRecipeForm.name,
        instructions: this.editRecipeForm.instructions,
        ingredients: this.editRecipeForm.ingredients,
        minutes: this.editRecipeForm.minutes,
      };
      this.updateRecipe(payload, this.editRecipeForm.id);
    },
  },
  created() {
    this.getRecipes();
  },
};
</script>
