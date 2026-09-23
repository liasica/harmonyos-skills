---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-permission-application
title: 受限ACL权限申请
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 开发准备 > 受限ACL权限申请
category: harmonyos-guides
scraped_at: 2026-09-24T06:50:51+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:b65f5179f5a2d4641ee46f2f32de81c0f049ede0a99409e36fb76b296f89ae34
---

调用Screen Time Guard Kit相关能力之前，需要检查是否已经获取"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"权限。该权限允许应用调用屏幕时间守护相关接口，进行屏幕使用限制、应用访问控制、管控使用时间等操作。该权限为受限ACL权限，需要特别配置和申请，具体操作步骤如下所示。

1. 在 [申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)和[发布Profile文件](../app/agc-help-release-profile-0000002248341090.md)之前，需要[申请相应的ACL权限](../app/agc-help-apply-acl-0000002394212138.md)。
2. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“开发与服务”，在项目列表中找到对应的项目，并点击选择您需要申请ACL权限的应用。在“项目设置”页面，选择“ACL权限”页签，开始为应用申请ACL权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/7T1yvfSbRa2FSf2AU2Rj9g/zh-cn_image_0000002739732272.png)
3. 在核对注意事项后，在“未获取权限”区域中勾选“我已知晓”。在权限搜索框中输入"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"，查找并勾选权限，提交申请。
4. 根据实际业务需求填写使用场景并提交，审批时间为3个工作日。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/SrsmqG5ZRTmHvFwIJcyQ5Q/zh-cn_image_0000002769331621.png)
5. 权限申请通过后，在申请profile文件时，在“申请权限”栏选中“受限ACL权限（HarmonyOS API9及以上）”选项，点击“查看”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/jQ5PQ9pdToW-cY-pZCfPLA/zh-cn_image_0000002769451483.png)
6. 在弹出的“选择受限ACL权限”窗口可以看到已申请的权限，勾选后点击确定。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/9yG5yksKQz-5FtneJTZVdQ/zh-cn_image_0000002739892152.png)
7. 选择权限后点击“添加”生成新的Profile文件，下载后按[手动配置签名信息](ide-signing-manual.md)替换profile文件。
8. 在工程中entry模块的module.json5文件中添加"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"权限，如下所示：

   ```json5
   "requestPermissions": [{
     "name": "ohos.permission.MANAGE_SCREEN_TIME_GUARD"
   }]
   ```
