<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10"
        <h1>Recipes</h1>
        <hr><br><br>
        <alert :message="message" v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.recipe-modal>Add Recipe</button>
        <br><br>
      </div>  
    </div>
    <b-modal ref="addRecipeModal"
            id="recipe-modal"
            title="Add a new recipe"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group"
                    label="Name:"
                    label-for="form-name-input">
            <b-form-input id="form-name-input"\
                        type="text"
                        v-model="addRecipeForm.name"
                        required
                        placeholder="Enter Name">
            </b-form-input>
        </b-form-group>
        <b-form-group id="form-ingredients-group"
                    label="Ingredients:"
                    label-for="form-ingredients-input">
            <b-form-input id="form-ingredients-input"\
                        type="text"
                        v-model="addRecipeForm.ingredients"
                        required
                        placeholder="Enter Ingredients">
            </b-form-input>
        </b-form-group>
        <b-form-group id="form-instructions-group"
                    label="Instructions:"
                    label-for="form-instructions-input">
            <b-form-input id="form-instructions-input"\
                        type="text"
                        v-model="addRecipeForm.instructions"
                        required
                        placeholder="Enter Instructions">
            </b-form-input>
        </b-form-group>
        <b-form-group id="form-minutes-group"
                    label="Minutes:"
                    label-for="form-minutes-input">
            <b-form-input id="form-minutes-input"\
                        type="int"
                        v-model="addRecipeForm.minutes"
                        placeholder="Enter Minutes">
            </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
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
      message: '',
      showMessage: false,
      editRecipeForm: {
        id: '',
        name: '',
        ingredients: '',
        instructions: '',
        minutes: '',
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getRecipes() {
      const path = 'http://localhost:5000';
      axios.get(path)
        .then((res) => {
          this.recipes = res.data.recipes;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addRecipe(recipeID) {
      const path = 'http://localhost:5000/recipes/new';
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
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addRecipeModal.hide();
      this.initForm();
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
    }
  },
  created() {
    this.getRecipes();
  },
};
</script>
