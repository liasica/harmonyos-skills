---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-4
title: HarmonyOS应用自动化签名时提示“Provision number exceeds limit”
breadcrumb: FAQ > DevEco Studio > 应用调试 > HarmonyOS应用自动化签名时提示“Provision number exceeds limit”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:bce088015755568c35c76ebb0eb21d6870614fe4b4bd0b588b0e7e442837a68d
---

**问题现象**

使用自动化签名功能对HarmonyOS进行签名时，提示“Provision number exceeds limit”信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/UeySE-d3T5aw6PLJtmBJMw/zh-cn_image_0000002654838095.png)

**解决措施**

AGC（AppGallery Connect）限制了自动化签名的使用次数。同一开发者账号在最近30天内使用自动化签名功能的次数不能超过150次。可使用手动签名方案，详情参考[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)。

如需继续使用自动签名，可通过如下几种方式进行解决：

* 方法1：建议相同BundleName的应用，如果设备无变化，请使用同一套签名文件信息，不要反复进行重签名操作。
* 方法2：更换其它开发者账号进行登录，然后进行签名。
* 方法3：AGC限制同一个账号在30天内使用自动化签名的次数不超过150次。AGC平台的次数限制是基于最近30天滚动计算的。您可以等待一段时间（例如几天），让部分早期的签名记录超出30天范围，从而使可用次数恢复，再重新使用原账号进行签名。
