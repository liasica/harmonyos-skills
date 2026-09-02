---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-72
title: 已发布模块如何本地调试
breadcrumb: FAQ > DevEco Studio > 应用调试 > 已发布模块如何本地调试
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ff979f9388c9d79910a077960896e591c5fcca5be6459fece15ad3a8288ef7c4
---

## 问题现象

模块HAR使用二进制产物编译发布，项目中使用ohpm的方法引用，在主项目中如何对这个模块进行Debug调试。

## 解决方案

二进制产物不支持本地调试，可以引入源码工程，对源码工程进行调试，按以下步骤配置：

1. 在根目录build-profile.json5文件声明本地har模块，可以将本地的HAR模块集成到当前项目中。

   ```json
   "modules": [
     {
       "name": "entry",
       "srcPath": "./entry",
       "targets": [
         {
           "name": "default",
           "applyToProducts": [
             "default"
           ]
         }
       ]
     },
     {
       "name": 'HarLibrary',
       "srcPath": '../HarApplication/HarLibrary'
     }
   ]
   ```
2. 在根目录oh-package.json5中添加overrides，引入本地模块路径，将依赖版本替换为本地版本。

   ```json
   "overrides": {
         'harlibrary': "file:../HarApplication/HarLibrary"
   }
   ```
