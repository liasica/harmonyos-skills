---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-2
title: 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:177d4530b9e0a70056609428213a5c1d96a754c41fc3ea39085a03a947992939
---

**问题现象**

调用接口报错1001502014 应用未申请scopes或permissions权限。

**可能原因**

1. 没有申请对应的账号权限。
2. 权限申请成功后，最迟会在25小时后生效。
3. 使用[获取风险等级](account-get-risklevel-introduction.md)能力，但未申请获取风险等级权限。

**解决措施**

1. 申请对应权限，请见[申请账号权限](account-config-permissions.md)章节。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/rabor6qCRluGPfBETwnP8g/zh-cn_image_0000002786520058.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=A20D2378708FE0604B81ADD23B3085EA23B01A4E40735B2DCCC1BB2DB2AEE41F)
2. 权限申请通过后，您可通过修改应用工程 > app.json5中的versionCode触发权限生效。

   **图1** 修改前

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/TDn6mPE6Qw-N1-1bRKNHOQ/zh-cn_image_0000002815559551.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE081AAF70459E751FA1D53F0C3FEB8B8B38345DF6C9F99CC6BDAFC9B8FEB93B)

   **图2** 修改后

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/iu47cD4STymA2LPQs3q3Fw/zh-cn_image_0000002815399635.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA72DCEE13D2B28277FCD3AF1C7F9147856409EA47B79E449A9B47AFFD94B116)
3. 确认是否需要使用获取风险等级能力，如需使用，请参考[获取风险等级](account-get-risklevel-introduction.md)申请对应权限。
