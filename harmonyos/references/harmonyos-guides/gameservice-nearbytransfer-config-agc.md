---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-nearbytransfer-config-agc
title: 开发准备
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏近场快传（可选） > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a01f83ff59f5bdebe88f6ff72e7307991ad0976023258f1a6e2c8fa6257df7d5
---

## 创建游戏

若在华为应用市场发布游戏，或使用AGC控制台提供的服务，需要前往AGC控制台创建游戏类应用，具体操作请参见[创建项目](../app/agc-help-create-project-0000002242804048.md)和[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。其中：

* “应用类型”：选择“HarmonyOS应用”。
* “应用分类”：选择“游戏”。

## 申请近场快传开放能力

基于安全考虑，系统侧对近场快传功能做了权限保护处理，使用相关接口开发者需先提交“近场快传”能力开关的申请，在申请通过后，再使用该能力开关。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“开发与服务”。在项目列表中找到项目，并点击选择需要申请权限的游戏。
2. 在“项目设置”页面，选择“开放能力管理”页签，开始为游戏申请近场快传开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/Wn6i-7rpSD2qXESizuqnEQ/zh-cn_image_0000002583478901.png?HW-CC-KV=V1&HW-CC-Date=20260427T234905Z&HW-CC-Expire=86400&HW-CC-Sign=FDD27C99CFD871549A6036F489D5CB1EFCC9B0982415DD282820CE00A3B15464)
3. 搜索“近场快传”，点击对应能力后面的“申请”，打开“新建业务申请”窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/ldpWhzccQ42Bv4p9XS1GaA/zh-cn_image_0000002552799252.png?HW-CC-KV=V1&HW-CC-Date=20260427T234905Z&HW-CC-Expire=86400&HW-CC-Sign=17C7EF91432634E6C61189CF54A91E39189A6DA807E46B9635C48ABA1106B7D0)
4. 在“新建业务申请”窗口填写申请信息，然后点击“提交”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/goC1CgxeS2OmBDgzozz8bA/zh-cn_image_0000002583438947.png?HW-CC-KV=V1&HW-CC-Date=20260427T234905Z&HW-CC-Expire=86400&HW-CC-Sign=4C03C1A813E98C96CD4563A3568E7D5E70E784791E070301D2DC22EB4856BA69)

   | 配置项 | 必填/选填 | 说明 |
   | --- | --- | --- |
   | 申请原因 | 必填 | 申请近场快传的原因，请按照模板填写相关信息，字数不超过512个字符。 |
   | 上传附件 | 选填 | 仅可上传1个附件，大小不超过500MB。支持文本、表格、图片、视频、压缩包格式。 |
5. 进入互动中心页面，可以看到申请已提交的消息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/nLd-izEqSJWdJuNkf0l9tQ/zh-cn_image_0000002552958902.png?HW-CC-KV=V1&HW-CC-Date=20260427T234905Z&HW-CC-Expire=86400&HW-CC-Sign=D309A5A04A921A72054192B3132B00EEE4C784BC1C3E8BC149C1058B9A7DF2BF)

   返回“开放能力管理”页面，近场快传显示“申请中”，1-3个工作日反馈申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/V5ATgkaZTtyGCkEGCB1Tgw/zh-cn_image_0000002583478903.png?HW-CC-KV=V1&HW-CC-Date=20260427T234905Z&HW-CC-Expire=86400&HW-CC-Sign=DBE2A5C7BFE59F2F986A499F721F3B8E29AAF861A2D752A0A407957C71CB5B71)
6. 申请审批通过后，互动中心将会发送通知给您，同时近场快传的能力开关会为您自动开启，“申请中”也会变为置灰显示的“申请”。至此，游戏已成功开启近场快传开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/mtmGStiAT6KKf0Ui0YxCNQ/zh-cn_image_0000002552799254.png?HW-CC-KV=V1&HW-CC-Date=20260427T234905Z&HW-CC-Expire=86400&HW-CC-Sign=DBB422F424411FDE23EFF8C2C8048D2C831E9B0DB96B3BB7C861BF5C13E7BDF6)

## 生成签名证书

数字证书和Profile文件等签名信息可以确保游戏的完整性，请参见[配置签名信息](application-dev-overview.md#section42841246144813)完成配置。

## 配置APP ID和相关权限

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的**APP ID**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/QUUx1bMXSOKcOdmcKgu0Dg/zh-cn_image_0000002583438949.png?HW-CC-KV=V1&HW-CC-Date=20260427T234905Z&HW-CC-Expire=86400&HW-CC-Sign=FD5BE787740642DF7EEBC6BC3C4B03872E8C3E770343F20A36CA203CA40BF15A)
2. 在工程的entry模块module.json5文件中，新增metadata并配置app\_id，同时新增requestPermissions并配置如下权限。

   ```
   1. "module": {
   2. "name": "entry",
   3. "type": "entry",
   4. "description": "xxxx",
   5. "mainElement": "xxxx",
   6. "deviceTypes": [
   7. "phone"
   8. ],
   9. "deliveryWithInstall": true,
   10. "pages": "$profile:main_pages",
   11. "abilities": [],
   12. "metadata": [ // 配置如下信息
   13. {
   14. "name": "app_id",
   15. "value": "xxxxxx" // 配置为前面步骤中获取的APP ID
   16. }
   17. ],
   18. "requestPermissions": [ // 配置权限
   19. {
   20. "name": "ohos.permission.INTERNET" // 允许使用Internet网络权限
   21. },
   22. {
   23. "name": "ohos.permission.GET_NETWORK_INFO"  // 允许应用获取数据网络信息权限
   24. },
   25. {
   26. "name": "ohos.permission.SET_NETWORK_INFO" // 允许应用配置数据网络权限
   27. },
   28. {
   29. "name": "ohos.permission.DISTRIBUTED_DATASYNC", // 允许不同设备间的数据交换权限
   30. "reason": "$string:distributed_permission",
   31. "usedScene": {
   32. "abilities": [
   33. "EntryAbility"
   34. ],
   35. "when": "inuse"
   36. }
   37. }
   38. ]
   39. }
   ```
