---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-6102
title: ArkUI
breadcrumb: 版本说明 > 更多版本 > 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta2引入的变更 > ArkUI
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:08+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:ed09dc16ebe063606e5710463c5d382ab469bd3e9324035de58bf3887a5dac20
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：componentSnapshot；  API声明：function getSync(id: string, options?: SnapshotOptions): image.PixelMap;  差异内容：NA | 类名：componentSnapshot；  API声明：function getSync(id: string, options?: SnapshotOptions): image.PixelMap;  差异内容：160003 | api/@ohos.arkui.componentSnapshot.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：setCustomKeyboardContinueFeature(feature: CustomKeyboardContinueFeature): void;  差异内容：setCustomKeyboardContinueFeature(feature: CustomKeyboardContinueFeature): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export const enum CustomKeyboardContinueFeature  差异内容：export const enum CustomKeyboardContinueFeature | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：CustomKeyboardContinueFeature；  API声明：ENABLED = 0  差异内容：ENABLED = 0 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：CustomKeyboardContinueFeature；  API声明：DISABLED = 1  差异内容：DISABLED = 1 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface VerticalAlignParam  差异内容：declare interface VerticalAlignParam | component/common.d.ts |
| 新增API | NA | 类名：VerticalAlignParam；  API声明：anchor: string;  差异内容：anchor: string; | component/common.d.ts |
| 新增API | NA | 类名：VerticalAlignParam；  API声明：align: VerticalAlign;  差异内容：align: VerticalAlign; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface HorizontalAlignParam  差异内容：declare interface HorizontalAlignParam | component/common.d.ts |
| 新增API | NA | 类名：HorizontalAlignParam；  API声明：anchor: string;  差异内容：anchor: string; | component/common.d.ts |
| 新增API | NA | 类名：HorizontalAlignParam；  API声明：align: HorizontalAlign;  差异内容：align: HorizontalAlign; | component/common.d.ts |
| 新增API | NA | 类名：MarqueeOptions；  API声明：spacing?: LengthMetrics;  差异内容：spacing?: LengthMetrics; | component/marquee.d.ts |
| 新增API | NA | 类名：MarqueeOptions；  API声明：delay?: number;  差异内容：delay?: number; | component/marquee.d.ts |
| 新增API | NA | 类名：SwiperController；  API声明：startFakeDrag(): boolean;  差异内容：startFakeDrag(): boolean; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperController；  API声明：fakeDragBy(offset: number): boolean;  差异内容：fakeDragBy(offset: number): boolean; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperController；  API声明：stopFakeDrag(): boolean;  差异内容：stopFakeDrag(): boolean; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperController；  API声明：isFakeDragging(): boolean;  差异内容：isFakeDragging(): boolean; | component/swiper.d.ts |
| 属性类型匿名对象整改兼容 | 类名：AlignRuleOption；  API声明：left?: {  anchor: string;  align: HorizontalAlign;  };  差异内容：{  anchor: string;  align: HorizontalAlign;  } | 类名：AlignRuleOption；  API声明：left?: HorizontalAlignParam;  差异内容：HorizontalAlignParam | component/common.d.ts |
| 属性类型匿名对象整改兼容 | 类名：AlignRuleOption；  API声明：right?: {  anchor: string;  align: HorizontalAlign;  };  差异内容：{  anchor: string;  align: HorizontalAlign;  } | 类名：AlignRuleOption；  API声明：right?: HorizontalAlignParam;  差异内容：HorizontalAlignParam | component/common.d.ts |
| 属性类型匿名对象整改兼容 | 类名：AlignRuleOption；  API声明：middle?: {  anchor: string;  align: HorizontalAlign;  };  差异内容：{  anchor: string;  align: HorizontalAlign;  } | 类名：AlignRuleOption；  API声明：middle?: HorizontalAlignParam;  差异内容：HorizontalAlignParam | component/common.d.ts |
| 属性类型匿名对象整改兼容 | 类名：AlignRuleOption；  API声明：top?: {  anchor: string;  align: VerticalAlign;  };  差异内容：{  anchor: string;  align: VerticalAlign;  } | 类名：AlignRuleOption；  API声明：top?: VerticalAlignParam;  差异内容：VerticalAlignParam | component/common.d.ts |
| 属性类型匿名对象整改兼容 | 类名：AlignRuleOption；  API声明：bottom?: {  anchor: string;  align: VerticalAlign;  };  差异内容：{  anchor: string;  align: VerticalAlign;  } | 类名：AlignRuleOption；  API声明：bottom?: VerticalAlignParam;  差异内容：VerticalAlignParam | component/common.d.ts |
| 属性类型匿名对象整改兼容 | 类名：AlignRuleOption；  API声明：center?: {  anchor: string;  align: VerticalAlign;  };  差异内容：{  anchor: string;  align: VerticalAlign;  } | 类名：AlignRuleOption；  API声明：center?: VerticalAlignParam;  差异内容：VerticalAlignParam | component/common.d.ts |
