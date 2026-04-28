---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/inputmethod-application-guide
title: 实现一个输入法应用
breadcrumb: 指南 > 应用框架 > IME Kit（输入法开发服务） > 实现一个输入法应用
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c5845aa5c20d74aa3951a6db69d65f78b9706e24f506d2c4dd522a98361bf626
---

[InputMethodExtensionAbility](../harmonyos-references/js-apis-inputmethod-extension-ability.md)提供了onCreate()和onDestroy()生命周期回调，根据需要重写对应的回调方法。InputMethodExtensionAbility的生命周期如下：

* **onCreate()**

  服务被首次创建时触发该回调，开发者可以在此进行一些初始化的操作，例如注册公共事件监听等。

  说明

  如果服务已创建，再次启动该InputMethodExtensionAbility不会触发onCreate()回调。
* **onDestroy()**

  当不再使用服务且准备将该实例销毁时，触发该回调。开发者可以在该回调中清理资源，如注销监听等。

## 开发步骤

开发者在实现一个输入法应用时，需要在DevEco Studio工程中新建一个InputMethodExtensionAbility，具体步骤如下：

1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录，并命名为InputMethodExtensionAbility。
2. 在InputMethodExtensionAbility目录下，右键选择“New > File”，新建四个文件，分别为KeyboardController.ets、InputMethodService.ets、Index.ets以及KeyboardKeyData.ets。目录如下：

   ```
   1. /src/main/
   2. ├── ets/InputMethodExtensionAbility
   3. │       └──model/KeyboardController.ets      # 显示键盘
   4. │       └──InputMethodService.ets        # 自定义类继承InputMethodExtensionAbility并加上需要的生命周期回调
   5. │       └──pages
   6. │         └── Index.ets            # 绘制键盘，添加输入删除功能
   7. │         └── KeyboardKeyData.ets          # 键盘属性定义
   8. ├── resources/base/profile/main_pages.json
   ```

## 文件介绍

