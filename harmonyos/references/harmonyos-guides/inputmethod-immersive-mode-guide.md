---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/inputmethod-immersive-mode-guide
title: 输入法应用沉浸模式
breadcrumb: 指南 > 应用框架 > IME Kit（输入法开发服务） > 输入法应用沉浸模式
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dc2ccd748f314141b73b1b6b468d1a6224ebb10b309add1e28897bc8168ff7b7
---

## 场景介绍

为了让应用能够提供一致的沉浸式体验，我们提供了前台应用和输入法应用之间的通信机制。通过该机制，输入法应用根据前台应用设置的沉浸模式来决定最终沉浸模式。

## 框架原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/gk6yAb7gRFK935Mt0Rj7dA/zh-cn_image_0000002736433367.png)

* 前台应用根据应用场景，设置应用期望的沉浸模式。
* 输入法框架在拉起输入法应用时会将前台应用期望的沉浸模式传递给输入法应用。
* 输入法应用根据前台应用的沉浸模式决定最终的沉浸模式，并设置最终沉浸模式给输入法框架。

## 接入指导

1. 前台应用设置编辑框沉浸模式[keyboardappearance](../harmonyos-references/ts-basic-components-textarea.md#keyboardappearance15)。示例代码如下。

   ```typescript
   TextArea({placeholder: '沉浸模式'})
     .keyboardAppearance(KeyboardAppearance.IMMERSIVE)

   TextArea({placeholder: '非沉浸模式'})
     .keyboardAppearance(KeyboardAppearance.NONE_IMMERSIVE)
   ```
2. 输入法应用订阅编辑框属性变化事件[editorAttributeChanged](../harmonyos-references/js-apis-inputmethodengine.md#oneditorattributechanged10)，通过回调参数EditorAttribute中的immersiveMode字段感知前台应用期望的沉浸模式。示例代码如下。

   ```typescript
   // 感知是否设置沉浸模式，如果是沉浸模式选择沉浸模式类型
   inputMethodEngine.getKeyboardDelegate().on("editorAttributeChanged", (attr : inputMethodEngine.EditorAttribute) => {
     console.info('recv editorAttributeChanged, immersiveMode: ', attr.immersiveMode);
     if (attr.immersiveMode == inputMethodEngine.ImmersiveMode.DARK_IMMERSIVE) {
       this.panel?.setImmersiveMode(inputMethodEngine.ImmersiveMode.DARK_IMMERSIVE);
       console.info('recv editorAttributeChanged, panel:', this.panel?.getImmersiveMode());
     }
   })
   ```
3. 输入法应用设置沉浸模式[setimmersivemode](../harmonyos-references/js-apis-inputmethodengine.md#setimmersivemode15)。

   * IMMERSIVE表示沉浸模式由输入法应用决定。
   * 输入法应用不能设置IMMERSIVE模式给输入法框架。
   * 如果输入法应用收到前台应用期望的沉浸模式为IMMERSIVE，建议输入法应用根据当前系统所处主题模式，将最终沉浸模式设置为浅色沉浸模式（LIGHT\_IMMERSIVE）或深色沉浸模式（DARK\_IMMERSIVE）。

   设置沉浸模式，示例代码如下。setImmersiveMode接口需使用[createPanel](../harmonyos-references/js-apis-inputmethodengine.md#createpanel10)获取到Panel实例后，通过实例调用。

   ```typescript
   // 感知是否设置沉浸模式，如果是沉浸模式选择沉浸模式类型
   inputMethodEngine.getKeyboardDelegate().on("editorAttributeChanged", (attr : inputMethodEngine.EditorAttribute) => {
     console.info('recv editorAttributeChanged, immersiveMode: ', attr.immersiveMode);
     if (attr.immersiveMode == inputMethodEngine.ImmersiveMode.DARK_IMMERSIVE) {
       this.panel?.setImmersiveMode(inputMethodEngine.ImmersiveMode.DARK_IMMERSIVE);
       console.info('recv editorAttributeChanged, panel:', this.panel?.getImmersiveMode());
     }
   })
   ```
