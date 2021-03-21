<template>
  <div>
    <parse-load ref="load"/>

    <form class="w-full" @submit.prevent="submitArticle">
      <div class="flex justify-center pt-16 pb-12 z-10">
        <div class="inline-flex items-center border-2 text-gray-400 divide-x rounded w-1/2">
          <input
            v-model="url"
            class="px-4 w-full h-full focus:outline-none focus:text-gray-600"
            placeholder="Input a specific article URL"
          >
          <button type="submit" class="px-3 py-2 focus:outline-none z-0 rounded bg-green-400 text-white">
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

    <div class="flex justify-center pb-6" v-if="$store.state.parsed">
      <div class="w-3/4">
        <div class="text-2xl font-semibold text-center pb-2">
          {{ $store.state.title }}
        </div>
        <div class="text-xl text-gray-600 text-center pb-8" v-if="$store.state.trans_title">
          {{ $store.state.trans_title }}
        </div>
        <div class="text-lg">
          {{ $store.state.summary }}
        </div>
      </div>
    </div>

    <div class="flex justify-center">
      <div class="inline-flex border rounded">
        <NuxtLink
          to="/"
          class="px-3 py-2 rounded cursor-pointer select-none bg-blue-400 text-white"
        >
          Return to home
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script>
import ParseLoad from '../../components/ParseLoad.vue'
export default {
  components: { ParseLoad },
  data () {
    return {
      url: this.$store.state.url
    }
  },
  methods: {
    submitArticle: function() {
      if (this.url) {
        this.$store.commit('setUrl', this.url)
        this.$router.push({
          path: '/article'
        })
      }
    }
  },
  mounted () {
    this.$store.dispatch('parse').then(() => {
      this.$refs.load.finish()
    }).catch((err) => {
      this.$refs.load.throwErr(err.message)
    })
  }
}
</script>

<style>

</style>