1. InputMethodService.ets文件。

   在InputMethodService.ets文件中，增加导入InputMethodExtensionAbility的依赖包，自定义类继承InputMethodExtensionAbility并加上需要的生命周期回调。

   ```
   1. import { InputMethodExtensionAbility } from '@kit.IMEKit';
   2. import Log from '../model/Log';
   3. import { keyboardController } from '../InputMethodExtensionAbility/model/KeyboardController';
   4. import { Want } from '@kit.AbilityKit';

   6. const TAG: string = 'ServiceExtAbility->';

   8. export default class ServiceExtAbility extends InputMethodExtensionAbility {
   9. onCreate(want: Want): void {
   10. this.addLog(`onCreate want: ${want.abilityName}`);
   11. keyboardController.onCreate(this.context);
   12. }

   14. onDestroy(): void {
   15. this.addLog('onDestroy');
   16. keyboardController.onDestroy();
   17. }

   19. addLog(message: string): void {
   20. Log.showInfo(TAG, `kikaInput-new: ${message}`);
   21. }
   22. }
   ```

   [InputMethodService.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/InputMethodExtensionAbility/InputMethodService.ets#L16-L40)
2. KeyboardController.ets文件。KeyboardController中除创建输入法窗口，设置输入法事件监听，实现文本插入、删除之外，还可以获取[输入法键盘与系统面板的偏移区域](../harmonyos-references/js-apis-inputmethodengine.md#getsystempanelcurrentinsets21)，输入法系统面板在不同设备上存在差异，当设备有系统面板时，输入法软键盘相对系统面板的偏移区域如图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/sG6OMuHvSJ-QRqXDQQOGPA/zh-cn_image_0000002583438361.png?HW-CC-KV=V1&HW-CC-Date=20260427T234135Z&HW-CC-Expire=86400&HW-CC-Sign=C43E7B4D22AC7FEC7CBECD8E49F7E905CFF81D2D50E69C37B645E42B475E8ABD)

   ```
   1. class KeyboardController {
   2. private barPosition: number = 0;
   3. private keyCodes: Array<number> = [];
   4. private mContext: InputMethodExtensionContext | undefined;
   5. private panel: inputMethodEngine.Panel | undefined;
   6. private isSpecialKeyPress: boolean = false;
   7. private isKeyboardShow: boolean = false;
   8. private inputHandle: InputHandler = InputHandler.getInstance();
   9. private mKeyboardDelegate: inputMethodEngine.KeyboardDelegate | undefined;

   11. constructor() {
   12. this.mContext = undefined;
   13. this.panel = undefined;
   14. this.mKeyboardDelegate = undefined;
   15. }

   17. public onCreate(context: InputMethodExtensionContext): void {
   18. this.mContext = context;
   19. this.inputHandle.addLog('onCreate');
   20. this.initWindow();
   21. this.registerListener();
   22. }

   24. public onDestroy(): void {
   25. this.inputHandle.addLog('onDestroy');
   26. this.unRegisterListener();
   27. this.destroyPanel();
   28. }

   30. private initWindow(): void {
   31. if (this.mContext === undefined) {
   32. return;
   33. }
   34. this.inputHandle.addLog('initWindow');
   35. let dis: display.Display | undefined = undefined;
   36. try {
   37. dis = display.getDefaultDisplaySync();
   38. } catch (err) {
   39. let error = err as BusinessError;
   40. Log.showError(TAG, `getDefaultDisplaySync catch error: ${error.code} ${error.message}`);
   41. return;
   42. }
   43. if (dis == undefined) {
   44. return;
   45. }
   46. this.inputHandle.addLog("initWindow-oncall display");
   47. let dWidth = dis.width;
   48. let dHeight = dis.height;
   49. let navigationBar_height = NAVIGATIONBAR_HEIGHT_DEFAULT;
   50. let keyHeightRate = KEYBOARD_HEIGHT_RATE_DEFAULT;
   51. AppStorage.setOrCreate('windowWidth', dis.width);
   52. AppStorage.setOrCreate('windowHeight', dis.height);
   53. let isLandscape = false;
   54. let isRkDevice = false;
   55. if (dis.width > dis.height) {
   56. isLandscape = true;
   57. AppStorage.setOrCreate('isLandscape', true);
   58. } else {
   59. AppStorage.setOrCreate('isLandscape', false);
   60. }
   61. if (dWidth === DEVICE_PHONE.width && dHeight === DEVICE_PHONE.height) {
   62. navigationBar_height = 0;
   63. keyHeightRate = KEYBOARD_HEIGHT_RATE_PHONE;
   64. } else if (dWidth === DEVICE_PHONE.height && dHeight === DEVICE_PHONE.width) {
   65. navigationBar_height = 0;
   66. keyHeightRate = KEYBOARD_HEIGHT_RATE_PHONE_LAND;
   67. } else if (dWidth === DEVICE_RK.width && dHeight === DEVICE_RK.height) {
   68. navigationBar_height = KEYBOARD_HEIGHT_RATE_DEFAULT;
   69. AppStorage.setOrCreate('isRkDevice', true);
   70. isRkDevice = true;
   71. } else if (dWidth === DEVICE_BIG.width && dHeight === DEVICE_BIG.height) {
   72. navigationBar_height = 0;
   73. keyHeightRate = KEYBOARD_HEIGHT_RATE_BIG_LAND;
   74. } else if (dWidth === DEVICE_BIG.height && dHeight === DEVICE_BIG.width) {
   75. navigationBar_height = 0;
   76. keyHeightRate = KEYBOARD_HEIGHT_RATE_BIG;
   77. }
   78. let keyHeight = dHeight * keyHeightRate;
   79. this.barPosition = dHeight - keyHeight - navigationBar_height;
   80. this.inputHandle.addLog(`initWindow-dWidth = ${dWidth};dHeight = ${dHeight};keyboard height = ${keyHeight};;navibar height = navigationBar_height`);
   81. this.inputHandle.addLog(`initWindow-deviceType = ${deviceInfo.deviceType}`);
   82. let panelInfo: inputMethodEngine.PanelInfo = {
   83. type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
   84. flag: inputMethodEngine.PanelFlag.FLG_FIXED
   85. }
   86. let inputStyle = StyleConfiguration.getInputStyle(isLandscape, isRkDevice, deviceInfo.deviceType);
   87. AppStorage.setOrCreate('inputStyle', inputStyle);
   88. inputMethodAbility.createPanel(this.mContext, panelInfo).then((panel: inputMethodEngine.Panel) => {
   89. this.panel = panel;
   90. panel.resize(dWidth, keyHeight).then(() => {
   91. panel.setUiContent('InputMethodExtensionAbility/pages/Index').then(() => {
   92. this.inputHandle.addLog('loadContent finished');
   93. })
   94. }).catch((err: BusinessError) => {
   95. Log.showError(TAG, `Failed to setUiContent: ${err.code} ${err.message}`);
   96. });
   97. }).catch((err: BusinessError) => {
   98. Log.showError(TAG, `Failed to resize: ${err.code} ${err.message}`);
   99. });
   100. }

   102. private destroyPanel(): void {
   103. this.inputHandle.addLog('destroyPanel');
   104. if (this.panel) {
   105. inputMethodAbility.destroyPanel(this.panel).then(() => {
   106. this.inputHandle.addLog('Succeeded in destroyPanel.');
   107. }).catch((err: BusinessError) => {
   108. Log.showError(TAG, `Failed to destroyPanel: ${err.code} ${err.message}`);
   109. });
   110. }
   111. }

   113. private resizePanel(): void {
   114. this.inputHandle.addLog('resizeWindow');
   115. let dis: display.Display | undefined = undefined;
   116. try {
   117. dis = display.getDefaultDisplaySync();
   118. } catch (err) {
   119. let error = err as BusinessError;
   120. Log.showError(TAG, `getDefaultDisplaySync catch error: ${error.code} ${error.message}`);
   121. return;
   122. }
   123. if (dis == undefined) {
   124. return;
   125. }
   126. this.inputHandle.addLog('resizeWindow-oncall display');
   127. let dWidth = dis.width;
   128. let dHeight = dis.height;
   129. let keyHeightRate = KEYBOARD_HEIGHT_RATE_DEFAULT;
   130. AppStorage.setOrCreate<number>('windowWidth', dis.width);
   131. AppStorage.setOrCreate<number>('windowHeight', dis.height);
   132. let isLandscape = false;
   133. let isRkDevice = false;
   134. if (dis.width > dis.height) {
   135. isLandscape = true;
   136. AppStorage.setOrCreate('isLandscape', true);
   137. } else {
   138. AppStorage.setOrCreate('isLandscape', false);
   139. }
   140. if (dWidth === DEVICE_PHONE.width && dHeight === DEVICE_PHONE.height) {
   141. keyHeightRate = KEYBOARD_HEIGHT_RATE_PHONE;
   142. } else if (dWidth === DEVICE_PHONE.height && dHeight === DEVICE_PHONE.width) {
   143. keyHeightRate = KEYBOARD_HEIGHT_RATE_PHONE_LAND;
   144. } else if (dWidth === DEVICE_RK.width && dHeight === DEVICE_RK.height) {
   145. AppStorage.setOrCreate('isRkDevice', true);
   146. isRkDevice = true;
   147. } else if (dWidth === DEVICE_BIG.width && dHeight === DEVICE_BIG.height) {
   148. keyHeightRate = KEYBOARD_HEIGHT_RATE_BIG_LAND;
   149. } else if (dWidth === DEVICE_BIG.height && dHeight === DEVICE_BIG.width) {
   150. keyHeightRate = KEYBOARD_HEIGHT_RATE_BIG;
   151. }
   152. let keyHeight = dHeight * keyHeightRate;
   153. let inputStyle = StyleConfiguration.getInputStyle(isLandscape, isRkDevice, deviceInfo.deviceType);
   154. AppStorage.setOrCreate('inputStyle', inputStyle);
   155. if (this.panel) {
   156. this.panel.resize(dWidth, keyHeight).then(() => {
   157. }).catch((err: BusinessError) => {
   158. this.inputHandle.addLog(`resizePanel err = ${err.code} ${err.message}`);
   159. })
   160. }
   161. }
   ```

   [KeyboardController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/InputMethodExtensionAbility/model/KeyboardController.ets#L348-L495)

   ```
   1. private registerListener(): void {
   2. this.inputHandle.addLog('registerListener');
   3. try {
   4. display.on('change', () => {
   5. this.inputHandle.addLog('screenChangeEvent');
   6. this.resizePanel();
   7. });
   8. } catch (err) {
   9. let error = err as BusinessError;
   10. Log.showError(TAG, `display on change catch error: ${error.code} ${error.message}`);
   11. }
   12. inputMethodAbility.on('inputStart',
   13. (kbController: inputMethodEngine.KeyboardController, textInputClient: inputMethodEngine.InputClient) => {
   14. this.inputHandle.addLog('keyboard inputStart');
   15. this.inputHandle.onInputStart(kbController, textInputClient);
   16. })

   18. // 设置监听子类型事件，改变输入法应用界面
   19. inputMethodAbility.on('setSubtype', (inputMethodSubtype: InputMethodSubtype) => {
   20. if (inputMethodSubtype.id === 'InputMethodExtAbility') {
   21. AppStorage.setOrCreate('subtypeChange', 0);
   22. }
   23. if (inputMethodSubtype.id === 'InputMethodExtAbility1') {
   24. AppStorage.setOrCreate('subtypeChange', 1);
   25. }
   26. });

   28. inputMethodAbility.on('inputStop', () => {
   29. this.inputHandle.addLog('keyboard inputStop');
   30. this.onDestroy();
   31. if (this.mContext) {
   32. this.mContext.destroy();
   33. }
   34. });

   36. this.inputHandle.addLog('pre on privateCommand');
   37. try {
   38. inputMethodAbility.on('privateCommand', (record: Record<string, inputMethodEngine.CommandDataType>) => {
   39. this.inputHandle.addLog(`keyboard privateCommand : ${record}`);
   40. Object.keys(record).forEach((key: string) => {
   41. this.inputHandle.addLog(`onPageShow private command key: ${key}, value: ${record[key]}`);
   42. })
   43. });
   44. } catch (err) {
   45. let error = err as BusinessError;
   46. this.inputHandle.addLog(`on privateCommand sendPrivateCommand catch error: ${error.code} ${error.message}`);
   47. }

   49. this.mKeyboardDelegate = inputMethodEngine.getKeyboardDelegate();

   51. this.mKeyboardDelegate.on('keyDown', (keyEvent: inputMethodEngine.KeyEvent) => {
   52. if (this.isKeyboardShow) {
   53. this.inputHandle.hideKeyboardSelf();
   54. }
   55. this.inputHandle.addLog(`keyDown: code = ${keyEvent.keyCode}`);
   56. let result = this.onKeyDown(keyEvent);
   57. this.inputHandle.addLog(`keyDown: result = ${result}`);
   58. return result;
   59. });

   61. this.mKeyboardDelegate.on('keyUp', (keyEvent: inputMethodEngine.KeyEvent) => {
   62. this.inputHandle.addLog(`keyUp: code = ${keyEvent.keyCode}`);
   63. let result = this.onKeyUp(keyEvent);
   64. this.inputHandle.addLog(`keyUp: result = ${result}`);
   65. return result;
   66. });
   67. this.mKeyboardDelegate.on('cursorContextChange', (x: number, y: number, height: number) => {
   68. let cursorInfo: CursorInfo = { x: x, y: y, height: height };
   69. this.inputHandle.setCursorInfo(cursorInfo);
   70. });
   71. if (isDebug) {
   72. this.mKeyboardDelegate.on('selectionChange',
   73. (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => {
   74. this.inputHandle.setSelectInfo('selectInfo: from(' + oldBegin + ',' + oldEnd + ') to (' + newBegin + ',' +
   75. newEnd + ')');
   76. });
   77. this.mKeyboardDelegate.on('textChange', (text: string) => {
   78. this.inputHandle.setTextInfo('textInfo: ' + text);
   79. });
   80. }
   81. }
   ```

   [KeyboardController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/InputMethodExtensionAbility/model/KeyboardController.ets#L497-L574)

   ```
   1. public isShiftKeyHold(): boolean {
   2. if (this.keyCodes.length === 0) {
   3. return false;
   4. }
   5. let preDownKey = this.keyCodes[0];
   6. return preDownKey === KeyCode.KEYCODE_SHIFT_LEFT || preDownKey === KeyCode.KEYCODE_SHIFT_RIGHT;
   7. }

   9. public onKeyDown(keyEvent: inputMethodEngine.KeyEvent): boolean {
   10. this.inputHandle.addLog('onKeyDown: code = ' + keyEvent.keyCode);
   11. let keyCode = keyEvent.keyCode;
   12. let idx = this.keyCodes.indexOf(keyCode);
   13. if (idx === -1) {
   14. this.keyCodes.push(keyCode);
   15. } else {
   16. this.inputHandle.addLog(`keyCode down is intercepted: ${keyCode}}`);
   17. }
   18. if (this.isShiftKeyHold() && this.keyCodes.length === 2 && !this.isKeyCodeAZ(keyCode)) {
   19. this.isSpecialKeyPress = true;
   20. return false;
   21. }
   22. if (this.isSpecialKeyPress || keyCode === KeyCode.KEYCODE_ALT_LEFT || keyCode === KeyCode.KEYCODE_ALT_RIGHT) {
   23. return false;
   24. }
   25. let keyValue: string = getHardKeyValue(keyCode, this.isShiftKeyHold());
   26. if (keyValue === '') {
   27. this.inputHandle.addLog('onKeyDown: unknown keyCode');
   28. this.isSpecialKeyPress = true;
   29. return false;
   30. }
   31. return this.inputHardKeyCode(keyValue, keyCode);
   32. }

   34. public onKeyUp(keyEvent: inputMethodEngine.KeyEvent): boolean {
   35. this.inputHandle.addLog('OnKeyUp: code = ' + keyEvent.keyCode);
   36. let keyCode = keyEvent.keyCode;
   37. let idx = this.keyCodes.indexOf(keyCode);
   38. if (idx !== -1) {
   39. this.keyCodes.splice(idx, 1);
   40. } else {
   41. this.inputHandle.addLog(`keyCode KeyUp is intercepted: ${keyCode}`);
   42. }

   44. // For KEYCODE_DEL/KEYCODE_FORWARD_DEL, processed in OnKeyDown, so just intercept it
   45. if (keyCode === 2055 || keyCode === 2071 || (keyCode >= 2012 && keyCode <= 2016)) {
   46. this.inputHandle.addLog(`special code: ${keyCode}`);
   47. return true;
   48. }

   50. if (this.isSpecialKeyPress) {
   51. let keyValue = getHardKeyValue(keyCode, this.isShiftKeyHold());
   52. if (!keyValue) {
   53. this.isSpecialKeyPress = true;
   54. }
   55. if (this.keyCodes.length === 0) {
   56. this.isSpecialKeyPress = false;
   57. }
   58. this.inputHandle.addLog(`OnKeyUp: this.isSpecialKeyPress: ${this.isSpecialKeyPress}`);
   59. return false;
   60. }
   61. return true;
   62. }

   64. public isKeyCodeAZ(keyCode: number): boolean {
   65. return keyCode >= KeyCode.KEYCODE_A && keyCode <= KeyCode.KEYCODE_Z;
   66. }

   68. public isKeyCodeNumber(keyCode: number): boolean {
   69. return (keyCode >= KeyCode.KEYCODE_0 && keyCode <= KeyCode.KEYCODE_9) ||
   70. (keyCode >= KeyCode.KEYCODE_NUMPAD_0 && keyCode <= KeyCode.KEYCODE_NUMPAD_9);
   71. }

   73. public inputHardKeyCode(keyValue: string, keyCode: number): boolean {
   74. this.inputHandle.addLog(`inputHardKeyCode keyValue is: ${keyValue}`);
   75. if (this.processFunctionKeys(keyValue)) {
   76. return true;
   77. }
   78. if (this.shiftKeys(keyValue)) {
   79. return false;
   80. }
   81. this.inputHandle.insertText(keyValue);
   82. return true;
   83. }

   85. public shiftKeys(keyValue: string): boolean {
   86. this.inputHandle.addLog(`shiftKeys keyValue is: ${keyValue}`);
   87. switch (keyValue) {
   88. case 'KEYCODE_SHIFT_LEFT':
   89. case 'KEYCODE_SHIFT_RIGHT':
   90. return true;
   91. default:
   92. return false;
   93. }
   94. }

   96. public processFunctionKeys(keyValue: string): boolean {
   97. this.inputHandle.addLog(`processFunctionKeys keyValue is: ${keyValue}`);
   98. switch (keyValue) {
   99. case "KEYCODE_DEL":
   100. this.inputHandle.deleteForward(1);
   101. return true;
   102. case "KEYCODE_FORWARD_DEL":
   103. this.inputHandle.deleteBackward(1);
   104. return true;
   105. case "KEYCODE_DPAD_UP":
   106. this.inputHandle.moveCursor(inputMethodEngine.Direction.CURSOR_UP);
   107. return true;
   108. case "KEYCODE_DPAD_DOWN":
   109. this.inputHandle.moveCursor(inputMethodEngine.Direction.CURSOR_DOWN);
   110. return true;
   111. case "KEYCODE_DPAD_LEFT":
   112. this.inputHandle.moveCursor(inputMethodEngine.Direction.CURSOR_LEFT);
   113. return true;
   114. case "KEYCODE_DPAD_RIGHT":
   115. this.inputHandle.moveCursor(inputMethodEngine.Direction.CURSOR_RIGHT);
   116. return true;
   117. default:
   118. return false;
   119. }
   120. }

   122. private unRegisterListener(): void {
   123. this.inputHandle.addLog('unRegisterListener');

   125. inputMethodAbility.off('inputStop', () => {
   126. this.inputHandle.addLog('inputStop off');
   127. });
   128. if (this.mKeyboardDelegate) {
   129. this.mKeyboardDelegate.off('keyDown');
   130. this.mKeyboardDelegate.off('keyUp');
   131. if (isDebug) {
   132. this.mKeyboardDelegate.off('cursorContextChange');
   133. this.mKeyboardDelegate.off('selectionChange');
   134. this.mKeyboardDelegate.off('textChange');
   135. }
   136. }
   137. }
   138. }

   140. export const keyboardController: KeyboardController = new KeyboardController();
   ```

   [KeyboardController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/InputMethodExtensionAbility/model/KeyboardController.ets#L576-L716)
3. KeyboardKeyData.ets文件。

   定义软键盘的按键显示内容。

   ```
   1. export interface keySourceListType {
   2. title: string,
   3. content: string,
   4. upperContent: string
   5. }

   7. export interface sourceListType {
   8. content: string
   9. }

   11. export enum MenuKey {
   12. NUMBER_KEY = '?123',
   13. NORMAL_KEY = 'ABC',
   14. SPECIAL_KEY = '=/\<'
   15. }

   17. export enum SubMenuType {
   18. NORMAL = 0,
   19. MENU = 1,
   20. EDIT = 2
   21. }

   23. export enum MenuType {
   24. NORMAL = 0,
   25. NUMBER = 1,
   26. SPECIAL = 2
   27. }

   29. export enum KeyState {
   30. LOWER_CASE = 0,
   31. ONCE_UPPER_CASE = 1,
   32. UPPER_CASE = 2
   33. }

   35. export let keySourceListData: keySourceListType[] = [
   36. {
   37. title: '1',
   38. content: 'q',
   39. upperContent: 'Q'
   40. },
   41. {
   42. title: '2',
   43. content: 'w',
   44. upperContent: 'W'
   45. },
   46. {
   47. title: '3',
   48. content: 'e',
   49. upperContent: 'E'
   50. },
   51. {
   52. title: '4',
   53. content: 'r',
   54. upperContent: 'R'
   55. },
   56. {
   57. title: '5',
   58. content: 't',
   59. upperContent: 'T'
   60. },
   61. {
   62. title: '6',
   63. content: 'y',
   64. upperContent: 'Y'
   65. },
   66. {
   67. title: '7',
   68. content: 'u',
   69. upperContent: 'U'
   70. },
   71. {
   72. title: '8',
   73. content: 'i',
   74. upperContent: 'I'
   75. },
   76. {
   77. title: '9',
   78. content: 'o',
   79. upperContent: 'O'
   80. },
   81. {
   82. title: '0',
   83. content: 'p',
   84. upperContent: 'P'
   85. },
   86. {
   87. title: String.fromCharCode(126),
   88. content: 'a',
   89. upperContent: 'A'
   90. },
   91. {
   92. title: String.fromCharCode(33),
   93. content: 's',
   94. upperContent: 'S'
   95. },
   96. {
   97. title: '@',
   98. content: 'd',
   99. upperContent: 'D'
   100. },
   101. {
   102. title: String.fromCharCode(35),
   103. content: 'f',
   104. upperContent: 'F'
   105. },
   106. {
   107. title: '%',
   108. content: 'g',
   109. upperContent: 'G'
   110. },
   111. {
   112. title: String.fromCharCode(39),
   113. content: 'h',
   114. upperContent: 'H'
   115. },
   116. {
   117. title: '&',
   118. content: 'j',
   119. upperContent: 'J'
   120. },
   121. {
   122. title: '*',
   123. content: 'k',
   124. upperContent: 'K'
   125. },
   126. {
   127. title: '?',
   128. content: 'l',
   129. upperContent: 'L'
   130. },
   131. {
   132. title: String.fromCharCode(72),
   133. content: 'z',
   134. upperContent: 'Z'
   135. },
   136. {
   137. title: String.fromCharCode(73),
   138. content: 'x',
   139. upperContent: 'X'
   140. },
   141. {
   142. title: String.fromCharCode(175),
   143. content: 'c',
   144. upperContent: 'C'
   145. },
   146. {
   147. title: String.fromCharCode(95),
   148. content: 'v',
   149. upperContent: 'V'
   150. },
   151. {
   152. title: String.fromCharCode(58),
   153. content: 'b',
   154. upperContent: 'B'
   155. },
   156. {
   157. title: String.fromCharCode(59),
   158. content: 'n',
   159. upperContent: 'N'
   160. },
   161. {
   162. title: String.fromCharCode(47),
   163. content: 'm',
   164. upperContent: 'M'
   165. }
   166. ]
   ```

   [KeyboardKeyData.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/model/KeyboardKeyData.ets#L16-L184)

   ```
   1. export let numberSourceListData: sourceListType[] = [
   2. {
   3. content: '1'
   4. },
   5. {
   6. content: '2'
   7. },
   8. {
   9. content: '3'
   10. },
   11. {
   12. content: '4'
   13. },
   14. {
   15. content: '5'
   16. },
   17. {
   18. content: '6'
   19. },
   20. {
   21. content: '7'
   22. },
   23. {
   24. content: '8'
   25. },
   26. {
   27. content: '9'
   28. },
   29. {
   30. content: '0'
   31. },
   32. {
   33. content: '@'
   34. },
   35. {
   36. content: '#'
   37. },
   38. {
   39. content: '$'
   40. },
   41. {
   42. content: '%'
   43. },
   44. {
   45. content: '&'
   46. },
   47. {
   48. content: '-'
   49. },
   50. {
   51. content: '+'
   52. },
   53. {
   54. content: '('
   55. },
   56. {
   57. content: ')'
   58. },
   59. {
   60. content: '/'
   61. },
   62. {
   63. content: '*'
   64. },
   65. {
   66. content: '"'
   67. },
   68. {
   69. content: "'"
   70. },
   71. {
   72. content: ':'
   73. },
   74. {
   75. content: ';'
   76. },
   77. {
   78. content: '!'
   79. },
   80. {
   81. content: '?'
   82. },

   84. ]

   86. export let symbolSourceListData: sourceListType[] = [
   87. {
   88. content: '~'
   89. },
   90. {
   91. content: '`'
   92. },
   93. {
   94. content: '|'
   95. },
   96. {
   97. content: '\u2022'
   98. },
   99. {
   100. content: '\u221A'
   101. },
   102. {
   103. content: '\u03A0'
   104. },
   105. {
   106. content: '\u00F7'
   107. },
   108. {
   109. content: '\u00D7'
   110. },
   111. {
   112. content: String.fromCharCode(182)
   113. },
   114. {
   115. content: '\u2206'
   116. },
   117. {
   118. content: String.fromCharCode(163)
   119. },
   120. {
   121. content: '\u20ac'
   122. },
   123. {
   124. content: String.fromCharCode(165)
   125. },
   126. {
   127. content: String.fromCharCode(162)
   128. },
   129. {
   130. content: String.fromCharCode(94)
   131. },
   132. {
   133. content: '\u00B0'
   134. },
   135. {
   136. content: '='
   137. },
   138. {
   139. content: String.fromCharCode(123)
   140. },
   141. {
   142. content: String.fromCharCode(125)
   143. },
   144. {
   145. content: String.fromCharCode(44)
   146. },
   147. {
   148. content: String.fromCharCode(92)
   149. },
   150. {
   151. content: String.fromCharCode(169)
   152. },
   153. {
   154. content: String.fromCharCode(174)
   155. },
   156. {
   157. content: '\u2122'
   158. },
   159. {
   160. content: '\u2105'
   161. },
   162. {
   163. content: '['
   164. },
   165. {
   166. content: ']'
   167. }
   168. ]
   ```

   [KeyboardKeyData.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/model/KeyboardKeyData.ets#L186-L355)
4. Index.ets文件。

   主要描绘了具体按键功能。如按下数字键，就会将数字内容在输入框中打印出来，按下删除键，就会将内容删除。

   ```
   1. import { deviceInfo } from '@kit.BasicServicesKit';
   2. import Log from '../../model/Log';
   3. import { EditView } from '../../components/EditView';
   4. import { InputHandler } from '../model/KeyboardController';
   5. import {
   6. MenuType,
   7. SubMenuType,
   8. } from '../../model/KeyboardKeyData';
   9. import { KeyMenu } from '../../components/KeyMenu';
   10. import { NumberMenu } from '../../components/NumberMenu';
   11. import { StyleConfiguration, KeyStyle } from '../../common/StyleConfiguration';
   12. import { SymbolMenu } from '../../components/SymbolMenu';
   13. import { Submenu } from '../../components/Submenu';
   14. import { TopMenu } from '../../components/TopMenu';
   15. import { inputMethodEngine } from '@kit.IMEKit';

   18. const DEVICE_TYPE: string = deviceInfo.deviceType;
   19. const TAG: string = 'index->';

   21. @Entry
   22. @Component
   23. struct Index {
   24. @Provide menuType: number = MenuType.NORMAL;
   25. @StorageLink('inputPattern') @Watch('inputPatternChange') inputPattern: InputType = InputType.Normal
   26. @StorageLink('submenuType') submenuType: number = SubMenuType.NORMAL;
   27. @StorageLink('isLandscape') @Watch('change') isLandscape: boolean = false;
   28. @StorageLink('isRkDevice') isRkDevice: boolean = true;
   29. @StorageLink('inputStyle') inputStyle: KeyStyle = StyleConfiguration.getInputStyle(this.isLandscape, this.isRkDevice, DEVICE_TYPE);
   30. private panel: inputMethodEngine.Panel | undefined;
   31. @StorageLink('subtypeChange') subtypeChange: number = 0;

   34. aboutToAppear(): void {
   35. // 感知是否设置沉浸模式，如果是沉浸模式选择沉浸模式类型
   36. inputMethodEngine.getKeyboardDelegate().on("editorAttributeChanged", (attr : inputMethodEngine.EditorAttribute) => {
   37. console.info('recv editorAttributeChanged, immersiveMode: ', attr.immersiveMode);
   38. if (attr.immersiveMode == 1) {
   39. this.panel?.setImmersiveMode(inputMethodEngine.ImmersiveMode.DARK_IMMERSIVE);
   40. console.info('recv editorAttributeChanged, panel:', this.panel?.getImmersiveMode());
   41. }
   42. })
   43. }

   45. onBackPress(): boolean {
   46. Log.showInfo(TAG, 'kikaInput onBackPress');
   47. this.submenuType = SubMenuType.NORMAL;
   48. InputHandler.getInstance().hideKeyboardSelf();
   49. return true;
   50. }

   52. inputPatternChange(): void {
   53. if (this.inputPattern === InputType.Number || this.inputPattern === InputType.PhoneNumber) {
   54. this.menuType = MenuType.NUMBER;
   55. } else {
   56. this.menuType = MenuType.NORMAL;
   57. }
   58. }

   60. change(): void {
   61. AppStorage.set('inputStyle', StyleConfiguration.getInputStyle(this.isLandscape, this.isRkDevice, DEVICE_TYPE));
   62. }

   66. build() {
   67. Stack() {
   68. Column() {
   69. TopMenu()
   70. Column() {
   71. if (this.submenuType > SubMenuType.NORMAL) {
   72. if (this.submenuType === SubMenuType.MENU) {
   73. Submenu()
   74. } else {
   75. EditView();
   76. }
   77. } else {
   78. if (this.menuType === MenuType.NORMAL) {
   79. if (this.subtypeChange == 0) {
   80. KeyMenu()
   81. } else {
   82. NumberMenu()
   83. }
   84. } else if (this.menuType === MenuType.NUMBER) {
   85. NumberMenu()
   86. } else {
   87. SymbolMenu()
   88. }
   89. }
   90. }
   91. .width('100%')
   92. .layoutWeight(1)
   93. .justifyContent(FlexAlign.Center)
   94. .backgroundColor('#D5D8DD')
   95. }
   96. .height('100%')
   97. }
   98. .height('100%')
   99. .backgroundColor(Color.White)
   100. }
   101. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/ets/InputMethodExtensionAbility/pages/Index.ets#L16-L127)
5. main\_pages.json文件。对应ets/InputMethodExtensionAbility/pages/路径下键盘的绘制页面。

   ```
   1. {
   2. "src": [
   3. "InputMethodExtensionAbility/pages/Index"
   4. ]
   5. }
   ```
6. 在工程Module对应的[module.json5配置文件](module-configuration-file.md)中注册InputMethodExtensionAbility，type标签需要设置为“inputMethod”，srcEntry标签表示当前InputMethodExtensionAbility组件所对应的代码路径。

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

## 约束与限制

为了降低InputMethodExtensionAbility能力被三方应用滥用的风险，现通过基础访问模式的功能约束对输入法应用进行安全管控。

说明

严格遵从基础访问模式的功能约束。在此模式下，开发者应仅提供基础打字功能，不应提供任何形式与网络交互相关的功能。系统会逐步增加基础访问模式的安全管控能力，包括但不限于：以独立进程和沙箱的方式运行Extension进程；禁止Extension进程创建子进程；进程间通信与网络访问等。因此未遵从此约定可能会导致功能异常。

## 示例效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/-MLhGLyUTT6j8e8TNtdmGA/zh-cn_image_0000002552958316.png?HW-CC-KV=V1&HW-CC-Date=20260427T234135Z&HW-CC-Expire=86400&HW-CC-Sign=12292EABFF81E62338D42972D60FED9FFACF479717F1CC7AC698EFDDC77F96A6)
