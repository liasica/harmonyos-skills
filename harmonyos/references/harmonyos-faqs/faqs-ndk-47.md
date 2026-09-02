---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-47
title: Native侧如何打印char指针
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何打印char指针
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:49434dcf6afc6aba39d9c9d7f4dab3b19af3ff42022ab41dcde17407845ccfdb
---

引入hilog库后直接打印。打印时需要加{public}。

OH\_LOG\_INFO(LOG\_APP, “%{public}s”,path); //可正常打印

OH\_LOG\_INFO(LOG\_APP, “%s”,path); //不可正常打印

示例代码如下：

```cpp
char *path = "abc";
OH_LOG_INFO(LOG_APP, "path: %{public}s", path);
```
