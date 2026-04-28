---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-5031
title: ArkUI
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta1引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:40+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:f42044ae53c4b526edb56dbb44352436435e88432e60036fd7d0d803c104e0f0
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：Window；  API声明：moveWindowToAsync(x: number, y: number, moveConfiguration?: MoveConfiguration): Promise<void>;  差异内容：moveWindowToAsync(x: number, y: number, moveConfiguration?: MoveConfiguration): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：moveWindowToGlobal(x: number, y: number, moveConfiguration?: MoveConfiguration): Promise<void>;  差异内容：moveWindowToGlobal(x: number, y: number, moveConfiguration?: MoveConfiguration): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明： interface WindowDensityInfo  差异内容： interface WindowDensityInfo | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowDensityInfo；  API声明：systemDensity: number;  差异内容：systemDensity: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowDensityInfo；  API声明：defaultDensity: number;  差异内容：defaultDensity: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowDensityInfo；  API声明：customDensity: number;  差异内容：customDensity: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：function getAllWindowLayoutInfo(displayId: number): Promise<Array<WindowLayoutInfo>>;  差异内容：function getAllWindowLayoutInfo(displayId: number): Promise<Array<WindowLayoutInfo>>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明： interface MoveConfiguration  差异内容： interface MoveConfiguration | api/@ohos.window.d.ts |
| 新增API | NA | 类名：MoveConfiguration；  API声明：displayId?: number;  差异内容：displayId?: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：getWindowDensityInfo(): WindowDensityInfo;  差异内容：getWindowDensityInfo(): WindowDensityInfo; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：on(type: 'systemDensityChange', callback: Callback<number>): void;  差异内容：on(type: 'systemDensityChange', callback: Callback<number>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：off(type: 'systemDensityChange', callback?: Callback<number>): void;  差异内容：off(type: 'systemDensityChange', callback?: Callback<number>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStage；  API声明：setCustomDensity(density: number): void;  差异内容：setCustomDensity(density: number): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明： interface WindowLayoutInfo  差异内容： interface WindowLayoutInfo | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowLayoutInfo；  API声明：windowRect: Rect;  差异内容：windowRect: Rect; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：NavigationAttribute；  API声明：enableModeChangeAnimation(isEnabled: Optional<boolean>): NavigationAttribute;  差异内容：enableModeChangeAnimation(isEnabled: Optional<boolean>): NavigationAttribute; | component/navigation.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：borderRadius(radius: Dimension | BorderRadiuses): T;  差异内容：borderRadius(radius: Dimension | BorderRadiuses): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：align(alignType: Alignment): T;  差异内容：align(alignType: Alignment): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：alignRules(alignRule: AlignRuleOption): T;  差异内容：alignRules(alignRule: AlignRuleOption): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：alignRules(alignRule: LocalizedAlignRuleOptions): T;  差异内容：alignRules(alignRule: LocalizedAlignRuleOptions): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：id(description: string): T;  差异内容：id(description: string): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：chainMode(direction: Axis, style: ChainStyle): T;  差异内容：chainMode(direction: Axis, style: ChainStyle): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明： interface PiPWindowSize  差异内容： interface PiPWindowSize | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindowSize；  API声明：width: number;  差异内容：width: number; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindowSize；  API声明：height: number;  差异内容：height: number; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindowSize；  API声明：scale: number;  差异内容：scale: number; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明： interface PiPWindowInfo  差异内容： interface PiPWindowInfo | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindowInfo；  API声明：windowId: number;  差异内容：windowId: number; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindowInfo；  API声明：size: PiPWindowSize;  差异内容：size: PiPWindowSize; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPController；  API声明：getPiPWindowInfo(): Promise<PiPWindowInfo>;  差异内容：getPiPWindowInfo(): Promise<PiPWindowInfo>; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface CrossLanguageOptions  差异内容： declare interface CrossLanguageOptions | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：CrossLanguageOptions；  API声明：attributeSetting?: boolean;  差异内容：attributeSetting?: boolean; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：setCrossLanguageOptions(options: CrossLanguageOptions): void;  差异内容：setCrossLanguageOptions(options: CrossLanguageOptions): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getCrossLanguageOptions(): CrossLanguageOptions;  差异内容：getCrossLanguageOptions(): CrossLanguageOptions; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function getAttribute(node: FrameNode, nodeType: 'Scroll'): ScrollAttribute | undefined;  差异内容：function getAttribute(node: FrameNode, nodeType: 'Scroll'): ScrollAttribute | undefined; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function bindController(node: FrameNode, controller: Scroller, nodeType: 'Scroll'): void;  差异内容：function bindController(node: FrameNode, controller: Scroller, nodeType: 'Scroll'): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：keyboardAppearance(appearance: Optional<KeyboardAppearance>): RichEditorAttribute;  差异内容：keyboardAppearance(appearance: Optional<KeyboardAppearance>): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：keyboardAppearance(appearance: Optional<KeyboardAppearance>): SearchAttribute;  差异内容：keyboardAppearance(appearance: Optional<KeyboardAppearance>): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：stopBackPress(isStopped: Optional<boolean>): SearchAttribute;  差异内容：stopBackPress(isStopped: Optional<boolean>): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SwiperAttribute；  API声明：onContentWillScroll(handler: ContentWillScrollCallback): SwiperAttribute;  差异内容：onContentWillScroll(handler: ContentWillScrollCallback): SwiperAttribute; | component/swiper.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SwiperContentWillScrollResult  差异内容： declare interface SwiperContentWillScrollResult | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperContentWillScrollResult；  API声明：currentIndex: number;  差异内容：currentIndex: number; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperContentWillScrollResult；  API声明：comingIndex: number;  差异内容：comingIndex: number; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperContentWillScrollResult；  API声明：offset: number;  差异内容：offset: number; | component/swiper.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean;  差异内容：declare type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean; | component/swiper.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：keyboardAppearance(appearance: Optional<KeyboardAppearance>): TextAreaAttribute;  差异内容：keyboardAppearance(appearance: Optional<KeyboardAppearance>): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：stopBackPress(isStopped: Optional<boolean>): TextAreaAttribute;  差异内容：stopBackPress(isStopped: Optional<boolean>): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum KeyboardAppearance  差异内容： declare enum KeyboardAppearance | component/text\_common.d.ts |
| 新增API | NA | 类名：KeyboardAppearance；  API声明：NONE\_IMMERSIVE = 0  差异内容：NONE\_IMMERSIVE = 0 | component/text\_common.d.ts |
| 新增API | NA | 类名：KeyboardAppearance；  API声明：IMMERSIVE = 1  差异内容：IMMERSIVE = 1 | component/text\_common.d.ts |
| 新增API | NA | 类名：KeyboardAppearance；  API声明：LIGHT\_IMMERSIVE = 2  差异内容：LIGHT\_IMMERSIVE = 2 | component/text\_common.d.ts |
| 新增API | NA | 类名：KeyboardAppearance；  API声明：DARK\_IMMERSIVE = 3  差异内容：DARK\_IMMERSIVE = 3 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：keyboardAppearance(appearance: Optional<KeyboardAppearance>): TextInputAttribute;  差异内容：keyboardAppearance(appearance: Optional<KeyboardAppearance>): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：stopBackPress(isStopped: Optional<boolean>): TextInputAttribute;  差异内容：stopBackPress(isStopped: Optional<boolean>): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：VideoAttribute；  API声明：enableShortcutKey(enabled: boolean): VideoAttribute;  差异内容：enableShortcutKey(enabled: boolean): VideoAttribute; | component/video.d.ts |
