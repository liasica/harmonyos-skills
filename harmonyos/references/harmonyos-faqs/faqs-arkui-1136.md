---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1136
title: LazyForEach渲染的List列表上滑触发刷新动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > LazyForEach渲染的List列表上滑触发刷新动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6db0529cb0568bb9a5d1b048d12a2bab74bbe79bedaf2e2ccf22252e07582141
---

## 问题现象

使用LazyForEach渲染List列表，实现下滑会触发transition动画，但是上滑也会触发动画，如何使其上滑过程中不会触发动画？

问题示意图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/dO5IpjdYRjS8KEBzLuI_rw/zh-cn_image_0000002628569432.gif "点击放大")

## 背景知识

* [transition](../harmonyos-references/ts-transition-animation-component.md)（组件内转场）：transition属性能够在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除。transition函数的入参为组件内转场的效果，可以定义平移、透明度、旋转、缩放这几种转场样式的单个或者组合的转场效果。
* [LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)：能够从提供的数据源中按需迭代数据，并在每次迭代过程中创建相应的组件。当在滚动容器中使用了LazyForEach，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会进行组件销毁回收以降低内存占用。

## 问题定位

当在滚动容器中使用了LazyForEach，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会进行组件销毁回收以降低内存占用，因此当List往下滑动，滚动出可视区域的列表项就会被销毁回收，当再往上回到顶部时，实际上会重新创建列表项，就会出现上滑过程中触发刷新动画。

## 分析结论

LazyForEach回收列表项子组件导致重新渲染而触发上滑时的刷新动画。

## 解决方案

可以根据滑动方向决定是否展示动画，来达到下滑不会触发动画的效果，具体实现为：

