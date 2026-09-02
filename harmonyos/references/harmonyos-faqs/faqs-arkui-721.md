---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-721
title: Radio组件通过ContentModifier实现自定义样式后如何实现单选
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Radio组件通过ContentModifier实现自定义样式后如何实现单选
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:939b147434aec604053023d4525c69dec1c1bc0ddbba3856f125bae4f4c49a9f
---

## 问题现象

当Radio设置通过ContentModifier设置自定义内容后，Radio无法实现单选功能。

问题代码如下：

```ts
class DiRadio implements ContentModifier<RadioConfiguration> {
  applyContent(): WrappedBuilder<[RadioConfiguration]> {
    return wrapBuilder(buildDiRadio);
  }
}

@Builder
function buildDiRadio(config: RadioConfiguration) {
  Column() {
    Image(config.checked ? $r('app.media.checked_true') : $r('app.media.checked_false'))
      .width(24).height(24)
  };
}

@Entry
@Component
struct CustomRadio {
  build() {
    Column({ space: 15 }) {
      Column({ space: 5 }) {
        Text('Radio1');
        Radio({ value: 'Radio1', group: 'radioGroup' }).contentModifier(new DiRadio());
      };

      Column({ space: 5 }) {
        Text('Radio2');
        Radio({ value: 'Radio2', group: 'radioGroup' }).contentModifier(new DiRadio());
      };

      Column({ space: 5 }) {
        Text('Radio3');
        Radio({ value: 'Radio3', group: 'radioGroup' }).contentModifier(new DiRadio());
      };
    }
    .height('100%')
    .width('100%');
  }
}
```

问题效果预览:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/AXeLT94VSSmpMMIb3suaCw/zh-cn_image_0000002658914533.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/BM71IsMDT1-Ad8FR4WThKQ/zh-cn_image_0000002628395308.png "点击放大")

## 背景知识

* [ContentModifier接口](../harmonyos-guides/arkts-common-attributes-content-modifier.md)：内容修改器，提供自定义绘制组件内容区的能力。
* [Radio](../harmonyos-references/ts-basic-components-radio.md)：单选框，提供相应的用户交互选择项。[contentModifier](../harmonyos-references/ts-basic-components-radio.md#contentmodifier18)，在Radio组件上，定制内容区的方法。modifier，内容修改器，开发者需要自定义class实现ContentModifier接口。当modifier的值为undefined时，不使用内容修改器。

## 问题定位

Radio组件添加了ContentModifier后，当选择Radio时没有修改checked的值。

## 分析结论

目前Radio组件添加了ContentModifier后，内容、样式和触发条件需要自己定义。

## 修改建议

在ContentModifier的基础上，给自定义内容添加点击事件。当checked的值为false时，通过triggerChange方法修改当前Radio的checked值为true（同group的其他Radio的checked值会自动变为false），可以解决该问题。

代码示例如下：

```ts
class DiRadio implements ContentModifier<RadioConfiguration> {
  applyContent(): WrappedBuilder<[RadioConfiguration]> {
    return wrapBuilder(buildDiRadio);
  }
}

@Builder
function buildDiRadio(config: RadioConfiguration) {
  Column() {
    Image(config.checked ? $r('app.media.startIcon') : $r('app.media.background'))
      .width(24).height(24)
      .onClick(() => {
        if (!config.checked) {
          config.triggerChange(true);
        }
      });
  };
}

@Entry
@Component
struct CustomRadio {
  build() {
    Column({ space: 15 }) {
      Column({ space: 5 }) {
        Text('Radio1');
        Radio({ value: 'Radio1', group: 'radioGroup' }).contentModifier(new DiRadio());
      };

      Column({ space: 5 }) {
        Text('Radio2');
        Radio({ value: 'Radio2', group: 'radioGroup' }).contentModifier(new DiRadio());
      };

      Column({ space: 5 }) {
        Text('Radio3');
        Radio({ value: 'Radio3', group: 'radioGroup' }).contentModifier(new DiRadio());
      };
    }
    .height('100%')
    .width('100%');
  }
}
```
