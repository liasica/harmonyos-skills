---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-troubleshooting-0007
title: ArkUI-List组件滑动与展示问题定位
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 故障排查 > ArkUI-List组件滑动与展示问题定位
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:33+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:011af641f38d09056170d9614d5ade2b59a969f7d44fe7f76d82d468fcd54853
---

## List展示不全

### 问题现象

List组件与其他组件同级并且List子组件总尺寸超过List父组件尺寸时，会导致ListItem部分内容顶出父组件显示区域外，上滑至底部时其内容展示不全。问题代码如下：

```ts
@Entry
@Component
struct ListDisplay {
  build() {
    Column() {
      Text('我是一级容器Column的Text组件')
        .fontSize(18)
        .width('100%')
        .height(200)
        .textAlign(TextAlign.Center)
        .backgroundColor('#ffdfe2e2');
      List() {
        ForEach([1, 2, 3, 4, 5, 6, 7], (item: number) => {
          ListItem() {
            Row() {
              Text(item + '').fontSize(18);
            }
            .width('92%')
            .height(200)
            .justifyContent(FlexAlign.Center)
            .backgroundColor('#ffdfe2e2')
            .margin({ top: 16, right: 16, left: 16 })
            .borderRadius(10);
          };
        });
      }.scrollBar(BarState.Off);
    }
    .height('100%')
    .width('100%');
  }
}
```

问题效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/M1t3OSNnRF6Z-w9GkD3lAg/zh-cn_image_0000002764664542.png "点击放大")

### 定位过程

1. 首先观察到List组件未设置高度，根据height属性说明：**height缺省时使用元素自身内容需要的高度**。所以List组件高度为子组件之和200vp\*7。
2. 之后根据官网List指南的[约束](../harmonyos-guides/arkts-layout-development-create-list.md#约束)得知，当子组件主轴方向总尺寸超过List父组件尺寸时，List主轴方向尺寸适应List的父组件尺寸，而200vp\*7>父组件高度100%，所以List组件高度为屏幕高度，示意图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/YehXB_3QTQGck279EJXk-w/zh-cn_image_0000002794183089.png "点击放大")
3. 再然后根据layoutWeight布局说明：**不设置layoutWeight属性或者layoutWeight属性生效值为0的元素优先占位**。所以List组件会在剩余空间内占位，导致List组件被下压，下压后List组件就有部分区域会超过当前屏幕高度，所以造成List展示不全现象。
4. 最后可以利用ArkUI Inspector可以看到List组件超出屏幕范围，超出的距离刚好是上面Text组件占据高度200vp：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/welL1Qs7QGOyi1GwBCocZg/zh-cn_image_0000002794183091.png "点击放大")

### 分析结论

当List组件上面有其他元素并且List子组件高度之和超出屏幕范围时，会导致List组件被下压，造成List展示不全的问题。

### 修改建议

