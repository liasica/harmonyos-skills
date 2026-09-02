---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-10
title: MDM设备控制管理：如何设置息屏时间
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > MDM设备控制管理：如何设置息屏时间
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:18+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:8c0dac2e470e6e474e601d25805314cace297f0758573300a039d4c70585329f
---

## 问题现象

MDM应用需要自定义息屏时间，通过[deviceSettings.setValue](../harmonyos-references/js-apis-enterprise-devicesettings.md#devicesettingssetvalue)设置3秒延迟息屏不生效。

## 背景知识

* [MDM Kit（企业设备管理服务）](../harmonyos-guides/mdm-kit.md)提供企业设备管理服务接入和开发指南。
* [@ohos.enterprise.deviceSettings （设备设置管理）](../harmonyos-references/js-apis-enterprise-devicesettings.md)本模块提供企业设备设置能力，包括设置、获取设备息屏时间等。

## 解决方案

[deviceSettings](../harmonyos-references/js-apis-enterprise-devicesettings.md)模块提供企业设备设置能力，包括设置、获取设备息屏时间等。使用[deviceSettings.setValue](../harmonyos-references/js-apis-enterprise-devicesettings.md#devicesettingssetvalue)接口，item参数设置为screenOff，设置设备息屏策略。

若需获取设备当前息屏时间，使用[deviceSettings.getValue](../harmonyos-references/js-apis-enterprise-devicesettings.md#devicesettingsgetvalue)接口，item参数设置为screenOff，返回设备息屏时间（单位：毫秒）。对于PC/2in1设备，返回设备电池供电下的息屏时间（单位：毫秒）。

**说明** 

* MDM应用开发需要[申请资质](../harmonyos-guides/mdm-kit-guide.md#申请资质)，并使用对应的证书和Profile才可以使用接口。
* 该接口使用需要ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS权限。
* 目前手机/平板可设置息屏时间范围与系统设置中的可选时间一致。可通过"设置"->"显示和亮度"->"休眠"，查看系统支持的休眠时间，当前手机系统最短休眠时间为15s。
* 当前永不息屏只在2in1设备上接通电源时才能生效。

## 常见FAQ

Q：MDM应用是否有与华为时间服务器同步时间的接口？

A：可以使用[getNTPServer](../harmonyos-references/js-apis-enterprise-systemmanager.md#systemmanagergetntpserver)方法来获取时间，同步时间。

Q：MDM应用如何实现无限期授权？

A：只要激活，正常进行授权后，后续永久授权。

Q：如何快速确认接口使用失败原因？

A：通过try-catch的形式捕获错误信息，并根据[企业设备管理错误码](../harmonyos-references/errorcode-enterprisedevicemanager.md)或[通用错误码](../harmonyos-references/errorcode-universal.md)排查。

Q：deviceSettings.setValue接口，item为'screenOff'，设置值"0"，为何报错误码401？

A：item为'screenOff'时，息屏时间需是正整数（单位毫秒），设置值"0"会报错误码401，当前手机系统最短休眠时间为15s。

Q：使用[systemManager.setNTPServer](../harmonyos-references/js-apis-enterprise-systemmanager.md#systemmanagersetntpserver)设置NTP服务器后，如何同步时间？

A：需在设备上进入"系统＞日期和时间＞自动设置"，开启自动设置开关后进行同步。

Q：企业应用如何设置系统壁纸？

A：可以使用[deviceSettings.setHomeWallpaper](../harmonyos-references/js-apis-enterprise-devicesettings.md#devicesettingssethomewallpaper20)接口设置桌面壁纸，使用[deviceSettings.setUnlockWallpaper](../harmonyos-references/js-apis-enterprise-devicesettings.md#devicesettingssetunlockwallpaper20)接口设置锁屏壁纸。

Q：MDM应用中通过setInterval设置的定时器，在手机断网息屏后过段时间不执行，如何处理？

A：手机息屏后系统会进入休眠状态，定时器会被系统挂起。可以通过[deviceSettings.setValue](../harmonyos-references/js-apis-enterprise-devicesettings.md#devicesettingssetvalue)接口将息屏时间设置较大值来延缓息屏，例如设置为30000000毫秒。若需保持设备不息屏，可以定期调用该接口刷新息屏时间。

Q：使用[deviceSettings.setValue](../harmonyos-references/js-apis-enterprise-devicesettings.md#devicesettingssetvalue)接口设置powerPolicy（设备电源策略）在手机和平板设备上不生效，如何处理？

A：powerPolicy（设备电源策略）仅支持PC/2in1设备，手机和平板设备不支持。策略设置后不会刷新"设置—电源和电池"页面。若后续规格更新，请参考[deviceSettings.setValue](../harmonyos-references/js-apis-enterprise-devicesettings.md#devicesettingssetvalue)官方文档。
