---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0017
title: ArkUI-Grid组件布局与交互常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > ArkUI-Grid组件布局与交互常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:32+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:01a28cb9f9efabdd8c0abb0b094fb93c1ac312e9553f683f41f17f800c1db20f
---

**Q：为Grid组件添加点击事件以实现缩放动画效果时，如何实现只点击特定GridItem项的功能？**

**A**：实现只点击特定GridItem项的功能的方法如下：

1. GridLayoutOptions是Grid组件的布局选项，在该对象中设置onGetRectByIndex方法用以初始化整个Grid组件。

   ```ts
   layoutOptions: GridLayoutOptions = {
       regularSize: [1, 1],
       onGetRectByIndex: (index: number) => {
         if (index === 0) {
           return [0, 0, 1, 1];
         } else if (index === 1) {
           return [0, 1, 2, 2];
         } else if (index === 2) {
           return [0, 3, 3, 3];
         } else if (index === 3) {
           return [3, 0, 3, 3];
         } else if (index === 4) {
           return [4, 3, 2, 2];
         } else {
           return [5, 5, 1, 1];
         }
       }
     };
   ```
2. 使用foreach方法依据上一步的设置的值循环渲染出每个GridItem组件，并为组件添加onclick方法，点击特定的GridItem组件时，在scale方法中将对应的GridItem组件缩放比例调整为0.5。

   ```ts
   ForEach(this.numberT, (day: string, index: number) => {
             GridItem() {
               Text(day)
                 .fontSize(16)
                 .backgroundColor(0xF9CF93)
                 .width('100%')
                 .height('100%')
                 .textAlign(TextAlign.Center);
             }
             .scale(this.currentGridItem === index ? {
               x: 0.5,
               y: 0.5,
               z: 0,
             } : null)
             .onClick(() => {
               this.currentGridItem = index;
             })
             .height('100%')
             .width('100%');
           }, (day: string) => day);
   ```

完整代码如下所示：

```ts
@Entry
@Component
struct GridClick {
  @State numberT: String[] = ['0', '1', '2', '3', '4', '5'];
  @State currentGridItem: number | null = null;
  layoutOptions: GridLayoutOptions = {
    regularSize: [1, 1],
    onGetRectByIndex: (index: number) => {
      if (index === 0) {
        return [0, 0, 1, 1];
      } else if (index === 1) {
        return [0, 1, 2, 2];
      } else if (index === 2) {
        return [0, 3, 3, 3];
      } else if (index === 3) {
        return [3, 0, 3, 3];
      } else if (index === 4) {
        return [4, 3, 2, 2];
      } else {
        return [5, 5, 1, 1];
      }
    }
  };

  build() {
    Column({ space: 5 }) {
      Grid(undefined, this.layoutOptions) {
        ForEach(this.numberT, (day: string, index: number) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height('100%')
              .textAlign(TextAlign.Center);
          }
          .scale(this.currentGridItem === index ? {
            x: 0.5,
            y: 0.5,
            z: 0,
          } : null)
          .onClick(() => {
            this.currentGridItem = index;
          })
          .height('100%')
          .width('100%');
        }, (day: string) => day);
      }
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300);
    }
    .width('100%')
    .margin({ top: 5 });
  }
}
```

运行效果图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/7KF4cB6vTESzjXJ34iZGZg/zh-cn_image_0000002765935784.png "点击放大")

**Q：Grid组件无法兼顾高度100%、子组件居中、拖拽事件三者同时存在。具体现象是：设置高度100%后，可以拖拽，但子项无法上下居中；如果想居中，就必须设置rowsTemplate和columnsTemplate，但没有拖拽动画。**

**A**：在EntryAbility设置全局背景色，实现沉浸式效果，示例代码如下：

```ts
import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
      windowStage.getMainWindowSync().setWindowBackgroundColor('#f1f3f5');

    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
};
```

通过单独添加一个GridItem子项，将其中组件高度设置为100%，并将该项的宽值设置为0fr，这样可以保证其余GridItem子项上下居中显示，且单独添加的GridItem不显示，拖拽动画也可以保留。完整代码如下：

