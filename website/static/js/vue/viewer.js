import {template} from "/static/js/vue/viewer.vue.js"

/**
 * Patient & Scan combined viewer
 *
 */

export let viewer = Vue.component('docy-viewer', {
  template: template,
  data: function() {
    return {
      patient: null,
      scan: null
    }
  },

  watch: {
  },

  computed: {
  },

  methods: {
  },
});
