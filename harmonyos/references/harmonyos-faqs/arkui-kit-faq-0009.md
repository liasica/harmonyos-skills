---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-faq-0009
title: ArkUI-List组件布局与渲染常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 常见问题 > ArkUI-List组件布局与渲染常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:33+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:a53e86dae3eb7ebcf87bf61edd7a1ee650ec5591cddfe9591148beac1f5d7634
---

**Q：如何实现每列Item的文字水平居中？问题展示：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/8UEuK7DwQPKKWF-jDKG7LQ/zh-cn_image_0000002764472192.png)

**A**：当List组件设置listDirection(Axis.Horizontal)和lanes(2)时，内部的ListItem自身会均匀分配父List的高度，只可以设置每个ListItem垂直方向的位置；而此时ListItem宽度由自适应撑开，故无法设置每列Item的水平居中，因此需要给ListItem一个固定宽度，在每个ListItem同宽的情况下设置子组件的水平方向位置。代码如下：

```ts
@Entry
@Component
export struct TwoLine {
  @State array?: Array<string> = new Array;

  aboutToAppear(): void {
    this.array?.push('一个栏目');
    this.array?.push('测试');
    this.array?.push('哈哈哈哈哈');
    this.array?.push('对对');
    this.array?.push('好吧好');
    this.array?.push('行行行行行');
    this.array?.push('对对对');
    this.array?.push('是吗');
    this.array?.push('栏目编辑');
  }

  build() {
    Column() {
      List({ space: 10 }) {
        ForEach(this.array, (item: string) => {
          ListItem() {
            Column() {
              Text(item)
                .height(20)
                .backgroundColor(Color.White)
                .textAlign(TextAlign.Center)
                .align(Alignment.Center)
                .alignSelf(ItemAlign.Center)
                .constraintSize({ minWidth: 30 })
            }
            .width("24%") // 设置width固定时可以实现水平居中，不设置时listItem宽度由内容撑开，无法设置居中。
            .height('100%')
            .justifyContent(FlexAlign.Center)
            .backgroundColor(Color.Blue)
          }
          .margin({ bottom: 10 })
        });
      }
      .width('100%')
      .height(70)
      .lanes(2)
      .listDirection(Axis.Horizontal)
      .backgroundColor('#87ceeb')
      .alignListItem(ListItemAlign.Center)

      Text('如何实现每列文字的水平居中？')
        .margin({ top: 100 })
        .fontSize(20)
    }
    .padding(10)
  }
}
```

代码运行结果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/t3zIKNzpTfyTDbu_czd00g/zh-cn_image_0000002793791337.png "点击放大")

**Q：在同一行中有多个ListItem时，ListItem中显示的文本高度不一致，导致各ListItem高度不一致，由于文本的长度不确定，无法通过设置height属性来固定ListItem的高度。问题图预览：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/Jt5Rk6yoS4KJIVepiRPToA/zh-cn_image_0000002793791951.png "点击放大")

**A**：方案一：使用Flex容器组件，修改FlexOptions的wrap和alignItems的参数，实现多行多列显示，且子组件在交叉轴方向拉伸填充。示例代码如下：

```ts
import { LengthUnit } from '@kit.ArkUI';

export class Area {
  name: string = '';
  heightSize: number = 0;

  constructor(name: string) {
    this.name = name;
  }
}

const ARR: Area[] = [
  new Area('铜梁区'), new Area('潼南区'), new Area('荣昌区'), new Area('开州区'), new Area('梁平区'),
  new Area('石柱土家族自治县'),
  new Area('秀山土家族苗族自治县kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'),
  new Area('酉阳土家族苗族自治县'), new Area('彭水苗族土家族自治县'),
  new Area('铜梁区'), new Area('潼南区'), new Area('荣昌区'), new Area('开州区'), new Area('梁平区'),
  new Area('石柱土家族自治县'),
  new Area('秀山土家族苗族自治县kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'),
  new Area('酉阳土家族苗族自治县'), new Area('彭水苗族土家族自治县'),
  new Area('铜梁区'), new Area('潼南区'), new Area('荣昌区'), new Area('开州区'), new Area('梁平区'),
  new Area('石柱土家族自治县'),
  new Area('秀山土家族苗族自治县kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'),
  new Area('酉阳土家族苗族自治县'), new Area('彭水苗族土家族自治县'),
];

// 元素子组件
@Component
struct TextComponentOne {
  content: string = '';

  build() {
    Column() {
      Text(this.content)
        .fontSize(14)
        .padding(9)
        .width(this.content.length >= 9 ? '100%' : null)
        .textAlign(this.content.length >= 9 ? TextAlign.Start : TextAlign.Center);
    };
  }
}

@Entry
@Component
struct Index {
  private arr: Area[] = ARR;

  build() {
    Scroll() {
      Flex({
        justifyContent: FlexAlign.Center,
        wrap: FlexWrap.Wrap, // Flex容器的元素多行/列排布
        alignItems: ItemAlign.Stretch, // 元素在Flex容器中，交叉轴方向拉伸填充
        space: {
          cross: { value: 0, unit: LengthUnit.VP }
        }
      }) {
        ForEach(this.arr, (item: Area) => {
          Column() {
            TextComponentOne({ content: item.name });
          }
          // 格式、宽度、圆角等属性需在Flex元素设置，若设置在元素子组件内，交叉轴防线拉伸填充可能不生效
          .justifyContent(item.name.length >= 9 ? FlexAlign.Start : FlexAlign.Center)
          .width('30%')
          .border({ width: 0, radius: 7 })
          .backgroundColor('#ffe5e5e5')
          .margin({
            bottom: 5,
            top: 5,
            right: 3,
            left: 3
          });
        });
      };
    }
    .width('100%');
  }
}
```

