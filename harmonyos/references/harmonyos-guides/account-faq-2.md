---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-2
title: 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fefbfa5de4641f8d7204e22449335cb194b03f64119298963e391996c31a60d9
---

**问题现象**

调用接口报错1001502014 应用未申请scopes或permissions权限。

**可能原因**

1. 没有申请对应的账号权限。
2. 权限申请成功后，最迟会在25小时后生效。
3. 使用[获取风险等级](account-get-risklevel-introduction.md)能力，但未申请获取风险等级权限。

**解决措施**

1. 申请对应权限，请见[申请账号权限](account-config-permissions.md)章节。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/bihy5neYTn6UTO2pEnEqvQ/zh-cn_image_0000002552958742.png?HW-CC-KV=V1&HW-CC-Date=20260427T234804Z&HW-CC-Expire=86400&HW-CC-Sign=B15E865685AA2C605EBAA2EB72C6DB5955F234096630065A141056069517385F)
2. 权限申请通过后，您可通过修改应用工程 > app.json5中的versionCode触发权限生效。

   **图1** 修改前

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/pAq5XEW3QjyWinvjwhInqQ/zh-cn_image_0000002552799094.png?HW-CC-KV=V1&HW-CC-Date=20260427T234804Z&HW-CC-Expire=86400&HW-CC-Sign=FA14FA61C2E9E9B9EFEAD3AD0751ED9DD344A1B5B7C0384CF1185B87C0383242)

   **图2** 修改后

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/4o8zz6Q6TPm3extnmUJvCQ/zh-cn_image_0000002583438789.png?HW-CC-KV=V1&HW-CC-Date=20260427T234804Z&HW-CC-Expire=86400&HW-CC-Sign=9377B1B26EC0FE33ECEBAB31B7AC27453A80709E98ABC0FC758E6CB68804C083)
3. 确认是否需要使用获取风险等级能力，如需使用，请参考[获取风险等级](account-get-risklevel-introduction.md)申请对应权限。
