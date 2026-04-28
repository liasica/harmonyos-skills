---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethodengine
title: @ohos.inputMethodEngine (输入法服务)
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > ArkTS API > @ohos.inputMethodEngine (输入法服务)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cb0e60c04956340ab9742c388e8f0bf5e9a3c08bdc5ffe34181d3a4155ddd1f5
---

本模块面向输入法应用（包括系统输入法应用、三方输入法应用），为输入法应用提供能力，包括：创建软键盘窗口、插入/删除字符、选中文本、监听物理键盘按键事件等。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { inputMethodEngine } from '@kit.IMEKit';
```

## 常量

PhonePC/2in1TabletTVWearable

功能键常量值、编辑框常量值及光标常量值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| ENTER\_KEY\_TYPE\_UNSPECIFIED | number | 0 | 无功能键。 |
| ENTER\_KEY\_TYPE\_GO | number | 2 | “前往”功能键。 |
| ENTER\_KEY\_TYPE\_SEARCH | number | 3 | “搜索”功能键。 |
| ENTER\_KEY\_TYPE\_SEND | number | 4 | “发送”功能键。 |
| ENTER\_KEY\_TYPE\_NEXT | number | 5 | “下一个”功能键。 |
| ENTER\_KEY\_TYPE\_DONE | number | 6 | “回车”功能键。 |
| ENTER\_KEY\_TYPE\_PREVIOUS | number | 7 | “前一个”功能键。 |
| ENTER\_KEY\_TYPE\_NEWLINE12+ | number | 8 | “换行”功能键。 |
| PATTERN\_NULL | number | -1 | 无特殊性编辑框。 |
| PATTERN\_TEXT | number | 0 | 文本编辑框。 |
| PATTERN\_NUMBER | number | 2 | 数字编辑框。 |
| PATTERN\_PHONE | number | 3 | 电话号码编辑框。 |
| PATTERN\_DATETIME | number | 4 | 日期编辑框。 |
| PATTERN\_EMAIL | number | 5 | 邮件编辑框。 |
| PATTERN\_URI | number | 6 | 超链接编辑框。 |
| PATTERN\_PASSWORD | number | 7 | 密码编辑框。 |
| PATTERN\_PASSWORD\_NUMBER11+ | number | 8 | 数字密码编辑框。 |
| PATTERN\_PASSWORD\_SCREEN\_LOCK11+ | number | 9 | 锁屏密码编辑框。 |
| PATTERN\_USER\_NAME20+ | number | 10 | 用户名编辑框。 |
| PATTERN\_NEW\_PASSWORD20+ | number | 11 | 新密码编辑框。 |
| PATTERN\_NUMBER\_DECIMAL20+ | number | 12 | 带小数点的数字编辑框。 |
| PATTERN\_ONE\_TIME\_CODE20+ | number | 13 | 验证码编辑框。 |
| OPTION\_ASCII | number | 20 | 允许输入ASCII值。 |
| OPTION\_NONE | number | 0 | 不指定编辑框输入属性。 |
| OPTION\_AUTO\_CAP\_CHARACTERS | number | 2 | 允许输入字符。 |
| OPTION\_AUTO\_CAP\_SENTENCES | number | 8 | 允许输入句子。 |
| OPTION\_AUTO\_WORDS | number | 4 | 允许输入单词。 |
| OPTION\_MULTI\_LINE | number | 1 | 允许输入多行。 |
| OPTION\_NO\_FULLSCREEN | number | 10 | 半屏样式。 |
| FLAG\_SELECTING | number | 2 | 编辑框处于选择状态。 |
| FLAG\_SINGLE\_LINE | number | 1 | 编辑框为单行。 |
| DISPLAY\_MODE\_PART | number | 0 | 编辑框显示为半屏。 |
| DISPLAY\_MODE\_FULL | number | 1 | 编辑框显示为全屏。 |
| CURSOR\_UP9+ | number | 1 | 光标上移。 |
| CURSOR\_DOWN9+ | number | 2 | 光标下移。 |
| CURSOR\_LEFT9+ | number | 3 | 光标左移。 |
| CURSOR\_RIGHT9+ | number | 4 | 光标右移。 |
| WINDOW\_TYPE\_INPUT\_METHOD\_FLOAT9+ | number | 2105 | 输入法应用窗口风格标识。 |

## inputMethodEngine.getInputMethodAbility9+

PhonePC/2in1TabletTVWearable

getInputMethodAbility(): InputMethodAbility

获取输入法应用客户端实例[InputMethodAbility](js-apis-inputmethodengine.md#inputmethodability)，仅支持输入法应用调用。

输入法应用获取该实例后，可订阅软键盘显示/隐藏请求事件、创建/销毁输入法面板等。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodAbility](js-apis-inputmethodengine.md#inputmethodability) | 输入法应用客户端。 |

**示例：**

```
1. let InputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
```

## inputMethodEngine.getKeyboardDelegate9+

PhonePC/2in1TabletTVWearable

getKeyboardDelegate(): KeyboardDelegate

获取客户端编辑事件监听代理实例[KeyboardDelegate](js-apis-inputmethodengine.md#keyboarddelegate)。

输入法应用获取该实例后，可订阅物理键盘按键事件、选中文本变化事件等。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [KeyboardDelegate](js-apis-inputmethodengine.md#keyboarddelegate) | 客户端编辑事件监听代理。 |

**示例：**

```
1. let KeyboardDelegate: inputMethodEngine.KeyboardDelegate = inputMethodEngine.getKeyboardDelegate();
```

## inputMethodEngine.getInputMethodEngine(deprecated)

PhonePC/2in1TabletTVWearable

getInputMethodEngine(): InputMethodEngine

获取输入法应用客户端实例[InputMethodEngine](js-apis-inputmethodengine.md#inputmethodenginedeprecated)。

输入法应用获取该实例后，可订阅软键盘显示/隐藏请求事件等。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[getInputMethodAbility](js-apis-inputmethodengine.md#inputmethodenginegetinputmethodability9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodEngine](js-apis-inputmethodengine.md#inputmethodenginedeprecated) | 输入法应用客户端。 |

**示例：**

```
1. let InputMethodEngine: inputMethodEngine.InputMethodEngine = inputMethodEngine.getInputMethodEngine();
```

## inputMethodEngine.createKeyboardDelegate(deprecated)

PhonePC/2in1TabletTVWearable

createKeyboardDelegate(): KeyboardDelegate

获取客户端编辑事件监听代理实例[KeyboardDelegate](js-apis-inputmethodengine.md#keyboarddelegate)。输入法应用获取该实例后，可订阅物理键盘按键事件、选中文本变化事件等。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[getKeyboardDelegate](js-apis-inputmethodengine.md#inputmethodenginegetkeyboarddelegate9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [KeyboardDelegate](js-apis-inputmethodengine.md#keyboarddelegate) | 客户端编辑事件监听代理。 |

**示例：**

```
1. let keyboardDelegate: inputMethodEngine.KeyboardDelegate = inputMethodEngine.createKeyboardDelegate();
```

## CommandDataType12+

PhonePC/2in1TabletTVWearable

type CommandDataType = number | string | boolean;

表示私有数据类型，接口参数具体类型根据其功能而定。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 类型 | 说明 |
| --- | --- |
| string | 表示值类型为字符串。 |
| number | 表示值类型为数字。 |
| boolean | 表示值类型为布尔值。 |

## SizeChangeCallback15+

PhonePC/2in1TabletTVWearable

type SizeChangeCallback = (size: window.Size, keyboardArea?: KeyboardArea) => void

当输入法面板大小变化时触发的回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [window.Size](arkts-apis-window-i.md#size7) | 是 | 当前面板大小。 |
| keyboardArea | [KeyboardArea](js-apis-inputmethodengine.md#keyboardarea15) | 否 | 当前面板中可作为键盘区域的大小。 |

## InputMethodEngine(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 8开始支持，API version 23开始废弃，建议使用[InputMethodAbility](js-apis-inputmethodengine.md#inputmethodability)替代。

下列API均需使用[getInputMethodEngine](js-apis-inputmethodengine.md#inputmethodenginegetinputmethodenginedeprecated)获取到InputMethodEngine实例后，通过实例调用。

### on('inputStart')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'inputStart', callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void

订阅输入法绑定成功事件。使用callback异步回调。

说明

从API version 8开始支持，API version 23开始废弃，建议使用[InputMethodAbility#on](js-apis-inputmethodengine.md#oninputstart9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: [KeyboardController](js-apis-inputmethodengine.md#keyboardcontroller), textInputClient: [TextInputClient](js-apis-inputmethodengine.md#textinputclientdeprecated)) => void | 是 | 回调函数，返回订阅输入法的KeyboardController和TextInputClient实例。 |

**示例：**

```
1. inputMethodEngine.getInputMethodEngine()
2. .on('inputStart',
3. (kbController: inputMethodEngine.KeyboardController, textClient: inputMethodEngine.TextInputClient) => {
4. let keyboardController: inputMethodEngine.KeyboardController = kbController;
5. let textInputClient: inputMethodEngine.TextInputClient = textClient;
6. });
```

### off('inputStart')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'inputStart', callback?: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void

取消订阅输入法绑定成功事件。

说明

从API version 8开始支持，API version 23开始废弃，建议使用[InputMethodAbility#off](js-apis-inputmethodengine.md#offinputstart9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: [KeyboardController](js-apis-inputmethodengine.md#keyboardcontroller), textInputClient: [TextInputClient](js-apis-inputmethodengine.md#textinputclientdeprecated)) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. inputMethodEngine.getInputMethodEngine()
2. .off('inputStart',
3. (kbController: inputMethodEngine.KeyboardController, textClient: inputMethodEngine.TextInputClient) => {
4. console.info('delete inputStart notification.');
5. });
```

### on('keyboardShow'|'keyboardHide')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'keyboardShow'|'keyboardHide', callback: () => void): void

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

说明

