---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-157
title: 编译报错“Unrecognized archive format in parameterFile”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Unrecognized archive format in parameterFile”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:bd35c58c1ba21bd47cb5f05d29d68abe2fab92b3ff9514aa2ad846e126d5c9a5
---

**错误描述**

parameterFile中包含无法识别的格式。

**可能原因**

使用parameterFile参数化配置的本地依赖既不是目录，也不是.har或.tgz文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/lMTRVGSmTam2Tx1cikKhiQ/zh-cn_image_0000002194318392.png?HW-CC-KV=V1&HW-CC-Date=20260429T062057Z&HW-CC-Expire=86400&HW-CC-Sign=1CFEC77DF448A8E9B69B448EF01401805ACB06EF32C55B8B25C46C82D9E615C4)

**解决措施**

将本地依赖修改为模块目录或模块编译后的har/tgz文件。
