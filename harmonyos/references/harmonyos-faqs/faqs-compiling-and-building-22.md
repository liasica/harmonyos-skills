---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-22
title: C/C++项目三方依赖库未打包到HAP
breadcrumb: FAQ > DevEco Studio > 编译构建 > C/C++项目三方依赖库未打包到HAP
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:b49588608834aacb3d1e43bc831ad16cd8f6d2a3d66498c5c09e32376afb361e
---

**问题现象**

C/C++项目依赖三方so时，在打包生成HAP后，发现三方so未打包到HAP中。

**解决措施**

当前DevEco Studio对C/C++项目中第三方so文件的寻址方式存在限制。如果第三方so文件未打包到HAP中，请尝试修改so文件的引入方式。

1. 定义一个别名，例如jsbind\_shared\_lib\_tracing，代表将要引入的三方so。
2. 使用SHARED IMPORT将三方so动态引入。
3. 使用IMPORTED\_LOCATION定义引入的so文件位置。
4. 将定义的三方so声明给目标。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/amRHOJKPQKK2DMDtmOEcWw/zh-cn_image_0000002624478492.png)
5. 再次打包生成HAP，确认三方so已打包到HAP中。
