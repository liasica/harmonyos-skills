---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-push-3
title: 消息推送后手机未收到消息提示怎么处理
breadcrumb: FAQ > 应用服务开发 > 消息推送服务（Push Kit） > 消息推送后手机未收到消息提示怎么处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:ab147680f2d0fe339ea219de6f013e95f96d983f42403599e12f9cf3e9ab82ea
---

## 问题现象

使用Push Kit（推送服务）提供的接口推送消息，但是客户端没有消息提示。

* 预期效果：推送消息后，客户端能及时收到消息提示，例如出现消息弹框。
* 实际效果：推送消息后，客户端未收到消息提示，或者没有及时收到消息，未出现消息弹框。

## 背景知识

* [Push Kit（推送服务）](../harmonyos-guides/push-kit-introduction.md)：华为提供的消息推送平台，建立了从云端到终端的消息推送通道。
* [申请推送场景化消息权益](../harmonyos-guides/push-apply-right.md)：Push Kit支持多种场景化消息类型，其中部分场景化消息类型需要开发者申请特殊权益才能正常发送。
* [请求通知授权](../harmonyos-guides/notification-enable.md)：应用需要获取用户授权才能发送通知。
* [开发消息回执](../harmonyos-guides/push-msg-receipt.md)：消息回执是指Push Kit服务端将消息推送到用户终端之后，端侧会给Push服务端反馈送达结果。与此同时，Push服务端会将消息送达状态以回执消息形式发送给应用回执服务端，方便开发者获取消息下达端侧后的状态，定位问题等。
* [发送消息通知](../harmonyos-guides/push-send-alert.md)：通知消息通过Push Kit通道直接下发，可在终端设备的通知中心、锁屏、横幅等展示，用户点击后拉起应用。

## 问题定位

* **用户收到了消息**
  + 检查是否是静默通知。
  + 检查是否手动关闭了消息提醒方式。
* **用户未收到消息**
* 检查Push token是否正确。
* 检查Authorization请求体是否错误。
* 检查是否推送后台消息场景。
* 检查设备是否离线。
* 检查自分类权益是否已申请，是否开启状态。
* 检查是否受到消息频控。
* 检查配置文件是否配置错误。

## 分析结论

* 资讯营销类消息的通知方式是静默通知，仅在通知中心展示消息。
* 服务与通讯类消息的通知方式默认是锁屏、铃声、振动，用户手动关闭锁屏、铃声、振动，导致未收到提示。
* 消息推送参数配置错误、被频控等情况下会导致消息推送失败。

## 修改建议

* 当收到资讯营销类消息时，由于静默通知仅在通知中心展示，并不会弹框提示，需要去通知中心查看。通知中心如下图，可以查看对应消息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/K7VtXzPKThe_bS64RgALGA/zh-cn_image_0000002658913759.png "点击放大")
* 若终端上的app手动关闭了消息提醒方式，终端收到消息不会有提醒，需要打开所需的提醒方式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/bQbLmDsoQYeDUZCU_bO3wA/zh-cn_image_0000002658793813.png "点击放大")
* 打开[AGC平台](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，按查询路径：“开发与服务>增长>推送服务>自助分析（Beta）”，在自助分析里面输入requestId和token，系统会自动分析消息推送失败的可能原因，注意requestId有效期为三天。

  也可能是Push token不是有效的token，建议您在应用启动时调用getToken()接口，若设备的Push Token发生变化，及时上报到您的应用服务器更新Push Token，以防由于Push Token失效导致收不到消息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/reswrI7_TsuIHBnWvS5CSw/zh-cn_image_0000002628394542.png "点击放大")