```ts
class TabItem {
  appletName: string = '';

  constructor(appletName: string) {
    this.appletName = appletName;
  }
}

@Entry
@Component
struct gridDemo {
  longPressTimer: number = 0;
  @State bottomNavList: TabItem[] = [
    new TabItem('首页'),
    new TabItem('消息'),
    new TabItem('通话'),
    new TabItem('设置'),
    new TabItem('我的'),
  ];

  $bottomNavList(list: TabItem[]) {
    this.bottomNavList = list;
  }

  swapBottomNavItemPosition(itemIndex: number, insertIndex: number) {
    let copyList = this.bottomNavList;
    let tmpBottomNavItem = copyList.splice(itemIndex, 1);
    copyList.splice(insertIndex, 0, tmpBottomNavItem[0]);
    this.$bottomNavList(copyList);
  }

  build() {
    Grid() {
      GridItem() { // 在最前单独添加一个GridItem，设置其中组件高度为100%
        Column()
          .height('100%');
      };

      ForEach(this.bottomNavList, (item: TabItem) => {
        GridItem() {
          this.BottomNavItem(item);
        };
      });
    }
    .height('100%')
    .layoutWeight(1)
    .align(Alignment.Center)
    .columnsTemplate('0fr 1fr 1fr 1fr 1fr 1fr') // 设置第一个GridItem的宽值为0fr，该项不显示
    .onItemDragStart((_, selectItemIndex: number) => {
      console.info('itemIndex:' + selectItemIndex);
      return this.BottomNavItem(this.bottomNavList[selectItemIndex - 1]); // 为保证拖拽时显示正确，需要将索引值-1
    })
    .onItemDrop((_, itemIndex: number, insertIndex: number) => {
      this.swapBottomNavItemPosition(itemIndex - 1, insertIndex - 1); // 为保证拖拽时显示正确，需要将索引值-1
    })
    .editMode(true)
    .backgroundColor('#F1F3F5')
    .supportAnimation(true)
    .align(Alignment.Center)
    .padding({
      left: 10,
      right: 10,
      bottom: 10 // 保留阴影不被截断
    })
  }

  // 底部Tab子项
  @Builder
  BottomNavItem(bottomNav: TabItem) {
    Column() {
      // 作用：设置padding来解决拖拽时阴影被截断的问题
      Stack({ alignContent: Alignment.TopEnd }) {
        Column({ space: 3 }) {
          Text(bottomNav.appletName)
            .fontSize(10)
            .margin({bottom:5})
        }
        .aspectRatio(1)
        .justifyContent(FlexAlign.Center)
        .shadow({ radius: 30, color: 'rgba(0,0,0,0.22)' })
        .borderRadius(12)
        .backgroundColor(Color.White)
        .margin({ top: 10, right: 10 })
        .padding({
          left: 16,
          top: 4,
          right: 16
        });
      };
    }
    .layoutWeight(1)
    .padding({
      left: 2,
      right: 2,
      bottom: 2,
      top: 2
    });
  }
}
```

**说明** 

此方法本质上是增加了一个GridItem子组件用于占满高度，保证其他GridItem子组件居中显示，所以针对拖拽时的索引值也要做出调整，上面例子将GridItem子组件添加在首位，所以对应的索引值需要-1。

实现效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/3OEV4zrcQEu-9F4RAySTdg/zh-cn_image_0000002766095730.png "点击放大")

**Q：在开发过程中，Grid布局是构建页面结构的强大工具。特别是在复杂界面设计中，常需利用Grid布局实现单元格的灵活合并，以确保界面元素的精确对齐和响应式调整，从而提升体验。如何使用Grid单元格实现合并布局？预期效果：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/bw3oWL4kTGGeuKH96HwVkQ/zh-cn_image_0000002766095732.png "点击放大")

**A**：方案一：通过GridItem的行列跨度属性合并单元格。

1. 适用场景：
   * 简单跨行/跨列：适用于需要手动控制少量单元格合并的场景，例如：表格标题栏跨多列（如合并首行前3列）、九宫格首项占据整行（如电商首页Banner）、日历中的周末日期合并（如周六、周日跨列显示）等。
   * 固定的复杂布局需求：当布局结构固定且无需频繁调整时，直接设置行列号更直观。例如固定导航栏按钮排列、商品分类标签的固定组合等。
