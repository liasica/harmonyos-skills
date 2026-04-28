---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview
title: ExtensionAbility组件
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > ExtensionAbility组件
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7c259a73578a259eb1053f19e8b1ef2f513aa1f20b1dcc253f5d8598bf80f0f3
---

[ExtensionAbility](../harmonyos-references/js-apis-app-ability-extensionability.md)组件是一种面向特定场景的应用组件。每一个具体场景对应一个不同类型的ExtensionAbility，例如用于卡片场景的[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)，用于输入法场景的[InputMethodExtensionAbility](../harmonyos-references/js-apis-inputmethod-extension-ability.md)，用于延时任务场景的[WorkSchedulerExtensionAbility](../harmonyos-references/js-apis-workschedulerextensionability.md)等。开发者通过使用不同类型的ExtensionAbility组件，可以扩展和丰富应用功能，更好地与其他应用或系统开展交互。

不同类型ExtensionAbility组件均由系统定义，且通常由相应的系统服务统一管理（例如[InputMethodExtensionAbility](../harmonyos-references/js-apis-inputmethod-extension-ability.md)组件由输入法管理服务统一管理）。开发者不能直接继承ExtensionAbility组件，只能使用（包括实现或访问）已定义的[ExtensionAbility类型](../harmonyos-references/js-apis-bundlemanager.md#extensionabilitytype)。

## ExtensionAbility类型说明

当前系统已定义的ExtensionAbility类型如下表所示。

说明

* “是否允许三方应用实现”是指：三方应用能否继承该类型ExtensionAbility实现自己的业务逻辑。
* “是否有独立Extension沙箱”是指：该类型ExtensionAbility的沙箱是否与主应用沙箱相对独立、不可互相访问。

| ExtensionAbility类型 | 功能描述 | 是否允许三方应用实现 | 是否有独立Extension沙箱 |
| --- | --- | --- | --- |
| [FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md) | 卡片扩展能力，用于提供[服务卡片](formkit-overview.md)的相关能力。 | 是 | 否 |
| [WorkSchedulerExtensionAbility](../harmonyos-references/js-apis-workschedulerextensionability.md) | 延时任务扩展能力，用于提供[延迟任务](work-scheduler.md)的相关能力。 | 是 | 否 |
| [InputMethodExtensionAbility](../harmonyos-references/js-apis-inputmethod-extension-ability.md) | 输入法扩展能力，用于实现[输入法应用](ime-kit-intro.md)的开发。 | 是 | 是 |
| ServiceExtensionAbility | 后台服务扩展能力，提供后台运行并对外提供相应能力。  三方应用可以连接该ExtensionAbility，并进行通信。 | 否 | 否 |
| [AccessibilityExtensionAbility](../harmonyos-references/js-apis-application-accessibilityextensionability.md) | 无障碍服务扩展能力，支持访问与操作前台界面。 | 是 | 否 |
| DataShareExtensionAbility | 数据共享扩展能力，用于对外提供数据读写服务。  三方应用可以连接该ExtensionAbility，进行数据读写。 | 否 | 否 |
| [BackupExtensionAbility](../harmonyos-references/js-apis-application-backupextensionability.md) | 数据备份扩展能力，用于提供[备份及恢复应用数据](app-file-backup-overview.md)的能力。 | 是 | 否 |
| [EnterpriseAdminExtensionAbility](../harmonyos-references/js-apis-enterpriseadminextensionability.md) | [企业设备管理扩展能力](mdm-kit-admin.md)，提供企业管理时处理管理事件的能力，  比如设备上应用安装事件、锁屏密码输入错误次数过多事件等。 | 是 | 否 |
| [PrintExtensionAbility](../harmonyos-references/js-apis-app-ability-printextensionability.md) | 文件[打印扩展能力](printextensionabilityguide.md)，提供应用打印照片、文档等办公场景。 | 是 | 否 |
| [ShareExtensionAbility](../harmonyos-references/js-apis-app-ability-shareextensionability.md) | 分享扩展组件，用于提供分享模板服务扩展的能力。 | 是 | 否 |
| [DriverExtensionAbility](../harmonyos-references/js-apis-app-ability-driverextensionability.md) | 驱动扩展能力，用于提供[驱动相关扩展框架](driverextensionability.md)。 | 是 | 否 |
| [ActionExtensionAbility](../harmonyos-references/js-apis-app-ability-actionextensionability.md) | 自定义服务扩展能力，为开发者提供基于UIExtension的自定义操作业务模板。 | 是 | 否 |
| [AdsServiceExtensionAbility](../harmonyos-references/js-apis-adsserviceextensionability.md) | 广告服务扩展能力，对外提供后台自定义广告业务服务。 | 是 | 否 |
| [EmbeddedUIExtensionAbility](../harmonyos-references/js-apis-app-ability-embeddeduiextensionability.md) | 嵌入式UI扩展能力，提供[跨进程界面嵌入](embeddeduiextensionability.md)的能力。 | 是 | 否 |
| [FenceExtensionAbility](../harmonyos-references/js-apis-app-ability-fenceextensionability.md) | 地理围栏扩展能力，用于提供[地理围栏](fenceextensionability.md)扩展的能力。 | 是 | 否 |
| [DistributedExtensionAbility](../harmonyos-references/js-apis-distributedextensionability.md) | 分布式扩展能力，提供分布式创建、销毁、连接的生命周期回调。 | 是 | 否 |
| [AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md) | 应用后台服务扩展能力，提供应用后台服务的创建、销毁、连接、断开等生命周期回调。 | 是 | 否 |
| [FaultLogExtensionAbility](../harmonyos-references/js-apis-hiviewdfx-faultlogextensionability.md) | 提供故障延迟通知的能力。 | 是 | 否 |
| [WebNativeMessagingExtensionAbility](../harmonyos-references/arkts-apis-web-webnativemessagingextensionability.md) | Web插件对接能力。提供插件对接native应用能力。 | 是 | 否 |
| [NotificationSubscriberExtensionAbility](../harmonyos-references/js-apis-notificationsubscriberextensionability.md) | 通知订阅拓展能力，用于发送通知数据到三方穿戴设备。 | 是 | 否 |
| [PartnerAgentExtensionAbility](../harmonyos-references/is-fusionconnectivity-partneragentextensionability.md) | 基于蓝牙通信技术，提供设备发现与设备下线的通知功能。 | 是 | 否 |
| [PhotoEditorExtensionAbility](../harmonyos-references/js-apis-app-ability-photoeditorextensionability.md) | 照片编辑扩展能力，提供给应用实现图片编辑的功能。 | 是 | 否 |
| [VpnExtensionAbility](../harmonyos-references/js-apis-vpnextensionability.md) | VPN扩展能力，提供三方VPN创建、销毁等生命周期回调。 | 是 | 否 |
| [FormEditExtensionAbility](../harmonyos-references/js-apis-app-form-formeditextensionability.md) | 卡片编辑扩展能力，提供卡片页面编辑能力，支持实现用户自定义卡片内容的功能，例如：编辑联系人卡片、修改卡片中展示的联系人、编辑天气卡片等。 | 是 | 否 |
| [LiveFormExtensionAbility](../harmonyos-references/js-apis-app-form-liveformextensionability.md) | 卡片动效扩展能力，提供卡片动效能力，例如卡片破框动效，丰富信息提醒、浅层交互功能，显著提升用户体验。 | 是 | 否 |
| [PushExtensionAbility](../harmonyos-references/push-extension-ability.md) | 推送扩展能力，提供获取场景化消息数据等能力。 | 是 | 否 |
| [InsightIntentUIExtensionAbility](../harmonyos-references/intents-arkts-api-insightintent-uiextension.md) | 为开发者提供能被小艺意图调用，以窗口形态呈现内容的扩展能力。 | 是 | 否 |
| [AssetAccelerationExtensionAbility](../harmonyos-references/graphics-accelerate-extensionability.md) | 资源预下载扩展能力，提供在设备闲时状态，进行后台资源预下载的能力。 | 是 | 否 |
| [VoIPExtensionAbility](../harmonyos-references/push-voip-ability.md) | 网音视频通话扩展能力，提供网络音视频通话服务。 | 是 | 否 |
| [RemoteLocationExtensionAbility](../harmonyos-references/remote-location-ability.md) | 远程定位扩展能力，提供查询用户位置的能力。 | 是 | 否 |
| [RemoteNotificationExtensionAbility](../harmonyos-references/push-remote-notification-extension-ability.md) | 远程通知扩展能力，提供获取场景化消息数据和生命周期结束的回调。 | 是 | 否 |
| [CallerInfoQueryExtensionAbility](../harmonyos-references/callservicekit-callerinfoquery-extension-ability.md) | 来电信息查询扩展能力，提供通话来去电页面显示企业联系人信息的能力。 | 是 | 否 |
| [StatusBarViewExtensionAbility](../harmonyos-references/statusbar-extension-ability.md) | 状态栏视图扩展能力，提供三方应用接入PC状态栏的能力。 | 是 | 否 |
| [TimeGuardExtensionAbility](../harmonyos-references/screentimeguard-timeguardextensionability.md) | 屏幕时间守护扩展能力，为开发者提供策略管控生效、停止和应用权限授予、取消时执行特定逻辑的能力。 | 是 | 否 |
| [LiveViewLockScreenExtensionAbility](../harmonyos-references/liveview-lock-screen-ability.md) | 锁屏沉浸实况窗扩展能力，提供通过实况窗开放能力和锁屏展示地图轨迹的能力。 | 是 | 否 |

说明

通常情况下，应用中（同一Bundle名称）所有同一类型的ExtensionAbility均运行在同一个独立进程。以下为例外场景：

* ServiceExtensionAbility（仅系统应用涉及）、DataShareExtensionAbility（仅系统应用涉及）与所有UIAbility均运行在同一个独立进程（主进程）。
* UIExtensionAbility以及继承该类型的ExtensionAbility可以通过module.json5配置文件中的[extensionProcessMode](module-configuration-file.md#extensionabilities标签)字段，配置进程运行模式。

## 访问指定类型的ExtensionAbility组件

所有类型的[ExtensionAbility](../harmonyos-references/js-apis-app-ability-extensionability.md)组件均不能被应用直接启动，而是由相应的系统管理服务拉起，以确保其生命周期受系统管控，使用时拉起，使用完销毁。ExtensionAbility组件的调用方无需关心目标ExtensionAbility组件的生命周期。

以[InputMethodExtensionAbility](../harmonyos-references/js-apis-inputmethod-extension-ability.md)组件为例进行说明，如下图所示，调用方应用发起对InputMethodExtensionAbility组件的调用，此时将先调用输入法管理服务，由输入法管理服务拉起InputMethodExtensionAbility组件，返回给调用方，同时开始管理其生命周期。

**图1** 使用InputMethodExtensionAbility组件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/doG5lksSSvaq8zhD2Y4jLA/zh-cn_image_0000002552957492.png?HW-CC-KV=V1&HW-CC-Date=20260427T233741Z&HW-CC-Expire=86400&HW-CC-Sign=8B77A7479CCF58C03504782048294BB757426560B53C131B659A5C9B2EB31BF2)

## 实现指定类型的ExtensionAbility组件

以实现卡片[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)为例进行说明。卡片框架提供了FormExtensionAbility基类，开发者通过派生此基类（如MyFormExtensionAbility），实现回调（如创建卡片的onCreate()回调、更新卡片的[onUpdateForm()](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonupdateform)回调等）来实现具体卡片功能，具体开发指导见[服务卡片](formkit-overview.md)。

卡片FormExtensionAbility实现方不用关心使用方何时去请求添加、删除卡片，FormExtensionAbility实例及其所在的[ExtensionAbility](../harmonyos-references/js-apis-app-ability-extensionability.md)进程的整个生命周期，都是由卡片管理系统服务FormManagerService进行调度管理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/Zwz-Fj-5RQmthcxXKD45Fg/zh-cn_image_0000002583477493.png?HW-CC-KV=V1&HW-CC-Date=20260427T233741Z&HW-CC-Expire=86400&HW-CC-Sign=6F2D7F99FD911E67538EFDCD73684A01DD9DDF9A283216AA878479C66E788928)

* **[EmbeddedUIExtensionAbility](embeddeduiextensionability.md)**
* **[使用AppServiceExtensionAbility组件实现后台服务](app-service-extension-ability.md)**
