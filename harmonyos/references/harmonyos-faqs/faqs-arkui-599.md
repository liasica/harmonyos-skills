---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-599
title: 停止滑动后Swiper的子组件获取的坐标发生骤变怎么解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 停止滑动后Swiper的子组件获取的坐标发生骤变怎么解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:db40c8005bd33ee4525f38877f999b1658af014a3e073839ddeff9e6824771a1
---

## 问题现象

[Swiper](../harmonyos-references/ts-container-swiper.md)（滑块视图容器）的子组件在手指拖动时通过触发[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)事件获取到的x坐标是平滑变动的，但在手指抬起后坐标会骤变。

关键代码如下：

```screen
Swiper() {
  LazyForEach(this.dataSource, (item: string, index: number) => {
    Column() {
      Image(item)
        .width(this.itemWidth)
        .height(this.itemHeight)
        .objectFit(ImageFit.Fill)
        .borderRadius(5)
    }
    .onAreaChange((_oldValue: Area, newValue: Area) => {
      this.func(index, _oldValue, newValue)
      this.getOldValue = _oldValue
      this.getNewValue = newValue
    })
  })
}
.loop(true)
.displayCount(1)
.prevMargin(this.previousWidth)
.nextMargin(this.previousWidth)
.itemSpace(10)
.width('100%')
.onAreaChange((_oldValue: Area, newValue: Area) => {
  this.bannerWidth = NumberUtils.lengthToNum(newValue.width)
})
.autoPlay(true)
```

## 背景知识

[组件区域变化事件](../harmonyos-references/ts-universal-component-area-change-event.md)是指组件显示的尺寸、位置等发生变化时触发的事件，onAreaChange可以响应组件位置发生变化时的回调，Swiper的子组件可通过调用该方法监听位置坐标的变化。

## 问题定位

手指抬起之后，Swiper默认的动画是隐式动画，所以无法触发onAreaChange事件，只在最后组件动画停止，位置确定下来后触发onAreaChange事件，从而出现坐标骤变的问题现象。

## 分析结论

隐式动画无法触发onAreaChange事件导致出现组件坐标骤变，可通过将隐式动画变为显式动画来解决。

## 修改建议