从API version 8开始支持，API version 23开始废弃，建议使用[InputMethodAbility#on](js-apis-inputmethodengine.md#onkeyboardshowkeyboardhide9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型。  -'keyboardShow'表示显示输入法软键盘。  -'keyboardHide'表示隐藏输入法软键盘。 |
| callback | () => void | 是 | 回调函数。 |

**示例：**

```
1. inputMethodEngine.getInputMethodEngine().on('keyboardShow', () => {
2. console.info('inputMethodEngine keyboardShow.');
3. });
4. inputMethodEngine.getInputMethodEngine().on('keyboardHide', () => {
5. console.info('inputMethodEngine keyboardHide.');
6. });
```

### off('keyboardShow'|'keyboardHide')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'keyboardShow'|'keyboardHide', callback?: () => void): void

取消订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

说明

从API version 8开始支持，API version 23开始废弃，建议使用[InputMethodAbility#off](js-apis-inputmethodengine.md#offkeyboardshowkeyboardhide9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要取消监听的输入法软键盘事件类型。  -'keyboardShow'表示显示输入法软键盘。  -'keyboardHide'表示隐藏输入法软键盘。 |
| callback | () => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. inputMethodEngine.getInputMethodEngine().off('keyboardShow');
2. inputMethodEngine.getInputMethodEngine().off('keyboardHide');
```

## InputMethodAbility

PhonePC/2in1TabletTVWearable

下列API均需使用[getInputMethodAbility](js-apis-inputmethodengine.md#inputmethodenginegetinputmethodability9)获取到InputMethodAbility实例后，通过实例调用。

### on('inputStart')9+

PhonePC/2in1TabletTVWearable

on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void

订阅输入法绑定成功事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: [KeyboardController](js-apis-inputmethodengine.md#keyboardcontroller), inputClient: [InputClient](js-apis-inputmethodengine.md#inputclient9)) => void | 是 | 回调函数，返回输入法操作相关实例。 |

**示例：**

```
1. inputMethodEngine.getInputMethodAbility()
2. .on('inputStart',
3. (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
4. let keyboardController: inputMethodEngine.KeyboardController = kbController;
5. let inputClient: inputMethodEngine.InputClient = client;
6. });
```

### off('inputStart')9+

PhonePC/2in1TabletTVWearable

off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void): void

取消订阅输入法绑定成功事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: [KeyboardController](js-apis-inputmethodengine.md#keyboardcontroller), inputClient: [InputClient](js-apis-inputmethodengine.md#inputclient9)) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. inputMethodEngine.getInputMethodAbility().off('inputStart');
```

### on('inputStop')9+

PhonePC/2in1TabletTVWearable

on(type: 'inputStop', callback: () => void): void

订阅停止输入法应用事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'inputStop'。 |
| callback | () => void | 是 | 回调函数。 |

**示例：**

```
1. inputMethodEngine.getInputMethodAbility().on('inputStop', () => {
2. console.info('inputMethodAbility inputStop');
3. });
```

### off('inputStop')9+

PhonePC/2in1TabletTVWearable

off(type: 'inputStop', callback: () => void): void

取消订阅停止输入法应用事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'inputStop'。 |
| callback | () => void | 是 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. inputMethodEngine.getInputMethodAbility().off('inputStop', () => {
2. console.info('inputMethodAbility delete inputStop notification.');
3. });
```

### on('setCallingWindow')9+

PhonePC/2in1TabletTVWearable

on(type: 'setCallingWindow', callback: (wid: number) => void): void

订阅设置调用窗口事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'setCallingWindow'。 |
| callback | (wid: number) => void | 是 | 回调函数，返回调用方窗口的Id。 |

**示例：**

```
1. inputMethodEngine.getInputMethodAbility().on('setCallingWindow', (wid: number) => {
2. console.info('inputMethodAbility setCallingWindow');
3. });
```

### off('setCallingWindow')9+

PhonePC/2in1TabletTVWearable

off(type: 'setCallingWindow', callback: (wid:number) => void): void

取消订阅设置调用窗口事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'setCallingWindow'。 |
| callback | (wid:number) => void | 是 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. inputMethodEngine.getInputMethodAbility().off('setCallingWindow', (wid: number) => {
2. console.info('inputMethodAbility delete setCallingWindow notification.');
3. });
```

### on('keyboardShow'|'keyboardHide')9+

PhonePC/2in1TabletTVWearable

on(type: 'keyboardShow'|'keyboardHide', callback: () => void): void

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型。  - 'keyboardShow'表示显示输入法软键盘。  - 'keyboardHide'表示隐藏输入法软键盘。 |
| callback | () => void | 是 | 回调函数。 |

**示例：**

```
1. inputMethodEngine.getInputMethodAbility().on('keyboardShow', () => {
2. console.info('InputMethodAbility keyboardShow.');
3. });
4. inputMethodEngine.getInputMethodAbility().on('keyboardHide', () => {
5. console.info('InputMethodAbility keyboardHide.');
6. });
```

### off('keyboardShow'|'keyboardHide')9+

PhonePC/2in1TabletTVWearable

off(type: 'keyboardShow'|'keyboardHide', callback?: () => void): void

取消订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型。  - 'keyboardShow'表示显示键盘。  - 'keyboardHide'表示隐藏键盘。 |
| callback | () => void | 否 | 回调函数。 |

**示例：**

```
1. inputMethodEngine.getInputMethodAbility().off('keyboardShow', () => {
2. console.info('InputMethodAbility delete keyboardShow notification.');
3. });
4. inputMethodEngine.getInputMethodAbility().off('keyboardHide', () => {
5. console.info('InputMethodAbility delete keyboardHide notification.');
6. });
```

### on('setSubtype')9+

PhonePC/2in1TabletTVWearable

on(type: 'setSubtype', callback: (inputMethodSubtype: InputMethodSubtype) => void): void

订阅设置输入法子类型事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'setSubtype'。 |
| callback | (inputMethodSubtype: [InputMethodSubtype](js-apis-inputmethod-subtype.md)) => void | 是 | 回调函数，返回设置的输入法子类型。 |

**示例：**

```
1. import { InputMethodSubtype } from '@kit.IMEKit';

3. inputMethodEngine.getInputMethodAbility().on('setSubtype', (inputMethodSubtype: InputMethodSubtype) => {
4. console.info('InputMethodAbility setSubtype.');
5. });
```

### off('setSubtype')9+

PhonePC/2in1TabletTVWearable

off(type: 'setSubtype', callback?: (inputMethodSubtype: InputMethodSubtype) => void): void

取消订阅设置输入法子类型事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'setSubtype'。 |
| callback | (inputMethodSubtype: [InputMethodSubtype](js-apis-inputmethod-subtype.md)) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. inputMethodEngine.getInputMethodAbility().off('setSubtype', () => {
2. console.info('InputMethodAbility delete setSubtype notification.');
3. });
```

### on('securityModeChange')11+

PhonePC/2in1TabletTVWearable

on(type: 'securityModeChange', callback: Callback< SecurityMode>): void

订阅输入法安全模式改变类型事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'securityModeChange'。 |
| callback | Callback<[SecurityMode](js-apis-inputmethodengine.md#securitymode11)> | 是 | 回调函数，返回当前输入法应用的安全模式。 |

**示例：**

```
1. inputMethodEngine.getInputMethodAbility()
2. .on('securityModeChange', (securityMode: inputMethodEngine.SecurityMode) => {
3. console.info(`InputMethodAbility securityModeChange, security is ${securityMode}`);
4. });
```

### off('securityModeChange')11+

PhonePC/2in1TabletTVWearable

off(type: 'securityModeChange', callback?: Callback< SecurityMode>): void

取消订阅输入法安全模式改变类型事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'securityModeChange'。 |
| callback | Callback<[SecurityMode](js-apis-inputmethodengine.md#securitymode11)> | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. let securityChangeCallback: (securityMode: inputMethodEngine.SecurityMode) => void =
2. (securityMode: inputMethodEngine.SecurityMode) => {
3. console.info(`InputMethodAbility securityModeChange, security is ${securityMode}`);
4. };
5. let inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
6. inputMethodAbility.on('securityModeChange', securityChangeCallback);
7. inputMethodAbility.off('securityModeChange', securityChangeCallback);
```

### on('privateCommand')12+

PhonePC/2in1TabletTVWearable

on(type: 'privateCommand', callback: Callback<Record<string, CommandDataType>>): void;

订阅输入法私有数据事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'privateCommand'。 |
| callback | Callback<Record<string, [CommandDataType](js-apis-inputmethodengine.md#commanddatatype12)>> | 是 | 回调函数，返回向输入法应用发送的私有数据。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800010 | not the preconfigured default input method. |

**示例：**

```
1. let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
2. (record: Record<string, inputMethodEngine.CommandDataType>) => {
3. for (let i :number = 0; i < record.length; i++) {
4. console.info(`private command key: ${i}, value: ${record[i]}`);
5. }
6. }
7. inputMethodEngine.getInputMethodAbility().on('privateCommand', privateCommandCallback);
```

### off('privateCommand')12+

PhonePC/2in1TabletTVWearable

off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void

取消订阅输入法私有数据事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'privateCommand'。 |
| callback | Callback<Record<string, [CommandDataType](js-apis-inputmethodengine.md#commanddatatype12)>> | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800010 | not the preconfigured default input method. |

**示例：**

```
1. let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
2. (record: Record<string, inputMethodEngine.CommandDataType>) => {
3. for (let i: number = 0; i < record.length; i++) {
4. console.info(`private command key: ${i}, value: ${record[i]}`);
5. }
6. }

8. inputMethodEngine.getInputMethodAbility().off('privateCommand', privateCommandCallback);
```

### on('callingDisplayDidChange')18+

PhonePC/2in1TabletTVWearable

on(type: 'callingDisplayDidChange', callback: Callback<number>): void

订阅编辑框对应窗口所在屏幕ID变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'callingDisplayDidChange'。 |
| callback | Callback<number> | 是 | 回调函数，返回编辑框设置对应窗口屏幕ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |

**示例：**

```
1. let callingDisplayDidChangeCallback: (num: number) => void = (num: number) => {
2. console.info(`display id: ${num}`);
3. }
4. inputMethodEngine.getInputMethodAbility().on('callingDisplayDidChange', callingDisplayDidChangeCallback);
```

### off('callingDisplayDidChange')18+

PhonePC/2in1TabletTVWearable

off(type: 'callingDisplayDidChange', callback?: Callback<number>): void

取消订阅编辑框对应窗口所在屏幕ID变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'callingDisplayDidChange'。 |
| callback | Callback<number> | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. inputMethodEngine.getInputMethodAbility().off('callingDisplayDidChange', (num: number) => {
2. console.info('InputMethodAbility delete calling display  notification.');
3. });
```

### on('discardTypingText')20+

PhonePC/2in1TabletTVWearable

on(type: 'discardTypingText', callback: Callback<void>): void

订阅编辑框应用发送“清空候选词”事件到输入法。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'discardTypingText'。  - 'discardTypingText'：表示订阅编辑框应用发送“清空候选词”事件到输入法。 |
| callback | Callback<void> | 是 | 回调函数。当命令发送成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. inputMethodEngine.getInputMethodAbility().on('discardTypingText', () => {
2. console.info('InputMethodAbility discard the typing text.');
3. });
```

### off('discardTypingText')20+

PhonePC/2in1TabletTVWearable

off(type: 'discardTypingText', callback?: Callback<void>): void

取消订阅编辑框应用发送“清空候选词”事件到输入法。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'discardTypingText'。  - 'discardTypingText'：表示取消订阅编辑框应用发送“清空候选词”事件到输入法。 |
| callback | Callback<void> | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. inputMethodEngine.getInputMethodAbility().off('discardTypingText', () => {
2. console.info('InputMethodAbility discard the typing text.');
3. });
```

### getSecurityMode11+

PhonePC/2in1TabletTVWearable

getSecurityMode(): SecurityMode

获取输入法应用的当前安全模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SecurityMode](js-apis-inputmethodengine.md#securitymode11) | 安全模式。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800004 | not an input method application. |

**示例：**

```
1. let security: inputMethodEngine.SecurityMode = inputMethodEngine.getInputMethodAbility().getSecurityMode();
2. console.error(`getSecurityMode, securityMode is : ${security}`);
```

### createPanel10+

PhonePC/2in1TabletTVWearable

createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void

创建输入法面板，仅支持输入法应用在[InputMethodExtensionAbility](js-apis-inputmethod-extension-ability.md#inputmethodextensionability)类中调用。使用callback异步回调。

说明

单个输入法应用仅允许创建一个[软键盘类型](js-apis-inputmethodengine.md#paneltype10)和一个[状态栏类型](js-apis-inputmethodengine.md#paneltype10)的面板。

输入法面板不支持创建子窗口。例如：不支持使用[window.createWindow](../harmonyos-guides/application-window-fa.md#设置应用子窗口)、[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu8)、[CustomDialog](ts-methods-custom-dialog-box.md)等接口创建子窗口弹窗。建议开发者采用非子窗的替代方案，如[弹出框](ohos-arkui-advanced-dialog.md)、[bindMenu](ts-universal-attributes-menu.md#bindmenu)或设置showInSubwindow为false。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | [BaseContext](js-apis-inner-application-basecontext.md) | 是 | 当前输入法应用上下文信息。 |
| info | [PanelInfo](js-apis-inputmethodengine.md#panelinfo10) | 是 | 输入法面板信息。 |
| callback | AsyncCallback<[Panel](js-apis-inputmethodengine.md#panel10)> | 是 | 回调函数。当输入法面板创建成功，返回当前创建的输入法面板对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800004 | not an input method application. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { inputMethodEngine, InputMethodExtensionAbility } from '@kit.IMEKit';
3. import { Want } from '@kit.AbilityKit';

5. let panelInfo: inputMethodEngine.PanelInfo = {
6. type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
7. flag: inputMethodEngine.PanelFlag.FLG_FIXED
8. }

10. class InputMethodExt extends InputMethodExtensionAbility {
11. onCreate(want: Want): void {
12. console.info(`onCreate, want: ${want.abilityName}`);
13. if (!this.context) {
14. inputMethodEngine.getInputMethodAbility()
15. .createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
16. if (err) {
17. console.error(`Failed to createPanel. Code is ${err.code}, message is ${err.message}`);
18. return;
19. }
20. console.info('Succeed in creating panel.');
21. })
22. }
23. }
24. }
```

### createPanel10+

PhonePC/2in1TabletTVWearable

createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>

创建输入法面板，仅支持输入法应用在[InputMethodExtensionAbility](js-apis-inputmethod-extension-ability.md#inputmethodextensionability)类中调用。使用promise异步回调。

说明

单个输入法应用仅允许创建一个[软键盘类型](js-apis-inputmethodengine.md#paneltype10)和一个[状态栏类型](js-apis-inputmethodengine.md#paneltype10)的面板。

输入法面板不支持创建子窗口。例如：不支持使用[window.createWindow](../harmonyos-guides/application-window-fa.md#设置应用子窗口)、[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu8)、[CustomDialog](ts-methods-custom-dialog-box.md)等接口创建子窗口弹窗。建议开发者采用非子窗的替代方案，如[弹出框](ohos-arkui-advanced-dialog.md)、[bindMenu](ts-universal-attributes-menu.md#bindmenu)或设置showInSubwindow为false。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | [BaseContext](js-apis-inner-application-basecontext.md) | 是 | 当前输入法应用上下文信息。 |
| info | [PanelInfo](js-apis-inputmethodengine.md#panelinfo10) | 是 | 输入法面板信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Panel](js-apis-inputmethodengine.md#panel10)> | 回调函数。当输入法面板创建成功，返回当前创建的输入法面板对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800004 | not an input method application. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { inputMethodEngine, InputMethodExtensionAbility } from '@kit.IMEKit';
3. import { Want } from '@kit.AbilityKit';

5. let panelInfo: inputMethodEngine.PanelInfo = {
6. type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
7. flag: inputMethodEngine.PanelFlag.FLG_FIXED
8. }

10. class InputMethodExt extends InputMethodExtensionAbility {
11. onCreate(want: Want): void {
12. console.info(`onCreate, want: ${want.abilityName}`);
13. if (this.context) {
14. inputMethodEngine.getInputMethodAbility().createPanel(this.context, panelInfo)
15. .then((panel: inputMethodEngine.Panel) => {
16. console.info('Succeed in creating panel.');
17. }).catch((err: BusinessError) => {
18. console.error(`Failed to create panel. Code is ${err.code}, message is ${err.message}`);
19. })
20. }
21. }
22. }
```

### destroyPanel10+

PhonePC/2in1TabletTVWearable

destroyPanel(panel: Panel, callback: AsyncCallback<void>): void

销毁输入法面板。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| panel | [Panel](js-apis-inputmethodengine.md#panel10) | 是 | 要销毁的面板对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当输入法面板销毁成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let panelInfo: inputMethodEngine.PanelInfo = {
4. type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
5. flag: inputMethodEngine.PanelFlag.FLG_FIXED
6. }

8. let inputPanel: inputMethodEngine.Panel | undefined = undefined;
9. if (this.context) {
10. inputMethodEngine.getInputMethodAbility()
11. .createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
12. if (err) {
13. console.error(`Failed to create panel. Code is ${err.code}, message is ${err.message}`);
14. return;
15. }
16. inputPanel = panel;
17. console.info('Succeed in creating panel.');
18. })
19. }

21. if (inputPanel) {
22. inputMethodEngine.getInputMethodAbility().destroyPanel(inputPanel, (err: BusinessError) => {
23. if (err !== undefined) {
24. console.error(`Failed to destroy panel. Code is ${err.code}, message is ${err.message}`);
25. return;
26. }
27. console.info('Succeed in destroying panel.');
28. })
29. }
```

### destroyPanel10+

PhonePC/2in1TabletTVWearable

destroyPanel(panel: Panel): Promise<void>

销毁输入法面板。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| panel | [Panel](js-apis-inputmethodengine.md#panel10) | 是 | 要销毁的面板对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let panelInfo: inputMethodEngine.PanelInfo = {
4. type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
5. flag: inputMethodEngine.PanelFlag.FLG_FIXED
6. }

8. let inputPanel: inputMethodEngine.Panel | undefined = undefined;
9. if (this.context) {
10. inputMethodEngine.getInputMethodAbility()
11. .createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
12. if (err) {
13. console.error(`Failed to create panel. Code is ${err.code}, message is ${err.message}`);
14. return;
15. }
16. inputPanel = panel;
17. console.info('Succeed in creating panel.');
18. })
19. }

21. if (inputPanel) {
22. inputMethodEngine.getInputMethodAbility().destroyPanel(inputPanel).then(() => {
23. console.info('Succeed in destroying panel.');
24. }).catch((err: BusinessError) => {
25. console.error(`Failed to destroy panel. Code is ${err.code}, message is ${err.message}`);
26. });
27. }
```

## KeyboardDelegate

PhonePC/2in1TabletTVWearable

下列API均需使用[getKeyboardDelegate](js-apis-inputmethodengine.md#inputmethodenginegetkeyboarddelegate9)获取到KeyboardDelegate实例后，通过实例调用。

### on('keyDown'|'keyUp')

PhonePC/2in1TabletTVWearable

on(type: 'keyDown'|'keyUp', callback: (event: KeyEvent) => boolean): void

订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型。  - 'keyDown'表示键盘按下。  - 'keyUp'表示键盘抬起。 |
| callback | (event: [KeyEvent](js-apis-inputmethodengine.md#keyevent)) => boolean | 是 | 回调函数，返回按键信息。 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。 |

**示例：**

```
1. inputMethodEngine.getKeyboardDelegate().on('keyUp', (keyEvent: inputMethodEngine.KeyEvent) => {
2. console.info(`inputMethodEngine keyCode.(keyUp): ${keyEvent.keyCode}`);
3. console.info(`inputMethodEngine keyAction.(keyUp): ${keyEvent.keyAction}`);
4. return true;
5. });
6. inputMethodEngine.getKeyboardDelegate().on('keyDown', (keyEvent: inputMethodEngine.KeyEvent) => {
7. console.info(`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}`);
8. console.info(`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}`);
9. return true;
10. });
```

### off('keyDown'|'keyUp')

PhonePC/2in1TabletTVWearable

off(type: 'keyDown'|'keyUp', callback?: (event: KeyEvent) => boolean): void

取消订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型。  - 'keyDown'表示键盘按下。  - 'keyUp'表示键盘抬起。 |
| callback | (event: [KeyEvent](js-apis-inputmethodengine.md#keyevent)) => boolean | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. inputMethodEngine.getKeyboardDelegate().off('keyUp', (keyEvent: inputMethodEngine.KeyEvent) => {
2. console.info('delete keyUp notification.');
3. return true;
4. });
5. inputMethodEngine.getKeyboardDelegate().off('keyDown', (keyEvent: inputMethodEngine.KeyEvent) => {
6. console.info('delete keyDown notification.');
7. return true;
8. });
```

### on('keyEvent')10+

PhonePC/2in1TabletTVWearable

on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void

订阅硬键盘（即物理键盘）事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'keyEvent'。 |
| callback | (event: [InputKeyEvent](js-apis-keyevent.md#keyevent)) => boolean | 是 | 回调函数，入参为按键事件信息，返回值类型为布尔类型。  - 入参按键事件信息的数据类型为[InputKeyEvent](js-apis-keyevent.md#keyevent)。  - 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。 |

**示例：**

```
1. import type { KeyEvent } from '@kit.InputKit';

3. inputMethodEngine.getKeyboardDelegate().on('keyEvent', (keyEvent: KeyEvent) => {
4. console.info(`inputMethodEngine keyEvent.action:${ keyEvent.action}`);
5. console.info(`inputMethodEngine keyEvent.key.code: ${keyEvent.key.code}`);
6. console.info(`inputMethodEngine keyEvent.ctrlKey: ${keyEvent.ctrlKey}`);
7. console.info(`inputMethodEngine keyEvent.unicodeChar: ${keyEvent.unicodeChar}`);
8. return true;
9. });
```

### off('keyEvent')10+

PhonePC/2in1TabletTVWearable

off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void

取消订阅硬键盘（即物理键盘）事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'keyEvent'。 |
| callback | (event: [InputKeyEvent](js-apis-keyevent.md#keyevent)) => boolean | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. import type { KeyEvent } from '@kit.InputKit';

3. inputMethodEngine.getKeyboardDelegate().off('keyEvent', (keyEvent: KeyEvent) => {
4. console.info('This is a callback function which will be deregistered.');
5. return true;
6. });
7. inputMethodEngine.getKeyboardDelegate().off('keyEvent');
```

### on('cursorContextChange')

PhonePC/2in1TabletTVWearable

on(type: 'cursorContextChange', callback: (x: number, y:number, height:number) => void): void

订阅光标变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 光标变化事件，固定取值为'cursorContextChange'。 |
| callback | (x: number, y: number, height: number) => void | 是 | 回调函数，返回光标信息。  - x为光标上端的x坐标值，y为光标上端的y坐标值，height为光标的高度值。 |

**示例：**

```
1. inputMethodEngine.getKeyboardDelegate().on('cursorContextChange', (x: number, y: number, height: number) => {
2. console.info('inputMethodEngine cursorContextChange x:' + x);
3. console.info('inputMethodEngine cursorContextChange y:' + y);
4. console.info('inputMethodEngine cursorContextChange height:' + height);
5. });
```

### off('cursorContextChange')

PhonePC/2in1TabletTVWearable

off(type: 'cursorContextChange', callback?: (x: number, y: number, height: number) => void): void

取消订阅光标变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 光标变化事件，固定取值为'cursorContextChange'。 |
| callback | (x: number, y:number, height:number) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. inputMethodEngine.getKeyboardDelegate().off('cursorContextChange', (x: number, y: number, height: number) => {
2. console.info('delete cursorContextChange notification.');
3. });
```

### on('selectionChange')

PhonePC/2in1TabletTVWearable

on(type: 'selectionChange', callback: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void): void

订阅文本选择范围变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 文本选择变化事件，固定取值为'selectionChange'。 |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void | 是 | 回调函数，返回文本选择信息。  - oldBegin为变化前被选中文本的起始下标，oldEnd为变化前被选中文本的终止下标。  - newBegin为变化后被选中文本的起始下标，newEnd为变化后被选中文本的终止下标。 |

**示例：**

```
1. inputMethodEngine.getKeyboardDelegate()
2. .on('selectionChange', (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => {
3. console.info('selectionChange oldBegin:' + oldBegin);
4. console.info('selectionChange oldEnd:' + oldEnd);
5. console.info('selectionChange newBegin:' + newBegin);
6. console.info('selectionChange newEnd:' + newEnd);
7. });
```

### off('selectionChange')

PhonePC/2in1TabletTVWearable

off(type: 'selectionChange', callback?: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void): void

取消订阅文本选择范围变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 文本选择变化事件，固定取值为'selectionChange'。 |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. inputMethodEngine.getKeyboardDelegate()
2. .off('selectionChange', (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => {
3. console.info('delete selectionChange notification.');
4. });
```

### on('textChange')

PhonePC/2in1TabletTVWearable

on(type: 'textChange', callback: (text: string) => void): void

订阅文本内容变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 文本变化事件，固定取值为'textChange'。 |
| callback | (text: string) => void | 是 | 回调函数，返回订阅的文本内容。 |

**示例：**

```
1. inputMethodEngine.getKeyboardDelegate().on('textChange', (text: string) => {
2. console.info('inputMethodEngine textChange. text:' + text);
3. });
```

### off('textChange')

PhonePC/2in1TabletTVWearable

off(type: 'textChange', callback?: (text: string) => void): void

取消订阅文本内容变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 文本变化事件，固定取值为'textChange'。 |
| callback | (text: string) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. inputMethodEngine.getKeyboardDelegate().off('textChange', (text: string) => {
2. console.info('delete textChange notification. text:' + text);
3. });
```

### on('editorAttributeChanged')10+

PhonePC/2in1TabletTVWearable

on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void

订阅编辑框属性变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 文本变化事件，固定取值为'editorAttributeChanged'。 |
| callback | (attr: [EditorAttribute](js-apis-inputmethodengine.md#editorattribute)) => void | 是 | 回调函数，返回变化的编辑框属性。 |

**示例：**

```
1. inputMethodEngine.getKeyboardDelegate()
2. .on('editorAttributeChanged', (attr: inputMethodEngine.EditorAttribute) => {
3. console.info(`Succeeded in receiving attribute of editor, inputPattern = ${attr.inputPattern}, enterKeyType = ${attr.enterKeyType}`);
4. });
```

### off('editorAttributeChanged')10+

PhonePC/2in1TabletTVWearable

off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void

取消订阅编辑框属性变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 文本变化事件，固定取值为'editorAttributeChanged'。 |
| callback | (attr: [EditorAttribute](js-apis-inputmethodengine.md#editorattribute)) => void | 否 | 所要取消订阅的回调处理函数。参数不填写时，默认取消订阅type对应的所有回调事件。 |

**示例：**

```
1. inputMethodEngine.getKeyboardDelegate().off('editorAttributeChanged');
```

## Panel10+

PhonePC/2in1TabletTVWearable

下列API均需使用[createPanel](js-apis-inputmethodengine.md#createpanel10)获取到Panel实例后，通过实例调用。

### setUiContent10+

PhonePC/2in1TabletTVWearable

setUiContent(path: string, callback: AsyncCallback<void>): void

为当前的输入法面板加载具体页面内容，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 具体页面的路径。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板页面内容加载成功，err为undefined，否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. panel.setUiContent('pages/page2/page2', (err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in setting the content.');
9. });
```

### setUiContent10+

PhonePC/2in1TabletTVWearable

setUiContent(path: string): Promise<void>

为当前的输入法面板加载具体页面内容，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 具体页面的路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. panel.setUiContent('pages/page2/page2').then(() => {
4. console.info('Succeeded in setting the content.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
7. });
```

### setUiContent10+

PhonePC/2in1TabletTVWearable

setUiContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void

为当前的输入法面板加载与LocalStorage相关联的具体页面内容，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | LocalStorage相关联的具体页面的路径。 |
| storage | [LocalStorage](ts-state-management.md#localstorage9) | 是 | 存储单元，为应用程序范围内的可变和不可变状态属性提供存储。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板页面内容加载成功，err为undefined，否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let storage: LocalStorage = new LocalStorage();
4. storage.setOrCreate('storageSimpleProp', 121);
5. panel.setUiContent('pages/page2/page2', storage, (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in setting the content.');
11. });
```

### setUiContent10+

PhonePC/2in1TabletTVWearable

setUiContent(path: string, storage: LocalStorage): Promise<void>

为当前面板加载与LocalStorage相关联的具体页面内容，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 设置加载页面的路径。 |
| storage | [LocalStorage](ts-state-management.md#localstorage9) | 是 | 存储单元，为应用程序范围内的可变状态属性和非可变状态属性提供存储。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let storage: LocalStorage = new LocalStorage();
4. storage.setOrCreate('storageSimpleProp', 121);
5. panel.setUiContent('pages/page2/page2', storage).then(() => {
6. console.info('Succeeded in setting the content.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
9. });
```

### resize10+

PhonePC/2in1TabletTVWearable

resize(width: number, height: number, callback: AsyncCallback<void>): void

改变当前输入法面板的大小，使用callback异步回调。

说明

面板宽度不超出屏幕宽度，面板高度不高于屏幕高度的0.7倍。

手机的PanelFlag是FLG\_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 目标面板的宽度，单位为px。该参数应为大于或等于0的整数，不超出屏幕宽度。 |
| height | number | 是 | 目标面板的高度，单位为px。该参数应为大于或等于0的整数，不高于屏幕高度的0.7倍。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板大小改变成功，err为undefined，否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. panel.resize(500, 1000, (err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to resize panel. Code is ${err.code}, message is ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in changing the panel size.');
9. });
```

### resize10+

PhonePC/2in1TabletTVWearable

resize(width: number, height: number): Promise<void>

改变当前输入法面板的大小，使用Promise异步回调。

说明

面板宽度不超出屏幕宽度，面板高度不高于屏幕高度的0.7倍。

手机的PanelFlag是FLG\_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 目标面板的宽度，单位为px。该参数应为大于或等于0的整数，不超出屏幕宽度。 |
| height | number | 是 | 目标面板的高度，单位为px。该参数应为大于或等于0的整数，不高于屏幕高度的0.7倍。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. panel.resize(500, 1000).then(() => {
4. console.info('Succeeded in changing the panel size.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to resize panel. Code is ${err.code}, message is ${err.message}`);
7. });
```

### moveTo10+

PhonePC/2in1TabletTVWearable

moveTo(x: number, y: number, callback: AsyncCallback<void>): void

移动面板位置，使用callback异步回调。[面板状态](js-apis-inputmethodengine.md#panelflag10)为固定态时，不产生实际移动效果。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 横轴方向移动的值，值大于0表示右移，单位为px。该参数应为整数。 |
| y | number | 是 | 纵轴方向移动的值，值大于0表示下移，单位为px。该参数应为整数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板位置移动成功，err为undefined，否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. panel.moveTo(300, 300, (err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to move panel. Code is ${err.code}, message is ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in moving the panel.');
9. });
```

### moveTo10+

PhonePC/2in1TabletTVWearable

moveTo(x: number, y: number): Promise<void>

移动面板位置，使用promise异步回调。[面板状态](js-apis-inputmethodengine.md#panelflag10)为固定态时，不产生实际移动效果。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 横轴方向移动的值，值大于0表示右移，单位为px。该参数应为整数。 |
| y | number | 是 | 纵轴方向移动的值，值大于0表示下移，单位为px。该参数应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. panel.moveTo(300, 300).then(() => {
4. console.info('Succeeded in moving the panel.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to move panel. Code is ${err.code}, message is ${err.message}`);
7. });
```

### startMoving15+

PhonePC/2in1TabletTVWearable

startMoving(): void

发送移动命令给窗口，不产生实际移动效果（仅在鼠标点击作用才可以移动）。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. |

**示例：**

```
1. panel.startMoving();
```

### getDisplayId15+

PhonePC/2in1TabletTVWearable

getDisplayId(): Promise<number>

获取当前窗口的所在id，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回窗口的displayId。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. panel.getDisplayId().then((result: number) => {
4. console.info('get displayId:' + result);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to get displayId. Code is ${err.code}, message is ${err.message}`);
7. });
```

### show10+

PhonePC/2in1TabletTVWearable

show(callback: AsyncCallback<void>): void

显示当前输入法面板，使用callback异步回调。输入法应用与编辑框绑定成功后可正常调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板显示成功，err为undefined，否则err为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. panel.show((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to show panel. Code is ${err.code}, message is ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in showing the panel.');
9. });
```

### show10+

PhonePC/2in1TabletTVWearable

show(): Promise<void>

显示当前输入法面板，使用promise异步回调。输入法应用与编辑框绑定成功后可正常调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. panel.show().then(() => {
4. console.info('Succeeded in showing the panel.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to show panel. Code is ${err.code}, message is ${err.message}`);
7. });
```

### hide10+

PhonePC/2in1TabletTVWearable

hide(callback: AsyncCallback<void>): void

隐藏当前输入法面板，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板隐藏成功，err为undefined，否则err为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. panel.hide((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to hide panel. Code is ${err.code}, message is ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in hiding the panel.');
9. });
```

### hide10+

PhonePC/2in1TabletTVWearable

hide(): Promise<void>

隐藏当前输入法面板，使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. panel.hide().then(() => {
4. console.info('Succeeded in hiding the panel.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to hide panel. Code is ${err.code}, message is ${err.message}`);
7. });
```

### adjustPanelRect12+

PhonePC/2in1TabletTVWearable

adjustPanelRect(flag: PanelFlag, rect: PanelRect): void

预设置输入法应用横竖屏大小。接口调用完毕表示adjust请求已提交到输入法框架，不表示执行完毕。

说明

仅用于SOFT\_KEYBOARD类型，状态为FLG\_FIXED或FLG\_FLOATING的面板。

此接口为同步接口，接口返回仅代表系统侧收到设置的请求，不代表已完成设置。

手机的PanelFlag是FLG\_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flag | [PanelFlag](js-apis-inputmethodengine.md#panelflag10) | 是 | 目标面板状态类型。类型为FLG\_FIXED或FLG\_FLOATING。 |
| rect | [PanelRect](js-apis-inputmethodengine.md#panelrect12) | 是 | 目标面板横屏状态及竖屏状态的横坐标，纵坐标，宽度以及高度。固定态：高度不能超过屏幕高度的70%，宽度不能超过屏幕宽度；悬浮态：高度不能超过屏幕高度，宽度不能超过屏幕宽度。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800013 | window manager service error. |

**示例：**

```
1. import { window } from '@kit.ArkUI';

3. let landscapeRect: window.Rect = {
4. left: 100,
5. top: 100,
6. width: 400,
7. height: 400
8. };

10. let portraitRect: window.Rect = {
11. left: 200,
12. top: 200,
13. width: 300,
14. height: 300
15. };

17. // 目标面板状态类型
18. let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
19. // 目标面板横屏状态及竖屏状态的横坐标，纵坐标，宽度以及高度
20. let panelRect: inputMethodEngine.PanelRect = {
21. landscapeRect: landscapeRect,
22. portraitRect: portraitRect
23. };
24. panel.adjustPanelRect(panelFlag, panelRect);
```

### adjustPanelRect15+

PhonePC/2in1TabletTVWearable

adjustPanelRect(flag: PanelFlag, rect: EnhancedPanelRect): void

预设置输入法应用横竖屏大小、位置、自定义避让区域以及热区。

说明

仅用于SOFT\_KEYBOARD类型，状态为FLG\_FIXED或FLG\_FLOATING的面板。此接口兼容[adjustPanelRect](js-apis-inputmethodengine.md#adjustpanelrect12)的调用方法，若入参rect仅填写属性landscapeRect和portraitRect，则默认调用[adjustPanelRect](js-apis-inputmethodengine.md#adjustpanelrect12)。

此接口为同步接口，接口返回仅代表系统侧收到设置的请求，不代表已完成设置。

手机的PanelFlag是FLG\_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flag | [PanelFlag](js-apis-inputmethodengine.md#panelflag10) | 是 | 目标面板状态类型。类型为FLG\_FIXED或FLG\_FLOATING。 |
| rect | [EnhancedPanelRect](js-apis-inputmethodengine.md#enhancedpanelrect15) | 是 | 目标面板横屏状态及竖屏状态的位置、大小、避让区域以及热区。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. |

**示例：**

```
1. import { window } from '@kit.ArkUI';

3. let landscapeRect1: window.Rect = {
4. left: 300,
5. top: 650,
6. width: 2000,
7. height: 500
8. };
9. let landscapeInputRegion: Array<window.Rect> = [landscapeRect1];

11. let portraitRect1: window.Rect = {
12. left: 0,
13. top: 1800,
14. width: 1200,
15. height: 800
16. }
17. let portraitInputRegion: Array<window.Rect> = [portraitRect1];
18. // 目标面板状态类型。
19. let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
20. // 目标面板横屏状态及竖屏状态的位置、大小、避让区域以及热区。
21. let panelRect: inputMethodEngine.EnhancedPanelRect = {
22. landscapeAvoidY: 650,
23. landscapeInputRegion: landscapeInputRegion,
24. portraitAvoidY: 1800,
25. portraitInputRegion: portraitInputRegion,
26. fullScreenMode: true
27. };
28. panel.adjustPanelRect(panelFlag, panelRect);
```

### updateRegion15+

PhonePC/2in1TabletTVWearable

updateRegion(inputRegion: Array<window.Rect>): void

更新当前状态下输入法面板内的热区。

说明

仅用于SOFT\_KEYBOARD类型，状态为FLG\_FIXED或FLG\_FLOATING的面板。

此接口为同步接口，接口返回仅代表系统侧收到更新热区的请求，不代表已完成热区更新。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputRegion | Array<[window.Rect](arkts-apis-window-i.md#rect7)> | 是 | 面板内接收输入事件的区域。  - 数组大小限制为[1, 4]。  - 传入的热区位置是相对于输入法面板窗口左顶点的位置。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { window } from '@kit.ArkUI';

4. let inputRegion: Array<window.Rect> = [{
5. left: 300,
6. top: 650,
7. width: 2000,
8. height: 500
9. }];
10. panel.updateRegion(inputRegion);
```

### on('show')10+

PhonePC/2in1TabletTVWearable

on(type: 'show', callback: () => void): void

监听当前面板显示状态，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听当前面板的状态类型，固定取值为'show'。 |
| callback | () => void | 是 | 回调函数。 |

**示例：**

```
1. panel.on('show', () => {
2. console.info('Panel is showing.');
3. });
```

### on('hide')10+

PhonePC/2in1TabletTVWearable

on(type: 'hide', callback: () => void): void

监听当前面板隐藏状态，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听当前面板的状态类型，固定取值为'hide'。 |
| callback | () => void | 是 | 回调函数。 |

**示例：**

```
1. panel.on('hide', () => {
2. console.info('Panel is hiding.');
3. });
```

### on('sizeChange')12+

PhonePC/2in1TabletTVWearable

on(type: 'sizeChange', callback: SizeChangeCallback): void

监听当前面板大小变化，使用callback异步回调。

说明

仅用于SOFT\_KEYBOARD类型，状态为FLG\_FIXED或FLG\_FLOATING的面板。输入法通过adjustPanelRect等接口对面板大小进行调节时，系统会根据一定规则校验计算出最终的数值（例如超出屏幕等场景），输入法应用可通过该回调获取的真实面板大小，完成最终的面板布局刷新。

* 从API version 12-14开始支持，此接口回调函数中仅包含[window.Size](arkts-apis-window-i.md#size7)类型的必选参数。
* 从API version 15起，调用[adjustPanelRect](js-apis-inputmethodengine.md#adjustpanelrect15)接口后，此接口回调函数增加[KeyboardArea](js-apis-inputmethodengine.md#keyboardarea15)类型的可选参数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听当前面板的大小是否产生变化，固定值为'sizeChange'。 |
| callback | [SizeChangeCallback](js-apis-inputmethodengine.md#sizechangecallback15) | 是 | 回调函数。返回当前软键盘面板的大小，包含宽度和高度值。 |

**示例：**

```
1. import { window } from '@kit.ArkUI';

3. panel.on('sizeChange', (windowSize: window.Size) => {
4. console.info(`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}`);
5. });

7. panel.on('sizeChange', (windowSize: window.Size, keyboardArea: inputMethodEngine.KeyboardArea) => {
8. console.info(`panel size changed, windowSize: ${windowSize.width}, ${windowSize.height}, ` +
9. `keyboardArea: ${keyboardArea.top}, ${keyboardArea.bottom}, ${keyboardArea.left}, ${keyboardArea.right}`);
10. });
```

### off('show')10+

PhonePC/2in1TabletTVWearable

off(type: 'show', callback?: () => void): void

取消监听当前面板的显示状态，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听当前面板的状态类型，固定取值为'show'。 |
| callback | () => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. panel.off('show');
```

### off('hide')10+

PhonePC/2in1TabletTVWearable

off(type: 'hide', callback?: () => void): void

取消监听当前面板的隐藏状态，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要取消监听的当前面板状态类型，固定取值为'hide'。 |
| callback | () => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. panel.off('hide');
```

### off('sizeChange')12+

PhonePC/2in1TabletTVWearable

off(type: 'sizeChange', callback?: SizeChangeCallback): void

取消监听当前面板大小变化，使用callback异步回调。

说明

仅用于SOFT\_KEYBOARD类型，状态为FLG\_FIXED或FLG\_FLOATING的面板。输入法通过adjustPanelRect等接口对面板大小进行调节时，系统会根据一定规则校验计算出最终的数值（例如超出屏幕等场景），输入法应用可通过该回调获取的真实面板大小，完成最终的面板布局刷新。

* 从API version 12-14开始支持，此接口回调函数中仅包含[window.Size](arkts-apis-window-i.md#size7)类型的必选参数。
* 从API version 15起，调用[adjustPanelRect](js-apis-inputmethodengine.md#adjustpanelrect15)接口后，此接口回调函数增加[KeyboardArea](js-apis-inputmethodengine.md#keyboardarea15)类型的可选参数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听当前面板的大小是否产生变化，固定取值为'sizeChange'。 |
| callback | [SizeChangeCallback](js-apis-inputmethodengine.md#sizechangecallback15) | 否 | 回调函数。返回当前软键盘面板的大小，包含宽度和高度值。 |

**示例：**

```
1. import { window } from '@kit.ArkUI';

3. panel.off('sizeChange', (windowSize: window.Size) => {
4. console.info(`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}`);
5. });
```

### changeFlag10+

PhonePC/2in1TabletTVWearable

changeFlag(flag: PanelFlag): void

将输入法应用的面板状态改变为其他[PanelFlag](js-apis-inputmethodengine.md#panelflag10)形态，仅对[SOFT\_KEYBOARD](js-apis-inputmethodengine.md#paneltype10)生效。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flag | [PanelFlag](js-apis-inputmethodengine.md#panelflag10) | 是 | 目标面板状态类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
2. panel.changeFlag(panelFlag);
```

### setPrivacyMode11+

PhonePC/2in1TabletTVWearable

setPrivacyMode(isPrivacyMode: boolean): void

将输入法应用的面板设置为隐私模式，隐私模式不可被录屏、截屏。

**需要权限：** ohos.permission.PRIVACY\_WINDOW

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacyMode | boolean | 是 | 是否设置隐私模式。  - 值为true，表示将设置为隐私模式。  - 值为false，表示将设置为非隐私模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permissions check fails. |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let isPrivacyMode: boolean = true;
2. panel.setPrivacyMode(isPrivacyMode);
```

### setImmersiveMode15+

PhonePC/2in1TabletTVWearable

setImmersiveMode(mode: ImmersiveMode): void

设置输入法应用的沉浸模式。只能设置不使用沉浸模式(NONE\_IMMERSIVE)、浅色沉浸模式(LIGHT\_IMMERSIVE)或深色沉浸模式(DARK\_IMMERSIVE)。不能设置为沉浸模式(IMMERSIVE)。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [ImmersiveMode](js-apis-inputmethodengine.md#immersivemode15) | 是 | 沉浸模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |

**示例：**

```
1. panel.setImmersiveMode(inputMethodEngine.ImmersiveMode.LIGHT_IMMERSIVE);
```

### getImmersiveMode15+

PhonePC/2in1TabletTVWearable

getImmersiveMode(): ImmersiveMode

获取输入法应用的沉浸模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImmersiveMode](js-apis-inputmethodengine.md#immersivemode15) | 沉浸模式。 |

**示例：**

```
1. let mode: inputMethodEngine.ImmersiveMode = panel.getImmersiveMode();
```

### setImmersiveEffect20+

PhonePC/2in1TabletTVWearable

setImmersiveEffect(effect: ImmersiveEffect): void

设置输入法应用的沉浸效果。

* 只有在[启用沉浸式模式](js-apis-inputmethodengine.md#setimmersivemode15)时，才能使用渐变模式和流光模式。
* 只有在启用渐变模式时，才能使用流光模式。
* 未启用渐变模式时，渐变高度必须为0px。
* 只有系统应用才能设置流光模式。
* 必须先调用以下任一接口，才能调用当前接口：
  + [adjustPanelRect](js-apis-inputmethodengine.md#adjustpanelrect12)(支持API version 12)
  + [adjustPanelRect](js-apis-inputmethodengine.md#adjustpanelrect15)(支持API version 15)
  + [resize](js-apis-inputmethodengine.md#resize10)(支持API version 10)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effect | [ImmersiveEffect](js-apis-inputmethodengine.md#immersiveeffect20) | 是 | 沉浸效果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 12800002 | input method engine error. Possible causes:1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |
| 12800020 | invalid immersive effect. 1.The gradient mode and the fluid light mode can only be used when the immersive mode is enabled. 2.The fluid light mode can only be used when the gradient mode is enabled. 3.When the gradient mode is not enabled, the gradient height can only be 0. |
| 12800021 | this operation is allowed only after adjustPanelRect or resize is called. |

**示例：**

```
1. let effect: inputMethodEngine.ImmersiveEffect = {
2. gradientHeight: 100,
3. gradientMode: inputMethodEngine.GradientMode.LINEAR_GRADIENT
4. }
5. panel.setImmersiveEffect(effect);
```

### setKeepScreenOn20+

PhonePC/2in1TabletTVWearable

setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>

设置屏幕常亮。使用Promise异步回调。

说明

* 当键盘拉起时设置常亮生效，键盘关闭则自动失效。
* 规范使用该接口：必要场景（例如：语音输入）下，设置该属性为true；退出必要场景后，重置该属性为false；其他场景下，不使用该接口。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isKeepScreenOn | boolean | 是 | 是否设置屏幕常亮。true表示打开屏幕常亮，false表示关闭屏幕常亮。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800013 | window manager service error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. panel.setKeepScreenOn(true).then(() => {
4. console.info(`setKeepScreenOn success.`);
5. }).catch((error: BusinessError) => {
6. console.error(`setKeepScreenOn failed, code: ${error.code}, message: ${error.message}`);
7. })
```

### getSystemPanelCurrentInsets21+

PhonePC/2in1TabletTVWearable

getSystemPanelCurrentInsets(displayId: number): Promise<SystemPanelInsets>

获取指定屏幕当前状态（例如：折叠或展开）下，当前输入法键盘状态（例如：悬浮或固定）下输入法软键盘相对系统面板的偏移区域。使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 输入法键盘所在屏幕的displayId，可通过[getDisplayId](js-apis-inputmethodengine.md#getdisplayid15)获取 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SystemPanelInsets](js-apis-inputmethodengine.md#systempanelinsets21)> | Promise对象。输入法键盘与系统面板的偏移区域。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. Possible causes: 1. Current panel's type is not SOFT\_KEYBOARD. 2. Panel's flag is not FLG\_FIXED or FLG\_FLOATING. |
| 12800022 | invalid displayId. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { inputMethodEngine } from '@kit.IMEKit';

4. let inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
5. let panelConfig: inputMethodEngine.PanelInfo = {
6. type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
7. flag: inputMethodEngine.PanelFlag.FLG_FIXED
8. }
9. // 以下逻辑需要在输入法InputMethodExtensionAbility中执行，this.context是InputMethodExtensionAbility的上下文
10. inputMethodAbility.createPanel(this.context, panelConfig).then( (panel: inputMethodEngine.Panel) =>{
11. panel.getDisplayId().then((displayId: number) => {
12. panel.getSystemPanelCurrentInsets(displayId).then((insets: inputMethodEngine.SystemPanelInsets) => {
13. console.info(`getSystemPanelCurrentInsets success, insets is { left: ${insets.left}, right: ${insets.right}, bottom: ${insets.bottom} }`);
14. }).catch((error: BusinessError) => {
15. console.error(`getSystemPanelCurrentInsets failed, code: ${error.code}, message: ${error.message}`);
16. })
17. });
18. })
```

### setSystemPanelButtonColor22+

PhonePC/2in1TabletTVWearable

setSystemPanelButtonColor(fillColor: string | undefined, backgroundColor: string | undefined): Promise<void>

设置当前面板功能键颜色和功能键的背景颜色。使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fillColor | string|undefined | 是 | 功能键的颜色，取值范围为[#01000000, #FFFFFFFF] 或 [#000000, #FFFFFF]，不支持具有完全透明Alpha通道（#00xxxxxx）的值。 |
| backgroundColor | string|undefined | 是 | 功能键的背景颜色，取值范围为[#01000000, #FFFFFFFF] 或 [#000000, #FFFFFF]，不支持具有完全透明Alpha通道（#00xxxxxx）的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let fillColor = "#FFFF00";
5. let backgroundColor = "#0000FF";
6. this.panel.setSystemPanelButtonColor(fillColor, backgroundColor).then(() => {
7. console.info(`setSystemPanelButtonColor success.`);
8. }).catch((error: BusinessError) => {
9. console.error(`setSystemPanelButtonColor failed, code: ${error.code}, message: ${error.message}`);
10. })
11. } catch (err) {
12. let error = err as BusinessError;
13. console.error(`setSystemPanelButtonColor failed, code: ${error.code}, message: ${error.message}`);
14. }
```

## KeyboardController

PhonePC/2in1TabletTVWearable

下列API均需使用[on('inputStart')](js-apis-inputmethodengine.md#oninputstart9)获取到KeyboardController实例后，通过实例调用。

### hide9+

PhonePC/2in1TabletTVWearable

hide(callback: AsyncCallback<void>): void

隐藏输入法。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当输入法隐藏成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. keyboardController.hide((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to hide. Code:${err.code}, message:${err.message}`);
6. return;
7. }
8. console.info('Succeeded in hiding keyboard.');
9. });
```

### hide9+

PhonePC/2in1TabletTVWearable

hide(): Promise<void>

隐藏输入法。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. keyboardController.hide().then(() => {
4. console.info('Succeeded in hiding keyboard.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to hide. Code:${err.code}, message:${err.message}`);
7. });
```

### hideKeyboard(deprecated)

PhonePC/2in1TabletTVWearable

hideKeyboard(callback: AsyncCallback<void>): void

隐藏输入法。使用callback异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[hide](js-apis-inputmethodengine.md#hide9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当输入法隐藏成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. keyboardController.hideKeyboard((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to hideKeyboard. Code is ${err.code}, message is ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in hiding keyboard.');
9. });
```

### hideKeyboard(deprecated)

PhonePC/2in1TabletTVWearable

hideKeyboard(): Promise<void>

隐藏输入法。使用promise异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[hide](js-apis-inputmethodengine.md#hide9-1)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. keyboardController.hideKeyboard().then(() => {
4. console.info('Succeeded in hiding keyboard.');
5. }).catch((err: BusinessError) => {
6. console.info(`Failed to hideKeyboard. Code is ${err.code}, message is ${err.message}`);
7. });
```

### exitCurrentInputType11+

PhonePC/2in1TabletTVWearable

exitCurrentInputType(callback: AsyncCallback<void>): void

退出当前输入类型，仅支持系统配置的默认输入法应用调用。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当退出当前输入类型成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800010 | not the preconfigured default input method. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. keyboardController.exitCurrentInputType((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to exit current input type. Code:${err.code}, message:${err.message}`);
6. return;
7. }
8. console.info('Succeeded in exiting current input type.');
9. });
```

### exitCurrentInputType11+

PhonePC/2in1TabletTVWearable

exitCurrentInputType(): Promise<void>

退出当前输入类型，仅支持系统配置的默认输入法应用调用。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800010 | not the preconfigured default input method. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. keyboardController.exitCurrentInputType().then(() => {
4. console.info('Succeeded in exiting current input type.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to exit current input type. Code:${err.code}, message:${err.message}`);
7. });
```

## SecurityMode11+

PhonePC/2in1TabletTVWearable

输入法的安全模式，如BASIC或FULL。

**系统能力**: SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BASIC | 0 | 基础访问模式，基础打字模式，会限制网络访问。 |
| FULL | 1 | 完全访问模式，不做限制，可以访问网络。 |

## ExtendAction10+

PhonePC/2in1TabletTVWearable

编辑框中文本的扩展编辑操作类型，如剪切、复制等。

**系统能力**: SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELECT\_ALL | 0 | 全选。 |
| CUT | 3 | 剪切。 |
| COPY | 4 | 复制。 |
| PASTE | 5 | 粘贴。 |

## Direction10+

PhonePC/2in1TabletTVWearable

光标的移动方向。

**系统能力**: SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CURSOR\_UP | 1 | 向上。 |
| CURSOR\_DOWN | 2 | 向下。 |
| CURSOR\_LEFT | 3 | 向左。 |
| CURSOR\_RIGHT | 4 | 向右。 |

## Range10+

PhonePC/2in1TabletTVWearable

选中的文本范围。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 否 | 选中文本的首字符在编辑框的索引值。 |
| end | number | 否 | 否 | 选中文本的末字符在编辑框的索引值。 |

## Movement10+

PhonePC/2in1TabletTVWearable

选中文本时，光标移动的方向

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| direction | [Direction](js-apis-inputmethodengine.md#direction10) | 否 | 否 | 选中文本时，光标的移动方向。 |

## MessageHandler15+

PhonePC/2in1TabletTVWearable

自定义通信对象。

说明

开发者可通过注册此对象来接收已绑定当前输入法应用的编辑框应用所发送的自定义通信数据，接收到自定义通信数据时会触发此对象中[onMessage](js-apis-inputmethodengine.md#onmessage15)回调函数。

此对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的[onTerminated](js-apis-inputmethodengine.md#onterminated15)回调函数。

若取消注册全局已注册的对象时，会触发被取消对象中[onTerminated](js-apis-inputmethodengine.md#onterminated15)回调函数。

### onMessage15+

PhonePC/2in1TabletTVWearable

onMessage(msgId: string, msgParam?: ArrayBuffer): void

接收已绑定当前输入法应用的编辑框应用发送的自定义数据回调函数。

说明

当已注册的[MessageHandler](js-apis-inputmethodengine.md#messagehandler15)接收到来自已绑定当前输入法应用的编辑框应用所发送的自定义通信数据时，会触发该回调函数。

msgId为必选参数，msgParam为可选参数。存在收到仅有msgId自定义数据的可能，需与数据发送方确认自定义数据。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msgId | string | 是 | 接收到的自定义通信数据的标识符。 |
| msgParam | ArrayBuffer | 否 | 接收到的自定义通信数据的消息体。 |

**示例：**

```
1. inputMethodEngine.getInputMethodAbility()
2. .on('inputStart',
3. (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
4. let keyboardController: inputMethodEngine.KeyboardController = kbController;
5. let inputClient: inputMethodEngine.InputClient = client;
6. let messageHandler: inputMethodEngine.MessageHandler = {
7. onTerminated(): void {
8. console.info('OnTerminated.');
9. },
10. onMessage(msgId: string, msgParam?: ArrayBuffer): void {
11. console.info(`recv message, msgId is ${msgId}, msgParam is ${JSON.stringify(msgParam)}`);
12. }
13. }
14. inputClient.recvMessage(messageHandler);
15. });
```

### onTerminated15+

PhonePC/2in1TabletTVWearable

onTerminated(): void

监听对象终止回调函数。

说明

当应用注册新的[MessageHandler](js-apis-inputmethodengine.md#messagehandler15)对象时，会触发上一个已注册[MessageHandler](js-apis-inputmethodengine.md#messagehandler15)对象的[onTerminated](js-apis-inputmethodengine.md#onterminated15)回调函数。

当应用取消注册时，会触发当前已注册[MessageHandler](js-apis-inputmethodengine.md#messagehandler15)对象的[onTerminated](js-apis-inputmethodengine.md#onterminated15)回调函数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**示例：**

```
1. inputMethodEngine.getInputMethodAbility()
2. .on('inputStart',
3. (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
4. let keyboardController: inputMethodEngine.KeyboardController = kbController;
5. let inputClient: inputMethodEngine.InputClient = client;
6. let messageHandler: inputMethodEngine.MessageHandler = {
7. onTerminated(): void {
8. console.info('OnTerminated.');
9. },
10. onMessage(msgId: string, msgParam?: ArrayBuffer): void {
11. console.info(`recv message, msgId is ${msgId}, msgParam is ${JSON.stringify(msgParam)}`);
12. }
13. }
14. inputClient.recvMessage(messageHandler);
15. });
```

## InputClient9+

PhonePC/2in1TabletTVWearable

下列API均需使用[on('inputStart')](js-apis-inputmethodengine.md#oninputstart9)获取到InputClient实例后，通过实例调用。

### sendKeyFunction9+

PhonePC/2in1TabletTVWearable

sendKeyFunction(action:number, callback: AsyncCallback<boolean>): void

发送功能键。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | number | 是 | 功能键键值。  - 当值为0时，表示无效按键。  - 当值为1时，表示确认键（即回车键）。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当功能键发送成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let action: number = 1;

5. inputClient.sendKeyFunction(action, (err: BusinessError, result: boolean) => {
6. if (err) {
7. console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
8. return;
9. }
10. if (result) {
11. console.info('Succeeded in sending key function.');
12. } else {
13. console.error('Failed to sendKeyFunction.');
14. }
15. });
```

### sendKeyFunction9+

PhonePC/2in1TabletTVWearable

sendKeyFunction(action: number): Promise<boolean>

发送功能键。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | number | 是 | 功能键键值。  当值为0时，表示无效按键；  当值为1时，表示确认键（即回车键）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示功能键发送成功；返回false表示功能键发送失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let action: number = 1;
4. inputClient.sendKeyFunction(action).then((result: boolean) => {
5. if (result) {
6. console.info('Succeeded in sending key function.');
7. } else {
8. console.error('Failed to sendKeyFunction.');
9. }
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
12. });
```

### getForward9+

PhonePC/2in1TabletTVWearable

getForward(length:number, callback: AsyncCallback<string>): void

获取光标前固定长度的文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当光标前固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. inputClient.getForward(length, (err: BusinessError, text: string) => {
5. if (err) {
6. console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in getting forward, text: ' + text);
10. });
```

### getForward9+

PhonePC/2in1TabletTVWearable

getForward(length:number): Promise<string>

获取光标前固定长度的文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回光标前固定长度的文本。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. inputClient.getForward(length).then((text: string) => {
5. console.info('Succeeded in getting forward, text: ' + text);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
8. });
```

### getForwardSync10+

PhonePC/2in1TabletTVWearable

getForwardSync(length:number): string

获取光标前固定长度的文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回光标前固定长度的文本。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```
1. let length: number = 1;
2. let text: string = inputClient.getForwardSync(length);
3. console.info(`Succeeded in getting forward, text: ${text}`);
```

### getBackward9+

PhonePC/2in1TabletTVWearable

getBackward(length:number, callback: AsyncCallback<string>): void

获取光标后固定长度的文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当光标后固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. inputClient.getBackward(length, (err: BusinessError, text: string) => {
5. if (err) {
6. console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in getting backward, text: ' + text);
10. });
```

### getBackward9+

PhonePC/2in1TabletTVWearable

getBackward(length:number): Promise<string>

获取光标后固定长度的文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回光标后固定长度的文本。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. inputClient.getBackward(length).then((text: string) => {
5. console.info('Succeeded in getting backward, text: ' + text);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
8. });
```

### getBackwardSync10+

PhonePC/2in1TabletTVWearable

getBackwardSync(length:number): string

获取光标后固定长度的文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回光标后固定长度的文本。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```
1. let length: number = 1;
2. let text: string = inputClient.getBackwardSync(length);
3. console.info(`Succeeded in getting backward, text: ${text}`);
```

### deleteForward9+

PhonePC/2in1TabletTVWearable

deleteForward(length:number, callback: AsyncCallback<boolean>): void

删除光标前固定长度的文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当光标前固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. inputClient.deleteForward(length, (err: BusinessError, result: boolean) => {
5. if (err) {
6. console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
7. return;
8. }
9. if (result) {
10. console.info('Succeeded in deleting forward.');
11. } else {
12. console.error(`Failed to deleteForward.`);
13. }
14. });
```

### deleteForward9+

PhonePC/2in1TabletTVWearable

deleteForward(length:number): Promise<boolean>

删除光标前固定长度的文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示删除光标前固定长度的文本成功；返回false表示删除光标前固定长度的文本失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. inputClient.deleteForward(length).then((result: boolean) => {
5. if (result) {
6. console.info('Succeeded in deleting forward.');
7. } else {
8. console.error('Failed to delete Forward.');
9. }
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
12. });
```

### deleteForwardSync10+

PhonePC/2in1TabletTVWearable

deleteForwardSync(length:number): void

删除光标前固定长度的文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. let length: number = 1;
2. inputClient.deleteForwardSync(length);
```

### deleteBackward9+

PhonePC/2in1TabletTVWearable

deleteBackward(length:number, callback: AsyncCallback<boolean>): void

删除光标后固定长度的文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当光标后固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. inputClient.deleteBackward(length, (err: BusinessError, result: boolean) => {
5. if (err) {
6. console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
7. return;
8. }
9. if (result) {
10. console.info('Succeeded in deleting backward.');
11. } else {
12. console.error(`Failed to deleteBackward.`);
13. }
14. });
```

### deleteBackward9+

PhonePC/2in1TabletTVWearable

deleteBackward(length:number): Promise<boolean>

删除光标后固定长度的文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示删除光标后固定长度的文本成功；返回false表示删除光标后固定长度的文本失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. inputClient.deleteBackward(length).then((result: boolean) => {
5. if (result) {
6. console.info('Succeeded in deleting backward.');
7. } else {
8. console.error('Failed to deleteBackward.');
9. }
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
12. });
```

### deleteBackwardSync10+

PhonePC/2in1TabletTVWearable

deleteBackwardSync(length:number): void

删除光标后固定长度的文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. let length: number = 1;
2. inputClient.deleteBackwardSync(length);
```

### insertText9+

PhonePC/2in1TabletTVWearable

insertText(text:string, callback: AsyncCallback<boolean>): void

插入文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 文本内容。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当文本插入成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

4. inputClient.insertText('test', (err: BusinessError, result: boolean) => {
5. if (err) {
6. console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
7. return;
8. }
9. if (result) {
10. console.info('Succeeded in inserting text.');
11. } else {
12. console.error('Failed to insertText.');
13. }
14. });
```

### insertText9+

PhonePC/2in1TabletTVWearable

insertText(text:string): Promise<boolean>

插入文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 文本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示插入文本成功；返回false表示插入文本失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputClient.insertText('test').then((result: boolean) => {
4. if (result) {
5. console.info('Succeeded in inserting text.');
6. } else {
7. console.error('Failed to insertText.');
8. }
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
11. });
```

### insertTextSync10+

PhonePC/2in1TabletTVWearable

insertTextSync(text: string): void

插入文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 文本内容。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. inputClient.insertTextSync('test');
```

### getEditorAttribute9+

PhonePC/2in1TabletTVWearable

getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void

获取编辑框属性值。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[EditorAttribute](js-apis-inputmethodengine.md#editorattribute)> | 是 | 回调函数。当编辑框属性值获取成功，err为undefined，data为编辑框属性值；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputClient.getEditorAttribute((err: BusinessError, editorAttribute: inputMethodEngine.EditorAttribute) => {
4. if (err) {
5. console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
6. return;
7. }
8. console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
9. console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
10. });
```

### getEditorAttribute9+

PhonePC/2in1TabletTVWearable

getEditorAttribute(): Promise<EditorAttribute>

获取编辑框属性值。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[EditorAttribute](js-apis-inputmethodengine.md#editorattribute)> | Promise对象，返回编辑框属性值。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputClient.getEditorAttribute().then((editorAttribute: inputMethodEngine.EditorAttribute) => {
4. console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
5. console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
8. });
```

### getEditorAttributeSync10+

PhonePC/2in1TabletTVWearable

getEditorAttributeSync(): EditorAttribute

获取编辑框属性值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EditorAttribute](js-apis-inputmethodengine.md#editorattribute) | 编辑框属性对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. let editorAttribute: inputMethodEngine.EditorAttribute = inputClient.getEditorAttributeSync();
2. console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
3. console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
```

### moveCursor9+

PhonePC/2in1TabletTVWearable

moveCursor(direction: number, callback: AsyncCallback<void>): void

移动光标。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | number | 是 | 光标移动方向。  - 当值为1时，表示向上。  - 当值为2时，表示向下。  - 当值为3时，表示向左。  - 当值为4时，表示向右。不能小于0。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当光标移动成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputClient.moveCursor(inputMethodEngine.Direction.CURSOR_UP, (err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to moveCursor. Code is ${err.code}, message is ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in moving cursor.');
9. });
```

### moveCursor9+

PhonePC/2in1TabletTVWearable

moveCursor(direction: number): Promise<void>

移动光标。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | number | 是 | 光标移动方向。  - 当值为1时，表示向上。  - 当值为2时，表示向下。  - 当值为3时，表示向左。  - 当值为4时，表示向右。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputClient.moveCursor(inputMethodEngine.Direction.CURSOR_UP).then(() => {
4. console.info('Succeeded in moving cursor.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to moveCursor. Code is ${err.code}, message is ${err.message}`);
7. });
```

### moveCursorSync10+

PhonePC/2in1TabletTVWearable

moveCursorSync(direction: number): void

移动光标。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | number | 是 | 光标移动方向。  - 当值为1时，表示向上。  - 当值为2时，表示向下。  - 当值为3时，表示向左。  - 当值为4时，表示向右。不能小于0。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. inputClient.moveCursorSync(inputMethodEngine.Direction.CURSOR_UP);
```

### selectByRange10+

PhonePC/2in1TabletTVWearable

selectByRange(range: Range, callback: AsyncCallback<void>): void

根据索引范围选中文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [Range](js-apis-inputmethodengine.md#range10) | 是 | 选中文本的范围。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当成功发送选中事件后，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let range: inputMethodEngine.Range = { start: 0, end: 1 };
4. inputClient.selectByRange(range, (err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to selectByRange. Code is ${err.code}, message is ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in selecting by range.');
10. });
```

### selectByRange10+

PhonePC/2in1TabletTVWearable

selectByRange(range: Range): Promise<void>

根据索引范围选中文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [Range](js-apis-inputmethodengine.md#range10) | 是 | 选中文本的范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let range: inputMethodEngine.Range = { start: 0, end: 1 };
4. inputClient.selectByRange(range).then(() => {
5. console.info('Succeeded in selecting by range.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to selectByRange. Code is ${err.code}, message is ${err.message}`);
8. });
```

### selectByRangeSync10+

PhonePC/2in1TabletTVWearable

selectByRangeSync(range: Range): void

根据索引范围选中文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [Range](js-apis-inputmethodengine.md#range10) | 是 | 选中文本的范围。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. let range: inputMethodEngine.Range = { start: 0, end: 1 };
2. inputClient.selectByRangeSync(range);
```

### selectByMovement10+

PhonePC/2in1TabletTVWearable

selectByMovement(movement: Movement, callback: AsyncCallback<void>): void

根据光标移动方向选中文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| movement | [Movement](js-apis-inputmethodengine.md#movement10) | 是 | 选中时光标移动的方向。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当成功发送选中事件后，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let movement: inputMethodEngine.Movement = { direction: 1 };
4. inputClient.selectByMovement(movement, (err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to selectByMovement. Code is ${err.code}, message is ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in selecting by movement.');
10. });
```

### selectByMovement10+

PhonePC/2in1TabletTVWearable

selectByMovement(movement: Movement): Promise<void>

根据光标移动方向选中文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| movement | [Movement](js-apis-inputmethodengine.md#movement10) | 是 | 选中时光标移动的方向。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let movement: inputMethodEngine.Movement = { direction: 1 };
4. inputClient.selectByMovement(movement).then(() => {
5. console.info('Succeeded in selecting by movement.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to selectByMovement. Code is ${err.code}, message is ${err.message}`);
8. });
```

### selectByMovementSync10+

PhonePC/2in1TabletTVWearable

selectByMovementSync(movement: Movement): void

根据光标移动方向选中文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| movement | [Movement](js-apis-inputmethodengine.md#movement10) | 是 | 选中时光标移动的方向。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```
1. let movement: inputMethodEngine.Movement = { direction: 1 };
2. inputClient.selectByMovementSync(movement);
```

### getTextIndexAtCursor10+

PhonePC/2in1TabletTVWearable

getTextIndexAtCursor(callback: AsyncCallback<number>): void

获取光标所在处的文本索引。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当文本索引获取成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputClient.getTextIndexAtCursor((err: BusinessError, index: number) => {
4. if (err) {
5. console.error(`Failed to getTextIndexAtCursor. Code is ${err.code}, message is ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in getTextIndexAtCursor: ' + index);
9. });
```

### getTextIndexAtCursor10+

PhonePC/2in1TabletTVWearable

getTextIndexAtCursor(): Promise<number>

获取光标所在处的文本索引。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回光标所在处的文本索引。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputClient.getTextIndexAtCursor().then((index: number) => {
4. console.info('Succeeded in getTextIndexAtCursor: ' + index);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to getTextIndexAtCursor. Code is ${err.code}, message is ${err.message}`);
7. });
```

### getTextIndexAtCursorSync10+

PhonePC/2in1TabletTVWearable

getTextIndexAtCursorSync(): number

获取光标所在处的文本索引。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回光标所在处的文本索引。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```
1. let index: number = inputClient.getTextIndexAtCursorSync();
2. console.info(`Succeeded in getTextIndexAtCursorSync, index: ${index}`);
```

### sendExtendAction10+

PhonePC/2in1TabletTVWearable

sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void

发送扩展编辑操作。使用callback异步回调。

说明

输入法应用调用该接口向编辑框发送扩展编辑操作，编辑框监听相应事件[on('handleExtendAction')](js-apis-inputmethod.md#onhandleextendaction10)，从而进一步做出处理。

编辑框响应[ExtendAction](js-apis-inputmethodengine.md#extendaction10)的PASTE命令时，需要编辑框应用申请[ohos.permission.READ\_PASTEBOARD](../harmonyos-guides/restricted-permissions.md#ohospermissionread_pasteboard)权限。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | [ExtendAction](js-apis-inputmethodengine.md#extendaction10) | 是 | 要发送的扩展操作。 |
| callback | AsyncCallback<void> | 是 | 回调函数。发送成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputClient.sendExtendAction(inputMethodEngine.ExtendAction.COPY, (err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to sendExtendAction. Code is ${err.code}, message is ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in sending extend action.');
9. });
```

### sendExtendAction10+

PhonePC/2in1TabletTVWearable

sendExtendAction(action: ExtendAction): Promise<void>

发送扩展编辑操作。使用promise异步回调。

说明

输入法应用调用该接口向编辑框发送扩展编辑操作，编辑框监听相应事件[on('handleExtendAction')](js-apis-inputmethod.md#onhandleextendaction10)，从而进一步做出处理。

编辑框响应[ExtendAction](js-apis-inputmethodengine.md#extendaction10)的PASTE命令时，需要编辑框应用申请[ohos.permission.READ\_PASTEBOARD](../harmonyos-guides/restricted-permissions.md#ohospermissionread_pasteboard)权限。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | [ExtendAction](js-apis-inputmethodengine.md#extendaction10) | 是 | 要发送的扩展操作。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputClient.sendExtendAction(inputMethodEngine.ExtendAction.COPY).then(() => {
4. console.info('Succeeded in sending extend action.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to sendExtendAction. Code is ${err.code}, message is ${err.message}`);
7. });
```

### sendPrivateCommand12+

PhonePC/2in1TabletTVWearable

sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>

发送私有数据至需要与输入法应用通信的系统其他部分。使用promise异步回调。

说明

* 私有数据通道是系统预置输入法应用与系统特定组件（如文本框、桌面应用等）的通信机制，常用于设备级厂商在特定设备上实现自定义的输入法功能。
* 私有数据规格限制：总大小32KB，数量限制5条。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commandData | Record<string, [CommandDataType](js-apis-inputmethodengine.md#commanddatatype12)> | 是 | 私有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800010 | not the preconfigured default input method. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethodEngine.getInputMethodAbility().on('inputStart', (kbController, textInputClient) => {
4. let record: Record<string, inputMethodEngine.CommandDataType> = {
5. "valueString1": "abcdefg",
6. "valueString2": true,
7. "valueString3": 500,
8. }
9. textInputClient.sendPrivateCommand(record).then(() => {
10. }).catch((err: BusinessError) => {
11. if (err !== undefined) {
12. console.error(`sendPrivateCommand catch error: ${err.code} ${err.message}`);
13. }
14. });
15. })
```

### getCallingWindowInfo12+

PhonePC/2in1TabletTVWearable

getCallingWindowInfo(): Promise<WindowInfo>

获取当前拉起输入法的输入框所在应用窗口信息。使用promise异步回调。

说明

本接口仅适用于适配使用[Panel](js-apis-inputmethodengine.md#panel10)作为软键盘窗口的输入法应用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WindowInfo](js-apis-inputmethodengine.md#windowinfo12)> | Promise对象，返回拉起输入法的输入框所在应用窗口信息。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800012 | the input method panel does not exist. |
| 12800013 | window manager service error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputClient.getCallingWindowInfo().then((windowInfo: inputMethodEngine.WindowInfo) => {
4. console.info(`windowInfo.rect: ${windowInfo.rect.left}, ${windowInfo.rect.top}, ${windowInfo.rect.width}, ${windowInfo.rect.height}`);
5. console.info(`windowInfo.status: ${windowInfo.status}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to getCallingWindowInfo. Code is ${err.code}, message is ${err.message}`);
8. });
```

### setPreviewText12+

PhonePC/2in1TabletTVWearable

setPreviewText(text: string, range: Range): Promise<void>

设置预上屏文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 将被预上屏的文本。 |
| range | [Range](js-apis-inputmethodengine.md#range10) | 是 | 目标替换的文本范围。  - 当值为{ start: -1, end: -1 }时，默认将参数text替换当前预上屏区域全部文本。  - 当start等于end，默认将参数text插入start对应的光标位置。  - 当start不等于end，将参数text替换range对应区域的文本。  - 当start与end为其他含有负数值的组合，按照参数错误返回。  - 当输入框已有预上屏文本，参数range不得超过预上屏文本范围，否则按照参数错误返回。  - 当输入框无预上屏文本，参数range不得超过输入框文本范围，否则按照参数错误返回。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800011 | text preview not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let range: inputMethodEngine.Range = { start: 0, end: 1 };
4. inputClient.setPreviewText('test', range).then(() => {
5. console.info('Succeeded in setting preview text.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to setPreviewText. Code is ${err.code}, message is ${err.message}`);
8. });
```

### setPreviewTextSync12+

PhonePC/2in1TabletTVWearable

setPreviewTextSync(text: string, range: Range): void

设置预上屏文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 将被预上屏的文本。 |
| range | [Range](js-apis-inputmethodengine.md#range10) | 是 | 目标替换的文本范围。  - 当值为{ start: -1, end: -1 }时，默认将参数text替换当前预上屏区域全部文本。  - 当start等于end，默认将参数text插入start对应的光标位置。  - 当start不等于end，将参数text替换range对应区域的文本。  - 当start与end为其他含有负数值的组合，按照参数错误返回。  - 当输入框已有预上屏文本，参数range不得超过预上屏文本范围，否则按照参数错误返回。  - 当输入框无预上屏文本，参数range不得超过输入框文本范围，否则按照参数错误返回。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800011 | text preview not supported. |

**示例：**

```
1. let range: inputMethodEngine.Range = { start: 0, end: 1 };
2. inputClient.setPreviewTextSync('test', range);
```

### finishTextPreview12+

PhonePC/2in1TabletTVWearable

finishTextPreview(): Promise<void>

结束预上屏。使用promise异步回调。

说明

若当前输入框已有预上屏状态文本，调用此接口后，预上屏内容将被系统正式上屏。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800011 | text preview not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputClient.finishTextPreview().then(() => {
4. console.info('Succeeded in finishing text preview.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to finishTextPreview. Code is ${err.code}, message is ${err.message}`);
7. });
```

### finishTextPreviewSync12+

PhonePC/2in1TabletTVWearable

finishTextPreviewSync(): void

结束预上屏。

说明

若当前输入框已有预上屏状态文本，调用此接口后，预上屏内容将被系统正式上屏。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800011 | text preview not supported. |

**示例：**

```
1. inputClient.finishTextPreviewSync();
```

### sendMessage15+

PhonePC/2in1TabletTVWearable

sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>

发送自定义通信至已绑定当前输入法应用的编辑框应用。使用Promise异步回调。

说明

该接口需要编辑框与输入法绑定并进入编辑状态，且输入法应用处于完整体验模式时才能调用。

msgId最大限制256B，msgParam最大限制128KB。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msgId | string | 是 | 需要发送至已绑定当前输入法应用的编辑框应用的自定义数据的标识符。 |
| msgParam | ArrayBuffer | 否 | 需要发送至已绑定当前输入法应用的编辑框应用的自定义数据的消息体。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Incorrect parameter types. 2. Incorrect parameter length. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800009 | input method client detached. |
| 12800014 | the input method is in basic mode. |
| 12800015 | the other side does not accept the request. |
| 12800016 | input method client is not editable. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let msgId: string = "testMsgId";
4. let msgParam: ArrayBuffer = new ArrayBuffer(128);
5. inputClient.sendMessage(msgId, msgParam).then(() => {
6. console.info('Succeeded send message.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to send message. Code is ${err.code}, message is ${err.message}`);
9. });
```

### recvMessage15+

PhonePC/2in1TabletTVWearable

recvMessage(msgHandler?: MessageHandler): void;

注册或取消注册Messagehandler。

说明

[MessageHandler](js-apis-inputmethodengine.md#messagehandler15)对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的[onTerminated](js-apis-inputmethodengine.md#onterminated15)回调函数。

未填写参数，则取消全局已注册的[MessageHandler](js-apis-inputmethodengine.md#messagehandler15)，并会触发被取消注册对象中[onTerminated](js-apis-inputmethodengine.md#onterminated15)回调函数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msgHandler | [MessageHandler](js-apis-inputmethodengine.md#messagehandler15) | 否 | 该对象将通过[onMessage](js-apis-inputmethodengine.md#onmessage15)接收来自已绑定当前输入法应用的编辑框应用所发送的自定义通信数据，并通过[onTerminated](js-apis-inputmethodengine.md#onterminated15)接收终止此对象订阅的消息。  若不填写此参数，则取消全局已注册的[MessageHandler](js-apis-inputmethodengine.md#messagehandler15)对象，同时触发其[onTerminated](js-apis-inputmethodengine.md#onterminated15)回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```
1. inputMethodEngine.getInputMethodAbility()
2. .on('inputStart',
3. (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
4. let keyboardController: inputMethodEngine.KeyboardController = kbController;
5. let inputClient: inputMethodEngine.InputClient = client;
6. let messageHandler: inputMethodEngine.MessageHandler = {
7. onTerminated(): void {
8. console.info('OnTerminated.');
9. },
10. onMessage(msgId: string, msgParam?: ArrayBuffer): void {
11. console.info('recv message.');
12. }
13. }
14. inputClient.recvMessage(messageHandler);
15. });
```

### getAttachOptions19+

PhonePC/2in1TabletTVWearable

getAttachOptions(): AttachOptions

获取绑定输入法时的附加选项。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AttachOptions](js-apis-inputmethodengine.md#attachoptions19) | 返回绑定输入法时的附加选项内容。 |

注意

从API version 20 开始，错误码801 Capability not supported.被移除。

**示例：**

```
1. let attachOptions: inputMethodEngine.AttachOptions = inputClient.getAttachOptions();
2. console.info(`Succeeded in getting AttachOptions, AttachOptions is ${attachOptions}`);
```

### on('attachOptionsDidChange')19+

PhonePC/2in1TabletTVWearable

on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void

订阅绑定输入法时的附加选项变更事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 绑定输入法时的附加选项变更事件，固定取值为'attachOptionsDidChange'。 |
| callback | Callback<[AttachOptions](js-apis-inputmethodengine.md#attachoptions19)> | 是 | 回调函数，返回绑定输入法时的附加选项。 |

注意

从API version 20 开始，错误码801 Capability not supported.被移除。

**示例：**

```
1. let attachOptionsDidChangeCallback: (attachOptions: inputMethodEngine.AttachOptions) => void =
2. (attachOptions: inputMethodEngine.AttachOptions) => {
3. console.info(`AttachOptionsDidChangeCallback1: attachOptionsDidChange event triggered`);
4. };