2. 实现方式：从背景知识中可知，若要实现问题描述中的预期效果，可以对GridItem进行设置。GridItem有属性如下：
   * rowStart：设置当前元素起始行号；
   * rowEnd：设置当前元素终点行号；
   * columnStart：设置当前元素起始列号；
   * columnEnd：设置当前元素终点列号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/WPMzQtRoQFWtcFJW9VDXKg/zh-cn_image_0000002766095736.png "点击放大")

   分析上图，这是一个五行四列的网格布局，其中编号1、2、3的网格占了整行（合并列），它们的元素起始列号为0，元素终点列号为3，如果设置了rowStart/rowEnd/columnStart/columnEnd，GridItem会占据指定的行数(rowEnd-rowStart+1)或列数(columnEnd-columnStart+1)。

   编号9的网格元素起始列号为1，元素终点列号为3，但若将其列号设置的与1、2、3号网格一样，则9号会和8号产生位置冲突。在设置行列号布局时，若该区域位置存在GridItem布局，则会产生避让，因此9号按照1、2、3号网格进行相同设置，同样能实现预期效果。

   示例代码如下：

   ```ts
   interface listItem {
     type: string;
     value: string;
   }

   @Entry
   @Component
   struct GridMerge {
     @State numbers: listItem[] =
       [{ type: 'title', value: '1' }, { type: 'title', value: '2' }, { type: 'title', value: '3' },
         { type: 'item', value: '4' }, { type: 'item', value: '5' }, { type: 'item', value: '6' },
         { type: 'item', value: '7' }, { type: 'item', value: '8' }, { type: 'title', value: '9' }];

     build() {
       Column({ space: 4 }) {
         Grid() {
           ForEach(this.numbers, (item: listItem) => {
             GridItem() {
               Text(item.value)
                 .fontSize(16)
                 .backgroundColor(0x0A59F7)
                 .width('100%')
                 .height('100%')
                 .textAlign(TextAlign.Center);
             }
             .columnStart(item.type === 'title' ? 0 : undefined)
             .columnEnd(item.type === 'title' ? 3 : undefined)
             .height('100%')
             .width('100%');
           }, (item: listItem) => item.value);
         }
         .columnsTemplate('1fr 1fr 1fr 1fr')
         .rowsTemplate('1fr 1fr 1fr 1fr 1fr')
         .columnsGap(10)
         .rowsGap(10)
         .width('90%')
         .backgroundColor(0xFAEEE0)
         .height(300)
         .animation({
           duration: 300,
           curve: Curve.Smooth
         });
       }
       .width('100%')
       .margin({ top: 5 })
     }
   }
   ```

方案二：通过layoutOptions配置不规则布局。

