---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-nearbytransfer-config-agc
title: 开发准备
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏近场快传（可选） > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:12+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:77deabbb32a3e5305c974082ee0ba78d046432b0f75c2556bfe63a2db3d6c3a6
---

## 创建游戏

若在华为应用市场发布游戏，或使用AGC控制台提供的服务，需要前往AGC控制台创建游戏类应用，具体操作请参见[创建项目](../app/agc-help-create-project-0000002242804048.md)和[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。其中：

* “应用类型”：选择“HarmonyOS应用”。
* “应用分类”：选择“游戏”。

## 申请近场快传开放能力

基于安全考虑，系统侧对近场快传功能做了权限保护处理，使用相关接口开发者需先提交“近场快传”能力开关的申请，在申请通过后，再使用该能力开关。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“开发与服务”。在项目列表中找到项目，并点击选择需要申请权限的游戏。
2. 在“项目设置”页面，选择“开放能力管理”页签，开始为游戏申请近场快传开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/ZmT10CkST32NDbRxELrgsQ/zh-cn_image_0000002558605744.png?HW-CC-KV=V1&HW-CC-Date=20260429T053811Z&HW-CC-Expire=86400&HW-CC-Sign=3A6230AFCA9640F85C59A43F943DFD044F00E330232F6E3B0078C01B06208297)
3. 搜索“近场快传”，点击对应能力后面的“申请”，打开“新建业务申请”窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/tb9OhEp7R1adllfG-6yTyQ/zh-cn_image_0000002589325271.png?HW-CC-KV=V1&HW-CC-Date=20260429T053811Z&HW-CC-Expire=86400&HW-CC-Sign=8E49B32D0C76ABDE3108D3237B149E980B10664A8D921282B7109606C313B1F6)
4. 在“新建业务申请”窗口填写申请信息，然后点击“提交”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/6Iu9gZfrSdShN0V99CdPkQ/zh-cn_image_0000002589245207.png?HW-CC-KV=V1&HW-CC-Date=20260429T053811Z&HW-CC-Expire=86400&HW-CC-Sign=0B88FF3EDF8A385AAEB5CD59DACD4C550C0AE8F0E200D7728057DFEB8C9464C7)

   | 配置项 | 必填/选填 | 说明 |
   | --- | --- | --- |
   | 申请原因 | 必填 | 申请近场快传的原因，请按照模板填写相关信息，字数不超过512个字符。 |
   | 上传附件 | 选填 | 仅可上传1个附件，大小不超过500MB。支持文本、表格、图片、视频、压缩包格式。 |
5. 进入互动中心页面，可以看到申请已提交的消息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/UpEWY8DoQ1mMfZgN6UdkXA/zh-cn_image_0000002558765402.png?HW-CC-KV=V1&HW-CC-Date=20260429T053811Z&HW-CC-Expire=86400&HW-CC-Sign=AFF2A9A73FD9CFF58F40D595FC16A1A7B69A9649345C0DF3E6E793577F42714F)

   返回“开放能力管理”页面，近场快传显示“申请中”，1-3个工作日反馈申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/9M49sVupRyKSzaRkDqZzNA/zh-cn_image_0000002558605746.png?HW-CC-KV=V1&HW-CC-Date=20260429T053811Z&HW-CC-Expire=86400&HW-CC-Sign=7D12E300270F638181C18253D8ACCBCE953868484FE623AA69AC774880D067F7)
6. 申请审批通过后，互动中心将会发送通知给您，同时近场快传的能力开关会为您自动开启，“申请中”也会变为置灰显示的“申请”。至此，游戏已成功开启近场快传开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/SesXOa6CREeVu0S-vgUxAg/zh-cn_image_0000002589325273.png?HW-CC-KV=V1&HW-CC-Date=20260429T053811Z&HW-CC-Expire=86400&HW-CC-Sign=66151E3394044AF2F9CFAA18EC75EC0F983297130A537E566109BB01DA119251)

## 生成签名证书

数字证书和Profile文件等签名信息可以确保游戏的完整性，请参见[配置签名信息](application-dev-overview.md#配置签名信息)完成配置。

## 配置APP ID和相关权限

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的**APP ID**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/FPNZcTRdRNKEKUD6Iu6fsQ/zh-cn_image_0000002589245209.png?HW-CC-KV=V1&HW-CC-Date=20260429T053811Z&HW-CC-Expire=86400&HW-CC-Sign=24FA731A4F6046E29C14FA8C2CFBEA0204D3514A6B5D561C2AB84F4BB3A3F19C)
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
