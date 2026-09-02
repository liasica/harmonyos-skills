---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-19
title: 为什么ArkTS API接口注释中@since版本看起来比接口实际引入时间更晚
breadcrumb: FAQ > DevEco Studio > 代码编辑 > 为什么ArkTS API接口注释中@since版本看起来比接口实际引入时间更晚
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:012a29a4af47ec751512e39326c65a2498f1df2de2762ba689e743bd37275366
---

**问题现象**

在DevEco Studio中查看ArkTS API的接口注释，或鼠标悬停在ArkTS API调用处时，发现某些接口标注的@since版本较高（例如@since 20），但实际这些接口在更早的版本（如API 19）就已经存在。

**原因说明**

HarmonyOS目前采用“多段式注释”策略来记录ArkTS API的变更历史。每当接口新增重要功能或发生行为变更（如支持卡片/元服务、变更异常错误码）时，均会追加一段新的注释，并标注此次变更生效的版本（即 @since X）。

* 在DevEco Studio中查看ArkTS API的声明文件时，IDE默认折叠旧版本的注释段落，只显示最新的一段。这可能导致开发者误以为该接口是从当前显示的高版本才开始引入的。实际上，默认展示的@since标注的是“最后一次变更的版本”，而非“首次引入的版本”。
* 在DevEco Studio中鼠标悬停在ArkTS API调用处时，IDE只会展示接口在“当前工程兼容的最低版本及以上版本”的相关信息。低于“当前工程兼容的最低版本”的接口信息不会展示。

**正确理解方式**

若需确认接口的最初引入版本，请展开完整的ArkTS API接口注释，查看最早的@since记录。

**示例**

以@ohos.inputMethodEngine.d.ts里inputMethodEngine.InputClient.getAttachOptions这个API为例：

```screen
declare namespace inputMethodEngine {
    interface InputClient {
        /**
         * Get input attachOptions.
         *
         * @returns { AttachOptions } return attach options.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 19
         */
        /**
         * Get input attachOptions.
         *
         * @returns { AttachOptions } return attach options.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        getAttachOptions(): AttachOptions;
    }
}
```

在此例中，使用两段注释说明API在19/20两个版本所出现的变化。getAttachOptions()最早在API 19引入，在部分不支持的设备上会抛出801错误码。从API 20起，所有设备均支持，不会再抛出801错误码。

|  |  |  |
| --- | --- | --- |
| 工程最低兼容版本  build-profile.json5中compatibleSdkVersion字段 | 查看SDK声明文件 | 鼠标悬停在接口调用处 |
| 5.0.0(12) | 只显示最新一段@since 20注释，其余折叠 | 分两段显示@since 19、@since 20注释内容 |
| 5.1.1(19) | 只显示最新一段@since 20注释，其余折叠 | 分两段显示@since 19、@since 20注释内容 |
| 6.0.0(20) | 只显示最新一段@since 20注释，其余折叠 | 只显示@since 20注释内容 |

开发者可能会误以为该API是API 20新增的。实际上，这个API自API 19起就已经引入了。
