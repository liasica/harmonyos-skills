---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-43
title: 如何正确地在CMakeLists.txt文件中配置头文件搜索路径
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何正确地在CMakeLists.txt文件中配置头文件搜索路径
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:37+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:3ec14508b9ba907ca3e5d116262c9d8b7ebbd7c70d832aa254c032d55563403f
---

请按照以下示例进行配置：

**例1****：**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/D1kFeN-dRRueSgRfe_O3Kw/zh-cn_image_0000002199836868.png?HW-CC-KV=V1&HW-CC-Date=20260428T002436Z&HW-CC-Expire=86400&HW-CC-Sign=F09A732FED3E84DC78B4DE27E54D36B4E533544713890868882E1A6F55C210FD)

CMakeLists.txt配置头文件搜索路径：

include\_directories(${NATIVERENDER\_ROOT\_PATH}/include)

cpp文件中引用头文件:

#include 'test.h'

**例2****：**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/ssJBD40TS6CkpEGfz8wOGw/zh-cn_image_0000002234797125.png?HW-CC-KV=V1&HW-CC-Date=20260428T002436Z&HW-CC-Expire=86400&HW-CC-Sign=489098655DDA76101E573FE039D8DF9435B87389276BC6C448746EE1FE588C1F)

CMakeLists.txt配置头文件搜索路径：

include\_directories(${NATIVERENDER\_ROOT\_PATH})

cpp文件中引用头文件:

#include 'include/test/test.h'

**例3：**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/AkwtuVQJSXSBGzuBMIE2Uw/zh-cn_image_0000002234956969.png?HW-CC-KV=V1&HW-CC-Date=20260428T002436Z&HW-CC-Expire=86400&HW-CC-Sign=1C31BE37B87D59B873095A257FD29237CBF9A907C02EC673D840B76D1FE0B754)

CMakeLists.txt配置头文件搜索路径：

include\_directories(${NATIVERENDER\_ROOT\_PATH}/include)

cpp文件中引用头文件:

#include 'test/test.h'

**例4:**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/SnW-dOWhS7GIiXYGXgyWxA/zh-cn_image_0000002199996680.png?HW-CC-KV=V1&HW-CC-Date=20260428T002436Z&HW-CC-Expire=86400&HW-CC-Sign=033B02CF1302227F1448EC5C352B331A0D21AACDECDC1D1C0BDE40E390C047D3)

CMakeLists.txt配置头文件搜索路径:

include\_directories(${NATIVERENDER\_ROOT\_PATH}/include/test)

cpp文件中引用头文件:

#include 'test.h'