1. 当Swiper数据源三个及以上的场景，可以通过在Swiper外设置一个空的[onContentDidScroll](../harmonyos-references/ts-container-swiper.md#oncontentdidscroll12)(()=>{})实现将动画变为显式动画，进而实现手抬起坐标也平滑变化的效果；
2. 在Swiper数据源只有两个的场景，因为在循环场景下，设置prevMargin和nextMargin属性，使得Swiper前后端显示同一页面时，onContentDidScroll接口是不生效的，所以需要把loop属性设置为false，这样可以实现组件坐标平滑变动的效果。

   完整代码如下：

   ```screen
   import { common } from '@kit.AbilityKit';
   import { UIContext } from '@kit.ArkUI';

   export class NumberUtils {
     static lengthToNum(length: Length): number {
       if (typeof length === 'number') {
         return (length as number);
       } else if (typeof length === 'string') {
         return parseFloat(length as string);
       } else {
         let parseRes = length as Resource;
         // 获取上下文
         return (new UIContext().getHostContext() as common.UIAbilityContext).resourceManager.getNumber(parseRes.id);
       }
     }
   }

   @Entry
   @Component
   struct CoordinateChanged {
     itemWidth: number = 300;
     itemHeight: number = 163;
     unselectScale: number = 0.83;
     itemSpace: number = 10;
     // Swiper轮播的图片列表，开发者可根据真实场景进行替换
     @State imgList: Resource [] = [
       $r('app.media.fig1'),
       $r('app.media.fig2'),
       $r('app.media.fig3')
     ];
     @State dataSource: MyDataSource = new MyDataSource(this.imgList);
     @State previousWidth: number = 0;
     @State @Watch('onBannerWidthChanged') bannerWidth: number = 0;
     @State viewInfo: Area[] = [];
     @State xL: number = 0;
     @State xC: number = 0;
     @State xR: number = 0;
     // 旧的坐标值
     @State getOldValue: Area = {
       width: 0,
       height: 0,
       position: { x: 0, y: 0 },
       globalPosition: { x: 0, y: 0 }
     };
     // 新的坐标值
     @State getNewValue: Area = {
       width: 0,
       height: 0,
       position: { x: 0, y: 0 },
       globalPosition: { x: 0, y: 0 }
     };

     // 横幅宽度变化时修改xL、xC、xR的值
     onBannerWidthChanged() {
       if (this.bannerWidth > 0) {
         this.previousWidth = (this.bannerWidth - this.itemWidth - this.itemSpace * 2) / 2;
         this.xC = this.bannerWidth / 2;
         this.xL = this.xC - this.itemWidth - this.itemSpace;
         this.xR = (this.xC - this.xL) + this.xC;
       }
     }

     // 获取实时坐标值
     func(index: number, _oldValue: Area, newValue: Area) {
       if (index >= this.viewInfo.length) {
         this.viewInfo.push(newValue);
       } else {
         this.viewInfo[index] = newValue;
       }
     }

     build() {
       Column() {
         Swiper() {
           LazyForEach(this.dataSource, (item: string, index: number) => {
             Column() {
               Image(item)
                 .width(this.itemWidth)
                 .height(this.itemHeight)
                 .objectFit(ImageFit.Fill)
                 .borderRadius(5);
             }
             .onAreaChange((_oldValue: Area, newValue: Area) => {
               this.func(index, _oldValue, newValue);
               this.getOldValue = _oldValue;
               this.getNewValue = newValue;
             });
           });
         }
         .onContentDidScroll(() => {
         })
         // 在Swiper数据源少于三个的场景，需要把loop属性设置为false，这样可以实现组件坐标平滑变动的效果
         .loop(this.imgList.length > 2 ? true : false)
         .displayCount(1)
         .prevMargin(this.previousWidth)
         .nextMargin(this.previousWidth)
         .itemSpace(10)
         .width('100%')
         .onAreaChange((_oldValue: Area, newValue: Area) => {
           this.bannerWidth = NumberUtils.lengthToNum(newValue.width);
         })
         .autoPlay(true);

         // 展示横幅的坐标属性
         Column({ space: 10 }) {
           Column() {
             Text(`Params`)
               .fontWeight(FontWeight.Bold);
             Text(`bannerWidth: ${this.bannerWidth}`).margin({ top: 8 });
             Text(`xL: ${this.xL}, xC: ${this.xC}, xR: ${this.xR}`);
           }
           .width('100%')
           .borderColor(Color.Brown)
           .borderWidth(1)
           .borderRadius(5)
           .padding(5)
           .alignItems(HorizontalAlign.Start);

           // 展示每张图片的坐标属性
           ForEach(this.viewInfo, (item: Area, index: number) => {
             Column() {
               Text(`Item[${index}]`)
                 .fontWeight(FontWeight.Bold);
               Text(`width: ${NumberUtils.lengthToNum(item.width)}, height: ${NumberUtils.lengthToNum(item.height)}`)
                 .margin({ top: 8 });
               Text(`localX: ${NumberUtils.lengthToNum(item.position.x ??
                 0)}, localY: ${NumberUtils.lengthToNum(item.position.y ?? 0)}`);
               Text(`globalX: ${NumberUtils.lengthToNum(item.globalPosition.x ??
                 0)}, globalY: ${NumberUtils.lengthToNum(item.globalPosition.y ?? 0)}`);
             }
             .width('100%')
             .borderColor(Color.Brown)
             .borderWidth(1)
             .borderRadius(5)
             .padding(5)
             .alignItems(HorizontalAlign.Start);
           });
         }.width('100%')
         .padding({ left: 15, right: 15 })
         .margin({ top: 20 });
       }
       .height('100%')
       .width('100%');
     }
   }

   // 设置数据源
   class MyDataSource implements IDataSource {
     private list: Resource[] = [];

     constructor(list: Resource[]) {
       this.list = list;
     }

     totalCount(): number {
       return this.list.length;
     }

     getData(index: number): Resource {
       return this.list[index];
     }

     registerDataChangeListener(): void {
     }

     unregisterDataChangeListener() {
     }
   }
   ```
