---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-5051
title: ArkUI
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.5(17) > OS平台能力 > API变更清单 > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:18+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:60e563a46c4c47c8e4ff748062bc15b48f2dc5d7dc5a71556982c18a8e25478b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：window；  API声明：function createWindow(config: Configuration, callback: AsyncCallback<Window>): void;  差异内容：1300008 | 类名：window；  API声明：function createWindow(config: Configuration, callback: AsyncCallback<Window>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：window；  API声明：function createWindow(config: Configuration): Promise<Window>;  差异内容：1300008 | 类名：window；  API声明：function createWindow(config: Configuration): Promise<Window>;  差异内容：NA | api/@ohos.window.d.ts |
| 函数变更 | 类名：SwiperController；  API声明：changeIndex(index: number, animationMode: SwiperAnimationMode | boolean);  差异内容：animationMode: SwiperAnimationMode | boolean | 类名：SwiperController；  API声明：changeIndex(index: number, animationMode?: SwiperAnimationMode | boolean);  差异内容：animationMode?: SwiperAnimationMode | boolean | component/swiper.d.ts |
| 新增API | NA | 类名：NavDestinationState；  API声明：ON\_ACTIVE = 8  差异内容：ON\_ACTIVE = 8 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationState；  API声明：ON\_INACTIVE = 9  差异内容：ON\_INACTIVE = 9 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface AxisEvent  差异内容：declare interface AxisEvent | component/common.d.ts |
| 新增API | NA | 类名：AxisEvent；  API声明：action: AxisAction;  差异内容：action: AxisAction; | component/common.d.ts |
| 新增API | NA | 类名：AxisEvent；  API声明：displayX: number;  差异内容：displayX: number; | component/common.d.ts |
| 新增API | NA | 类名：AxisEvent；  API声明：displayY: number;  差异内容：displayY: number; | component/common.d.ts |
| 新增API | NA | 类名：AxisEvent；  API声明：windowX: number;  差异内容：windowX: number; | component/common.d.ts |
| 新增API | NA | 类名：AxisEvent；  API声明：windowY: number;  差异内容：windowY: number; | component/common.d.ts |
| 新增API | NA | 类名：AxisEvent；  API声明：x: number;  差异内容：x: number; | component/common.d.ts |
| 新增API | NA | 类名：AxisEvent；  API声明：y: number;  差异内容：y: number; | component/common.d.ts |
| 新增API | NA | 类名：AxisEvent；  API声明：scrollStep?: number;  差异内容：scrollStep?: number; | component/common.d.ts |
| 新增API | NA | 类名：AxisEvent；  API声明：propagation: Callback<void>;  差异内容：propagation: Callback<void>; | component/common.d.ts |
| 新增API | NA | 类名：AxisEvent；  API声明：getHorizontalAxisValue(): number;  差异内容：getHorizontalAxisValue(): number; | component/common.d.ts |
| 新增API | NA | 类名：AxisEvent；  API声明：getVerticalAxisValue(): number;  差异内容：getVerticalAxisValue(): number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum AxisAction  差异内容：declare enum AxisAction | component/enums.d.ts |
| 新增API | NA | 类名：AxisAction；  API声明：NONE = 0  差异内容：NONE = 0 | component/enums.d.ts |
| 新增API | NA | 类名：AxisAction；  API声明：BEGIN = 1  差异内容：BEGIN = 1 | component/enums.d.ts |
| 新增API | NA | 类名：AxisAction；  API声明：UPDATE = 2  差异内容：UPDATE = 2 | component/enums.d.ts |
| 新增API | NA | 类名：AxisAction；  API声明：END = 3  差异内容：END = 3 | component/enums.d.ts |
| 新增API | NA | 类名：AxisAction；  API声明：CANCEL = 4  差异内容：CANCEL = 4 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum NavDestinationActiveReason  差异内容：declare enum NavDestinationActiveReason | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationActiveReason；  API声明：TRANSITION = 0  差异内容：TRANSITION = 0 | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationActiveReason；  API声明：CONTENT\_COVER = 1  差异内容：CONTENT\_COVER = 1 | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationActiveReason；  API声明：SHEET = 2  差异内容：SHEET = 2 | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationActiveReason；  API声明：DIALOG = 3  差异内容：DIALOG = 3 | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationActiveReason；  API声明：OVERLAY = 4  差异内容：OVERLAY = 4 | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationActiveReason；  API声明：APP\_STATE = 5  差异内容：APP\_STATE = 5 | component/nav\_destination.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIContext；  API声明：static createUIContextWithoutWindow(context: common.UIAbilityContext | common.ExtensionContext): UIContext | undefined;  差异内容：static createUIContextWithoutWindow(context: common.UIAbilityContext | common.ExtensionContext): UIContext | undefined; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIContext；  API声明：static destroyUIContextWithoutWindow(): void;  差异内容：static destroyUIContextWithoutWindow(): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CommonMethod；  API声明：onAxisEvent(event: Callback<AxisEvent>): T;  差异内容：onAxisEvent(event: Callback<AxisEvent>): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CommonMethod；  API声明：onVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): void;  差异内容：onVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): void; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextContentControllerBase；  API声明：clearPreviewText(): void;  差异内容：clearPreviewText(): void; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ImageAnimatorAttribute；  API声明：monitorInvisibleArea(monitorInvisibleArea: boolean): ImageAnimatorAttribute;  差异内容：monitorInvisibleArea(monitorInvisibleArea: boolean): ImageAnimatorAttribute; | component/image\_animator.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：NavDestinationAttribute；  API声明：onActive(callback: Optional<Callback<NavDestinationActiveReason>>): NavDestinationAttribute;  差异内容：onActive(callback: Optional<Callback<NavDestinationActiveReason>>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：NavDestinationAttribute；  API声明：onInactive(callback: Optional<Callback<NavDestinationActiveReason>>): NavDestinationAttribute;  差异内容：onInactive(callback: Optional<Callback<NavDestinationActiveReason>>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：setFollowParentWindowLayoutEnabled(enabled: boolean): Promise<void>;  差异内容：setFollowParentWindowLayoutEnabled(enabled: boolean): Promise<void>; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：setWindowShadowRadius(radius: number): void;  差异内容：setWindowShadowRadius(radius: number): void; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：setWindowCornerRadius(cornerRadius: number): Promise<void>;  差异内容：setWindowCornerRadius(cornerRadius: number): Promise<void>; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：getWindowCornerRadius(): number;  差异内容：getWindowCornerRadius(): number; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：setFollowParentMultiScreenPolicy(enabled: boolean): Promise<void>;  差异内容：setFollowParentMultiScreenPolicy(enabled: boolean): Promise<void>; | api/@ohos.window.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PiPConfiguration；  API声明：localStorage?: LocalStorage;  差异内容：localStorage?: LocalStorage; | api/@ohos.PiPWindow.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BaseEvent；  API声明：rollAngle?: number;  差异内容：rollAngle?: number; | component/common.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：WindowStage；  API声明：setWindowRectAutoSave(enabled: boolean): Promise<void>;  差异内容：setWindowRectAutoSave(enabled: boolean): Promise<void>; | 类名：WindowStage；  API声明：setWindowRectAutoSave(enabled: boolean, isSaveBySpecifiedFlag: boolean): Promise<void>;  差异内容：setWindowRectAutoSave(enabled: boolean, isSaveBySpecifiedFlag: boolean): Promise<void>; | api/@ohos.window.d.ts |
