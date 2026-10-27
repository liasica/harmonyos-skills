---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-123
title: "如何解决编译报错“Error: cJSON_Parse failed, please check the JSON file.”的问题"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“Error: cJSON_Parse failed, please check the JSON file.”的问题"
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:b2142f665be7c14434f55579b5b3bba71ad4a5c104c015f1d69ec3a83bce170e
---

**问题现象**

编译错误：“Error: cJSON\\_Parse failed”。请检查JSON文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/tTa4W1gCSrOJ8Nb-fCjD7Q/zh-cn_image_0000002654797961.png "点击放大")

**报错原因**

module.json 文件格式不正确。

**常见场景**

1. JSON文件末尾有多余的逗号。

2. 根标签不是大括号{}。

**解决方案**

检查报错指向的 JSON 文件格式，例如末尾是否有多余的逗号，根标签是否为大括号 {}。
