---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1506
title: 如何解决Grid组件在编辑模式打开后拖拽子组件异常问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Grid组件在编辑模式打开后拖拽子组件异常问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:846454ee89b5b043693bd6ccfe40b20b8bf5d41a892da120622549659624a0f3
---

## 问题现象

Grid组件编辑模式打开后拖拽效果异常，预期和实际效果如下：

预期效果：预加载的图片能够通过点击来添加图片到Grid组件，被添加的图片可以通过拖拽改变排序。

实际效果：打开editMode的状态下，被添加的图片只有拖拽动画，无法实现拖拽排序。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/bgtDbEsjQ1S320uJBAlfFA/zh-cn_image_0000002658845801.png "点击放大")

问题代码如下：

DimensionUtil：

```ts
import display from '@ohos.display';

export class DimensionUtil {

  static getScreenInfo(isVp: boolean = true): ScreenSize {
    let displayInfo = display.getDefaultDisplaySync();
    let screenW = displayInfo.width / (isVp ? displayInfo.scaledDensity : 1)
    let screenH = displayInfo.height / (isVp ? displayInfo.scaledDensity : 1)
    return {
      screenW: screenW,
      screenH: screenH
    }
  }
}

export interface ScreenSize {
  screenW: number
  screenH: number
}
```

GridPullPage：

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit'
import { BusinessError } from '@kit.BasicServicesKit'
import { DimensionUtil } from './DimensionUtil'

@Entry
@Component
struct GridPullPage {
  @State selectMedias: Array<string> = ["-1"] // 选择的图片和视频
  @State imageWH: number = 60
  @State editMode: boolean = true;
  @State maxSelectPics: number = 9 // 最大选择图片数量
  private scroller: Scroller = new Scroller()

  aboutToAppear() {
    let screenW = DimensionUtil.getScreenInfo(true).screenW
    this.imageWH = (screenW - 4 * 15) / 3
  }

  build() {
    Column() {
      this.imageList()
    }
  }

  @Builder
  itemGrid(item: string, index: number) {
    // 此处'app.media.newsinformantspage_item_imagepicker_default'仅作示例。
    Image(item === "-1" ? $r('app.media.newsinformantspage_item_imagepicker_default') : item)
      .objectFit(ImageFit.Cover)
      .width(this.imageWH)
      .height(this.imageWH)
      .borderRadius(4)
      .onClick(() => {
        if (item === "-1") {
          this.selectImages({
            maxSelectNumber: this.maxSelectPics - (this.selectMedias.length - 1)
          }, (photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
            this.selectMedias = this.selectMedias.concat(photoSelectResult.photoUris)
            if (this.selectMedias.length > this.maxSelectPics) {
              this.selectMedias = this.selectMedias.filter(data => data !== "-1");
            }
          })
        }
      })
  }

  @Builder
  itemDragGrid(item: string, index: number) {
    Image(item)
      .objectFit(ImageFit.Cover)
      .width(this.imageWH)
      .height(this.imageWH)
      .borderRadius(4)
  }

  @Builder
  imageList() {
    Grid(this.scroller) {
      ForEach(this.selectMedias, (item: string, index: number) => {
        GridItem() {
          Stack() {
            this.itemGrid(item, index)
          }
          .padding({ bottom: 15 })
        }
      }, (item: string, index: number) => {
        return `${item}_${index}`
      })
    }
    .editMode(this.editMode)
    .height(this.calculateGridHeight())
    .width('100%')
    .padding({ left: 15, right: 15 })
    .margin({ top: 15 })
    .columnsTemplate('1fr 1fr 1fr')
    .supportAnimation(true)
    .scrollBar(BarState.Off)
    .onItemDragStart((event: ItemDragInfo, itemIndex: number) => {
        // 在onItemDragStart函数返回自定义组件，可在拖拽过程中显示此自定义组件。
        return this.itemDragGrid(this.selectMedias[itemIndex], itemIndex)
    })
    .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => {
      // 执行gridItem切换操作
      if (isSuccess && insertIndex < this.selectMedias.length) {
        // 点击选择图标不进行交换
        if (this.selectMedias[itemIndex] === "-1") {
          return
        }
        this.changeIndex(itemIndex, insertIndex)
      }
    })
  }

  selectImages(photoSelectOptions: photoAccessHelper.PhotoSelectOptions,
    onSelected: (photoSelectResult: photoAccessHelper.PhotoSelectResult) => void) {
    try {
      let photoPicker = new photoAccessHelper.PhotoViewPicker();
      photoPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
        onSelected?.(photoSelectResult)
      }).catch((err: BusinessError) => {
      });
    } catch (error) {
    }
  }

  changeIndex(itemIndex: number, insertIndex: number): void {
    this.selectMedias.splice(insertIndex, 0, this.selectMedias.splice(itemIndex, 1)[0])
  }

  calculateGridHeight(): number {
    let lineSize = 0
    if (this.selectMedias.length > 3) {
      lineSize = Math.ceil(this.selectMedias.length / 3)
    } else {
      lineSize = 1
    }
    let lineSpace = 15
    return lineSize * this.imageWH + (lineSize - 1) * lineSpace + lineSpace
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/YSHas0OvR_GEh02fpvR3kQ/zh-cn_image_0000002628766432.png "点击放大")

