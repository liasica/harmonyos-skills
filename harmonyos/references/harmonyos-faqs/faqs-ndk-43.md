---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-43
title: 如何正确地在CMakeLists.txt文件中配置头文件搜索路径
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何正确地在CMakeLists.txt文件中配置头文件搜索路径
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:2e7aff94c416fabc4026c8aa24bc3df3657d054f8f4340ffe6fd2cb5f1b6e686
---

请按照以下示例进行配置：

**例1****：**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/ZD_6m9VRQpKuy1ncEMjpbA/zh-cn_image_0000002654835209.png?HW-CC-KV=V1&HW-CC-Date=20261112T233214Z&HW-CC-Expire=31536000000&HW-CC-Sign=D73E4B9DE4CF1C5540C10A6CD5955DA430C982B0C9BE28189EC69C6B067C58D0)

CMakeLists.txt配置头文件搜索路径：

include\_directories(${NATIVERENDER\_ROOT\_PATH}/include)

cpp文件中引用头文件:

#include 'test.h'

**例2****：**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/YQWMO5yyQY2Qf_tiZU7xJg/zh-cn_image_0000002654795275.png?HW-CC-KV=V1&HW-CC-Date=20261112T233214Z&HW-CC-Expire=31536000000&HW-CC-Sign=DDE5A8CA4E2EF806AB874089CF563D61692B59DDF7D9CD89E739B0680A3BC5D1)

CMakeLists.txt配置头文件搜索路径：

include\_directories(${NATIVERENDER\_ROOT\_PATH})

cpp文件中引用头文件:

#include 'include/test/test.h'

**例3：**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Xg8ZYJ4HQKG4hDhYX4jKtg/zh-cn_image_0000002624635808.png?HW-CC-KV=V1&HW-CC-Date=20261112T233214Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A68624FB3D8A679BB22866A7B568C3435F7A71C6B2893265BD95F896677E30A)

CMakeLists.txt配置头文件搜索路径：

include\_directories(${NATIVERENDER\_ROOT\_PATH}/include)

cpp文件中引用头文件:

#include 'test/test.h'

**例4:**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/ojYbNuT9RTO-fBNmdoDbnA/zh-cn_image_0000002624475906.png?HW-CC-KV=V1&HW-CC-Date=20261112T233214Z&HW-CC-Expire=31536000000&HW-CC-Sign=0BF65E22A7449F5800FBE7A9BD90DE79B1E076DF8EC10533040E62BECEEC3096)

CMakeLists.txt配置头文件搜索路径:

include\_directories(${NATIVERENDER\_ROOT\_PATH}/include/test)

cpp文件中引用头文件:

#include 'test.h'
