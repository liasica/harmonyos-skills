---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/priority-notification-permission-guidelines
title: 申请优先通知权益
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 申请优先通知权益
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:06+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:e6af27d4e02509acdb0e6290635e12ace4d4a72f11b030019d4699606f210cd5
---

当用户终端收到携带[priorityNotificationType](../harmonyos-references/js-apis-inner-notification-notificationrequest.md)字段的通知消息时，系统会将其识别为优先通知并优先显示。

申请优先通知权益存在以下限制：

1）该优先通知消息仅对商务类、社交通讯类应用开放。

2）应用内需具备重要联系人、@我、加急消息提醒功能，且申请后仅在上述场景中使用该能力，申请时需提供相应功能截图/示意图。

3）重要联系人场景需同时接入跳转应用内“重要联系人列表”能力。详情请参考[应用链接说明](app-uri-config.md)，[linkFeature](app-uri-config.md#linkfeature标签说明)字段使用PrimaryContactMgmt即可。

说明：优先通知权益仅允许在审核通过的场景中使用，如果申请权限后使用的功能和场景超出申请的范围，则属于违规，平台将禁用应用的优先通知权益。

## 申请步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/xn_86n07QRufdpuLI_QhjA/zh-cn_image_0000002791566532.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=67E87DB85CF42BFEC8DC8FF5E2D489885C3EF0D97CDC35BBAAAE5727A2DCC403)
2. 在项目列表中找到您的项目，在项目下的应用列表中选择需要申请优先通知权益的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/3o1bovV0Ta26-fbJbcnf_A/zh-cn_image_0000002820526485.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F6E9345132B82DE16A3143971E7630FE1C61C013999B403E57BD5E6AAAE72C2)
3. 进入“项目设置 > 开放能力管理”页面，点击“优先通知”的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/WbaSmWTSQjSvKnQVQ2k44Q/zh-cn_image_0000002820406485.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA98FFBE2B5ADCC8E1E4904572A2B6B378DF482AC04BE6D4B5EDCEDFB1089FC5)
4. 开发者可参考“申请原因”中的模板，提供申请必须的相关信息，包括应用介绍、使用场景、申请用途、附件、承诺信息，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/v7N8a9FZRH6OoFEpjkplNQ/zh-cn_image_0000002791726506.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=74BE2D1D93693EBA02D41999F72D4270D875F13C5433A78DF40AA16BD0BAAC35)
5. 开发者可通过互动中心的“服务开通申请”消息获取优先通知权益申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/rY1OlYz6Q12AgsY9U4IYpw/zh-cn_image_0000002791566534.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=ECB9FDD6B66FB94439D3E442C844335068A66B6D92DBB7F9224EB37FFBA5D73C)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/DU0bEPfGTp2N49ihSqqkaQ/zh-cn_image_0000002820526487.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC84622AC7E81D71A423352EB0C84B4C00B299315D1C59A7D07D8D56CEBD4D5B)
6. 优先通知权益申请通过后，须在“证书、APP ID和Profile”页面下左侧树形菜单的“Profile”页签，点击“添加”重新生成Profile文件，并下载Profile文件到本地，然后在“[发布应用](ide-publish-app.md)”时，须将该Profile打包到应用包中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/kobMWT-qTgKeGQhzWhxe5Q/zh-cn_image_0000002820406487.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=F211929521494ADA15D70CEC0C206D028502A31E3B387AFC7AF146C8091183C2)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/R8qnifX8QkSKUGcqm1bqqg/zh-cn_image_0000002791726508.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=9510A93934684965C133DD3A05A549AC3DCBB52EBE9A1E621226326B9805126F)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/ea5oPh2aScuhH9nplsI-dQ/zh-cn_image_0000002791566536.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=01A7CDB067BA9098B7EC52E7FC442AA905098E9C9FB213F32B06C984FF78C7C7)
