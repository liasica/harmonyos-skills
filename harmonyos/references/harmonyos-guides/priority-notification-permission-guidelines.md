---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/priority-notification-permission-guidelines
title: 申请优先通知权益
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 申请优先通知权益
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:26+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:51a5330c1e2d1ca6a8eca15bde1b696abaa7d8ecc04a728a14a77a3e626ad0c4
---

当用户终端收到携带[priorityNotificationType](../harmonyos-references/js-apis-inner-notification-notificationrequest.md)字段的通知消息时，系统会将其识别为优先通知并优先显示。

申请优先通知权益存在以下限制：

1）该优先通知消息仅对商务类、社交通讯类应用开放。

2）应用内需具备重要联系人、@我、加急消息提醒功能，且申请后仅在上述场景中使用该能力，申请时需提供相应功能截图/示意图。

3）重要联系人场景需同时接入跳转应用内“重要联系人列表”能力。详情请参考[应用链接说明](app-uri-config.md)，[linkFeature](app-uri-config.md#linkfeature标签说明)字段使用PrimaryContactMgmt即可。

说明：优先通知权益仅允许在审核通过的场景中使用，如果申请权限后使用的功能和场景超出申请的范围，则属于违规，平台将禁用应用的优先通知权益。

## 申请步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/Vc3vEbdQSTiGYvHddve14w/zh-cn_image_0000002589245373.png?HW-CC-KV=V1&HW-CC-Date=20260429T053924Z&HW-CC-Expire=86400&HW-CC-Sign=EF2BC606E68CABB210B35F95EE1A0F5123A5FBE852F1E40829F2E15DC3326B31)
2. 在项目列表中找到您的项目，在项目下的应用列表中选择需要申请优先通知权益的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/WYcqxj-rRjCC-ZndUHhYAA/zh-cn_image_0000002558765566.png?HW-CC-KV=V1&HW-CC-Date=20260429T053924Z&HW-CC-Expire=86400&HW-CC-Sign=EC8D7609AE558D701554C8135D798FF45B7A5C5ADABE23F8B4C48E0AE494DBCD)
3. 进入“项目设置 > 开放能力管理”页面，点击“优先通知”的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/QQ-qmjWIR4-5-MeFG8AvSA/zh-cn_image_0000002558605910.png?HW-CC-KV=V1&HW-CC-Date=20260429T053924Z&HW-CC-Expire=86400&HW-CC-Sign=C2D0772F054E7A25E402B07E69ED722F1910DD3B99BFA11AAC119CA65DC287B3)
4. 开发者可参考“申请原因”中的模板，提供申请必须的相关信息，包括应用介绍、使用场景、申请用途、附件、承诺信息，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/QtD-0hgyQ6WmP1yjcVC-Jg/zh-cn_image_0000002589325437.png?HW-CC-KV=V1&HW-CC-Date=20260429T053924Z&HW-CC-Expire=86400&HW-CC-Sign=8B015B34EA447D293116B36E37749EEC16DD27CDE5C538EF87DBA1772698F106)
5. 开发者可通过互动中心的“服务开通申请”消息获取优先通知权益申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/-EFdkUXgTPCdLXjDrZ3neA/zh-cn_image_0000002589245375.png?HW-CC-KV=V1&HW-CC-Date=20260429T053924Z&HW-CC-Expire=86400&HW-CC-Sign=473E5FD7E6CE68EF3C91F143FF7C7AC3BE91F636617E3F55400A6527E8799979)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/GPoPeB20TkWE2sI61cOviA/zh-cn_image_0000002558765568.png?HW-CC-KV=V1&HW-CC-Date=20260429T053924Z&HW-CC-Expire=86400&HW-CC-Sign=A2A44AAF8A59040E64ED042F99F6C1989D30B2D2166A91834DF5590BE0224796)
6. 优先通知权益申请通过后，须在“证书、APP ID和Profile”页面下左侧树形菜单的“Profile”页签，点击“添加”重新生成Profile文件，并下载Profile文件到本地，然后在“[发布应用](ide-publish-app.md)”时，须将该Profile打包到应用包中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/Z1Sq802dQsOlnFWBfLC02A/zh-cn_image_0000002558605912.png?HW-CC-KV=V1&HW-CC-Date=20260429T053924Z&HW-CC-Expire=86400&HW-CC-Sign=3CA0DB4FCF1166CA8F187F99E73EA44A13AE2480FBFB9DA375CE4DC7349DE65F)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/JRvv0CoOT3WU5eSQZN5rvw/zh-cn_image_0000002589325439.png?HW-CC-KV=V1&HW-CC-Date=20260429T053924Z&HW-CC-Expire=86400&HW-CC-Sign=AA5FF682249AF4BF35DA5AAE6D4B89CC072D3EA91656147899A3D7697A0C24CF)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/e2Evo6aKSD2CjA89mNq-VQ/zh-cn_image_0000002589245377.png?HW-CC-KV=V1&HW-CC-Date=20260429T053924Z&HW-CC-Expire=86400&HW-CC-Sign=C57579F2A6EA5A5242A43DBFA8E0C08DA60DBF78DAB12CCE8CC04C31A125BE70)
