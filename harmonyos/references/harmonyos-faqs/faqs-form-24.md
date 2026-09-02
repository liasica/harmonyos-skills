---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-24
title: 卡片的生命周期回调函数有哪些
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 卡片的生命周期回调函数有哪些
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:566819513a61451a6e961c9c488351db6768211b18bcd8fd88f0d3b8dc2af325
---

## 问题现象

卡片的生命周期包含哪些回调函数。

## 背景知识

[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)卡片扩展模块，提供卡片创建、销毁、刷新等生命周期回调。

## 解决方案

| 回调函数 | 函数介绍 | 触发时机 | 使用限制 |
| --- | --- | --- | --- |
| [onAddForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonaddform) | 卡片提供方接收创建卡片的通知接口。 | 1. 拉起卡片管理页面预览卡片时。 2. 从卡片管理页面将卡片添加至桌面时。 3. 长按桌面卡片，将卡片移动并落至其他屏时。 4. 使用[FormMenu](../harmonyos-references/ohos-arkui-advanced-formmenu.md)将卡片添加至桌面时。 5. 长按桌面卡片，拖动卡片调整大小时。 | 1. 回调函数需返回[卡片数据绑定类](../harmonyos-references/js-apis-app-form-formbindingdata.md)。 2. 拉起卡片管理页面预览卡片时，仅触发当前预览卡片与前后两个卡片的onAddForm函数；通过左右滑动，可继续触发后续卡片的onAddForm函数。 3. 若卡片需要调整尺寸大小，应在[卡片配置文件form\_config.json](../harmonyos-guides/arkts-ui-widget-configuration.md#配置文件字段说明)中，将resizable设置为true。 |
| [onCastToNormalForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityoncasttonormalform) | 卡片提供方收到卡片使用方将临时卡片转常态卡片的通知接口。 | 卡片提供方收到卡片使用方将临时卡片转常态卡片的通知时。 | 当前卡片使用方不会使用临时卡片，不涉及该回调函数。 |
| [onUpdateForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonupdateform) | 卡片提供方接收携带参数的更新卡片的通知接口。 | 1. 将卡片添加至桌面时。 2. 长按桌面卡片，将卡片移动并落至其他屏时。 3. 桌面卡片设置为[被动刷新](../harmonyos-guides/arkts-ui-widget-interaction-overview.md#被动刷新)时。 4. 卡片页面组件使用reloadForms和reloadAllForms接口请求刷新卡片内容时，参考[卡片提供方批量请求刷新卡片内容](../harmonyos-guides/arkts-ui-widget-active-refresh.md#卡片提供方批量请求刷新卡片内容)。 5. 长按桌面卡片，拖动卡片调整大小时。 | 1. 若支持[卡片定时更新](../harmonyos-guides/arkts-ui-widget-passive-refresh.md#卡片定时刷新)/[卡片定点更新](../harmonyos-guides/arkts-ui-widget-passive-refresh.md#卡片定点刷新)/卡片使用方主动请求更新功能，则提供方需要重写该方法以支持数据更新。 2. [卡片定时更新](../harmonyos-guides/arkts-ui-widget-passive-refresh.md#卡片定时刷新)需在[卡片配置文件form\_config.json](../harmonyos-guides/arkts-ui-widget-configuration.md#配置文件字段说明)中，设置updateEnabled为true，且updateDuration设置为大于0的整数值。 3. [卡片定点更新](../harmonyos-guides/arkts-ui-widget-passive-refresh.md#卡片定点刷新)需在[卡片配置文件form\_config.json](../harmonyos-guides/arkts-ui-widget-configuration.md#配置文件字段说明)中，scheduledUpdateTime或multiScheduledUpdateTime设置需刷新的24小时制时刻。 4. 同时配置了定时刷新updateDuration和定点刷新scheduledUpdateTime时，定时刷新的优先级更高且定点刷新不会执行。如果想要配置定点刷新，则需要将updateDuration配置为0。 5. 若卡片需要调整尺寸大小，应在[卡片配置文件form\_config.json](../harmonyos-guides/arkts-ui-widget-configuration.md#配置文件字段说明)中，将resizable设置为true。 |
| [onChangeFormVisibility](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonchangeformvisibility) | 卡片提供方接收修改可见性的通知接口。 | 卡片可见性发生变更时。 | 仅对系统应用生效，且需要将formVisibleNotify配置为true。 |
| [onFormEvent](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonformevent) | 卡片提供方接收处理卡片事件的通知接口。 | 卡片页面组件使用postCardAction接口且action类型为message时，参考[卡片提供方主动刷新卡片内容](../harmonyos-guides/arkts-ui-widget-active-refresh.md#卡片提供方主动刷新卡片内容)。 | 无。 |
| [onRemoveForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonremoveform) | 卡片提供方接收销毁卡片的通知接口。 | 1. 卡片管理页面退出时。 2. 卡片从桌面上移除时。 3. 长按桌面卡片，拖动卡片调整大小时。 | 若卡片需要调整尺寸大小，应在[卡片配置文件form\_config.json](../harmonyos-guides/arkts-ui-widget-configuration.md#配置文件字段说明)中，将resizable设置为true。 |
| [onConfigurationUpdate](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonconfigurationupdate) | 卡片配置发生变更的通知接口。 | 当系统环境发生变更时（例如深色模式开关时）。 | 仅当FormExtensionAbility存活时才会触发onConfigurationUpdate回调，FormExtensionAbility创建后10秒内无操作将会被清理，此时无法触发。 |
| [onStop](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonstop12) | 卡片提供方的卡片进程退出的通知接口。 | 卡片提供方的卡片进程退出时。 | FormExtensionAbility创建后10秒内无操作将会被清理，卡片进程退出，此时会触发onStop回调。 |
| [onFormLocationChanged](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonformlocationchanged20) | 卡片提供方接收卡片位置变更的通知接口。 | 卡片添加至桌面时。 | 无。 |

典型场景介绍：

* 长按桌面应用图标，将卡片添加至桌面。
  + 长按桌面应用图标拉起卡片管理页面时，触发当前预览卡片及其前后的卡片的onAddForm回调函数；通过左右滑动，触发后续卡片的onAddForm回调函数。
  + 点击“添加至桌面”，触发onAddForm、onUpdateForm和onFormLocationChanged回调函数。
  + 退出卡片管理页面时，触发onRemoveForm回调函数，若有卡片添加至桌面，则触发次数比拉起卡片管理页面时触发的onAddForm次数少一次；若无卡片添加至桌面，直接退出，则与拉起卡片管理页面时触发的onAddForm次数相同。
  + 10秒内无操作，FormExtensionAbility被清理，触发onStop回调函数。
* 移动卡片并落至其他屏幕。
  + 松开卡片落至屏幕时，触发onUpdateForm回调函数。
  + 10秒内无操作，FormExtensionAbility被清理，触发onStop回调函数。
  + 若卡片配置文件的resizable字段设置为true，长按卡片唤起菜单时，卡片外出现尺寸调整框，触发onAddForm，触发次数与该卡片配置的，且设备支持的规格（supportDimensions）数量相同。

    拖动卡片时，触发onRemoveForm回调，触发次数与onAddForm次数相同。

    松开卡片落至屏幕时，除了触发onUpdateForm回调函数外，再次触发onAddForm。

    点击屏幕，取消尺寸调整框，触发onRemoveForm回调。

## 总结

卡片扩展模块FormExtensionAbility提供了包含卡片创建、销毁、刷新等生命周期，应用可以在不同的业务场景，根据触发时机需要在对应函数中执行操作。
