---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/switch-inputmethod-guide
title: 切换输入法应用
breadcrumb: 指南 > 应用框架 > IME Kit（输入法开发服务） > 切换输入法应用
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:70c1b83ad6ab7dd4b1f85192e501474741880fcb1b183bef2d933daf782bf37f
---

输入法框架服务提供了切换输入法应用的API，支持切换输入法、切换输入法和子类型、切换当前输入法的子类型。

说明

1. 以下接口的使用仅允许在当前输入法应用中调用。
2. 本示例假设已经在输入法应用中执行，如何实现一个输入法应用，请参考[实现一个输入法应用](inputmethod-application-guide.md)开发指导。

## 切换当前输入法子类型

1. 在已完成一个输入法应用的基础上，当输入法应用是当前输入法时，在输入法应用中使用[switchCurrentInputMethodSubtype](../harmonyos-references/js-apis-inputmethod.md#inputmethodswitchcurrentinputmethodsubtype9)接口，传入当前输入法的子类型[InputMethodSubtype](../harmonyos-references/js-apis-inputmethod-subtype.md#inputmethodsubtype)作为参数即可切换当前输入法子类型。

   ```
   1. async switchCurrentInputMethodSubtype(item: InputMethodSubtype) {
   2. try {
   3. await inputMethod.switchCurrentInputMethodSubtype(item);
   4. this.currentInputMethodSubtype = inputMethod.getCurrentInputMethodSubtype().id;
   5. } catch (err) {
   6. console.error(`SwitchCurrentInputMethodSubtype error: ${err.code} ${err.message}`);
   7. let error: BusinessError = err as BusinessError;
   8. }
   9. }
   ```

   [Submenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/components/Submenu.ets#L67-L77)
2. 输入法应用中注册子类型变化事件，根据不同子类型加载不同的输入界面。

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

## 切换输入法应用

在已完成一个输入法应用的基础上，当输入法应用是当前输入法时，在输入法应用中使用[switchInputMethod](../harmonyos-references/js-apis-inputmethod.md#inputmethodswitchinputmethod9)接口，传入目标输入法的[InputMethodProperty](../harmonyos-references/js-apis-inputmethod.md#inputmethodproperty8)信息，即可切换输入法到目标输入法。

```
1. async switchInputMethod(item: string) {
2. try {
3. this.inputMethods = await inputMethod.getSetting().getInputMethods(true); // 获取已使能的输入法列表
4. let currentInputMethod = inputMethod.getCurrentInputMethod(); // 获取当前输入法
5. for (let i = 0; i < this.inputMethods.length; i++) {
6. if (item != currentInputMethod.name) { // 判断不是当前输入法时，切换到该输入法，实际开发中可以切换到固定输入法
7. await inputMethod.switchInputMethod(this.inputMethods[i]);
8. }
9. }
10. } catch (err) {
11. let error = err as BusinessError;
12. Log.showError(TAG, `switchInputMethod catch error: ${error.code} ${error.message}`);
13. }
14. }
```

[Submenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/components/Submenu.ets#L55-L65)

## 切换输入法应用和子类型

在已完成一个输入法应用的基础上，当输入法应用是当前输入法时，在输入法应用中使用[switchCurrentInputMethodAndSubtype](../harmonyos-references/js-apis-inputmethod.md#inputmethodswitchcurrentinputmethodandsubtype9)接口，传入目标输入法的[InputMethodProperty](../harmonyos-references/js-apis-inputmethod.md#inputmethodproperty8)，目标输入法的子类型[InputMethodSubtype](../harmonyos-references/js-apis-inputmethod-subtype.md#inputmethodsubtype)信息，即可切换输入法到目标输入法的指定子类型。

```
1. import { inputMethod } from '@kit.IMEKit';

3. export class KeyboardController {
4. async switchInputMethodAndSubtype() {
5. try {
6. let inputMethods: Array<inputMethod.InputMethodProperty> =
7. await inputMethod.getSetting().getInputMethods(true); // 获取已使能的输入法列表
8. let currentInputMethod: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod(); // 获取当前输入法
9. for (let i = 0; i < inputMethods.length; i++) {
10. if (inputMethods[i].name != currentInputMethod.name) { // 判断不是当前输入法时，切换到该输入法，实际开发中可以切换到固定输入法
11. let subTypes = await inputMethod.getSetting().listInputMethodSubtype(inputMethods[i]); // 获取目标输入法的子类型
12. if (subTypes.length > 0) {
13. await inputMethod.switchCurrentInputMethodAndSubtype(inputMethods[i], subTypes[0]); // 本示例默认切换到获取的第一个子类型
14. }
15. return;
16. }
17. }
18. } catch (err) {
19. let error: BusinessError = err as BusinessError;
20. console.error(`Failed to switchCurrentInputMethodAndSubtype, code: ${err.code}, message: ${err.message}`);
21. }
22. }
23. }
```
