---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-201
title: IDE编译报错Invalid dependency
breadcrumb: FAQ > DevEco Studio > 编译构建 > IDE编译报错Invalid dependency
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ecd9c56c6ea4b1b1acb8f71702c82127282714046bf771febe49c4879b35163e
---

## 问题现象

DevEco Studio编译有以下报错：

```screen
ohpm ERROR: Invalid dependency entry@...\entry -> entry@1.0.0.
ohpm ERROR: Found exception: Error: Invalid dependency, reached retry limit or non retryable error encountered.
// ...
ohpm ERROR: Install failed, detail: Error: Invalid dependency.
```

如何解决？

## 解决方案

源码依赖方式存在“依赖名称不能与其所在的模块名称相同”的校验规则，当出现这种依赖时，ohpm在安装时会报ohpm ERROR: Invalid dependency错误。如题中报错，entry模块依赖了entry@1.0.0。

* **场景一**：该报错可能会发生在远程仓库管理时，在分支代码中该模块错误依赖主干代码中该模块本身的情况。解决方案是找到对应报错的模块，在模块的oh-package.json5的dependencies，devDependencies以及dynamicDependencies中检查是否存在标红报错，并删除这种依赖项。
* **场景二**：如果该依赖项确实存在，解决方案是修改该模块名称，或者在该模块的oh-package.json5中修改该依赖项名称，并找到该依赖项所在模块，用修改模块名称的方法做出相应修改。
* **场景三**：ohpm缓存的问题导致，执行以下命令：

  ```screen
  ohpm cache clean
  ```

  ```screen
  ohpm clean
  ```

  再同步一下工程(File -> Sync and Refresh Project)，最后编译运行即可。
