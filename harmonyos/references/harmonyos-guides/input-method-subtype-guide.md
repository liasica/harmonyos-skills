---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/input-method-subtype-guide
title: 输入法子类型开发指南
breadcrumb: 指南 > 应用框架 > IME Kit（输入法开发服务） > 输入法子类型开发指南
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:128a9e44eba92d33941b7366ddb39f23ce9c2d0fa74a3741e6e5c601632c0d98
---

输入法子类型允许输入法展现不同的输入模式或语言，用户可以根据需要在不同模式和语言中切换。如输入法的中文键盘、英文键盘等，都属于输入法的子类型。

## 输入法子类型的配置与实现

1. 输入法应用开发者只需要注册实现一个InputMethodExtensionAbility，所有的输入法子类型共用该InputMethodExtensionAbility，在[module.json5配置文件](module-configuration-file.md)中添加[metadata](module-configuration-file.md#metadata标签)，name为ohos.extension.input\_method，用于配置所有子类型的资源信息。

   ```json5
   "extensionAbilities": [
     {
       "srcEntry": "./ets/InputMethodExtensionAbility/InputMethodService.ets",
       "name": "InputMethodService",
       "label": "$string:MainAbility_label",
       "description": "$string:extension_ability_descriptor",
       "type": "inputMethod",
       "exported": true,
       "metadata": [
         {
           "name": "ohos.extension.input_method",
           "resource": "$profile:input_method_config"
         }
       ]
     }
   ],
   ```
2. 子类型配置文件input\_method\_config.json需要放在应用资源目录的profile文件夹中，格式如下，字段释义参照[InputMethodSubtype](../harmonyos-references/js-apis-inputmethod-subtype.md#inputmethodsubtype)；开发者需要严格按照配置文件格式及字段进行子类型信息配置，locale字段的配置参照[i18n-locale-culture](i18n-locale-culture.md#实现原理)。

   ```json5
   {
     "subtypes": [
       {
         "icon": "$media:icon",
         "id": "InputMethodExtAbility",
         "label": "$string:english",
         "locale": "en-US",
         "mode": "lower"
       },
       {
         "icon": "$media:icon",
         "id": "InputMethodExtAbility1",
         "label": "$string:chinese",
         "locale": "zh-CN",
         "mode": "lower"
       }
     ]
   }
   ```
3. 输入法应用中监听子类型事件，根据不同的子类型，可以加载不同的软键盘界面，或者通过状态变量控制软键盘显示效果。

   ```typescript
   // 设置监听子类型事件，改变输入法应用界面
   inputMethodAbility.on('setSubtype', (inputMethodSubtype: InputMethodSubtype) => {
     if (inputMethodSubtype.id === 'InputMethodExtAbility') {
       AppStorage.setOrCreate('subtypeChange', CustomInputMethodSubtype.english);
     }
     if (inputMethodSubtype.id === 'InputMethodExtAbility1') {
       AppStorage.setOrCreate('subtypeChange', CustomInputMethodSubtype.chinese);
     }
   });
   ```

## 输入法子类型相关信息的获取

1. 开发者可以通过调用[getCurrentInputMethodSubtype](../harmonyos-references/js-apis-inputmethod.md#inputmethodgetcurrentinputmethodsubtype9)获取当前输入法应用的当前子类型。
2. 开发者可以通过调用[listCurrentInputMethodSubtype](../harmonyos-references/js-apis-inputmethod.md#listcurrentinputmethodsubtype9)获取当前输入法应用的所有子类型。
3. 开发者可以通过调用[listInputMethodSubtype](../harmonyos-references/js-apis-inputmethod.md#listinputmethodsubtype9)获取指定输入法应用的所有子类型。

## 输入法子类型的切换

1. 开发者可以通过调用[switchCurrentInputMethodSubtype](../harmonyos-references/js-apis-inputmethod.md#inputmethodswitchcurrentinputmethodsubtype9)切换当前输入法应用的子类型。
2. 开发者可以通过调用[switchCurrentInputMethodAndSubtype](../harmonyos-references/js-apis-inputmethod.md#inputmethodswitchcurrentinputmethodandsubtype9)切换至指定输入法应用的指定子类型。
