---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-permission-application
title: 受限ACL权限申请
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 开发准备 > 受限ACL权限申请
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:12+08:00
doc_updated_at: 2026-10-26
content_hash: sha256:0716d84b3d4cd80b7ba4bf033ccb37a5c97d9b1ed4f4d3e7aacb1abea988b28b
---

调用Screen Time Guard Kit相关能力之前，需要确保已获取ACL权限："ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"，该权限允许应用调用屏幕时间守护相关接口，进行屏幕使用限制、应用访问控制、管控使用时间等操作。具体申请和配置过程如下。

**说明** 

该权限申请入口目前仅对企业开发者开放，个人开发者不可见。

1. 在 [申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)和[发布Profile文件](../app/agc-help-release-profile-0000002248341090.md)之前，需要[申请相应的ACL权限](../app/agc-help-apply-acl-0000002394212138.md)。
2. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“开发与服务”，在项目列表中找到对应的项目，并点击选择您需要申请ACL权限的应用。在“项目设置”页面，选择“ACL权限”页签，开始为应用申请ACL权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/zbhlH9UPQ0aaw2_PsAIwjw/zh-cn_image_0000002791726612.png?HW-CC-KV=V1&HW-CC-Date=20261119T014818Z&HW-CC-Expire=31536000000&HW-CC-Sign=9520B9CAF84B263D7E1BDB4C6DE721A0CA734C9F6EE1A79587EDCD18ECCB2EA7)
3. 在核对注意事项后，在“未获取权限”区域中勾选“我已知晓”。在权限搜索框中输入"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"，查找并勾选权限，提交申请。
4. 根据实际业务需求填写使用场景并提交，审批时间为3个工作日。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Y4v9D149RletMPI3jlzt0A/zh-cn_image_0000002791566640.png?HW-CC-KV=V1&HW-CC-Date=20261119T014818Z&HW-CC-Expire=31536000000&HW-CC-Sign=E64F30860CC8C1133EBC2C91BD2FBD41363CB73DFF43F460590CB5A521C63EFE)
5. 权限申请通过后，在申请profile文件时，在“申请权限”栏选中“受限ACL权限（HarmonyOS API9及以上）”选项，点击“查看”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/5S6sQY5GSsyx8rtmCOggVQ/zh-cn_image_0000002820526593.png?HW-CC-KV=V1&HW-CC-Date=20261119T014818Z&HW-CC-Expire=31536000000&HW-CC-Sign=27D98C96731C6C3CA60FAE3D528778295B2D6DA507FD6BFDD40689AD5E0D6D6A)
6. 在弹出的“选择受限ACL权限”窗口可以看到已申请的权限，勾选后点击确定。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/Wkl1bNwZRHC9Z04pK7hvzA/zh-cn_image_0000002820406593.png?HW-CC-KV=V1&HW-CC-Date=20261119T014818Z&HW-CC-Expire=31536000000&HW-CC-Sign=110E764E80602CC1680EDF57364FEAB36133DDE52D8E594000FC5C6F384FC95A)
7. 选择权限后点击“添加”生成新的Profile文件，下载后按[手动配置签名信息](ide-signing-manual.md)替换profile文件。
8. 在工程中entry模块的module.json5文件中添加"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"权限，如下所示：

   ```json5
   "requestPermissions": [{
     "name": "ohos.permission.MANAGE_SCREEN_TIME_GUARD"
   }]
   ```
