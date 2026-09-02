---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-31
title: "编译报错“ninja: error: mkdir(xxx): No such file or directory”"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 编译报错“ninja: error: mkdir(xxx): No such file or directory”"
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:ab39c01a87ddb1e015afc166a032866faa9ab32862afec1aeab5fc3d3b269071
---

**问题现象**

Native工程编译时出现以下告警和报错信息。

出现工程目录长度超过250字符的告警，示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/GvGhjz7wRZGqpkDE6gRhCw/zh-cn_image_0000002624638402.png "点击放大")

出现编译错误“ninja: error: mkdir(xxx): No such file or directory”。示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/zDMprlvfRy-es_NfXzqFbw/zh-cn_image_0000002654837811.png "点击放大")

**解决措施**

CMAKE\_OBJECT\_PATH\_MAX默认值为250，如果工程中object file的实际路径长度超出该值，将导致编译错误。

开发者需在工程的CMakeLists.txt文件中，根据object file实际路径长度设置CMAKE\_OBJECT\_PATH\_MAX的大小，具体方法如下：

* 方法一： 在CMAKE\_OBJECT\_PATH\_MAX默认值基础上增加一个文件名长度即可。

  示例中的告警文件为TextMeasureCache.cpp.obj，长度为24字符。在默认值250的基础上增加24，即设置set(CMAKE\_OBJECT\_PATH\_MAX 274)。
* 方法二：根据对象文件的实际路径长度计算CMAKE\_OBJECT\_PATH\_MAX的大小。

  计算公式：CMAKE\_OBJECT\_PATH\_MAX = 总路径长度 - object file目录长度 + 32（CMake哈希值字符数）

  + 总路径长度为 object file directory 长度与 object file 长度之和。object file directory 和 object file 如下图所示，两个长度之和为 297 个字符，具体以实际为准。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/fJyyTt1fRNi5Y-n5pvQkqg/zh-cn_image_0000002624478500.png "点击放大")
  + object file中目录部分长度：示例中“\_\_/\_\_/\_\_/\_\_/\_\_/third-party/rn/ReactCommon/react/renderer/textlayoutmanager”长度为74字符，具体以实际为准。
  + CMake哈希值字符数：CMake将长路径转换为哈希值时，哈希值的长度固定为32。

  代入示例中的长度后，计算可得：CMAKE\_OBJECT\_PATH\_MAX = 297 - 74 + 32 = 255。设置 CMAKE\_OBJECT\_PATH\_MAX 为 255。
