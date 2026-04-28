---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-b060
title: ArkUI
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta5引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:25+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:14bba3405ad35472b28a0d81519fbaabf3d99557e56cc053d2f24dd8050948e7
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API卡片权限变更 | 类名：CommonMethod；  API声明：clip(value: boolean): T;  差异内容：NA | 类名：CommonMethod；  API声明：clip(value: boolean): T;  差异内容：form | component/common.d.ts |
| API卡片权限变更 | 类名：CommonMethod；  API声明：clipShape(value: CircleShape | EllipseShape | PathShape | RectShape): T;  差异内容：NA | 类名：CommonMethod；  API声明：clipShape(value: CircleShape | EllipseShape | PathShape | RectShape): T;  差异内容：form | component/common.d.ts |
| API卡片权限变更 | 类名：CommonMethod；  API声明：maskShape(value: CircleShape | EllipseShape | PathShape | RectShape): T;  差异内容：NA | 类名：CommonMethod；  API声明：maskShape(value: CircleShape | EllipseShape | PathShape | RectShape): T;  差异内容：form | component/common.d.ts |
| 错误码变更 | 类名：FrameNode；  API声明：addComponentContent<T>(content: ComponentContent<T>): void;  差异内容：NA | 类名：FrameNode；  API声明：addComponentContent<T>(content: ComponentContent<T>): void;  差异内容：100021 | api/arkui/FrameNode.d.ts |
| 错误码变更 | 类名：Window；  API声明：setWindowMask(windowMask: Array<Array<number>>): Promise<void>;  差异内容：1300002,1300003,401,801 | 类名：Window；  API声明：setWindowMask(windowMask: Array<Array<number>>): Promise<void>;  差异内容：1300002,1300003,1300004,401,801 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ParticleModifier  差异内容： export declare class ParticleModifier | api/arkui/ParticleModifier.d.ts |
| 新增API | NA | 类名：ParticleModifier；  API声明：applyNormalAttribute?(particleAttribute: ParticleAttribute): void;  差异内容：applyNormalAttribute?(particleAttribute: ParticleAttribute): void; | api/arkui/ParticleModifier.d.ts |
| 新增API | NA | 类名：WindowProperties；  API声明：displayId?: number;  差异内容：displayId?: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：moveWindowToAsync(x: number, y: number): Promise<void>;  差异内容：moveWindowToAsync(x: number, y: number): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：resizeAsync(width: number, height: number): Promise<void>;  差异内容：resizeAsync(width: number, height: number): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getAttachedFrameNodeById(id: string): FrameNode | null;  差异内容：getAttachedFrameNodeById(id: string): FrameNode | null; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：display；  API声明：function getDisplayByIdSync(displayId: number): Display;  差异内容：function getDisplayByIdSync(displayId: number): Display; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：StyledString；  API声明：static fromHtml(html: string): Promise<StyledString>;  差异内容：static fromHtml(html: string): Promise<StyledString>; | component/styled\_string.d.ts |