* **方案一：给List组件设置高度。**

  设置固定高度以后List组件就会在限定的范围内滑动，比如设置300vp后List组件就在300vp内进行滑动：

  ```ts
  @Entry
  @Component
  struct ListDisplayOne {
    build() {
      Column() {
        Text('我是一级容器Column的Text组件')
          .fontSize(18)
          .width('100%')
          .height(200)
          .textAlign(TextAlign.Center)
          .backgroundColor('#ffdfe2e2')
        List() {
          ForEach([1, 2, 3, 4, 5, 6, 7], (item: number) => {
            ListItem() {
              Row() {
                Text(item + '').fontSize(18);
              }
              .width('92%')
              .height(200)
              .justifyContent(FlexAlign.Center)
              .backgroundColor('#ffdfe2e2')
              .margin({ top: 16, right: 16, left: 16 })
              .borderRadius(10);
            };
          });
        }.scrollBar(BarState.Off).height(300)
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  **须知** 

  上文300vp只是演示效果，具体数值看业务需要；若height值超过剩余屏幕高度，比如1000vp，则设置无效。

  或者利用calc特性计算List组件在主轴方向剩余高度：

  ```ts
  @Entry
  @Component
  struct ListDisplayTwo {
    build() {
      Column() {
        Text('我是一级容器Column的Text组件')
          .fontSize(18)
          .width('100%')
          .height(200)
          .textAlign(TextAlign.Center)
          .backgroundColor('#ffdfe2e2')
        List() {
          ForEach([1, 2, 3, 4, 5, 6, 7], (item: number) => {
            ListItem() {
              Row() {
                Text(item + '').fontSize(18);
              }
              .width('92%')
              .height(200)
              .justifyContent(FlexAlign.Center)
              .backgroundColor('#ffdfe2e2')
              .margin({ top: 16, right: 16, left: 16 })
              .borderRadius(10);
            };
          });
        }.scrollBar(BarState.Off).height('calc(100% - 200vp)')
      }
      .height('100%')
      .width('100%')
    }
  }
  ```

  **须知** 

  calc公式中200vp的高度为List上面Text组件的高度。

* **方案二：给List组件设置layoutWeight属性。**

  在主轴剩余空间内，设置了layoutWeight属性的子元素与兄弟元素会在主轴方向按照权重分配尺寸。给List组件设置layoutWeight属性即可：

  ```ts
  @Entry
  @Component
  struct ListDisplayThree {
    build() {
      Column() {
        Text('我是一级容器Column的Text组件')
          .fontSize(18)
          .width('100%')
          .height(200)
          .textAlign(TextAlign.Center)
          .backgroundColor('#ffdfe2e2')
        List() {
          ForEach([1, 2, 3, 4, 5, 6, 7], (item: number) => {
            ListItem() {
              Row() {
                Text(item + '').fontSize(18)
              }
              .width('92%')
              .height(200)
              .justifyContent(FlexAlign.Center)
              .backgroundColor('#ffdfe2e2')
              .margin({ top: 16, right: 16, left: 16 })
              .borderRadius(10);
            };
          });
        }.scrollBar(BarState.Off).layoutWeight(1)

      }
      .height('100%')
      .width('100%')
    }
  }
  ```

  **须知** 

  以上场景Text组件后面只有List组件，故layoutWeight设置无论何值都行，不过一般都会设置成layoutWeight(1)。

* **方案三：给List组件设置margin属性。**

  利用ArkUI Inspector可以看到List组件超出屏幕范围，超出的距离刚好是上面Text组件占据高度200vp。而margin属性就是用于设置组件的外边距，所以给List组件设置margin底部200vp即可：

  ```ts
  @Entry
  @Component
  struct ListDisplayFour {
    build() {
      Column() {
        Text('我是一级容器Column的Text组件')
          .fontSize(18)
          .width('100%')
          .height(200)
          .textAlign(TextAlign.Center)
          .backgroundColor('#ffdfe2e2')
        List() {
          ForEach([1, 2, 3, 4, 5, 6, 7], (item: number) => {
            ListItem() {
              Row() {
                Text(item + '').fontSize(18);
              }
              .width('92%')
              .height(200)
              .justifyContent(FlexAlign.Center)
              .backgroundColor('#ffdfe2e2')
              .margin({ top: 16, right: 16, left: 16 })
              .borderRadius(10);
            };
          });
        }.scrollBar(BarState.Off).margin({ bottom: 200 })

      }
      .height('100%')
      .width('100%')
    }
  }
  ```

* **方案四：使用Flex布局。**

  Flex组件提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间，设置FlexWrap.NoWrap即可让子元素尽可能约束在容器内：

  ```ts
  @Entry
  @Component
  struct ListDisplayFive {
    build() {
      Flex({ wrap: FlexWrap.NoWrap, alignItems: ItemAlign.Center, direction: FlexDirection.Column }) {
        Text('我是一级容器Column的Text组件')
          .fontSize(18)
          .width('100%')
          .height(200)
          .textAlign(TextAlign.Center)
          .backgroundColor('#ffdfe2e2')
        List() {
          ForEach([1, 2, 3, 4, 5, 6, 7], (item: number) => {
            ListItem() {
              Row() {
                Text(item + '').fontSize(18)
              }
              .width('92%')
              .height(200)
              .justifyContent(FlexAlign.Center)
              .backgroundColor('#ffdfe2e2')
              .margin({ top: 16, right: 16, left: 16 })
              .borderRadius(10);
            };
          });
        }.scrollBar(BarState.Off);
      }
      .height('100%')
      .width('100%')
    }
  }
  ```
* **方案五：给List组件设置contentEndOffset属性。**

  设置内容区域末尾偏移量。

  ```ts
  @Entry
  @Component
  struct ListDisplaySix {
    build() {
      Column() {
        Text('我是一级容器Column的Text组件')
          .fontSize(18)
          .width('100%')
          .height(200)
          .textAlign(TextAlign.Center)
          .backgroundColor('#ffdfe2e2')
        List() {
          ForEach([1, 2, 3, 4, 5, 6, 7], (item: number) => {
            ListItem() {
              Row() {
                Text(item + '').fontSize(18)
              }
              .width('92%')
              .height(200)
              .justifyContent(FlexAlign.Center)
              .backgroundColor('#ffdfe2e2')
              .margin({ top: 16, right: 16, left: 16 })
              .borderRadius(10);
            };
          });
        }.scrollBar(BarState.Off).contentStartOffset(0).contentEndOffset(200)
      }
      .height('100%')
      .width('100%')
    }
  }
  ```

  以上方案均可修复List展示不全问题，修正效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/_mMmw6KRTSCFpycfAGnx8g/zh-cn_image_0000002764665048.png "点击放大")

## 滑动组件出现不规则分隔线

### 问题现象

在滑动组件中，会出现不规则分隔线的情况，例如Grid组件：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/MwScicXISMGdLiLEEBtbjA/zh-cn_image_0000002764826882.png)

或者List组件：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/vmIvDmbOQvKeEKee6a-1qA/zh-cn_image_0000002764666958.png "点击放大")

以List列表为例，其中ListItem的height属性交替设置成162lpx以及163lpx，滚动时会出现闪烁的分隔线。问题代码如下：

```ts
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

