---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-inputmethod-in-custom-edit-box
title: 在自绘编辑框中使用输入法
breadcrumb: 指南 > 应用框架 > IME Kit（输入法开发服务） > 在自绘编辑框中使用输入法
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:58059606542501c27ee5a47382e0caff511964076ff3aa691331d7dd41acc981
---

在输入法框架中，可以通过[getController](../harmonyos-references/js-apis-inputmethod.md#inputmethodgetcontroller9)方法获取到[InputMethodController](../harmonyos-references/js-apis-inputmethod.md#inputmethodcontroller)实例来绑定输入法并监听输入法应用的各种操作，比如插入、删除、选择、光标移动等。这样就可以在自绘编辑框中使用输入法，并实现更加灵活和自由的编辑操作。

## 开发步骤

1. 开发者在自绘编辑框中使用输入法时，首先需要在DevEco Studio工程中新建一个ets文件，命名为自定义控件的名称，本示例中命名为CustomInput，在文件中定义一个自定义控件，并从@kit.IMEKit中导入inputMethod。

   ```
   1. import { inputMethod } from '@kit.IMEKit';

   3. @Component
   4. export struct CustomInput {
   5. build() {
   6. }
   7. }
   ```
2. 在控件中，使用Text组件作为自绘编辑框的文本显示组件，使用状态变量inputText作为Text组件要显示的内容。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { inputMethod } from '@kit.IMEKit';
   3. import Log from '../model/Log';

   5. const TAG = '[Submenu]';

   7. @Component
   8. export struct CustomInput {
   9. @State inputText: string = ''; // inputText作为Text组件要显示的内容
   10. private isAttach: boolean = false;
   11. private inputController: inputMethod.InputMethodController = inputMethod.getController();

   13. build() {
   14. Text(this.inputText) // Text组件作为自绘编辑框的文本显示组件。
   15. .fontSize(16)
   16. .width('100%')
   17. .lineHeight(40)
   18. .id('customInput')
   19. .height(45)
   20. .border({ color: '#554455', radius: 30, width: 1 })
   21. .maxLines(1)
   22. .onBlur(() => {
   23. this.off();
   24. })
   25. .onClick(() => {
   26. this.attachAndListener(); // 点击控件
   27. })
   28. }
   ```

   [CustomInput.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/components/CustomInput.ets#L17-L42)
3. 在控件中获取inputMethodController实例，先在文本点击时调用controller实例的attach方法绑定和拉起软键盘，再注册监听输入法插入文本、删除等方法。本示例仅展示插入、删除。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { inputMethod } from '@kit.IMEKit';
   3. import Log from '../model/Log';

   5. const TAG = '[Submenu]';

   7. @Component
   8. export struct CustomInput {
   9. @State inputText: string = ''; // inputText作为Text组件要显示的内容
   10. private isAttach: boolean = false;
   11. private inputController: inputMethod.InputMethodController = inputMethod.getController();

   13. build() {
   14. Text(this.inputText) // Text组件作为自绘编辑框的文本显示组件。
   15. .fontSize(16)
   16. .width('100%')
   17. .lineHeight(40)
   18. .id('customInput')
   19. .height(45)
   20. .border({ color: '#554455', radius: 30, width: 1 })
   21. .maxLines(1)
   22. .onBlur(() => {
   23. this.off();
   24. })
   25. .onClick(() => {
   26. this.attachAndListener(); // 点击控件
   27. })
   28. }
   29. async attachAndListener() { // 绑定和设置监听
   30. focusControl.requestFocus('customInput');
   31. try {
   32. await this.inputController.attach(true, {
   33. inputAttribute: {
   34. textInputType: inputMethod.TextInputType.TEXT,
   35. enterKeyType: inputMethod.EnterKeyType.SEARCH
   36. }
   37. });
   38. if (!this.isAttach) {
   39. this.inputController.on('insertText', (text) => {
   40. this.inputText += text;
   41. })
   42. this.inputController.on('deleteLeft', (length) => {
   43. this.inputText = this.inputText.substring(0, this.inputText.length - length);
   44. })
   45. this.isAttach = true;
   46. }
   47. } catch (err) {
   48. let error = err as BusinessError;
   49. Log.showError(TAG, `attach catch error: ${error.code} ${error.message}`);
   50. }
   51. }

   53. off() {
   54. this.isAttach = false;
   55. this.inputController.off('insertText');
   56. this.inputController.off('deleteLeft');
   57. }
   58. }
   ```

   [CustomInput.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/components/CustomInput.ets#L16-L68)
4. 在应用界面布局中引入该控件即可，此处假设使用界面为Index.ets和控件CustomInput.ets在同一目录下。

   ```
   1. CustomInput()
   ```

   [PrivatePreview.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/pages/PrivatePreview.ets#L127-L129)

## 示例效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/rZnyMhXWQmCR0qdFFT2D9w/zh-cn_image_0000002589244621.png?HW-CC-KV=V1&HW-CC-Date=20260429T053004Z&HW-CC-Expire=86400&HW-CC-Sign=DBE5F81C5025B909C81CA7DE0BE5CA8CCF5C067F1B32AB86B29F0ACEA7EE1F4F)
