---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-565
title: 如何给LazyForEach中的listitem添加动画效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何给LazyForEach中的listitem添加动画效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c43a351debbe63671fab70479ee3e6186b09f46df19009860b68cfd215acfeb5
---

## 问题现象

使用LazyForEach渲染一个List，如何给每个ListItem都添加动画效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/SyWZ9iH9S_qIHKBZ6Ero-A/zh-cn_image_0000002658911355.gif "点击放大")

## 背景知识

* [@AnimatableExtend](../harmonyos-guides/arkts-animatable-extend.md)可以将一个属性定义为可动画属性，例如给fontSize添加可动画属性即可实现字体大小变化时的动画。
* 开发者可以使用[@ObservedV2装饰器和@Trace装饰器](../harmonyos-guides/arkts-new-observedv2-and-trace.md)装饰类以及类中的属性。使被@Trace装饰的属性成为状态变量，从而去刷新UI动画。

## 解决方案

1. 定义LazyForEach的数据类MaterialWrap，并用@ObservedV2装饰器和@Trace装饰器观察其中属性。

   ```screen
   @ObservedV2
   export class MaterialWrap {
     @Trace size: number;

     constructor(size: number) {
       this.size = size;
     }
   }
   ```
2. 使用@AnimatableExtend定义用于执行动画的属性。

   ```screen
   // 使用fontSize作为动画属性
   @AnimatableExtend(Button)
   function animatableFontSize(size: number) {
     .fontSize(size);
   }
   ```
3. 使用LazyForEach进行渲染时利用item.size的变化去执行动画效果。

   ```screen
   List({ space: 24 }) {
     LazyForEach(this.materialsDataSource, (item: MaterialWrap) => {
       ListItem() {
         Button('button')
           .animatableFontSize(item.size)
           .animation({ duration: 1000, curve: Curve.Linear });
       }
       .onClick(() => {
         item.size = item.size === 10 ? 20 : 10;
       });
     }, (item: MaterialWrap) => item.size.toString());
   }
   ```

完整示例参考如下：

```screen
class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: MaterialWrap[] = [];

  public totalCount(): number {
    return this.originDataArray.length;
  }

  public getData(index: number): MaterialWrap {
    return this.originDataArray[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener');
      this.listeners.push(listener);
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener');
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

  notifyDatasetChange(operations: DataOperation[]): void {
    this.listeners.forEach(listener => {
      listener.onDatasetChange(operations);
    });
  }
}

class FilterItemDataSource extends BasicDataSource {
  filterDataItems: MaterialWrap[] = [];

  public totalCount(): number {
    return this.filterDataItems.length;
  }

  public getData(index: number): MaterialWrap {
    return this.filterDataItems[index];
  }

  public pushData(data: MaterialWrap): void {
    this.filterDataItems.push(data);
    this.notifyDataAdd(this.filterDataItems.length - 1);
  }
}

@ObservedV2
export class MaterialWrap {
  @Trace size: number;

  constructor(size: number) {
    this.size = size;
  }
}

@Entry
@Component
struct AnimatableList {
  @State private materialsDataSource: FilterItemDataSource = new FilterItemDataSource();
  private dataOrign: MaterialWrap[] = [];

  aboutToAppear() {
    for (let i = 0; i <= 2; i++) {
      this.dataOrign.push(new MaterialWrap(10));
    }
    this.materialsDataSource.filterDataItems = this.dataOrign;
    this.materialsDataSource.notifyDataReload();
  }

  build() {
    Column() {
      List({ space: 24 }) {
        LazyForEach(this.materialsDataSource, (item: MaterialWrap) => {
          ListItem() {
            Button('button')
              .animatableFontSize(item.size)
              .animation({ duration: 1000, curve: Curve.Linear });
          }
          .onClick(() => {
            item.size = item.size === 10 ? 20 : 10;
          });
        }, (item: MaterialWrap) => item.size.toString());
      }

      .cachedCount(5)
      .alignListItem(ListItemAlign.Center);
    }
    .justifyContent(FlexAlign.Center)
    .height('100%');

  }
}

// 使用fontSize作为动画属性
@AnimatableExtend(Button)
function animatableFontSize(size: number) {
  .fontSize(size);
}
```
