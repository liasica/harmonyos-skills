---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/priority-notification-permission-guidelines
title: 申请优先通知权益
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 申请优先通知权益
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:26+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:d451ad3b625fe5306969a26de10b48f81b3dfb948f4bf33cc7e6533b60935f97
---

当用户终端收到携带[priorityNotificationType](../harmonyos-references/js-apis-inner-notification-notificationrequest.md)字段的通知消息时，系统会将其识别为优先通知并优先显示。

申请优先通知权益存在以下限制：

1）该优先通知消息仅对商务类、社交通讯类应用开放。

2）应用内需具备重要联系人、@我、加急消息提醒功能，且申请后仅在上述场景中使用该能力，申请时需提供相应功能截图/示意图。

3）重要联系人场景需同时接入跳转应用内“重要联系人列表”能力。详情请参考[应用链接说明](app-uri-config.md)，[linkFeature](app-uri-config.md#linkfeature标签说明)字段使用PrimaryContactMgmt即可。

说明：优先通知权益仅允许在审核通过的场景中使用，如果申请权限后使用的功能和场景超出申请的范围，则属于违规，平台将禁用应用的优先通知权益。

## 申请步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/3mUS2ByfQtqzjidnvS59Eg/zh-cn_image_0000002788468146.png?HW-CC-KV=V1&HW-CC-Date=20261114T004642Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B3C7C60DE1F7669CB518AA6F5F167D3D4AE80ECA68A5B9106262DCF4D058080)
2. 在项目列表中找到您的项目，在项目下的应用列表中选择需要申请优先通知权益的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/5m01wm6MTKepMFHXlHKYaA/zh-cn_image_0000002817507635.png?HW-CC-KV=V1&HW-CC-Date=20261114T004642Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0978966BC80D9FE00D44FA0FC773F03955804BF5737F935541945D94CB9FE30)
3. 进入“项目设置 > 开放能力管理”页面，点击“优先通知”的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/EGJxcfo0TeqOu476C5Ij1Q/zh-cn_image_0000002788308204.png?HW-CC-KV=V1&HW-CC-Date=20261114T004642Z&HW-CC-Expire=31536000000&HW-CC-Sign=C393020B6B47FF378ED3E5D3054A0E6FBC31D94AF449AFABA6958C66FC855301)
4. 开发者可参考“申请原因”中的模板，提供申请必须的相关信息，包括应用介绍、使用场景、申请用途、附件、承诺信息，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/NDo_r9NYR2KdQtPqt7jc8Q/zh-cn_image_0000002817427567.png?HW-CC-KV=V1&HW-CC-Date=20261114T004642Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B32D1CA4F837B2B3C172F669243DE16CDC64A96DF14482717B2789EA422BA7F)
5. 开发者可通过互动中心的“服务开通申请”消息获取优先通知权益申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/WFmcExLIRk2zeeOOPdOVcQ/zh-cn_image_0000002788468148.png?HW-CC-KV=V1&HW-CC-Date=20261114T004642Z&HW-CC-Expire=31536000000&HW-CC-Sign=334A1AE13E1D15EABC2C1C1CF18961C8E091DBD5EEA186A1392EBC8EA55460A8)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/0bIZDjh8TDKOq89QL2tZvQ/zh-cn_image_0000002817507637.png?HW-CC-KV=V1&HW-CC-Date=20261114T004642Z&HW-CC-Expire=31536000000&HW-CC-Sign=463E5000EB4B3DAFE1C26E9256D1042B8CE3ACD683443CAC024096CCE5EBE665)
6. 优先通知权益申请通过后，须在“证书、APP ID和Profile”页面下左侧树形菜单的“Profile”页签，点击“添加”重新生成Profile文件，并下载Profile文件到本地，然后在“[发布应用](ide-publish-app.md)”时，须将该Profile打包到应用包中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/XDgAkXT5SmyrhHe729F6Xg/zh-cn_image_0000002788308206.png?HW-CC-KV=V1&HW-CC-Date=20261114T004642Z&HW-CC-Expire=31536000000&HW-CC-Sign=5FE51FEBE9B6F612A2C665A62C2052E99C241F55D1B4E973FDE5B7222DA3DA87)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/URtx7vd8Q56ZLgnvITaIzg/zh-cn_image_0000002817427569.png?HW-CC-KV=V1&HW-CC-Date=20261114T004642Z&HW-CC-Expire=31536000000&HW-CC-Sign=63E99B94B616E2005397E47580D36FFD7EE6D7C5DA33A3DF29CF49B1E14F4CE0)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/fcG-90CKTRKnPDBmQ5gc8A/zh-cn_image_0000002788468150.png?HW-CC-KV=V1&HW-CC-Date=20261114T004642Z&HW-CC-Expire=31536000000&HW-CC-Sign=57E48D4ACC94D85AE1B7A65EE7E64E96386B5362B8B53569E0E5DED9C35CC539)
