---
layout: post
title: Github Publisher
date: 2024-03-09 18:20 +0900
categories:
  - 대분류
  - 소분류
tags: []
math: true
---

## Intro: 

tag test



처음부터 테스트

Internal Link test

[[_posts/2024-03-09-Obsidian to Notion 자동화|2024-03-09-Obsidian to Notion 자동화]]

[[_posts/2024-03-05-RAG 우리가 절대 쉽게 결과물을 얻을 수 없는 이유 노트|2024-03-05-RAG 우리가 절대 쉽게 결과물을 얻을 수 없는 이유 노트]]



https://alexoliveira.cc/guide/jekyll-with-obsidian




```yml
{
  "githubRepo": "blog",
  "githubName": "kurko",
  "GhToken": "ghp_[REDACTED]",
  "githubBranch": "main",
  "shareKey": "share",
  "ExcludedFolder": "",
  "fileMenu": true,
  "editorMenu": true,
  "downloadedFolder": "fixed",
  "folderDefaultName": "obsidian",
  "yamlFolderKey": "",
  "rootFolder": "",
  "workflowName": "",
  "embedImage": true,
  "defaultImageFolder": "images/obsidian",
  "autoCleanUp": true,
  "autoCleanUpExcluded": "",
  "folderNote": false,
  "convertWikiLinks": true,
  "convertForGithub": true,
  "subFolder": "",
  "embedNotes": false,
  "copyLink": false,
  "mainLink": "",
  "linkRemover": "",
  "hardBreak": false,
  "logNotice": false,
  "convertDataview": true,
  "useFrontmatterTitle": true,
  "censorText": [
    {
      "entry": "(?<!\\`)\\[(.*?)\\]\\((?!(http|\\/*image|obsidian\\/image))(\\.\\/)*(.+?)(\\.md)*\\)",
      "replace": "[$1]({% link obsidian/$4.md %})"
    },
    {
      "entry": "(?<!\\`)\\[(.*?)\\]\\(((obsidian\\/)?image)(.+)\\)",
      "replace": "[$1](/image$4)"
    }
  ],
  "inlineTags": false,
  "dataviewFields": [],
  "excludeDataviewValue": [],
  "metadataFileFields": [
    "obsidian"
  ],
  "frontmatterTitleKey": "filename",
  "shareExternalModified": false
}
```