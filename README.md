# rounce

> **rounce** /ræuns/
>
> *n. (printing)* The handle by which the bed of a hand press is run under the printing mechanism to produce printed material.

## Inspiration
With the advent of the Internet and the Information Age, it has become important to stay connected with our increasingly globalized world. However, it is difficult to stay on top of current events around the world, as much foreign news is only available in foreign languages. Adequate understanding of foreign material involves manually translating articles and comprehending often mangled text, takes mass time and effort for readers. There is no easy way to tailor one's news feed to accommodate the wealth of information in foreign languages. Therefore, people are left with little information of what is happening around the world.

## Our solution
Rounce is an **easy-to-use, concise, and informative** global news summarizer. We leverage the power of Transformer models with abstractive summarization and translation to perform cross-lingual summarization. Given a specific article URL, it will simultaneously summarize that article and translate it into English, as needed. In just one click, Rounce will quickly display the most relevant information, in English, for the convenience of users.

## How we built it
We used a pipeline-based model, incorporating models from both extractive and abstractive summarization techniques. By using the Edmundson model, an extractive summarization model that ranks all sentences by informativeness, top sentences are then fed to a Transformer-based combined abstractive summarization and translation model. This allows for effective and fast CLS on a variety of target languages and articles. 

The entire backend model runs on a Flask app, and the Rounce frontend is displayed using Nuxt.js, incorporating CSS, JS, and HTML.

## What's next for Rounce
I would like to expand Rounce by including more features, such as allowing the parsing of RSS or Atom feeds to summarize batch articles at once.

## Build Setup

```bash
# install dependencies
$ yarn install

# serve with hot reload at localhost:3000
$ yarn dev

# build for production and launch server
$ yarn build
$ yarn start

# generate static project
$ yarn generate
```

For detailed explanation on how things work, check out [Nuxt.js docs](https://nuxtjs.org).
