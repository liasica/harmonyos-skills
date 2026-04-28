---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-permission-application
title: 受限ACL权限申请
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 开发准备 > 受限ACL权限申请
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b1308eba2df1c39d0f895456a5d3421c49b3c80cbf10a1a6853e131051c0fb18
---

1. 在 [申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)和[发布Profile文件](../app/agc-help-release-profile-0000002248341090.md)之前，需要[申请相应的ACL权限](../app/agc-help-apply-acl-0000002394212138.md)。
2. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“开发与服务”，在项目列表中找到对应的项目，并点击选择您需要申请ACL权限的应用。在“项目设置”页面，选择“ACL权限”页签，开始为应用申请ACL权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/yGjtCC3mRCG6oyLKEUd0ZA/zh-cn_image_0000002583439207.png?HW-CC-KV=V1&HW-CC-Date=20260427T235050Z&HW-CC-Expire=86400&HW-CC-Sign=D0CC79D1F27DA873F84DD440C1903B6371EEFDC4A5647721FB8324246B1E0505)
3. 在核对注意事项后，在“未获取权限”区域中勾选“我已知晓”。在权限搜索框中输入"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"，查找并勾选权限，提交申请。
4. 根据实际业务需求填写申请原因并提交，提交后将在1个工作日回复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/MpT1RkPpRq6153rNdOAPOQ/zh-cn_image_0000002552959162.png?HW-CC-KV=V1&HW-CC-Date=20260427T235050Z&HW-CC-Expire=86400&HW-CC-Sign=1F5122B96BFA35C93566707E6DBBDDE9E7AB840C52626C6CF802B09B5A6F8281)
5. 权限申请通过后，在申请profile文件时，在“申请权限”栏选中“受限ACL权限（HarmonyOS API9及以上）”选项，点击“选择”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/huNCLx39R42y61wS4RqxqQ/zh-cn_image_0000002583479163.png?HW-CC-KV=V1&HW-CC-Date=20260427T235050Z&HW-CC-Expire=86400&HW-CC-Sign=8E65212BDB2B6068AC346C21F4A6BC399EAD76AD3A539F730E21AF97D570AA8E)
6. 在弹出的“选择受限ACL权限”窗口可以看到已申请的权限，勾选后点击确定。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/_uel0SmpSxuF_4beZetqpQ/zh-cn_image_0000002552799514.png?HW-CC-KV=V1&HW-CC-Date=20260427T235050Z&HW-CC-Expire=86400&HW-CC-Sign=5DD24ECD8CF4E25877F0572DD36367B01E28CCCD88B8D3B326E0A15BC9871FB0)
7. 选择权限后点击“添加”生成新的Profile文件，下载后按[手动配置签名信息](ide-signing.md#section297715173233)替换profile文件。
8. 在工程中entry模块的module.json5文件中添加"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"权限，如下所示：

   ```
   1. "requestPermissions": [{
   2. "name": "ohos.permission.MANAGE_SCREEN_TIME_GUARD"
   3. }]
   ```
