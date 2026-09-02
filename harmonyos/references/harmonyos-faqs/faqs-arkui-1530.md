---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1530
title: 滑动组件出现不规则分隔线
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 滑动组件出现不规则分隔线
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:52564de95111a1b8b873b4c675f900e52241c6c50023d5fbce39436811298ca8
---

## 问题现象

在滑动组件中，会出现不规则分隔线的情况，例如Grid组件：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/Z_fnwkNHRzO0_mq0UBAAbA/zh-cn_image_0000002658846241.png "点击放大")

或者List组件：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/6hUUGAH7RHGU1HyKY_dvtQ/zh-cn_image_0000002628766882.png "点击放大")

以List列表为例，其中ListItem的height属性交替设置成162lpx以及163lpx，滚动时会出现闪烁的分隔线。问题代码如下：

```screen
@Entry
@Component
export struct TestList {
  private dataSource: string [] = []

  aboutToAppear(): void {
    let list: string[] = []
    for (let index = 0; index < 100; index++) {
      list.push(`--- ${index} ---`)
    }
    this.dataSource = list
  }

  build() {
    Column(){
      List() {
        ForEach(this.dataSource, (item: string, index: number) => {
          ListItem() {
            Row() {
              Text(item)
                .width('100%')
                .height('100%')
                .fontColor(Color.Black)
                .textAlign(TextAlign.Center)
                .backgroundColor(Color.White)
            }
            .width('100%')
            .height(index % 2 === 0 ? `162lpx` : `163lpx`)
          }
        }, (item: string) => {
          return item
        })
      }
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
      .listDirection(Axis.Vertical)
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor(Color.Black)
  }
}
```

## 背景知识

* [组件级像素取整](../harmonyos-references/ts-universal-attributes-pixelroundforcomponent.md)是将像素取整功能作为组件的属性，其中的[pixelRound](../harmonyos-references/ts-universal-attributes-pixelroundforcomponent.md#pixelround)方法能够指定当前组件在指定方向上的像素取整对齐方式，某方向未设置时默认在该方向进行四舍五入取整，能够有效避免闪烁情况的发生。
* [像素单位](../harmonyos-references/ts-pixel-units.md)vp是屏幕密度相关像素，根据屏幕像素密度转换为屏幕物理像素，当数值不带单位时，默认单位vp。而lpx是视窗逻辑像素单位，lpx单位为实际屏幕宽度与逻辑宽度的比值，比值能够通过designWidth配置。在[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)的window标签中，autoDesignWidth属性能够设置页面设计基准宽度是否允许自动计算。

## 问题定位

通过分析List例子问题代码，发现由于162lpx和163lpx的高度不同，并且lpx单位为实际屏幕宽度与逻辑宽度的比值，导致某些像素在滚动时无法正确对齐，再加上没有设置适当的对齐方式，从而在ListItem子组件之间产生分隔线，并且随着列表的滑动产生视觉上的闪烁。

## 分析结论

当List组件的子组件ListItem之间的高度不同并且没有设置适当的对齐方式时，子组件之间就会产生间隙，即分隔线，并且伴随着列表的滑动形成分隔线闪烁的情况。

## 修改建议

* **方案一：设置autoDesignWidth属性。**

  在resources/base/profile/main\_pages.json中添加属性autoDesignWidth，并将其设置为true，即可标识页面设计基准宽度允许自动计算，List组件就能够根据设备的屏幕密度和宽度来调整布局，在不同的环境里保持一致的视觉效果。

  修正效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/eew9oIKATfCx6vv70oE36g/zh-cn_image_0000002658966209.png "点击放大")
* **方案二：设置相同的背景颜色。**

  可以将外层与内层的背景颜色设置为相同颜色，即可将分隔线覆盖，从而避免分隔线出现闪烁情况。关键示例代码如下：

  ```ts
  @Entry
  @Component
  export struct ListDivideLineOne {
    private dataSource: string [] = [];

    aboutToAppear(): void {
      let list: string[] = [];
      for (let index = 0; index < 100; index++) {
        list.push(`--- ${index} ---`);
      }
      this.dataSource = list;
    }

    build() {
      Column(){
        List() {
          ForEach(this.dataSource, (item: string, index: number) => {
            ListItem() {
              Row() {
                Text(item)
                  .backgroundColor(Color.White);
              }
              .justifyContent(FlexAlign.Center)
              .width('100%')
              .height(index % 2 === 0 ? `162lpx` : `163lpx`);
            };
          }, (item: string) => {
            return item;
          });
        }
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
        .listDirection(Axis.Vertical)
        .width('100%')
        .height('100%');
      }
      .backgroundColor(Color.White)
      .width('100%')
      .height('100%');
    }
  }
  ```

  修复效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/vYzZ1w2HSLaGd5Puk0gV4A/zh-cn_image_0000002628606990.png "点击放大")

