---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameplayer-minigame-preparation
title: 开发准备
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 基础游戏服务（必选） > 小游戏 > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:83f5c46c0b40ccf700d9910ba3f152fe91df99a2cf7958dd2b04af94caa609e5
---

## 创建小游戏

在华为应用市场发布小游戏，要求前往AppGallery Connect创建小游戏类元服务，具体操作请参见[创建小游戏](../app/agc-help-create-minigame-0000002434138360.md)。其中：

* “应用类型”：选择“元服务”。
* “应用分类”：选择“小游戏”。

说明

用于正式上架的游戏包名建议不要包含test、dev等信息。

## 申请版署实名认证

按照版署《关于开展网络游戏防沉迷实名认证系统接口对接工作的通知》，各游戏出版运营企业均要求在2021年6月1日前完成接入[网络游戏防沉迷实名认证系统](https://wlc.nppa.gov.cn/fcm_company/index.html#/login?redirect=/)，并获取“bizID（游戏备案识别码）”，再将bizID配置到AppGallery Connect，华为将为游戏自动对接国家新闻出版署的实名认证系统并开启强制实名认证，开发者无需进行额外的开发。具体操作请参见[版署实名认证申请](../games-guides/game-center-identification-applyfor-0000002392353221.md)。

## 申请备案

请参考[APP备案FAQ](../App/50130.md)、[快游戏备案指南](../quickApp-Guides/quickgame-filing-guide-0000001806139508.md)和[国产游戏小程序备案准备](../games-guides/quickgame-filing-chinese-preparation-0000001979934858.md)完成小游戏备案，并保存好备案信息。

## 申请JSVM权限和存储空间管理开放能力

小游戏上架必须申请JSVM权限和存储空间管理开放能力，具体操作请参见[申请ACL权限和开放能力](../app/agc-help-release-minigame-acl-and-ability-0000002425276004.md)。

## 生成签名证书

数字证书和Profile文件等签名信息可以确保小游戏的完整性：

* 调试阶段：[手动签名](ide-signing.md#section297715173233)、[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)、[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。
* 发布阶段：[手动签名](ide-signing.md#section297715173233)、[申请发布证书](../app/agc-help-release-cert-0000002283336729.md)、[申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)。

## 配置签名证书指纹

AppGallery Connect会自动生成证书对应的公钥信息，并计算出对应的SHA256指纹。开发者前往AppGallery Connect获取并配置SHA256指纹，且每个游戏至多添加4个签名证书指纹，配置签名证书指纹的具体操作请参见[配置公钥指纹](../app/agc-help-cert-fingerprint-0000002278002933.md)。

说明

请在调试阶段添加调试证书对应的指纹，在发布阶段添加发布证书对应的指纹。

## 配置APP ID、Client ID和权限信息

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“开发与服务”下选择项目及项目下的小游戏，获取“应用”下的APP ID和Client ID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/CouHudZ6Sq2Dib_UZmAkZQ/zh-cn_image_0000002583478895.png?HW-CC-KV=V1&HW-CC-Date=20260427T234903Z&HW-CC-Expire=86400&HW-CC-Sign=99487A7BEB4AA7E727008E4B5C568740786ACD3A37886A4CC0667829409A55C5)
2. 在工程的entry模块module.json5文件中，新增metadata并配置client\_id和app\_id，同时新增requestPermissions以配置ACL权限和开放能力。如下所示：

   ```
   1. "module": {
   2. "name": "entry",
   3. "type": "xxx",
   4. "description": "xxxx",
   5. "mainElement": "xxxx",
   6. "deviceTypes": [],
   7. "pages": "xxxx",
   8. "abilities": [],
   9. "metadata": [ // 配置如下信息
   10. {
   11. "name": "client_id",
   12. "value": "xxxxxx" // 配置为前面步骤中获取的Client ID
   13. },
   14. {
   15. "name": "app_id",
   16. "value": "xxxxxx" // 配置为前面步骤中获取的APP ID
   17. }
   18. ],
   19. "requestPermissions": [ // 配置JSVM权限和存储空间管理开放能力
   20. {
   21. "name": "ohos.permission.kernel.ALLOW_EXECUTABLE_FORT_MEMORY"
   22. },
   23. {
   24. "name": "ohos.permission.atomicService.MANAGE_STORAGE"
   25. }
   26. ]
   27. }
   ```

## 配置APP ID映射关系

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“开发与服务”下选择项目及项目下的小游戏，左侧菜单选择“构建 > 游戏服务”，在右侧点击“新增配置”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/5wjo-rrZR52JyLisHuTjzg/zh-cn_image_0000002552799246.png?HW-CC-KV=V1&HW-CC-Date=20260427T234903Z&HW-CC-Expire=86400&HW-CC-Sign=E9601FA1E54A6CFAE703ED2F7964999436FBCDEFAAE81A43F433277D62D2F281)
2. 在弹出的“新增配置信息”窗口中填写信息，完成后点击“下一步”。

   说明

   请正确配置HAP小游戏与RPK快游戏的映射关系。若开发者配置错误类型的游戏，将会提示重新选择游戏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/nHYlUup1TsebX4WUyDO6pA/zh-cn_image_0000002583438941.png?HW-CC-KV=V1&HW-CC-Date=20260427T234903Z&HW-CC-Expire=86400&HW-CC-Sign=79AB9D458955077FD84A59ECE9E9ECB514E2B1BAC44D7BD237AB8071E449CCD6)

   | 信息项 | 说明 |
   | --- | --- |
   | HarmonyOS 5.0及以上游戏 | 请选择待上架的HAP小游戏。 |
   | HarmonyOS 4及以下游戏 | 请选择已上架或草稿态的RPK快游戏。 |
3. （可选）填写开发者服务器的回调地址，完成后点击“确定”提交APP ID映射关系的审批申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/YiMH3w5URgyqqUGRKWaKnw/zh-cn_image_0000002552958896.png?HW-CC-KV=V1&HW-CC-Date=20260427T234903Z&HW-CC-Expire=86400&HW-CC-Sign=32C7A81CAD9175F089CF6D8C1C61F11A08201DD7CB09A9569FD3B39401F21873)
4. 若出现异常情况（例如在架状态不符合要求），将在提示框以红字提醒，建议点击“取消”并重新配置映射关系。若忽略异常情况点击“确定”继续提交申请，可能会造成映射关系审批不通过。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/iSO4n5vOSM2ugpT83OSZAQ/zh-cn_image_0000002583478897.png?HW-CC-KV=V1&HW-CC-Date=20260427T234903Z&HW-CC-Expire=86400&HW-CC-Sign=3119A2B9487D763B892CD4439C2C0E764B0E97DA1363F21FDB48A56724A25567)
5. 提交申请后，华为工作人员完成审核需要1-3个工作日，请耐心等待。APP ID映射关系生效后如需重新配置，请先提交映射关系的删除申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/YTwIrRhGRtCfbNf2g_xBvg/zh-cn_image_0000002552799248.png?HW-CC-KV=V1&HW-CC-Date=20260427T234903Z&HW-CC-Expire=86400&HW-CC-Sign=9BDFF71F7490E3F3BE99674EC5D74DC3877600E86421D22D3ECFC5FAB6649A78)

   配置/删除APP ID映射关系的审核结果将通过互动中心或邮件进行通知。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/ZAXlgFEsRmy1scTOgQTH-A/zh-cn_image_0000002583438943.png?HW-CC-KV=V1&HW-CC-Date=20260427T234903Z&HW-CC-Expire=86400&HW-CC-Sign=A227042E559154E7DE37C07AC45DB822A038B5D92C8212CB348BD6F603CC0317)
