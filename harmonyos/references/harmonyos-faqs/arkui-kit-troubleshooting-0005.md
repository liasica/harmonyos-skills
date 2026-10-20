---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-troubleshooting-0005
title: Grid组件拖拽边缘无法继续拖动问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 故障排查 > Grid组件拖拽边缘无法继续拖动问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:33+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:2baebc990f1fa50897c67a0ae2e3f8b9d167e8564212f932b24950e934643326
---

## 问题现象

将Grid里的元素拖拽到边缘位置时，无法继续拖动。如下图：

（1）原始元素排列。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/y4_zl1yJR1q9mNlxnBTyVw/zh-cn_image_0000002793383055.png "点击放大")

（2）拖拽元素至边缘位置时，无法继续拖动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/Ikvw675gTTOK4tPPmkxSfg/zh-cn_image_0000002764144440.png "点击放大")

## 定位过程

1. 由于当前Grid不支持拖拽自动滚屏效果，所以考虑先捕捉拖拽动作，然后进行滚屏处理。
   * 使用API onItemDragMove捕捉到拖拽动作。
   * 使用API onScrollIndex定位当前页面的起始和终止元素的index。
2. 通过item被拖拽的目标位置来判断是上滑还是下滑：
   * 如果被拖动超过2个index，最终的目标位置还是在**上栏**，就往上滑。
   * 如果被拖动的目标位置在下图的**下栏**，就往下滑。如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/tc3W_QAySeKFM0TtboOOTg/zh-cn_image_0000002764144676.png "点击放大")

## 分析结论

由于当前Grid不支持拖拽自动滚屏效果，所以考虑先捕捉拖拽动作，然后进行滚屏处理：可以通过item被拖拽的目标位置来判断是上滑还是下滑。

## 修改建议

1. 通过onScrollIndex记录下滑动时的起始位置和终点位置。
2. 通过onItemDragMove来判断元素移动是上滑还是下滑。
3. 通过onItemDrop在GridItem拖动结束时，修改item的序号。

**代码示例如下：**

```ts
import Curves from '@ohos.curves';
import { display, window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct GridExample {
  @State numbers: string[] = [];
  scroller: Scroller = new Scroller();
  @State text: string = 'drag';
  @State currentIndex: number = 0;
  @State startIndex: number = 0;
  @State endIndex: number = 0;
  @State @Watch('currentYChange') currentY: number = 0;
  context: Context | undefined = undefined;

  @Builder
  pixelMapBuilder() { // 拖拽过程样式
    Column() {
      Text(this.text)
        .fontSize(16)
        .width(80)
        .height(80)
        .textAlign(TextAlign.Center)
        .backgroundColor('rgba(241, 243, 245, 1)');
    };
  }

  aboutToAppear() {
    for (let i = 1; i <= 30; i++) {
      this.numbers.push(i + '');
    }
    this.context = this.getUIContext().getHostContext() as common.Context;
    this.setScreenFull();
  }

  setScreenFull() { // 设置沉浸式
    let windowClass: window.Window | undefined = undefined;
    try {
      let promise = window.getLastWindow(this.context);
      promise.then((data) => {
        windowClass = data;
        windowClass.setWindowLayoutFullScreen(true).then(() => {
        }).catch(() => {
        });
        // 状态栏隐藏
        windowClass.setSpecificSystemBarEnabled('status', true).then(() => {
        }).catch(() => {
        });
        // 导航条隐藏
        windowClass.setSpecificSystemBarEnabled('navigationIndicator', false).then(() => {
        }).catch(() => {
        });
      }).catch(() => {

      });
    } catch (e) {

    }
  }

  changeIndex(index1: number, index2: number) {
    // 交换数组位置
    let temp: string;
    temp = this.numbers[index1];
    this.numbers[index1] = this.numbers[index2];
    this.numbers[index2] = temp;
  }

  build() {
    Column({ space: 5 }) {
      Grid(this.scroller) {
        ForEach(this.numbers, (day: string) => {
          GridItem() {
            Column() {
              Text(day)
                .fontSize(16)
                .backgroundColor('rgba(241, 243, 245, 1)')
                .width(98.6)
                .height(97)
                .textAlign(TextAlign.Center)
                .borderRadius(16);
            }
            .borderWidth(0); // 设置边框宽度

          };
        });
      }
      .columnsTemplate('1fr 1fr 1fr')
      .columnsGap(16)
      .rowsGap(16)
      .backgroundColor('rgba(255, 255, 255, 1)')
      .scrollBar(BarState.Off)
      // 设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem
      .editMode(true)
      .onScrollIndex((start: number, end: number) => {
        this.startIndex = start;
        this.endIndex = end;

      })
      .onItemDragStart((event: ItemDragInfo, itemIndex: number) => {

        // 第一次拖拽此事件绑定的组件时，触发回调。
        this.text = this.numbers[itemIndex];
        this.currentIndex = itemIndex;
        return this.pixelMapBuilder(); // 设置拖拽过程中显示的图片。
      })
      .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number,
        isSuccess: boolean) => { // 绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调。

        // isSuccess=false时，说明drop的位置在grid外部；insertIndex > length时，说明有新增元素的事件发生
        if (!isSuccess || insertIndex >= this.numbers.length) {
          return;
        }
        this.changeIndex(itemIndex, insertIndex);
      })
      .onItemDragMove((event: ItemDragInfo) => {
        let screenHeight = display.getDefaultDisplaySync().height;

        // 计算当前Y轴的位移量
        let yOffset: number = this.scroller.currentOffset().yOffset;

        if (event.y <= 55) {
          this.currentY = yOffset - 55;
          yOffset = this.currentY;
        }
        if (event.y >= this.getUIContext().px2vp(screenHeight - 55)) {
          this.currentY = yOffset + 55;
          yOffset = this.currentY;
        }

      });
    }
    .backgroundColor('rgba(241, 243, 245, 1)')
    .margin({
      top: 44,
      bottom: 0,
      left: 16,
      right: 16
    });
  }

  currentYChange() {
    // 创建一个阶梯曲线
    let curve = Curves.interpolatingSpring(10, 1, 228, 30);
    this.scroller.scrollTo({ xOffset: 0, yOffset: this.currentY, animation: { duration: 1000, curve: curve } });
  }
}
```

问题解决后效果如下图所示，拖拽元素能够自动滚屏：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/x53yYAGIRSKewy4RPABp7g/zh-cn_image_0000002763986368.png "点击放大")

从API Version 26 Release开始，Grid支持使用[onMove](../harmonyos-references/ts-universal-attributes-drag-sorting.md#onmove)进行拖拽排序，支持拖拽到边缘时自动滚动，无需手动实现滚屏逻辑。使用方式为在ForEach中设置onMove回调处理数据移动，具体可参考[Grid组件](../harmonyos-references/ts-container-grid.md)中的拖拽排序示例。
