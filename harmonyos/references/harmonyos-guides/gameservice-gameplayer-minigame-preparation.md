---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameplayer-minigame-preparation
title: 开发准备
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 基础游戏服务（必选） > 小游戏 > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e22df37c91cb72056a9e5f3c615e19445e233a0a7578130f1ff3631d8aa98739
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/w9qfNt_NQAGac6nZn_H0UQ/zh-cn_image_0000002558605738.png?HW-CC-KV=V1&HW-CC-Date=20260429T053809Z&HW-CC-Expire=86400&HW-CC-Sign=4B98E1651580CACFA1892846C19BEB50928AFE7250CE17603F242A5A41AEFFCA)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/SVaVQ0BcRgaEkfk0stoaDg/zh-cn_image_0000002589325265.png?HW-CC-KV=V1&HW-CC-Date=20260429T053809Z&HW-CC-Expire=86400&HW-CC-Sign=A1C95E4B4DC92AEB755795FDF65CD4A415E57B1ECB3DB5C45222D9B4C8FD6B6E)
2. 在弹出的“新增配置信息”窗口中填写信息，完成后点击“下一步”。

   说明

   请正确配置HAP小游戏与RPK快游戏的映射关系。若开发者配置错误类型的游戏，将会提示重新选择游戏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/dlu_A7zCQEij-vqpiE2Cug/zh-cn_image_0000002589245201.png?HW-CC-KV=V1&HW-CC-Date=20260429T053809Z&HW-CC-Expire=86400&HW-CC-Sign=A396F7200CDAB407BE49919C86A435FA04B3F4BF5CA6429BF2206F398B8F1A80)

   | 信息项 | 说明 |
   | --- | --- |
   | HarmonyOS 5.0及以上游戏 | 请选择待上架的HAP小游戏。 |
   | HarmonyOS 4及以下游戏 | 请选择已上架或草稿态的RPK快游戏。 |
3. （可选）填写开发者服务器的回调地址，完成后点击“确定”提交APP ID映射关系的审批申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/5GefoeMrQtuXWWOqgXOcag/zh-cn_image_0000002558765396.png?HW-CC-KV=V1&HW-CC-Date=20260429T053809Z&HW-CC-Expire=86400&HW-CC-Sign=E1B09887857FC9AA894C4CF74131422A09BBA15F0069FE25C5AA70066A109EBA)
4. 若出现异常情况（例如在架状态不符合要求），将在提示框以红字提醒，建议点击“取消”并重新配置映射关系。若忽略异常情况点击“确定”继续提交申请，可能会造成映射关系审批不通过。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/tpy3cb7mSJi_HDogmWq7Yw/zh-cn_image_0000002558605740.png?HW-CC-KV=V1&HW-CC-Date=20260429T053809Z&HW-CC-Expire=86400&HW-CC-Sign=34B3106434DC3E8004355D6FFF5F3092782D083E67F28408BFA0A8B489F0508B)
5. 提交申请后，华为工作人员完成审核需要1-3个工作日，请耐心等待。APP ID映射关系生效后如需重新配置，请先提交映射关系的删除申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/GYLFGTLITOS43HnXR36f_g/zh-cn_image_0000002589325267.png?HW-CC-KV=V1&HW-CC-Date=20260429T053809Z&HW-CC-Expire=86400&HW-CC-Sign=4EA1D05DB0A10C7623A9311620839C38D04EA5C7EB07DFCEDB3A26C1D5102D28)

   配置/删除APP ID映射关系的审核结果将通过互动中心或邮件进行通知。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/SfXQBvY-SRK0a6SOW1fw9Q/zh-cn_image_0000002589245203.png?HW-CC-KV=V1&HW-CC-Date=20260429T053809Z&HW-CC-Expire=86400&HW-CC-Sign=1AF77D87A7BFFB8A4DCBC9A42D3FCE5401F832B52D025A0403A9677153317ECD)
