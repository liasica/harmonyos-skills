---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-shortcutinfo
title: ShortcutInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 已停止维护的接口 > bundle > ShortcutInfo
category: harmonyos-references
scraped_at: 2026-04-28T07:58:54+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:0aeb5223300b5a63856f6260a96d578a5cbc0570ebb12df2f7af3ce415f4a242
---

应用配置文件中定义的快捷方式信息，[FA模型](../harmonyos-guides/ability-terminology.md#fa模型)配置在[config.json](../harmonyos-guides/application-configuration-file-overview-fa.md)文件中进行配置，[Stage模型](../harmonyos-guides/ability-terminology.md#stage模型)配置在开发视图的resources/base/profile下面定义配置文件即可。

说明

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护。建议使用[bundleManager-ShortcutInfo](js-apis-bundlemanager-shortcutinfo.md)替代。

## ShortcutInfo(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager-ShortcutInfo](js-apis-bundlemanager-shortcutinfo.md#shortcutinfo-1)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 是 | 否 | 快捷方式所属应用程序的ID。 |
| bundleName | string | 是 | 否 | 包含该快捷方式的Bundle名称。 |
| hostAbility | string | 是 | 否 | 快捷方式的本地Ability信息。 |
| icon | string | 是 | 否 | 快捷方式的图标。 |
| iconId8+ | number | 是 | 否 | 快捷方式的图标ID。 |
| label | string | 是 | 否 | 快捷方式的名称。 |
| labelId8+ | number | 是 | 否 | 快捷方式的名称ID。 |
| disableMessage | string | 是 | 否 | 快捷方式的禁用消息。 |
| wants | Array<ShortcutWant> | 是 | 否 | 快捷方式意图列表。 |
| isStatic | boolean | 是 | 是 | 快捷方式是否为静态，取值为true表示是静态的快捷方式，取值为false表示不是静态的快捷方式。 |
| isHomeShortcut | boolean | 是 | 是 | 快捷方式是否为主页面快捷方式，取值为true表示是主页面快捷方式，取值为false表示不是主页面快捷方式。 |
| isEnabled | boolean | 是 | 是 | 是否启用快捷方式，取值为true表示启用快捷方式，取值为false表示停用快捷方式。 |
