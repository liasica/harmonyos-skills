---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sensorservicekit-510
title: Sensor Service Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Sensor Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:15+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4210638e5bf9f944604319e1052ba8d242dbfb934a8be7bfb96b1e79374f4432
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 自定义类型变更 | 类名：vibrator；  API声明：type VibrateEffect = VibrateTime | VibratePreset | VibrateFromFile;  差异内容：VibrateTime | VibratePreset | VibrateFromFile | 类名：vibrator；  API声明：type VibrateEffect = VibrateTime | VibratePreset | VibrateFromFile | VibrateFromPattern;  差异内容：VibrateTime | VibratePreset | VibrateFromFile | VibrateFromPattern | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：HapticFeedback；  API声明：EFFECT\_NOTICE\_SUCCESS = 'haptic.notice.success'  差异内容：EFFECT\_NOTICE\_SUCCESS = 'haptic.notice.success' | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：HapticFeedback；  API声明：EFFECT\_NOTICE\_FAILURE = 'haptic.notice.fail'  差异内容：EFFECT\_NOTICE\_FAILURE = 'haptic.notice.fail' | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：HapticFeedback；  API声明：EFFECT\_NOTICE\_WARNING = 'haptic.notice.warning'  差异内容：EFFECT\_NOTICE\_WARNING = 'haptic.notice.warning' | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：vibrator；  API声明：enum VibratorEventType  差异内容：enum VibratorEventType | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorEventType；  API声明：CONTINUOUS = 0  差异内容：CONTINUOUS = 0 | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorEventType；  API声明：TRANSIENT = 1  差异内容：TRANSIENT = 1 | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：vibrator；  API声明：interface VibratorCurvePoint  差异内容：interface VibratorCurvePoint | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorCurvePoint；  API声明：time: number;  差异内容：time: number; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorCurvePoint；  API声明：intensity?: number;  差异内容：intensity?: number; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorCurvePoint；  API声明：frequency?: number;  差异内容：frequency?: number; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：vibrator；  API声明：interface VibratorEvent  差异内容：interface VibratorEvent | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorEvent；  API声明：eventType: VibratorEventType;  差异内容：eventType: VibratorEventType; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorEvent；  API声明：time: number;  差异内容：time: number; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorEvent；  API声明：duration?: number;  差异内容：duration?: number; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorEvent；  API声明：intensity?: number;  差异内容：intensity?: number; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorEvent；  API声明：frequency?: number;  差异内容：frequency?: number; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorEvent；  API声明：index?: number;  差异内容：index?: number; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorEvent；  API声明：points?: Array<VibratorCurvePoint>;  差异内容：points?: Array<VibratorCurvePoint>; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：vibrator；  API声明：interface VibratorPattern  差异内容：interface VibratorPattern | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorPattern；  API声明：time: number;  差异内容：time: number; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorPattern；  API声明：events: Array<VibratorEvent>;  差异内容：events: Array<VibratorEvent>; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：vibrator；  API声明：interface ContinuousParam  差异内容：interface ContinuousParam | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：ContinuousParam；  API声明：intensity?: number;  差异内容：intensity?: number; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：ContinuousParam；  API声明：frequency?: number;  差异内容：frequency?: number; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：ContinuousParam；  API声明：points?: VibratorCurvePoint[];  差异内容：points?: VibratorCurvePoint[]; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：ContinuousParam；  API声明：index?: number;  差异内容：index?: number; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：vibrator；  API声明：interface TransientParam  差异内容：interface TransientParam | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：TransientParam；  API声明：intensity?: number;  差异内容：intensity?: number; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：TransientParam；  API声明：frequency?: number;  差异内容：frequency?: number; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：TransientParam；  API声明：index?: number;  差异内容：index?: number; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：vibrator；  API声明：class VibratorPatternBuilder  差异内容：class VibratorPatternBuilder | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorPatternBuilder；  API声明：addContinuousEvent(time: number, duration: number, options?: ContinuousParam): VibratorPatternBuilder;  差异内容：addContinuousEvent(time: number, duration: number, options?: ContinuousParam): VibratorPatternBuilder; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorPatternBuilder；  API声明：addTransientEvent(time: number, options?: TransientParam): VibratorPatternBuilder;  差异内容：addTransientEvent(time: number, options?: TransientParam): VibratorPatternBuilder; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibratorPatternBuilder；  API声明：build(): VibratorPattern;  差异内容：build(): VibratorPattern; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：vibrator；  API声明：interface VibrateFromPattern  差异内容：interface VibrateFromPattern | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibrateFromPattern；  API声明：type: 'pattern';  差异内容：type: 'pattern'; | api/@ohos.vibrator.d.ts |
| 新增API | NA | 类名：VibrateFromPattern；  API声明：pattern: VibratorPattern;  差异内容：pattern: VibratorPattern; | api/@ohos.vibrator.d.ts |
