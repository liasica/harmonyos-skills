---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-157
title: 编译报错“Unrecognized archive format in parameterFile”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Unrecognized archive format in parameterFile”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:86fcc0fe5f02b3c6941462bc9a3acfa534010882d88459a47a61ddb17e745fa2
---

**错误描述**

parameterFile中包含无法识别的格式。

**可能原因**

使用parameterFile参数化配置的本地依赖既不是目录，也不是.har或.tgz文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/lMTRVGSmTam2Tx1cikKhiQ/zh-cn_image_0000002194318392.png)

**解决措施**

将本地依赖修改为模块目录或模块编译后的har/tgz文件。