6. inputClient.on('attachOptionsDidChange', attachOptionsDidChangeCallback);
7. console.info(`attachOptionsDidChangeCallback subscribed to attachOptionsDidChange`);
8. inputClient.off('attachOptionsDidChange', attachOptionsDidChangeCallback);
9. console.info(`attachOptionsDidChange unsubscribed from attachOptionsDidChange`);
```

### off('attachOptionsDidChange')19+

PhonePC/2in1TabletTVWearable

off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void

取消订阅绑定输入法时的附加选项变更事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 绑定输入法时的附加选项变更事件，固定取值为'attachOptionsDidChange'。 |
| callback | Callback<[AttachOptions](js-apis-inputmethodengine.md#attachoptions19)> | 否 | 取消订阅的回调函数。参数不填写时，默认取消订阅type对应的所有回调事件。 |

**示例：**

```
1. let attachOptionsDidChangeCallback: (attachOptions: inputMethodEngine.AttachOptions) => void =
2. (attachOptions: inputMethodEngine.AttachOptions) => {
3. console.info(`AttachOptionsDidChangeCallback1: attachOptionsDidChange event triggered`);
4. };

6. inputClient.on('attachOptionsDidChange', attachOptionsDidChangeCallback);
7. console.info(`attachOptionsDidChangeCallback subscribed to attachOptionsDidChange`);
8. inputClient.off('attachOptionsDidChange', attachOptionsDidChangeCallback);
9. console.info(`attachOptionsDidChange unsubscribed from attachOptionsDidChange`);
```

### CapitalizeMode20+

PhonePC/2in1TabletTVWearable

枚举，定义了文本首字母大写的不同模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不进行任何首字母大写处理。 |
| SENTENCES | 1 | 每个句子的首字母大写。 |
| WORDS | 2 | 每个单词的首字母大写。 |
| CHARACTERS | 3 | 每个字母都大写。 |

### EditorAttribute

PhonePC/2in1TabletTVWearable

编辑框属性值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enterKeyType | number | 是 | 否 | 编辑框的功能属性，详见[常量中的功能键定义](js-apis-inputmethodengine.md#常量)。 |
| inputPattern | number | 是 | 否 | 编辑框的文本属性，详见[常量中的编辑框定义](js-apis-inputmethodengine.md#常量)。 |
| isTextPreviewSupported12+ | boolean | 否 | 否 | 编辑框是否支持预上屏。  - 值为true，表示支持。  - 值为false，表示不支持。 |
| bundleName14+ | string | 是 | 是 | 编辑框所属应用包名；该值可能为""，使用该属性时需要考虑为""的场景。 |
| immersiveMode15+ | [ImmersiveMode](js-apis-inputmethodengine.md#immersivemode15) | 是 | 是 | 输入法沉浸模式。 |
| windowId18+ | number | 是 | 是 | 编辑框设置所属窗口ID。 |
| displayId18+ | number | 是 | 是 | 编辑框设置窗口对应的屏幕ID。如果没有设置windowId，取当前焦点窗口屏幕ID。 |
| placeholder20+ | string | 是 | 是 | 编辑框设置的占位符信息。 |
| abilityName20+ | string | 是 | 是 | 编辑框设置的ability名称。 |
| capitalizeMode20+ | [CapitalizeMode](js-apis-inputmethodengine.md#capitalizemode20) | 是 | 是 | 编辑框设置大小写模式。如果没有设置或设置非法值，默认不进行任何首字母大写处理。 |
| gradientMode20+ | [GradientMode](js-apis-inputmethodengine.md#gradientmode20) | 是 | 是 | 渐变模式。如果没有设置或设置非法值，默认不使用渐变模式。 |
| extraConfig22+ | [InputMethodExtraConfig](js-apis-inputmethod-extraconfig.md#inputmethodextraconfig) | 是 | 是 | 输入法扩展信息。 |

## KeyEvent

PhonePC/2in1TabletTVWearable

按键属性值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keyCode | number | 是 | 否 | 按键的键值。键码值说明参考[KeyCode](js-apis-keycode.md#keycode)。 |
| keyAction | number | 是 | 否 | 按键事件类型。  - 当值为2时，表示按下事件；  - 当值为3时，表示抬起事件。 |

## PanelFlag10+

PhonePC/2in1TabletTVWearable

输入法面板状态类型枚举。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FLG\_FIXED | 0 | 固定态面板类型。 |
| FLG\_FLOATING | 1 | 悬浮态面板类型。 |
| FLAG\_CANDIDATE15+ | 2 | 候选词态面板类型。 |

## PanelType10+

PhonePC/2in1TabletTVWearable

输入法面板类型枚举。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SOFT\_KEYBOARD | 0 | 软键盘类型。 |
| STATUS\_BAR | 1 | 状态栏类型。 |

## PanelInfo10+

PhonePC/2in1TabletTVWearable

输入法面板属性。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [PanelType](js-apis-inputmethodengine.md#paneltype10) | 否 | 否 | 面板的类型。 |
| flag | [PanelFlag](js-apis-inputmethodengine.md#panelflag10) | 否 | 是 | 面板的状态类型。 |

## PanelRect12+

PhonePC/2in1TabletTVWearable

输入法面板位置大小信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| landscapeRect | [window.Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 横屏状态时输入法面板窗口的位置大小。 |
| portraitRect | [window.Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 竖屏状态时输入法面板窗口的位置大小。 |

## EnhancedPanelRect15+

PhonePC/2in1TabletTVWearable

增强的输入法面板位置、大小信息，包含自定义避让区域、自定义热区。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| landscapeRect | [window.Rect](arkts-apis-window-i.md#rect7) | 否 | 是 | 横屏状态时输入法面板窗口的位置大小。  - 当fullScreenMode不填写或值为false时，此属性为必选。 |
| portraitRect | [window.Rect](arkts-apis-window-i.md#rect7) | 否 | 是 | 竖屏状态时，输入法面板窗口的位置大小。  - 当fullScreenMode不填写或值为false时，此属性为必选。 |
| landscapeAvoidY | number | 否 | 是 | 横屏状态时，面板中的避让线距离面板顶部的距离，单位px。默认值为0。  - 应用内其他系统组件会对避让线以下的输入法面板区域进行避让。  - 面板为固定态时，避让线到屏幕底部的高度不能超过屏幕高度的70%。 |
| landscapeInputRegion | Array<[window.Rect](arkts-apis-window-i.md#rect7)> | 否 | 是 | 横屏状态时，面板接收输入事件的区域。  - 数组大小限制为[1, 4]。默认值为横屏时的面板大小。  - 传入的热区位置是相对于输入法面板窗口左顶点的位置。 |
| portraitAvoidY | number | 否 | 是 | 竖屏状态时，面板中的避让线距离面板顶部的距离，单位px。默认值为0。  - 应用内其他系统组件会对避让线以下的输入法面板区域进行避让。  - 面板为固定态时，避让线到屏幕底部的高度不能超过屏幕高度的70%。 |
| portraitInputRegion | Array<[window.Rect](arkts-apis-window-i.md#rect7)> | 否 | 是 | 竖屏状态时，面板接收输入事件的区域。  - 数组大小限制为[1, 4]。默认值为竖屏时的面板大小。  - 传入的热区位置是相对于输入法面板窗口左顶点的位置。 |
| fullScreenMode | boolean | 否 | 是 | 是否开启全屏模式。默认值为false。  - 值为true，landscapeRect和portraitRect可不填写。  - 值为false，landscapeRect和portraitRect为必选属性。 |

## KeyboardArea15+

PhonePC/2in1TabletTVWearable

面板中的键盘区域。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | number | 否 | 否 | 键盘区域的上边界到面板区域上边界的距离，单位为px，该参数为整数。 |
| bottom | number | 否 | 否 | 键盘区域的下边界到面板区域下边界的距离，单位为px，该参数为整数。 |
| left | number | 否 | 否 | 键盘区域的左边界到面板区域左边界的距离，单位为px，该参数为整数。 |
| right | number | 否 | 否 | 键盘区域的右边界到面板区域右边界的距离，单位为px，该参数为整数。 |

## AttachOptions19+

PhonePC/2in1TabletTVWearable

绑定输入法时的附加选项。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| requestKeyboardReason | [RequestKeyboardReason](js-apis-inputmethodengine.md#requestkeyboardreason19) | 否 | 是 | 该属性由编辑框应用设置，如果没有设置或设置非法值，则默认没有特定的原因触发键盘请求。 |
| isSimpleKeyboardEnabled20+ | boolean | 否 | 是 | 是否使能简单键盘，该属性由编辑框应用设置，true表示使能简单键盘，false表示不使能简单键盘。  如果没有设置或设置非法值，则默认不使能简单键盘。 |

## WindowInfo12+

PhonePC/2in1TabletTVWearable

窗口信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rect | [window.Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 窗口矩形区域。 |
| status | [window.WindowStatusType](arkts-apis-window-e.md#windowstatustype11) | 否 | 否 | 窗口模式类型。 |

## ImmersiveMode15+

PhonePC/2in1TabletTVWearable

枚举，输入法沉浸模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE\_IMMERSIVE | 0 | 不使用沉浸模式。 |
| IMMERSIVE | 1 | 沉浸模式，由输入法应用确定沉浸模式类型。 |
| LIGHT\_IMMERSIVE | 2 | 浅色沉浸模式。 |
| DARK\_IMMERSIVE | 3 | 深色沉浸模式。 |

## RequestKeyboardReason19+

PhonePC/2in1TabletTVWearable

枚举，请求键盘输入的原因。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 表示没有特定的原因触发键盘请求。 |
| MOUSE | 1 | 表示键盘请求是由鼠标操作触发的。 |
| TOUCH | 2 | 表示键盘请求是由触摸操作触发的。 |
| OTHER | 20 | 表示键盘请求是由其他原因触发的。 |

## GradientMode20+

PhonePC/2in1TabletTVWearable

枚举，输入法渐变模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不使用渐变模式。 |
| LINEAR\_GRADIENT | 1 | 线性渐变。 |

## ImmersiveEffect20+

PhonePC/2in1TabletTVWearable

沉浸效果。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| gradientHeight | number | 否 | 否 | 渐变高度，不能超过屏幕高度的15%。 |
| gradientMode | [GradientMode](js-apis-inputmethodengine.md#gradientmode20) | 否 | 否 | 渐变模式。 |

## SystemPanelInsets21+

PhonePC/2in1TabletTVWearable

输入法软键盘相对系统面板的偏移区域。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bottom | number | 是 | 否 | 键盘区域的下边界到系统面板区域下边界的距离，单位为px，该参数为整数。 |
| left | number | 是 | 否 | 键盘区域的左边界到系统面板区域左边界的距离，单位为px，该参数为整数。 |
| right | number | 是 | 否 | 键盘区域的右边界到系统面板区域右边界的距离，单位为px，该参数为整数。 |

## TextInputClient(deprecated)

PhonePC/2in1TabletTVWearable

下列API示例中都需使用[on('inputStart')](js-apis-inputmethodengine.md#oninputstartdeprecated)回调获取到TextInputClient实例，再通过此实例调用对应方法。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[InputClient](js-apis-inputmethodengine.md#inputclient9)替代。

### getForward(deprecated)

PhonePC/2in1TabletTVWearable

getForward(length:number, callback: AsyncCallback<string>): void

获取光标前固定长度的文本。使用callback异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[getForward](js-apis-inputmethodengine.md#getforward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当光标前固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. textInputClient.getForward(length, (err: BusinessError, text: string) => {
5. if (err) {
6. console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in getting forward, text: ' + text);
10. });
```