修正效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/p_MLpMsmSY6AnsR0xeuzVg/zh-cn_image_0000002764473744.png "点击放大")

方案二：通过onAreaChange获取各ListItem高度并判断行内最大高度，通过状态变量变化和if/else条件语句，刷新页面布局，将组件高度设置为行内最大高度。

1. 计算每个ListItem的高度，并判断同一行中所有ListItem的最大高度。

   ```ts
   // 判断行内高度的最大值，并将arr中的元素的高度设置为高度最大值
     reSetHeightSize() {
       for (let i = 0; i < this.arr.length; i += 3) {
         let arrTmp: number[] = [];
         arrTmp.push(this.arr[i].heightSize);
         arrTmp.push(this.arr[i + 1].heightSize);
         arrTmp.push(this.arr[i + 2].heightSize);
         arrTmp.sort((a, b) => a - b);
         let maxHeight = Math.max(...arrTmp);
         this.arr[i].heightSize = maxHeight;
         this.arr[i + 1].heightSize = maxHeight;
         this.arr[i + 2].heightSize = maxHeight;
       }
     }
   ```
2. 首次布局时，通过onAreaChange收集并计算ListItem高度。

   ```ts
   @Builder
     ListItemChangeRegion() {
       List({ space: 8 }) {
         ForEach(this.arr, (item: RegionOne, index: number) => {
           ListItem() {
             TextComponentTwo({ content: item.name })
               .onAreaChange((oldValue: Area, newValue: Area) => {
                 // 遍历全部ListItem并收集高度后，调用reSetHeightSize方法计算各行的最大高度，并再完成遍历后改变状态变量isBoolean的值，UI渲染改变
                 this.arr[index].heightSize = newValue.height as number;
                 if (this.flags === this.arr.length - 1) {
                   this.isBoolean = false;
                   this.reSetHeightSize();
                 }
                 this.flags += 1;
                 console.info(`Ace: on area change, oldValue is ${JSON.stringify(oldValue)} value is ${JSON.stringify(newValue)}`);
               });
           };
         });
       }
       .lanes(3);
     }
   ```
3. 二次布局时，设置组件高度为行内最大高度。

   ```ts
   @Builder
     ListItemSameHeight() {
       List({ space: 8 }) {
         ForEach(this.arr, (item: RegionOne, index: number) => {
           ListItem() {
             TextComponentTwo({ content: item.name, hgt: item.heightSize, index: index });
           };
         }, (item: RegionOne) => JSON.stringify(item));
       }
       .lanes(3);
     }
   ```
4. 使用条件语句if和状态变量isBoolean，通过判断状态变量的值的变化，重新对布局进行刷新。

   ```ts
   if (this.isBoolean) {
           // 首次布局，组件区域变化触发onRegionOneChange回调，收集并计算ListItem高度
           this.ListItemChangeRegion();
         } else {
           // isBoolean值发生改变，重新布局进入else语句，此时，各ListItem的高度已是行内的最大高度值
           this.ListItemSameHeight();
         }
   ```

完整示例代码如下：

