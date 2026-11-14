---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-permission-application
title: 受限ACL权限申请
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 开发准备 > 受限ACL权限申请
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:31+08:00
doc_updated_at: 2026-10-26
content_hash: sha256:20df37f28cefb4237c7ccdb8b0981624df44eca2f3dd42c3f006cbca32559bdb
---

调用Screen Time Guard Kit相关能力之前，需要确保已获取ACL权限："ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"，该权限允许应用调用屏幕时间守护相关接口，进行屏幕使用限制、应用访问控制、管控使用时间等操作。具体申请和配置过程如下。

**说明** 

该权限申请入口目前仅对企业开发者开放，个人开发者不可见。

1. 在 [申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)和[发布Profile文件](../app/agc-help-release-profile-0000002248341090.md)之前，需要[申请相应的ACL权限](../app/agc-help-apply-acl-0000002394212138.md)。
2. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“开发与服务”，在项目列表中找到对应的项目，并点击选择您需要申请ACL权限的应用。在“项目设置”页面，选择“ACL权限”页签，开始为应用申请ACL权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/l0t_pFzeSrqgJrILr9af9A/zh-cn_image_0000002817427673.png?HW-CC-KV=V1&HW-CC-Date=20261114T004831Z&HW-CC-Expire=31536000000&HW-CC-Sign=298B42D3A928FFEC5294CFA851BC9E6BFB1E7568DD6B737FB38DFF44B12DF879)
3. 在核对注意事项后，在“未获取权限”区域中勾选“我已知晓”。在权限搜索框中输入"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"，查找并勾选权限，提交申请。
4. 根据实际业务需求填写使用场景并提交，审批时间为3个工作日。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/fa9Mk3RcTraih7YAMjfT-Q/zh-cn_image_0000002788468254.png?HW-CC-KV=V1&HW-CC-Date=20261114T004831Z&HW-CC-Expire=31536000000&HW-CC-Sign=841196A0E7EF365A91CBE6327A28273CC8B611516E5457A6345EED3968D6F0F4)
5. 权限申请通过后，在申请profile文件时，在“申请权限”栏选中“受限ACL权限（HarmonyOS API9及以上）”选项，点击“查看”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/filKp4ggRAONcG1CbirFqA/zh-cn_image_0000002817507743.png?HW-CC-KV=V1&HW-CC-Date=20261114T004831Z&HW-CC-Expire=31536000000&HW-CC-Sign=D50CF04D7E383AC0E5AD826518C504A36060B744AE0C7B2B7ADFA6AB85865A10)
6. 在弹出的“选择受限ACL权限”窗口可以看到已申请的权限，勾选后点击确定。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/eQVqPoxfQ-ajPX5-tlelKA/zh-cn_image_0000002788308312.png?HW-CC-KV=V1&HW-CC-Date=20261114T004831Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D710D99805D17054D60EA481770B98E82822DB5D281F9E3EAD8FAB879BF582A)
7. 选择权限后点击“添加”生成新的Profile文件，下载后按[手动配置签名信息](ide-signing-manual.md)替换profile文件。
8. 在工程中entry模块的module.json5文件中添加"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"权限，如下所示：

   ```json5
   "requestPermissions": [{
     "name": "ohos.permission.MANAGE_SCREEN_TIME_GUARD"
   }]
   ```
