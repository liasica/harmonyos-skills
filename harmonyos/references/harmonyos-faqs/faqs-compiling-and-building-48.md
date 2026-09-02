---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-48
title: 如何配置oh-package.json5动态依赖
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何配置oh-package.json5动态依赖
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7abfbef6a9643b8847c830598698fb77c30adbe8624508bba33c7eb736d1da20
---

oh-package.json5文件中：

* dependencies（生产依赖）：声明生产依赖，即代码中需要导入的HarmonyOS三方库，用于编译和运行阶段。
* devDependencies（开发依赖）：用于项目的开发或测试阶段。
* dynamicDependencies（动态依赖）：配置用于动态加载的HSP模块。

示例如下：

```json
{
  "name": "parameter-test",
  "version": "@param:version",
  "modelVersion": "5.0.4",
  "description": "test desc.",
  "main": "index.ets",
  "author": "test author",
  "license": "ISC",
  "dependencies": {
    "libtest1": "@param:dependencies.libtest1"
  },
  "devDependencies": {
    "libtest2": "@param:devDependencies.libtest2"
  },
  "dynamicDependencies": {
    "libtest3": "@param:dynamicDependencies.libtest3"
  },
  "parameterFile": '.parameterFile/parameterFile.json5',// Enable parameterization and specify the path to the parameterized configuration file
}
```

**参考链接**

[oh-package.json5文件](../harmonyos-guides/ide-oh-package-json5.md)，[添加依赖项](../harmonyos-guides/ide-hvigor-dependencies.md)