```ts
class RegionOne {
  name: string = '';
  heightSize: number = 0;

  constructor(name: string) {
    this.name = name;
  }
}

const ARR: RegionOne[] = [
  new RegionOne('铜梁区'), new RegionOne('潼南区'), new RegionOne('荣昌区'), new RegionOne('开州区'),
  new RegionOne('梁平区'),
  new RegionOne('石柱土家族自治县'),
  new RegionOne('秀山土家族苗族自治县kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'),
  new RegionOne('酉阳土家族苗族自治县'), new RegionOne('彭水苗族土家族自治县'),
  new RegionOne('铜梁区'), new RegionOne('潼南区'), new RegionOne('荣昌区'), new RegionOne('开州区'),
  new RegionOne('梁平区'),
  new RegionOne('石柱土家族自治县'),
  new RegionOne('秀山土家族苗族自治县kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'),
  new RegionOne('酉阳土家族苗族自治县'), new RegionOne('彭水苗族土家族自治县'),
  new RegionOne('铜梁区'), new RegionOne('潼南区'), new RegionOne('荣昌区'), new RegionOne('开州区'),
  new RegionOne('梁平区'),
  new RegionOne('石柱土家族自治县'),
  new RegionOne('秀山土家族苗族自治县kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'),
  new RegionOne('酉阳土家族苗族自治县'), new RegionOne('彭水苗族土家族自治县'),
];

// 元素子组件
@Component
struct TextComponentTwo {
  content: string = '';
  hgt: Length = 'auto';
  index: number = 0;

  build() {
    Column() {
      Text(this.content)
        .zIndex(this.index)
        .fontSize(14)
        .padding(9)
        .width(115)
        .textAlign(this.content.length >= 9 ? TextAlign.Start : TextAlign.Center);
    }
    .height(this.hgt)
    .backgroundColor('#ffe5e5e5')
    .justifyContent(this.content.length >= 9 ? FlexAlign.Start : FlexAlign.Center)
    .border({
      width: 0,
      radius: 7
    });
  }
}

@Entry
@Component
struct Page {
  private arr: RegionOne[] = ARR;
  private flags: number = 0;
  @State private isBoolean: boolean = true;

  // 判断行内高度的最大值，并将arr中的元素的高度设置为高度最大值
  reSetHeightSize() {
    for (let i = 0; i < this.arr.length; i += 3) {
      let arrTmp: number[] = [];
      arrTmp.push(this.arr[i].heightSize);
      arrTmp.push(this.arr[i + 1].heightSize);
      arrTmp.push(this.arr[i + 2].heightSize);
      arrTmp.sort((a, b) => a - b);
      let maxHeight = Math.max(...arrTmp);
      this.arr[i].heightSize = maxHeight;
      this.arr[i + 1].heightSize = maxHeight;
      this.arr[i + 2].heightSize = maxHeight;
    }
  }
  @Builder
  ListItemChangeRegion() {
    List({ space: 8 }) {
      ForEach(this.arr, (item: RegionOne, index: number) => {
        ListItem() {
          TextComponentTwo({ content: item.name })
            .onAreaChange((oldValue: Area, newValue: Area) => {
              // 遍历全部ListItem并收集高度后，调用reSetHeightSize方法计算各行的最大高度，并再完成遍历后改变状态变量isBoolean的值，UI渲染改变
              this.arr[index].heightSize = newValue.height as number;
              if (this.flags === this.arr.length - 1) {
                this.isBoolean = false;
                this.reSetHeightSize();
              }
              this.flags += 1;
              console.info(`Ace: on area change, oldValue is ${JSON.stringify(oldValue)} value is ${JSON.stringify(newValue)}`);
            });
        };
      });
    }
    .lanes(3);
  }
  @Builder
  ListItemSameHeight() {
    List({ space: 8 }) {
      ForEach(this.arr, (item: RegionOne, index: number) => {
        ListItem() {
          TextComponentTwo({ content: item.name, hgt: item.heightSize, index: index });
        };
      }, (item: RegionOne) => JSON.stringify(item));
    }
    .lanes(3);
  }
  build() {
    Column() {
      if (this.isBoolean) {
        // 首次布局，组件区域变化触发onRegionOneChange回调，收集并计算ListItem高度
        this.ListItemChangeRegion();
      } else {
        // isBoolean值发生改变，重新布局进入else语句，此时，各ListItem的高度已是行内的最大高度值
        this.ListItemSameHeight();
      }
      }
    .width('100%')
    .height('100%')
    .padding({ top: 5, left: 12, right: 6 });
  }
}
```

修正效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/qnC0CfsrTJmYyFhvrJfj3g/zh-cn_image_0000002793793197.png "点击放大")

**Q：列表如何实现树视图折叠交互，并支持展开/折叠父项查看子项？示例图如下：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/4aCA5f35RGOcvH6XBM4gJQ/zh-cn_image_0000002764474434.png "点击放大")

**A**：方案一：

