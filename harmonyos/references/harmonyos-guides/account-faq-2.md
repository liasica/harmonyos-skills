---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-2
title: 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3f6a03cc0e7166cdabfef13cb11582c54c5fdd3a002a3106bb817ec5e3bd6be3
---

**问题现象**

调用接口报错1001502014 应用未申请scopes或permissions权限。

**可能原因**

1. 没有申请对应的账号权限。
2. 权限申请成功后，最迟会在25小时后生效。
3. 使用[获取风险等级](account-get-risklevel-introduction.md)能力，但未申请获取风险等级权限。

**解决措施**

1. 申请对应权限，请见[申请账号权限](account-config-permissions.md)章节。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/6IL6dIULTR-gfF4UgjWamw/zh-cn_image_0000002558765242.png?HW-CC-KV=V1&HW-CC-Date=20260429T053656Z&HW-CC-Expire=86400&HW-CC-Sign=C3A43B29BFFE89F3594334AC187A311700B2C7E1A4261959F05F0B8B35213426)
2. 权限申请通过后，您可通过修改应用工程 > app.json5中的versionCode触发权限生效。

   **图1** 修改前

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/JUeBZ1A7THG591--OKfhoA/zh-cn_image_0000002589325113.png?HW-CC-KV=V1&HW-CC-Date=20260429T053656Z&HW-CC-Expire=86400&HW-CC-Sign=917C28D617080C463A1C45056843D54C71735A530C31EA2425FDD7B6CB8C9E2D)

   **图2** 修改后

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/Chr485GlQZiMPpO5QfBJHw/zh-cn_image_0000002589245049.png?HW-CC-KV=V1&HW-CC-Date=20260429T053656Z&HW-CC-Expire=86400&HW-CC-Sign=A5953A6D5591F5DB16486D063E8F1BE2F221FFA0FF020ADDF6D99A3E97DD85BE)
3. 确认是否需要使用获取风险等级能力，如需使用，请参考[获取风险等级](account-get-risklevel-introduction.md)申请对应权限。
