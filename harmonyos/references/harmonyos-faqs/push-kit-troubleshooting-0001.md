---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/push-kit-troubleshooting-0001
title: 消息推送后手机未收到消息提示怎么处理
breadcrumb: FAQ > 应用服务开发 > 消息推送服务（Push Kit） > 故障排查 > 消息推送后手机未收到消息提示怎么处理
category: harmonyos-faqs
scraped_at: 2026-10-23T07:14:32+08:00
doc_updated_at: 2026-10-22
content_hash: sha256:b96d73c12cd95a037f7426b30f78ff64510e732ca3dec0743263245df67a59ad
---

## 问题现象

使用Push Kit（推送服务）提供的接口推送消息，但是客户端没有消息提示。

* 预期效果：推送消息后，客户端能及时收到消息提示，例如出现消息弹框。
* 实际效果：推送消息后，客户端未收到消息提示，或者没有及时收到消息，未出现消息弹框。

## 定位过程

* **用户收到了消息：**
  + 检查是否是静默通知。
  + 检查是否手动关闭了消息提醒方式。
* **用户未收到消息：**
  + 检查消息[回执状态码](../harmonyos-guides/push-msg-receipt.md#section19100519195717)是否为6，若为6则继续排查通知开关、Push SDK方法调用等问题。
  + 检查Push token是否正确。
  + 检查Authorization请求体是否错误。
  + 检查是否推送后台消息场景。
  + 检查设备是否离线。
  + 检查应用是否被杀死，是否开启"自启动"和"后台活动"权限。
  + 检查应用的"通知渠道（通知类别）开关"是否被关闭，该开关独立于应用级总开关。
  + 检查应用或三方SDK是否调用过pushService.turnOffPush()方法，设置了不显示通知栏消息。
  + 检查自分类权益是否已申请，是否开启状态。
  + 检查是否受到消息频控。
  + 检查配置文件是否配置错误。

## 分析结论

* 资讯营销类消息的通知方式是静默通知，仅在通知中心展示消息。
* 服务与通讯类消息的通知方式默认是锁屏、铃声、振动，用户手动关闭锁屏、铃声、振动，导致未收到提示。
* 消息推送参数配置错误、被频控等情况下会导致消息推送失败。
* 推送请求中未正确携带category字段或取值与已申请的自分类权益不匹配时，消息会被默认按MARKETING处理，根据通知消息推送数量管理规则限制单设备单应用下每个自然日，限制推送数量为2条或5条，可能因此触发营销消息频控。
* 应用被杀死后，若未开启"自启动"权限或系统限制了后台活动，系统不会主动将应用拉起，导致消息无法投递。
* 应用的"通知渠道（通知类别）开关"是独立于应用级总开关的子开关，若被关闭则端侧收不到推送消息。
* 应用或三方SDK调用pushService.turnOffPush()方法后，会设置不显示通知栏消息，端侧同样上报"通知栏开关关闭"回执。

## 修改建议

* 当收到资讯营销类消息时，由于静默通知仅在通知中心展示，并不会弹框提示，需要去通知中心查看。通知中心如下图，可以查看对应消息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/9UNUaxU4QtScOBG82Co4NQ/zh-cn_image_0000002794653837.png "点击放大")
* 若终端上的app手动关闭了消息提醒方式，终端收到消息不会有提醒，需要打开所需的提醒方式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/Zh8C8o1QREaSkw1o0Y759Q/zh-cn_image_0000002794653841.png "点击放大")
* 检查应用的"通知渠道（通知类别）开关"是否被关闭。进入设置>通知和状态栏>找到该应用，除确认顶部"允许通知"总开关外，展开下方"通知类别"列表，逐一确认各类别（尤其服务与通讯/Push相关渠道）开关均处于开启状态。"通知类别"属于独立的子开关，此前确认的应用级总开关不包含子开关。
* 检查应用或三方SDK是否调用过pushService.turnOffPush()方法，该方法会设置不显示通知栏消息，端侧同样上报"通知栏开关关闭"回执。若存在调用记录，执行pushService.turnOnPush()恢复后重推验证。
* 打开[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/#/home/)，按查询路径："开发与服务>增长>推送服务>自助分析"，在自助分析里面输入requestId和token，系统会自动分析消息推送失败的可能原因，注意requestId有效期为三天。

  也可能是Push token不是有效的token，建议您在应用启动时调用getToken()接口，若设备的Push Token发生变化，及时上报到您的应用服务器更新Push Token，以防由于Push Token失效导致收不到消息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/rAM30CM7SASWj83cVqUU4w/zh-cn_image_0000002794573613.png "点击放大")
* 检查服务端发送请求时是否正确携带Authorization请求头，value为JWT格式字符串，是基于服务账号生成鉴权令牌。可参考：[请求体结构说明](../harmonyos-references/push-scenariozed-api-request-struct.md)。
* [推送后台消息](../harmonyos-guides/push-background.md)用于内容不频繁更新的场景，不会显示通知、播放铃声或改变应用角标。终端设备接收到后台消息后，如果应用进程在前台则将消息内容传给应用；如果应用进程不在前台则缓存消息，等待应用启动后再传给应用。
* 如果设备离线，Push Kit会缓存消息，待设备上线后，再将消息推送给设备。
* 应用被杀死后收不到推送消息时，需引导用户开启"自启动"和"后台活动"权限，使用长时任务防止进程被轻易杀死，并检查推送服务端是否配置了离线消息保存策略。
* 检查自分类权益是否已申请，并且打开自分类权益开关，请参考：[申请推送场景化消息权益](../harmonyos-guides/push-apply-right.md)。
* 排查推送请求中是否正确携带category字段，若未设置或取值与已申请的自分类权益不匹配，消息会被默认按MARKETING处理，触发营销消息频控。在推送请求体中添加category字段，设置为与HarmonyOS 开发者中心已审核通过的自分类权益一致的值（如"IM"），然后重新推送。可参考[发送通知消息](../harmonyos-guides/push-send-alert.md)文档。
* 检查是否受到消息频控。
  + 调测阶段：每个项目每个自然日最多可推送1000条测试消息（非设备级，所有设备共用1000条），且不受场景化消息频控限制（即不区分通知消息类别、不区分场景化消息类别）。可以在消息发送请求体中设置[pushOptions.testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)为true，发送测试消息。
  + 注意：testMessage参数类型为Boolean，设置字符串"false"在弱类型判断下等效于true，服务端仍将消息识别为测试消息。若需关闭测试消息，应设置为布尔值false或直接省略pushOptions字段。
  + 正式发布阶段：单设备单应用下每个自然日最多可推送3000条消息，并受[场景化消息频控](../harmonyos-references/push-msg-freq-control.md#场景化消息频控)限制。
* 参考[推送消息跳转能力](../harmonyos-guides/push-send-alert.md#点击消息动作)文档，检查module.json5中skills配置是否正确。
  + 应用只需要配置一条skill对象。
    - 设置action参数点击消息进入应用页面（若skills中添加了uris参数，则**uris内容需为空**）
    - 设置uris参数点击消息进入应用页面（skills中必须同时设置actions参数，**actions参数需为空**）
  + 应用需要配置多条skill对象。

    比如同时设置推送消息跳转能力和其他跳转能力（如NFC跳转、浏览器跳转等），可以在skills数组中创建不同的skill对象，分别映射对应的能力。
