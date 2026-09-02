---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-6112
title: ArkGraphics 2D
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Release引入的API > ArkGraphics 2D
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:d76d6d2112fa6512d4927c863d9373c4b93420ab21cfe2e117c77bbafdd278ac
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API卡片权限变更 | 类名：uiEffect；  API声明：function createEffect(): VisualEffect;  差异内容：NA | 类名：uiEffect；  API声明：function createEffect(): VisualEffect;  差异内容：form | api/@ohos.graphics.uiEffect.d.ts |
| 函数变更 | 类名：Matrix；  API声明：isEqual(matrix: Matrix): Boolean;  差异内容：Boolean | 类名：Matrix；  API声明：isEqual(matrix: Matrix): boolean;  差异内容：boolean | api/@ohos.graphics.drawing.d.ts |
| 函数变更 | 类名：Matrix；  API声明：invert(matrix: Matrix): Boolean;  差异内容：Boolean | 类名：Matrix；  API声明：invert(matrix: Matrix): boolean;  差异内容：boolean | api/@ohos.graphics.drawing.d.ts |
| 函数变更 | 类名：Matrix；  API声明：isIdentity(): Boolean;  差异内容：Boolean | 类名：Matrix；  API声明：isIdentity(): boolean;  差异内容：boolean | api/@ohos.graphics.drawing.d.ts |
| 函数变更 | 类名：Canvas；  API声明：drawPixelMapMesh(pixelmap: image.PixelMap, meshWidth: number, meshHeight: number, vertices: Array<number>, vertOffset: number, colors: Array<number>, colorOffset: number): void;  差异内容：colors: Array<number> | 类名：Canvas；  API声明：drawPixelMapMesh(pixelmap: image.PixelMap, meshWidth: number, meshHeight: number, vertices: Array<number>, vertOffset: number, colors: Array<number> | null, colorOffset: number): void;  差异内容：colors: Array<number> | null | api/@ohos.graphics.drawing.d.ts |
