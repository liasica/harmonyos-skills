---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-607
title: 如何解决ForEach渲染对象数组时，删除数据异常的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决ForEach渲染对象数组时，删除数据异常的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1a6bb9e608ae2c5765c63762ba1185e3b69558ab1cf4d5776e95fa63eefa04f7
---

## 问题现象

ForEach渲染对象数组时，删除第三项ListItem时，剩余的ListItem会出现“选项6”重复显示的问题。问题代码如下：

```ts
class TestItem {
  id: number = 0;
  content: string = '';
}

@Entry
@Component
struct ListTestPage {
  @State testArray: Array<TestItem> = [];

  // 删除数组项
  changeArray(testArray: Array<TestItem>, index: number): Array<TestItem> {
    if (testArray.length <= 0 || index < 0 || index >= testArray.length) {
      return testArray;
    }
    return testArray.filter((_, i) => i !== index);
  }

  build() {
    Column() {
      Text('测试List复用异常的问题')
        .fontColor(Color.Black)
        .fontSize(18);
      List({ space: 8 }) {
        ForEach(this.testArray, (itemBean: TestItem, index: number) => {
          ListItem() {
            this.builderVoteOpinionView(itemBean, index);
          };
        });
      }
      .width('90%')
      .enableScrollInteraction(false)
      .scrollBar(BarState.Off)
      .edgeEffect(EdgeEffect.None)
      .margin({ top: 30 });

      // 添加按钮
      Row() {
        Button('添加列表数量');
      }
      .margin({ top: 20 })
      .borderRadius(4)
      .alignItems(VerticalAlign.Center)
      .onClick(() => {
        this.testArray.push(new TestItem());
      });
    }
    .width('100%')
    .backgroundColor(Color.White)
    .alignItems(HorizontalAlign.Center);
  }

  @Builder
  private builderVoteOpinionView(itemBean: TestItem, index: number) {
    Row() {
      TextInput({
        text: itemBean.content,
        placeholder: `选项${index + 1}`
      })
        .layoutWeight(1)
        .maxLength(14)
        .onChange((value: string) => {
          itemBean.content = value;
        })
        .defaultFocus(false); // 弹出软键盘
      Text('删除')
        .visibility(index >= 2 ? Visibility.Visible : Visibility.None)
        .onClick(() => {
          this.testArray = this.changeArray(this.testArray, index);
        });
    };
  }
}
```

问题现象如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/SNwikjZrSXmA2n7aOwEL3w/zh-cn_image_0000002628392724.png "点击放大")

## 背景知识

