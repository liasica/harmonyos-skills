---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-35
title: 元服务如何获取设备ID
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 元服务如何获取设备ID
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:6391a055ea32621ec76c1c0f1aac60ddeeadc593526c7f206c36103373b4b3d7
---

## 问题现象

HarmonyOS应用里可以通过获取OAID和ODID获取设备标识，元服务不支持。元服务如何获取设备ID呢？

## 背景知识

AAID是应用匿名标识符，标识应用实例，只存在于安装期，长度36位。AAID具有更好的隐私属性。AAID具有以下特性：

* 匿名化、无隐私风险：AAID和已有的任何标识符都不关联，并且每个应用只能访问自己的AAID。
* 同一个设备上，同一个开发者的多个应用，AAID取值不同。
* 同一个设备上，不同开发者的应用，AAID取值不同。
* 不同设备上，同一个开发者的应用，AAID取值不同。
* 不同设备上，不同开发者的应用，AAID取值不同。

OAID是开放匿名设备标识符，非永久性。OAID保护用户隐私，提供个性化广告，支持广告转化分析。

ODID：开发者匿名设备标识符，它主要用于开放给开发者的设备标识，同一设备上运行的同一个开发者的应用，ODID相同。帮助开发者更好地理解用户在不同应用间的行为，从而提供更个性化的服务和推荐。

## 解决方案

HarmonyOS出于对用户隐私的保护不开放OAID、ODID等，开发者可以获取AAID，不过每次重新安装都会变化，具体可以参考[获取AAID](../harmonyos-guides/push-get-aaid.md)。

若需要获取在元服务卸载重装后保持不变的设备标识，可采用自行生成UUID并通过[Asset Store Kit](../harmonyos-guides/asset-store-kit-overview.md)持久化存储的方案。核心思路是首次启动时生成UUID并通过关键资产存储以持久化方式保存，后续读取已缓存的UUID实现跨卸载周期稳定标识。

实施步骤如下：

1. 在元服务首次启动时，检查关键资产存储中是否已存在缓存的UUID。
2. 若不存在，使用[util.generateRandomUUID](../harmonyos-references/js-apis-util.md#utilgeneraterandomuuid9)生成新的UUID，通过[asset.add](../harmonyos-references/js-apis-asset.md#assetadd)存入关键资产存储，设置IS\_PERSISTENT为true（需申请ohos.permission.STORE\_PERSISTENT\_DATA权限，该权限为user\_grant级别，需引导用户授权）。
3. 若存在，直接从关键资产存储读取已缓存的UUID上报后端。
4. 若业务需要跨设备用户识别，可集成华为账号Account Kit，通过静默登录获取OpenID/UnionID，后端维护"用户→设备UUID列表"映射关系。

## 常见FAQ

Q：开发者需要对比从元服务和应用处获取到的设备唯一标识符来区分不同设备的会话，AAID可以吗？

A：同一个设备上，同一个开发者的多个应用，AAID取值不同。该ID无法实现同设备会话绑定，AAID无法满足需求。

Q：应用和元服务如何在端侧做相关的数据分享？

A：应用和元服务对于OS来说，属于两个载体，不建议在端侧做相关的数据共享。如果确实需要，建议基于云端能力做数据拉通，账号有OpenID和UnionID，可以快速关联用户，具体可以参考[华为账号统一认证服务](../harmonyos-references/account-api-authentication.md)。

Q：ODID是否会通过工具被修改？

A：ODID由系统底层自动生成，普通工具无法直接修改。其生成规则依赖设备硬件和开发者证书信息，未开放修改接口，第三方应用无法通过常规手段篡改。

Q：AAID是否固定是36位，是否会变化？

A：AAID长度是固定的，值不是。

Q：使用UUID和关键资产存储方案生成的设备标识，在元服务卸载重装后是否保持不变？

A：是的。通过设置IS\_PERSISTENT为true，关键资产存储中的数据在元服务卸载后仍会保留，重新添加元服务后可读取到相同的UUID。

Q：UUID和关键资产存储方案生成的设备标识在恢复出厂设置后是否保留？

A：不保留。恢复出厂设置会清除关键资产存储中的所有数据，再次启动时UUID会重新生成。