## 背景知识

* [editMode](../harmonyos-references/ts-container-grid.md#editmode8)属性能够设置Grid是否进入编辑模式，Grid进入编辑模式后就可以拖曳Grid组件内部[GridItem](../harmonyos-references/ts-container-griditem.md)。
* [hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)属性用于设置不同的触摸测试响应模式，影响触摸测试收集结果及后续触屏事件分发。具体影响参考[HitTestMode枚举说明](../harmonyos-references/ts-appendix-enums.md#hittestmode9)。

## 问题定位

Grid组件的editMode属性能够控制整个Grid组件是否能编辑，在问题代码中，editMode属性设置为true时，Grid组件拖拽效果异常，是因为拖动事件跟onClick事件发生了冲突。

## 分析结论

由于拖动事件跟onClick事件发生冲突，因此可以使用hitTestBehavior属性对不同的组件设置不同的触摸测试效果：将包含点击事件的图片设置为HitTestMode.Default，并将被添加进来的图片设置为HitTestMode.None。保证添加图片的固定图片无法被拖曳位置，onClick事件可以生效；添加进来的图片可以被拖曳位置，onClick事件不生效。

## 修改建议

根据以上分析，修改建议如下：

1. 不同的元素，设置不同的HitTestMode。

   ```ts
   @Builder
   itemGrid(item: string, index: number) {
     if (item === '-1') {
       // 此处'app.media.newsinformantspage_item_imagepicker_default'仅作示例。
       Image($r('app.media.newsinformantspage_item_imagepicker_default'))
         .objectFit(ImageFit.Cover)
         .width(this.imageWH)
         .height(this.imageWH)
         .borderRadius(4)
         .hitTestBehavior(HitTestMode.Default)
         .onClick(() => {
           this.selectImages({
             maxSelectNumber: this.maxSelectPics - (this.selectMedias.length - 1)
           }, (photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
             this.selectMedias = this.selectMedias.concat(photoSelectResult.photoUris);
             if (this.selectMedias.length > this.maxSelectPics) {
               this.selectMedias = this.selectMedias.filter(data => data !== '-1');
             }
           });
         });
     } else {
       Image(item)
         .objectFit(ImageFit.Cover)
         .width(this.imageWH)
         .height(this.imageWH)
         .borderRadius(4)
         .hitTestBehavior(HitTestMode.None)
         .onClick(() => {
           console.info(`index：${index}`);
         });
     }
   }
   ```
2. 拖拽图片后，根据拖拽的位置序号来进行重新排序。

   ```ts
   .onItemDragStart((event: ItemDragInfo, itemIndex: number) => {
     // 在onItemDragStart函数返回自定义组件，可在拖拽过程中显示此自定义组件
     return this.itemDragGrid(this.selectMedias[itemIndex], itemIndex);
   })
   .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => {
     // 执行gridItem切换操作
     if (isSuccess && insertIndex < this.selectMedias.length) {
       // 点击选择图标不进行交换
       if (this.selectMedias[itemIndex] === '-1') {
         return;
       }
       this.changeIndex(itemIndex, insertIndex);
     }
   });
   ```

完整代码如下：

DimensionUtil：

```ts
import display from '@ohos.display';

export class DimensionUtil {
  static getScreenInfo(isVp: boolean = true): ScreenSize {
    let displayInfo = display.getDefaultDisplaySync();
    let screenW = displayInfo.width / (isVp ? displayInfo.scaledDensity : 1);
    let screenH = displayInfo.height / (isVp ? displayInfo.scaledDensity : 1);
    return {
      screenW: screenW,
      screenH: screenH
    };
  }
}

export interface ScreenSize {
  screenW: number;
  screenH: number;
}
```

GridPullPage：

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { DimensionUtil } from './DimensionUtil';

@Entry
@Component
struct GridPullPage {
  @State selectMedias: Array<string> = ['-1']; // 选择的图片和视频
  @State imageWH: number = 60;
  editMode: boolean = true;
  maxSelectPics: number = 9; // 最大选择图片数量
  private scroller: Scroller = new Scroller();

  aboutToAppear() {
    let screenW = DimensionUtil.getScreenInfo(true).screenW;
    this.imageWH = (screenW - 4 * 15) / 3;
  }

  build() {
    Column() {
      this.imageList();
    };
  }

  @Builder
  itemGrid(item: string, index: number) {
    if (item === '-1') {
      // 此处'app.media.newsinformantspage_item_imagepicker_default'仅作示例。
      Image($r('app.media.newsinformantspage_item_imagepicker_default'))
        .objectFit(ImageFit.Cover)
        .width(this.imageWH)
        .height(this.imageWH)
        .borderRadius(4)
        .hitTestBehavior(HitTestMode.Default)
        .onClick(() => {
          this.selectImages({
            maxSelectNumber: this.maxSelectPics - (this.selectMedias.length - 1)
          }, (photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
            this.selectMedias = this.selectMedias.concat(photoSelectResult.photoUris);
            if (this.selectMedias.length > this.maxSelectPics) {
              this.selectMedias = this.selectMedias.filter(data => data !== '-1');
            }
          });
        });
    } else {
      Image(item)
        .objectFit(ImageFit.Cover)
        .width(this.imageWH)
        .height(this.imageWH)
        .borderRadius(4)
        .hitTestBehavior(HitTestMode.None)
        .onClick(() => {
          console.info(`index：${index}`);
        });
    }
  }

  @Builder
  itemDragGrid(item: string, index: number) {
    Image(item)
      .objectFit(ImageFit.Cover)
      .width(this.imageWH)
      .height(this.imageWH)
      .borderRadius(4)
      .onClick(() => {
        console.info(`index：${index}`);
      });
  }

  @Builder
  imageList() {
    Grid(this.scroller) {
      ForEach(this.selectMedias, (item: string, index: number) => {
        GridItem() {
          Stack() {
            this.itemGrid(item, index);
          }
          .padding({ bottom: 15 });
        };
      }, (item: string, index: number) => {
        return `${item}_${index}`;
      });
    }
    .editMode(this.editMode)
    .height(this.calculateGridHeight())
    .width('100%')
    .padding({ left: 15, right: 15 })
    .margin({ top: 15 })
    .columnsTemplate('1fr 1fr 1fr')
    .supportAnimation(true)
    .scrollBar(BarState.Off)
    .onItemDragStart((event: ItemDragInfo, itemIndex: number) => {
      // 在onItemDragStart函数返回自定义组件，可在拖拽过程中显示此自定义组件
      return this.itemDragGrid(this.selectMedias[itemIndex], itemIndex);
    })
    .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => {
      // 执行gridItem切换操作
      if (isSuccess && insertIndex < this.selectMedias.length) {
        // 点击选择图标不进行交换
        if (this.selectMedias[itemIndex] === '-1') {
          return;
        }
        this.changeIndex(itemIndex, insertIndex);
      }
    });
  }

  selectImages(photoSelectOptions: photoAccessHelper.PhotoSelectOptions,
    onSelected: (photoSelectResult: photoAccessHelper.PhotoSelectResult) => void) {
    try {
      let photoPicker = new photoAccessHelper.PhotoViewPicker();
      photoPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
        onSelected?.(photoSelectResult);
      }).catch(() => {
      });
    } catch (error) {
    }
  }

  changeIndex(itemIndex: number, insertIndex: number): void {
    this.selectMedias.splice(insertIndex, 0, this.selectMedias.splice(itemIndex, 1)[0]);
  }

  calculateGridHeight(): number {
    let lineSize = 0;
    if (this.selectMedias.length > 3) {
      lineSize = Math.ceil(this.selectMedias.length / 3);
    } else {
      lineSize = 1;
    }
    let lineSpace = 15;
    return lineSize * this.imageWH + (lineSize - 1) * lineSpace + lineSpace;
  }
}
```
