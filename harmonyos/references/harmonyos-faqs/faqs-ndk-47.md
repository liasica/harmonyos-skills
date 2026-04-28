---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-47
title: Native侧如何打印char指针
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何打印char指针
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c66f950672738528287b294499b996b84077269a9d87c0de1e70d40e717fc5ff
---

引入hilog库后直接打印。打印时需要加{public}。

OH\_LOG\_INFO(LOG\_APP, “%{public}s”,path); //可正常打印

OH\_LOG\_INFO(LOG\_APP, “%s”,path); //不可正常打印

示例代码如下：

```
1. char *path = "abc";
2. OH_LOG_INFO(LOG_APP, "path: %{public}s", path);
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/napi_init.cpp#L12-L13)
