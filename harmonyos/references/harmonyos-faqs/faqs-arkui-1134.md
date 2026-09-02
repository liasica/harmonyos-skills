---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1134
title: 如何解决Grid组件拖拽到边缘时无法继续拖动的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Grid组件拖拽到边缘时无法继续拖动的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f715d1acadea565078117baddbfe843788778e0714d2d1a9eb0f9da6ae28f90e
---

## 问题现象

将Grid里的元素拖拽到边缘位置时，无法继续拖动。如下图：

（1）原始元素排列。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Eul3VtcUSt24_MSGdVybPg/zh-cn_image_0000002658928741.png "点击放大")

（2）拖拽元素至边缘位置时，无法继续拖动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/O4eBZ2P5Stird7UJ0raGCQ/zh-cn_image_0000002658808793.png "点击放大")

## 背景知识

* [onItemDragMove官方文档](../harmonyos-references/ts-container-grid.md#onitemdragmove8)：拖拽在网格元素范围内移动时触发。
* [onScrollIndex官方文档](../harmonyos-references/ts-container-grid.md#onscrollindex)：Grid显示区域上第一个子组件/最后一个组件的索引值有变化就会触发。
* [curves.interpolatingSpring官方文档](../harmonyos-references/js-apis-curve.md#curvesinterpolatingspring10)：构造插值器弹簧曲线对象，生成一条从0到1的动画曲线，实际动画值根据曲线进行插值计算。

## 问题定位

1. 由于当前Grid不支持拖拽自动滚屏效果，所以考虑先捕捉拖拽动作，然后进行滚屏处理。
   * 使用API onItemDragMove捕捉到拖拽动作。
   * 使用API onScrollIndex定位当前页面的起始和终止元素的index。
2. 通过item被拖拽的目标位置来判断是上滑还是下滑：
   * 如果被拖动超过2个index，最终的目标位置还是在**上栏**，就往上滑。
   * 如果被拖动的目标位置在下图的**下栏**，就往下滑。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/iMnafA-jTlG9SbN_n42M3Q/zh-cn_image_0000002628569430.png "点击放大")

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
  pixelMapBuilder() { //拖拽过程样式
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
        //状态栏隐藏
        windowClass.setSpecificSystemBarEnabled('status', true).then(() => {
        }).catch(() => {
        });
        //导航条隐藏
        windowClass.setSpecificSystemBarEnabled('navigationIndicator', false).then(() => {
        }).catch(() => {
        });
      }).catch(() => {

      });
    } catch (e) {

    }
  }

  changeIndex(index1: number, index2: number) {
    //交换数组位置
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
      //设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem
      .editMode(true)
      .onScrollIndex((start: number, end: number) => {
        this.startIndex = start;
        this.endIndex = end;

      })
      .onItemDragStart((event: ItemDragInfo, itemIndex: number) => {

        //第一次拖拽此事件绑定的组件时，触发回调。
        this.text = this.numbers[itemIndex];
        this.currentIndex = itemIndex;
        return this.pixelMapBuilder(); //设置拖拽过程中显示的图片。
      })
      .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number,
        isSuccess: boolean) => { //绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调。

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
    //创建一个阶梯曲线
    let curve = Curves.interpolatingSpring(10, 1, 228, 30);
    this.scroller.scrollTo({ xOffset: 0, yOffset: this.currentY, animation: { duration: 1000, curve: curve } });
  }
}
```

问题解决后效果如下图所示，拖拽元素能够自动滚屏：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/4v4YqIVMTbG0iEqn9YQJ9A/zh-cn_image_0000002628409530.png "点击放大")
