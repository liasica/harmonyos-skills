---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-56
title: 静态共享包HAR如何引用另一个HAR包中的so文件
breadcrumb: FAQ > DevEco Studio > 编译构建 > 静态共享包HAR如何引用另一个HAR包中的so文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:13c993684f9d97322d793f02bc133e9e76efbf35519f1fed5e6106f09ab05a6a
---

可以将so库导出并放置在libs目录下，然后在CMakeLists.txt中添加以下代码，将libnativeSub.so添加到har包中。

```text
target_link_directories(entry PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../../../libs/${OHOS_ARCH}/)
target_link_libraries(entry PUBLIC libace_napi.z.so libc++.a libnativeSub.so)
```
