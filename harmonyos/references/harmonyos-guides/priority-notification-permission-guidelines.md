---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/priority-notification-permission-guidelines
title: 申请优先通知权益
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 申请优先通知权益
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:32+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:bc2b8efdc1407e2ded26d61d402d59e79d165d6c5bdd9ea88183a68afa0b04ff
---

当用户终端收到携带[priorityNotificationType](../harmonyos-references/js-apis-inner-notification-notificationrequest.md)字段的通知消息时，系统会将其识别为优先通知并优先显示。

申请优先通知权益存在以下限制：

1）该优先通知消息仅对商务类、社交通讯类应用开放。

2）应用内需具备重要联系人、@我、加急消息提醒功能，且申请后仅在上述场景中使用该能力，申请时需提供相应功能截图/示意图。

3）重要联系人场景需同时接入跳转应用内“重要联系人列表”能力。详情请参考[应用链接说明](app-uri-config.md)，[linkFeature](app-uri-config.md#linkfeature标签说明)字段使用PrimaryContactMgmt即可。

说明：优先通知权益仅允许在审核通过的场景中使用，如果申请权限后使用的功能和场景超出申请的范围，则属于违规，平台将禁用应用的优先通知权益。

## 申请步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/xPgDghZHQNGTwrXDmOCI8w/zh-cn_image_0000002821758093.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=0872F329C91AE6C17AA2CB586C2FC78F4B4A713001CBB39185183602B3E92FE4)
2. 在项目列表中找到您的项目，在项目下的应用列表中选择需要申请优先通知权益的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/8nSNET9FQZaLPJOJDRJ7lw/zh-cn_image_0000002793038156.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C70C1548A79B6F8CC2D8123DD94DE61C8D31537DFA9597429785F0789C9CDB6)
3. 进入“项目设置 > 开放能力管理”页面，点击“优先通知”的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/FCwktIrJTlypVHRhSGmTGw/zh-cn_image_0000002792878186.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF67A1DC0F9162AA50B39BCD62AFEDA4FF3E9AB09389F34DD69BE1869D493B03)
4. 开发者可参考“申请原因”中的模板，提供申请必须的相关信息，包括应用介绍、使用场景、申请用途、附件、承诺信息，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/MGB7apZARTeD9XbABQ1jsA/zh-cn_image_0000002821838093.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB71C6E4120743094E390C3B3C775E77F2B42AAFF84394CC483037A9DE6BC71D)
5. 开发者可通过互动中心的“服务开通申请”消息获取优先通知权益申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/4d1RZlPJRYSp3GtGCcDyYA/zh-cn_image_0000002821758095.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=6EC3BD52007BA45C37968F414A6F518E8B1752656A454847A5C3F505E612D077)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/On9P6vLCR0aGUxvW_nHSXA/zh-cn_image_0000002793038158.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=315DECF0909268ACAAA1573357E9F0EFAE13D0947879196195DBB56A44003C06)
6. 优先通知权益申请通过后，须在“证书、APP ID和Profile”页面下左侧树形菜单的“Profile”页签，点击“添加”重新生成Profile文件，并下载Profile文件到本地，然后在“[发布应用](ide-publish-app.md)”时，须将该Profile打包到应用包中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/AaPZwS5xRW6y_Rs6dQlZZw/zh-cn_image_0000002792878188.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC4D805EF65006F1DB748318D7D1CFB57A2CF7BBF67F938A266C21679319240C)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/X1qtUD4IQt6DwAwQOuiBlQ/zh-cn_image_0000002821838095.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2C024344F22EC48263FE318EBF8EE0EC2A34C8BD3D1A155C7B61F8E153125D3)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/eTVwjLwhTfW-CGVSpX5ETQ/zh-cn_image_0000002821758097.png?HW-CC-KV=V1&HW-CC-Date=20261121T011105Z&HW-CC-Expire=31536000000&HW-CC-Sign=60038CF4F690A01B45139E23E16F86A2E9996CB58EA9A72011647EFB416E69A4)
