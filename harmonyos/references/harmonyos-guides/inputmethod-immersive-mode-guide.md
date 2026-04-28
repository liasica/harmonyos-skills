---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/inputmethod-immersive-mode-guide
title: 输入法应用沉浸模式
breadcrumb: 指南 > 应用框架 > IME Kit（输入法开发服务） > 输入法应用沉浸模式
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7b78d319b5b8ffbd1ad0612d442ce621f9022451454831d2a1903ad908adfd36
---

## 场景介绍

为了让应用能够提供一致的沉浸式体验，我们提供了前台应用和输入法应用之间的通信机制。通过该机制，输入法应用根据前台应用设置的沉浸模式来决定最终沉浸模式。

## 框架原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/I84_EI32QWaObQxffUBMPA/zh-cn_image_0000002552958318.png?HW-CC-KV=V1&HW-CC-Date=20260427T234137Z&HW-CC-Expire=86400&HW-CC-Sign=E54B12E7657FBC39F0793AA7D4B9F46B965AC0B9F8C2B615FF29D0F99577ECB0)

* 前台应用根据应用场景，设置应用期望的沉浸模式。
* 输入法框架在拉起输入法应用时会将前台应用期望的沉浸模式传递给输入法应用。
* 输入法应用根据前台应用的沉浸模式决定最终的沉浸模式，并设置最终沉浸模式给输入法框架。

## 接入指导

1. 前台应用[设置编辑框沉浸模式](../harmonyos-references/ts-basic-components-textarea.md#keyboardappearance15)。示例代码如下。

   ```
   1. TextArea({placeholder: '沉浸模式'})
   2. .keyboardAppearance(KeyboardAppearance.IMMERSIVE)

   4. TextArea({placeholder: '非沉浸模式'})
   5. .keyboardAppearance(KeyboardAppearance.NONE_IMMERSIVE)
   ```

   [PrivatePreview.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/pages/PrivatePreview.ets#L131-L137)
2. 输入法应用[订阅编辑框属性变化事件](../harmonyos-references/js-apis-inputmethodengine.md#oneditorattributechanged10)，通过回调参数EditorAttribute中的immersiveMode字段感知前台应用期望的沉浸模式。示例代码如下。

   ```
   1. // 感知是否设置沉浸模式，如果是沉浸模式选择沉浸模式类型
   2. inputMethodEngine.getKeyboardDelegate().on("editorAttributeChanged", (attr : inputMethodEngine.EditorAttribute) => {
   3. console.info('recv editorAttributeChanged, immersiveMode: ', attr.immersiveMode);
   4. if (attr.immersiveMode == 1) {
   5. this.panel?.setImmersiveMode(inputMethodEngine.ImmersiveMode.DARK_IMMERSIVE);
   6. console.info('recv editorAttributeChanged, panel:', this.panel?.getImmersiveMode());
   7. }
   8. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/InputMethodExtensionAbility/pages/Index.ets#L56-L67)
3. 输入法应用[设置沉浸模式](../harmonyos-references/js-apis-inputmethodengine.md#setimmersivemode15)。

   * IMMERSIVE表示沉浸模式由输入法应用决定。
   * 输入法应用不能设置IMMERSIVE模式给输入法框架。
   * 如果输入法应用收到前台应用期望的沉浸模式为IMMERSIVE，建议输入法应用根据当前系统所处颜色模式，将最终沉浸模式设置为浅色沉浸模式（LIGHT\_IMMERSIVE）或深色沉浸模式（DARK\_IMMERSIVE）。

   设置沉浸模式，示例代码如下。setImmersiveMode接口需使用[createPanel](../harmonyos-references/js-apis-inputmethodengine.md#createpanel10)获取到Panel实例后，通过实例调用。

   ```
   1. // 感知是否设置沉浸模式，如果是沉浸模式选择沉浸模式类型
   2. inputMethodEngine.getKeyboardDelegate().on("editorAttributeChanged", (attr : inputMethodEngine.EditorAttribute) => {
   3. console.info('recv editorAttributeChanged, immersiveMode: ', attr.immersiveMode);
   4. if (attr.immersiveMode == 1) {
   5. this.panel?.setImmersiveMode(inputMethodEngine.ImmersiveMode.DARK_IMMERSIVE);
   6. console.info('recv editorAttributeChanged, panel:', this.panel?.getImmersiveMode());
   7. }
   8. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/InputMethodExtensionAbility/pages/Index.ets#L56-L67)
