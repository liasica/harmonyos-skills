---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-23
title: Static Library模块中src/main/cpp目录下的文件未打包进HAR
breadcrumb: FAQ > DevEco Studio > 编译构建 > Static Library模块中src/main/cpp目录下的文件未打包进HAR
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:089d83c20683c6c9f0abf763c138b697317fddb0e8e71633ae174080a42aac2a
---

**问题现象**

点击**Build > Make Module ${libraryName}**编译构建生成HAR后，发现构建产物中未出现cpp目录下的文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/39NaJGLBSG6xlHfSjl3TYQ/zh-cn_image_0000002229758217.png?HW-CC-KV=V1&HW-CC-Date=20260429T062025Z&HW-CC-Expire=86400&HW-CC-Sign=BC48608A16555E06AE23806EB9012E1250C9DFE8074965F18BA7BA2E5BE57DE5)

**解决措施**

如果使用的Hvigor为2.5.0-s及以上版本，在编译构建HAR的过程中，仅会将dependencies内处于本模块路径下的本地依赖打包进.har文件中，devDependencies里的依赖不会打包进.har文件中。

请将相应的本地依赖移至dependencies中，然后重新编译。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/oKM4-hmaR5mv1nC0XhMEOQ/zh-cn_image_0000002229603749.png?HW-CC-KV=V1&HW-CC-Date=20260429T062025Z&HW-CC-Expire=86400&HW-CC-Sign=4489F7AC601795AC870CF082F3DCC691C598AE26AA1880F324810245F06FEF55)