### 定位过程

通过分析List例子问题代码，发现由于162lpx和163lpx的高度不同，并且lpx单位为实际屏幕宽度与逻辑宽度的比值，导致某些像素在滚动时无法正确对齐，再加上没有设置适当的对齐方式，从而在ListItem子组件之间产生分隔线，并且随着列表的滑动产生视觉上的闪烁。

### 分析结论

当List组件的子组件ListItem之间的高度不同并且没有设置适当的对齐方式时，子组件之间就会产生间隙，即分隔线，并且伴随着列表的滑动形成分隔线闪烁的情况。

### 修改建议

* **方案一：设置autoDesignWidth属性。**

  在resources/base/profile/main\_pages.json中添加属性autoDesignWidth，并将其设置为true，即可标识页面设计基准宽度允许自动计算，List组件就能够根据设备的屏幕密度和宽度来调整布局，在不同的环境里保持一致的视觉效果。

  修正效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/jgrHrWbORWuMG-MRog9zuw/zh-cn_image_0000002764827004.png "点击放大")

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/De9AMsEFQGWXsAfaBvGQVA/zh-cn_image_0000002764667102.png "点击放大")
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

## 滚动条组件ScrollBar滑动时出现跳动

### 问题现象

滚动条ScrollBar配合List，通过懒加载实现子组件ListItem按需加载。但是滑动ScrollBar时，若持续加载ListItem，ScrollBar组件滑动距离会骤变。问题现象图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/hRU5gJBmTk60106m_F_Bwg/zh-cn_image_0000002764828308.png "点击放大")

问题代码如下：

