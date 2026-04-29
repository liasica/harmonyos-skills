---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-43
title: 如何正确地在CMakeLists.txt文件中配置头文件搜索路径
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何正确地在CMakeLists.txt文件中配置头文件搜索路径
category: harmonyos-faqs
scraped_at: 2026-04-29T14:15:53+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:d9971aaf82b4b1b06dc256b9e1e0c3b40b8ba4a598e1c1ec24717fc98bf239a0
---

请按照以下示例进行配置：

**例1****：**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/D1kFeN-dRRueSgRfe_O3Kw/zh-cn_image_0000002199836868.png?HW-CC-KV=V1&HW-CC-Date=20260429T061553Z&HW-CC-Expire=86400&HW-CC-Sign=0801B230363487B45422EFDE61D6D384868FFFF4F89078E8D9F5A450B8926EEC)

CMakeLists.txt配置头文件搜索路径：

include\_directories(${NATIVERENDER\_ROOT\_PATH}/include)

cpp文件中引用头文件:

#include 'test.h'

**例2****：**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/ssJBD40TS6CkpEGfz8wOGw/zh-cn_image_0000002234797125.png?HW-CC-KV=V1&HW-CC-Date=20260429T061553Z&HW-CC-Expire=86400&HW-CC-Sign=EAE5DAE271C273223F7E5E56A61602079ED13602D0961278294BF9A21241DD2D)

CMakeLists.txt配置头文件搜索路径：

include\_directories(${NATIVERENDER\_ROOT\_PATH})

cpp文件中引用头文件:

#include 'include/test/test.h'

**例3：**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/AkwtuVQJSXSBGzuBMIE2Uw/zh-cn_image_0000002234956969.png?HW-CC-KV=V1&HW-CC-Date=20260429T061553Z&HW-CC-Expire=86400&HW-CC-Sign=DAB3B7CD675732E22FC49106ECC2F32E1D5BCDE37822892280FA1030795BD0A8)

CMakeLists.txt配置头文件搜索路径：

include\_directories(${NATIVERENDER\_ROOT\_PATH}/include)

cpp文件中引用头文件:

#include 'test/test.h'

**例4:**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/SnW-dOWhS7GIiXYGXgyWxA/zh-cn_image_0000002199996680.png?HW-CC-KV=V1&HW-CC-Date=20260429T061553Z&HW-CC-Expire=86400&HW-CC-Sign=C933815C1737304B05EFCEE3B8A3609DFBB637527A7EED6D6DD01F2E2BB9D8FD)

CMakeLists.txt配置头文件搜索路径:

include\_directories(${NATIVERENDER\_ROOT\_PATH}/include/test)

cpp文件中引用头文件:

#include 'test.h'
