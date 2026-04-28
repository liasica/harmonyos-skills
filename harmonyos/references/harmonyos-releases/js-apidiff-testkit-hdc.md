---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-testkit-hdc
title: Test Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta1引入的API > Test Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:14+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4965f5b07def1efeff2b5fed3cd64e22f15f4203ff5bd9abd9936e548de48866
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：abilityDelegatorRegistry；  API声明：function getAbilityDelegator(): AbilityDelegator;  差异内容：NA | 类名：abilityDelegatorRegistry；  API声明：function getAbilityDelegator(): AbilityDelegator;  差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：abilityDelegatorRegistry；  API声明：function getArguments(): AbilityDelegatorArgs;  差异内容：NA | 类名：abilityDelegatorRegistry；  API声明：function getArguments(): AbilityDelegatorArgs;  差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：abilityDelegatorRegistry；  API声明： export enum AbilityLifecycleState  差异内容：NA | 类名：abilityDelegatorRegistry；  API声明： export enum AbilityLifecycleState  差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：AbilityLifecycleState；  API声明：UNINITIALIZED  差异内容：NA | 类名：AbilityLifecycleState；  API声明：UNINITIALIZED  差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：AbilityLifecycleState；  API声明：CREATE  差异内容：NA | 类名：AbilityLifecycleState；  API声明：CREATE  差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：AbilityLifecycleState；  API声明：FOREGROUND  差异内容：NA | 类名：AbilityLifecycleState；  API声明：FOREGROUND  差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：AbilityLifecycleState；  API声明：BACKGROUND  差异内容：NA | 类名：AbilityLifecycleState；  API声明：BACKGROUND  差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：AbilityLifecycleState；  API声明：DESTROY  差异内容：NA | 类名：AbilityLifecycleState；  API声明：DESTROY  差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：WindowFilter；  API声明：actived?: boolean;  差异内容：NA | 类名：WindowFilter；  API声明：actived?: boolean;  差异内容：11 | api/@ohos.UiTest.d.ts |
| API废弃版本变更 | 类名：UiWindow；  API声明：isActived(): Promise<boolean>;  差异内容：NA | 类名：UiWindow；  API声明：isActived(): Promise<boolean>;  差异内容：11 | api/@ohos.UiTest.d.ts |
| 错误码变更 | 类名：UiDriver；  API声明：assertComponentExist(by: By): Promise<void>;  差异内容：NA | 类名：UiDriver；  API声明：assertComponentExist(by: By): Promise<void>;  差异内容：17000002,17000003,401 | api/@ohos.UiTest.d.ts |
| 权限变更 | 类名：global；  API声明： declare namespace abilityDelegatorRegistry  差异内容：N/A | 类名：global；  API声明： declare namespace abilityDelegatorRegistry  差异内容：NA | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| 权限变更 | 类名：global；  API声明： export interface TestRunner  差异内容：N/A | 类名：global；  API声明： export interface TestRunner  差异内容：NA | api/@ohos.application.testRunner.d.ts |
| 新增API | NA | 类名：Driver；  API声明：fling(direction: UiDirection, speed: number): Promise<void>;  差异内容：fling(direction: UiDirection, speed: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：WindowFilter；  API声明：active?: boolean;  差异内容：active?: boolean; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface UIElementInfo  差异内容： declare interface UIElementInfo | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIElementInfo；  API声明：readonly bundleName: string;  差异内容：readonly bundleName: string; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIElementInfo；  API声明：readonly type: string;  差异内容：readonly type: string; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIElementInfo；  API声明：readonly text: string;  差异内容：readonly text: string; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface UIEventObserver  差异内容： declare interface UIEventObserver | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIEventObserver；  API声明：once(type: 'toastShow', callback: Callback<UIElementInfo>): void;  差异内容：once(type: 'toastShow', callback: Callback<UIElementInfo>): void; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIEventObserver；  API声明：once(type: 'dialogShow', callback: Callback<UIElementInfo>): void;  差异内容：once(type: 'dialogShow', callback: Callback<UIElementInfo>): void; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum UiDirection  差异内容： declare enum UiDirection | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UiDirection；  API声明：LEFT = 0  差异内容：LEFT = 0 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UiDirection；  API声明：RIGHT = 1  差异内容：RIGHT = 1 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UiDirection；  API声明：UP = 2  差异内容：UP = 2 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UiDirection；  API声明：DOWN = 3  差异内容：DOWN = 3 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum MouseButton  差异内容： declare enum MouseButton | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：MouseButton；  API声明：MOUSE\_BUTTON\_LEFT = 0  差异内容：MOUSE\_BUTTON\_LEFT = 0 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：MouseButton；  API声明：MOUSE\_BUTTON\_RIGHT = 1  差异内容：MOUSE\_BUTTON\_RIGHT = 1 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：MouseButton；  API声明：MOUSE\_BUTTON\_MIDDLE = 2  差异内容：MOUSE\_BUTTON\_MIDDLE = 2 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：On；  API声明：within(on: On): On;  差异内容：within(on: On): On; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：On；  API声明：inWindow(bundleName: string): On;  差异内容：inWindow(bundleName: string): On; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：On；  API声明：description(val: string, pattern?: MatchPattern): On;  差异内容：description(val: string, pattern?: MatchPattern): On; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Component；  API声明：getDescription(): Promise<string>;  差异内容：getDescription(): Promise<string>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：mouseClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>;  差异内容：mouseClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：mouseMoveTo(p: Point): Promise<void>;  差异内容：mouseMoveTo(p: Point): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>;  差异内容：mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number, speed?: number): Promise<void>;  差异内容：mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number, speed?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：screenCapture(savePath: string, rect?: Rect): Promise<boolean>;  差异内容：screenCapture(savePath: string, rect?: Rect): Promise<boolean>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：createUIEventObserver(): UIEventObserver;  差异内容：createUIEventObserver(): UIEventObserver; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：mouseDoubleClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>;  差异内容：mouseDoubleClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>;  差异内容：mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：mouseMoveWithTrack(from: Point, to: Point, speed?: number): Promise<void>;  差异内容：mouseMoveWithTrack(from: Point, to: Point, speed?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：mouseDrag(from: Point, to: Point, speed?: number): Promise<void>;  差异内容：mouseDrag(from: Point, to: Point, speed?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：inputText(p: Point, text: string): Promise<void>;  差异内容：inputText(p: Point, text: string): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UiWindow；  API声明：isActive(): Promise<boolean>;  差异内容：isActive(): Promise<boolean>; | api/@ohos.UiTest.d.ts |
