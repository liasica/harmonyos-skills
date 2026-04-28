---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-4
title: HarmonyOS应用自动化签名时提示“Provision number exceeds limit”
breadcrumb: FAQ > DevEco Studio > 应用调试 > HarmonyOS应用自动化签名时提示“Provision number exceeds limit”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:06+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:08b2beb018dcddf548ff388cfdd98fd6bf6c0183501acc0dfa2ce0169dabf749
---

**问题现象**

使用自动化签名功能对HarmonyOS进行签名时，提示“Provision number exceeds limit”信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/8ZLcW0aURtmjsitbsX8IEQ/zh-cn_image_0000002194318424.png?HW-CC-KV=V1&HW-CC-Date=20260428T003004Z&HW-CC-Expire=86400&HW-CC-Sign=0471861D0EC4D5B5EF3938AD79C27AD29FFABE7EC5F9D2415416FEE9A9D82D97)

**解决措施**

AGC（AppGallery Connect）限制了自动化签名的使用次数。同一开发者账号在最近30天内使用自动化签名功能的次数不能超过150次。

可通过如下几种方式进行解决：

* 方法1：建议相同BundleName的应用，如果设备无变化，请使用同一套签名文件信息，不要反复进行重签名操作。
* 方法2：更换其它开发者账号进行登录，然后进行签名。
* 方法3：AGC限制同一个账号在30天内使用自动化签名的次数不超过150次。等待一段时间后，可重新使用该账号签名。
