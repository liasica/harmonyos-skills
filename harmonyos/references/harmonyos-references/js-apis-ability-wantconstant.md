---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-wantconstant
title: @ohos.ability.wantConstant (wantConstant)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 已停止维护的接口 > @ohos.ability.wantConstant (wantConstant)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:50+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:609ac5b254e3df8298c4246fd9c6909edb3ef2edb369d2e36a201ca0d76c29a4
---

wantConstant模块提供want中操作want常数和解释Flags说明的能力。

说明

本模块首批接口从API version 6开始支持，从API version 9废弃，替换模块为[@ohos.app.ability.wantConstant](js-apis-app-ability-wantconstant.md)。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import wantConstant from '@ohos.ability.wantConstant';
```

## Action

PhonePC/2in1TabletTVWearable

want操作的常数。用于表示要执行的通用操作。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACTION\_HOME | ohos.want.action.home | 指示返回原点的操作。 |
| ACTION\_DIAL | ohos.want.action.dial | 指示启动显示小键盘的页面功能的操作。 |
| ACTION\_SEARCH | ohos.want.action.search | 指示启动页面搜索功能的操作。 |
| ACTION\_WIRELESS\_SETTINGS | ohos.settings.wireless | 指示启动提供无线网络设置的页面功能的操作，例如，Wi-Fi选项。 |
| ACTION\_MANAGE\_APPLICATIONS\_SETTINGS | ohos.settings.manage.applications | 指示启动管理已安装应用程序的页面功能的操作。 |
| ACTION\_APPLICATION\_DETAILS\_SETTINGS | ohos.settings.application.details | 指示启动显示指定应用程序详细信息的页面功能的操作。 |
| ACTION\_SET\_ALARM | ohos.want.action.setAlarm | 指示启动页面功能以设置闹钟的操作。 |
| ACTION\_SHOW\_ALARMS | ohos.want.action.showAlarms | 指示启动显示所有警报的页面功能的操作。 |
| ACTION\_SNOOZE\_ALARM | ohos.want.action.snoozeAlarm | 指示启动用于使闹钟睡眠的页面功能的操作。 |
| ACTION\_DISMISS\_ALARM | ohos.want.action.dismissAlarm | 指示启动删除闹钟的页面功能的操作。 |
| ACTION\_DISMISS\_TIMER | ohos.want.action.dismissTimer | 指示启动页面功能以关闭计时器的操作。 |
| ACTION\_SEND\_SMS | ohos.want.action.sendSms | 指示启动发送sms的页面功能的操作。 |
| ACTION\_CHOOSE | ohos.want.action.choose | 指示启动页面功能以打开联系人或图片的操作。 |
| ACTION\_IMAGE\_CAPTURE8+ | ohos.want.action.imageCapture | 指示启动页面拍照功能的操作。 |
| ACTION\_VIDEO\_CAPTURE8+ | ohos.want.action.videoCapture | 指示启动页面功能以拍摄视频的操作。 |
| ACTION\_SELECT | ohos.want.action.select | 指示显示应用程序选择对话框的操作。 |
| ACTION\_SEND\_DATA | ohos.want.action.sendData | 指示发送单个数据记录的操作。 |
| ACTION\_SEND\_MULTIPLE\_DATA | ohos.want.action.sendMultipleData | 指示发送多个数据记录的操作。 |
| ACTION\_SCAN\_MEDIA\_FILE | ohos.want.action.scanMediaFile | 指示请求媒体扫描仪扫描文件并将文件添加到媒体库的操作。 |
| ACTION\_VIEW\_DATA | ohos.want.action.viewData | 指示查看数据的操作。 |
| ACTION\_EDIT\_DATA | ohos.want.action.editData | 指示编辑数据的操作。 |
| INTENT\_PARAMS\_INTENT | ability.want.params.INTENT | 指示用行为选择器来展示选择的操作。 |
| INTENT\_PARAMS\_TITLE | ability.want.params.TITLE | 指示与行为选择器一起使用时的字符序列对话框标题。 |
| ACTION\_FILE\_SELECT7+ | ohos.action.fileSelect | 指示选择文件的操作。 |
| PARAMS\_STREAM7+ | ability.params.stream | 指示发送数据时与目标关联的数据流的URI。对应的value必须是string类型的数组。 |
| ACTION\_APP\_ACCOUNT\_OAUTH 8+ | ohos.account.appAccount.action.oauth | 指示提供oauth服务的操作。 |

## Entity

PhonePC/2in1TabletTVWearable

want实体的常数。用于表示目标Ability额外的类别信息。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENTITY\_DEFAULT | entity.system.default | 指示默认实体，如果未指定实体，则使用该实体。 |
| ENTITY\_HOME | entity.system.home | 指示主屏幕实体。 |
| ENTITY\_VOICE | entity.system.voice | 表示语音交互实体。 |
| ENTITY\_BROWSABLE | entity.system.browsable | 指示浏览器类别。 |
| ENTITY\_VIDEO | entity.system.video | 指示视频类别。 |

## Flags

PhonePC/2in1TabletTVWearable

Flags说明。用于表示处理Want的方式。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FLAG\_AUTH\_READ\_URI\_PERMISSION | 0x00000001 | 指示对URI执行读取操作的授权。 |
| FLAG\_AUTH\_WRITE\_URI\_PERMISSION | 0x00000002 | 指示对URI执行写入操作的授权。 |
| FLAG\_ABILITY\_FORWARD\_RESULT | 0x00000004 | 将结果返回给元能力。 |
| FLAG\_ABILITY\_CONTINUATION | 0x00000008 | 确定是否可以将本地设备上的功能迁移到远程设备。 |
| FLAG\_NOT\_OHOS\_COMPONENT | 0x00000010 | 指定组件是否属于OHOS。 |
| FLAG\_ABILITY\_FORM\_ENABLED | 0x00000020 | 指定是否启动某个能力。 |
| FLAG\_ABILITYSLICE\_MULTI\_DEVICE | 0x00000100 | 支持分布式调度系统中的多设备启动。 |
| FLAG\_START\_FOREGROUND\_ABILITY | 0x00000200 | 指示无论主机应用程序是否已启动，都将启动使用服务模板的功能。 |
| FLAG\_INSTALL\_ON\_DEMAND | 0x00000800 | 如果未安装指定的功能，请安装该功能。 |
| FLAG\_INSTALL\_WITH\_BACKGROUND\_MODE | 0x80000000 | 如果未安装，使用后台模式安装该功能。 |
| FLAG\_ABILITY\_CLEAR\_MISSION | 0x00008000 | 指示清除其他任务的操作。可以为传递给 **FeatureAbility** 中[startAbility](js-apis-ability-featureability.md#featureabilitystartability)方法的**Want**设置此标志，并且必须与**FLAG\_ABILITY\_NEW\_MISSION**一起使用。 |
| FLAG\_ABILITY\_NEW\_MISSION | 0x10000000 | 指示在历史任务堆栈上创建任务的操作。 |
| FLAG\_ABILITY\_MISSION\_TOP | 0x20000000 | 指示如果启动能力的现有实例已位于任务堆栈的顶部，则将重用该实例。否则，将创建一个新的能力实例。 |
