---
layout: post
title: Github Action google-protobuf 오류
date: 2024-01-15 21:51 +0900
categories:
  - ETC
  - Problem
tags: 
math: true
---

## 오류:


Github Actions에 다음과 같은 오류가 났다:

![](https://i.imgur.com/K6npfCb.png)


```shell
An error occurred while installing google-protobuf (3.25.2), and Bundler cannot
continue.

In Gemfile:
  jekyll-theme-chirpy was resolved to 5.6.1, which depends on
    jekyll-archives was resolved to 2.2.1, which depends on
      jekyll was resolved to 4.3.3, which depends on
        jekyll-sass-converter was resolved to 3.0.0, which depends on
          sass-embedded was resolved to 1.69.7, which depends on
            google-protobuf
Error: The process '/opt/hostedtoolcache/Ruby/3.3.0/x64/bin/bundle' failed with exit code 5
```



## 해결 방법:

ruby 버전과 호환이 안되서 발생하는 오류다.

.github/workflows/pages-deploy.yml 에서

ruby version을 3 에서 3.2로 변경해주자 해결되었다


```yml
jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v3
        with:
          fetch-depth: 0
          # submodules: true
          # If using the 'assets' git submodule from Chirpy Starter, uncomment above
          # (See: https://github.com/cotes2020/chirpy-starter/tree/main/assets)

      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v3

      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: 3.2   # reads from a '.ruby-version' or '.tools-version' file if 'ruby-version' is omitted
          bundler-cache: true

```


![](https://i.imgur.com/AvImp0M.png)

짠 다시 잘 되는것을 확인할 수 있다