---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-160
title: 编译报错“CMake task execution failed”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“CMake task execution failed”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:155890fb36de7b03be66b7af3aa7f59903c36222f8539bf5bc182ef78e484780
---

**错误描述**

CMake任务执行时提示“CMake task execution failed”错误信息。

**可能原因**

需要手动删除 .cxx 目录，并在 build-profile.json5 文件的 arguments 字段中添加 “--version” 参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/i_v94r97SLuqEifM-TW9Hw/zh-cn_image_0000002229604133.png?HW-CC-KV=V1&HW-CC-Date=20260429T062058Z&HW-CC-Expire=86400&HW-CC-Sign=37F7A53DBE55116B0C936846A1680CCF812BB832AB6C2770A07343FC2626C100)

**解决措施**

移除arguments字段中的“--version”参数。
