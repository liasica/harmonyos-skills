---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-18
title: entry引用本地library时，没有ASan日志输出
breadcrumb: FAQ > DevEco Studio > 应用调试 > entry引用本地library时，没有ASan日志输出
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0082232c32d3f59bddcab77a3cf5d0cb3dc7105249f233000417b53d25553b6c
---

**问题现象**

entry引用本地library时，已经勾选ASan选择项，没有ASan日志输出。

**解决措施**

引用本地C++ library时，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_ASAN=ON”，表示以ASan模式编译so文件。

```
1. {
2. // ...
3. "arguments": "-DOHOS_ENABLE_ASAN=ON",
4. // ...
5. }
6. },
7. // ...
8. }
```

[build-profile.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Ndk/ndk1/Modulea/build-profile.json5#L3-L47)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/Ko2neRETSCiVirrrCRYVbw/zh-cn_image_0000002194318360.png)
