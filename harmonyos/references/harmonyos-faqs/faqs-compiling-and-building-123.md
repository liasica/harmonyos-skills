---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-123
title: 如何解决编译报错“Error: cJSON_Parse failed, please check the JSON file.”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“Error: cJSON_Parse failed, please check the JSON file.”的问题
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:47+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0bff314a264e9b98b7c35ef66becd0e72aaf7bf9b5bd95c12786a679d1e13fd5
---

**问题现象**

编译错误：“Error: cJSON\\_Parse failed”。请检查JSON文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/Lm54PnnnTNiGp8-iso3kNQ/zh-cn_image_0000002194158800.png?HW-CC-KV=V1&HW-CC-Date=20260429T062046Z&HW-CC-Expire=86400&HW-CC-Sign=D020CD01E0763F0E6F0CE6035AFE2E25E06BB3D549DC0F65EB2440ABEB7EF85A "点击放大")

**报错原因**

module.json 文件格式不正确。

**常见场景**

1. JSON文件末尾有多余的逗号。

2. 根标签不是大括号{}。

**解决方案**

检查报错指向的 JSON 文件格式，例如末尾是否有多余的逗号，根标签是否为大括号 {}。
