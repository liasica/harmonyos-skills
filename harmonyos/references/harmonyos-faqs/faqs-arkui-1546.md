---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1546
title: 如何解决复杂嵌套对象属性更新失效的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决复杂嵌套对象属性更新失效的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5cf7833182f036bdf4a226824b644adc7bbeb325afc6cabfb01e48e222c64a27
---

## 问题现象

当页面数据使用的复杂嵌套类型时，涉及的不刷新的原因较多，应该如何排查复杂嵌套对象属性更新失效的问题？

## 背景知识

* [@Observed/@ObjectLink](../harmonyos-guides/arkts-observed-and-objectlink.md)：用于嵌套场景的观察，比如二维数组、对象数组、嵌套类场景，需要观察到深层的属性变化，且@Observed/@ObjectLink需要配套使用。一般的嵌套失效问题可参考官网链接：[常见问题](../harmonyos-guides/arkts-observed-and-objectlink.md#常见问题)。
* [makeV1Observed](../harmonyos-references/js-apis-statemanagement.md#makev1observed19)：将不可观察的对象包装成状态管理V1可观察的对象，其能力等同于@Observed装饰器，可初始化@ObjectLink。

**对于复杂嵌套对象没有触发UI刷新的问题可以从以下方面考虑：**

* 装饰器的作用规则。以@Observed/@ObjectLink为例，根据官方文档[@Observed/@ObjectLink概述](../harmonyos-guides/arkts-observed-and-objectlink.md#概述)，当一个类能被监听需要满足以下条件：
  1. 被声明的状态变量必须通过new操作符进行创建。
  2. 若这个类是深层嵌套的类，需要保证被监听的属性所在的深层的类也被@Observed装饰。
  3. 在子组件使用@Prop接收状态变量，此时若在子组件中修改该变量，并不会引起父组件刷新，需要使用@ObjectLink接收状态变量，且每接收一层对象都需要单独封装一个@Component子组件，并使用@ObjectLink接收。
* 控制渲染规则。存在[ForEach组件](../harmonyos-guides/arkts-rendering-control-foreach.md)、[Repeat组件](../harmonyos-guides/arkts-new-rendering-control-repeat.md)等控制渲染组件时，由于其渲染规则导致的UI不刷新（数据为对象数组时常出现该类问题）。
* 参数传递规则。在进行状态变量传递时，子组件若是采用[@Builder](../harmonyos-guides/arkts-builder.md)或者[@LocalBuilder](../harmonyos-guides/arkts-localbuilder.md)装饰的自定义构建函数时，还应该考虑值传递、引用传递与回调传递等参数传递的问题。

## 解决方案

针对以上排查的各步骤可能会出现的问题，对应的解决方案如下：

|  |  |  |
| --- | --- | --- |
| 场景 | 违反的规则 | 解决方案 |
| 场景一 | 违背装饰器作用规则第一点，未使用new创建可深度观测的嵌套对象，导致复杂嵌套对象不刷新。 | 方案一：使用new操作符创建。 |
| 方案二：使用makeV1Observed方法代替@Observed装饰器。 |
| 场景二 | 违背装饰器作用规则第二点和第三点，@Observed/@ObjectLink搭配使用不正确，导致复杂嵌套对象不刷新。 | 参考官网链接[复杂嵌套对象属性更改失效](../harmonyos-guides/arkts-observed-and-objectlink.md#复杂嵌套对象属性更改失效)。 |
| 场景三 | 违背控制渲染规则，以ForEach为例，参数更新时，key值未改变，导致复杂嵌套对象不刷新。 | 详情可参考官网行业常见问题，[如何解决使用@State修饰对象数组，数据变化时页面不刷新问题](faqs-arkui-1071.md)场景三。 |
| 场景四 | 违反参数传递规则，在进行复杂嵌套对象属性更新时，由于内部自定义组件使用了@Builder/@LocalBuilder自定义构建函数，且使用的值传递的方式，导致复杂嵌套对象不刷新。 | 在不违反其它上述使用规则的前提下，[按回调传递参数](../harmonyos-guides/arkts-builder.md#按回调传递参数)、[按引用传递参数](../harmonyos-guides/arkts-builder.md#按引用传递参数)即可刷新自定义构建函数内的UI。 |

**须知** 

在状态管理V2中深度观测的装饰器为[@ObservedV2/@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)，其装饰器规则与V1版本@Observed/@ObjectLink存在一定差异，详情可参考官网行业常见问题[使用@ObservedV2和@Trace深度观测对象时，数据改变而UI未刷新](faqs-arkui-1011.md)、[使用状态管理V1、V2进行深度观测的区别和优缺点](faqs-arkui-1068.md)，其它排查步骤一致。

* 场景一：违背装饰器作用规则第一点，未使用new创建可深度观测的嵌套对象，导致复杂嵌套对象不刷新。
  + 方案一：参考官网行业常见问题，[如何解决使用@State修饰对象数组，数据变化时页面不刷新问题](faqs-arkui-1071.md)场景一，使用new创建即可。
  + 方案二：状态管理V1中，为了应对某些三方包中的类等无法被状态管理装饰器装饰，从而导致UI无法刷新的问题，在V1版本中推出了makeV1Observed接口，实现普通变量的深层监听。使用方式如下：

    ```ts
    @State items: Item[] = [
      UIUtils.makeV1Observed({ name: '张三', num: 18 }),
      UIUtils.makeV1Observed({ name: '李四', num: 20 })
    ];
    ```

  完整的代码参考如下：

  ```ts
  import { UIUtils } from '@kit.ArkUI';

  @Observed
  class Item {
    name: string = '';
    num: number = 0;
  }

  @Component
  @Entry
  struct SceneOneOptionTwo {
    @State items: Item[] = [
      UIUtils.makeV1Observed({ name: '张三', num: 18 }),
      UIUtils.makeV1Observed({ name: '李四', num: 20 })
    ];

    build() {
      Column() {
        ForEach(this.items, (item: Item) => {
          MyItem({ item: item });
        });
      };
    }
  }

  @Component
  struct MyItem {
    @ObjectLink item: Item;

    build() {
      Row() {
        Text(this.item.name);
        Row() {
          Button('+').onClick(() => {
            this.item.num++;
          });
          Row() {
            Text(`${this.item.num}`);
          }
          .width(50)
          .justifyContent(FlexAlign.Center);

          Button('-').onClick(() => {
            this.item.num--;
          });
        };
      }
      .margin({
        top: 20
      })
      .justifyContent(FlexAlign.SpaceAround)
      .width('100%');
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/gKf0UgPyRMCFB5ZqpiNP4g/zh-cn_image_0000002658968441.png "点击放大")
* 场景二：违背装饰器作用规则第二点和第三点，@Observed/@ObjectLink搭配使用不正确，导致复杂嵌套对象不刷新。

  @ObjectLink装饰器仅能观察其代理的属性，无法观察到代理属性的嵌套对象属性，所以每一层被嵌套的对象都需要封装一个子组件并用@ObjectLink接收。详情可参考官网链接：[复杂嵌套对象属性更改失效](../harmonyos-guides/arkts-observed-and-objectlink.md#复杂嵌套对象属性更改失效)。
* 场景三：违背控制渲染规则，以ForEach为例，参数更新时，key值未改变，导致复杂嵌套对象不刷新。

  在ForEach组件进行非首次渲染时，它会检查新生成的键值是否在上次渲染中已经存在。如果键值不存在，则会创建一个新的组件；如果键值存在，则不会创建新的组件，而是直接渲染该键值所对应的组件。此时，若未注意控制渲染组件刷新规则，则可能造成UI不刷新的情况，详情可参考官网行业常见问题，[如何解决使用@State修饰对象数组，数据变化时页面不刷新问题](faqs-arkui-1071.md)场景三，区别控制渲染刷新与状态管理刷新即可。
* 场景四：违反参数传递规则，在进行复杂嵌套对象属性更新时，由于内部自定义组件使用了@Builder/@LocalBuilder自定义构建函数，且使用的值传递的方式，导致复杂嵌套对象不刷新。

  在@Builder/@LocalBuilder自定义构建函数传参过程中，如果使用的是值传递的方式，会导致自定义构建函数中的UI不会刷新，建议使用引用传递与回调传递，详情可参考官网：[按回调传递参数](../harmonyos-guides/arkts-builder.md#按回调传递参数)、[按引用传递参数](../harmonyos-guides/arkts-builder.md#按引用传递参数)。此时，需要注意深层嵌套的数据需要是被@ObjectLink装饰器接收的，否则依旧不会刷新。完整示例代码如下：

  ```ts
  @Observed
  class ItemFour {
    name: string = '';
    num: number = 0;

    constructor(name: string, num: number) {
      this.name = name;
      this.num = num;
    }
  }

  interface BuilderItem {
    name: string;
    num: number;
  }

  @Component
  @Entry
  struct SceneFour {
    @State items: ItemFour[] = [new ItemFour('张三', 18), new ItemFour('李四', 20)];

    build() {
      Column() {
        ForEach(this.items, (item: ItemFour) => {
          Column() {
            Text('Builder传递的是@ObjectLink接收的参数(可以刷新)：');
            MyItemFour({ item: item });
            Text('Builder传递的参数未经过@ObjectLink接收（无法刷新）：');
            Row() {
              Text(`${item.name}`);
              Row() {
                Button('+').onClick(() => {
                  item.num++;
                });
                builderFunctionTwo({ name: item.name, num: item.num }); // 引用传递可以刷新
                Button('-').onClick(() => {
                  item.num--;
                });
              };
            }
            .margin({
              top: 20
            })
            .justifyContent(FlexAlign.SpaceAround)
            .width('100%');
          }.width('90%');
        });
      }.width('100%');
    }
  }

  @Builder
  function builderFunctionTwo(item: BuilderItem) {
    Row() {
      Text(`${item.num}`);
    }
    .width(50)
    .justifyContent(FlexAlign.Center);
  }

  @Builder
  function builderFunction(item: BuilderItem) {
    Row() {
      Text(`${item.num}`);
    }
    .width(50)
    .justifyContent(FlexAlign.Center);
  }

  @Component
  struct MyItemFour {
    @ObjectLink item: ItemFour;

    build() {
      Row() {
        Text(`${this.item.name}`);
        Row() {
          Button('+').onClick(() => {
            this.item.num++;
          });
          builderFunction({ name: this.item.name, num: this.item.num }); // 引用传递可以刷新
          Button('-').onClick(() => {
            this.item.num--;
          });
        };
      }
      .margin({
        top: 20
      })
      .justifyContent(FlexAlign.SpaceAround)
      .width('100%');
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/11gSJIKCSPy9K5DtJ14iEg/zh-cn_image_0000002658848489.png "点击放大")
