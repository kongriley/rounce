<template>
  <div class="container text-lg text-gray-700">
    <div class="flex justify-center items-center pt-32 pb-4">
      <img class="mr-4" src="../static/rounce.png" width="50" height="50">
      <div class="header text-center text-5xl font-bold text-black">
        Rounce
      </div>
    </div>

    <div class="text-center text-2xl text-gray-600 pb-20">
      Global news, delivered.
    </div>

    <div class="text-center pb-4">
      Enter a news site to translate and summarize:
    </div>

    <form class="w-full" @submit.prevent="submitArticle">
      <div class="flex justify-center pb-16 z-10">
        <div class="inline-flex items-center border-2 text-gray-400 divide-x rounded w-1/2">
          <input
            v-model="article"
            class="px-4 w-full h-full focus:outline-none focus:text-gray-600"
            placeholder="Input a specific article URL"
          >
          <button type="submit" class="px-3 py-2 focus:outline-none z-0 rounded" :class="{'bg-green-400': article, 'text-white': article}">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              width="24"
              height="24"
            >
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
          </button>
        </div>
      </div>
    </form>


  </div>
</template>

<script>
export default {
  data () {
    return {
      article: ''
    }
  },
  methods: {
    submitArticle: function() {
      if (this.article) {
        this.$store.commit('setUrl', this.article)
        this.$router.push({
          path: '/article'
        })
      }
    }
  }
}
</script>
