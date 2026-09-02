---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1422
title: 如何封装自定义UI框架
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何封装自定义UI框架
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d3fcd01208e5b85b147e81287b7c0a9096f4f769394b772de05b744d961cc06f
---

## 问题现象

如何基于基础组件来构建自己的UI框架？例如构建自定义List组件UI框架。

## 背景知识

* [动态属性](../harmonyos-references/ts-universal-attributes-attribute-modifier.md)能够动态设置组件的属性，支持开发者在属性设置时使用if/else语法，且根据需要使用多态样式设置属性。其中的[自定义Modifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#自定义modifier)支持TextModifier、ListModifier等接口，但是[自定义Modifier不支持感知@State装饰的状态数据变化](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#示例3自定义modifier不支持感知state装饰的状态数据变化)。
* [AttributeUpdater](../harmonyos-guides/arkts-user-defined-extension-attributeupdater.md)是一个特殊的[AttributeModifier](../harmonyos-guides/arkts-user-defined-extension-attributemodifier.md)，不仅继承了AttributeModifier的功能，还提供了直接获取属性对象的能力。通过属性对象，AttributeUpdater能够直接更新对应属性，无需经过状态变量，并且可以利用AttributeUpdater实现自定义的更新策略，从而进一步提升属性更新的性能。

## 解决方案

建议采用AttributeUpdater方法自定义框架，具体实现如下：

1. 首先，继承AttributeUpdater类定义ExListModify类，初始化并配置一个列表属性对象，通过链式调用的方式设置一些可选的属性，如滚动条状态exScrollBar、约束尺寸exConstrainSize、边缘效果exEdgeEffect和边缘效果选项exEdgeEffectOption。

   ```ts
   export class ExListModify extends AttributeUpdater<ListModifier> {
     private exScrollBar: BarState = BarState.Off;
     private exConstrainSize: ConstraintSizeOptions = { maxHeight: '100%' };

     initializeModifier(instance: ListAttribute): void {
       instance.scrollBar(this.exScrollBar)
         .constraintSize(this.exConstrainSize)
         .edgeEffect(EdgeEffect.None)
         .layoutWeight(1);
     }
   };
   ```
2. 接下来，实现一个自定义列表组件ExList，在build方法中，使用List组件构建列表结构，并通过AttributeModifier方法调用封装好的修饰类ExListModify。

   ```ts
   @Component
   export struct ExList {
     @BuilderParam bindView: () => void;
     attribute: ExListModify = new ExListModify();
     scroller: Scroller = new Scroller();
     @Prop space: string | number | undefined = undefined;
     @Prop initialIndex?: number = undefined;

     build() {
       List({ scroller: this.scroller, space: this.space, initialIndex: this.initialIndex }) {
         this.bindView();
       }.attributeModifier(this.attribute); // AttributeModifier方法调用封装好的修饰类ExListModify
     }
   }
   ```
3. 最后，通过使用自定义列表组件ExList来展示相关数据，完成列表内容的渲染与呈现。

   ```ts
   ExList({ attribute: this.modify }) {
     ForEach(this.dataList1, (item: number) => {
       ListItem() {
         Text('列表项目' + item.toString()).width('100%').height(44).textAlign(TextAlign.Center);
       };
     });
   };
   ```

完整示例参考如下：

```ts
import { AttributeUpdater, ListModifier } from '@kit.ArkUI';

// 初始化并配置列表属性对象
export class ExListModify extends AttributeUpdater<ListModifier> {
  private exScrollBar: BarState = BarState.Off;
  private exConstrainSize: ConstraintSizeOptions = { maxHeight: '100%' };

  initializeModifier(instance: ListAttribute): void {
    instance.scrollBar(this.exScrollBar)
      .constraintSize(this.exConstrainSize)
      .edgeEffect(EdgeEffect.None)
      .layoutWeight(1);
  }
};

// 自定义列表组件ExList
@Component
export struct ExList {
  @BuilderParam bindView: () => void;
  attribute: ExListModify = new ExListModify();
  scroller: Scroller = new Scroller();
  @Prop space: string | number | undefined = undefined;
  @Prop initialIndex?: number = undefined;

  build() {
    List({ scroller: this.scroller, space: this.space, initialIndex: this.initialIndex }) {
      this.bindView();
    }.attributeModifier(this.attribute); // AttributeModifier方法调用封装好的修饰类ExListModify
  }
}

@Entry
@Component
export struct CustomUiDemo {
  dataList1: number[] =
    [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2,
      3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2];
  dataList2: number[] =
    [23, 213, 213, 123, 21312, 421, 3123, 123, 124, 123, 124, 3512, 3512, 4324234, 12312, 213, 123, 12, 312, 321, 3,
      123, 124, 124, 234];
  dataType: number = 1;
  listScroller = new Scroller();
  modify: ExListModify = new ExListModify();

  build() {
    Column() {
      Button('点击更换列表').onClick(() => {
        this.modify.attribute?.backgroundColor('#0A59f7');
        this.modify.attribute?.scrollBar(BarState.On);
      });
      Blank().height(10);
      Button('点击增加').onClick(() => {
        this.modify.attribute?.scrollBar(BarState.Off);
        this.modify.attribute?.edgeEffect(EdgeEffect.Spring);
      });

      Blank().height(10);
      // 组件ExList展示相关数据
      ExList({ attribute: this.modify }) {
        ForEach(this.dataList1, (item: number) => {
          ListItem() {
            Text('列表项目' + item.toString()).width('100%').height(44).textAlign(TextAlign.Center);
          };
        });
      };

    }
    .width('100%')
    .height('100%');
  }
}
```

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/XyFKjGpbTD6kPCWcoyZ3Xw/zh-cn_image_0000002658962959.png "点击放大")

## 常见FAQ

Q：在构建页面时，去使用不同的Text组件替代List组件，这种情况下，构建几个Text组件就要创建几个Modifier，页面比较复杂时就可能要创建过多的Modifier，如何处理这种散装字段的数据源？

A：可以使用统一风格封装全局动态属性，专有特性方面可以自定义设置。

Q：可以使用AttributeModifier方法来实现自定义UI吗？TextModifier呢？

A：使用AttributeModifier实现的自定义UI不能在其中设置所有属性，会出现达不到预期效果的情况，而TextModifier实现的自定义UI包含所有属性，但是其不支持自定义Modifier感知@State装饰的数据的变化，无法进行数据变更。

Q：自定义组件不支持设置AttributeModifier吗？

A：从API version 20开始，AttributeModifier支持自定义组件。