### getForward(deprecated)

PhonePC/2in1TabletTVWearable

getForward(length:number): Promise<string>

获取光标前固定长度的文本。使用promise异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[getForward](js-apis-inputmethodengine.md#getforward9-1)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回光标前固定长度的文本。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. textInputClient.getForward(length).then((text: string) => {
5. console.info('Succeeded in getting forward, text: ' + text);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
8. });
```

### getBackward(deprecated)

PhonePC/2in1TabletTVWearable

getBackward(length:number, callback: AsyncCallback<string>): void

获取光标后固定长度的文本。使用callback异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[getBackward](js-apis-inputmethodengine.md#getbackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当光标后固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. textInputClient.getBackward(length, (err: BusinessError, text: string) => {
5. if (err) {
6. console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in getting backward, text: ' + text);
10. });
```

### getBackward(deprecated)

PhonePC/2in1TabletTVWearable

getBackward(length:number): Promise<string>

获取光标后固定长度的文本。使用promise异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[getBackward](js-apis-inputmethodengine.md#getbackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回光标后固定长度的文本。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. textInputClient.getBackward(length).then((text: string) => {
5. console.info(`'Succeeded in getting backward: ${text}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
8. });
```

### deleteForward(deprecated)

PhonePC/2in1TabletTVWearable

deleteForward(length:number, callback: AsyncCallback<boolean>): void

删除光标前固定长度的文本。使用callback异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[deleteForward](js-apis-inputmethodengine.md#deleteforward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当光标前固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. textInputClient.deleteForward(length, (err: BusinessError, result: boolean) => {
5. if (err) {
6. console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
7. return;
8. }
9. if (result) {
10. console.info('Succeeded in deleting forward.');
11. } else {
12. console.error('Failed to deleteForward.');
13. }
14. });
```

### deleteForward(deprecated)

PhonePC/2in1TabletTVWearable

deleteForward(length:number): Promise<boolean>

删除光标前固定长度的文本。使用promise异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[deleteForward](js-apis-inputmethodengine.md#deleteforward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示删除光标前固定长度的文本成功；返回false表示删除光标前固定长度的文本失败。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. textInputClient.deleteForward(length).then((result: boolean) => {
5. if (result) {
6. console.info('Succeeded in deleting forward.');
7. } else {
8. console.error('Failed to delete forward.');
9. }
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
12. });
```

### deleteBackward(deprecated)

PhonePC/2in1TabletTVWearable

deleteBackward(length:number, callback: AsyncCallback<boolean>): void

删除光标后固定长度的文本。使用callback异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[deleteBackward](js-apis-inputmethodengine.md#deletebackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当光标后固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. textInputClient.deleteBackward(length, (err: BusinessError, result: boolean) => {
5. if (err) {
6. console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
7. return;
8. }
9. if (result) {
10. console.info('Succeeded in deleting backward.');
11. } else {
12. console.error('Failed to deleteBackward.');
13. }
14. });
```

### deleteBackward(deprecated)

PhonePC/2in1TabletTVWearable

deleteBackward(length:number): Promise<boolean>

删除光标后固定长度的文本。使用promise异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[deleteBackward](js-apis-inputmethodengine.md#deletebackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示删除光标后固定长度的文本成功；返回false表示删除光标后固定长度的文本失败。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let length: number = 1;
4. textInputClient.deleteBackward(length).then((result: boolean) => {
5. if (result) {
6. console.info('Succeeded in deleting backward.');
7. } else {
8. console.error('Failed to deleteBackward.');
9. }
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
12. });
```

