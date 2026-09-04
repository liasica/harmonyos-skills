---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property
title: 自定义属性设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 动态属性与自定义 > 自定义属性设置
category: harmonyos-references
scraped_at: 2026-09-05T06:17:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2f2dd99d67fea451402f734045102a9b070013f75261bdf31e45376d85b2c541
---

当开发者希望在组件上设置自定义的属性时，可以使用自定义属性设置功能。这些自定义属性可以在组件对应的FrameNode上获取，从而便于根据自定义属性管理组件。

**说明** 

* 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## customProperty

customProperty(name: string, value: Optional<Object>): T

设置组件的自定义属性。

API版本26.0.0之前，[自定义组件](../harmonyos-guides/arkts-create-custom-components.md)不支持设置自定义属性。

从API版本26.0.0开始，自定义组件支持设置并读取自定义属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 自定义属性的名称。 |
| value | [Optional](ts-universal-attributes-custom-property.md#optionalt)<Object> | 是 | 自定义属性的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，可用于链式调用。 |

## Optional<T>

type Optional<T> = T | undefined

定义可选类型，其值可以是undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

| 类型 | 说明 |
| --- | --- |
| T | 表示泛型T所指定的类型。 |
| undefined | 表示该类型声明的对象是undefined。 |

## 示例

### 示例1（系统组件设置自定义属性）

在[Column](ts-container-column.md)组件上设置自定义属性，并在其对应的[FrameNode](js-apis-arkui-framenode.md#framenode-1)上获取所设置的自定义属性。

```ts
// xxx.ets
import { FrameNode, UIContext } from '@kit.ArkUI';

@Entry
@Component
struct CustomPropertyExample {
  build() {
    Column() {
      Text('text')
      Button('print').onClick(() => {
        // 获取Column对应的frameNode节点并查询设置的自定义属性
        const uiContext: UIContext = this.getUIContext();
        if (uiContext) {
          const node: FrameNode | null = uiContext.getFrameNodeById('Test_Column');
          if (node) {
            for (let i = 1; i < 4; i++) {
              const key = 'customProperty' + i;
              const property = node.getCustomProperty(key);
              console.info(key, JSON.stringify(property));
            }
          }
        }
      })
    }
    .id('Test_Column')
    // 设置Column组件的自定义属性
    .customProperty('customProperty1', {
      'number': 10,
      'string': 'this is a string',
      'bool': true,
      'object': {
        'name': 'name',
        'value': 100
      }
    })
    .customProperty('customProperty2', {})
    .customProperty('customProperty3', undefined)
    .width('100%')
    .height('100%')
  }
}
```

### 示例2（自定义组件设置自定义属性）

从API版本26.0.0开始，自定义组件支持通过[customProperty](ts-universal-attributes-custom-property.md#customproperty)接口设置自定义属性。本示例以[自定义组件的自定义布局](../harmonyos-guides/arkts-page-custom-components-layout.md)场景为例，在自定义组件上设置自定义属性，并在其[onMeasureSize](ts-custom-component-layout.md#onmeasuresize10)回调中获取所设置的自定义属性。

```ts
// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      CustomLayout({ builder: columnChildren })
        .customProperty('width', 100) // 为自定义组件设置自定义属性
        .customProperty('height', 400)
    }
  }
}

// 通过builder的方式传递多个组件，作为自定义组件的一级子组件（即不包含容器组件，如Column）
@Builder
function columnChildren() {
  ForEach([1, 2, 3], (index: number) => {
    Text('S' + index)
      .fontSize(30)
      .width(100)
      .height(100)
      .borderWidth(2)
      .offset({ x: 10, y: 20 })
  })
}

@Component
struct CustomLayout {
  @Builder
  doNothingBuilder() {
  };

  @BuilderParam builder: () => void = this.doNothingBuilder;
  result: SizeResult = {
    width: 0,
    height: 0
  };

  // 计算各子组件的大小
  onMeasureSize(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions) {
    let size = 100;
    children.forEach((child) => {
      let result: MeasureResult = child.measure({ minHeight: size, minWidth: size, maxWidth: size, maxHeight: size })
      size += result.width / 2;
    })
    let frameNode = this.getUIContext().getFrameNodeByUniqueId(this.getUniqueId());
    // 通过getCustomProperty获取设置的自定义属性
    // this.result在该用例中代表自定义组件本身的大小，onMeasureSize方法返回的是组件自身的尺寸
    this.result.width = (frameNode?.getCustomProperty('width') as number) ?? 50;
    this.result.height = (frameNode?.getCustomProperty('height') as number) ?? 50;
    return this.result;
  }
  // 放置各子组件的位置
  onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions) {
    let startPos = 300;
    children.forEach((child) => {
      let pos = startPos - child.measureResult.height;
      child.layout({ x: pos, y: pos })
    })
  }

  build() {
    this.builder()
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/2UpwDoF2RAe-sxbpmvJySA/zh-cn_image_0000002712245970.png)
