---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-770
title: 解决LazyForEach懒加载数据UI渲染失败的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 解决LazyForEach懒加载数据UI渲染失败的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:41+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:28a3ac94a904eac1cbd7a96affbb88a5a7890aee352599be2159dafeebf99d33
---

## 问题现象

使用LazyForEach从提供的数据源中按需迭代数据时，数据发生了变化，但是UI未自动渲染，导致数据与页面展示不一致。

## 背景知识

[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)从提供的数据源中按需迭代数据，并在每次迭代过程中创建相应的组件，可以保证数据加载以及绘制的流畅度，提升使用体验。LazyForEach依赖生成的键值判断是否刷新子组件，若键值不发生改变，则无法触发LazyForEach刷新对应的子组件。

## 解决方案

### 场景一：外层组件高度问题导致渲染失败。

* **原因：** 懒加载外层组件如果未设置高度，可能导致框架无法判断哪些组件需要显示或缓存，导致渲染失败。同时外层组件的高度只有在小于数据的总高度，且小于屏幕的高度时，懒加载才会生效。
* **修改方式：** 为外层组件设置合适的固定高度。

  示例代码如下：

  ```ts
  List() {
    ListItemGroup() {
      ListItem() {
        List() {
          LazyForEach(this.data, (index: number) => {
            ListItem() {
              Text(`index = ${index}`)
            }
            .backgroundColor(Color.Green)
          })
        }
        // 为外层组件添加高度
        .height(300)
      }
    }
  }
  ```

### 场景二：错误键值导致渲染异常。

* **原因：** LazyForEach依赖唯一键值来标识组件，若键值重复，会导致组件渲染异常。
* **修改方式：** 使用自定义keyGenerator函数，确保每个数据项生成唯一键值。比如生成键值时添加Math.random或Date.now信息。

  示例代码如下：

  ```ts
  List() {
    LazyForEach(this.data, (index: number) => {
      ListItem() {
        Text(`index = ${index}`)
          .reuseId('article')
      }
      // 需确保每个index值唯一
    }, (index: number) => index.toString())
  }
  ```

### 场景三：没有重建数据项导致渲染失败。

* **原因：** 在数据变化时，需重建数据项，更新index索引。
* **修改方式：** 构造reloadData方法，在改变数据项后调用，重建后面的数据项。详细可参考：[渲染结果非预期](../harmonyos-guides/arkts-rendering-control-lazyforeach.md#删除节点后渲染结果非预期)。

完整代码示例如下：

1. LazyForEach的数据源需要实现IDataSource接口。

   ```ts
   class BasicDataSource<T>  implements IDataSource {
     private listeners: DataChangeListener[] = [];
     private originDataArray: T[] = [];

     public totalCount(): number {
       return this.originDataArray.length;
     }

     public getData(index: number): T {
       return this.originDataArray[index];
     }

     registerDataChangeListener(listener: DataChangeListener): void {
       if (this.listeners.indexOf(listener) < 0) {
         console.info('add listener');
         this.listeners.push(listener);
       };
     }

     unregisterDataChangeListener(listener: DataChangeListener): void {
       const pos = this.listeners.indexOf(listener);
       if (pos >= 0) {
         console.info('remove listener');
         this.listeners.splice(pos, 1);
       };
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

   // LazyForEach的数据源需要实现IDataSource接口
   export class DataSource extends BasicDataSource<number> {
     private dataArray: number[] = [];

     public getAllData(): number[] {
       return this.dataArray;
     }

     public totalCount(): number {
       return this.dataArray.length;
     }

     public getData(index: number): number {
       return this.dataArray[index];
     }

     public pushData(data: number): void {
       this.dataArray.push(data);
       this.notifyDataAdd(this.dataArray.length - 1);
     }
   }
   ```
2. 加载数据，渲染UI。

   ```ts
   import { DataSource } from '../models/DataSource';

   @Entry
   @Component
   struct Index {
     // LazyForEach的数据源需要实现IDataSource接口，DataSource为自定义类，已实现IDataSource接口
     @State data: DataSource = new DataSource();

     // 构造数据
     aboutToAppear(): void {
       for (let i = 0; i < 50; i++) {
         this.data.pushData(i);
       };
     }

     build() {
       Column() {
         Row() {
           List() {
             ListItemGroup() {
               ListItem() {
                 List() {
                   LazyForEach(this.data, (index: number) => {
                     ListItem() {
                       Text(`index = ${index}`)
                     }
                     .backgroundColor(Color.Green)
                   })
                 }
                 // 为外层组件添加高度
                 .height(300)
               }
             }
           }
           .width('50%')
           .height('100%')

           List() {
             LazyForEach(this.data, (index: number) => {
               ListItem() {
                 Text(`index = ${index}`)
                   .reuseId('article')
               }
               // 需确保每个index值唯一
             }, (index: number) => index.toString())
           }
           .cachedCount(10)
           .width('50%')
           .height('100%')
           .edgeEffect(EdgeEffect.None)
           .padding({ left: '10vp', right: '10vp' })

         }
         .width('100%')
         .height('100%')
       }
       .width('100%')
       .height('100%')
     }
   }
   ```

## 常见FAQ

Q：LazyForEach是否适用所有组件实现懒加载？

A：LazyForEach必须在容器组件内使用，仅有List、ListItemGroup、Grid、Swiper以及WaterFlow组件支持数据懒加载（可配置cachedCount属性，即只加载可视部分以及其前后少量数据用于缓冲），其他组件仍然是一次性加载所有的数据。

Q：LazyForEach是否可嵌套使用？

A：容器组件内使用LazyForEach的时候，只能包含一个LazyForEach。以List为例，同时包含ListItem、ForEach、LazyForEach的情形是不推荐的；同时包含多个LazyForEach也是不推荐的。