1. 通过List与ListItem搭建标准化垂直列表架构，每个列表项均作为独立单元参与布局。
2. 借助[Column](../harmonyos-references/ts-container-column.md)实现列表项内的纵向层级堆叠。

   ```ts
   @Entry
   @Component
   struct ListTest {
     private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
     @State isContentShow: boolean = true;
     @State selectItem: number = 0;
     uiContext: UIContext | undefined = undefined;

     aboutToAppear() {
       this.uiContext = this.getUIContext();
       if (!this.uiContext) {
         console.warn('no uiContext');
         return;
       }
     }

     build() {
       Column() {
         List({ initialIndex: 0 }) {
           ForEach(this.arr, (item: number, index: number) => {
             ListItem() {
               Column() {
                 Row() {
                   Text(item.toString());
                   Button(this.isContentShow && this.selectItem === item ? '收起' : '展开')
                     .onClick(() => {
                       console.info('index', index);
                       this.uiContext?.animateTo({
                         duration: 300,
                         onFinish: () => {
                           console.info('animation end');
                         }
                       }, () => {
                         this.isContentShow = !this.isContentShow;
                         this.selectItem = item;
                       });
                     });
                 }
                 .width('100%')
                 .justifyContent(FlexAlign.SpaceBetween);

                 if (this.isContentShow && this.selectItem === item) {
                   Text('这是内容区域')
                     .backgroundColor(Color.Gray)
                     .width('100%')
                     .height(100);
                 }
               }
               .backgroundColor(0xFFFFFF)
               .width('100%')
               .padding({
                 top: 12,
                 bottom: 12
               })
               .margin({ top: 10 });
             };
           }, (item: string) => item.toString());
         }
         .scrollBar(BarState.Off)
         .height('100%')
         .width('100%');
       }
       .backgroundColor(0xF1F3F5)
       .padding(12);
     }
   }
   ```

   效果图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/Ula5mNEmQVCDrzON0POkMw/zh-cn_image_0000002793713461.png "点击放大")

方案二：

参考[TreeView](../harmonyos-references/ohos-arkui-advanced-treeview.md)，作为一种分层显示的列表，适合显示嵌套结构。拥有父列表项和子列表项，可展开或折叠。示例代码如下：