```ts
export class MyDataSource implements IDataSource {
  private dataArray: HSFileItemForOperation[] = [];
  private listeners: DataChangeListener[] = [];

  public pushInitData(dataArray: HSFileItemForOperation[]) {
    for (let i = 0; i < dataArray.length; i++) {
      this.dataArray.push(dataArray[i]);
    }

    this.notifyDataReload();
  }

  public getData(index: number): HSFileItemForOperation {
    return this.dataArray[index];
  }

  // 数据源的数据总量
  public totalCount(): number {
    return this.dataArray.length;
  }

  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    });
  }

  registerDataChangeListener(): void {
  }

  unregisterDataChangeListener(): void {
  }
}

@Observed
export class HSFileItemForOperation implements IDataSource {
  private dataArray: number[] = [];

  public pushData(dataArray: number[]) {
    for (let i = 0; i < dataArray.length; i++) {
      this.dataArray.push(dataArray[i]);
    }
  }

  constructor(dataArray: number[]) {
    this.dataArray = dataArray;
  }

  // 返回指定索引位置的数据
  public getData(index: number): number {
    return this.dataArray[index];
  }

  // 数据源的数据总量
  public totalCount(): number {
    return this.dataArray.length;
  }

  registerDataChangeListener(): void {
  }

  unregisterDataChangeListener(): void {
  }
}

// 模拟数据
export const FILEITEM_LIST: HSFileItemForOperation[] = [
  new HSFileItemForOperation([
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
  ]),
  new HSFileItemForOperation([
    21, 22, 23,
    24, 25, 26, 27, 28,
    29, 30
  ]),
  new HSFileItemForOperation([
    31, 32, 33, 34, 35, 36, 37
  ]),
  new HSFileItemForOperation(
    [38, 39,])
];

@Entry
@Component
struct Page {
  private scroller: Scroller = new Scroller();

  build() {
    Column() {
      Stack() {
        Scroll(this.scroller) {
          Column() {
            TabsView();
          };
        }
        .width('100%')
        .height('100%')
        .scrollable(ScrollDirection.Vertical)
        .scrollBar(BarState.Off)
        .edgeEffect(EdgeEffect.None);
      }
      .width('100%')
      .height('100%')
      .alignContent(Alignment.Top);
    };
  }
}

@Component
export struct TabsView {
  private tabController: TabsController = new TabsController();
  private groups: MyDataSource = new MyDataSource();
  private scroller: Scroller = new Scroller();

  aboutToAppear(): void {
    this.groups.pushInitData(FILEITEM_LIST);
  }

  build() {
    Tabs({ controller: this.tabController }) {
      TabContent() {
        Stack({ alignContent: Alignment.End }) {
          List({ scroller: this.scroller }) {
            LazyForEach(this.groups, (headItem: HSFileItemForOperation, index: number) => {
              ReusableListGroupComponent({
                group: headItem,
                index: index
              });
            }, (headItem: number) => headItem.toString() + Math.random() * 10);
          }
          .width('100%')
          .height('100%')
          .lanes(4)
          .sticky(StickyStyle.Header)
          .backgroundColor(Color.White)
          .nestedScroll({
            scrollForward: NestedScrollMode.PARENT_FIRST,
            scrollBackward: NestedScrollMode.SELF_FIRST
          })
          .edgeEffect(EdgeEffect.None)
          .scrollBar(BarState.Off);

          ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical, state: BarState.Auto }) {
            Stack() {
              Image($r('app.media.startIcon'))
                .width(40);
            };
          }
          .backgroundColor(0xF1F3F5)
          .hitTestBehavior(HitTestMode.Transparent);
        };
      }.tabBar('test');
    };
  }
}

@Component
struct ReusableListGroupComponent {
  @ObjectLink group: HSFileItemForOperation;
  @Prop index: number;

  @Builder
  itemHead(text: string) {
    Text(text)
      .fontSize(20)
      .margin(10)
      .backgroundColor(0xAABBCC)
      .width('100%')
      .padding(10);
  }

  build() {
    ListItemGroup({ header: this.itemHead('group' + this.index.toString()) }) {
      LazyForEach(this.group, (item: number, index: number) => {
        ListItem() {
          // 使用可复用自定义组件
          ReusableChildComponent({ item: item })
            .onAppear(() => {
              console.info('ReusableChildComponent', index);
            });
        };
      }, (item: number) => item.toString() + Math.random());
    };
  }
}

@Reusable
@Component
struct ReusableChildComponent {
  @State item: number = 0;

  aboutToReuse(params: Record<string, number>) {
    this.item = params.item;
  }

  build() {
    Column() {
      Image($r('app.media.startIcon'))
        .padding(15)
        .objectFit(ImageFit.Fill)
        .layoutWeight(1);
      Text(`图片${this.item}`)
        .fontSize(16)
        .textAlign(TextAlign.Center);
    }
    .width('100%')
    .height(120)
    .backgroundColor(0xF9CF93);
  }
}
```

