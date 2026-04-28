---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-78
title: har包的libc++版本与工程不一致时，程序如何兼容
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > har包的libc++版本与工程不一致时，程序如何兼容
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9665b6e621e4545b622d757bd9a6dd18fb427c791540c7e93849f09e0dbddfe4
---

**问题现象**

har包的libc++和工程的libc++版本不一致的情况是隔离的吗？还是不能共存，只能使用一个？

**解决措施**

对于har包：

如果其ohpm版本为1.5及以上，当项目同时依赖了某个三方库的不同版本时。ohpm将选择其中的最高版本进行安装。可参考[resolve\_conflict](../harmonyos-guides/ide-ohpmrc.md#section368717475562)。

对于sdk：

SDK中是否导入libc++库由各SDK打包时决定。不同SDK中可能存在不同版本的libc++库。使用时可指定链接对应的libc++库。

使用set(CMAKE\_CXX\_STANDARD xxx)指定版本。具体可参考[如何修改代码工程所支持的C++语言版本](faqs-ndk-9.md)。