1. 实现LazyForEach数据源相关接口，使用BasicDataSource类实现IDataSource接口，负责管理数据变化的监听者和数据本身，可以参考官网[BasicDataSource示例代码](../harmonyos-guides/arkts-rendering-control-lazyforeach.md#basicdatasource示例代码)，并且使用MyDataSource类继承BasicDataSource类，增加自定义的方法，MyDataSource代码如下：

   ```ts
   class MyDataSource extends BasicDataSource {
     private dataArray: string[] = [];

     public totalCount(): number {
       return this.dataArray.length;
     }

     public getData(index: number): string {
       return this.dataArray[index];
     }

     public addData(index: number, data: string): void {
       this.dataArray.splice(index, 0, data);
       this.notifyDataAdd(index);
     }

     public pushData(data: string): void {
       this.dataArray.push(data);
       this.notifyDataAdd(this.dataArray.length - 1);
     }
   }
   ```
2. 定义状态变量，创建数据源data。

   ```ts
   private data: MyDataSource = new MyDataSource();
   @State showItemAnimation: boolean = false;
   @State currentScrollOffsetInList: number = 0;
   private currentScrollStateInList: ScrollState | null = null;
   private lastOffset: number = 0;
   ```
3. 在aboutToAppear生命周期方法中，初始化数据源，向其中添加50个数据项，每个数据项为字符串格式。

   ```ts
   aboutToAppear() {
     for (let i = 0; i <= 50; i++) {
       this.data.pushData(`Hello ${i}`);
     }
   }
   ```
4. 使用LazyForEach来渲染列表项，每个列表项显示一个字符串,并且使用状态变量showItemAnimation决定是否添加动画效果，当showItemAnimation为true时，列表项会显示透明度和位置的动画效果。通过transition属性为列表项添加动画效果：使用TransitionEffect.OPACITY和TransitionEffect.move实现列表项的透明度和位置变化动画，并使用[curves.springMotion](../harmonyos-references/js-apis-curve.md#curvesspringmotion9)，根据index调整延迟，实现类似弹簧动画效果。

   ```ts
   List({ space: 20, initialIndex: 0 }) {
     LazyForEach(this.data, (item: number, index: number) => {
       ListItem() {
         Text('' + item)
           .width('100%')
           .height(100)
           .fontSize(16)
           .textAlign(TextAlign.Center)
           .borderRadius(10)
           .backgroundColor(0xFFFFFF);
       }
       .transition(this.showItemAnimation ?
         TransitionEffect.OPACITY.combine(TransitionEffect.move(TransitionEdge.END))
           .animation({ curve: curves.springMotion(), duration: 300, delay: (index % 10) * 30 }) : null);
     }, (item: string) => item);
   }
   ```
5. 使用[onDidScroll](../harmonyos-references/ts-container-scrollable-common.md#ondidscroll12)监听列表的滚动事件，更新currentScrollOffsetInList和currentScrollStateInList状态。

   根据onDidScroll的参数scrollOffset的正负来决定是否显示动画效果，当滚动到顶部且之前滚动方向为向上时，不显示动画效果。

   ```ts
   .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
     this.currentScrollOffsetInList = scrollOffset;
     this.currentScrollStateInList = scrollState;
     if (scrollOffset != 0) {
       this.lastOffset = scrollOffset;
     }
     this.showItemAnimation = ((scrollOffset <= 0 && this.lastOffset < 0) ? false : true);
   })
   ```

完整示例代码如下：

```ts
import { curves } from '@kit.ArkUI';

class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: string[] = [];

  public totalCount(): number {
    return this.originDataArray.length;
  }

  public getData(index: number): string {
    return this.originDataArray[index];
  }

  // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      this.listeners.push(listener);
    }
  }

  // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      this.listeners.splice(pos, 1);
    }
  }

  // 通知LazyForEach组件需要重载所有子组件
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    });
  }

  // 通知LazyForEach组件需要在index对应索引处添加子组件
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }

  // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    });
  }

  // 通知LazyForEach组件需要在index对应索引处删除该子组件
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    });
  }

  // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    });
  }

  notifyDatasetChange(operations: DataOperation[]): void {
    this.listeners.forEach(listener => {
      listener.onDatasetChange(operations);
    });
  }
}

class MyDataSource extends BasicDataSource {
  private dataArray: string[] = [];

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): string {
    return this.dataArray[index];
  }

  public addData(index: number, data: string): void {
    this.dataArray.splice(index, 0, data);
    this.notifyDataAdd(index);
  }

  public pushData(data: string): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}

@Entry
@Component
struct LazyForEachListTransition {
  private data: MyDataSource = new MyDataSource();
  @State showItemAnimation: boolean = false;
  @State currentScrollOffsetInList: number = 0;
  private currentScrollStateInList: ScrollState | null = null;
  private lastOffset: number = 0;

  aboutToAppear() {
    for (let i = 0; i <= 50; i++) {
      this.data.pushData(`Hello ${i}`);
    }
  }

  build() {
    Column() {
      List({ space: 20, initialIndex: 0 }) {
        LazyForEach(this.data, (item: number, index: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF);
          }
          .transition(this.showItemAnimation ?
          TransitionEffect.OPACITY.combine(TransitionEffect.move(TransitionEdge.END))
            .animation({ curve: curves.springMotion(), duration: 300, delay: (index % 10) * 30 }) : null);
        }, (item: string) => item);
      }
      .listDirection(Axis.Vertical) // 排列方向
      .scrollBar(BarState.Off)
      .friction(0.6)
      .divider({
        strokeWidth: 2,
        color: 0xFFFFFF,
        startMargin: 20,
        endMargin: 20
      }) // 每行之间的分界线
      .edgeEffect(EdgeEffect.Spring) // 边缘效果设置为Spring
      .onScrollIndex(() => {})
      .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
        this.currentScrollOffsetInList = scrollOffset;
        this.currentScrollStateInList = scrollState;
        if (scrollOffset != 0) {
          this.lastOffset = scrollOffset;
        }
        this.showItemAnimation = ((scrollOffset <= 0 && this.lastOffset < 0) ? false : true);
      })
      .width('90%');
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 });
  }
}
```

修正效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/JHayv-C8QOWw_M9zIReziw/zh-cn_image_0000002628409532.png "点击放大")

## 总结

配合刷新动画的滚动组件在嵌套LazyForEach时，需注意LazyForEach的特性，控制相应的组件的动画效果不受LazyForEach影响，以免出现动画不正常刷新的情况。
