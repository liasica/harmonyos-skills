---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameplayer-minigame-preparation
title: 开发准备
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 基础游戏服务（必选） > 小游戏 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:17+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:3bafc3349812dd53e4fd9fdf92bf6f1b570e9152fcea4e0cb4379374e9b62a8d
---

## 创建小游戏

在华为应用市场发布小游戏，要求前往AppGallery Connect创建小游戏类元服务，具体操作请参见[创建小游戏](../app/agc-help-create-minigame-0000002434138360.md)。其中：

* “应用类型”：选择“元服务”。
* “应用分类”：选择“小游戏”。

**说明** 

用于正式上架的游戏包名建议不要包含test、dev等信息。

## 申请版署实名认证

按照版署《关于开展网络游戏防沉迷实名认证系统接口对接工作的通知》，各游戏出版运营企业均要求在2021年6月1日前完成接入[网络游戏防沉迷实名认证系统](https://wlc.nppa.gov.cn/fcm_company/index.html#/login?redirect=/)，并获取“bizID（游戏备案识别码）”，再将bizID配置到AppGallery Connect，华为将为游戏自动对接国家新闻出版署的实名认证系统并开启强制实名认证，开发者无需进行额外的开发。具体操作请参见[版署实名认证申请](../app/game-center-next-identification-applyfor-0000002660208647.md)。

## 申请备案

请参考[APP核准（APP备案）指引](../App/50130.md)、[快游戏核准（备案）指南](../games-guides/games-quickgame-filing-guide-0000002318138840.md)和[国产游戏小程序核准（备案）准备](../games-guides/quickgame-filing-chinese-preparation-0000001979934858.md)完成小游戏备案，并保存好备案信息。

## 申请JSVM权限和存储空间管理开放能力

小游戏上架必须申请JSVM权限和存储空间管理开放能力，具体操作请参见[申请ACL权限和开放能力](../app/agc-help-release-minigame-acl-and-ability-0000002425276004.md)。

## 生成签名证书

数字证书和Profile文件等签名信息可以确保小游戏的完整性：

* 调试阶段，配置签名信息的具体操作请参见[手动签名](ide-signing-manual.md)。
* 发布阶段，配置签名信息的具体操作请参见[发布应用](ide-publish-app.md)。

## 配置签名证书指纹

AppGallery Connect会自动生成证书对应的公钥信息，并计算出对应的SHA256指纹。开发者前往AppGallery Connect获取并配置SHA256指纹，且每个游戏至多添加4个签名证书指纹，配置签名证书指纹的具体操作请参见[配置公钥指纹](../app/agc-help-cert-fingerprint-0000002278002933.md)。

**说明** 

请在调试阶段添加调试证书对应的指纹，在发布阶段添加发布证书对应的指纹。

## 配置APP ID、Client ID和权限信息

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“开发与服务”下选择项目及项目下的小游戏，获取“应用”下的APP ID和Client ID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/b6gdupurTvunr_DqomHQkg/zh-cn_image_0000002788308022.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=85B00A464BA258898A57194EC5A92AB3E8CBAED05FDA606F858E8E3F6EBA7AAB)
2. 在工程的entry模块module.json5文件中，新增metadata并配置client\_id和app\_id，同时新增requestPermissions以配置ACL权限和开放能力。如下所示：

   ```typescript
   "module": {
     "name": "entry",
     "type": "xxx",
     "description": "xxxx",
     "mainElement": "xxxx",
     "deviceTypes": [],
     "pages": "xxxx",
     "abilities": [],
     "metadata": [ // 配置如下信息
       {
         "name": "client_id",
         "value": "xxxxxx" // 配置为前面步骤中获取的Client ID
       },
       {
         "name": "app_id",
         "value": "xxxxxx" // 配置为前面步骤中获取的APP ID
       }
     ],
     "requestPermissions": [ // 配置JSVM权限和存储空间管理开放能力
       {
         "name": "ohos.permission.kernel.ALLOW_EXECUTABLE_FORT_MEMORY"
       },
       {
         "name": "ohos.permission.atomicService.MANAGE_STORAGE"
       }
     ]
   }
   ```

## 配置APP ID映射关系

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“开发与服务”下选择项目及项目下的小游戏，左侧菜单选择“构建 > 游戏服务”，在右侧点击“新增配置”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/2VZLDZt7RZmb8x9UBV2eew/zh-cn_image_0000002817427385.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D16F8D8B11307E3C630EA4C910071EF8072B0213C8D1CD30513C0CF67DB9201)
2. 在弹出的“新增配置信息”窗口中填写信息，完成后点击“下一步”。

   **说明** 

   请正确配置HAP小游戏与RPK快游戏的映射关系。若开发者配置错误类型的游戏，将会提示重新选择游戏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/uVUhcG3bRK--mt-FJu4pTA/zh-cn_image_0000002788467966.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=649C0B5855BA33031B4C34F7ACFBF1FBDE5F1D22C7C96F0BE79FE98CFB13EAA2)

   | 信息项 | 说明 |
   | --- | --- |
   | HarmonyOS 5.0及以上游戏 | 请选择待上架的HAP小游戏。 |
   | HarmonyOS 4及以下游戏 | 请选择已上架或草稿态的RPK快游戏。 |
3. （可选）填写开发者服务器的回调地址，完成后点击“确定”提交APP ID映射关系的审批申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/Bloswy8nSMOgcfqyiwseRw/zh-cn_image_0000002817507455.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=B0A24DF59BDADAA59FB766A03B68FF8E989B63CBBF63B059F9913B05719761ED)
4. 若出现异常情况（例如在架状态不符合要求），将在提示框以红字提醒，建议点击“取消”并重新配置映射关系。若忽略异常情况点击“确定”继续提交申请，可能会造成映射关系审批不通过。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/1BCsu0KSSouAMPOGIipytw/zh-cn_image_0000002788308024.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=D987440918ADBCE088068BAA855976A13EB9A24897EC0506B152302A6A22048C)
5. 提交申请后，华为工作人员完成审核需要1-3个工作日，请耐心等待。APP ID映射关系生效后如需重新配置，请先提交映射关系的删除申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/Iq24LDdJQLGNByM_WHHEpg/zh-cn_image_0000002817427387.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7202D0D2C44E80216C7085C120ACC7E582D2079180E793CA9629E6CEB31F6B3)

   配置/删除APP ID映射关系的审核结果将通过互动中心或邮件进行通知。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/9gHBs0F0SbGAWynkLCBRAQ/zh-cn_image_0000002788467968.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=33FB8D70BD1F1C81F959B4F72BE3BCA9417914004EB589EE32CA4D3CA53F1235)
