---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-appinfo-manage
title: 通过AppGallery Connect动态管理应用图标
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 图标管理服务 > 通过AppGallery Connect动态管理应用图标
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7e51210524ae93dc62ce68bcaf27abe7594c079b6798632b2fac88e1112e920c
---

通过图标管理服务，开发者可以在不升级应用版本的情况下，通过AGC页面动态管理应用的个性化图标，并在应用侧实现应用图标动态切换。

## 申请开通服务

使用图标管理服务之前，请按如下格式向华为运营人员发送邮件申请开通服务。申请审核时间为1-3个工作日，审核结果请关注邮件信息或[互动中心](../app/agc-help-interaction-center-0000002276985946.md)通知。

* 请确保申请开通图标管理服务的应用处于正式上架状态，避免服务开通失败。
* 应用信息和开发者账号信息查询方法参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。

**邮箱地址：** agconnect@huawei.com

**邮件标题：** HarmonyOS应用图标管理开通申请-应用名称

**邮件内容：**

开发者账号ID：\*\*\*\*\*\*\*\*

应用名称：\*\*\*\*\*\*\*

应用ID：\*\*\*\*\*\*\*

应用包名：\*\*\*\*\*\*\*\*

应用状态：\*\*\*\*\*\*\*\*

## 通过AppGallery Connect配置应用图标

登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“APP与元服务”，在应用列表中选择已经开通图标管理服务的HarmonyOS应用，选择“分发 > 服务 > 图标管理”，进入图标管理页面，就可以管理HarmonyOS应用的个性化图标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/21HXQZZRQxW8RKj3XMLFZg/zh-cn_image_0000002589245097.png?HW-CC-KV=V1&HW-CC-Date=20260429T053714Z&HW-CC-Expire=86400&HW-CC-Sign=D4FE572FF6671F1A1B48A2685D1A819DD1F0A28743954D6B74EEBA1C35EB6563)

说明

* 只有正式发布的HarmonyOS应用支持管理个性化图标。
* 在创建个性化图标前，您需要提前准备好需要上传的图标文件，图标文件需要满足应用市场的审核政策要求，详情参见《[应用审核指南](../app/50104.md)》。

## 创建图标

1. 在图标管理页面点击“新增图标”按钮，进入创建图标页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/iEjkXXhXSA6vIxqTmqH3Mg/zh-cn_image_0000002558765292.png?HW-CC-KV=V1&HW-CC-Date=20260429T053714Z&HW-CC-Expire=86400&HW-CC-Sign=C48D6CDB61368337FEBB62E8B0B7CCFCE286E767DFDD68A037C19F9A83999B0C)
2. 输入图标ID、图标名称，选择设备类型，上传图标文件，点击“保存”或者“提交”按钮，将图标保存为草稿状态或提交审核。

说明

* 新创建的图标，需要经过应用市场审核通过，才能在客户端使用。
* 图标审核时间为1-3个工作日，审核状态和审核意见直接展示在图标信息查看页面，不会单独通知。

## 编辑和更新图标

1. 在图标管理页面选择一个草稿或审核不通过的图标，点击“编辑”按钮，或选择一个审核通过的图标，点击“更新”按钮，进入图标编辑页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ijGGqIBaTgmp3mSr16upmw/zh-cn_image_0000002558605636.png?HW-CC-KV=V1&HW-CC-Date=20260429T053714Z&HW-CC-Expire=86400&HW-CC-Sign=8B126AFAFAA5A69355ABE8C766CE1C3EB73FAAB131973B10FF372EFD7EEF6C0F)
2. 输入图标ID、图标名称，选择设备类型，上传图标文件，点击“保存”或者“提交”按钮，将图标保存为草稿状态或提交审核。

说明

* 草稿、审核不通过状态的图标支持编辑，审核中的图标不支持编辑，但是可以点击“撤销”按钮，将审核中的图标撤回草稿状态。
* 审核通过的图标支持更新，但只支持变更图标名称和图标文件，图标ID和设备类型不支持变更，图标更新也需要审核通过才能生效。

## 删除图标

1. 在图标管理页面选择一个图标，点击“删除”按钮，再点击提示框中的“确认”按钮，就可以删除指定图标。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/Forw7MQPS6-uB5hTenmrIg/zh-cn_image_0000002589325163.png?HW-CC-KV=V1&HW-CC-Date=20260429T053714Z&HW-CC-Expire=86400&HW-CC-Sign=227825507FD155332FDDBDB5B37C59B87E7216A8BE167859B73A6FB7808DE4D6)

说明

* 图标删除不需要审批，删除之后不可恢复，请谨慎操作。
* 如果被删除的图标正在用户设备桌面上使用，图标删除后，桌面上的图标不会自动回退，需要客户端触发图标切换。