* 检查服务端发送请求时是否正确携带Authorization请求头，value为JWT格式字符串，是基于服务账号生成鉴权令牌。可参考：[请求体结构说明](../harmonyos-references/push-scenariozed-api-request-struct.md)。
* [推送后台消息](../harmonyos-guides/push-background.md)用于内容不频繁更新的场景，不会显示通知、播放铃声或改变应用角标。终端设备接收到后台消息后，如果应用进程在前台则将消息内容传给应用；如果应用进程不在前台则缓存消息，等待应用启动后再传给应用。
* 如果设备离线，Push Kit会缓存消息，待设备上线后，再将消息推送给设备。
* 检查自分类权益是否已申请，并且打开自分类权益开关，请参考：[申请推送场景化消息权益](../harmonyos-guides/push-apply-right.md)。
* 检查是否受到消息频控。
  + 调测阶段：每个项目每个自然日最多可推送1000条测试消息（非设备级，所有设备共用1000条），且不受场景化消息频控限制（即不区分通知消息类别、不区分场景化消息类别）。可以在消息发送请求体中设置[pushOptions.testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)为true，发送测试消息。
  + 正式发布阶段：单设备单应用下每个自然日最多可推送3000条消息，并受[场景化消息频控](../harmonyos-references/push-msg-freq-control.md#场景化消息频控)限制。

* 参考[推送消息跳转能力](../harmonyos-guides/push-send-alert.md#点击消息动作)文档，检查module.json5中skills配置是否正确。
  + 应用只需要配置一条skill对象。
    - 设置action参数点击消息进入应用页面（若skills中添加了uris参数，则uris内容需为空）。
    - 设置uris参数点击消息进入应用页面（skills中必须同时设置actions参数，actions参数需为空）。
  + 应用需要配置多条skill对象。

    比如同时设置推送消息跳转能力和其他跳转能力（如NFC跳转、浏览器跳转等），可以在skills数组中创建不同的skill对象，分别映射对应的能力。

## 总结

Push Kit消息下发成功后，可能会因为消息频控、通知开关未打开等原因，导致端侧消息未展示。通常可以从消息通知是否打开、消息分类权益是否申请、配置文件中skills标签是否正确这几个方面进行排查。同时，建议开发消息回执，Push服务端会将消息送达状态以回执消息形式发送给应用回执服务端，方便获取消息下达端的状态，通过回执状态码定位问题。

## 常见FAQ

Q：云侧推送消息成功端侧消息未展示呢？

A：请您自查是否为以下情况造成：

* 是否申请通知权限。
* 终端设备的网络连接异常。
* 终端的通知开关关闭。
* 应用已卸载，未安装。

Q：已申请到VOIP场景化消息权益。A给B拨打音视频，VOIP请求成功推送至华为推送服务器，但目标用户没有收到，在平台的查询的结果是应用不支持该场景。

A：

1. 排查创建的VoIPUIAbility中pushService.receiveMessage是否配置的是“VOIP”类型。
2. 在项目工程的src/main/module.json5文件的abilities模块中配置VoIPUIAbility的actions信息，需要单独定义一个VoIPUIAbility，而不是把它写到MainAbility里面。示例代码请参考[开发步骤](../harmonyos-guides/push-send-extend-noti.md#开发步骤)中步骤2和步骤4。

Q：因设备离线等因素时token失效导致未收到消息，是否占用推送额度？如何清理token？

A：

1. 失效token会占用推送额度。
2. token由开发者服务端进行存储管理，需要伙伴服务端对失效token进行清理。可在推送后，定期清理未推送成功的token，再对有效token和新上报的token进行推送。

Q：服务端已发送消息，但是客户端无法接收到推送消息，报错信息：80300002、80200001、80300007等错误的可能是什么原因？

A：首先排查“服务账号密钥”凭证中的project\_id是否与您的应用所属项目一致，如果不同需要更换正确的凭证；然后排查[场景化消息请求体](../harmonyos-references/push-scenariozed-api-request-struct.md)接口URL中projectId是否为当前项目。

Q：Push Token失效的场景有哪些？

A：下列场景会导致之前的Push Token发生变化而失效：

* 卸载应用后重新安装。
* 设备恢复出厂设置。
* 应用显式调用deleteToken()接口后重新调用getToken()接口。
* 应用显式调用deleteAAID()接口后重新调用getToken()接口。
* 将设备（仅涉及Wearable设备）拿到海外其他国家或者地区后，系统会更新设备的token。更新后的token通过pushService.on('tokenUpdate')接口的回调返回。
