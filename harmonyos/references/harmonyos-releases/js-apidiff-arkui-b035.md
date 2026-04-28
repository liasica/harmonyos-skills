---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-b035
title: ArkUI
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:29+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:88ea275cd883f1ed74ac2d54e6ca8cf200b295fd208feaca0f40ba71027f6a8a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：Window；  API声明：setWindowLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Window；  API声明：setWindowLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void;  差异内容：12 | api/@ohos.window.d.ts |
| API废弃版本变更 | 类名：Window；  API声明：setWindowSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Window；  API声明：setWindowSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void;  差异内容：12 | api/@ohos.window.d.ts |
| API废弃版本变更 | 类名：Window；  API声明：setWindowSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Window；  API声明：setWindowSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void;  差异内容：12 | api/@ohos.window.d.ts |
| API卡片权限变更 | 类名：global；  API声明： interface SymbolGlyphInterface  差异内容：NA | 类名：global；  API声明： interface SymbolGlyphInterface  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare enum SymbolRenderingStrategy  差异内容：NA | 类名：global；  API声明： declare enum SymbolRenderingStrategy  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：SymbolRenderingStrategy；  API声明：SINGLE = 0  差异内容：NA | 类名：SymbolRenderingStrategy；  API声明：SINGLE = 0  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：SymbolRenderingStrategy；  API声明：MULTIPLE\_COLOR = 1  差异内容：NA | 类名：SymbolRenderingStrategy；  API声明：MULTIPLE\_COLOR = 1  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：SymbolRenderingStrategy；  API声明：MULTIPLE\_OPACITY = 2  差异内容：NA | 类名：SymbolRenderingStrategy；  API声明：MULTIPLE\_OPACITY = 2  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare enum SymbolEffectStrategy  差异内容：NA | 类名：global；  API声明： declare enum SymbolEffectStrategy  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：SymbolEffectStrategy；  API声明：NONE = 0  差异内容：NA | 类名：SymbolEffectStrategy；  API声明：NONE = 0  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：SymbolEffectStrategy；  API声明：SCALE = 1  差异内容：NA | 类名：SymbolEffectStrategy；  API声明：SCALE = 1  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：SymbolEffectStrategy；  API声明：HIERARCHICAL = 2  差异内容：NA | 类名：SymbolEffectStrategy；  API声明：HIERARCHICAL = 2  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare enum EffectDirection  差异内容：NA | 类名：global；  API声明： declare enum EffectDirection  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：EffectDirection；  API声明：DOWN = 0  差异内容：NA | 类名：EffectDirection；  API声明：DOWN = 0  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：EffectDirection；  API声明：UP = 1  差异内容：NA | 类名：EffectDirection；  API声明：UP = 1  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare enum EffectScope  差异内容：NA | 类名：global；  API声明： declare enum EffectScope  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：EffectScope；  API声明：LAYER = 0  差异内容：NA | 类名：EffectScope；  API声明：LAYER = 0  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：EffectScope；  API声明：WHOLE = 1  差异内容：NA | 类名：EffectScope；  API声明：WHOLE = 1  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare enum EffectFillStyle  差异内容：NA | 类名：global；  API声明： declare enum EffectFillStyle  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：EffectFillStyle；  API声明：CUMULATIVE = 0  差异内容：NA | 类名：EffectFillStyle；  API声明：CUMULATIVE = 0  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：EffectFillStyle；  API声明：ITERATIVE = 1  差异内容：NA | 类名：EffectFillStyle；  API声明：ITERATIVE = 1  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class SymbolEffect  差异内容：NA | 类名：global；  API声明： declare class SymbolEffect  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class ScaleSymbolEffect  差异内容：NA | 类名：global；  API声明： declare class ScaleSymbolEffect  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：ScaleSymbolEffect；  API声明：scope?: EffectScope;  差异内容：NA | 类名：ScaleSymbolEffect；  API声明：scope?: EffectScope;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：ScaleSymbolEffect；  API声明：direction?: EffectDirection;  差异内容：NA | 类名：ScaleSymbolEffect；  API声明：direction?: EffectDirection;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class HierarchicalSymbolEffect  差异内容：NA | 类名：global；  API声明： declare class HierarchicalSymbolEffect  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：HierarchicalSymbolEffect；  API声明：fillStyle?: EffectFillStyle;  差异内容：NA | 类名：HierarchicalSymbolEffect；  API声明：fillStyle?: EffectFillStyle;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class AppearSymbolEffect  差异内容：NA | 类名：global；  API声明： declare class AppearSymbolEffect  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：AppearSymbolEffect；  API声明：scope?: EffectScope;  差异内容：NA | 类名：AppearSymbolEffect；  API声明：scope?: EffectScope;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class DisappearSymbolEffect  差异内容：NA | 类名：global；  API声明： declare class DisappearSymbolEffect  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：DisappearSymbolEffect；  API声明：scope?: EffectScope;  差异内容：NA | 类名：DisappearSymbolEffect；  API声明：scope?: EffectScope;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class BounceSymbolEffect  差异内容：NA | 类名：global；  API声明： declare class BounceSymbolEffect  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：BounceSymbolEffect；  API声明：scope?: EffectScope;  差异内容：NA | 类名：BounceSymbolEffect；  API声明：scope?: EffectScope;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：BounceSymbolEffect；  API声明：direction?: EffectDirection;  差异内容：NA | 类名：BounceSymbolEffect；  API声明：direction?: EffectDirection;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class ReplaceSymbolEffect  差异内容：NA | 类名：global；  API声明： declare class ReplaceSymbolEffect  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：ReplaceSymbolEffect；  API声明：scope?: EffectScope;  差异内容：NA | 类名：ReplaceSymbolEffect；  API声明：scope?: EffectScope;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class PulseSymbolEffect  差异内容：NA | 类名：global；  API声明： declare class PulseSymbolEffect  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class SymbolGlyphAttribute  差异内容：NA | 类名：global；  API声明： declare class SymbolGlyphAttribute  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：SymbolGlyphAttribute；  API声明：fontSize(value: number | string | Resource): SymbolGlyphAttribute;  差异内容：NA | 类名：SymbolGlyphAttribute；  API声明：fontSize(value: number | string | Resource): SymbolGlyphAttribute;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：SymbolGlyphAttribute；  API声明：fontColor(value: Array<ResourceColor>): SymbolGlyphAttribute;  差异内容：NA | 类名：SymbolGlyphAttribute；  API声明：fontColor(value: Array<ResourceColor>): SymbolGlyphAttribute;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：SymbolGlyphAttribute；  API声明：fontWeight(value: number | FontWeight | string): SymbolGlyphAttribute;  差异内容：NA | 类名：SymbolGlyphAttribute；  API声明：fontWeight(value: number | FontWeight | string): SymbolGlyphAttribute;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：SymbolGlyphAttribute；  API声明：effectStrategy(value: SymbolEffectStrategy): SymbolGlyphAttribute;  差异内容：NA | 类名：SymbolGlyphAttribute；  API声明：effectStrategy(value: SymbolEffectStrategy): SymbolGlyphAttribute;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：SymbolGlyphAttribute；  API声明：renderingStrategy(value: SymbolRenderingStrategy): SymbolGlyphAttribute;  差异内容：NA | 类名：SymbolGlyphAttribute；  API声明：renderingStrategy(value: SymbolRenderingStrategy): SymbolGlyphAttribute;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：SymbolGlyphAttribute；  API声明：symbolEffect(symbolEffect: SymbolEffect, isActive?: boolean): SymbolGlyphAttribute;  差异内容：NA | 类名：SymbolGlyphAttribute；  API声明：symbolEffect(symbolEffect: SymbolEffect, isActive?: boolean): SymbolGlyphAttribute;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：SymbolGlyphAttribute；  API声明：symbolEffect(symbolEffect: SymbolEffect, triggerValue?: number): SymbolGlyphAttribute;  差异内容：NA | 类名：SymbolGlyphAttribute；  API声明：symbolEffect(symbolEffect: SymbolEffect, triggerValue?: number): SymbolGlyphAttribute;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare const SymbolGlyph: SymbolGlyphInterface;  差异内容：NA | 类名：global；  API声明：declare const SymbolGlyph: SymbolGlyphInterface;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare const SymbolGlyphInstance: SymbolGlyphAttribute;  差异内容：NA | 类名：global；  API声明：declare const SymbolGlyphInstance: SymbolGlyphAttribute;  差异内容：form | component/symbolglyph.d.ts |
| API卡片权限变更 | 类名：global；  API声明： interface SymbolSpanInterface  差异内容：NA | 类名：global；  API声明： interface SymbolSpanInterface  差异内容：form | component/symbol\_span.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class SymbolSpanAttribute  差异内容：NA | 类名：global；  API声明： declare class SymbolSpanAttribute  差异内容：form | component/symbol\_span.d.ts |
| API卡片权限变更 | 类名：SymbolSpanAttribute；  API声明：fontSize(value: number | string | Resource): SymbolSpanAttribute;  差异内容：NA | 类名：SymbolSpanAttribute；  API声明：fontSize(value: number | string | Resource): SymbolSpanAttribute;  差异内容：form | component/symbol\_span.d.ts |
| API卡片权限变更 | 类名：SymbolSpanAttribute；  API声明：fontColor(value: Array<ResourceColor>): SymbolSpanAttribute;  差异内容：NA | 类名：SymbolSpanAttribute；  API声明：fontColor(value: Array<ResourceColor>): SymbolSpanAttribute;  差异内容：form | component/symbol\_span.d.ts |
| API卡片权限变更 | 类名：SymbolSpanAttribute；  API声明：fontWeight(value: number | FontWeight | string): SymbolSpanAttribute;  差异内容：NA | 类名：SymbolSpanAttribute；  API声明：fontWeight(value: number | FontWeight | string): SymbolSpanAttribute;  差异内容：form | component/symbol\_span.d.ts |
| API卡片权限变更 | 类名：SymbolSpanAttribute；  API声明：effectStrategy(value: SymbolEffectStrategy): SymbolSpanAttribute;  差异内容：NA | 类名：SymbolSpanAttribute；  API声明：effectStrategy(value: SymbolEffectStrategy): SymbolSpanAttribute;  差异内容：form | component/symbol\_span.d.ts |
| API卡片权限变更 | 类名：SymbolSpanAttribute；  API声明：renderingStrategy(value: SymbolRenderingStrategy): SymbolSpanAttribute;  差异内容：NA | 类名：SymbolSpanAttribute；  API声明：renderingStrategy(value: SymbolRenderingStrategy): SymbolSpanAttribute;  差异内容：form | component/symbol\_span.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare const SymbolSpan: SymbolSpanInterface;  差异内容：NA | 类名：global；  API声明：declare const SymbolSpan: SymbolSpanInterface;  差异内容：form | component/symbol\_span.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare const SymbolSpanInstance: SymbolSpanAttribute;  差异内容：NA | 类名：global；  API声明：declare const SymbolSpanInstance: SymbolSpanAttribute;  差异内容：form | component/symbol\_span.d.ts |
| 错误码变更 | 类名：ComponentSnapshot；  API声明：get(id: string, callback: AsyncCallback<image.PixelMap>): void;  差异内容：NA | 类名：ComponentSnapshot；  API声明：get(id: string, callback: AsyncCallback<image.PixelMap>, options?: componentSnapshot.SnapshotOptions): void;  差异内容：100001,401 | api/@ohos.arkui.UIContext.d.ts |
| 错误码变更 | 类名：ComponentSnapshot；  API声明：get(id: string): Promise<image.PixelMap>;  差异内容：NA | 类名：ComponentSnapshot；  API声明：get(id: string, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>;  差异内容：100001,401 | api/@ohos.arkui.UIContext.d.ts |
| 错误码变更 | 类名：ComponentSnapshot；  API声明：createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>): void;  差异内容：NA | 类名：ComponentSnapshot；  API声明：createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>, delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): void;  差异内容：100001,401 | api/@ohos.arkui.UIContext.d.ts |
| 错误码变更 | 类名：ComponentSnapshot；  API声明：createFromBuilder(builder: CustomBuilder): Promise<image.PixelMap>;  差异内容：NA | 类名：ComponentSnapshot；  API声明：createFromBuilder(builder: CustomBuilder, delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>;  差异内容：100001,401 | api/@ohos.arkui.UIContext.d.ts |
| 错误码变更 | 类名：window；  API声明：function createWindow(config: Configuration, callback: AsyncCallback<Window>): void;  差异内容：1300001,1300006,1300008,1300009,201,401 | 类名：window；  API声明：function createWindow(config: Configuration, callback: AsyncCallback<Window>): void;  差异内容：1300001,1300004,1300006,1300008,1300009,201,401,801 | api/@ohos.window.d.ts |
| 错误码变更 | 类名：window；  API声明：function createWindow(config: Configuration): Promise<Window>;  差异内容：1300001,1300006,1300008,1300009,201,401 | 类名：window；  API声明：function createWindow(config: Configuration): Promise<Window>;  差异内容：1300001,1300004,1300006,1300008,1300009,201,401,801 | api/@ohos.window.d.ts |
| 错误码变更 | 类名：Window；  API声明：getUIContext(): UIContext;  差异内容：1300002,401 | 类名：Window；  API声明：getUIContext(): UIContext;  差异内容：1300002 | api/@ohos.window.d.ts |
| 错误码变更 | 类名：Window；  API声明：enableLandscapeMultiWindow(): Promise<void>;  差异内容：1300002,1300003,401 | 类名：Window；  API声明：enableLandscapeMultiWindow(): Promise<void>;  差异内容：1300002,1300003 | api/@ohos.window.d.ts |
| 错误码变更 | 类名：Window；  API声明：disableLandscapeMultiWindow(): Promise<void>;  差异内容：1300002,1300003,401 | 类名：Window；  API声明：disableLandscapeMultiWindow(): Promise<void>;  差异内容：1300002,1300003 | api/@ohos.window.d.ts |
| 错误码变更 | 类名：Window；  API声明：off(type: 'noInteractionDetected', callback?: Callback<void>): void;  差异内容：1300002,1300003,801 | 类名：Window；  API声明：off(type: 'noInteractionDetected', callback?: Callback<void>): void;  差异内容：1300002,1300003,401,801 | api/@ohos.window.d.ts |
| 权限变更 | 类名：window；  API声明：function createWindow(config: Configuration, callback: AsyncCallback<Window>): void;  差异内容：NA | 类名：window；  API声明：function createWindow(config: Configuration, callback: AsyncCallback<Window>): void;  差异内容：ohos.permission.SYSTEM\_FLOAT\_WINDOW | api/@ohos.window.d.ts |
| 权限变更 | 类名：window；  API声明：function createWindow(config: Configuration): Promise<Window>;  差异内容：NA | 类名：window；  API声明：function createWindow(config: Configuration): Promise<Window>;  差异内容：ohos.permission.SYSTEM\_FLOAT\_WINDOW | api/@ohos.window.d.ts |
| 权限变更 | 类名：WindowType；  API声明：TYPE\_FLOAT  差异内容：ohos.permission.SYSTEM\_FLOAT\_WINDOW | 类名：WindowType；  API声明：TYPE\_FLOAT  差异内容：NA | api/@ohos.window.d.ts |
| 函数变更 | 类名：componentSnapshot；  API声明：function get(id: string, callback: AsyncCallback<image.PixelMap>): void;  差异内容：NA | 类名：componentSnapshot；  API声明：function get(id: string, callback: AsyncCallback<image.PixelMap>, options?: SnapshotOptions): void;  差异内容：options?: SnapshotOptions | api/@ohos.arkui.componentSnapshot.d.ts |
| 函数变更 | 类名：componentSnapshot；  API声明：function get(id: string): Promise<image.PixelMap>;  差异内容：NA | 类名：componentSnapshot；  API声明：function get(id: string, options?: SnapshotOptions): Promise<image.PixelMap>;  差异内容：options?: SnapshotOptions | api/@ohos.arkui.componentSnapshot.d.ts |
| 函数变更 | 类名：componentSnapshot；  API声明：function createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>): void;  差异内容：NA | 类名：componentSnapshot；  API声明：function createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>, delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): void;  差异内容：delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions | api/@ohos.arkui.componentSnapshot.d.ts |
| 函数变更 | 类名：componentSnapshot；  API声明：function createFromBuilder(builder: CustomBuilder): Promise<image.PixelMap>;  差异内容：NA | 类名：componentSnapshot；  API声明：function createFromBuilder(builder: CustomBuilder, delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): Promise<image.PixelMap>;  差异内容：delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions | api/@ohos.arkui.componentSnapshot.d.ts |
| 函数变更 | 类名：ComponentSnapshot；  API声明：get(id: string, callback: AsyncCallback<image.PixelMap>): void;  差异内容：NA | 类名：ComponentSnapshot；  API声明：get(id: string, callback: AsyncCallback<image.PixelMap>, options?: componentSnapshot.SnapshotOptions): void;  差异内容：options?: componentSnapshot.SnapshotOptions | api/@ohos.arkui.UIContext.d.ts |
| 函数变更 | 类名：ComponentSnapshot；  API声明：get(id: string): Promise<image.PixelMap>;  差异内容：NA | 类名：ComponentSnapshot；  API声明：get(id: string, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>;  差异内容：options?: componentSnapshot.SnapshotOptions | api/@ohos.arkui.UIContext.d.ts |
| 函数变更 | 类名：ComponentSnapshot；  API声明：createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>): void;  差异内容：NA | 类名：ComponentSnapshot；  API声明：createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>, delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): void;  差异内容：delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions | api/@ohos.arkui.UIContext.d.ts |
| 函数变更 | 类名：ComponentSnapshot；  API声明：createFromBuilder(builder: CustomBuilder): Promise<image.PixelMap>;  差异内容：NA | 类名：ComponentSnapshot；  API声明：createFromBuilder(builder: CustomBuilder, delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>;  差异内容：delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions | api/@ohos.arkui.UIContext.d.ts |
| 函数变更 | 类名：Window；  API声明：maximize(): Promise<void>;  差异内容：NA | 类名：Window；  API声明：maximize(presentation?: MaximizePresentation): Promise<void>;  差异内容：presentation?: MaximizePresentation | api/@ohos.window.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：overlay(value: string | CustomBuilder, options?: {  align?: Alignment;  offset?: {  x?: number;  y?: number;  };  }): T;  差异内容：options?: {  align?: Alignment;  offset?: {  x?: number;  y?: number;  };  } | 类名：CommonMethod；  API声明：overlay(value: string | CustomBuilder | ComponentContent, options?: OverlayOptions): T;  差异内容：options?: OverlayOptions | component/common.d.ts |
| 函数变更 | 类名：FolderStackAttribute；  API声明：onFolderStateChange(callback: (event: {  /\*\*  \* folder state.  \*  \* @type { FoldStatus }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \*/  foldStatus: FoldStatus;  }) => void): FolderStackAttribute;  差异内容：callback: (event: {  /\*\*  \* folder state.  \*  \* @type { FoldStatus }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \*/  foldStatus: FoldStatus;  }) => void | 类名：FolderStackAttribute；  API声明：onFolderStateChange(callback: (event: {  /\*\*  \* folder state.  \*  \* @type { FoldStatus }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \*/  /\*\*  \* folder state.  \*  \* @type { FoldStatus }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 12  \*/  foldStatus: FoldStatus;  }) => void): FolderStackAttribute;  差异内容：callback: (event: {  /\*\*  \* folder state.  \*  \* @type { FoldStatus }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \*/  /\*\*  \* folder state.  \*  \* @type { FoldStatus }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 12  \*/  foldStatus: FoldStatus;  }) => void | component/folder\_stack.d.ts |
| 函数变更 | 类名：RichEditorAttribute；  API声明：onReady(callback: () => void): RichEditorAttribute;  差异内容：callback: () => void | 类名：RichEditorAttribute；  API声明：onReady(callback: Callback<void>): RichEditorAttribute;  差异内容：callback: Callback<void> | component/rich\_editor.d.ts |
| 函数变更 | 类名：RichEditorAttribute；  API声明：onSelect(callback: (value: RichEditorSelection) => void): RichEditorAttribute;  差异内容：callback: (value: RichEditorSelection) => void | 类名：RichEditorAttribute；  API声明：onSelect(callback: Callback<RichEditorSelection>): RichEditorAttribute;  差异内容：callback: Callback<RichEditorSelection> | component/rich\_editor.d.ts |
| 函数变更 | 类名：RichEditorAttribute；  API声明：onSelectionChange(callback: (value: RichEditorRange) => void): RichEditorAttribute;  差异内容：callback: (value: RichEditorRange) => void | 类名：RichEditorAttribute；  API声明：onSelectionChange(callback: Callback<RichEditorRange>): RichEditorAttribute;  差异内容：callback: Callback<RichEditorRange> | component/rich\_editor.d.ts |
| 函数变更 | 类名：RichEditorAttribute；  API声明：aboutToIMEInput(callback: (value: RichEditorInsertValue) => boolean): RichEditorAttribute;  差异内容：callback: (value: RichEditorInsertValue) => boolean | 类名：RichEditorAttribute；  API声明：aboutToIMEInput(callback: Callback<RichEditorInsertValue, boolean>): RichEditorAttribute;  差异内容：callback: Callback<RichEditorInsertValue, boolean> | component/rich\_editor.d.ts |
| 函数变更 | 类名：RichEditorAttribute；  API声明：onIMEInputComplete(callback: (value: RichEditorTextSpanResult) => void): RichEditorAttribute;  差异内容：callback: (value: RichEditorTextSpanResult) => void | 类名：RichEditorAttribute；  API声明：onIMEInputComplete(callback: Callback<RichEditorTextSpanResult>): RichEditorAttribute;  差异内容：callback: Callback<RichEditorTextSpanResult> | component/rich\_editor.d.ts |
| 函数变更 | 类名：RichEditorAttribute；  API声明：aboutToDelete(callback: (value: RichEditorDeleteValue) => boolean): RichEditorAttribute;  差异内容：callback: (value: RichEditorDeleteValue) => boolean | 类名：RichEditorAttribute；  API声明：aboutToDelete(callback: Callback<RichEditorDeleteValue, boolean>): RichEditorAttribute;  差异内容：callback: Callback<RichEditorDeleteValue, boolean> | component/rich\_editor.d.ts |
| 函数变更 | 类名：RichEditorAttribute；  API声明：onDeleteComplete(callback: () => void): RichEditorAttribute;  差异内容：callback: () => void | 类名：RichEditorAttribute；  API声明：onDeleteComplete(callback: Callback<void>): RichEditorAttribute;  差异内容：callback: Callback<void> | component/rich\_editor.d.ts |
| 函数变更 | 类名：RichEditorAttribute；  API声明：onPaste(callback: (event?: PasteEvent) => void): RichEditorAttribute;  差异内容：callback: (event?: PasteEvent) => void | 类名：RichEditorAttribute；  API声明：onPaste(callback: PasteEventCallback): RichEditorAttribute;  差异内容：callback: PasteEventCallback | component/rich\_editor.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：overlay(value: string | CustomBuilder, options?: {  align?: Alignment;  offset?: {  x?: number;  y?: number;  };  }): T;  差异内容：value: string | CustomBuilder | 类名：CommonMethod；  API声明：overlay(value: string | CustomBuilder | ComponentContent, options?: OverlayOptions): T;  差异内容：value: string | CustomBuilder | ComponentContent | component/common.d.ts |
| 函数变更 | 类名：SearchAttribute；  API声明：cancelButton(value: {  style?: CancelButtonStyle;  icon?: IconOptions;  }): SearchAttribute;  差异内容：value: {  style?: CancelButtonStyle;  icon?: IconOptions;  } | 类名：SearchAttribute；  API声明：cancelButton(value: CancelButtonOptions | CancelButtonSymbolOptions): SearchAttribute;  差异内容：value: CancelButtonOptions | CancelButtonSymbolOptions | component/search.d.ts |
| 函数变更 | 类名：SearchAttribute；  API声明：searchIcon(value: IconOptions): SearchAttribute;  差异内容：value: IconOptions | 类名：SearchAttribute；  API声明：searchIcon(value: IconOptions | SymbolGlyphModifier): SearchAttribute;  差异内容：value: IconOptions | SymbolGlyphModifier | component/search.d.ts |
| 属性变更 | 类名：RepeatItem；  API声明：index?: number;  差异内容：index?: number; | 类名：RepeatItem；  API声明：index: number;  差异内容：index: number; | component/repeat.d.ts |
| 属性变更 | 类名：RichEditorTextStyle；  API声明：decoration?: {  type: TextDecorationType;  color?: ResourceColor;  };  差异内容：{  type: TextDecorationType;  color?: ResourceColor;  } | 类名：RichEditorTextStyle；  API声明：decoration?: DecorationStyleInterface;  差异内容：DecorationStyleInterface | component/rich\_editor.d.ts |
| 属性变更 | 类名：PasteEvent；  API声明：preventDefault?: () => void;  差异内容：() => void | 类名：PasteEvent；  API声明：preventDefault?: Callback<void>;  差异内容：Callback<void> | component/rich\_editor.d.ts |
| 属性变更 | 类名：RichEditorTextStyleResult；  API声明：decoration: {  type: TextDecorationType;  color: ResourceColor;  };  差异内容：{  type: TextDecorationType;  color: ResourceColor;  } | 类名：RichEditorTextStyleResult；  API声明：decoration: DecorationStyleResult;  差异内容：DecorationStyleResult | component/rich\_editor.d.ts |
| 属性变更 | 类名：RichEditorGesture；  API声明：onClick?: (event: ClickEvent) => void;  差异内容：(event: ClickEvent) => void | 类名：RichEditorGesture；  API声明：onClick?: Callback<ClickEvent>;  差异内容：Callback<ClickEvent> | component/rich\_editor.d.ts |
| 属性变更 | 类名：RichEditorGesture；  API声明：onLongPress?: (event: GestureEvent) => void;  差异内容：(event: GestureEvent) => void | 类名：RichEditorGesture；  API声明：onLongPress?: Callback<GestureEvent>;  差异内容：Callback<GestureEvent> | component/rich\_editor.d.ts |
| 属性变更 | 类名：SelectionMenuOptions；  API声明：onDisappear?: () => void;  差异内容：() => void | 类名：SelectionMenuOptions；  API声明：onDisappear?: Callback<void>;  差异内容：Callback<void> | component/rich\_editor.d.ts |
| 自定义类型变更 | 类名：PiPWindow；  API声明：type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup;  差异内容：VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup | 类名：PiPWindow；  API声明：type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup | VideoLiveControlGroup;  差异内容：VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup | VideoLiveControlGroup | api/@ohos.PiPWindow.d.ts |
| 自定义类型变更 | 类名：PiPWindow；  API声明：type PiPCallActionEvent = 'hangUp' | 'micStateChanged' | 'videoStateChanged';  差异内容：'hangUp' | 'micStateChanged' | 'videoStateChanged' | 类名：PiPWindow；  API声明：type PiPCallActionEvent = 'hangUp' | 'micStateChanged' | 'videoStateChanged' | 'voiceStateChanged';  差异内容：'hangUp' | 'micStateChanged' | 'videoStateChanged' | 'voiceStateChanged' | api/@ohos.PiPWindow.d.ts |
| 自定义类型变更 | 类名：PiPWindow；  API声明：type PiPMeetingActionEvent = 'hangUp' | 'voiceStateChanged' | 'videoStateChanged';  差异内容：'hangUp' | 'voiceStateChanged' | 'videoStateChanged' | 类名：PiPWindow；  API声明：type PiPMeetingActionEvent = 'hangUp' | 'voiceStateChanged' | 'videoStateChanged' | 'micStateChanged';  差异内容：'hangUp' | 'voiceStateChanged' | 'videoStateChanged' | 'micStateChanged' | api/@ohos.PiPWindow.d.ts |
| 自定义类型变更 | 类名：PiPWindow；  API声明：type PiPLiveActionEvent = 'playbackStateChanged';  差异内容：'playbackStateChanged' | 类名：PiPWindow；  API声明：type PiPLiveActionEvent = 'playbackStateChanged' | 'voiceStateChanged';  差异内容：'playbackStateChanged' | 'voiceStateChanged' | api/@ohos.PiPWindow.d.ts |
| 自定义类型变更 | 类名：global；  API声明：declare type StyledStringValue = TextStyle | DecorationStyle | BaselineOffsetStyle | LetterSpacingStyle | TextShadowStyle | GestureStyle | ImageAttachment | ParagraphStyle | LineHeightStyle | CustomSpan;  差异内容：TextStyle | DecorationStyle | BaselineOffsetStyle | LetterSpacingStyle | TextShadowStyle | GestureStyle | ImageAttachment | ParagraphStyle | LineHeightStyle | CustomSpan | 类名：global；  API声明：declare type StyledStringValue = TextStyle | DecorationStyle | BaselineOffsetStyle | LetterSpacingStyle | TextShadowStyle | GestureStyle | ImageAttachment | ParagraphStyle | LineHeightStyle | CustomSpan | UserDataSpan;  差异内容：TextStyle | DecorationStyle | BaselineOffsetStyle | LetterSpacingStyle | TextShadowStyle | GestureStyle | ImageAttachment | ParagraphStyle | LineHeightStyle | CustomSpan | UserDataSpan | component/styled\_string.d.ts |
| 自定义类型变更 | 类名：global；  API声明：declare type EditableTextOnChangeCallback = (value: string, previewRange?: TextRange) => void;  差异内容：value: string, previewRange?: TextRange | 类名：global；  API声明：declare type EditableTextOnChangeCallback = (value: string, previewText?: PreviewText) => void;  差异内容：value: string, previewText?: PreviewText | component/text\_common.d.ts |
| 新增API | NA | 类名：AttributeUpdater；  API声明：onComponentChanged(component: T): void;  差异内容：onComponentChanged(component: T): void; | api/arkui/AttributeUpdater.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface IDataSourcePrefetching  差异内容： export interface IDataSourcePrefetching | api/@ohos.arkui.Prefetcher.d.ts |
| 新增API | NA | 类名：IDataSourcePrefetching；  API声明：prefetch(index: number): Promise<void> | void;  差异内容：prefetch(index: number): Promise<void> | void; | api/@ohos.arkui.Prefetcher.d.ts |
| 新增API | NA | 类名：IDataSourcePrefetching；  API声明：cancel?(index: number): Promise<void> | void;  差异内容：cancel?(index: number): Promise<void> | void; | api/@ohos.arkui.Prefetcher.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface IPrefetcher  差异内容： export interface IPrefetcher | api/@ohos.arkui.Prefetcher.d.ts |
| 新增API | NA | 类名：IPrefetcher；  API声明：setDataSource(dataSource: IDataSourcePrefetching): void;  差异内容：setDataSource(dataSource: IDataSourcePrefetching): void; | api/@ohos.arkui.Prefetcher.d.ts |
| 新增API | NA | 类名：IPrefetcher；  API声明：visibleAreaChanged(minVisible: number, maxVisible: number): void;  差异内容：visibleAreaChanged(minVisible: number, maxVisible: number): void; | api/@ohos.arkui.Prefetcher.d.ts |
| 新增API | NA | 类名：global；  API声明： export class BasicPrefetcher  差异内容： export class BasicPrefetcher | api/@ohos.arkui.Prefetcher.d.ts |
| 新增API | NA | 类名：BasicPrefetcher；  API声明：setDataSource(dataSource: IDataSourcePrefetching): void;  差异内容：setDataSource(dataSource: IDataSourcePrefetching): void; | api/@ohos.arkui.Prefetcher.d.ts |
| 新增API | NA | 类名：BasicPrefetcher；  API声明：visibleAreaChanged(minVisible: number, maxVisible: number): void;  差异内容：visibleAreaChanged(minVisible: number, maxVisible: number): void; | api/@ohos.arkui.Prefetcher.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare struct AtomicServiceNavigation  差异内容： export declare struct AtomicServiceNavigation | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：AtomicServiceNavigation；  API声明：@State  navPathStack?: NavPathStack;  差异内容：@State  navPathStack?: NavPathStack; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：AtomicServiceNavigation；  API声明：@BuilderParam  navigationContent?: Callback<void>;  差异内容：@BuilderParam  navigationContent?: Callback<void>; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：AtomicServiceNavigation；  API声明：@Prop  title?: ResourceStr;  差异内容：@Prop  title?: ResourceStr; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：AtomicServiceNavigation；  API声明：@Prop  titleOptions?: TitleOptions;  差异内容：@Prop  titleOptions?: TitleOptions; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：AtomicServiceNavigation；  API声明：@Prop  hideTitleBar?: boolean;  差异内容：@Prop  hideTitleBar?: boolean; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：AtomicServiceNavigation；  API声明：@Prop  navBarWidth?: Length;  差异内容：@Prop  navBarWidth?: Length; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：AtomicServiceNavigation；  API声明：@Prop  mode?: NavigationMode;  差异内容：@Prop  mode?: NavigationMode; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：AtomicServiceNavigation；  API声明：@BuilderParam  navDestinationBuilder?: NavDestinationBuilder;  差异内容：@BuilderParam  navDestinationBuilder?: NavDestinationBuilder; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：AtomicServiceNavigation；  API声明：@Prop  navBarWidthRange?: [  Dimension,  Dimension  ];  差异内容：@Prop  navBarWidthRange?: [  Dimension,  Dimension  ]; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：AtomicServiceNavigation；  API声明：@Prop  minContentWidth?: Dimension;  差异内容：@Prop  minContentWidth?: Dimension; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：AtomicServiceNavigation；  API声明：stateChangeCallback?: Callback<boolean>;  差异内容：stateChangeCallback?: Callback<boolean>; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：AtomicServiceNavigation；  API声明：modeChangeCallback?: Callback<NavigationMode>;  差异内容：modeChangeCallback?: Callback<NavigationMode>; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface TitleOptions  差异内容： export interface TitleOptions | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：TitleOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：TitleOptions；  API声明：isBlurEnabled?: boolean;  差异内容：isBlurEnabled?: boolean; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：TitleOptions；  API声明：barStyle?: BarStyle;  差异内容：barStyle?: BarStyle; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：global；  API声明：export type NavDestinationBuilder = (name: string, param?: Object) => void;  差异内容：export type NavDestinationBuilder = (name: string, param?: Object) => void; | api/@ohos.atomicservice.AtomicServiceNavigation.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct AtomicServiceTabs  差异内容： export declare struct AtomicServiceTabs | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：AtomicServiceTabs；  API声明：@BuilderParam  tabContents?: [  TabContentBuilder?,  TabContentBuilder?,  TabContentBuilder?,  TabContentBuilder?,  TabContentBuilder?  ];  差异内容：@BuilderParam  tabContents?: [  TabContentBuilder?,  TabContentBuilder?,  TabContentBuilder?,  TabContentBuilder?,  TabContentBuilder?  ]; | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：AtomicServiceTabs；  API声明：@Prop  tabBarOptionsArray: [  TabBarOptions,  TabBarOptions,  TabBarOptions?,  TabBarOptions?,  TabBarOptions?  ];  差异内容：@Prop  tabBarOptionsArray: [  TabBarOptions,  TabBarOptions,  TabBarOptions?,  TabBarOptions?,  TabBarOptions?  ]; | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：AtomicServiceTabs；  API声明：@Prop  tabBarPosition?: TabBarPosition;  差异内容：@Prop  tabBarPosition?: TabBarPosition; | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：AtomicServiceTabs；  API声明：@Prop  barBackgroundColor?: ResourceColor;  差异内容：@Prop  barBackgroundColor?: ResourceColor; | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：AtomicServiceTabs；  API声明：@Prop  index?: number;  差异内容：@Prop  index?: number; | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：AtomicServiceTabs；  API声明：@Prop  barOverlap?: boolean;  差异内容：@Prop  barOverlap?: boolean; | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：AtomicServiceTabs；  API声明：controller?: TabsController;  差异内容：controller?: TabsController; | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：AtomicServiceTabs；  API声明：onChange?: Callback<number>;  差异内容：onChange?: Callback<number>; | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：AtomicServiceTabs；  API声明：onTabBarClick?: Callback<number>;  差异内容：onTabBarClick?: Callback<number>; | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：AtomicServiceTabs；  API声明：onContentWillChange?: OnContentWillChangeCallback;  差异内容：onContentWillChange?: OnContentWillChangeCallback; | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class TabBarOptions  差异内容： export declare class TabBarOptions | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum TabBarPosition  差异内容： export declare enum TabBarPosition | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：TabBarPosition；  API声明：LEFT = 0  差异内容：LEFT = 0 | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：TabBarPosition；  API声明：BOTTOM = 1  差异内容：BOTTOM = 1 | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：global；  API声明：export type TabContentBuilder = () => void;  差异内容：export type TabContentBuilder = () => void; | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：global；  API声明：export type OnContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean;  差异内容：export type OnContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean; | api/@ohos.atomicservice.AtomicServiceTabs.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct AtomicServiceWeb  差异内容： export declare struct AtomicServiceWeb | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWeb；  API声明：src: ResourceStr;  差异内容：src: ResourceStr; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWeb；  API声明：navPathStack?: NavPathStack;  差异内容：navPathStack?: NavPathStack; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWeb；  API声明：onMessage?: Callback<OnMessageEvent>;  差异内容：onMessage?: Callback<OnMessageEvent>; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWeb；  API声明：onErrorReceive?: Callback<OnErrorReceiveEvent>;  差异内容：onErrorReceive?: Callback<OnErrorReceiveEvent>; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWeb；  API声明：onHttpErrorReceive?: Callback<OnHttpErrorReceiveEvent>;  差异内容：onHttpErrorReceive?: Callback<OnHttpErrorReceiveEvent>; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWeb；  API声明：onPageBegin?: Callback<OnPageBeginEvent>;  差异内容：onPageBegin?: Callback<OnPageBeginEvent>; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWeb；  API声明：onPageEnd?: Callback<OnPageEndEvent>;  差异内容：onPageEnd?: Callback<OnPageEndEvent>; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare interface OnMessageEvent  差异内容： export declare interface OnMessageEvent | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：OnMessageEvent；  API声明：data: object[];  差异内容：data: object[]; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare interface OnErrorReceiveEvent  差异内容： export declare interface OnErrorReceiveEvent | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：OnErrorReceiveEvent；  API声明：request: WebResourceRequest;  差异内容：request: WebResourceRequest; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：OnErrorReceiveEvent；  API声明：error: WebResourceError;  差异内容：error: WebResourceError; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare interface OnHttpErrorReceiveEvent  差异内容： export declare interface OnHttpErrorReceiveEvent | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：OnHttpErrorReceiveEvent；  API声明：request: WebResourceRequest;  差异内容：request: WebResourceRequest; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：OnHttpErrorReceiveEvent；  API声明：response: WebResourceResponse;  差异内容：response: WebResourceResponse; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare interface OnPageBeginEvent  差异内容： export declare interface OnPageBeginEvent | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：OnPageBeginEvent；  API声明：url: string;  差异内容：url: string; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare interface OnPageEndEvent  差异内容： export declare interface OnPageEndEvent | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：OnPageEndEvent；  API声明：url: string;  差异内容：url: string; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum IconStyle  差异内容： export declare enum IconStyle | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：IconStyle；  API声明：DARK = 0  差异内容：DARK = 0 | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：IconStyle；  API声明：LIGHT = 1  差异内容：LIGHT = 1 | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum TitlePosition  差异内容： export declare enum TitlePosition | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：TitlePosition；  API声明：TOP = 0  差异内容：TOP = 0 | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：TitlePosition；  API声明：BOTTOM = 1  差异内容：BOTTOM = 1 | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum BottomOffset  差异内容： export declare enum BottomOffset | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：BottomOffset；  API声明：OFFSET\_FOR\_BAR = 0  差异内容：OFFSET\_FOR\_BAR = 0 | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：BottomOffset；  API声明：OFFSET\_FOR\_NONE = 1  差异内容：OFFSET\_FOR\_NONE = 1 | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare interface DialogOptions  差异内容： export declare interface DialogOptions | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：DialogOptions；  API声明：uiContext: UIContext;  差异内容：uiContext: UIContext; | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：DialogOptions；  API声明：bottomOffsetType?: BottomOffset;  差异内容：bottomOffsetType?: BottomOffset; | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：DialogOptions；  API声明：title?: ResourceStr;  差异内容：title?: ResourceStr; | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：DialogOptions；  API声明：subtitle?: ResourceStr;  差异内容：subtitle?: ResourceStr; | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：DialogOptions；  API声明：titleColor?: ResourceStr | Color;  差异内容：titleColor?: ResourceStr | Color; | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：DialogOptions；  API声明：subtitleColor?: ResourceStr | Color;  差异内容：subtitleColor?: ResourceStr | Color; | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：DialogOptions；  API声明：backgroundImage?: Resource;  差异内容：backgroundImage?: Resource; | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：DialogOptions；  API声明：foregroundImage?: Resource;  差异内容：foregroundImage?: Resource; | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：DialogOptions；  API声明：iconStyle?: IconStyle;  差异内容：iconStyle?: IconStyle; | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：DialogOptions；  API声明：titlePosition?: TitlePosition;  差异内容：titlePosition?: TitlePosition; | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：DialogOptions；  API声明：onDialogClick?: Callback<void>;  差异内容：onDialogClick?: Callback<void>; | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：DialogOptions；  API声明：onDialogClose?: Callback<void>;  差异内容：onDialogClose?: Callback<void>; | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class InterstitialDialogAction  差异内容： export declare class InterstitialDialogAction | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：InterstitialDialogAction；  API声明：openDialog(): void;  差异内容：openDialog(): void; | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：InterstitialDialogAction；  API声明：closeDialog(): void;  差异内容：closeDialog(): void; | api/@ohos.atomicservice.InterstitialDialogAction.d.ets |
| 新增API | NA | 类名：global；  API声明： declare enum ImageAnalyzerType  差异内容： declare enum ImageAnalyzerType | component/image\_common.d.ts |
| 新增API | NA | 类名：ImageAnalyzerType；  API声明：SUBJECT = 0  差异内容：SUBJECT = 0 | component/image\_common.d.ts |
| 新增API | NA | 类名：ImageAnalyzerType；  API声明：TEXT  差异内容：TEXT | component/image\_common.d.ts |
| 新增API | NA | 类名：ImageAnalyzerType；  API声明：OBJECT\_LOOKUP  差异内容：OBJECT\_LOOKUP | component/image\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ImageAnalyzerController  差异内容： declare class ImageAnalyzerController | component/image\_common.d.ts |
| 新增API | NA | 类名：ImageAnalyzerController；  API声明：getImageAnalyzerSupportTypes(): ImageAnalyzerType[];  差异内容：getImageAnalyzerSupportTypes(): ImageAnalyzerType[]; | component/image\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ImageAnalyzerConfig  差异内容： declare interface ImageAnalyzerConfig | component/image\_common.d.ts |
| 新增API | NA | 类名：ImageAnalyzerConfig；  API声明：types: ImageAnalyzerType[];  差异内容：types: ImageAnalyzerType[]; | component/image\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ImageAIOptions  差异内容： declare interface ImageAIOptions | component/image\_common.d.ts |
| 新增API | NA | 类名：ImageAIOptions；  API声明：types?: ImageAnalyzerType[];  差异内容：types?: ImageAnalyzerType[]; | component/image\_common.d.ts |
| 新增API | NA | 类名：ImageAIOptions；  API声明：aiController?: ImageAnalyzerController;  差异内容：aiController?: ImageAnalyzerController; | component/image\_common.d.ts |
| 新增API | NA | 类名：componentSnapshot；  API声明： interface SnapshotOptions  差异内容： interface SnapshotOptions | api/@ohos.arkui.componentSnapshot.d.ts |
| 新增API | NA | 类名：SnapshotOptions；  API声明：scale?: number;  差异内容：scale?: number; | api/@ohos.arkui.componentSnapshot.d.ts |
| 新增API | NA | 类名：SnapshotOptions；  API声明：waitUntilRenderFinished?: boolean;  差异内容：waitUntilRenderFinished?: boolean; | api/@ohos.arkui.componentSnapshot.d.ts |
| 新增API | NA | 类名：PromptAction；  API声明：openCustomDialog(options: promptAction.CustomDialogOptions): Promise<number>;  差异内容：openCustomDialog(options: promptAction.CustomDialogOptions): Promise<number>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：PromptAction；  API声明：closeCustomDialog(dialogId: number): void;  差异内容：closeCustomDialog(dialogId: number): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：openBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>, sheetOptions?: SheetOptions, targetId?: number): Promise<void>;  差异内容：openBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>, sheetOptions?: SheetOptions, targetId?: number): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：updateBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>, sheetOptions: SheetOptions, partialUpdate?: boolean): Promise<void>;  差异内容：updateBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>, sheetOptions: SheetOptions, partialUpdate?: boolean): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：closeBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>): Promise<void>;  差异内容：closeBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：PiPConfiguration；  API声明：customUIController?: NodeController;  差异内容：customUIController?: NodeController; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：VideoCallControlGroup；  API声明：MUTE\_SWITCH = 204  差异内容：MUTE\_SWITCH = 204 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：VideoMeetingControlGroup；  API声明：MICROPHONE\_SWITCH = 304  差异内容：MICROPHONE\_SWITCH = 304 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明： enum VideoLiveControlGroup  差异内容： enum VideoLiveControlGroup | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：VideoLiveControlGroup；  API声明：VIDEO\_PLAY\_PAUSE = 401  差异内容：VIDEO\_PLAY\_PAUSE = 401 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：VideoLiveControlGroup；  API声明：MUTE\_SWITCH = 402  差异内容：MUTE\_SWITCH = 402 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明： enum PiPControlStatus  差异内容： enum PiPControlStatus | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPControlStatus；  API声明：PLAY = 1  差异内容：PLAY = 1 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPControlStatus；  API声明：PAUSE = 0  差异内容：PAUSE = 0 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPControlStatus；  API声明：OPEN = 1  差异内容：OPEN = 1 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPControlStatus；  API声明：CLOSE = 0  差异内容：CLOSE = 0 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明： enum PiPControlType  差异内容： enum PiPControlType | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPControlType；  API声明：VIDEO\_PLAY\_PAUSE = 0  差异内容：VIDEO\_PLAY\_PAUSE = 0 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPControlType；  API声明：VIDEO\_PREVIOUS = 1  差异内容：VIDEO\_PREVIOUS = 1 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPControlType；  API声明：VIDEO\_NEXT = 2  差异内容：VIDEO\_NEXT = 2 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPControlType；  API声明：FAST\_FORWARD = 3  差异内容：FAST\_FORWARD = 3 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPControlType；  API声明：FAST\_BACKWARD = 4  差异内容：FAST\_BACKWARD = 4 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPControlType；  API声明：HANG\_UP\_BUTTON = 5  差异内容：HANG\_UP\_BUTTON = 5 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPControlType；  API声明：MICROPHONE\_SWITCH = 6  差异内容：MICROPHONE\_SWITCH = 6 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPControlType；  API声明：CAMERA\_SWITCH = 7  差异内容：CAMERA\_SWITCH = 7 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPControlType；  API声明：MUTE\_SWITCH = 8  差异内容：MUTE\_SWITCH = 8 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明： interface ControlEventParam  差异内容： interface ControlEventParam | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：ControlEventParam；  API声明：controlType: PiPControlType;  差异内容：controlType: PiPControlType; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：ControlEventParam；  API声明：status?: PiPControlStatus;  差异内容：status?: PiPControlStatus; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPController；  API声明：updatePiPControlStatus(controlType: PiPControlType, status: PiPControlStatus): void;  差异内容：updatePiPControlStatus(controlType: PiPControlType, status: PiPControlStatus): void; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPController；  API声明：setPiPControlEnabled(controlType: PiPControlType, enabled: boolean): void;  差异内容：setPiPControlEnabled(controlType: PiPControlType, enabled: boolean): void; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPController；  API声明：on(type: 'controlEvent', callback: Callback<ControlEventParam>): void;  差异内容：on(type: 'controlEvent', callback: Callback<ControlEventParam>): void; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPController；  API声明：off(type: 'controlEvent', callback?: Callback<ControlEventParam>): void;  差异内容：off(type: 'controlEvent', callback?: Callback<ControlEventParam>): void; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：window；  API声明： enum MaximizePresentation  差异内容： enum MaximizePresentation | api/@ohos.window.d.ts |
| 新增API | NA | 类名：MaximizePresentation；  API声明：FOLLOW\_APP\_IMMERSIVE\_SETTING = 0  差异内容：FOLLOW\_APP\_IMMERSIVE\_SETTING = 0 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：MaximizePresentation；  API声明：EXIT\_IMMERSIVE = 1  差异内容：EXIT\_IMMERSIVE = 1 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：MaximizePresentation；  API声明：ENTER\_IMMERSIVE = 2  差异内容：ENTER\_IMMERSIVE = 2 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'ListItemGroup'): ListItemGroup;  差异内容：function createNode(context: UIContext, nodeType: 'ListItemGroup'): ListItemGroup; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'WaterFlow'): WaterFlow;  差异内容：function createNode(context: UIContext, nodeType: 'WaterFlow'): WaterFlow; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'FlowItem'): FlowItem;  差异内容：function createNode(context: UIContext, nodeType: 'FlowItem'): FlowItem; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'XComponent'): XComponent;  差异内容：function createNode(context: UIContext, nodeType: 'XComponent'): XComponent; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type ListItemGroup = TypedFrameNode<ListItemGroupInterface, ListItemGroupAttribute>;  差异内容：type ListItemGroup = TypedFrameNode<ListItemGroupInterface, ListItemGroupAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type WaterFlow = TypedFrameNode<WaterFlowInterface, WaterFlowAttribute>;  差异内容：type WaterFlow = TypedFrameNode<WaterFlowInterface, WaterFlowAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type FlowItem = TypedFrameNode<FlowItemInterface, FlowItemAttribute>;  差异内容：type FlowItem = TypedFrameNode<FlowItemInterface, FlowItemAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type XComponent = TypedFrameNode<XComponentInterface, XComponentAttribute>;  差异内容：type XComponent = TypedFrameNode<XComponentInterface, XComponentAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class NodeAdapter  差异内容： declare class NodeAdapter | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：NodeAdapter；  API声明：dispose(): void;  差异内容：dispose(): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：NodeAdapter；  API声明：reloadAllItems(): void;  差异内容：reloadAllItems(): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：NodeAdapter；  API声明：reloadItem(start: number, count: number): void;  差异内容：reloadItem(start: number, count: number): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：NodeAdapter；  API声明：removeItem(start: number, count: number): void;  差异内容：removeItem(start: number, count: number): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：NodeAdapter；  API声明：insertItem(start: number, count: number): void;  差异内容：insertItem(start: number, count: number): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：NodeAdapter；  API声明：moveItem(from: number, to: number): void;  差异内容：moveItem(from: number, to: number): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：NodeAdapter；  API声明：getAllAvailableItems(): Array<FrameNode>;  差异内容：getAllAvailableItems(): Array<FrameNode>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：NodeAdapter；  API声明：onAttachToNode?(target: FrameNode): void;  差异内容：onAttachToNode?(target: FrameNode): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：NodeAdapter；  API声明：onDetachFromNode?(): void;  差异内容：onDetachFromNode?(): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：NodeAdapter；  API声明：onGetChildId?(index: number): number;  差异内容：onGetChildId?(index: number): number; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：NodeAdapter；  API声明：onCreateChild?(index: number): FrameNode;  差异内容：onCreateChild?(index: number): FrameNode; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：NodeAdapter；  API声明：onDisposeChild?(id: number, node: FrameNode): void;  差异内容：onDisposeChild?(id: number, node: FrameNode): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：NodeAdapter；  API声明：onUpdateChild?(id: number, node: FrameNode): void;  差异内容：onUpdateChild?(id: number, node: FrameNode): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：NodeAdapter；  API声明：static attachNodeAdapter(adapter: NodeAdapter, node: FrameNode): boolean;  差异内容：static attachNodeAdapter(adapter: NodeAdapter, node: FrameNode): boolean; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：NodeAdapter；  API声明：static detachNodeAdapter(node: FrameNode): void;  差异内容：static detachNodeAdapter(node: FrameNode): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：transition(effect: TransitionEffect, onFinish: Optional<TransitionFinishCallback>): T;  差异内容：transition(effect: TransitionEffect, onFinish: Optional<TransitionFinishCallback>): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：accessibilityText(text: Resource): T;  差异内容：accessibilityText(text: Resource): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：accessibilityDescription(description: Resource): T;  差异内容：accessibilityDescription(description: Resource): T; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const LocalBuilder: MethodDecorator;  差异内容：declare const LocalBuilder: MethodDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type TransitionFinishCallback = (transitionIn: boolean) => void;  差异内容：declare type TransitionFinishCallback = (transitionIn: boolean) => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface OverlayOptions  差异内容： declare interface OverlayOptions | component/common.d.ts |
| 新增API | NA | 类名：OverlayOptions；  API声明：align?: Alignment;  差异内容：align?: Alignment; | component/common.d.ts |
| 新增API | NA | 类名：OverlayOptions；  API声明：offset?: OverlayOffset;  差异内容：offset?: OverlayOffset; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface OverlayOffset  差异内容： declare interface OverlayOffset | component/common.d.ts |
| 新增API | NA | 类名：OverlayOffset；  API声明：x?: number;  差异内容：x?: number; | component/common.d.ts |
| 新增API | NA | 类名：OverlayOffset；  API声明：y?: number;  差异内容：y?: number; | component/common.d.ts |
| 新增API | NA | 类名：ImageFit；  API声明：TOP\_START = 7  差异内容：TOP\_START = 7 | component/enums.d.ts |
| 新增API | NA | 类名：ImageFit；  API声明：TOP = 8  差异内容：TOP = 8 | component/enums.d.ts |
| 新增API | NA | 类名：ImageFit；  API声明：TOP\_END = 9  差异内容：TOP\_END = 9 | component/enums.d.ts |
| 新增API | NA | 类名：ImageFit；  API声明：START = 10  差异内容：START = 10 | component/enums.d.ts |
| 新增API | NA | 类名：ImageFit；  API声明：CENTER = 11  差异内容：CENTER = 11 | component/enums.d.ts |
| 新增API | NA | 类名：ImageFit；  API声明：END = 12  差异内容：END = 12 | component/enums.d.ts |
| 新增API | NA | 类名：ImageFit；  API声明：BOTTOM\_START = 13  差异内容：BOTTOM\_START = 13 | component/enums.d.ts |
| 新增API | NA | 类名：ImageFit；  API声明：BOTTOM = 14  差异内容：BOTTOM = 14 | component/enums.d.ts |
| 新增API | NA | 类名：ImageFit；  API声明：BOTTOM\_END = 15  差异内容：BOTTOM\_END = 15 | component/enums.d.ts |
| 新增API | NA | 类名：RichEditorBaseController；  API声明：getPreviewText(): PreviewText;  差异内容：getPreviewText(): PreviewText; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：editMenuOptions(editMenu: EditMenuOptions): RichEditorAttribute;  差异内容：editMenuOptions(editMenu: EditMenuOptions): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type PasteEventCallback = (event?: PasteEvent) => void;  差异内容：declare type PasteEventCallback = (event?: PasteEvent) => void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：StyledStringKey；  API声明：USER\_DATA = 500  差异内容：USER\_DATA = 500 | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare abstract class UserDataSpan  差异内容： declare abstract class UserDataSpan | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextDataDetectorType；  API声明：DATE\_TIME = 4  差异内容：DATE\_TIME = 4 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextEditControllerEx；  API声明：getPreviewText?(): PreviewText;  差异内容：getPreviewText?(): PreviewText; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface PreviewText  差异内容： declare interface PreviewText | component/text\_common.d.ts |
| 新增API | NA | 类名：PreviewText；  API声明：offset: number;  差异内容：offset: number; | component/text\_common.d.ts |
| 新增API | NA | 类名：PreviewText；  API声明：value: string;  差异内容：value: string; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class TextMenuItemId  差异内容： declare class TextMenuItemId | component/text\_common.d.ts |
| 新增API | NA | 类名：TextMenuItemId；  API声明：static of(id: ResourceStr): TextMenuItemId;  差异内容：static of(id: ResourceStr): TextMenuItemId; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextMenuItemId；  API声明：equals(id: TextMenuItemId): boolean;  差异内容：equals(id: TextMenuItemId): boolean; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextMenuItemId；  API声明：static readonly CUT: TextMenuItemId;  差异内容：static readonly CUT: TextMenuItemId; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextMenuItemId；  API声明：static readonly COPY: TextMenuItemId;  差异内容：static readonly COPY: TextMenuItemId; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextMenuItemId；  API声明：static readonly PASTE: TextMenuItemId;  差异内容：static readonly PASTE: TextMenuItemId; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextMenuItemId；  API声明：static readonly SELECT\_ALL: TextMenuItemId;  差异内容：static readonly SELECT\_ALL: TextMenuItemId; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextMenuItemId；  API声明：static readonly COLLABORATION\_SERVICE: TextMenuItemId;  差异内容：static readonly COLLABORATION\_SERVICE: TextMenuItemId; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextMenuItemId；  API声明：static readonly CAMERA\_INPUT: TextMenuItemId;  差异内容：static readonly CAMERA\_INPUT: TextMenuItemId; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TextMenuItem  差异内容： declare interface TextMenuItem | component/text\_common.d.ts |
| 新增API | NA | 类名：TextMenuItem；  API声明：content: ResourceStr;  差异内容：content: ResourceStr; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextMenuItem；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextMenuItem；  API声明：id: TextMenuItemId;  差异内容：id: TextMenuItemId; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface EditMenuOptions  差异内容： declare interface EditMenuOptions | component/text\_common.d.ts |
| 新增API | NA | 类名：EditMenuOptions；  API声明：onCreateMenu(menuItems: Array<TextMenuItem>): Array<TextMenuItem>;  差异内容：onCreateMenu(menuItems: Array<TextMenuItem>): Array<TextMenuItem>; | component/text\_common.d.ts |
| 新增API | NA | 类名：EditMenuOptions；  API声明：onMenuItemClick(menuItem: TextMenuItem, range: TextRange): boolean;  差异内容：onMenuItemClick(menuItem: TextMenuItem, range: TextRange): boolean; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： interface DecorationStyleResult  差异内容： interface DecorationStyleResult | component/text\_common.d.ts |
| 新增API | NA | 类名：DecorationStyleResult；  API声明：type: TextDecorationType;  差异内容：type: TextDecorationType; | component/text\_common.d.ts |
| 新增API | NA | 类名：DecorationStyleResult；  API声明：color: ResourceColor;  差异内容：color: ResourceColor; | component/text\_common.d.ts |
| 新增API | NA | 类名：DecorationStyleResult；  API声明：style?: TextDecorationStyle;  差异内容：style?: TextDecorationStyle; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare function loadNativeModule(moduleName: string): Object;  差异内容：export declare function loadNativeModule(moduleName: string): Object; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：CustomContentDialog；  API声明：localizedContentAreaPadding?: LocalizedPadding;  差异内容：localizedContentAreaPadding?: LocalizedPadding; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：BuilderNode；  API声明：updateConfiguration(): void;  差异内容：updateConfiguration(): void; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：ComponentContent；  API声明：updateConfiguration(): void;  差异内容：updateConfiguration(): void; | api/arkui/ComponentContent.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ShapeClip  差异内容： export declare class ShapeClip | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ShapeClip；  API声明：setRectShape(rect: Rect): void;  差异内容：setRectShape(rect: Rect): void; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ShapeClip；  API声明：setRoundRectShape(roundRect: RoundRect): void;  差异内容：setRoundRectShape(roundRect: RoundRect): void; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ShapeClip；  API声明：setCircleShape(circle: Circle): void;  差异内容：setCircleShape(circle: Circle): void; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ShapeClip；  API声明：setOvalShape(oval: Rect): void;  差异内容：setOvalShape(oval: Rect): void; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ShapeClip；  API声明：setCommandPath(path: CommandPath): void;  差异内容：setCommandPath(path: CommandPath): void; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：LaunchMode；  API声明：NEW\_INSTANCE = 3  差异内容：NEW\_INSTANCE = 3 | component/navigation.d.ts |
| 新增API | NA | 类名：SearchType；  API声明：URL = 13  差异内容：URL = 13 | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：editMenuOptions(editMenu: EditMenuOptions): SearchAttribute;  差异内容：editMenuOptions(editMenu: EditMenuOptions): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：edgeEffect(edgeEffect: Optional<EdgeEffect>): TabsAttribute;  差异内容：edgeEffect(edgeEffect: Optional<EdgeEffect>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：editMenuOptions(editMenu: EditMenuOptions): TextAttribute;  差异内容：editMenuOptions(editMenu: EditMenuOptions): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAreaType；  API声明：URL = 13  差异内容：URL = 13 | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：editMenuOptions(editMenu: EditMenuOptions): TextAreaAttribute;  差异内容：editMenuOptions(editMenu: EditMenuOptions): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextClockAttribute；  API声明：dateTimeOptions(dateTimeOptions: Optional<DateTimeOptions>): TextClockAttribute;  差异内容：dateTimeOptions(dateTimeOptions: Optional<DateTimeOptions>): TextClockAttribute; | component/text\_clock.d.ts |
| 新增API | NA | 类名：InputType；  API声明：URL = 13  差异内容：URL = 13 | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：editMenuOptions(editMenu: EditMenuOptions): TextInputAttribute;  差异内容：editMenuOptions(editMenu: EditMenuOptions): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TimePickerAttribute；  API声明：enableHapticFeedback(enable: boolean): TimePickerAttribute;  差异内容：enableHapticFeedback(enable: boolean): TimePickerAttribute; | component/time\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface XComponentOptions  差异内容： declare interface XComponentOptions | component/xcomponent.d.ts |
| 新增API | NA | 类名：XComponentOptions；  API声明：type: XComponentType;  差异内容：type: XComponentType; | component/xcomponent.d.ts |
| 新增API | NA | 类名：XComponentOptions；  API声明：controller: XComponentController;  差异内容：controller: XComponentController; | component/xcomponent.d.ts |
| 新增API | NA | 类名：XComponentOptions；  API声明：imageAIOptions?: ImageAIOptions;  差异内容：imageAIOptions?: ImageAIOptions; | component/xcomponent.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class SymbolSpanModifier  差异内容： export declare class SymbolSpanModifier | api/arkui/SymbolSpanModifier.d.ts |
| 新增API | NA | 类名：SymbolSpanModifier；  API声明：applyNormalAttribute?(attribute: SymbolSpanAttribute): void;  差异内容：applyNormalAttribute?(attribute: SymbolSpanAttribute): void; | api/arkui/SymbolSpanModifier.d.ts |
| 新增API | NA | 类名：Window；  API声明：setDialogBackGestureEnabled(enabled: boolean): Promise<void>;  差异内容：setDialogBackGestureEnabled(enabled: boolean): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setImmersiveModeEnabledState(enabled: boolean): void;  差异内容：setImmersiveModeEnabledState(enabled: boolean): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：getImmersiveModeEnabledState(): boolean;  差异内容：getImmersiveModeEnabledState(): boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：BuilderNode；  API声明：build(builder: WrappedBuilder<Args>, arg: Object, options: BuildOptions): void;  差异内容：build(builder: WrappedBuilder<Args>, arg: Object, options: BuildOptions): void; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface BuildOptions  差异内容： export interface BuildOptions | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：BuildOptions；  API声明：nestingBuilderSupported?: boolean;  差异内容：nestingBuilderSupported?: boolean; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：global；  API声明： interface CancelButtonOptions  差异内容： interface CancelButtonOptions | component/search.d.ts |
| 新增API | NA | 类名：CancelButtonOptions；  API声明：style?: CancelButtonStyle;  差异内容：style?: CancelButtonStyle; | component/search.d.ts |
| 新增API | NA | 类名：CancelButtonOptions；  API声明：icon?: IconOptions;  差异内容：icon?: IconOptions; | component/search.d.ts |
| 新增API | NA | 类名：global；  API声明： interface CancelButtonSymbolOptions  差异内容： interface CancelButtonSymbolOptions | component/search.d.ts |
| 新增API | NA | 类名：CancelButtonSymbolOptions；  API声明：style?: CancelButtonStyle;  差异内容：style?: CancelButtonStyle; | component/search.d.ts |
| 新增API | NA | 类名：CancelButtonSymbolOptions；  API声明：icon?: SymbolGlyphModifier;  差异内容：icon?: SymbolGlyphModifier; | component/search.d.ts |
| 新增API | NA | 类名：display；  API声明：function getAllDisplayPhysicalResolution(): Promise<Array<DisplayPhysicalResolution>>;  差异内容：function getAllDisplayPhysicalResolution(): Promise<Array<DisplayPhysicalResolution>>; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明： interface DisplayPhysicalResolution  差异内容： interface DisplayPhysicalResolution | api/@ohos.display.d.ts |
| 新增API | NA | 类名：DisplayPhysicalResolution；  API声明：foldDisplayMode: FoldDisplayMode;  差异内容：foldDisplayMode: FoldDisplayMode; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：DisplayPhysicalResolution；  API声明：physicalWidth: number;  差异内容：physicalWidth: number; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：DisplayPhysicalResolution；  API声明：physicalHeight: number;  差异内容：physicalHeight: number; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：Display；  API声明：availableWidth: number;  差异内容：availableWidth: number; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：Display；  API声明：availableHeight: number;  差异内容：availableHeight: number; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：Display；  API声明：getAvailableArea(): Promise<Rect>;  差异内容：getAvailableArea(): Promise<Rect>; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：Display；  API声明：on(type: 'availableAreaChange', callback: Callback<Rect>): void;  差异内容：on(type: 'availableAreaChange', callback: Callback<Rect>): void; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：Display；  API声明：off(type: 'availableAreaChange', callback?: Callback<Rect>): void;  差异内容：off(type: 'availableAreaChange', callback?: Callback<Rect>): void; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：onDidIMEInput(callback: Callback<TextRange>): RichEditorAttribute;  差异内容：onDidIMEInput(callback: Callback<TextRange>): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：SymbolSpanAttribute；  API声明：attributeModifier(modifier: AttributeModifier<SymbolSpanAttribute>): SymbolSpanAttribute;  差异内容：attributeModifier(modifier: AttributeModifier<SymbolSpanAttribute>): SymbolSpanAttribute; | component/symbol\_span.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：minFontScale(scale: number | Resource): TextAttribute;  差异内容：minFontScale(scale: number | Resource): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：maxFontScale(scale: number | Resource): TextAttribute;  差异内容：maxFontScale(scale: number | Resource): TextAttribute; | component/text.d.ts |
| 删除API | 类名：global；  API声明： declare enum BlurStyleActivePolicy  差异内容： declare enum BlurStyleActivePolicy | NA | component/common.d.ts |
| 删除API | 类名：BlurStyleActivePolicy；  API声明：FOLLOWS\_WINDOW\_ACTIVE\_STATE = 0  差异内容：FOLLOWS\_WINDOW\_ACTIVE\_STATE = 0 | NA | component/common.d.ts |
| 删除API | 类名：BlurStyleActivePolicy；  API声明：ALWAYS\_ACTIVE = 1  差异内容：ALWAYS\_ACTIVE = 1 | NA | component/common.d.ts |
| 删除API | 类名：BlurStyleActivePolicy；  API声明：ALWAYS\_INACTIVE = 2  差异内容：ALWAYS\_INACTIVE = 2 | NA | component/common.d.ts |
| 删除API | 类名：global；  API声明： declare enum BlurType  差异内容： declare enum BlurType | NA | component/common.d.ts |
| 删除API | 类名：BlurType；  API声明：WITHIN\_WINDOW = 0  差异内容：WITHIN\_WINDOW = 0 | NA | component/common.d.ts |
| 删除API | 类名：BlurType；  API声明：BEHIND\_WINDOW = 1  差异内容：BEHIND\_WINDOW = 1 | NA | component/common.d.ts |
| 删除API | 类名：BackgroundBlurStyleOptions；  API声明：policy?: BlurStyleActivePolicy;  差异内容：policy?: BlurStyleActivePolicy; | NA | component/common.d.ts |
| 删除API | 类名：BackgroundBlurStyleOptions；  API声明：inactiveColor?: ResourceColor;  差异内容：inactiveColor?: ResourceColor; | NA | component/common.d.ts |
| 删除API | 类名：BackgroundBlurStyleOptions；  API声明：type?: BlurType;  差异内容：type?: BlurType; | NA | component/common.d.ts |
| 删除API | 类名：BackgroundEffectOptions；  API声明：policy?: BlurStyleActivePolicy;  差异内容：policy?: BlurStyleActivePolicy; | NA | component/common.d.ts |
| 删除API | 类名：BackgroundEffectOptions；  API声明：inactiveColor?: ResourceColor;  差异内容：inactiveColor?: ResourceColor; | NA | component/common.d.ts |
| 删除API | 类名：BackgroundEffectOptions；  API声明：type?: BlurType;  差异内容：type?: BlurType; | NA | component/common.d.ts |
| 删除API | 类名：ListAttribute；  API声明：fadingEdge(value: Optional<boolean>): ListAttribute;  差异内容：fadingEdge(value: Optional<boolean>): ListAttribute; | NA | component/list.d.ts |
| 起始版本有变化 | 类名：global；  API声明： declare namespace screenshot  差异内容：7 | 类名：global；  API声明： declare namespace screenshot  差异内容：12 | api/@ohos.screenshot.d.ts |
| 起始版本有变化 | 类名：screenshot；  API声明： interface Rect  差异内容：7 | 类名：screenshot；  API声明： interface Rect  差异内容：12 | api/@ohos.screenshot.d.ts |
| 起始版本有变化 | 类名：Rect；  API声明：left: number;  差异内容：7 | 类名：Rect；  API声明：left: number;  差异内容：12 | api/@ohos.screenshot.d.ts |
| 起始版本有变化 | 类名：Rect；  API声明：top: number;  差异内容：7 | 类名：Rect；  API声明：top: number;  差异内容：12 | api/@ohos.screenshot.d.ts |
| 起始版本有变化 | 类名：Rect；  API声明：width: number;  差异内容：7 | 类名：Rect；  API声明：width: number;  差异内容：12 | api/@ohos.screenshot.d.ts |
| 起始版本有变化 | 类名：Rect；  API声明：height: number;  差异内容：7 | 类名：Rect；  API声明：height: number;  差异内容：12 | api/@ohos.screenshot.d.ts |
