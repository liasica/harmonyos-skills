---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1194
title: 如何实现图标长按震动拖动并动态添加到另外一个Grid
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现图标长按震动拖动并动态添加到另外一个Grid
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eac17ba3ff40ce433796bc2ac44280a9f0c5f1d6b91a48c99025d3c444c41696
---

## 问题现象

如何实现长按图标后，拖动时手机发出震动；拖动图标时，图标样式可变，并且最终可以被拖到另外一个Grid？

## 背景知识

* 震动效果需要申请ohos.permission.VIBRATE权限，然后使用[vibrator.startVibration](../harmonyos-references/js-apis-vibrator.md#vibratorstartvibration9)调用震动。
* 图标的拖拽可以使用Grid组件的拖拽能力，并且可以通过[onItemDragStart](../harmonyos-references/ts-container-grid.md#onitemdragstart8)和[onItemDrop](../harmonyos-references/ts-container-grid.md#onitemdrop8)监听图标拖拽和落下事件。
* [使用animateTo产生属性动画](../harmonyos-guides/arkts-attribute-animation-apis.md#使用animateto产生属性动画)和[rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)图形变换可以实现图标抖动的效果。

## 解决方案

需要使用Grid的拖拽能力实现长按图标的拖拽效果，在onItemDragStart拖拽回调中调用vibrator.startVibration来触发震动，同时在拖拽的回调中调用属性动画使图标抖动，并且可以自定义替换图标或者更换透明度等其他效果；拖拽的图标落下时，在onItemDrop回调中增加图标数量变化的业务逻辑。

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
