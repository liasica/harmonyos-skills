---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/telephony-sms
title: 短信服务
breadcrumb: 指南 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > 短信服务
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:35+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:f2488a241fdb5232e363db507196d6efeaf1ffeb1db66d3977ec75d9acc266e4
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

**说明** 

为了保证应用的运行效率，大部分API调用都是异步的，对于异步调用的API均提供了callback和Promise两种方式，以下示例采用callback回调方式，其他调用方式请参考[@ohos.telephony.sms (短信服务)](../harmonyos-references/js-apis-sms.md)文档。

| 接口名 | 描述 |
| --- | --- |
| sendShortMessage(options: SendMessageOptions, callback: AsyncCallback<void>): void | 发送文本或数据SMS消息。需要配置ohos.permission.SEND\_MESSAGES权限，该权限仅系统应用可申请。 |
| createMessage(pdu: Array<number>, specification: string, callback: AsyncCallback<ShortMessage>): void | 基于协议数据单元（PDU）和指定的SMS协议创建SMS消息实例。 |
| getDefaultSmsSlotId(callback: AsyncCallback<number>): void | 获取用于发送短信的默认SIM卡。 |

## 应用内跳转到短信编辑界面

发送短信的接口需要系统权限才可调用，三方应用如果有发送短信需求，需要在应用内实现跳转到短信编辑的功能，并且需要携带编辑内容和收件人号码，可以通过调用元能力startAbility接口指定号码并跳转到发送短信页面的方式实现。开启[混淆](ide-build-obfuscation.md)后，contactsName和telephone可能被混淆，建议在-keep-property-name保留属性名称。

```ts
// 示例代码
import { common, Want } from '@kit.AbilityKit';

const MMS_BUNDLE_NAME = "com.ohos.mms";
const MMS_ABILITY_NAME = "com.ohos.mms.MainAbility";
const MMS_ENTITIES = "entity.system.home";

export class Contact {
    contactsName: string;
    telephone: number;

    constructor(contactsName: string, telephone: number) {
        this.contactsName = contactsName;
        this.telephone = telephone;
    }
}

@Entry
@Component
struct JumpMessage {
    private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

    startMMSAbilityExplicit() {
        // 这里完善联系人和号码；姓名主要是通过手机号来查询实际联系人名称，因此这种方式还是以手机号码为主。
        let params: Array<Object> = [new Contact("张三", 133XXXXXXXX)];

        let want: Want = {
            bundleName: "com.ohos.mms",
            abilityName: "com.ohos.mms.MainAbility",
            parameters: {
                contactObjects: JSON.stringify(params), // 开启混淆后，contactsName和telephone可能被混淆，建议在-keep-property-name保留属性名称
                pageFlag: "conversation",
                // 这里填写短信内容。
                content: "我是短信具体内容"
            }
        };

        this.context.startAbilityForResult(want).then((data) => {
            console.info("Success" + JSON.stringify(data));
        }).catch(() => {
            console.error("error");
        });
    }

    build() {
        Row() {
            Column() {
                Button('发送短信')
                  .onClick(() => {
                      this.startMMSAbilityExplicit();
                  })
            }
            .width('100%')
        }
        .height('100%')
    }
}
```

## sms方式跳转到短信编辑界面

### 使用场景

通过sms短信协议，可以创建指向短信收件人的超链接，方便用户通过网页或应用中的超链接直接跳转到短信应用。同时，支持在sms:的相关字段中定义短信的收件人、发送内容等，节省用户编辑短信的时间。

### sms协议格式

sms协议标准格式如下：

```txt
sms:106XXXXXXXXXX?body=发送短信内容
```

* sms:：sms scheme，必填。
* 106XXXXXXXXXX：收件人号码，选填。如果存在多个地址，用英文逗号分隔。
* ?：短信内容声明开始符号。如果带短信内容参数，则必填。
* body-value：发送内容参数，选填。

### 拉起方开发步骤

**从网页拉起**

网页中的超链接需要满足sms协议。示例如下：

```txt
<a href="sms:106XXXXXXXXXX?body=%E5%8F%91%E9%80%81%E7%9F%AD%E4%BF%A1%E5%86%85%E5%AE%B9">发送短信</a>
```

实际开发时，需要将收件人号码替换为真实的号码，短信内容可以根据需要进行配置。

**从应用拉起**

保证sms字符串传入uri参数即可，在应用中page页面可通过 this.getUIContext().getHostContext() 获取context，在ability中可通过this.context获取context。

```ts
// 示例代码
import { common, Want } from '@kit.AbilityKit';

@Entry
@Component
struct Index {

  build() {
    Column() {
      Button('发送短信')
        .onClick(() => {
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          let exampleUrl = "sms:106XXXXXXXXXX?body=%E5%8F%91%E9%80%81%E7%9F%AD%E4%BF%A1%E5%86%85%E5%AE%B9";
        
          let want: Want = {
              bundleName: 'com.ohos.mms',
              action: 'ohos.want.action.viewData',
              uri:exampleUrl,
            }
        
          context.startAbility(want).then((data) => {
              console.info("Success" + JSON.stringify(data));
          }).catch(() => {
              console.error("error");
          });

        })
    }
  }
}
```
