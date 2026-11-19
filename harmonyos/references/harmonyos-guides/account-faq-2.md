---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-2
title: 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:50+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:2d3a1a91a49298df51effc8fded263d34e0a06038140373bd299701833c19e95
---

**问题现象**

调用接口报错1001502014 应用未申请scopes或permissions权限。

**可能原因**

1. 没有申请对应的账号权限。
2. 权限申请成功后，最迟会在25小时后生效。
3. 使用[获取风险等级](account-get-risklevel-introduction.md)能力，但未申请获取风险等级权限。

**解决措施**

1. 申请对应权限，请见[申请账号权限](account-config-permissions.md)章节。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/GtlRe4d5RfS1OFK9uz4KpA/zh-cn_image_0000002820406143.png?HW-CC-KV=V1&HW-CC-Date=20261119T014757Z&HW-CC-Expire=31536000000&HW-CC-Sign=5956D865E6911C7454EF4FE6C3F308E25DA2F41C5B67298C7CAA6774FB2947AA)
2. 权限申请通过后，您可通过修改应用工程 > app.json5中的versionCode触发权限生效。

   **图1** 修改前

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/Z7YFJMgUTvCzFc0f81ZEcA/zh-cn_image_0000002791566192.png?HW-CC-KV=V1&HW-CC-Date=20261119T014757Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A3D1705B502DEC7BE57687DB7F134D3AF02C8614D43CB6E4EC4AE09301FD6C7)

   **图2** 修改后

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/5qYfjcJBSjGyy8FWDmIVQQ/zh-cn_image_0000002820526145.png?HW-CC-KV=V1&HW-CC-Date=20261119T014757Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFAEEBCC3E2436761B2E3085673735481A04BA41CF7387C18A642E53E4768F53)
3. 确认是否需要使用获取风险等级能力，如需使用，请参考[获取风险等级](account-get-risklevel-introduction.md)申请对应权限。
