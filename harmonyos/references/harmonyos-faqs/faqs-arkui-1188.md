---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1188
title: GridItem包含图片时，拖拽图片无法交换位置
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > GridItem包含图片时，拖拽图片无法交换位置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9cc9afcdf1675de97c5a8dc3260cc4060e4364eed4e6196f11ea37bfb7f5c995
---

## 问题现象

Grid拖拽场景中，如果GridItem中包含图片，则在拖拽图片时只有拖拽动画，没有交换元素功能。

现象如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/hlg7aYFQR2mE9_q75EAfmA/zh-cn_image_0000002628592956.png)

## 背景知识

* [onItemDragStart](../harmonyos-references/ts-container-grid.md#onitemdragstart8)回调在开始拖拽网格元素时触发，[onItemDrop](../harmonyos-references/ts-container-grid.md#onitemdrop8)回调当GridItem停止拖拽时触发。
* [Image组件](../harmonyos-references/ts-basic-components-image.md)的[draggable属性](../harmonyos-references/ts-basic-components-image.md#draggable9)能够设置组件默认拖拽效果，默认值为true。

## 解决方案

Grid拖拽场景需要调用onItemDragStart和onItemDrop回调，而Image组件的draggable属性默认值为true，在点击图片时，优先响应的是draggable属性，导致无法触发Grid组件的onItemDragStart回调，因此可以将Image组件的draggable属性改为false即可正常触发onItemDragStart回调，从而正常实现交换位置功能。完整示例代码如下：

```ts
@Entry
@Component
struct Second {
  @State addedItems: string[] = ['1', '2', '3', '4', '5', '6', '7', '8'];
  private scroller: Scroller = new Scroller();

  // 设置拖拽过程样式
  @Builder
  dragItem(item: string) {
    Column() {
      Image($r('app.media.startIcon')) // 仅供参考，需根据业务场景更换
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

  build() {
    Column() {
      Grid(this.scroller) {
        ForEach(this.addedItems, (item: string) => {
          GridItem() {
            Column() {
              Image($r('app.media.startIcon')) // 仅供参考，需根据业务场景更换
                .width(44)
                .height(44)
                .objectFit(ImageFit.Contain)
                .draggable(false); // 将draggable属性设置为false
              Text(`index:${item}`)
                .fontSize(12)
                .margin({ top: 5 });
            }
            .height(99);
          };
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
      .editMode(true) // 设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem
      .onItemDragStart(((event: ItemDragInfo, index: number) => { // 第一次拖拽此事件绑定的组件时，触发回调
        console.log('onItemDragStart');
        return this.dragItem(this.addedItems[index]); // 设置拖拽过程中显示的图片
      }))
      .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number,
        isSuccess: boolean) => { // 绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调
        console.log('onItemDrop');
        // isSuccess=false时，说明drop的位置在grid外部；insertIndex > length时，说明有新增元素的事件发生
        if (!isSuccess || insertIndex >= this.addedItems.length) {
          return;
        }
        console.info( itemIndex + '', insertIndex + ''); // itemIndex拖拽起始位置，insertIndex拖拽插入位置
        this.changeIndex(itemIndex, insertIndex);
      });
    }
    .height('100%')
    .width('100%');
  }

  // 交换数组位置
  changeIndex(index1: number, index2: number) {
    let temp: string;
    temp = this.addedItems[index1];
    this.addedItems[index1] = this.addedItems[index2];
    this.addedItems[index2] = temp;
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/-hCYn01kRRKPNWfv2pvOtA/zh-cn_image_0000002658832209.png)
