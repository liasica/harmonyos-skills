---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-87
title: 如何获取应用打印的hilog日志到本地查看
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 如何获取应用打印的hilog日志到本地查看
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b316dacbffe042df7de82fdfc35e93bd1242325d45f6c431dd846d62e8a2abb1
---

## 问题现象

hilog日志如何导出到本地？

## 解决方案

hilog日志导出到本地有2种方案：

1. hdc shell hilog > 导出的文件地址。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/nspNT5myRb2ECJ5NydBkTQ/zh-cn_image_0000002628554934.png "点击放大")
2. 通过hdc file recv /data/log/hilog获取。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/0zkPWsENSnW4lnMLtR2ykg/zh-cn_image_0000002628395034.png "点击放大")
