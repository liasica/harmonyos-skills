---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-2
title: 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:01+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:fcde8aaa231c8806f28bc1f548a4a799e4414652fb182c8fa0fc5004fa9e1ae2
---

**问题现象**

调用接口报错1001502014 应用未申请scopes或permissions权限。

**可能原因**

1. 没有申请对应的账号权限。
2. 权限申请成功后，最迟会在25小时后生效。
3. 使用[获取风险等级](account-get-risklevel-introduction.md)能力，但未申请获取风险等级权限。

**解决措施**

1. 申请对应权限，请见[申请账号权限](account-config-permissions.md)章节。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/-oPIA6fZSWungdaCR06pbw/zh-cn_image_0000002712244998.png)
2. 权限申请通过后，您可通过修改应用工程 > app.json5中的versionCode触发权限生效。

   **图1** 修改前

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/mqgh0BeSTsSk-OvKSdGiCg/zh-cn_image_0000002712404958.png)

   **图2** 修改后

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/eckKWnNWR_KGwDZaADTh6Q/zh-cn_image_0000002742123907.png)
3. 确认是否需要使用获取风险等级能力，如需使用，请参考[获取风险等级](account-get-risklevel-introduction.md)申请对应权限。
