---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/accessibilityactionoptions-scrollstep
title: 自定义无障碍滚动步数
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 自定义无障碍滚动步数
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:33ae003562b3d2a6b7cf997176678c50d836a2a23841a1c812558edd1d44e799
---

## 设计场景

可调节的滑动条支持长按拖拽调节，调节步长通常允许小于取值范围的1%，适用于视频进度等精细控制场景。然而，长按拖拽操作对视障用户不够友好。为此，当屏幕朗读功能开启时，系统额外支持了通过上下扫动手势调节已聚焦的滑动条，每次调节后自动播报当前状态值（默认为百分比格式）。为避免连续调节时重复播报相同状态值，需通过[accessibilityActionOptions](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilityactionoptions23)配置滑动条的无障碍操作步数，确保每次调节步长大于或等于取值范围的1%。

## accessibilityActionOptions说明：

* [scrollStep](../harmonyos-references/ts-universal-attributes-accessibility.md)：指定由无障碍手势触发的无障碍滚动操作步数。屏幕朗读模式下，聚焦[Slider](../harmonyos-references/ts-basic-components-slider.md)组件时，通过上下扫动手势调节滑动条，实际步长为[scrollStep](../harmonyos-references/ts-universal-attributes-accessibility.md)×[step](../harmonyos-references/ts-basic-components-slider.md#slideroptions对象说明)。仅对[Slider](../harmonyos-references/ts-basic-components-slider.md)组件配置生效，其他组件配置不生效，取值范围为[1, ([max](../harmonyos-references/ts-basic-components-slider.md#slideroptions对象说明)- [min](../harmonyos-references/ts-basic-components-slider.md#slideroptions对象说明))/[step](../harmonyos-references/ts-basic-components-slider.md#slideroptions对象说明)]，默认值为1。设置值超出取值范围时取默认值1，设置值为取值范围内的非整数时向下取整。

## 开发流程

如下示例实现一个可调节的滑动条，并指定无障碍操作的步数：

```typescript
@Entry
@Component
export struct Rule_2_1_15 {
  title: string = 'Rule 2.1.15';
  @State scrollStep: number = 3;

  build() {
    NavDestination() {
      Column() {
        // 创建一个滑动条，最小值为0，最大值为100，当前值为10，步长为10。
        Slider({
          min: 0,
          max: 100,
          value: 10,
          step: 10,
          style: SliderStyle.OutSet
        })
          // 在屏幕朗读模式下，聚焦滑动条后执行上下扫动，滑动条调节步数为3。
          .accessibilityActionOptions({ scrollStep: this.scrollStep })
          .onChange((value: number, mode: SliderChangeMode) => {
            console.info('value:' + value + 'mode:' + mode.toString());
          })
      }
      .width('100%')
      .height('100%')
    }
    .title(this.title)
  }
}
```
