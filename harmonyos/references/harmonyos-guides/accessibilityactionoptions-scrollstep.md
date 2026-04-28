---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/accessibilityactionoptions-scrollstep
title: 自定义无障碍滚动步数的场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 自定义无障碍滚动步数的场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6fdf7df8781599c0f9e447dfecccd9579ab7fec4dfaa9a02f8e9c9ece1d5b3ea
---

## 设计场景

可调节的滑动条支持长按拖拽调节，调节步长通常允许小于取值范围的1%，适用于视频进度等精细控制场景。然而，长按拖拽操作对视障用户不够友好。为此，当屏幕朗读功能开启时，系统额外支持了通过上下扫动手势调节已聚焦的滑动条，每次调节后自动播报当前状态值（默认为百分比格式）。为避免连续调节时重复播报相同状态值，需通过accessibilityActionOptions配置滑动条的无障碍操作步数，确保每次调节步长大于或等于取值范围的1%。

## accessibilityActionOptions说明：

* [scrollStep](../harmonyos-references/ts-universal-attributes-accessibility.md)：指定由无障碍手势触发的无障碍滚动操作步数。屏幕朗读模式下，聚焦[Slider](../harmonyos-references/ts-basic-components-slider.md)组件时，通过上下扫动手势调节滑动条，实际步长为[scrollStep](../harmonyos-references/ts-universal-attributes-accessibility.md)×[step](../harmonyos-references/ts-basic-components-slider.md#slideroptions对象说明)。仅对[Slider](../harmonyos-references/ts-basic-components-slider.md)组件配置生效，其他组件配置不生效，取值范围为[1, ([max](../harmonyos-references/ts-basic-components-slider.md#slideroptions对象说明)- [min](../harmonyos-references/ts-basic-components-slider.md#slideroptions对象说明))/[step](../harmonyos-references/ts-basic-components-slider.md#slideroptions对象说明)]，默认值为1。设置值超出取值范围时取默认值1，设置值为取值范围内的非整数时向下取整。

## 开发实例

如下示例实现一个可调节的滑动条，并指定无障碍操作的步数：

```
1. @Entry
2. @Component
3. struct Rule_2_1_15 {
4. title: string = 'Rule 2.1.15';
5. @State scrollStep: number = 3

7. build() {
8. NavDestination() {
9. Column() {
10. // 创建一个滑动条，最小值为0，最大值为100，当前值为10，步长为10
11. Slider({
12. min: 0,
13. max: 100,
14. value: 10,
15. step: 10,
16. style: SliderStyle.OutSet
17. })
18. // 在屏幕朗读模式下，聚焦滑动条后执行上下扫动，滑动条调节步数为3
19. .accessibilityActionOptions({ scrollStep: this.scrollStep })
20. .onChange((value: number, mode: SliderChangeMode) => {
21. console.info('value:' + value + 'mode:' + mode.toString())
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. .title(this.title)
28. }
29. }
```
