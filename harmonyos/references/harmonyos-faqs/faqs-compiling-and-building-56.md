---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-56
title: 静态共享包HAR如何引用另一个HAR包中的so文件
breadcrumb: FAQ > DevEco Studio > 编译构建 > 静态共享包HAR如何引用另一个HAR包中的so文件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:69c1b545b5fa38cf92b90a9e6c87ee1f3f8a44c1a58509b3dc130fb444fe03d8
---

可以将so库导出并放置在libs目录下，然后在CMakeLists.txt中添加以下代码，将libnativeSub.so添加到har包中。

```
1. target_link_directories(entry PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../../../libs/${OHOS_ARCH}/)
2. target_link_libraries(entry PUBLIC libace_napi.z.so libc++.a libnativeSub.so)
```

[CMakeLists.txt](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/cpp/CMakeLists.txt#L3-L4)
