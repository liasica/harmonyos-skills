---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-2
title: 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:16+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:2673de20e2a2371b0c3c0f19e3e7d13a18f60f89734cce465bf82928fe424753
---

**问题现象**

调用接口报错1001502014 应用未申请scopes或permissions权限。

**可能原因**

1. 没有申请对应的账号权限。
2. 权限申请成功后，最迟会在25小时后生效。
3. 使用[获取风险等级](account-get-risklevel-introduction.md)能力，但未申请获取风险等级权限。

**解决措施**

1. 申请对应权限，请见[申请账号权限](account-config-permissions.md)章节。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/IJqXJiJvQuqtzmp-DgY89g/zh-cn_image_0000002792877844.png?HW-CC-KV=V1&HW-CC-Date=20261121T011216Z&HW-CC-Expire=31536000000&HW-CC-Sign=165E5E3DC38FE6014D861F26B36722F0F9E0F096E7B278557962264976C8117F)
2. 权限申请通过后，您可通过修改应用工程 > app.json5中的versionCode触发权限生效。

   **图1** 修改前

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/kxmaFEkQQAOO5ZdvUv1Trg/zh-cn_image_0000002821757753.png?HW-CC-KV=V1&HW-CC-Date=20261121T011216Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5D0963B43B090DA6D07F10E930C67818F3816849A90F4ACA2A5F44B281378DF)

   **图2** 修改后

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/orH2M2M5QXOf1dY-j0JmQg/zh-cn_image_0000002793037816.png?HW-CC-KV=V1&HW-CC-Date=20261121T011216Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C52BCA1462F43D3757DBB68F39E76CB18844832724245A6C8A74AB5FD15BD5B)
3. 确认是否需要使用获取风险等级能力，如需使用，请参考[获取风险等级](account-get-risklevel-introduction.md)申请对应权限。
