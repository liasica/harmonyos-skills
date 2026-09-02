---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-permission-application
title: 受限ACL权限申请
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 开发准备 > 受限ACL权限申请
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1f350d556a74832d058896b9af3e2bb5cc78621054f29301f5d47b0f8c4c95f1
---

1. 在 [申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)和[发布Profile文件](../app/agc-help-release-profile-0000002248341090.md)之前，需要[申请相应的ACL权限](../app/agc-help-apply-acl-0000002394212138.md)。
2. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“开发与服务”，在项目列表中找到对应的项目，并点击选择您需要申请ACL权限的应用。在“项目设置”页面，选择“ACL权限”页签，开始为应用申请ACL权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/H6NsG15LRumLmDu4OmeCeQ/zh-cn_image_0000002589325533.png)
3. 在核对注意事项后，在“未获取权限”区域中勾选“我已知晓”。在权限搜索框中输入"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"，查找并勾选权限，提交申请。
4. 根据实际业务需求填写申请原因并提交，提交后将在1个工作日回复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/zJeXjw_iRiCZb2ljYlclAw/zh-cn_image_0000002589245471.png)
5. 权限申请通过后，在申请profile文件时，在“申请权限”栏选中“受限ACL权限（HarmonyOS API9及以上）”选项，点击“选择”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/wpfxBTGQTp2YI_qSVwZewA/zh-cn_image_0000002558765664.png)
6. 在弹出的“选择受限ACL权限”窗口可以看到已申请的权限，勾选后点击确定。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/btbbpu4TQWuYKqLp_p-iQg/zh-cn_image_0000002558606008.png)
7. 选择权限后点击“添加”生成新的Profile文件，下载后按[手动配置签名信息](ide-signing.md#section297715173233)替换profile文件。
8. 在工程中entry模块的module.json5文件中添加"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"权限，如下所示：

   ```
   1. "requestPermissions": [{
   2. "name": "ohos.permission.MANAGE_SCREEN_TIME_GUARD"
   3. }]
   ```
