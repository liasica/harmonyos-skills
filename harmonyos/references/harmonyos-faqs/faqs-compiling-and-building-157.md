---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-157
title: 编译报错“Unrecognized archive format in parameterFile”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Unrecognized archive format in parameterFile”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f309335fdfb57d71e2e9b69612df81a1afef1066eeb06caef62e800038b22f4e
---

**错误描述**

parameterFile中包含无法识别的格式。

**可能原因**

使用parameterFile参数化配置的本地依赖既不是目录，也不是.har或.tgz文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/lMTRVGSmTam2Tx1cikKhiQ/zh-cn_image_0000002194318392.png?HW-CC-KV=V1&HW-CC-Date=20260428T002941Z&HW-CC-Expire=86400&HW-CC-Sign=9CDD1057F491BB6742796D31069E5238F9743A98496B06E1B0339BE1E27F07A2)

**解决措施**

将本地依赖修改为模块目录或模块编译后的har/tgz文件。
