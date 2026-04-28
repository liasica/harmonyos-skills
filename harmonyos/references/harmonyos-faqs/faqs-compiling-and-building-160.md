---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-160
title: 编译报错“CMake task execution failed”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“CMake task execution failed”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:871f0aa71dbc3f7ed2e2968142825ac2196b0848202ed3b40ee4aca375bf3e2b
---

**错误描述**

CMake任务执行时提示“CMake task execution failed”错误信息。

**可能原因**

需要手动删除 .cxx 目录，并在 build-profile.json5 文件的 arguments 字段中添加 “--version” 参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/i_v94r97SLuqEifM-TW9Hw/zh-cn_image_0000002229604133.png?HW-CC-KV=V1&HW-CC-Date=20260428T002942Z&HW-CC-Expire=86400&HW-CC-Sign=EDDA89A6488C3925BE7D8DF8002BFEF125F295FAAE4267C86DA34B8F56093E10)

**解决措施**

移除arguments字段中的“--version”参数。