```ts
import { TreeController, TreeView } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private treeController: TreeController = new TreeController();
  clickId: number = 0;

  aboutToAppear(): void {
    this.treeController
      .addNode({
        parentNodeId: -1,
        currentNodeId: 1,
        isFolder: true,
        primaryTitle: '目录1',
        secondaryTitle: '2'
      })
      .addNode({
        parentNodeId: 1,
        currentNodeId: 2,
        isFolder: false,
        primaryTitle: '项目1_1'
      })
      .addNode({
        parentNodeId: 1,
        currentNodeId: 3,
        isFolder: false,
        primaryTitle: '项目1_2'
      })
      .addNode({
        parentNodeId: -1,
        currentNodeId: 24,
        isFolder: false,
        primaryTitle: '项目2'
      })
      .addNode({
        parentNodeId: -1,
        currentNodeId: 32,
        isFolder: true,
        primaryTitle: '目录3',
        secondaryTitle: '0'
      })
      .addNode({
        parentNodeId: 32,
        currentNodeId: 35,
        isFolder: true,
        primaryTitle: '目录3-1',
        secondaryTitle: '0'
      })
      .addNode({
        parentNodeId: -1,
        currentNodeId: 33,
        isFolder: true,
        primaryTitle: '目录4',
        secondaryTitle: '0'
      })
      .addNode({
        parentNodeId: 33,
        currentNodeId: 34,
        isFolder: false,
        primaryTitle: '项目5'
      })
      .buildDone();
    this.treeController.refreshNode(-1, '父节点', '子节点');
  }

  build() {
    Column() {
      SideBarContainer(SideBarContainerType.Embed) {
        TreeView({ treeController: this.treeController });
      }
      .sideBarWidth('100%')
      .focusable(true)
      .showControlButton(false)
      .showSideBar(true);
    };
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/TtMqzwyPS4exQ__0vADkeg/zh-cn_image_0000002764475246.png "点击放大")

**Q：如何使用List嵌套Grid实现内容分类展示效果？如何实现这种组合布局？**

A：实现步骤如下：

1. ListGridDemo.ets：
   * 定义状态变量curIndex用于跟踪当前选中的标签索引，以及tabItem数组用于存储各个分类的名称。
   * 实现tabBuilder方法，用于构建每个标签的样式，即选中时的字体变化。
   * ForEach循环遍历tabItem数组，为每个标签创建TabContent。每个TabContent内部是一个Scroll组件，里面嵌入ItemsPageView组件，并传递tabBarIndex参数。

   示例代码如下：

   ```ts
   import { ItemsPageView } from './ItemsPageView';

   @Entry
   @Component
   struct ListGridDemo {
     @State curIndex: number = 0;
     @State tabItem: Array<string> =
       ['全部', '咨询', '医生', '经络', '膳食', '茶饮', '运动', '足浴'];

     @Builder
     tabBuilder(index: number, name: string) {
       Column() {
         Text(name)
           .fontSize(this.curIndex === index ? 20 : 16)
           .fontColor(Color.Black)
           .fontWeight(this.curIndex === index ? FontWeight.Bold : FontWeight.Normal)
           .id(index.toString())
           .margin({ bottom: 10 });
       }
       .margin({ left: 10, right: 10 })
       .width(this.curIndex === index ? name.length * 20 : name.length * 16)
       .alignItems(HorizontalAlign.Center)
       .justifyContent(FlexAlign.Center)
       .height(56);
     }

     build() {
       Column() {
         Stack({ alignContent: Alignment.TopStart }) {
           Column() {
             Tabs({ index: this.curIndex, barPosition: BarPosition.Start }) {
               ForEach(this.tabItem, (item: string, index: number) => {
                 TabContent() {
                   Scroll() {
                     Column() {
                       ItemsPageView({ tabBarIndex: this.curIndex }).expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END]);
                     }.expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END]) ;
                   }.expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END]);
                 }.expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END])
                 .tabBar(this.tabBuilder(index, item));
               });
             }.expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END])
             .onTabBarClick((index: number) => {
               this.curIndex = index;
             })
             .onChange((index: number) => {
               this.curIndex = index;
             })
             .layoutWeight(1)
             .barOverlap(false)
             .barMode(BarMode.Scrollable)
             .barHeight(56);
           }.expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END]);
         }.expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END])
         .height('100%')
         .width('100%');
       }.backgroundColor(Color.White).expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END]);
     }
   }
   ```
2. ItemsPageView.ets：
   * 定义两个数据模型gridItems和listItems，分别用于网格和列表布局。
   * 使用ListItemAdapter管理数据，在aboutToAppear方法中将gridItems和listItems添加到Adapter中。
   * 使用LazyForEach遍历Adapter中的每个数据项，根据itemType字段决定渲染ListComponent还是GridComponent。

   示例代码如下：

   ```ts
   import { ListItemAdapter } from './ListItemAdapter';

   @Component
   export struct ItemsPageView {
     @Prop tabBarIndex: number;
     @State private adapter: ListItemAdapter<DataModel> = new ListItemAdapter();
     gridItems: DataModel = {
       itemType: ItemType.gridItems,
       'result': [
         {
           'name': 'grid_1',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'grid_2',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'grid_3',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'grid_4',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         }
       ]
     };
     listItems: DataModel = {
       itemType: ItemType.listItems,
       'result': [
         {
           'name': 'list_1',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'list_2',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'list_3',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'list_4',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'list_5',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'list_6',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'list_7',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         },
         {
           'name': 'list_8',
           'icon': 'resources/base/media/startIcon.png' // 仅供参考，根据实际情况调整。
         }
       ]
     };

     aboutToAppear(): void {
       let tmp: DataModel[] = [];
       tmp.push(this.listItems);
       tmp.push(this.gridItems);
       this.adapter.addList(tmp);
     }

     build() {
       Column() {
         // 使用LazyForEach遍历adapter中的数据，并根据itemType决定渲染列表还是网格
         LazyForEach(this.adapter, (item: DataModel) => {
           if (item.itemType === ItemType.listItems) {
             ListComponent({ listItemData: item.result });
           } else if (item.itemType === ItemType.gridItems) {
             GridComponent({ gridItemData: item.result });
           }
         });
       }.expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM,SafeAreaEdge.END])
       .height('auto')
       .padding(10);
     }
   }

   export interface Grids {
     icon?: Resource;
     name: string;
   }

   @Component
   export struct GridComponent {
     gridAdapter: ListItemAdapter<Grids> = new ListItemAdapter();
     gridItemData: Array<Grids> = [];

     aboutToAppear(): void {
       this.gridAdapter.addList(this.gridItemData);
     }

     build() {
       Grid() {
         LazyForEach(this.gridAdapter, (item: Grids) => {
           GridItem() {
             Column() {
               Text(item.name)
                 .textAlign(TextAlign.Center)
                 .width('100%')
                 .height('50%');
             }
           }.backgroundColor('#F1F3F5').borderRadius(15);
         }, (item: Grids) => item.name);
       }
       .layoutDirection(GridDirection.Column)
       .columnsTemplate('1fr 1fr')
       .rowsGap(15)
       .columnsGap(10)
       .padding({ top: 10, bottom: 10 })
       .height(210)
       .width('100%');
     }
   }

   export interface Lists {
     icon?: Resource;
     name: string;
   }

   @Component
   export struct ListComponent {
     listAdapter: ListItemAdapter<Lists> = new ListItemAdapter();
     listItemData: Array<Lists> = [];

     aboutToAppear(): void {
       this.listAdapter.addList(this.listItemData);
     }

     build() {
       Column() {
         LazyForEach(this.listAdapter, (item: Lists) => {
           Column() {
             Text(item.name)
               .textAlign(TextAlign.Center)
               .width('100%')
               .height('20%')
               .margin({ top: 15 });
           }.backgroundColor('#F1F3F5')
           .borderRadius(15)
           .margin({bottom:12});
         }, (item: Lists) => item.name);
       }
       .padding({ top: 10, bottom: 10 })
       .height('auto')
       .width('100%');
     }
   }

   export enum ItemType {
     listItems = 'listItems',
     gridItems = 'gridItems'
   }

   export class DataModel {
     itemType: ItemType = ItemType.listItems;
     result: ESObject;
   }
   ```
3. ListItemAdapter.ets：
   * 实现一个泛型类，实现IDataSource接口。
   * 维护一个列表listItems和数据变更的监听器listeners。

   示例代码如下：

   ```ts
   export class ListItemAdapter<T> implements IDataSource {
     private listItems: T[] = [];
     private listeners: DataChangeListener[] = [];

     getList(): T[] {
       return this.listItems;
     }

     setList(list: T[]) {
       this.listItems = list;
     }

     addList(list: T[]) {
       this.listItems = this.listItems.concat(list);
       this.notifyDataAdd(this.listItems.length - 1);
     }

     totalCount(): number {
       return this.listItems.length;
     }

     getData(index: number): T {
       return this.listItems[index];
     }

     registerDataChangeListener(listener: DataChangeListener): void {
       if (this.listeners.indexOf(listener) < 0) {
         this.listeners.push(listener);
       }
     }

     unregisterDataChangeListener(listener: DataChangeListener): void {
       const pos = this.listeners.indexOf(listener);
       if (pos >= 0) {
         this.listeners.splice(pos, 1);
       }
     }

     notifyDataReload(): void {
       this.listeners.forEach(listener => {
         listener.onDataReloaded();
       });
     }

     notifyDataAdd(index: number): void {
       this.listeners.forEach(listener => {
         listener.onDataAdd(index);
       });
     }

     notifyDataChange(index: number): void {
       this.listeners.forEach(listener => {
         listener.onDataChange(index);
       });
     }

     notifyDataDelete(index: number): void {
       this.listeners.forEach(listener => {
         listener.onDataDelete(index);
       });
     }

     notifyDataMove(from: number, to: number): void {
       this.listeners.forEach(listener => {
         listener.onDataMove(from, to);
       });
     }
   }
   ```

   效果图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/EJW99G3hRXOZdGaAGkFnQw/zh-cn_image_0000002764476642.gif "点击放大")

**Q：怎样在此场景上实现下拉刷新功能？**

**A**：下拉刷新可以使用Refresh嵌套List来实现，刷新逻辑在onRefreshing回调方法里面执行，具体参考[官方文档](faqs-arkui-278.md)。

**Q：如何实现朋友圈效果，如下图所示（仅涉及UI，不涉及具体功能）？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/CJXVZcKJSf6WV8uEigbtww/zh-cn_image_0000002764316046.png "点击放大")

A：实现步骤如下：

1. 在主页面创建Refresh组件，并在该组件中使用LazyForEach对MomentListItem进行渲染，并按特定方式实现图片和视频组件的交替渲染，这是该demo的框架功能实现。

   ```ts
   Refresh({ refreshing: $$this.isRefreshing }) {
         List({ space: 20 }) {
           LazyForEach(this.listDataSource, (item: MomentItem) => {
             ListItem() {
               MomentListItem({
                 data: item
               });
             }
             .padding({ left: 14, right: 14 })
             .backgroundColor(Color.White)
             .borderRadius(16);
           });
         }
         .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
         .width('100%')
         .height('100%')
         .padding({ left: 14, right: 14 });
       }
       .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
       .onRefreshing(() => {
         setTimeout(() => {
           this.isRefreshing = false;
         }, 1000);
       })
       .pullToRefresh(true);
   ```

2. 在MomentListItem组件中，对用户昵称，头像，时间以及文案内容，评论，点赞进行展示，并根据data属性的不同，进行图片和视频的展示。

   具体代码展示如下，以下各代码文件均位于pages目录下：

   * Moment.ets.

     ```ts
     import { CommonDataSource } from './CommonDataSource';
     import { MomentItem } from './ListModel';
     import { MomentListItem } from './MomentListItem';

     @Entry
     @Component
     struct Moments {
       @State isRefreshing: boolean = false;
       private listDataSource = new CommonDataSource<MomentItem>();

       aboutToAppear(): void {
         this.getListData();
       }

       getListData() {
         let followList: MomentItem[] = [];
         for (let i = 0; i < 10; i++) {
           // 此处'itemData值'仅作示例
           let itemData: MomentItem = new MomentItem();
           itemData.id = 'id_' + i;
           itemData.userId = 'userId_' + i;
           // 此处资源文件仅作展示，根据实际情况可自行替换
           itemData.userName = $r('app.string.userName');
           itemData.postingTime = '2025/07/09 10:30:00';
           itemData.isFollow = false;
           if (i % 2 === 0) {
             // 此处资源文件仅作展示，根据实际情况可自行替换
             itemData.title = $r('app.string.content1');
             itemData.images = [
               // 此处图片资源仅作展示，根据实际情况可自行替换
               $r('app.media.img'),
               $r('app.media.img'),
               $r('app.media.img'),
               $r('app.media.img'),
               $r('app.media.img'),
               $r('app.media.img'),
               $r('app.media.img'),
               $r('app.media.img'),
               $r('app.media.img'),
             ];
           } else {
             // 此处'video.mp4'仅作示例
             itemData.videoUrl = $rawfile('video.mp4');
             // 此处资源文件仅作展示，根据实际情况可自行替换
             itemData.title = $r('app.string.content2');
           }
           followList.push(itemData);
         }
         this.listDataSource.setData(followList);
       }

       @Builder
       ListContent() {
         Refresh({ refreshing: $$this.isRefreshing }) {
           List({ space: 20 }) {
             LazyForEach(this.listDataSource, (item: MomentItem) => {
               ListItem() {
                 MomentListItem({
                   data: item
                 });
               }
               .padding({ left: 14, right: 14 })
               .backgroundColor(Color.White)
               .borderRadius(16);
             });
           }
           .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
           .width('100%')
           .height('100%')
           .padding({ left: 14, right: 14 });
         }
         .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
         .onRefreshing(() => {
           setTimeout(() => {
             this.isRefreshing = false;
           }, 1000);
         })
         .pullToRefresh(true);

       }

       build() {
         Column() {
           this.ListContent();
         }
         .width('100%')
         .height('100%')
         .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
         .backgroundColor('#f1f3f5');
       }
     }
     ```
   * ListModel.ets.

     ```ts
     @ObservedV2
     export class MomentItem {
       id: string = '';
       userId: string = '';
       @Trace userName: ResourceStr = '';
       // 此处图片资源仅作展示，根据实际情况可自行替换
       @Trace userIcon: Resource = $r('app.media.avatar');
       @Trace title: ResourceStr = '';
       @Trace postingTime: string = '';
       @Trace isFollow: boolean = false;
       @Trace images: Resource[] = [];
       @Trace videoUrl: Resource | string = '';
       @Trace videoPreviewUrl: Resource | string = '';
       @Trace likeCount: number = 0;
       @Trace shareCount: number = 0;
       @Trace commentCount: number = 0;
       favorite: number = 0;
     }
     ```
   * MomentListItem.ets.

     ```ts
     import { MomentItem } from './ListModel';

     @Component
     export struct MomentListItem {
       data: MomentItem | null = null;
       controller: VideoController = new VideoController();
       isPlay: boolean = false;

       getPostingTime(time: string = ''): string {
         let date: Date = new Date(time);

         let M: number = date.getMonth() + 1;
         let D: number = date.getDate();
         let h: number = date.getHours();
         let m: number = date.getMinutes();

         return `${M}-${D} ${h}:${m}`;
       }

       build() {
         Column() {
           Row() {
             Image(this.data?.userIcon).width(30).height(30);
             Column() {
               Text(this.data?.userName)
                 .fontSize(13)
                 .fontColor('#e6000000')
                 .fontWeight(FontWeight.Bold);
               Text(this.getPostingTime(this.data?.postingTime))
                 .fontSize(10)
                 .fontColor('#99000000')
                 .margin({ top: 2 });
             }
             .offset({ x: 8 })
             .alignItems(HorizontalAlign.Start);
           }
           .width('100%');

           Text(this.data?.title)
             .fontSize(16)
             .width('100%')
             .fontColor('#e6000000')
             .margin({ top: 12 });

           Column() {
             if (this.data?.images && this.data.images.length) {
               if (this.data.images.length > 2) {
                 this.imageGridBuilder(this.data.images);
               } else {
                 this.imageBuilder(this.data.images);
               }
             }
             if (this.data?.videoUrl) {
               this.videoBuilder(this.data);
             }
           }
           .margin({ top: 8 })
           .alignItems(HorizontalAlign.Start);

           // 判断是否存在评论
           if (true) {
             Column({ space: 10 }) {
               ForEach([1, 2, 3], () => {
                 this.CommentListView();
               });
               // 判断评论数量是否超过3条
               if (true) {
                 Text('查看更多回复')
                   .fontColor('#0A59F7')
                   .fontSize(12)
                   .margin({ left: 38 })
                   .onClick(() => {
                   });
               }
             }
             .padding({
               left: 14,
               right: 14,
               top: 14,
               bottom: 12
             })
             .backgroundColor('#F1F3F5')
             .margin({ top: 10 })
             .borderRadius(12)
             .alignItems(HorizontalAlign.Start);
           }
         }
         .width('100%')
         .height('auto')
         .borderRadius(16)
         .padding({ bottom: 16 })
         .margin({ top: 16 });
       }

       @Builder
       CommentListView() {
         Column() {
           Row() {
             Image(this.data?.userIcon).width(30).height(30);
             Column() {
               Text(this.data?.userName).fontSize(12).fontColor('#e6000000');
               Text(this.getPostingTime(this.data?.postingTime))
                 .fontSize(10)
                 .fontColor('#99000000')
                 .margin({ top: 2 });
             }
             .alignItems(HorizontalAlign.Start)
             .offset({ x: 8 });
           }
           .width('100%');

           Text(this.data?.title)
             .fontSize(12)
             .margin({ left: 38 });
         }
         .width('100%')
         .alignItems(HorizontalAlign.Start);
       }

       @Builder
       imageBuilder(images: Resource[]) {
         Row({ space: 6 }) {
           ForEach(images, (item: Resource) => {
             Image(item).width(`${100 / 2}%`);
           });
         };
       }

       @Builder
       imageGridBuilder(images: Resource[]) {
         Grid() {
           ForEach(images, (item: Resource) => {
             GridItem() {
               Column() {
                 Image(item)
                   .borderRadius(4)
                   .width('calc((100% - 16vp) / 3)')
                   .aspectRatio(1);
               }
               .onClick(() => {
               });
             };
           });
         }
         .width('100%')
         .constraintSize({ maxWidth: '100%' })
         .maxCount(3)
         .columnsGap(8)
         .rowsGap(8)
         .backgroundColor(Color.White);
       }

       @Builder
       videoBuilder(item: MomentItem) {
         Stack() {
           Video({ src: item.videoUrl, controller: this.controller })
             .width('50%')
             .height(220)
             .loop(false)
             .objectFit(ImageFit.Contain)
             .autoPlay(true)
             .controls(false);
         }
         .onClick(() => {
           this.isPlay = !this.isPlay;
           if (this.isPlay) {
             this.controller.start();
           } else {
             this.controller.pause();
           }
         });
       }

       @Builder
       cellItemBuilder(icon: Resource, text: string) {
         Row() {
           Image(icon).width(16).height(16);
           Text(text).fontSize(12).margin({ left: 2 });
         };
       }
     }
     ```
   * CommonDataSource.ets.

     ```ts
     export class CommonDataSource<T> implements IDataSource {
       private listeners: DataChangeListener[] = [];
       originDataArray: T[] = [];

       totalCount(): number {
         return this.originDataArray.length;
       }

       getAllData(): T[] {
         return this.originDataArray;
       }

       getData(index: number) {
         return this.originDataArray[index];
       }

       addData(index: number, data: T): void {
         this.originDataArray.splice(index, 0, data);
         this.notifyDataAdd(index);
       }

       pushData(data: T): void {
         this.originDataArray.push(data);
         this.notifyDataAdd(this.originDataArray.length - 1);
       }

       pushDataArray(...items: T[]): void {
         for (let data of items) {
           this.originDataArray.push(data);
           this.notifyDataAdd(this.originDataArray.length - 1);
         }
       }

       deleteDataUseContent(data: T): void {
         let delIndex: number = -1;
         for (let index = 0; index < this.originDataArray.length; index++) {
           const element = this.originDataArray[index];
           if (data === element) {
             delIndex = index;
           }
         }
         if (delIndex !== -1) {
           this.deleteData(delIndex);
         }
       }

       deleteData(index: number): void {
         this.originDataArray.splice(index, 1);
         this.notifyDataDelete(index);
       }

       clear() {
         this.originDataArray.splice(0, this.originDataArray.length);
         this.listeners.forEach(listener => {
           listener.onDataDelete(0);
         });
       }

       setData(dataArray?: T[]) {
         if (dataArray) {
           this.originDataArray = dataArray;
         } else {
           this.originDataArray = [];
         }
         this.notifyDataReload();
       }

       refreshDataByIndex(start: number, end: number, dataArray: T[]) {
         this.originDataArray.splice(start, end - start, ...dataArray);
         this.notifyDataReload();
       }

       changeData(index: number, data: T): void {
         this.originDataArray.splice(index, 1, data);
         this.notifyDataChange(index);
       }

       registerDataChangeListener(listener: DataChangeListener): void {
         if (this.listeners.indexOf(listener) < 0) {
           this.listeners.push(listener);
         }
       }

       unregisterDataChangeListener(listener: DataChangeListener): void {
         const pos = this.listeners.indexOf(listener);
         if (pos >= 0) {
           this.listeners.splice(pos, 1);
         }
       }

       notifyDataReload() {
         this.listeners.forEach(listener => {
           listener.onDataReloaded();
         });
       }

       notifyDataAdd(index: number) {
         this.listeners.forEach(listener => {
           listener.onDataAdd(index);
         });
       }

       notifyDataMove(from: number, to: number) {
         this.listeners.forEach(listener => {
           listener.onDataMove(from, to);
         });
       }

       notifyDataDelete(index: number) {
         this.listeners.forEach(listener => {
           listener.onDataDelete(index);
         });
       }

       notifyDataChange(index: number) {
         this.listeners.forEach(listener => {
           listener.onDataChange(index);
         });
       }
     }
     ```
