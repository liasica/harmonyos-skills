---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-penkit-b061
title: Pen Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta6引入的API > Pen Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:24+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:9b9ca4d9b4883a2868974f6595bbe2c300cd2c66901d2a8b5d92e1ee6ca979ef
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace imageFeaturePicker  差异内容： declare namespace imageFeaturePicker | api/@hms.officeservice.imageFeaturePicker.d.ts |
| 新增API | NA | 类名：imageFeaturePicker；  API声明： interface PickedColorInfo  差异内容： interface PickedColorInfo | api/@hms.officeservice.imageFeaturePicker.d.ts |
| 新增API | NA | 类名：PickedColorInfo；  API声明：color: common2D.Color;  差异内容：color: common2D.Color; | api/@hms.officeservice.imageFeaturePicker.d.ts |
| 新增API | NA | 类名：PickedColorInfo；  API声明：colorSpace: colorSpaceManager.ColorSpace;  差异内容：colorSpace: colorSpaceManager.ColorSpace; | api/@hms.officeservice.imageFeaturePicker.d.ts |
| 新增API | NA | 类名：PickedColorInfo；  API声明：timestamp: number;  差异内容：timestamp: number; | api/@hms.officeservice.imageFeaturePicker.d.ts |
| 新增API | NA | 类名：imageFeaturePicker；  API声明：function pickForResult(x?: number, y?: number): Promise<PickedColorInfo>;  差异内容：function pickForResult(x?: number, y?: number): Promise<PickedColorInfo>; | api/@hms.officeservice.imageFeaturePicker.d.ts |
