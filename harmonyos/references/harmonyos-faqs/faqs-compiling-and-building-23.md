---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-23
title: Static Library模块中src/main/cpp目录下的文件未打包进HAR
breadcrumb: FAQ > DevEco Studio > 编译构建 > Static Library模块中src/main/cpp目录下的文件未打包进HAR
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:d424512cf2de3e1993f68d06ff0d285a75b6a8081bb7a2891c120d10b55dcc69
---

**问题现象**

点击**Build > Make Module ${libraryName}**编译构建生成HAR后，发现构建产物中未出现cpp目录下的文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/ATwG3vPDTiW2Bx7DreOkvQ/zh-cn_image_0000002654797853.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=00AC92AC610AE82C4E2E89CB82DB80413063E2111DB0E9D29DFCE93960AC0CF5)

**解决措施**

如果使用的Hvigor为2.5.0-s及以上版本，在编译构建HAR的过程中，仅会将dependencies内处于本模块路径下的本地依赖打包进.har文件中，devDependencies里的依赖不会打包进.har文件中。

请将相应的本地依赖移至dependencies中，然后重新编译。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/GCaECPFmQ3K-ziq2AVG82Q/zh-cn_image_0000002624638398.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=04380BB18A8729A51E5D99C6206491523E526A1A46A869F449D09E749938C018)
