---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-72
title: 如何获取BuildProfile中的值
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何获取BuildProfile中的值
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b457289625e130fec433c37955175be053b4a07d90ad24d14cc1773a2b2e2279
---

生成 BuildProfile 文件后，可以通过相对路径在代码中引入该文件。例如，在 HAR 模块的 Index.ets 文件中使用该文件：

```
1. import BuildProfile from './BuildProfile';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CompilingAndBuilding/library/Index.ets#L3-L4)

获取 BuildProfile 类中的值：

```
1. const HAR_VERSION: string = BuildProfile.HAR_VERSION;
2. const BUILD_MODE_NAME: string = BuildProfile.BUILD_MODE_NAME;
3. const DEBUG: boolean = BuildProfile.DEBUG;
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CompilingAndBuilding/library/Index.ets#L8-L11)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/RyJwmuxVTYOddqyp5ZzF7w/zh-cn_image_0000002229604169.png?HW-CC-KV=V1&HW-CC-Date=20260429T062036Z&HW-CC-Expire=86400&HW-CC-Sign=362216D085729FD2980A89F8D67B991A4546C405E083F82935A5F793E3DEBF66 "点击放大")

**参考链接**

[HAR运行时获取编译构建参数](../harmonyos-guides/ide-hvigor-get-build-profile-para-guide.md#section68146594553)
