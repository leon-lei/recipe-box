<template>
  <b-container fluid>
    <!-- Add new recipe -->
    <b-row class="text-center">
      <b-col sm="12">
        <h1>Recipes</h1>
        <hr>
        <b-alert v-bind:message="message" :show="showMessage">{{ message }}</b-alert>
        <b-button variant="primary" v-b-modal.recipe-modal>
          Add Recipe
        </b-button>
        <b-button variant="primary" v-b-modal.ingredient-modal>
          Add Ingredient
        </b-button>
        <br><br>
        <b-form-input v-model="search" placeholder="Search for recipe"></b-form-input>
        <br><br>
      </b-col>
    </b-row>
    <b-row>
      <b-col sm="4" v-for="recipe in filteredRecipes" v-bind:key="recipe.id">
        <b-card
          style="height: 20rem;"
          class="m-2">
          <b-tabs card>
            <b-tab title="Recipe">
              <b-card-title>{{ `${recipe.name}` }}</b-card-title>
              <b-card-text>Time: {{ `${recipe.minutes}` }} minutes</b-card-text>
                <b-button
                        variant="outline-info"
                        size="sm"
                        v-b-modal.recipe-update-modal
                        @click="editRecipe(recipe)">
                    Update
                </b-button>
                <b-button
                        variant="outline-danger"
                        size="sm"
                        @click="onDeleteRecipe(recipe)">
                    Delete
                </b-button>
            </b-tab>
            <b-tab title="Ingredients">
              <b-card-text>
                <ul id="example-1">
                  <li v-for="ingredient in `${recipe.ingredients}`.split(',') ">
                    {{ ingredient }}
                  </li>
                </ul>

              </b-card-text>
            </b-tab>
            <b-tab title="Instructions">
              <b-card-text>
                {{ `${recipe.instructions}` }}
              </b-card-text>
            </b-tab>
          </b-tabs>
        </b-card>
      </b-col>
    </b-row>
    <!-- Add ingredient modal -->
    <b-modal ref="addIngredientModal"
             id="ingredient-modal"
             title="Add a new ingredient"
             hide-footer>
      <b-form @submit="ingredientSubmit" @reset="ingredientReset" class="w-100">
        <b-form-group id="form-name-group"
                      label="Name:"
                      label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addIngredientForm.name"
                        required
                        placeholder="Egg">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
      </b-modal>
    <!-- Add recipe modal -->
    <b-modal ref="addRecipeModal"
             id="recipe-modal"
             title="Add a new recipe"
             hide-footer>
      <b-form @submit="recipeSubmit" @reset="recipeReset" class="w-100">
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
      <b-form @submit="recipeSubmitUpdate" @reset="recipeResetUpdate" class="w-100">
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
      <b-button type="submit" variant="success">Update</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </b-container>
</template>

<script>
import axios from 'axios';
import Alert from './Alert';

export default {
  data() {
    return {
      ingredients: [],
      recipes: [],
      addIngredientForm: {
        name: '',
      },
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
      search: '',
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
    getIngredients() {
      const path = 'http://localhost:5000/api/ingredients/';
      axios.get(path)
        .then((res) => {
          this.ingredients = res.data.ingredients;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addIngredient(payload) {
      const path = 'http://localhost:5000/api/ingredients/';
      axios.post(path, payload)
        .then(() => {
          this.getIngredients();
          this.message = 'Ingredient added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getIngredients();
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
    created() {
      this.getRecipes();
    },
    editRecipe(recipe) {
      this.editRecipeForm = recipe;
    },
    ingredientInitForm() {
      this.addIngredientForm.name = '';
    },
    ingredientReset(evt) {
      evt.preventDefault();
      this.ingredientInitForm();
    },
    ingredientSubmit(evt) {
      evt.preventDefault();
      this.$refs.addIngredientModal.hide();
      const payload = {
        name: this.addIngredientForm.name,
      };
      this.addIngredient(payload);
      this.ingredientInitForm();
    },
    recipeInitForm() {
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
    recipeReset(evt) {
      evt.preventDefault();
      this.recipeInitForm();
    },
    recipeResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editRecipeModal.hide();
      this.recipeInitForm();
      this.getRecipes();
    },
    recipeSubmit(evt) {
      evt.preventDefault();
      this.$refs.addRecipeModal.hide();
      const payload = {
        name: this.addRecipeForm.name,
        instructions: this.addRecipeForm.instructions,
        ingredients: this.addRecipeForm.ingredients,
        minutes: this.addRecipeForm.minutes,
      };
      this.addRecipe(payload);
      this.recipeInitForm();
    },
    recipeSubmitUpdate(evt) {
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
  computed: {
    filteredRecipes: function () {
      // eslint-disable-next-line
      return this.recipes.filter((recipe) => {
        return recipe.name.toLowerCase().match(this.search, 'i') || recipe.ingredients.toLowerCase().match(this.search, 'i');
      });
    },
  },
};
</script>
