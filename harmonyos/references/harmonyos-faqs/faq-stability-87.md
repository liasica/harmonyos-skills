---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-87
title: 如何获取应用打印的hilog日志到本地查看
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 如何获取应用打印的hilog日志到本地查看
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5777fdda79c2dec55a05d833a8de8796ed4ba83fc5d75e9fdc22019856753d29
---

## 问题现象

hilog日志如何导出到本地？

## 解决方案

hilog日志导出到本地有2种方案：

1. hdc shell hilog > 导出的文件地址。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/HRQlY1CwTB6PHN6rypwKqw/zh-cn_image_0000002628554934.png?HW-CC-KV=V1&HW-CC-Date=20261112T233142Z&HW-CC-Expire=31536000000&HW-CC-Sign=051C859D9D891CE88F1399775E07E4448F302FF0F88D8FBADBF3FE6383A244FE "点击放大")
2. 通过hdc file recv /data/log/hilog获取。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/KRMZ3tjsSemabqJGj3X5jw/zh-cn_image_0000002628395034.png?HW-CC-KV=V1&HW-CC-Date=20261112T233142Z&HW-CC-Expire=31536000000&HW-CC-Sign=C08216154D5FF6A420EB20285AD9AFE9B0F8D23EDD34D98AC9070822EBD43891 "点击放大")
