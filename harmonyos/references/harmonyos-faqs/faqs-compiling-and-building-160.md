---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-160
title: 编译报错“CMake task execution failed”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“CMake task execution failed”
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:608f3525b2b7888e0c853d6cc015abaecdbf7ceaba4caca8c55141d7816c4165
---

**错误描述**

CMake任务执行时提示“CMake task execution failed”错误信息。

**可能原因**

需要手动删除 .cxx 目录，并在 build-profile.json5 文件的 arguments 字段中添加 “--version” 参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/a5pWeaxaQL-l8wNIRztscw/zh-cn_image_0000002654837953.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=366C16D27E6E964A218A197D8FC37216D2B3EDF0871C2EC645CD937C8305B576)

**解决措施**

移除arguments字段中的“--version”参数。
