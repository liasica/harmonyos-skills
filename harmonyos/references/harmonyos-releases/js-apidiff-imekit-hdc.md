---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-hdc
title: IME Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta1引入的API > IME Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:05+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d75081d8934aba6825b2e011912a9d5440b81d0b9ee32b7913d54aa3b2673038
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：InputMethodExtensionAbility；  API声明：onCreate(want: Want): void;  差异内容：401 | 类名：InputMethodExtensionAbility；  API声明：onCreate(want: Want): void;  差异内容：NA | api/@ohos.InputMethodExtensionAbility.d.ts |
| 错误码变更 | 类名：InputMethodExtensionAbility；  API声明：onDestroy(): void;  差异内容：401 | 类名：InputMethodExtensionAbility；  API声明：onDestroy(): void;  差异内容：NA | api/@ohos.InputMethodExtensionAbility.d.ts |
| 错误码变更 | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void;  差异内容：12800005,12800008,201,401 | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void;  差异内容：12800005,12800008,401 | api/@ohos.inputMethod.d.ts |
| 错误码变更 | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty): Promise<boolean>;  差异内容：12800005,12800008,201,401 | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty): Promise<boolean>;  差异内容：12800005,12800008,401 | api/@ohos.inputMethod.d.ts |
| 错误码变更 | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：12800005,12800008,201,401 | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：12800005,12800008,401 | api/@ohos.inputMethod.d.ts |
| 错误码变更 | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise<boolean>;  差异内容：12800005,12800008,201,401 | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise<boolean>;  差异内容：12800005,12800008,401 | api/@ohos.inputMethod.d.ts |
| 错误码变更 | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：12800005,12800008,201,401 | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：12800005,12800008,401 | api/@ohos.inputMethod.d.ts |
| 错误码变更 | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise<boolean>;  差异内容：12800005,12800008,201,401 | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise<boolean>;  差异内容：12800005,12800008,401 | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void;  差异内容：ohos.permission.CONNECT\_IME\_ABILITY | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void;  差异内容：NA | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty): Promise<boolean>;  差异内容：ohos.permission.CONNECT\_IME\_ABILITY | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty): Promise<boolean>;  差异内容：NA | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：ohos.permission.CONNECT\_IME\_ABILITY | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：NA | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise<boolean>;  差异内容：ohos.permission.CONNECT\_IME\_ABILITY | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise<boolean>;  差异内容：NA | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：ohos.permission.CONNECT\_IME\_ABILITY | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：NA | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise<boolean>;  差异内容：ohos.permission.CONNECT\_IME\_ABILITY | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise<boolean>;  差异内容：NA | api/@ohos.inputMethod.d.ts |
| 属性变更 | 类名：InputMethodProperty；  API声明：extra: object;  差异内容：extra: object; | 类名：InputMethodProperty；  API声明：extra?: object;  差异内容：extra?: object; | api/@ohos.inputMethod.d.ts |
| 属性变更 | 类名：InputMethodSubtype；  API声明：extra: object;  差异内容：extra: object; | 类名：InputMethodSubtype；  API声明：extra?: object;  差异内容：extra?: object; | api/@ohos.InputMethodSubtype.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明：function getDefaultInputMethod(): InputMethodProperty;  差异内容：function getDefaultInputMethod(): InputMethodProperty; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明：function getSystemInputMethodConfigAbility(): ElementName;  差异内容：function getSystemInputMethodConfigAbility(): ElementName; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodSetting；  API声明：getInputMethodsSync(enable: boolean): Array<InputMethodProperty>;  差异内容：getInputMethodsSync(enable: boolean): Array<InputMethodProperty>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodSetting；  API声明：getAllInputMethods(callback: AsyncCallback<Array<InputMethodProperty>>): void;  差异内容：getAllInputMethods(callback: AsyncCallback<Array<InputMethodProperty>>): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodSetting；  API声明：getAllInputMethods(): Promise<Array<InputMethodProperty>>;  差异内容：getAllInputMethods(): Promise<Array<InputMethodProperty>>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodSetting；  API声明：getAllInputMethodsSync(): Array<InputMethodProperty>;  差异内容：getAllInputMethodsSync(): Array<InputMethodProperty>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：attach(showKeyboard: boolean, textConfig: TextConfig, callback: AsyncCallback<void>): void;  差异内容：attach(showKeyboard: boolean, textConfig: TextConfig, callback: AsyncCallback<void>): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：attach(showKeyboard: boolean, textConfig: TextConfig): Promise<void>;  差异内容：attach(showKeyboard: boolean, textConfig: TextConfig): Promise<void>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：showTextInput(callback: AsyncCallback<void>): void;  差异内容：showTextInput(callback: AsyncCallback<void>): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：showTextInput(): Promise<void>;  差异内容：showTextInput(): Promise<void>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：hideTextInput(callback: AsyncCallback<void>): void;  差异内容：hideTextInput(callback: AsyncCallback<void>): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：hideTextInput(): Promise<void>;  差异内容：hideTextInput(): Promise<void>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：detach(callback: AsyncCallback<void>): void;  差异内容：detach(callback: AsyncCallback<void>): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：detach(): Promise<void>;  差异内容：detach(): Promise<void>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：setCallingWindow(windowId: number, callback: AsyncCallback<void>): void;  差异内容：setCallingWindow(windowId: number, callback: AsyncCallback<void>): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：setCallingWindow(windowId: number): Promise<void>;  差异内容：setCallingWindow(windowId: number): Promise<void>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：updateCursor(cursorInfo: CursorInfo, callback: AsyncCallback<void>): void;  差异内容：updateCursor(cursorInfo: CursorInfo, callback: AsyncCallback<void>): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：updateCursor(cursorInfo: CursorInfo): Promise<void>;  差异内容：updateCursor(cursorInfo: CursorInfo): Promise<void>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：changeSelection(text: string, start: number, end: number, callback: AsyncCallback<void>): void;  差异内容：changeSelection(text: string, start: number, end: number, callback: AsyncCallback<void>): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：changeSelection(text: string, start: number, end: number): Promise<void>;  差异内容：changeSelection(text: string, start: number, end: number): Promise<void>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：updateAttribute(attribute: InputAttribute, callback: AsyncCallback<void>): void;  差异内容：updateAttribute(attribute: InputAttribute, callback: AsyncCallback<void>): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：updateAttribute(attribute: InputAttribute): Promise<void>;  差异内容：updateAttribute(attribute: InputAttribute): Promise<void>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：on(type: 'selectByRange', callback: Callback<Range>): void;  差异内容：on(type: 'selectByRange', callback: Callback<Range>): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：off(type: 'selectByRange', callback?: Callback<Range>): void;  差异内容：off(type: 'selectByRange', callback?: Callback<Range>): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：on(type: 'selectByMovement', callback: Callback<Movement>): void;  差异内容：on(type: 'selectByMovement', callback: Callback<Movement>): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：off(type: 'selectByMovement', callback?: Callback<Movement>): void;  差异内容：off(type: 'selectByMovement', callback?: Callback<Movement>): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：on(type: 'insertText', callback: (text: string) => void): void;  差异内容：on(type: 'insertText', callback: (text: string) => void): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：off(type: 'insertText', callback?: (text: string) => void): void;  差异内容：off(type: 'insertText', callback?: (text: string) => void): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：on(type: 'deleteLeft', callback: (length: number) => void): void;  差异内容：on(type: 'deleteLeft', callback: (length: number) => void): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：off(type: 'deleteLeft', callback?: (length: number) => void): void;  差异内容：off(type: 'deleteLeft', callback?: (length: number) => void): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：on(type: 'deleteRight', callback: (length: number) => void): void;  差异内容：on(type: 'deleteRight', callback: (length: number) => void): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：off(type: 'deleteRight', callback?: (length: number) => void): void;  差异内容：off(type: 'deleteRight', callback?: (length: number) => void): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：on(type: 'sendKeyboardStatus', callback: (keyboardStatus: KeyboardStatus) => void): void;  差异内容：on(type: 'sendKeyboardStatus', callback: (keyboardStatus: KeyboardStatus) => void): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：off(type: 'sendKeyboardStatus', callback?: (keyboardStatus: KeyboardStatus) => void): void;  差异内容：off(type: 'sendKeyboardStatus', callback?: (keyboardStatus: KeyboardStatus) => void): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：on(type: 'sendFunctionKey', callback: (functionKey: FunctionKey) => void): void;  差异内容：on(type: 'sendFunctionKey', callback: (functionKey: FunctionKey) => void): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：off(type: 'sendFunctionKey', callback?: (functionKey: FunctionKey) => void): void;  差异内容：off(type: 'sendFunctionKey', callback?: (functionKey: FunctionKey) => void): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：on(type: 'moveCursor', callback: (direction: Direction) => void): void;  差异内容：on(type: 'moveCursor', callback: (direction: Direction) => void): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：off(type: 'moveCursor', callback?: (direction: Direction) => void): void;  差异内容：off(type: 'moveCursor', callback?: (direction: Direction) => void): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：on(type: 'handleExtendAction', callback: (action: ExtendAction) => void): void;  差异内容：on(type: 'handleExtendAction', callback: (action: ExtendAction) => void): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：off(type: 'handleExtendAction', callback?: (action: ExtendAction) => void): void;  差异内容：off(type: 'handleExtendAction', callback?: (action: ExtendAction) => void): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：on(type: 'getLeftTextOfCursor', callback: (length: number) => string): void;  差异内容：on(type: 'getLeftTextOfCursor', callback: (length: number) => string): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：off(type: 'getLeftTextOfCursor', callback?: (length: number) => string): void;  差异内容：off(type: 'getLeftTextOfCursor', callback?: (length: number) => string): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：on(type: 'getRightTextOfCursor', callback: (length: number) => string): void;  差异内容：on(type: 'getRightTextOfCursor', callback: (length: number) => string): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：off(type: 'getRightTextOfCursor', callback?: (length: number) => string): void;  差异内容：off(type: 'getRightTextOfCursor', callback?: (length: number) => string): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：on(type: 'getTextIndexAtCursor', callback: () => number): void;  差异内容：on(type: 'getTextIndexAtCursor', callback: () => number): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：off(type: 'getTextIndexAtCursor', callback?: () => number): void;  差异内容：off(type: 'getTextIndexAtCursor', callback?: () => number): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodProperty；  API声明：readonly labelId?: number;  差异内容：readonly labelId?: number; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明： export enum Direction  差异内容： export enum Direction | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：Direction；  API声明：CURSOR\_UP = 1  差异内容：CURSOR\_UP = 1 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：Direction；  API声明：CURSOR\_DOWN  差异内容：CURSOR\_DOWN | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：Direction；  API声明：CURSOR\_LEFT  差异内容：CURSOR\_LEFT | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：Direction；  API声明：CURSOR\_RIGHT  差异内容：CURSOR\_RIGHT | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明： export interface Range  差异内容： export interface Range | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：Range；  API声明：start: number;  差异内容：start: number; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：Range；  API声明：end: number;  差异内容：end: number; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明： export interface Movement  差异内容： export interface Movement | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：Movement；  API声明：direction: Direction;  差异内容：direction: Direction; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明： export enum TextInputType  差异内容： export enum TextInputType | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextInputType；  API声明：NONE = -1  差异内容：NONE = -1 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextInputType；  API声明：TEXT = 0  差异内容：TEXT = 0 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextInputType；  API声明：MULTILINE  差异内容：MULTILINE | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextInputType；  API声明：NUMBER  差异内容：NUMBER | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextInputType；  API声明：PHONE  差异内容：PHONE | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextInputType；  API声明：DATETIME  差异内容：DATETIME | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextInputType；  API声明：EMAIL\_ADDRESS  差异内容：EMAIL\_ADDRESS | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextInputType；  API声明：URL  差异内容：URL | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextInputType；  API声明：VISIBLE\_PASSWORD  差异内容：VISIBLE\_PASSWORD | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextInputType；  API声明：NUMBER\_PASSWORD  差异内容：NUMBER\_PASSWORD | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明： export enum EnterKeyType  差异内容： export enum EnterKeyType | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：EnterKeyType；  API声明：UNSPECIFIED = 0  差异内容：UNSPECIFIED = 0 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：EnterKeyType；  API声明：NONE  差异内容：NONE | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：EnterKeyType；  API声明：GO  差异内容：GO | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：EnterKeyType；  API声明：SEARCH  差异内容：SEARCH | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：EnterKeyType；  API声明：SEND  差异内容：SEND | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：EnterKeyType；  API声明：NEXT  差异内容：NEXT | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：EnterKeyType；  API声明：DONE  差异内容：DONE | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：EnterKeyType；  API声明：PREVIOUS  差异内容：PREVIOUS | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明： export enum KeyboardStatus  差异内容： export enum KeyboardStatus | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：KeyboardStatus；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：KeyboardStatus；  API声明：HIDE = 1  差异内容：HIDE = 1 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：KeyboardStatus；  API声明：SHOW = 2  差异内容：SHOW = 2 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明： export interface InputAttribute  差异内容： export interface InputAttribute | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputAttribute；  API声明：textInputType: TextInputType;  差异内容：textInputType: TextInputType; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputAttribute；  API声明：enterKeyType: EnterKeyType;  差异内容：enterKeyType: EnterKeyType; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明： export interface FunctionKey  差异内容： export interface FunctionKey | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：enterKeyType: EnterKeyType;  差异内容：enterKeyType: EnterKeyType; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明： export interface CursorInfo  差异内容： export interface CursorInfo | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：CursorInfo；  API声明：left: number;  差异内容：left: number; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：CursorInfo；  API声明：top: number;  差异内容：top: number; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：CursorInfo；  API声明：width: number;  差异内容：width: number; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：CursorInfo；  API声明：height: number;  差异内容：height: number; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明： export interface TextConfig  差异内容： export interface TextConfig | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextConfig；  API声明：inputAttribute: InputAttribute;  差异内容：inputAttribute: InputAttribute; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextConfig；  API声明：cursorInfo?: CursorInfo;  差异内容：cursorInfo?: CursorInfo; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextConfig；  API声明：selection?: Range;  差异内容：selection?: Range; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextConfig；  API声明：windowId?: number;  差异内容：windowId?: number; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明： export enum ExtendAction  差异内容： export enum ExtendAction | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：ExtendAction；  API声明：SELECT\_ALL = 0  差异内容：SELECT\_ALL = 0 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：ExtendAction；  API声明：CUT = 3  差异内容：CUT = 3 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：ExtendAction；  API声明：COPY = 4  差异内容：COPY = 4 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：ExtendAction；  API声明：PASTE = 5  差异内容：PASTE = 5 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明： export interface InputWindowInfo  差异内容： export interface InputWindowInfo | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputWindowInfo；  API声明：name: string;  差异内容：name: string; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputWindowInfo；  API声明：left: number;  差异内容：left: number; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputWindowInfo；  API声明：top: number;  差异内容：top: number; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputWindowInfo；  API声明：width: number;  差异内容：width: number; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputWindowInfo；  API声明：height: number;  差异内容：height: number; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明：const PATTERN\_PASSWORD\_SCREEN\_LOCK: number;  差异内容：const PATTERN\_PASSWORD\_SCREEN\_LOCK: number; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明：const PATTERN\_PASSWORD\_NUMBER: number;  差异内容：const PATTERN\_PASSWORD\_NUMBER: number; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明：type CommandDataType = number | string | boolean;  差异内容：type CommandDataType = number | string | boolean; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：KeyboardController；  API声明：exitCurrentInputType(callback: AsyncCallback<void>): void;  差异内容：exitCurrentInputType(callback: AsyncCallback<void>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：KeyboardController；  API声明：exitCurrentInputType(): Promise<void>;  差异内容：exitCurrentInputType(): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputMethodAbility；  API声明：on(type: 'securityModeChange', callback: Callback<SecurityMode>): void;  差异内容：on(type: 'securityModeChange', callback: Callback<SecurityMode>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputMethodAbility；  API声明：off(type: 'securityModeChange', callback?: Callback<SecurityMode>): void;  差异内容：off(type: 'securityModeChange', callback?: Callback<SecurityMode>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputMethodAbility；  API声明：on(type: 'privateCommand', callback: Callback<Record<string, CommandDataType>>): void;  差异内容：on(type: 'privateCommand', callback: Callback<Record<string, CommandDataType>>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputMethodAbility；  API声明：off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void;  差异内容：off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputMethodAbility；  API声明：getSecurityMode(): SecurityMode;  差异内容：getSecurityMode(): SecurityMode; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputMethodAbility；  API声明：createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void;  差异内容：createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputMethodAbility；  API声明：createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>;  差异内容：createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputMethodAbility；  API声明：destroyPanel(panel: Panel, callback: AsyncCallback<void>): void;  差异内容：destroyPanel(panel: Panel, callback: AsyncCallback<void>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputMethodAbility；  API声明：destroyPanel(panel: Panel): Promise<void>;  差异内容：destroyPanel(panel: Panel): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：deleteForwardSync(length: number): void;  差异内容：deleteForwardSync(length: number): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：deleteBackwardSync(length: number): void;  差异内容：deleteBackwardSync(length: number): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：insertTextSync(text: string): void;  差异内容：insertTextSync(text: string): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：getForwardSync(length: number): string;  差异内容：getForwardSync(length: number): string; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：getBackwardSync(length: number): string;  差异内容：getBackwardSync(length: number): string; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：getEditorAttributeSync(): EditorAttribute;  差异内容：getEditorAttributeSync(): EditorAttribute; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：moveCursorSync(direction: number): void;  差异内容：moveCursorSync(direction: number): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：selectByRange(range: Range, callback: AsyncCallback<void>): void;  差异内容：selectByRange(range: Range, callback: AsyncCallback<void>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：selectByRange(range: Range): Promise<void>;  差异内容：selectByRange(range: Range): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：selectByRangeSync(range: Range): void;  差异内容：selectByRangeSync(range: Range): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：selectByMovement(movement: Movement, callback: AsyncCallback<void>): void;  差异内容：selectByMovement(movement: Movement, callback: AsyncCallback<void>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：selectByMovement(movement: Movement): Promise<void>;  差异内容：selectByMovement(movement: Movement): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：selectByMovementSync(movement: Movement): void;  差异内容：selectByMovementSync(movement: Movement): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：getTextIndexAtCursor(callback: AsyncCallback<number>): void;  差异内容：getTextIndexAtCursor(callback: AsyncCallback<number>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：getTextIndexAtCursor(): Promise<number>;  差异内容：getTextIndexAtCursor(): Promise<number>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：getTextIndexAtCursorSync(): number;  差异内容：getTextIndexAtCursorSync(): number; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void;  差异内容：sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：sendExtendAction(action: ExtendAction): Promise<void>;  差异内容：sendExtendAction(action: ExtendAction): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>;  差异内容：sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：getCallingWindowInfo(): Promise<WindowInfo>;  差异内容：getCallingWindowInfo(): Promise<WindowInfo>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：setPreviewText(text: string, range: Range): Promise<void>;  差异内容：setPreviewText(text: string, range: Range): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：setPreviewTextSync(text: string, range: Range): void;  差异内容：setPreviewTextSync(text: string, range: Range): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：finishTextPreview(): Promise<void>;  差异内容：finishTextPreview(): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient；  API声明：finishTextPreviewSync(): void;  差异内容：finishTextPreviewSync(): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：KeyboardDelegate；  API声明：on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void;  差异内容：on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：KeyboardDelegate；  API声明：off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void;  差异内容：off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：KeyboardDelegate；  API声明：on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void;  差异内容：on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：KeyboardDelegate；  API声明：off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void;  差异内容：off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明： interface Panel  差异内容： interface Panel | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：setUiContent(path: string, callback: AsyncCallback<void>): void;  差异内容：setUiContent(path: string, callback: AsyncCallback<void>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：setUiContent(path: string): Promise<void>;  差异内容：setUiContent(path: string): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：setUiContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：setUiContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：setUiContent(path: string, storage: LocalStorage): Promise<void>;  差异内容：setUiContent(path: string, storage: LocalStorage): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：resize(width: number, height: number, callback: AsyncCallback<void>): void;  差异内容：resize(width: number, height: number, callback: AsyncCallback<void>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：resize(width: number, height: number): Promise<void>;  差异内容：resize(width: number, height: number): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：moveTo(x: number, y: number, callback: AsyncCallback<void>): void;  差异内容：moveTo(x: number, y: number, callback: AsyncCallback<void>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：moveTo(x: number, y: number): Promise<void>;  差异内容：moveTo(x: number, y: number): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：show(callback: AsyncCallback<void>): void;  差异内容：show(callback: AsyncCallback<void>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：show(): Promise<void>;  差异内容：show(): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：hide(callback: AsyncCallback<void>): void;  差异内容：hide(callback: AsyncCallback<void>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：hide(): Promise<void>;  差异内容：hide(): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：on(type: 'show', callback: () => void): void;  差异内容：on(type: 'show', callback: () => void): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：off(type: 'show', callback?: () => void): void;  差异内容：off(type: 'show', callback?: () => void): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：on(type: 'hide', callback: () => void): void;  差异内容：on(type: 'hide', callback: () => void): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：off(type: 'hide', callback?: () => void): void;  差异内容：off(type: 'hide', callback?: () => void): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：changeFlag(flag: PanelFlag): void;  差异内容：changeFlag(flag: PanelFlag): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：setPrivacyMode(isPrivacyMode: boolean): void;  差异内容：setPrivacyMode(isPrivacyMode: boolean): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：adjustPanelRect(flag: PanelFlag, rect: PanelRect): void;  差异内容：adjustPanelRect(flag: PanelFlag, rect: PanelRect): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：on(type: 'sizeChange', callback: Callback<window.Size>): void;  差异内容：on(type: 'sizeChange', callback: Callback<window.Size>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：off(type: 'sizeChange', callback?: Callback<window.Size>): void;  差异内容：off(type: 'sizeChange', callback?: Callback<window.Size>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：EditorAttribute；  API声明：isTextPreviewSupported: boolean;  差异内容：isTextPreviewSupported: boolean; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明： export enum PanelFlag  差异内容： export enum PanelFlag | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：PanelFlag；  API声明：FLG\_FIXED = 0  差异内容：FLG\_FIXED = 0 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：PanelFlag；  API声明：FLG\_FLOATING  差异内容：FLG\_FLOATING | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明： export enum PanelType  差异内容： export enum PanelType | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：PanelType；  API声明：SOFT\_KEYBOARD = 0  差异内容：SOFT\_KEYBOARD = 0 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：PanelType；  API声明：STATUS\_BAR  差异内容：STATUS\_BAR | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明： export interface PanelInfo  差异内容： export interface PanelInfo | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：PanelInfo；  API声明：type: PanelType;  差异内容：type: PanelType; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：PanelInfo；  API声明：flag?: PanelFlag;  差异内容：flag?: PanelFlag; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明： export enum Direction  差异内容： export enum Direction | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Direction；  API声明：CURSOR\_UP = 1  差异内容：CURSOR\_UP = 1 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Direction；  API声明：CURSOR\_DOWN  差异内容：CURSOR\_DOWN | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Direction；  API声明：CURSOR\_LEFT  差异内容：CURSOR\_LEFT | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Direction；  API声明：CURSOR\_RIGHT  差异内容：CURSOR\_RIGHT | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明： export enum SecurityMode  差异内容： export enum SecurityMode | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：SecurityMode；  API声明：BASIC = 0  差异内容：BASIC = 0 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：SecurityMode；  API声明：FULL  差异内容：FULL | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明： export interface Range  差异内容： export interface Range | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Range；  API声明：start: number;  差异内容：start: number; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Range；  API声明：end: number;  差异内容：end: number; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明： export interface Movement  差异内容： export interface Movement | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Movement；  API声明：direction: Direction;  差异内容：direction: Direction; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明： export enum ExtendAction  差异内容： export enum ExtendAction | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：ExtendAction；  API声明：SELECT\_ALL = 0  差异内容：SELECT\_ALL = 0 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：ExtendAction；  API声明：CUT = 3  差异内容：CUT = 3 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：ExtendAction；  API声明：COPY = 4  差异内容：COPY = 4 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：ExtendAction；  API声明：PASTE = 5  差异内容：PASTE = 5 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明： export interface WindowInfo  差异内容： export interface WindowInfo | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：WindowInfo；  API声明：rect: window.Rect;  差异内容：rect: window.Rect; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：WindowInfo；  API声明：status: window.WindowStatusType;  差异内容：status: window.WindowStatusType; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明： export interface PanelRect  差异内容： export interface PanelRect | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：PanelRect；  API声明：landscapeRect: window.Rect;  差异内容：landscapeRect: window.Rect; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：PanelRect；  API声明：portraitRect: window.Rect;  差异内容：portraitRect: window.Rect; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputMethodExtensionContext；  API声明：startAbility(want: Want): Promise<void>;  差异内容：startAbility(want: Want): Promise<void>; | api/@ohos.InputMethodExtensionContext.d.ts |
| 新增API | NA | 类名：InputMethodSubtype；  API声明：readonly labelId?: number;  差异内容：readonly labelId?: number; | api/@ohos.InputMethodSubtype.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface PanelInfo  差异内容： export interface PanelInfo | api/@ohos.inputMethod.Panel.d.ts |
| 新增API | NA | 类名：PanelInfo；  API声明：type: PanelType;  差异内容：type: PanelType; | api/@ohos.inputMethod.Panel.d.ts |
| 新增API | NA | 类名：PanelInfo；  API声明：flag?: PanelFlag;  差异内容：flag?: PanelFlag; | api/@ohos.inputMethod.Panel.d.ts |
| 新增API | NA | 类名：global；  API声明： export enum PanelFlag  差异内容： export enum PanelFlag | api/@ohos.inputMethod.Panel.d.ts |
| 新增API | NA | 类名：PanelFlag；  API声明：FLAG\_FIXED = 0  差异内容：FLAG\_FIXED = 0 | api/@ohos.inputMethod.Panel.d.ts |
| 新增API | NA | 类名：PanelFlag；  API声明：FLAG\_FLOATING  差异内容：FLAG\_FLOATING | api/@ohos.inputMethod.Panel.d.ts |
| 新增API | NA | 类名：PanelFlag；  API声明：FLAG\_CANDIDATE  差异内容：FLAG\_CANDIDATE | api/@ohos.inputMethod.Panel.d.ts |
| 新增API | NA | 类名：global；  API声明： export enum PanelType  差异内容： export enum PanelType | api/@ohos.inputMethod.Panel.d.ts |
| 新增API | NA | 类名：PanelType；  API声明：SOFT\_KEYBOARD = 0  差异内容：SOFT\_KEYBOARD = 0 | api/@ohos.inputMethod.Panel.d.ts |
| 新增API | NA | 类名：PanelType；  API声明：STATUS\_BAR  差异内容：STATUS\_BAR | api/@ohos.inputMethod.Panel.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface PatternOptions  差异内容： export interface PatternOptions | api/@ohos.inputMethodList.d.ets |
| 新增API | NA | 类名：PatternOptions；  API声明：defaultSelected?: number;  差异内容：defaultSelected?: number; | api/@ohos.inputMethodList.d.ets |
| 新增API | NA | 类名：PatternOptions；  API声明：patterns: Array<Pattern>;  差异内容：patterns: Array<Pattern>; | api/@ohos.inputMethodList.d.ets |
| 新增API | NA | 类名：PatternOptions；  API声明：action: (index: number) => void;  差异内容：action: (index: number) => void; | api/@ohos.inputMethodList.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface Pattern  差异内容： export interface Pattern | api/@ohos.inputMethodList.d.ets |
| 新增API | NA | 类名：Pattern；  API声明：icon: Resource;  差异内容：icon: Resource; | api/@ohos.inputMethodList.d.ets |
| 新增API | NA | 类名：Pattern；  API声明：selectedIcon: Resource;  差异内容：selectedIcon: Resource; | api/@ohos.inputMethodList.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct InputMethodListDialog  差异内容： export declare struct InputMethodListDialog | api/@ohos.inputMethodList.d.ets |
| 新增API | NA | 类名：InputMethodListDialog；  API声明：controller: CustomDialogController;  差异内容：controller: CustomDialogController; | api/@ohos.inputMethodList.d.ets |
| 新增API | NA | 类名：InputMethodListDialog；  API声明：patternOptions?: PatternOptions;  差异内容：patternOptions?: PatternOptions; | api/@ohos.inputMethodList.d.ets |
