---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-pixelroundforpage
title: 页面级像素取整
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 布局与边框 > 页面级像素取整
category: harmonyos-references
scraped_at: 2026-09-02T15:00:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:93efd48b0189add6835cbe27d2d70c1c7187b36d78c22c0f1d140cc226d7ce47
---

页面级像素取整是一种像素对齐机制，通过对组件尺寸和位置的计算结果进行取整处理，解决因浮点数像素值导致的显示模糊或边缘锯齿问题。页面级像素取整将像素取整模式设为页面的上下文属性，以便在页面层面统一控制像素对齐方式，提升UI显示的清晰度和一致性。适用于需要精确控制像素对齐的场景，如高质量图片渲染、精细动画效果等。

**说明** 

* 本模块从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 若出现像素取整[常见问题](ts-universal-attributes-pixelroundforcomponent.md#常见问题)，且使用[组件级像素取整](ts-universal-attributes-pixelroundforcomponent.md)无法解决时，建议尝试采用PIXEL\_ROUND\_AFTER\_MEASURE模式。
* 在PIXEL\_ROUND\_AFTER\_MEASURE模式下，组件会在测量大小结束时进行取整，即最终大小相比于PIXEL\_ROUND\_ON\_LAYOUT\_FINISH模式可能扩大1px。
* 页面级像素取整与组件级像素取整的区别在于：页面级像素取整调整整个页面的像素取整时机，而组件级像素取整调整特定组件在特定方向上的像素取整对齐方式。

## setPixelRoundMode

setPixelRoundMode(mode: PixelRoundMode): void

设置当前页面的像素取整模式，影响整个页面的像素取整时机。通常在使用[组件级像素取整](ts-universal-attributes-pixelroundforcomponent.md)无法解决像素取整问题时，可尝试采用PIXEL\_ROUND\_AFTER\_MEASURE模式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [PixelRoundMode](ts-appendix-enums.md#pixelroundmode18) | 是 | 像素取整模式，可选值：  - PIXEL\_ROUND\_ON\_LAYOUT\_FINISH：在布局完成后进行像素取整，适合大多数场景。  - PIXEL\_ROUND\_AFTER\_MEASURE：在组件测量大小结束后进行像素取整，适用于使用组件级像素取整无法解决的像素取整问题场景，但最终大小相比PIXEL\_ROUND\_ON\_LAYOUT\_FINISH模式可能扩大1px。  设置异常值时，按PixelRoundMode.PIXEL\_ROUND\_ON\_LAYOUT\_FINISH模式处理。 |

**示例：**

```ts
// EntryAbility.ets
import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

onWindowStageCreate(windowStage: window.WindowStage) {
   windowStage.loadContent('pages/Index', (err, data) => {
      // 获取UIContext实例
      let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
      // 设置像素取整模式为PIXEL_ROUND_AFTER_MEASURE
      uiContext.setPixelRoundMode(PixelRoundMode.PIXEL_ROUND_AFTER_MEASURE);
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
```

## getPixelRoundMode

getPixelRoundMode(): PixelRoundMode

获取当前页面的像素取整模式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelRoundMode](ts-appendix-enums.md#pixelroundmode18) | 当前页面的像素取整模式，取值包括：  - PIXEL\_ROUND\_ON\_LAYOUT\_FINISH（对应数值：0）：在布局完成后进行像素取整。  - PIXEL\_ROUND\_AFTER\_MEASURE（对应数值：1）：在组件测量大小结束后进行像素取整。 |

**示例：**

```ts
// EntryAbility.ets
import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', (err, data) => {
      // 获取UIContext实例
      let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
      // 获取并打印当前像素取整模式
      console.info("pixelRoundMode : " + uiContext.getPixelRoundMode().valueOf());
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
```
