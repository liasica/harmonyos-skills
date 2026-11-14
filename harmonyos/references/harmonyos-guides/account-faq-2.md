---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-2
title: 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:10+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:cc035745151ad53de69132d44bca6f6559a59f2dc43fd855c959e960d3d5450e
---

**问题现象**

调用接口报错1001502014 应用未申请scopes或permissions权限。

**可能原因**

1. 没有申请对应的账号权限。
2. 权限申请成功后，最迟会在25小时后生效。
3. 使用[获取风险等级](account-get-risklevel-introduction.md)能力，但未申请获取风险等级权限。

**解决措施**

1. 申请对应权限，请见[申请账号权限](account-config-permissions.md)章节。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/hD6Jjp1BRRmwYRXUAvw1LA/zh-cn_image_0000002788307862.png?HW-CC-KV=V1&HW-CC-Date=20261114T004810Z&HW-CC-Expire=31536000000&HW-CC-Sign=B442DCC01AC78FB589B1552F6A49DF797E2056EFACF11C889D2201740980AB19)
2. 权限申请通过后，您可通过修改应用工程 > app.json5中的versionCode触发权限生效。

   **图1** 修改前

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/qZDkOb16S_6C_Qo3tUIlyg/zh-cn_image_0000002788467806.png?HW-CC-KV=V1&HW-CC-Date=20261114T004810Z&HW-CC-Expire=31536000000&HW-CC-Sign=CAA088FA92DCFA9F8E4FEF03C5C1142C61D3D8862F139BF73CB6654A972EB2A1)

   **图2** 修改后

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/LFFEfk0CSB2DB0nUdtb9iA/zh-cn_image_0000002817507295.png?HW-CC-KV=V1&HW-CC-Date=20261114T004810Z&HW-CC-Expire=31536000000&HW-CC-Sign=F600B2F4AF7CC769DA0BC93F3AA4794C51DF06B996FF1974FFE691F27F1149C8)
3. 确认是否需要使用获取风险等级能力，如需使用，请参考[获取风险等级](account-get-risklevel-introduction.md)申请对应权限。
