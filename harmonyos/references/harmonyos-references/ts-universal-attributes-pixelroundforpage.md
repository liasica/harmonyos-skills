---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-pixelroundforpage
title: 页面级像素取整
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 布局与边框 > 页面级像素取整
category: harmonyos-references
scraped_at: 2026-04-28T08:01:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:780193182aeccd92392b2746343cfc5fdf308c8867e84c88b6b0ea42c2521f1b
---

页面级像素取整的目标是将像素取整模式设为页面的上下文属性，以便在页面层面设置像素取整模式。

说明

* 本模块从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 若出现像素取整[问题](ts-universal-attributes-pixelroundforcomponent.md#常见问题)，且使用[组件级像素取整](ts-universal-attributes-pixelroundforcomponent.md)无法解决时，建议尝试采用PIXEL\_ROUND\_AFTER\_MEASURE模式。
* 在PIXEL\_ROUND\_AFTER\_MEASURE模式下，组件会在测量大小结束时进行取整，即最终大小相比于PIXEL\_ROUND\_ON\_LAYOUT\_FINISH模式可能扩大1px。
* 页面级像素取整与组件级像素取整的区别在于：页面级像素取整调整整个页面的像素取整时机，而组件级像素取整调整特定组件在特定方向上的像素取整对齐方式。

## setPixelRoundMode

PhonePC/2in1TabletTVWearable

setPixelRoundMode(mode: PixelRoundMode): void

设置当前页面的像素取整模式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [PixelRoundMode](ts-appendix-enums.md#pixelroundmode18) | 是 | 像素取整模式。  默认值：PixelRoundMode.PIXEL\_ROUND\_ON\_LAYOUT\_FINISH  设置异常值时，该属性为默认值。 |

**示例：**

```
1. // EntryAbility.ets
2. import { UIContext } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. onWindowStageCreate(windowStage: window.WindowStage) {
6. windowStage.loadContent('pages/Index', (err, data) => {
7. let uiContext :UIContext = windowStage.getMainWindowSync().getUIContext();
8. uiContext.setPixelRoundMode(PixelRoundMode.PIXEL_ROUND_AFTER_MEASURE);
9. if (err.code) {
10. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
11. return;
12. }
13. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
14. });
15. }
```

## getPixelRoundMode

PhonePC/2in1TabletTVWearable

getPixelRoundMode(): PixelRoundMode

获取当前页面的像素取整模式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelRoundMode](ts-appendix-enums.md#pixelroundmode18) | 当前页面的像素取整模式。 |

**示例：**

```
1. // EntryAbility.ets
2. import { UIContext } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. onWindowStageCreate(windowStage: window.WindowStage) {
6. windowStage.loadContent('pages/Index', (err, data) => {
7. let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
8. console.info("pixelRoundMode : " + uiContext.getPixelRoundMode().valueOf());
9. if (err.code) {
10. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
11. return;
12. }
13. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
14. });
15. }
```
