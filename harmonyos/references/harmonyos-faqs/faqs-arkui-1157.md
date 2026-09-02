---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1157
title: List组件通过拖拽改变排序
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > List组件通过拖拽改变排序
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-08-27
content_hash: sha256:fb4331ab74ecbb47b1a78f730c113a8255381e2b66a46b05b402098319ec2f14
---

## 问题现象

如何通过List列表实现拖拽改变排序的功能？以及能否做到拖拽排序功能可开关？如何实现按住指定区域才能触发拖拽排序？

## 背景知识

* 通用属性[draggable](../harmonyos-references/ts-universal-attributes-drag-drop.md#draggable)能够设置组件是否允许进行拖拽，能够通过draggable控制拖拽排序功能的开关。
* 在绑定手势方法中，gesture属性能够给组件[绑定手势方法](../harmonyos-references/ts-gesture-settings.md)，手势识别成功后可以通过事件回调通知组件。还可以通过[组合手势](../harmonyos-references/ts-combined-gestures.md)的方法将多种手势组合为复合手势，支持连续识别、并行识别和互斥识别。
* 显式动画组件[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)能够插入自定义过渡动效，在组件出现和消失时，可以通过组件内转场添加动画效果。

## 解决方案

实现拖拽功能的方法与示例代码如下：

1. 定义scaleSelect方法，能够根据当前缩放的列表项和相邻项目返回缩放比例。如果当前列表项正在缩放，返回1.05；如果当前列表项是相邻项目，返回预设的缩放比例；否则返回1。

   ```ts
   scaleSelect(item: number): number {
       if (this.scaleItem === item) {
         return 1.05;
       } else if (this.neighborItem === item) {
         return this.neighborScale;
       } else {
         return 1;
       }
     }
   ```
2. 定义itemMove方法，该方法通过splice在数组中移动项目位置，改变项目排序。

   ```ts
   itemMove(index: number, newIndex: number): void {
       let tmp = this.arr.splice(index, 1);
       this.arr.splice(newIndex, 0, tmp[0]);
     }
   ```
3. 使用长按手势和滑动手势组成顺序识别组合手势。长按手势用于触发缩放效果，拖动手势用于拖动项目改变排序。通过animateTo设置显示动画。在拖动过程中，根据拖动的位移计算相邻项目的缩放比例，并且使用Curves.initCurve和interpolate方法实现平滑的缩放效果。

   ```ts
   // 添加手势
               .gesture(
                 // 以下组合手势为顺序识别，当长按手势事件未正常触发时则不会触发拖动手势事件
                 GestureGroup(GestureMode.Sequence,
                   // 长按手势识别
                   LongPressGesture({ repeat: true })
                     .onAction(() => { // 长按手势识别成功回调
                       // 设置显示动画为阻尼曲线，持续时间为300毫秒
                       this.uiContext.animateTo({ curve: Curve.Friction, duration: 300 }, () => {
                         this.scaleItem = item;
                       });
                     })
                     // 长按手势识别成功，最后一根手指抬起后触发回调
                     .onActionEnd(() => {
                       // 设置显示动画为阻尼曲线，持续时间为300毫秒
                       this.uiContext.animateTo({ curve: Curve.Friction, duration: 300 }, () => {
                         this.scaleItem = -1;
                       });
                     }),
                   // 设置滑动手势事件，任意滑动方向都能够触发事件，触发滑动手势事件的最小滑动距离为0
                   PanGesture({ fingers: 1, direction: null, distance: 0 })
                   // 滑动手势识别成功回调
                     .onActionStart(() => {
                       this.dragItem = item;
                       this.dragRefOffset = 0;
                     })
                     // 滑动手势移动过程中回调
                     .onActionUpdate((event: GestureEvent) => {
                       this.offsetY = event.offsetY - this.dragRefOffset;
                       this.neighborItem = -1;
                       let index = this.arr.indexOf(item);
                       let curveValue: ICurve = curves.initCurve(Curve.Sharp);
                       let value: number = 0;
                       // 根据位移计算相邻项的缩放
                       if (this.offsetY < 0) {
                         value = curveValue.interpolate(-this.offsetY / this.itemIntv);
                         this.neighborItem = this.arr[index - 1];
                         this.neighborScale = 1 - value / 20;
                         console.info(`neighborScale: ${this.neighborScale}`);
                       } else if (this.offsetY > 0) {
                         value = curveValue.interpolate(this.offsetY / this.itemIntv);
                         this.neighborItem = this.arr[index + 1];
                         this.neighborScale = 1 - value / 20;
                       }
                       // 根据位移交换排序
                       if (this.offsetY > this.itemIntv / 2) {
                         // 设置显式动画曲线
                         this.uiContext.animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                           this.offsetY -= this.itemIntv;
                           this.dragRefOffset += this.itemIntv;
                           this.itemMove(index, index + 1);
                         });
                       } else if (this.offsetY < -this.itemIntv / 2) {
                         this.uiContext.animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                           this.offsetY += this.itemIntv;
                           this.dragRefOffset -= this.itemIntv;
                           this.itemMove(index, index - 1);
                         });
                       }
                     })
                     // 滑动手势识别成功，手指抬起后触发回调
                     .onActionEnd(() => {
                       console.info(this.arr.toString());
                       this.uiContext.animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                         this.dragItem = -1;
                         this.neighborItem = -1;
                       });
                       this.uiContext.animateTo({
                         curve: curves.interpolatingSpring(14, 1, 170, 17), delay: 150
                       }, () => {
                         this.scaleItem = -1;
                       });
                     })
                 )
                 // 滑动手势识别成功，接收到触摸取消事件触发回调
                   .onCancel(() => {
                     this.uiContext.animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                       this.dragItem = -1;
                       this.neighborItem = -1;
                     });
                     this.uiContext.animateTo({
                       curve: curves.interpolatingSpring(14, 1, 170, 17), delay: 150
                     }, () => {
                       this.scaleItem = -1;
                     });
                   })
               );
   ```

完整示例代码如下：

```ts
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct ListDrag {
  @State private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  @State dragItem: number = -1; // 当前拖拽的项目
  @State scaleItem: number = -1; // 当前缩放的项目
  @State neighborItem: number = -1; // 相邻项目
  @State neighborScale: number = -1; // 相邻项目的缩放比例
  private dragRefOffset: number = 0; // 拖拽参考偏移
  offsetX: number = 0; // 偏移量
  @State offsetY: number = 0;
  private itemIntv: number = 120; // 项目间隔
  @State moveControls: boolean = false; // 控制拖拽功能
  private uiContext: UIContext = this.getUIContext();

  aboutToAppear() {
    this.uiContext = this.getUIContext();
  }

  scaleSelect(item: number): number {
    if (this.scaleItem === item) {
      return 1.05;
    } else if (this.neighborItem === item) {
      return this.neighborScale;
    } else {
      return 1;
    }
  }

  itemMove(index: number, newIndex: number): void {
    let tmp = this.arr.splice(index, 1);
    this.arr.splice(newIndex, 0, tmp[0]);
  }

  build() {
    Stack() {
      Column() {
        Button('moveControls:' + !this.moveControls)
          .width(200)
          .margin(20)
          .onClick(() => {
            this.moveControls = !this.moveControls;
          });
        List({ space: 20, initialIndex: 0 }) {
          ForEach(this.arr, (item: number) => {
            ListItem() {
              Text('' + item)
                .width('100%')
                .height(100)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor('#f1f3f5')
                // 通过状态变量scaleItem判断是否为组件添加阴影效果
                .shadow(this.scaleItem === item ? {
                  radius: 70,
                  color: '#15000000',
                  offsetX: 0,
                  offsetY: 0
                } :
                  {
                    radius: 0,
                    // 阴影半径为0，相当于没有阴影
                    color: '#15000000',
                    offsetX: 0,
                    offsetY: 0
                  })
                // 设置锐利曲线动画，持续时间为300毫秒
                .animation({ curve: Curve.Sharp, duration: 300 });
            }
            .draggable(this.moveControls)
            .margin({ left: 12, right: 12 })
            // 增加x轴、y轴缩放效果
            .scale({ x: this.scaleSelect(item), y: this.scaleSelect(item) })
            // 设置组件的堆叠顺序，实现拖拽过程中被拖拽组件覆盖其他组件的效果
            .zIndex(this.dragItem === item ? 1 : 0)
            // 设置页面转场时的纵向的平移距离
            .translate(this.dragItem === item ? { y: this.offsetY } : { y: 0 })
            // 添加手势
            .gesture(
              // 以下组合手势为顺序识别，当长按手势事件未正常触发时则不会触发拖动手势事件
              GestureGroup(GestureMode.Sequence,
                // 长按手势识别
                LongPressGesture({ repeat: true })
                  .onAction(() => { // 长按手势识别成功回调
                    // 设置显示动画为阻尼曲线，持续时间为300毫秒
                    this.uiContext.animateTo({ curve: Curve.Friction, duration: 300 }, () => {
                      this.scaleItem = item;
                    });
                  })
                  // 长按手势识别成功，最后一根手指抬起后触发回调
                  .onActionEnd(() => {
                    // 设置显示动画为阻尼曲线，持续时间为300毫秒
                    this.uiContext.animateTo({ curve: Curve.Friction, duration: 300 }, () => {
                      this.scaleItem = -1;
                    });
                  }),
                // 设置滑动手势事件，任意滑动方向都能够触发事件，触发滑动手势事件的最小滑动距离为0
                PanGesture({ fingers: 1, direction: null, distance: 0 })
                // 滑动手势识别成功回调
                  .onActionStart(() => {
                    this.dragItem = item;
                    this.dragRefOffset = 0;
                  })
                  // 滑动手势移动过程中回调
                  .onActionUpdate((event: GestureEvent) => {
                    this.offsetY = event.offsetY - this.dragRefOffset;
                    this.neighborItem = -1;
                    let index = this.arr.indexOf(item);
                    let curveValue: ICurve = curves.initCurve(Curve.Sharp);
                    let value: number = 0;
                    // 根据位移计算相邻项的缩放
                    if (this.offsetY < 0) {
                      value = curveValue.interpolate(-this.offsetY / this.itemIntv);
                      this.neighborItem = this.arr[index - 1];
                      this.neighborScale = 1 - value / 20;
                      console.info(`neighborScale: ${this.neighborScale}`);
                    } else if (this.offsetY > 0) {
                      value = curveValue.interpolate(this.offsetY / this.itemIntv);
                      this.neighborItem = this.arr[index + 1];
                      this.neighborScale = 1 - value / 20;
                    }
                    // 根据位移交换排序
                    if (this.offsetY > this.itemIntv / 2) {
                      // 设置显式动画曲线
                      this.uiContext.animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                        this.offsetY -= this.itemIntv;
                        this.dragRefOffset += this.itemIntv;
                        this.itemMove(index, index + 1);
                      });
                    } else if (this.offsetY < -this.itemIntv / 2) {
                      this.uiContext.animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                        this.offsetY += this.itemIntv;
                        this.dragRefOffset -= this.itemIntv;
                        this.itemMove(index, index - 1);
                      });
                    }
                  })
                  // 滑动手势识别成功，手指抬起后触发回调
                  .onActionEnd(() => {
                    console.info(this.arr.toString());
                    this.uiContext.animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                      this.dragItem = -1;
                      this.neighborItem = -1;
                    });
                    this.uiContext.animateTo({
                      curve: curves.interpolatingSpring(14, 1, 170, 17), delay: 150
                    }, () => {
                      this.scaleItem = -1;
                    });
                  })
              )
              // 滑动手势识别成功，接收到触摸取消事件触发回调
                .onCancel(() => {
                  this.uiContext.animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                    this.dragItem = -1;
                    this.neighborItem = -1;
                  });
                  this.uiContext.animateTo({
                    curve: curves.interpolatingSpring(14, 1, 170, 17), delay: 150
                  }, () => {
                    this.scaleItem = -1;
                  });
                })
            );
          }, (item: number) => item.toString());
        };
      }
      .width('100%')
      .height('100%')
      .padding({ top: 5 });
    };
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/r8l3dsLYSfmwyVdiHmUNQg/zh-cn_image_0000002691501638.png "点击放大")

## 常见FAQ

Q：二级嵌套List中使用什么方法触发拖拽回调？

A：使用[onDragStart](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)作为在拖拽开始时触发的回调；拖拽结束时的回调函数使用List组件的方法[onItemDrop](../harmonyos-references/ts-container-list.md#onitemdrop8)绑定列表元素作为拖拽释放目标，当在列表元素内停止拖拽时触发。

Q：通过onItemDrag实现拖拽改变排序，拖拽开始时，手指放在子组件的左侧或右侧，被拖拽的子组件就会偏左侧或偏右，如何解决？

A：基于onItemDrag实现的拖拽，拖拽的小窗是基于手指位置居中的，改用手势实现拖拽即可。

Q：在分组外添加了分组标题如：“分组一”，如何让标题参与到拖拽排序中？

A：可以将标题用ListItem包裹，参与List排序。

Q：Grid能够使用[supportAnimation](../harmonyos-references/ts-container-grid.md#supportanimation8)设置动画属性实现拖拽动画，List如何实现拖拽动画？

A：List组件不支持设置supportAnimation属性，但是可以通过使用onMove方法实现拖拽动画，也可以结合拖拽事件、组合手势、动画效果来实现拖拽动画效果，具体实现可参考解决方案。

Q：拖拽时被拖拽的项消失，不跟随手指移动，如何解决？

A：通常是因为[onItemDragStart](../harmonyos-references/ts-container-list.md#onitemdragstart8)没有返回有效的拖拽预览Builder。原节点进入拖拽状态后会从原位置让位，跟手显示的部分需要由返回的CustomBuilder提供。

Q：如何使用onMove简化拖拽排序实现？

A：以ForEach或[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)的[onMove](../harmonyos-references/ts-universal-attributes-drag-sorting.md#onmove)作为数据换位入口，让List负责长按、让位和排序过程，[onItemDragStart](../harmonyos-references/ts-container-list.md#onitemdragstart8)只负责返回轻量预览。注意不要同时在onMove和[onItemDrop](../harmonyos-references/ts-container-list.md#onitemdrop8)中各移动一次数据，否则会出现二次换位或索引错乱。

Q：列表数据量较大时，拖拽排序的性能如何保证？

A：建议改用[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)，数据源实现移动并只通知对应的move变化，不要整表刷新。key必须使用稳定且唯一的业务ID，不能使用index，否则移动后会产生节点复用错位。预览只保留文字、缩略图等轻量内容，不要在预览中加载网络图片或叠加重度模糊效果。不要在[onItemDragMove](../harmonyos-references/ts-container-list.md#onitemdragmove8)的每一帧修改整个数组，只在onMove或最终落点更新数据。List的editMode已被标记为废弃，不需要依赖它开启排序，绑定动态节点的onMove即可。

Q：拖拽预览图跟手指位置始终有偏移如何解决？

A：确保[onDragStart](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)返回的预览组件与原组件的尺寸、边距完全一致，无额外布局偏移。onDragStart的extraInfo参数无法控制预览位置偏移。

Q：拖拽手势与列表滑动手势冲突导致列表异常滚动如何解决？

A：通过[draggable](../harmonyos-references/ts-universal-attributes-drag-drop.md#draggable)属性控制组件是否允许拖拽，在不需要拖拽时将draggable设为false，避免拖拽手势与滑动手势冲突。

Q：跨组件拖拽时onDrop中获取的DragItem数据为空如何解决？

A：跨组件拖拽需要正确配置拖拽数据传递，确保在onDragStart的extraInfo中设置了需要传递的数据，并在onDrop中通过DragItem.getExtraData()正确解析。具体实现可参考[List跨列表拖拽示例](../harmonyos-references/ts-container-list.md#示例15在两个列表之间实现拖拽功能)。
