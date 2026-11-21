---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-appinfo-manage
title: 通过HarmonyOS 开发者中心动态管理应用图标
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 图标管理服务 > 通过HarmonyOS 开发者中心动态管理应用图标
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:18+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:5b72ced112dcd1f830492b6db33928d48af2e4106ab7a824017b8b65bd302ed7
---

图标管理服务支持开发者在应用客户端完成接口适配（查询、切换、恢复默认图标）并发布新版本后，通过HarmonyOS 开发者中心页面动态管理应用的个性化图标，实现应用侧图标动态切换，开发者无需再升级应用版本。

## 申请开通服务

使用图标管理服务之前，请按如下格式向华为运营人员发送邮件申请开通服务。申请审核时间为1-3个工作日，审核结果请关注邮件信息或[互动中心](https://developer.huawei.com/consumer/cn/message-center/myMessage)通知。

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

## 通过HarmonyOS 开发者中心配置应用图标

登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/index.html#/home/101653523124949886)，在“所有应用”列表中找到并点击已开通图标管理服务的HarmonyOS应用，进入应用管理页面。在左侧导航栏中，依次选择“分发 >更多服务> 图标管理”，进入图标管理页面后，就可以管理HarmonyOS应用的个性化图标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/gB-ukTZgTdeP6XD6UfuQGA/zh-cn_image_0000002793037868.png?HW-CC-KV=V1&HW-CC-Date=20261121T011051Z&HW-CC-Expire=31536000000&HW-CC-Sign=1246D9905C0AD6E0DBE477C7930BCA8B59AA1638613CA89338FC383E9AB7FBB2)

**说明** 

* 只有正式发布的HarmonyOS应用支持管理个性化图标。
* 在创建个性化图标前，您需要提前准备好需要上传的图标文件，图标文件需要满足应用市场的审核政策要求，详情参见《[应用审核指南](../app/50104.md)》。

## 创建图标

1. 在图标管理页面点击“新增图标”按钮，进入创建图标页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/jMBfoNELTh-JosV9tCjTtg/zh-cn_image_0000002792877898.png?HW-CC-KV=V1&HW-CC-Date=20261121T011051Z&HW-CC-Expire=31536000000&HW-CC-Sign=6120DED1C219CDC1CF7883AF75C3AA4B8CB66F57A3F051E691A59B387DD2B100)
2. 输入图标ID、图标名称，选择设备类型，上传图标文件，点击“保存”或者“提交”按钮，将图标保存为草稿状态或提交审核。

**说明** 

* 新创建的图标，需要经过应用市场审核通过，才能在客户端使用。
* 图标审核时间为1-3个工作日，审核状态和审核意见直接展示在图标信息查看页面，不会单独通知。

## 编辑和更新图标

1. 在图标管理页面选择一个草稿或审核不通过的图标，点击“编辑”按钮，或选择一个审核通过的图标，点击“更新”按钮，进入图标编辑页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/qPvZPnlnQ6igpkVPlBlQgw/zh-cn_image_0000002821837805.png?HW-CC-KV=V1&HW-CC-Date=20261121T011051Z&HW-CC-Expire=31536000000&HW-CC-Sign=033F10A46388DB560ACAD8EDAC3A7DD8238A5568A3609A3C7E80802EC4BA9796)
2. 输入图标ID、图标名称，选择设备类型，上传图标文件，点击“保存”或者“提交”按钮，将图标保存为草稿状态或提交审核。

**说明** 

* 草稿、审核不通过状态的图标支持编辑，审核中的图标不支持编辑，但是可以点击“撤销”按钮，将审核中的图标撤回草稿状态。
* 审核通过的图标支持更新，但只支持变更图标名称和图标文件，图标ID和设备类型不支持变更，图标更新也需要审核通过才能生效。

## 删除图标

1. 在图标管理页面选择一个图标，点击“删除”按钮，再点击提示框中的“确认”按钮，就可以删除指定图标。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/T_o-Qz6ZTFO3x5m1jpEMWA/zh-cn_image_0000002821757807.png?HW-CC-KV=V1&HW-CC-Date=20261121T011051Z&HW-CC-Expire=31536000000&HW-CC-Sign=F97A52BE05F28916CEA424893CB83F2150E7FD07FD2DC98C20C6A3C76333CDE5)

**说明** 

* 图标删除不需要审批，删除之后不可恢复，请谨慎操作。
* 如果被删除的图标正在用户设备桌面上使用，图标删除后，桌面上的图标不会自动回退，需要客户端触发图标切换。
