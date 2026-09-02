---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1021
title: 如何在Toggle的圆形滑块上添加文字
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何在Toggle的圆形滑块上添加文字
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cd21c823040138d01de7d8dcc163fdfad30d6fca2a9b90e1e1a7a3df61fdb2d2
---

## 问题现象

Toggle使用开关样式，如何在圆形滑块上加字？

## 背景知识

* [Toggle](../harmonyos-references/ts-basic-components-toggle.md)设置为开关样式时，支持设置包含圆形滑块半径、颜色等的[switchStyle](../harmonyos-references/ts-basic-components-toggle.md#switchstyle12)，更多设置可以使用[contentModifier](../harmonyos-references/ts-basic-components-toggle.md#contentmodifier12)定制Toggle内容区。
* 组件的某些通用属性变化时，可以通过[属性动画](../harmonyos-references/ts-animatorproperty.md)实现渐变过渡效果。

## 解决方案

Toggle的switchStyle仅支持设置圆形滑块半径或颜色，不支持添加内容，因此需要自定义Toggle内容区实现。

1. 自定义开关样式接口，并创建其实现类。
2. 构建自定义Toggle内容区。并使用属性动画animation达到与Toggle相似的动效。
3. 使用contentModifier定制Toggle内容区。

示例代码如下：

```ts
// 自定义开关样式接口
interface SwitchParam {
  circleRadius: number,
  borderRadius: number,
  selectedCircleColor: ResourceColor,
  unselectedCircleColor: ResourceColor,
  selectedColor: ResourceColor,
  unselectedColor: ResourceColor,
  selectedLabel?: string,
  unselectedLabel?: string,
  labelColor?: ResourceColor,
  labelSize?: number
}

// 开关样式接口的实现类
class MySwitchStyle implements ContentModifier<ToggleConfiguration> {
  switchStyle: SwitchParam;

  constructor(switchStyle: SwitchParam) {
    this.switchStyle = switchStyle;
  }

  applyContent(): WrappedBuilder<[ToggleConfiguration]> {
    return wrapBuilder(buildSwitch);
  }
}
@Builder
function buildSwitch(config: ToggleConfiguration) { // 自定义Toggle内容区。
  Column() {
    Button(config.isOn ? // 配置圆形滑块的文字。
      (config.contentModifier as MySwitchStyle).switchStyle.selectedLabel ?? '' :
      (config.contentModifier as MySwitchStyle).switchStyle.unselectedLabel ?? '',
      { type: ButtonType.Circle })
      .fontColor((config.contentModifier as MySwitchStyle).switchStyle.labelColor)
      .fontSize((config.contentModifier as MySwitchStyle).switchStyle.labelSize)
      .height((config.contentModifier as MySwitchStyle).switchStyle.circleRadius * 2)
      .width((config.contentModifier as MySwitchStyle).switchStyle.circleRadius * 2)
      .padding(0)
      .backgroundColor(config.isOn ?
      (config.contentModifier as MySwitchStyle).switchStyle.selectedCircleColor :
      (config.contentModifier as MySwitchStyle).switchStyle.unselectedCircleColor)
  }
  .padding((config.contentModifier as MySwitchStyle).switchStyle.borderRadius -
  (config.contentModifier as MySwitchStyle).switchStyle.circleRadius)
  .alignItems(config.isOn ? HorizontalAlign.Start : HorizontalAlign.End)
  .justifyContent(FlexAlign.Center)
  .backgroundColor(config.isOn ?
  (config.contentModifier as MySwitchStyle).switchStyle.selectedColor :
  (config.contentModifier as MySwitchStyle).switchStyle.unselectedColor)
  .borderRadius((config.contentModifier as MySwitchStyle).switchStyle.borderRadius)
  .height((config.contentModifier as MySwitchStyle).switchStyle.borderRadius * 2)
  .width((config.contentModifier as MySwitchStyle).switchStyle.borderRadius * 4 + 2)
  .onClick(() => {
    config.triggerChange(!config.isOn);
  })
  // 当开关切换时，存在背景色过渡动画。
  .animation({
    duration: 200,
    curve: Curve.Ease,
    playMode: PlayMode.Normal
  });
}
@Entry
@Component
struct ToggleTypeSwitch {
  build() {
    Column() {
      Toggle({ type: ToggleType.Switch })
        .enabled(true)
        .contentModifier(new MySwitchStyle({
          circleRadius: 9,
          borderRadius: 10,
          selectedCircleColor: Color.White,
          unselectedCircleColor: Color.White,
          selectedColor: '#ff5d7ef5',
          unselectedColor: '#e4a0b4e7',
          selectedLabel: '开',
          unselectedLabel: '关',
          labelColor: Color.Black,
          labelSize: 12
        }))
        .onChange((isOn: boolean) => {
          console.info(`Switch Log: ${isOn}`);
        });
    }.height('100%').width('100%').justifyContent(FlexAlign.Center);
  }
}
```
