---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-31
title: 编译报错“ninja: error: mkdir(xxx): No such file or directory”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“ninja: error: mkdir(xxx): No such file or directory”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:13+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:56427def192d5fec47284b76454e68ccddd8f42650d47b1e5dc353702f07a8ad
---

**问题现象**

Native工程编译时出现以下告警和报错信息。

出现工程目录长度超过250字符的告警，示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/YzgwcoibRTmQCro1ygkjlA/zh-cn_image_0000002229604401.png?HW-CC-KV=V1&HW-CC-Date=20260428T002912Z&HW-CC-Expire=86400&HW-CC-Sign=722217E9EF5174F20E847B11C3EBB3D83F5F4DAD9820EC7BBC6AFAB1CDFD4BB3 "点击放大")

出现编译错误“ninja: error: mkdir(xxx): No such file or directory”。示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/e3zR2d9RSFWpVIqe0FXLeQ/zh-cn_image_0000002229758889.png?HW-CC-KV=V1&HW-CC-Date=20260428T002912Z&HW-CC-Expire=86400&HW-CC-Sign=793063E0E17AFB8A068E33A7AC035864435B60864B8C8BCA787409C768E73BCF "点击放大")

**解决措施**

CMAKE\_OBJECT\_PATH\_MAX默认值为250，如果工程中object file的实际路径长度超出该值，将导致编译错误。

开发者需在工程的CMakeLists.txt文件中，根据object file实际路径长度设置CMAKE\_OBJECT\_PATH\_MAX的大小，具体方法如下：

* 方法一： 在CMAKE\_OBJECT\_PATH\_MAX默认值基础上增加一个文件名长度即可。

  示例中的告警文件为TextMeasureCache.cpp.obj，长度为24字符。在默认值250的基础上增加24，即设置set(CMAKE\_OBJECT\_PATH\_MAX 274)。
* 方法二：根据对象文件的实际路径长度计算CMAKE\_OBJECT\_PATH\_MAX的大小。

  计算公式：CMAKE\_OBJECT\_PATH\_MAX = 总路径长度 - object file目录长度 + 32（CMake哈希值字符数）

  + 总路径长度为 object file directory 长度与 object file 长度之和。object file directory 和 object file 如下图所示，两个长度之和为 297 个字符，具体以实际为准。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/ARq_rygnSf6NaNSdypolAQ/zh-cn_image_0000002194318624.png?HW-CC-KV=V1&HW-CC-Date=20260428T002912Z&HW-CC-Expire=86400&HW-CC-Sign=20957129E8450C2B2F413A85BC4B8D9E65EC17EF70A5C1292631138D02DC8E10 "点击放大")
  + object file中目录部分长度：示例中“\_\_/\_\_/\_\_/\_\_/\_\_/third-party/rn/ReactCommon/react/renderer/textlayoutmanager”长度为74字符，具体以实际为准。
  + CMake哈希值字符数：CMake将长路径转换为哈希值时，哈希值的长度固定为32。

  代入示例中的长度后，计算可得：CMAKE\_OBJECT\_PATH\_MAX = 297 - 74 + 32 = 255。设置 CMAKE\_OBJECT\_PATH\_MAX 为 255。
