---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-1
title: 登录华为开发者账号后，提示需要实名认证
breadcrumb: FAQ > DevEco Studio > 应用运行 > 登录华为开发者账号后，提示需要实名认证
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:b00da20a265bf15dd0d2c707929f636ed9f556fd59685396a2847784328a0660
---

**问题现象**

使用本地模拟器时，需用实名认证的开发者账号登录授权。若账号未实名认证，本地模拟器会提示需要实名认证。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/LGVjr4Y0Th6UyRLXEj5UrQ/zh-cn_image_0000002624478746.png "点击放大")

**解决措施**

原因包括以下两种情况：

* 华为账号未实名认证，请开发者按照如下步骤进行处理。
* 刚完成实名认证但认证未生效，开发者可根据步骤4清除浏览器Cookie后重试。

1. 点击上图中的**Verify Identity**，前往开发者联盟实名认证。
2. 根据浏览器界面提示进行实名认证，具体指导可以参考[实名认证介绍](../start/itrna-0000001076878172.md)。个人开发者可以选择银行卡认证或者身份证认证。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/ihEe0wSoSHKHm3IfDGgFdw/zh-cn_image_0000002654798107.png "点击放大")
3. 认证完成后，在DevEco Studio界面，点击右上角个人中心，点击Sign out退出，重新登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/XRcuRuK-T-maTvCyJbTOJw/zh-cn_image_0000002624638656.png)
4. （可选）如果实名认证后重新登录，仍提示需要进行实名认证，可清除浏览器 **Cookie（快捷键 Ctrl+Shift+Del）**后重试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/SPnSj2etQiOHCaiLOGRVWQ/zh-cn_image_0000002654838059.png "点击放大")