### sendKeyFunction(deprecated)

PhonePC/2in1TabletTVWearable

sendKeyFunction(action: number, callback: AsyncCallback<boolean>): void

发送功能键。使用callback异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[sendKeyFunction](js-apis-inputmethodengine.md#sendkeyfunction9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | number | 是 | 功能键键值。  - 当值为0时，表示无效按键；  - 当值为1时，表示确认键（即回车键）。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当功能键发送成功，err为undefined，data为true；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let action: number = 1;
4. textInputClient.sendKeyFunction(action, (err: BusinessError, result: boolean) => {
5. if (err) {
6. console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
7. return;
8. }
9. if (result) {
10. console.info('Succeeded in sending key function.');
11. } else {
12. console.error('Failed to sendKeyFunction.');
13. }
14. });
```

### sendKeyFunction(deprecated)

PhonePC/2in1TabletTVWearable

sendKeyFunction(action: number): Promise<boolean>

发送功能键。使用promise异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[sendKeyFunction](js-apis-inputmethodengine.md#sendkeyfunction9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | number | 是 | 功能键键值。  当值为0时，表示无效按键；  当值为1时，表示确认键（即回车键）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示发送功能键成功；返回false表示发送功能键失败。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let action: number = 1;
4. textInputClient.sendKeyFunction(action).then((result: boolean) => {
5. if (result) {
6. console.info('Succeeded in sending key function.');
7. } else {
8. console.error('Failed to sendKeyFunction.');
9. }
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to sendKeyFunction:. Code is ${err.code}, message is ${err.message}`);
12. });
```

### insertText(deprecated)

PhonePC/2in1TabletTVWearable

insertText(text:string, callback: AsyncCallback<boolean>): void

插入文本。使用callback异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[insertText](js-apis-inputmethodengine.md#inserttext9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 文本。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当文本插入成功，err为undefined，data为true；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. textInputClient.insertText('test', (err: BusinessError, result: boolean) => {
4. if (err) {
5. console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
6. return;
7. }
8. if (result) {
9. console.info('Succeeded in inserting text.');
10. } else {
11. console.error('Failed to insertText.');
12. }
13. });
```

