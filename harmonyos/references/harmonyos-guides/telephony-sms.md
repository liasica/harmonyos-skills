---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/telephony-sms
title: 短信服务
breadcrumb: 指南 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > 短信服务
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ac9e6b1ea003af224f06b6858debdff42c7c77bf0df5e4220717cb32d0086be9
---

## 场景介绍

短信服务模块提供了管理短信的一些基础能力，包括创建/发送短信、获取/设置发送短信的默认SIM卡槽ID、获取/设置短信服务中心地址，以及检查当前设备是否具备短信发送和接收能力等。

常见的应用场景举例如下：

* 从网页拉起：
  + 用户在网页上浏览，看到“发送短信”按钮，点击后会拉起短信应用，预先填写收件人号码、发送内容。
* 从应用拉起：
  + 移动应用中，用户点击“发送短信”按钮时，应用调用系统功能，拉起短信应用，预先填写收件人号码、发送内容。

## 基本概念

* 短信服务

  即SMS（Short Messaging Service），是一种存储和转发服务。用户的移动电话可以通过它进行相互收发短信，内容以文本、数字或二进制非文本数据为主。发送方的信息通过短信服务中心进行储存并转发给接收方。
* 短信服务中心

  即SMSC（Short Message Service Center），负责在基站和移动设备间中继、储存或转发短消息。移动设备到短信服务中心的协议能传输来自移动设备或朝向移动设备的短消息，协议内容遵从GSM 03.40协议。
* 协议数据单元

  即PDU（Protocol Data Unit），PDU模式收发短信可以使用3种编码：7-bit、8-bit和UCS-2编码。7-bit编码用于发送普通的ASCII字符，8-bit编码通常用于发送数据短信，UCS-2编码用于发送Unicode字符。

## 约束与限制

1. 仅支持在标准系统上运行。
2. 需授予发送短信权限且插入SIM卡才可成功发送短信。

## 接口说明

说明

为了保证应用的运行效率，大部分API调用都是异步的，对于异步调用的API均提供了callback和Promise两种方式，以下示例采用callback回调方式，其他调用方式请参考[API](../harmonyos-references/js-apis-sms.md)文档。

| 接口名 | 描述 |
| --- | --- |
| sendShortMessage(options: SendMessageOptions, callback: AsyncCallback<void>): void | 发送文本或数据SMS消息。需要配置ohos.permission.SEND\_MESSAGES权限，该权限仅系统应用可申请。 |
| createMessage(pdu: Array<number>, specification: string, callback: AsyncCallback<ShortMessage>): void | 基于协议数据单元（PDU）和指定的SMS协议创建SMS消息实例。 |
| getDefaultSmsSlotId(callback: AsyncCallback<number>): void | 获取用于发送短信的默认SIM卡。 |

## 应用内跳转到短信编辑界面

发送短信的接口需要系统权限才可调用，三方应用如果有发送短信需求，需要在应用内实现跳转到短信编辑的功能，并且需要携带编辑内容和收件人号码，可以通过调用元能力startAbility接口指定号码并跳转到发送短信页面的方式实现。

```
1. // 示例代码
2. import { common, Want } from '@kit.AbilityKit';

4. const MMS_BUNDLE_NAME = "com.ohos.mms";
5. const MMS_ABILITY_NAME = "com.ohos.mms.MainAbility";
6. const MMS_ENTITIES = "entity.system.home";

8. export class Contact {
9. contactsName: string;
10. telephone: number;

12. constructor(contactsName: string, telephone: number) {
13. this.contactsName = contactsName;
14. this.telephone = telephone;
15. }
16. }

18. @Entry
19. @Component
20. struct JumpMessage {
21. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

23. startMMSAbilityExplicit() {
24. // 这里完善联系人和号码；姓名主要是通过手机号来查询实际联系人名称，因此这种方式还是以手机号码为主。
25. let params: Array<Object> = [new Contact("张三", 133XXXXXXXX)];

27. let want: Want = {
28. bundleName: "com.ohos.mms",
29. abilityName: "com.ohos.mms.MainAbility",
30. parameters: {
31. contactObjects: JSON.stringify(params),
32. pageFlag: "conversation",
33. // 这里填写短信内容。
34. content: "我是短信具体内容"
35. }
36. };

38. this.context.startAbilityForResult(want).then((data) => {
39. console.info("Success" + JSON.stringify(data));
40. }).catch(() => {
41. console.error("error");
42. });
43. }

45. build() {
46. Row() {
47. Column() {
48. Button('发送短信')
49. .onClick(() => {
50. this.startMMSAbilityExplicit();
51. })
52. }
53. .width('100%')
54. }
55. .height('100%')
56. }
57. }
```

## sms方式跳转到短信编辑界面

### 使用场景

通过sms短信协议，可以创建指向短信收件人的超链接，方便用户通过网页或应用中的超链接直接跳转到短信应用。同时，支持在sms:的相关字段中定义短信的收件人、发送内容等，节省用户编辑短信的时间。

### sms协议格式

sms协议标准格式如下：

```
1. sms:106XXXXXXXXXX?body=发送短信内容
```

* sms:：sms scheme，必填。
* 106XXXXXXXXXX：收件人号码，选填。如果存在多个地址，用英文逗号分隔。
* ?：短信内容声明开始符号。如果带短信内容参数，则必填。
* body-value：发送内容参数，选填。

### 拉起方开发步骤

**从网页拉起**

网页中的超链接需要满足sms协议。示例如下：

```
1. <a href="sms:106XXXXXXXXXX?body=%E5%8F%91%E9%80%81%E7%9F%AD%E4%BF%A1%E5%86%85%E5%AE%B9">发送短信</a>
```

实际开发时，需要将收件人号码替换为真实的号码，短信内容可以根据需要进行配置。

**从应用拉起**

保证sms字符串传入uri参数即可，在应用中page页面可通过 this.getUIContext().getHostContext() 获取context，在ability中可通过this.context获取context。

```
1. // 示例代码
2. import { common, Want } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {

8. build() {
9. Column() {
10. Button('发送短信')
11. .onClick(() => {
12. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
13. let exampleUrl = "sms:106XXXXXXXXXX?body=%E5%8F%91%E9%80%81%E7%9F%AD%E4%BF%A1%E5%86%85%E5%AE%B9";

15. let want: Want = {
16. bundleName: 'com.ohos.mms',
17. action: 'ohos.want.action.viewData',
18. uri:exampleUrl,
19. }

21. context.startAbility(want).then((data) => {
22. console.info("Success" + JSON.stringify(data));
23. }).catch(() => {
24. console.error("error");
25. });

27. })
28. }
29. }
30. }
```
