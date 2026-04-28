---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/priority-notification-permission-guidelines
title: 申请优先通知权益
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 申请优先通知权益
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:03+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:c4f4e31047442ec6a527de4b717d6149c7a6a0011e1face36fa0eb2f34e52f8d
---

当用户终端收到携带[priorityNotificationType](../harmonyos-references/js-apis-inner-notification-notificationrequest.md)字段的通知消息时，系统会将其识别为优先通知并优先显示。

申请优先通知权益存在以下限制：

1）该优先通知消息仅对商务类、社交通讯类应用开放。

2）应用内需具备重要联系人、@我、加急消息提醒功能，且申请后仅在上述场景中使用该能力，申请时需提供相应功能截图/示意图。

3）重要联系人场景需同时接入跳转应用内“重要联系人列表”能力。详情请参考[应用链接说明](app-uri-config.md)，[linkFeature](app-uri-config.md#linkfeature标签说明)字段使用PrimaryContactMgmt即可。

说明：优先通知权益仅允许在审核通过的场景中使用，如果申请权限后使用的功能和场景超出申请的范围，则属于违规，平台将禁用应用的优先通知权益。

## 申请步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/UNu5Rzs7TKiUrKpUBf0OAw/zh-cn_image_0000002583439109.png?HW-CC-KV=V1&HW-CC-Date=20260427T235002Z&HW-CC-Expire=86400&HW-CC-Sign=1D15F1B8127B5D7021EC074AE9B5CE3CE7C6908805B1F51759CD78144214DE90)
2. 在项目列表中找到您的项目，在项目下的应用列表中选择需要申请优先通知权益的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/yaxAv9PxSlyJYa5Diy3UxQ/zh-cn_image_0000002552959064.png?HW-CC-KV=V1&HW-CC-Date=20260427T235002Z&HW-CC-Expire=86400&HW-CC-Sign=623BDF5D017105CBE2A2469B80B94EC08504BF6B2AB8119217D6056D777FD13C)
3. 进入“项目设置 > 开放能力管理”页面，点击“优先通知”的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/XrsWb8x8Qs-FbuSep05Yhw/zh-cn_image_0000002583479065.png?HW-CC-KV=V1&HW-CC-Date=20260427T235002Z&HW-CC-Expire=86400&HW-CC-Sign=79BFF753BD014FBBE24B791C36ABB57658ED14013A0974743FCE5EC6C4A530B4)
4. 开发者可参考“申请原因”中的模板，提供申请必须的相关信息，包括应用介绍、使用场景、申请用途、附件、承诺信息，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/RfJmnw74T9yhx9E5lamVHQ/zh-cn_image_0000002552799416.png?HW-CC-KV=V1&HW-CC-Date=20260427T235002Z&HW-CC-Expire=86400&HW-CC-Sign=5EA18CD3256E994F37069B08E05B843E6A418BDA70917D7EBB942BEACBDB2DD1)
5. 开发者可通过互动中心的“服务开通申请”消息获取优先通知权益申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/ZvyIeGf4QfW5vMzd4BYgFw/zh-cn_image_0000002583439111.png?HW-CC-KV=V1&HW-CC-Date=20260427T235002Z&HW-CC-Expire=86400&HW-CC-Sign=ADBC0CB201F166B8043065636B89BEA01344D87B1C3D25025AFF4EDF0BD60026)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/s2K7AVdYSUGdE_0sZaPCpg/zh-cn_image_0000002552959066.png?HW-CC-KV=V1&HW-CC-Date=20260427T235002Z&HW-CC-Expire=86400&HW-CC-Sign=0A55B685FFAECC77B72ABBFB6806C0FF9C1AED84EFD9501FC59B699DB45684B2)
6. 优先通知权益申请通过后，须在“证书、APP ID和Profile”页面下左侧树形菜单的“Profile”页签，点击“添加”重新生成Profile文件，并下载Profile文件到本地，然后在“[发布应用](ide-publish-app.md)”时，须将该Profile打包到应用包中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/UM7QHw3oT8SG2S30oBOFhg/zh-cn_image_0000002583479067.png?HW-CC-KV=V1&HW-CC-Date=20260427T235002Z&HW-CC-Expire=86400&HW-CC-Sign=DEEDF2021148C2A4AB4A34230CA586CE55E056842211566C664F316ED958AD17)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/hiN2XpnJQHSFa_jYBQGvkA/zh-cn_image_0000002552799418.png?HW-CC-KV=V1&HW-CC-Date=20260427T235002Z&HW-CC-Expire=86400&HW-CC-Sign=B9CA8AC20116BBC1237988F409CC50FF149333E258351046ED77F6D145ACE23F)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/m47sC6QiSwm84kUGixESJw/zh-cn_image_0000002583439113.png?HW-CC-KV=V1&HW-CC-Date=20260427T235002Z&HW-CC-Expire=86400&HW-CC-Sign=5CB8ACA8B54FD88F225583B3C9EC24FB42BF4594211C8EE0DC908B1BE05FC7F7)
