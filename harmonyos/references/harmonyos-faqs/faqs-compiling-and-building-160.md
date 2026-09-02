---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-160
title: 编译报错“CMake task execution failed”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“CMake task execution failed”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f0317155f589118a491874d941803dcf1487b8e4957ae93bb3d238fd04352115
---

**错误描述**

CMake任务执行时提示“CMake task execution failed”错误信息。

**可能原因**

需要手动删除 .cxx 目录，并在 build-profile.json5 文件的 arguments 字段中添加 “--version” 参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/i_v94r97SLuqEifM-TW9Hw/zh-cn_image_0000002229604133.png)

**解决措施**

移除arguments字段中的“--version”参数。
