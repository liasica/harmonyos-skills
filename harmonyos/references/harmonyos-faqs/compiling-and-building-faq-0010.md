---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0010
title: C/C++项目三方so库未打包入HAP问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > C/C++项目三方so库未打包入HAP问题排查
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:39+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:11b81bcc3cdb3f8f1ea465772112992a753490a4d19527aac169cc15250081b5
---

**Q：C/C++项目依赖三方so时，在打包生成HAP后，发现三方so未打包到HAP中，如何解决？**

**A**：当前DevEco Studio对C/C++项目中第三方so文件的寻址方式存在限制。如果第三方so文件未打包到HAP中，请尝试修改so文件的引入方式。

1. 定义一个别名，例如jsbind\_shared\_lib\_tracing，代表将要引入的三方so。
2. 使用SHARED IMPORT将三方so动态引入。
3. 使用IMPORTED\_LOCATION定义引入的so文件位置。
4. 将定义的三方so声明给目标。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/finqhHgoTUeP98yfaVMjgQ/zh-cn_image_0000002794546783.png "点击放大")
5. 再次打包生成HAP，确认三方so已打包到HAP中。