1. 适用场景：
   * 大量的不复杂布局：适用于需要稍微复杂的计算单元格尺寸或位置的场景，例如：计算器按键布局（如“0”键跨2列，“=”键跨2行）、促销广告栏横向跨多列（如“买一送一”横跨3列）、[可滚动的跨行跨列场景](../harmonyos-references/ts-container-grid.md#示例3可滚动grid设置跨行跨列节点)等。
   * 频繁合并单元格场景：当网格项数量较多时，GridLayoutOptions通过预计算布局减少渲染开销，避免因频繁操作行列号导致的性能问题。
2. 实现方式：制作不均匀的网格布局也可以通过[GridLayoutOptions对象](../harmonyos-references/ts-container-grid.md#gridlayoutoptions10对象说明)中的onGetRectByIndex属性返回的[rowStart,columnStart,rowSpan,columnSpan]来实现跨行跨列布局。属性含义如下：
   * rowStart：当前元素起始行号；
   * columnStart：当前元素起始列号；
   * rowSpan：指定当前元素的占用行数；
   * columnSpan：指定当前元素的占用列数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/XjMtnFnMTfyaK3H4pHJYHQ/zh-cn_image_0000002795494297.png "点击放大")

   分析上图，为了实现预期效果，可以对网格进行起始位置以及占用列数的设置，如编号1号的网格起始行号为0，起始列号也为0，占用行数为1，占用列数为4；编号9号的网格起始行号为4，起始列号为1，占用行数为1，占用列数为3。其余网格依次推理，更多示例代码详见：[固定行列Grid](../harmonyos-references/ts-container-grid.md#示例1固定行列grid)。

**Q：如何让Grid组件在高度不确定的情况下，实现自适应高度？**

**A**：页面中使用Grid组件，因为GridItem数量不固定，且不允许滚动，理想中Grid组件高度会被GridItem内容自动撑起，实际体验中发现：

1. Grid必须显式设置固定height属性，这种由于GridItem数量不固定，且不允许出现滚动，不满足需求；
2. 设置maxCount属性后，可以实现高度被撑起，但与文档的解释好像不符，且GridItem数量不固定，所以也不满足需求；
3. Grid的height设置为auto时也不会被自动撑起。可能原因：Grid不会自适应子节点的高度，不设置高度就是和父组件一样高。解决措施：目前有两个替代方案：
4. 使用list替代，设置其lanes属性进行分列。
5. 可以动态计算GridItem高度，然后给Grid的height设置高度。

   参考代码如下：

   ```ts
   interface Item {
     text: string
     img: Resource
   }

   @Entry
   @Component
   struct Index {
     data: Item[] = [
       { text: 'aaa', img: $r('app.media.app_icon') },
       { text: 'bbb', img: $r('app.media.app_icon') },
       { text: 'ccc', img: $r('app.media.app_icon') },
       { text: 'ddd', img: $r('app.media.app_icon') },
       { text: 'eee', img: $r('app.media.app_icon') },
       { text: 'fff', img: $r('app.media.app_icon') },
       { text: 'ggg', img: $r('app.media.app_icon') },
       { text: 'hhh', img: $r('app.media.app_icon') },
       { text: 'jjj', img: $r('app.media.app_icon') },
       { text: 'kkk', img: $r('app.media.app_icon') }]
     // Calculate the number of rows in the grid
     getCategoryRowCount() {
       return Math.ceil(this.data.length / 4);
     }
     // Calculate the height of the grid based on the height of the item
     getCategoryViewHeight() {
       return `${68.33 * this.getCategoryRowCount()}vp`;
     }

     build() {
       Column() {
         Grid() {
           ForEach(this.data, (item: Item) => {
             GridItem() {
               Column() {
                 Image(item.img)
                   .width(40)
                   .height(40)
                 Text(item.text)
                   .margin({ top: 2 })
                   .fontSize(14)
                   .textAlign(TextAlign.Center)
               }
             }
           }, (item: Item) => item.text)
         }
         .height(this.getCategoryViewHeight())
         .columnsTemplate('1fr 1fr 1fr 1fr')
         .columnsGap(10)
         .rowsGap(10)
         .margin({ top: 10 })
       }
       .padding(10)
       .width('100%')
     }
   }
   ```

**Q：在Grid中使用带有RelativeLayout的自定义组件时，分屏模式下，滑动页面时会出现回弹效果，无法正常滑动，如何解决？**

**A**：分析问题可知，由于没有正确设置父组件高度，导致组件锚点异常，致使Text组件无法定位锚点而异常渲染。可以将父组件高度设置为自适应，锚点即可正常定位，解决渲染异常问题。

RelativeContainer支持宽高自适应子组件，因此可以将其设置为auto，限制是当width设置为auto时，如果水平方向上子组件以容器作为锚点，则auto不生效，垂直方向上同理。完整示例代码如下：

```ts
@Entry
@Component
struct SplitScreenScroll {
  @State numbers: String[] = ['0', '1', '2', '3', '4'];
  scroller: Scroller = new Scroller();

  build() {
    Column({ space: 5 }) {
      Text('scroll').fontColor(0xCCCCCC).fontSize(9).width('75%').height('5%');
      Grid(this.scroller) {
        ForEach(this.numbers, () => {
          ForEach(this.numbers, (day: string) => {
            GridItem() {
              CustomGridItem({ day: day });
            };
          }, (day: string) => day);
        }, (day: string) => day);
      }
      .columnsTemplate('1fr')
      .columnsGap(10)
      .rowsGap(10)
      .width('85%')
      .height('95%');
    }.width('100%');
  }
}

@Component
struct CustomGridItem {
  day: string = '';

  build() {
    RelativeContainer() {
      Row() {
      }
      .width('100%')
      .height(50)
      .backgroundColor('#F1F2F3')
      .alignRules({})
      .id('row');
    }
    .width('auto')
    .height('auto')
    .border({ width: 2, color: '#F1F3F5' });
  }
}
```

实现效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/vKJA_7aWTtaoxrT5UqwkQg/zh-cn_image_0000002795494411.png "点击放大")

**Q：如何实现长按图标后，拖动时手机发出震动；拖动图标时，图标样式可变，并且最终可以被拖到另外一个Grid？**

**A**：需要使用Grid的拖拽能力实现长按图标的拖拽效果，在onItemDragStart拖拽回调中调用vibrator.startVibration来触发震动，同时在拖拽的回调中调用属性动画使图标抖动，并且可以自定义替换图标或者更换透明度等其他效果；拖拽的图标落下时，在onItemDrop回调中增加图标数量变化的业务逻辑。

1. 实现手机震动需要先配置[ohos.permission.VIBRATE](../harmonyos-guides/permissions-for-all.md#ohospermissionvibrate)权限，然后调用vibrator.startVibration增加震动效果。权限申请：{"name": "ohos.permission.VIBRATE"}。
2. 使用animateTo属性动画设计动画效果，实现抖动。
3. 设置.editMode(true)使Grid进入拖拽，然后增加图标替换和数量变化的逻辑。
4. 图片资源需要根据实际情况进行替换，将startIcon、img1替换为已有资源。

完整demo参考如下：

```ts
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

@Entry
@Component
struct GridDragIconsTest {
  @State addedItems1: string[] = ['1', '2', '3', '4', '5', '6', '7'];
  @State addedItems2: string[] = ['1', '2', '3'];
  private scroller1: Scroller = new Scroller();
  private scroller2: Scroller = new Scroller();

  @Builder
  dragItem(item: string) { // 拖拽过程样式
    Column() {
      // 图片替换为已有资源
      Image($r('app.media.img1'))
        .width(44)
        .height(44)
        .draggable(false)
        .objectFit(ImageFit.Contain);
      Text(`index:${item}`)
        .fontSize(12)
        .margin({ top: 5 });
    }
    .height('auto');
  }

  // 拖动时图片变化
  @State scaleValue: number = 1;
  @State opacityValue: number = 1;
  private angle: number = 0;
  // 是否在拖动
  @State isDrag1: boolean = false;
  @State isDrag2: boolean = false;
  // 落点是否在另外一个grid
  @State isDropIn1: boolean = false;
  @State isDropIn2: boolean = false;
  // 设置抖动
  @State rotateZ: number = 0;
  // 记录拖拽的图标起点和落点索引（无论上下哪个grid）
  @State indexUp: number = 0;
  @State indexDown: number = 0;

  private jumpWithSpeed(speed: number, isDrag: boolean) {
    if (isDrag) {
      this.rotateZ = -1;
      this.getUIContext().animateTo({
        delay: 0,
        tempo: speed,
        duration: 1000,
        curve: Curve.Smooth,
        playMode: PlayMode.Normal,
        iterations: -1
      }, () => {
        this.rotateZ = 1;
      });
    } else {
      this.stopJump();
    }
  }

  private stopJump() {
    this.getUIContext().animateTo({
      delay: 0,
      tempo: 5,
      duration: 0,
      curve: Curve.Smooth,
      playMode: PlayMode.Normal,
      iterations: 1
    }, () => {
      this.rotateZ = 0;
    });
  }

  build() {
    Column() {
      Grid(this.scroller1) {
        ForEach(this.addedItems1, (item: string) => {
          GridItem() {
            Column() {
              // 图片替换为已有资源
              Image($r('app.media.startIcon'))
                .width(44)
                .height(44)
                .objectFit(ImageFit.Contain)
                .draggable(false) // 设置为false
                .scale({ x: this.scaleValue, y: this.scaleValue })
                .opacity(this.opacityValue)
                .rotate({
                  angle: this.angle
                });

              Text(`index:${item}`)
                .fontSize(12)
                .margin({ top: 5 });
            }
            .height(99);
          }
          .rotate({
            z: this.rotateZ,
            angle: 1,
            centerX: '50%',
            centerY: '50%'
          });
        }, (item: string) => JSON.stringify(item) + util.generateRandomUUID(false));
      }
      .columnsGap(10)
      .rowsGap(0)
      .columnsTemplate('1fr 1fr 1fr 1fr')
      .supportAnimation(true)
      .height(220)
      .width('100%')
      .padding({
        top: 30
      })
      .backgroundColor(0xFAEEE0)
      .editMode(true) // 设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem
      .onItemDragStart(((event: ItemDragInfo, index: number) => { // 第一次拖拽此事件绑定的组件时，触发回调。
        console.info(`kevin1---onItemDragStart1---index:${index}`);
        this.indexUp = index;

        // 1、触发震动
        this.vibrator1();

        // 2、按住旋转
        this.isDrag1 = true;
        this.jumpWithSpeed(5, this.isDrag1);
        this.scaleValue = 0.9; // 缩小至90%
        this.opacityValue = 0.8; // 透明度80%
        return this.dragItem(this.addedItems1[index]); // 设置拖拽过程中显示的图片。
      }))
      .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number) => { // 绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调。
        this.indexDown = insertIndex;
        this.isDropIn1 = true;
        console.info('kevin1', 'onItemDrop1');
        console.info(`itemIndex---itemIndex:${insertIndex}`); // itemIndex拖拽起始位置，insertIndex拖拽插入位置
        this.changeIndex1();
        this.stopJump();
        this.scaleValue = 1;
        this.opacityValue = 1;
        this.init();
      });

      // grid2
      Grid(this.scroller2) {
        ForEach(this.addedItems2, (item: string) => {
          GridItem() {
            Column() {
              // 图片替换为已有资源
              Image($r('app.media.startIcon'))
                .width(44)
                .height(44)
                .objectFit(ImageFit.Contain)
                .draggable(false) // 设置为false
                .scale({ x: this.scaleValue, y: this.scaleValue })
                .opacity(this.opacityValue)
                .rotate({
                  angle: this.angle
                });

              Text(`index:${item}`)
                .fontSize(12)
                .margin({ top: 5 });
            }
            .height(99);
          }
          .rotate({
            z: this.rotateZ,
            angle: 1,
            centerX: '50%',
            centerY: '50%'
          });

        });
      }
      .columnsGap(10)
      .rowsGap(0)
      .columnsTemplate('1fr 1fr 1fr 1fr')
      .supportAnimation(true)
      .height(220)
      .width('100%')
      .padding({
        top: 30
      })
      .backgroundColor(0xFAEEE0)
      .editMode(true) // 设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem
      .onItemDragStart(((event: ItemDragInfo, index: number) => { // 第一次拖拽此事件绑定的组件时，触发回调。
        console.info(`kevin2---onItemDragStart2---index:${index}`);
        this.indexUp = index;

        // 1、触发震动
        this.vibrator1();

        // 2、按住旋转
        this.isDrag2 = true;

        this.jumpWithSpeed(5, this.isDrag2);

        this.scaleValue = 0.9; // 缩小至90%
        this.opacityValue = 0.8; // 透明度80%
        return this.dragItem(this.addedItems2[index]); // 设置拖拽过程中显示的图片。
      }))
      .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number) => { // 绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调。
        this.indexDown = insertIndex;
        this.isDropIn2 = true;
        this.stopJump();
        console.info('kevin2', 'onItemDrop2');
        console.info(`itemIndex---itemIndex:${insertIndex}`); // itemIndex拖拽起始位置，insertIndex拖拽插入位置
        this.changeIndex2();
        this.scaleValue = 1;
        this.opacityValue = 1;
        this.init();
      });
    }
    .justifyContent(FlexAlign.SpaceEvenly)
    .height('100%')
    .width('100%');
  }

  // 初始化长按拖拽状态
  init() {
    this.isDropIn2 = false;
    this.isDrag2 = false;
    this.isDropIn1 = false;
    this.isDrag1 = false;
  }

  // 触发马达振动
  vibrator1() {
    try {
      // 触发马达振动
      if (canIUse('SystemCapability.Sensors.MiscDevice')) {
        vibrator.startVibration({
          type: 'time',
          duration: 100,
        }, {
          id: 0,
          usage: 'alarm'
        }, (error: BusinessError) => {
          if (error) {
            console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
            return;
          }
          console.info('Succeed in starting vibration');
        });
      } else {
        // Fallback for unsupported SystemCapability
      }
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
    }
  }

  // 交换数组位置
  // 拖入1中
  changeIndex1() {
    const index1 = this.indexUp;
    const index2 = this.indexDown;
    // 从2拖到1：在2中按住，然后从1中落地
    if (this.isDrag2 && this.isDropIn1) {
      let temp: string;
      temp = this.addedItems2[index1];
      this.addedItems2.splice(index1, 1);
      this.addedItems1.splice(index2, 0, temp);
    } else if (this.isDrag1 && this.isDropIn1 && !this.isDropIn2) {
      // 从1拖到1：在1按住，然后在1中落地
      let temp: string;
      temp = this.addedItems1[index1];
      this.addedItems1[index1] = this.addedItems1[index2];
      this.addedItems1[index2] = temp;
    }
  }

  // 拖入2中
  changeIndex2() {
    const index1 = this.indexUp;
    const index2 = this.indexDown;
    // 从1拖到2：在1中按住，然后从2中落地
    if (this.isDrag1 && this.isDropIn2) {
      let temp: string;
      temp = this.addedItems1[index1];
      this.addedItems1.splice(index1, 1);
      this.addedItems2.splice(index2, 0, temp);
    } else if (this.isDrag2 && this.isDropIn2 && !this.isDropIn1) {
      // 从2拖到2：在2按住，然后在2中落地
      let temp: string;
      temp = this.addedItems2[index1];
      this.addedItems2[index1] = this.addedItems2[index2];
      this.addedItems2[index2] = temp;
    }
  }
}
```