### insertText(deprecated)

PhonePC/2in1TabletTVWearable

insertText(text:string): Promise<boolean>

插入文本。使用promise异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[insertText](js-apis-inputmethodengine.md#inserttext9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 文本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示插入文本成功；返回false表示插入文本失败。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. textInputClient.insertText('test').then((result: boolean) => {
4. if (result) {
5. console.info('Succeeded in inserting text.');
6. } else {
7. console.error('Failed to insertText.');
8. }
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
11. });
```

### getEditorAttribute(deprecated)

PhonePC/2in1TabletTVWearable

getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void

获取编辑框属性值。使用callback异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[getEditorAttribute](js-apis-inputmethodengine.md#geteditorattribute9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[EditorAttribute](js-apis-inputmethodengine.md#editorattribute)> | 是 | 回调函数。当编辑框的属性值获取成功，err为undefined，data为编辑框属性值；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

4. textInputClient.getEditorAttribute((err: BusinessError,
5. editorAttribute: inputMethodEngine.EditorAttribute) => {
6. if (err) {
7. console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
8. return;
9. }
10. console.info(`editorAttribute.inputPattern: ${editorAttribute.inputPattern}`);
11. console.info(`editorAttribute.enterKeyType: ${editorAttribute.enterKeyType}`);
12. });
```

### getEditorAttribute(deprecated)

PhonePC/2in1TabletTVWearable

getEditorAttribute(): Promise<EditorAttribute>

获取编辑框属性值。使用promise异步回调。

说明

从API version 8开始支持，API version 9开始废弃，建议使用[getEditorAttribute](js-apis-inputmethodengine.md#geteditorattribute9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[EditorAttribute](js-apis-inputmethodengine.md#editorattribute)> | Promise对象，返回编辑框属性值。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. textInputClient.getEditorAttribute().then((editorAttribute: inputMethodEngine.EditorAttribute) => {
4. console.info(`editorAttribute.inputPattern: ${editorAttribute.inputPattern}`);
5. console.info(`editorAttribute.enterKeyType: ${editorAttribute.enterKeyType}}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
8. });
```
