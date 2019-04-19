import Vue from 'vue';
import Router from 'vue-router';
import Recipes from '@/components/Recipes';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/recipes/',
      name: 'Recipes',
      component: Recipes,
    },
  ],
  mode: 'history',
});
