---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-22
title: C/C++项目三方依赖库未打包到HAP
breadcrumb: FAQ > DevEco Studio > 编译构建 > C/C++项目三方依赖库未打包到HAP
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9eaf0263521955e51abf919f4193477120b3daf95d289702e897c5d0d6dff8fa
---

**问题现象**

C/C++项目依赖三方so时，在打包生成HAP后，发现三方so未打包到HAP中。

**解决措施**

当前DevEco Studio对C/C++项目中第三方so文件的寻址方式存在限制。如果第三方so文件未打包到HAP中，请尝试修改so文件的引入方式。

1. 定义一个别名，例如jsbind\_shared\_lib\_tracing，代表将要引入的三方so。
2. 使用SHARED IMPORT将三方so动态引入。
3. 使用IMPORTED\_LOCATION定义引入的so文件位置。
4. 将定义的三方so声明给目标。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/xwfaM8LfROm6ytsrOmTKxg/zh-cn_image_0000002194318404.png?HW-CC-KV=V1&HW-CC-Date=20260428T002913Z&HW-CC-Expire=86400&HW-CC-Sign=D8A0FA7AAE5772E2F6D671F0196891780FE500DD011EAA7B3739C9A051BD670A)
5. 再次打包生成HAP，确认三方so已打包到HAP中。