* **方案三：更换lpx单位。**

  在使用lpx单位时，由于单位lpx是逻辑像素单位，主要用来确保界面元素在不同屏幕尺寸的设备上保持一致的视觉比例，会导致lpx单位与屏幕的实际物理像素不完全对应，从而无法将渲染组件精确映射到物理像素上。因此当height属性交替设置为162lpx和163lpx时，由于lpx的精度问题，可能导致某些像素被重复渲染或遗漏，从而在滚动时出现闪烁的分隔线。可以采用vp单位替换lpx单位，px、fp单位也可以起到同样的作用。示例代码如下：

  ```ts
  @Entry
  @Component
  export struct ListDivideLineTwo {
    private dataSource: string [] = [];

    aboutToAppear(): void {
      let list: string[] = [];
      for (let index = 0; index < 100; index++) {
        list.push(`--- ${index} ---`);
      }
      this.dataSource = list;
    }

    build() {
      Column(){
        List() {
          ForEach(this.dataSource, (item: string, index: number) => {
            ListItem() {
              Row() {
                Text(item)
                  .backgroundColor(Color.White);
              }
              .justifyContent(FlexAlign.Center)
              .width('100%')
              .height(index % 2 == 0 ? `162vp` : `163vp`);
            };
          }, (item: string) => {
            return item;
          });
        }
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
        .listDirection(Axis.Vertical)
        .width('100%')
        .height('100%')
      }
      .width('100%')
      .height('100%')
    }
  }
  ```

  修复效果同方案一。

* **方案四：设置pixelRound属性。**

  在Text组件下添加属性pixelRound，并将其属性top设置为PixelRoundCalcPolicy.FORCE\_FLOOR，bottom设置为PixelRoundCalcPolicy.FORCE\_CEIL，这样Text组件的上部边界取下整对齐方式，底部边界取上整对齐方式，Text组件的交界处就不会出现分隔线闪烁的情况。示例图中的Grid组件也可以通过设置pixelRound属性解决分隔线问题。完整示例代码如下：

  ```ts
  @Entry
  @Component
  export struct ListDivideLineThree {
    private dataSource: string [] = [];

    aboutToAppear(): void {
      let list: string[] = [];
      for (let index = 0; index < 100; index++) {
        list.push(`--- ${index} ---`);
      }
      this.dataSource = list;
    }

    build() {
      Column(){
        List() {
          ForEach(this.dataSource, (item: string, index: number) => {
            ListItem() {
              Row() {
                Text(item)
                  .width('100%')
                  .fontColor(Color.Black)
                  .textAlign(TextAlign.Center)
                  .backgroundColor(Color.White)
                  .pixelRound({
                    top: PixelRoundCalcPolicy.FORCE_FLOOR,
                    bottom: PixelRoundCalcPolicy.FORCE_CEIL,
                  });
              }
              .justifyContent(FlexAlign.Center)
              .width('100%')
              .height(index % 2 === 0 ? `162lpx` : `163lpx`);
            };
          }, (item: string) => {
            return item;
          });
        }
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
        .backgroundColor(Color.White)
        .listDirection(Axis.Vertical)
        .width('100%')
        .height('100%');
      }
      .backgroundColor(Color.Black)
      .width('100%')
      .height('100%');
    }
  }
  ```

  修复效果同方案二。

## 总结

对于组件出现分隔线的问题，本文提供四种方案进行解决，四种方案对比情况如下：

| 方案 | 适用场景 |
| --- | --- |
| 设置autoDesignWidth属性 | 在需要设置designWidth场景不适用，启用autoDesignWidth会使designWidth的值被忽略。 |
| 设置相同的背景颜色 | 规避类型的方法，只能在特定场景下使用。 |
| 更换lpx单位 | 部分场景无法保持一致的视觉效果，不适配所有屏幕。 |
| 设置pixelRound属性 | 适用大多数场景与组件，推荐使用。 |
