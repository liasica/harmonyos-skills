---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/input-method-subtype-guide
title: 输入法子类型开发指南
breadcrumb: 指南 > 应用框架 > IME Kit（输入法开发服务） > 输入法子类型开发指南
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:27671bfca187fdeb6d0c90644bde4447d4151394d53ec93e50f7f1eb6ef585a9
---

输入法子类型允许输入法展现不同的输入模式或语言，用户可以根据需要在不同模式和语言中切换。如输入法的中文键盘、英文键盘等，都属于输入法的子类型。

## 输入法子类型的配置与实现

1. 输入法应用开发者只需要注册实现一个InputMethodExtensionAbility，所有的输入法子类型共用该InputMethodExtensionAbility，在[module.json5配置文件](module-configuration-file.md)中添加metadata，name为ohos.extension.input\_method，用于配置所有子类型的资源信息。

   ```
   1. "extensionAbilities": [
   2. {
   3. "srcEntry": "./ets/InputMethodExtensionAbility/InputMethodService.ets",
   4. "name": "InputMethodService",
   5. "label": "$string:MainAbility_label",
   6. "description": "$string:extension_ability_descriptor",
   7. "type": "inputMethod",
   8. "exported": true,
   9. "metadata": [
   10. {
   11. "name": "ohos.extension.input_method",
   12. "resource": "$profile:input_method_config"
   13. }
   14. ]
   15. }
   16. ],
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/module.json5#L36-L53)
2. 子类型配置文件input\_method\_config.json需要放在应用资源目录的profile文件夹中，格式如下，字段释义参照[InputMethodSubtype](../harmonyos-references/js-apis-inputmethod-subtype.md#inputmethodsubtype)；开发者需要严格按照配置文件格式及字段进行子类型信息配置，locale字段的配置参照[i18n-locale-culture](i18n-locale-culture.md#实现原理)。

   ```
   1. {
   2. "subtypes": [
   3. {
   4. "icon": "$media:icon",
   5. "id": "InputMethodExtAbility",
   6. "label": "$string:english",
   7. "locale": "en-US",
   8. "mode": "lower"
   9. },
   10. {
   11. "icon": "$media:icon",
   12. "id": "InputMethodExtAbility1",
   13. "label": "$string:chinese",
   14. "locale": "zh-CN",
   15. "mode": "lower"
   16. }
   17. ]
   18. }
   ```
3. 输入法应用中监听子类型事件，根据不同的子类型，可以加载不同的软键盘界面，或者通过状态变量控制软键盘显示效果。

   ```
   1. // 设置监听子类型事件，改变输入法应用界面
   2. inputMethodAbility.on('setSubtype', (inputMethodSubtype: InputMethodSubtype) => {
   3. if (inputMethodSubtype.id === 'InputMethodExtAbility') {
   4. AppStorage.setOrCreate('subtypeChange', 0);
   5. }
   6. if (inputMethodSubtype.id === 'InputMethodExtAbility1') {
   7. AppStorage.setOrCreate('subtypeChange', 1);
   8. }
   9. });
   ```

   [KeyboardController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/InputMethodExtensionAbility/model/KeyboardController.ets#L510-L520)

## 输入法子类型相关信息的获取

1. 开发者可以通过调用[getCurrentInputMethodSubtype](../harmonyos-references/js-apis-inputmethod.md#inputmethodgetcurrentinputmethodsubtype9)获取当前输入法应用的当前子类型。
2. 开发者可以通过调用[listCurrentInputMethodSubtype](../harmonyos-references/js-apis-inputmethod.md#listcurrentinputmethodsubtype9)获取当前输入法应用的所有子类型。
3. 开发者可以通过调用[listInputMethodSubtype](../harmonyos-references/js-apis-inputmethod.md#listinputmethodsubtype9)获取指定输入法应用的所有子类型。

## 输入法子类型的切换

1. 开发者可以通过调用[switchCurrentInputMethodSubtype](../harmonyos-references/js-apis-inputmethod.md#inputmethodswitchcurrentinputmethodsubtype9)切换当前输入法应用的子类型。
2. 开发者可以通过调用[switchCurrentInputMethodAndSubtype](../harmonyos-references/js-apis-inputmethod.md#inputmethodswitchcurrentinputmethodandsubtype9)切换至指定输入法应用的指定子类型。