[ForEach](../harmonyos-references/ts-rendering-control-foreach.md)：在ForEach循环渲染过程中，系统会为每个数组元素生成一个唯一且持久的键值，用于标识对应的组件。当键值变化时，ArkUI框架会视为该数组元素已被替换或修改，并会基于新的键值创建一个新的组件。其使用方式及注意事项，详见官方指南：[键值生成规则](../harmonyos-guides/arkts-rendering-control-foreach.md#键值生成规则)与[组件创建规则](../harmonyos-guides/arkts-rendering-control-foreach.md#组件创建规则)。

## 问题定位

1. 从问题现象中可以发现在点击删除时，“选项6”为非首次渲染。从“选项3”开始依次删除时，“选项6”作为最后一个被修改的数据会一直显示到最后，直到数组的数量不足以显示“选项6”时，“选项6”消失。
2. 从数据结构上看，ForEach渲染的每一个对象都是一致的，按照ForEach的默认keyGenerator创建规则：如果函数缺省，框架默认的键值生成函数为(item: T, index: number) => { return index + '\_\_' + JSON.stringify(item); }，也就是所有的ListItem的keyGenerator除了Index都是一致的。

对ListItem的前三次删除后，所对应的“ListItem对应的keyGenerator，ListItem显示的值”分析如下表：

| ListItem | 删除操作前 | 第一次删除后 | 第二次删除后 | 第三次删除后 |
| --- | --- | --- | --- | --- |
| 选项1 | 0\_\_{"id":0,"content":""}，1 | 0\_\_{"id":0,"content":"1"}，1 | 0\_\_{"id":0,"content":"1"}，1 | 0\_\_{"id":0,"content":"1"}，1 |
| 选项2 | 1\_\_{"id":0,"content":""}，2 | 1\_\_{"id":0,"content":"2"}，2 | 1\_\_{"id":0,"content":"2"}，2 | 1\_\_{"id":0,"content":"2"}，2 |
| 选项3（每次点击删除的项） | 2\_\_{"id":0,"content":""}，3 | 2\_\_{"id":0,"content":"4"}，4 | 2\_\_{"id":0,"content":"5"}，5 | 2\_\_{"id":0,"content":"6"}，6 |
| 选项4 | 3\_\_{"id":0,"content":""}，4 | 3\_\_{"id":0,"content":"5"}，5 | 3\_\_{"id":0,"content":"6"}，6 | 3\_\_{"id":0,"content":""}，空 |
| 选项5 | 4\_\_{"id":0,"content":""}，5 | 4\_\_{"id":0,"content":"6"}，6 | 4\_\_{"id":0,"content":""}，空 | 4\_\_{"id":0,"content":""}，空 |
| 选项6 | 5\_\_{"id":0,"content":""}，6 | 5\_\_{"id":0,"content":""}，6 | 5\_\_{"id":0,"content":""}，6 | 5\_\_{"id":0,"content":""}，6 |
| 选项7 | 6\_\_{"id":0,"content":""}，空 | 6\_\_{"id":0,"content":""}，空 | 6\_\_{"id":0,"content":""}，空 | / |
| 选项8 | 7\_\_{"id":0,"content":""}，空 | 7\_\_{"id":0,"content":""}，空 | / | / |
| 选项9 | 8\_\_{"id":0,"content":""}，空 | / | / | / |

分析现象总结如下：

1. 选项6：keyGenerator一直没有变化，复用的原组件，所以输入为“6”以后，就一直显示“6”，直到对象数组长度不够，然后消失。
2. 选项5：第一次删除后，新建为显示“6”的ListItem；第二次删除后，新建为显示“空”的ListItem，之后就一直显示“空”，直到对象数组长度不够，然后消失。
3. 选项4：第一次删除后，新建为显示“5”的ListItem；第二次删除后，新建为显示“6”的ListItem；第三次删除后，新建为显示“空”的ListItem，之后就一直显示“空”，直到对象数组长度不够，然后消失。
4. 选项3：第一次删除后，新建为显示“4”的ListItem；第二次删除后，新建为显示“5”的ListItem；第三次删除后，新建为显示“6”的ListItem；如果有第四次删除，第四次删除后，会新建为显示“空”的ListItem，之后就一直显示“空”，直到对象数组长度不够，然后消失。

## 分析结论

ForEach渲染对象数组，删除数据时，刷新异常的原因是：ForEach一开始创建的ListItem都是用的相同的对象，使得删除操作后，系统默认生成的keyGenerator无法有效区分各个ListItem是否需要新建组件，从而产生刷新异常。

## 修改建议

根据以上分析结论，总结方案如下：

* 方案一：每个对象创建的时候做差异化处理，比如给每个对象的id传入不同的值。

  ```ts
  class TestItemOne {
    id: number = 0;
    content: string = '';

    constructor(id: number) {
      // 构造时传入不同的id
      this.id = id;
    }
  }

  @Entry
  @Component
  struct OptionOne {
    @State testArray: Array<TestItemOne> = [];

    // 删除数组项
    changeArray(testArray: Array<TestItemOne>, index: number): Array<TestItemOne> {
      if (testArray.length <= 0 || index < 0 || index >= testArray.length) {
        return testArray;
      }
      return testArray.filter((_, i) => i !== index);
    }

    build() {
      Column() {
        Text('测试List复用异常的问题')
          .fontColor(Color.Black)
          .fontSize(18);
        List({ space: 8 }) {
          ForEach(this.testArray, (itemBean: TestItemOne, index: number) => {
            ListItem() {
              this.builderVoteOpinionView(itemBean, index);
            };
          });
        }
        .width('90%')
        .enableScrollInteraction(false)
        .scrollBar(BarState.Off)
        .edgeEffect(EdgeEffect.None)
        .margin({ top: 30 });

        // 添加按钮
        Row() {
          Button('添加列表数量');
        }
        .margin({ top: 20 })
        .borderRadius(4)
        .alignItems(VerticalAlign.Center)
        .onClick(() => {
          // 构造时传入不同的id，此处以数组的长度作为数组最后一项的id，从而保证每个对象的id都不一致，从而刷新ForEach
          this.testArray.push(new TestItemOne(this.testArray.length));
        });
      }
      .width('100%')
      .backgroundColor(Color.White)
      .alignItems(HorizontalAlign.Center);
    }

    @Builder
    private builderVoteOpinionView(itemBean: TestItemOne, index: number) {
      Row({ space: 10 }) {
        TextInput({
          text: itemBean.content,
          placeholder: `选项${index + 1}`
        })
          .layoutWeight(1)
          .maxLength(14)
          .onChange((value: string) => {
            itemBean.content = value;
          })
          .defaultFocus(false);
        Text('删除')
          .visibility(index >= 2 ? Visibility.Visible : Visibility.None)
          .onClick(() => {
            this.testArray = this.changeArray(this.testArray, index);
          });
      };
    }
  }
  ```

  方案一对应的“ListItem对应的keyGenerator，ListItem显示的值”分析表如下：

  | ListItem | 删除操作前 | 第一次删除后 | 第二次删除后 | 第三次删除后 |
  | --- | --- | --- | --- | --- |
  | 选项1 | 0\_\_{"id":0,"content":""}，1 | 0\_\_{"id":0,"content":"1"}，1 | 0\_\_{"id":0,"content":"1"}，1 | 0\_\_{"id":0,"content":"1"}，1 |
  | 选项2 | 1\_\_{"id":1,"content":""}，2 | 1\_\_{"id":1,"content":"2"}，2 | 1\_\_{"id":1,"content":"2"}，2 | 1\_\_{"id":1,"content":"2"}，2 |
  | 选项3（每次点击删除的项） | 2\_\_{"id":2,"content":""}，3 | 2\_\_{"id":3,"content":"4"}，4 | 2\_\_{"id":4,"content":"5"}，5 | 2\_\_{"id":5,"content":"6"}，6 |
  | 选项4 | 3\_\_{"id":3,"content":""}，4 | 3\_\_{"id":4,"content":"5"}，5 | 3\_\_{"id":5,"content":"6"}，6 | 3\_\_{"id":6,"content":""}，空 |
  | 选项5 | 4\_\_{"id":4,"content":""}，5 | 4\_\_{"id":5,"content":"6"}，6 | 4\_\_{"id":6,"content":""}，空 | 4\_\_{"id":7,"content":""}，空 |
  | 选项6 | 5\_\_{"id":5,"content":""}，6 | 5\_\_{"id":6,"content":""}，空 | 5\_\_{"id":7,"content":""}，空 | 5\_\_{"id":8,"content":""}，空 |
  | 选项7 | 6\_\_{"id":6,"content":""}，空 | 6\_\_{"id":7,"content":""}，空 | 6\_\_{"id":8,"content":""}，空 | / |
  | 选项8 | 7\_\_{"id":7,"content":""}，空 | 7\_\_{"id":8,"content":""}，空 | / | / |
  | 选项9 | 8\_\_{"id":8,"content":""}，空 | / | / | / |

  从分析表可以看到每次点击“选项3”，进行删除后，由于每个数组对象的id不一致，所以从“选项3”往后的每个ListItem的keyGenerator前后都不一致，所以都会重新创建，而不是复用原ListItem组件。
* 方案二：给ForEach的keyGenerator参数传入一个会一直变化的Date.now()。由于当前点击的时间和上一次的时间是不一致的，所以keyGenerator也不会重复，会一直重新创建ListItem。

  ```ts
  class TestItemTwo {
    id: number = 0;
    content: string = '';
  }

  @Entry
  @Component
  struct OptionTwo {
    @State testArray: Array<TestItemTwo> = [];

    // 删除数组项
    changeArray(testArray: Array<TestItemTwo>, index: number): Array<TestItemTwo> {
      if (testArray.length <= 0 || index < 0 || index >= testArray.length) {
        return testArray;
      }
      return testArray.filter((_, i) => i !== index);
    }

    build() {
      Column() {
        Text('测试List复用异常的问题')
          .fontColor(Color.Black)
          .fontSize(18);
        List({ space: 8 }) {
          ForEach(this.testArray, (itemBean: TestItemTwo, index: number) => {
            ListItem() {
              this.builderVoteOpinionView(itemBean, index);
            };
          }, (item: TestItemTwo, index: number) => {
            return index + '__' + JSON.stringify(item) + JSON.stringify(Date.now()); // 为系统默认的返回值增加Date.now()
          });
        }
        .width('90%')
        .enableScrollInteraction(false)
        .scrollBar(BarState.Off)
        .edgeEffect(EdgeEffect.None)
        .margin({ top: 30 });

        // 添加按钮
        Row() {
          Button('添加列表数量');
        }
        .margin({ top: 20 })
        .borderRadius(4)
        .alignItems(VerticalAlign.Center)
        .onClick(() => {
          this.testArray.push(new TestItemTwo());
        });
      }
      .width('100%')
      .backgroundColor(Color.White)
      .alignItems(HorizontalAlign.Center);
    }

    @Builder
    private builderVoteOpinionView(itemBean: TestItemTwo, index: number) {
      Row({ space: 10 }) {
        TextInput({
          text: itemBean.content,
          placeholder: `选项${index + 1}`
        })
          .layoutWeight(1)
          .maxLength(14)
          .onChange((value: string) => {
            itemBean.content = value;
          })
          .defaultFocus(false);
        Text('删除')
          .visibility(index >= 2 ? Visibility.Visible : Visibility.None)
          .onClick(() => {
            this.testArray = this.changeArray(this.testArray, index);
          });
      };
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/84mKBDvzRXmHC8cNG6igiA/zh-cn_image_0000002658791997.png "点击放大")

## 总结

方案一与方案二都可以实现正常且符合预期的刷新操作。注意事项参考如下：

| 方案 | 优点 | 缺点 |
| --- | --- | --- |
| 方案一 | 该方案只会对删除的选项后的ListItem进行刷新，但是对于删除的选项前面的ListItem不会再次创建，比如方案一中的“选项1”、“选项2”，由于不需要重新创建，所以会一直复用之前的ListItem。 | 需要注意传入的数组内的对象id不能与原数组内的对象id重复。 |
| 方案二 | 无需对数组内的对象做差异化处理也可对ForEach进行刷新。 | 由于当前点击的时间和上一次点击的时间是不一致的，导致点击前后的所有keyGenerator都会发生变化，所以会对ForEach内所有的ListItem都会重新创建，特别是当ListItem数量较多时，会产生不必要的内存消耗。 |
