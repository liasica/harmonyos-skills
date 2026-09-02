---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-72
title: 如何获取BuildProfile中的值
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何获取BuildProfile中的值
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:54ae8081154a45a7ee3f851d37568258cb9845b5584524cca45760e90dba2e6e
---

生成 BuildProfile 文件后，可以通过相对路径在代码中引入该文件。例如，在 HAR 模块的 Index.ets 文件中使用该文件：

```typescript
import BuildProfile from './BuildProfile';
```

获取 BuildProfile 类中的值：

```typescript
const HAR_VERSION: string = BuildProfile.HAR_VERSION;
const BUILD_MODE_NAME: string = BuildProfile.BUILD_MODE_NAME;
const DEBUG: boolean = BuildProfile.DEBUG;
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/GGJ8CP4WQCCVhinXlWNFRA/zh-cn_image_0000002654837847.png "点击放大")

**参考链接**

[HAR运行时获取编译构建参数](../harmonyos-guides/ide-hvigor-get-build-profile-para-guide.md#section68146594553)
