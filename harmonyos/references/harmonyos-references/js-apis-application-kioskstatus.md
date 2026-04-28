---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-kioskstatus
title: KioskStatus (Kiosk状态信息)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > KioskStatus (Kiosk状态信息)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:40+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b5686cad5ca9210705cbd45ed49fbaf0252304ca8694fe21e2fbd0a90ca6357d
---

表示Kiosk状态信息，包括系统是否处于Kiosk模式以及该模式下的应用信息。

说明

* 本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## KioskStatus

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isKioskMode | boolean | 否 | 否 | 当前系统是否处于Kiosk模式。true表示处于Kiosk模式，false表示不处于。 |
| kioskBundleName | string | 否 | 否 | 进入Kiosk模式的应用的名称。 |
| kioskBundleUid | number | 否 | 否 | 进入Kiosk模式的应用的UID。 |
