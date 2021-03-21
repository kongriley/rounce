<template>
  <div>
    <transition name="fade">
      <div class="flex justify-center align-center items-center text-center loading-page pb-32" v-if="display">
        <span v-if="error" class="text-red-600"> {{ errorMsg }} </span>
        <svg
        class="mr-8"
        :class="{ 'hidden': !loading, 'animate-spin' : loading }"
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        fill="currentColor"
        viewBox="0 0 16 16"
        v-if="!error">
          <path fill-rule="evenodd" d="M8 3a5 5 0 1 0 4.546 2.914.5.5 0 0 1 .908-.417A6 6 0 1 1 8 2v1z"/>
          <path d="M8 4.466V.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384L8.41 4.658A.25.25 0 0 1 8 4.466z"/>
        </svg>
        <span v-if="!error">
          {{ loadText }}
        </span>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  data: () => ({
    error: false,
    errorMsg: '',

    loading: true,
    display: true,
    loadText: 'Parsing...'
  }),
  methods: {
    start () {
      this.loading = true
      this.display = true
    },
    finish () {
      this.loadText = 'Complete!'
      this.loading = false
      setTimeout(() => {
        this.display = false
      }, 500)
    },
    throwErr (msg) {
      this.error = true
      this.errorMsg = msg
    }
  }
}
</script>

<style scoped>
  .fade-enter, .fade-leave-active {
    transition: opacity .25s ease-out;
  }

  .fade-enter, .fade-leave-active /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0%;
  }

  .loading-page {
    position: fixed;
    z-index: 100;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 1.0);
    font-size: 30px;
  }
</style>
