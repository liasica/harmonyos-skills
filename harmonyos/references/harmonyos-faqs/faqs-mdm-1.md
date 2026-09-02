---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-1
title: 使用企业MDM应用权限调用API不生效
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > 使用企业MDM应用权限调用API不生效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:d05ed71d9990e681d0bdbe98eb9dd445f99c0a9b139ef79bb0d5ef675f51d733
---

## 问题现象

在调试企业MDM权限时，发现使用@ohos.enterprise.applicationManager模块中的applicationManager.addDisallowedRunningBundlesSync接口将应用添加到黑名单时没有生效。权限和黑名单的包名都是正确的，运行时也没有报错，这是什么原因？

## 背景知识

* [applicationManager.addDisallowedRunningBundlesSync](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanageradddisallowedrunningbundlessync)接口功能：添加应用至应用运行禁止名单，添加至禁止名单的应用不允许在当前/指定用户下运行。
* [bm工具](../harmonyos-guides/bm-tool.md)：Bundle Manager（包管理工具，简称bm）是实现应用安装、卸载、更新、查询等功能的工具，bm为开发者提供基本的应用安装包的调试能力。

## 问题定位

* 检查当前应用是否具备MDM资质，各项权限是否具备。
* 查看applicationManager.addDisallowedRunningBundlesSync接口的使用说明以及各属性参数的限制。

## 分析结论

非权限原因导致，applicationManager.addDisallowedRunningBundlesSync接口的参数appIds数组填入的应是应用ID，而不是应用包名，因此导致添加黑名单未生效。

## 修改建议

使用[applicationManager.addDisallowedRunningBundlesSync](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanageradddisallowedrunningbundlessync)接口添加应用至应用运行禁止名单，其参数appIds数组需要填入应用的ID。可以通过以下方式查询应用ID：

* 使用bm工具[查询应用信息命令](../harmonyos-guides/bm-tool.md#查询应用信息命令dump)获取APPID：bm dump -n (应用包名)。
* 通过项目ID查询项目下所有应用信息：[参考链接](../AppGallery-connect-References/agcapi-queryprojectdetail-0000001158365067.md)。

## 常见FAQ

Q：MDM应用黑名单接口addDisallowedRunningBundlesSync，加了黑名单之后，用户界面是什么样的？

A：禁止运行，此时点击图标无法打开。

Q：加了黑名单后用户可以在应用中心看到应用图标吗？

A：可以。

Q：是否可以随时使用[removeDisallowedRunningBundlesSync](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanagerremovedisallowedrunningbundlessync)接口移除黑名单？

A：可以。

Q：加了黑名单之后，外部应用是否可以间接拉起？

A：无法拉起。

Q：MDM Kit的约束与限制是什么？

A：要求SDK版本为5.0.0（API 12）及以上，且仅支持Stage模型和HarmonyOS NEXT设备。

Q：MDM Kit是否支持自定义设备管理策略？

A：MDM Kit支持自定义设备管理策略。[@ohos.enterprise.restrictions](../harmonyos-references/js-apis-enterprise-restrictions.md)模块提供设置通用限制类策略能力，可以实现全局禁用和解除禁用蓝牙、HDC、USB、Wi-Fi等特性。例如使用[restrictions.setDisallowedPolicy](../harmonyos-references/js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy24)接口设置禁用设备打印能力；使用[restrictions.setUserRestriction](../harmonyos-references/js-apis-enterprise-restrictions.md#restrictionssetuserrestriction)接口设置用户行为（包括APN设置、长按电源键打开电源菜单、修改以太网IP地址、修改设备名称、修改锁屏密码行为）的限制规则。

Q：添加应用的appIdentifier至白名单，后续会报错：[16000110](../harmonyos-references/errorcode-ability.md#section16000110-当前应用不在kiosk模式的列表内)当前应用不在Kiosk模式的列表内，是为什么？

A：若应用尚未安装，白名单下发时尝试将appIdentifier转为packageName，会因无法解析而失败，因此报错16000110。

Q：在[Kiosk模式](../harmonyos-references/js-apis-app-ability-kioskmanager.md)下，用户仍可通过设置界面停用应用，同时Kiosk模式退出，该行为是否符合预期？

A：当前规格如此，[Kiosk模式](../harmonyos-references/js-apis-app-ability-kioskmanager.md)下可以在设置中停用应用，应用停用后将退出Kiosk模式。

Q：在[Kiosk模式](../harmonyos-references/js-apis-app-ability-kioskmanager.md)下，仅将com.huawei.hmos.settings（设置应用主入口）加入白名单后，部分功能提示页面加载失败，设置中是否有必需加入项？

A：设置功能由多个独立应用或服务形式存在。当点击设置中的子功能时，系统会尝试拉起对应的独立应用模块，若这些模块未加入白名单，Kiosk模式会阻止其运行。即只要使用，就需加入白名单。

Q：MDM应用用户手动停用后，是否能在对手机进行管控？

A：MDM应用用户手动停用后，之前下发的策略是存在的。