### 定位过程

排查是否使用LazyForEach懒加载遍历：在懒加载场景，ListItemGroup内容高度不同的场景下，ScrollBar组件需要获取ListItemGroup的高度。

### 分析结论

分组遍历的ListItemGroup内容高度不同的情况下，使用LazyForEach无法获取确定子组件的高度。

### 修改建议

可以使用childrenMainSize接口提前设置ListItemGroup内容的高度。

* 页面加载前使用[ChildrenMainSize](../harmonyos-references/ts-container-scrollable-common.md#childrenmainsize12对象说明)对象提供的splice方法批量增删改子组件在主轴方向的大小信息。

  ```ts
  aboutToAppear(): void {
      // splice方法批量增删改子组件在主轴方向的大小信息。
      let childrenSize: Array<number> = [];
      LIST_DATA.forEach((data: GroupItemSource) => {
        childrenSize.push(Math.ceil(data.dataArray.length / 4) * this.listItemHeight + this.groupHeaderHeight);
      });
      this.childrenSize.splice(0, 3, childrenSize);
      this.groups.pushInitData(LIST_DATA);
    }
  ```

  示例代码如下：

  ```ts
  // 自定义数据源
  export class MyDataSource implements IDataSource {
    dataArray: GroupItemSource[] = [];
    private listeners: DataChangeListener[] = [];

    public pushInitData(dataArray: GroupItemSource[]) {
      for (let i = 0; i < dataArray.length; i++) {
        this.dataArray.push(dataArray[i]);
      }
      this.notifyDataReload();
    }

    public getData(index: number): GroupItemSource {
      return this.dataArray[index];
    }

    // 数据源的数据总量
    public totalCount(): number {
      return this.dataArray.length;
    }

    notifyDataReload(): void {
      this.listeners.forEach(listener => {
        listener.onDataReloaded();
      });
    }

    registerDataChangeListener(): void {
    }

    unregisterDataChangeListener(): void {
    }
  }

  @Observed
  export class GroupItemSource implements IDataSource {
    dataArray: number[] = [];

    public pushData(dataArray: number[]) {
      for (let i = 0; i < dataArray.length; i++) {
        this.dataArray.push(dataArray[i]);
      }
    }

    constructor(dataArray: number[]) {
      this.dataArray = dataArray;
    }

    // 返回指定索引位置的数据
    public getData(index: number): number {
      return this.dataArray[index];
    }

    // 数据源的数据总量
    public totalCount(): number {
      return this.dataArray.length;
    }

    registerDataChangeListener(): void {
    }

    unregisterDataChangeListener(): void {
    }
  }

  // 模拟List数据
  export const LIST_DATA: GroupItemSource[] = [
    new GroupItemSource([
      0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    ]),
    new GroupItemSource([
      21, 22, 23,
      24, 25, 26, 27, 28,
      29, 30
    ]),
    new GroupItemSource([
      31, 32, 33, 34, 35, 36, 37
    ]),
    new GroupItemSource(
      [38, 39,])
  ];

  @Entry
  @Component
  struct Page {
    private scroller: Scroller = new Scroller();

    build() {
      Column() {
        Stack() {
          Scroll(this.scroller) {
            Column() {
              TabsView();
            };
          }
          .width('100%')
          .height('100%')
          .scrollable(ScrollDirection.Vertical)
          .scrollBar(BarState.Off)
          .edgeEffect(EdgeEffect.None);
        }
        .width('100%')
        .height('100%')
        .alignContent(Alignment.Top);
      }.margin({ left: 8, right: 8 });
    }
  }

  @Component
  export struct TabsView {
    private tabController: TabsController = new TabsController();
    private groups: MyDataSource = new MyDataSource();
    private scroller: Scroller = new Scroller();
    private listItemHeight: number = 120; // listItem子组件高度
    private groupHeaderHeight: number = 40; // groupHeader高度
    private columns: number = 4; // 列数
    @State childrenSize: ChildrenMainSize = new ChildrenMainSize(this.listItemHeight);

    aboutToAppear(): void {
      // splice方法批量增删改子组件在主轴方向的大小信息。
      let childrenSize: Array<number> = [];
      LIST_DATA.forEach((data: GroupItemSource) => {
        childrenSize.push(Math.ceil(data.dataArray.length / 4) * this.listItemHeight + this.groupHeaderHeight);
      });
      this.childrenSize.splice(0, 3, childrenSize);
      this.groups.pushInitData(LIST_DATA);
    }

    build() {
      Tabs({ controller: this.tabController }) {
        TabContent() {
          Stack({ alignContent: Alignment.End }) {
            List({ scroller: this.scroller }) {
              LazyForEach(this.groups, (headItem: GroupItemSource, index: number) => {
                ReusableListGroupComponent({
                  group: headItem,
                  index: index
                });
              });
            }
            .childrenMainSize(this.childrenSize)
            .width('100%')
            .height('100%')
            .lanes(this.columns)
            .sticky(StickyStyle.Header)
            .backgroundColor(Color.White)
            .nestedScroll({
              scrollForward: NestedScrollMode.PARENT_FIRST,
              scrollBackward: NestedScrollMode.SELF_FIRST
            })
            .edgeEffect(EdgeEffect.None)
            .scrollBar(BarState.Off);

            ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical, state: BarState.Auto }) {
              Stack() {
                // 此处'app.media.startIcon'仅作示例
                Image($r('app.media.startIcon'))
                  .width(40)
                  .aspectRatio(1);
              };
            }
            .backgroundColor(Color.Blue)
            .hitTestBehavior(HitTestMode.Transparent);
          };
        }.tabBar('test');
      };
    }
  }

  @Component
  struct ReusableListGroupComponent {
    @ObjectLink group: GroupItemSource;
    @Prop index: number;
    @State childrenSize: ChildrenMainSize = new ChildrenMainSize(120); // 设置ListItemGroup组件的子组件在主轴方向的大小信息
    private groupHeaderHeight: number = 40;

    @Builder
    itemHead(text: string) {
      Text(text)
        .fontSize(20)
        .backgroundColor(0xAABBCC)
        .width('100%')
        .height(this.groupHeaderHeight);
    }

    build() {
      ListItemGroup({ header: this.itemHead('group' + this.index.toString()) }) {
        LazyForEach(this.group, (item: number, index: number) => {
          ListItem() {
            // 使用可复用自定义组件
            ReusableChildComponent({ item: item })
              .onAppear(() => {
                console.info(`ReusableChildComponent:\n${index}`);
              });
          };
        });
      }
      .childrenMainSize(this.childrenSize);
    }
  }

  @Reusable
  @Component
  struct ReusableChildComponent {
    @State item: number = 0;
    private listItemHeight: number = 120;

    aboutToReuse(params: Record<string, number>) {
      this.item = params.item;
    }

    build() {
      Column() {
        // 此处'app.media.startIcon'仅作示例
        Image($r('app.media.startIcon'))
          .padding(5)
          .objectFit(ImageFit.Fill)
          .layoutWeight(1);
        Text(`图片${this.item}`)
          .fontSize(16)
          .textAlign(TextAlign.Center);
      }
      .width('100%')
      .height(this.listItemHeight)
      .backgroundColor(0xF1F3F5);
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/F73Jm0S5TGa0aGHNpoIdmA/zh-cn_image_0000002764829338.png "点击放大")
