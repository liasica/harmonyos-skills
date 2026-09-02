---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-605
title: LazyForEach懒加载修改数据界面不刷新
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > LazyForEach懒加载修改数据界面不刷新
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:51b2f7167ac524185dd1123bfc21b84c8a7b053ea16fbf7b002360e34039158b
---

## 问题现象

使用LazyForEach实现懒加载列表时，修改数据后界面没有刷新，显示内容与实际数据不一致。

## 背景知识

* [onDatasetChange](../harmonyos-references/ts-rendering-control-lazyforeach.md#ondatasetchange12)：进行批量的数据处理后，调用onDatasetChange接口通知组件按照dataOperations刷新组件。
* [DataReloadOperation](../harmonyos-references/ts-rendering-control-lazyforeach.md#datareloadoperation12)：重载所有数据操作。当onDatasetChange含有DataOperationType.RELOAD操作时，其余操作全部失效，框架会自己调用keyGenerator进行键值比对。
* [DataChangeOperation](../harmonyos-references/ts-rendering-control-lazyforeach.md#datachangeoperation12)：改变数据操作。
* LazyForEach提供了参数keyGenerator，如果未定义keyGenerator函数，ArkUI框架将使用默认的键值生成函数：(item: Object, index: number) => { return viewId + '-' + index.toString(); }。其中viewId在编译器转换过程中生成，同一个LazyForEach组件内的viewId一致。详细参考：[键值生成规则](../harmonyos-guides/arkts-rendering-control-lazyforeach.md#键值生成规则)。

## 问题定位

查看数据修改后刷新数据的实现，修改数据后调用刷新的操作是[DataReloadOperation](../harmonyos-references/ts-rendering-control-lazyforeach.md#datareloadoperation12)，查看LazyForEach的参数keyGenerator，调用刷新操作后LazyForEach生成的键值没有变化，界面没有刷新。

```ts
// 数据修改后刷新界面的实现
notifyDataReload() {
  this.listeners.forEach(listener => {
    listener.onDatasetChange([{ type: DataOperationType.RELOAD }]);
  });
}
```

## 分析结论

修改数据后调用的刷新操作是DataReloadOperation，但是LazyForEach的参数keyGenerator生成的键值没有变化，所以界面不会更新。

## 修改建议

* 方案一：修改数据后刷新操作从[DataReloadOperation](../harmonyos-references/ts-rendering-control-lazyforeach.md#datareloadoperation12)改为[DataChangeOperation](../harmonyos-references/ts-rendering-control-lazyforeach.md#datachangeoperation12)，使用DataChangeOperation会重新渲染数据对应组件，界面正常更新。

  ```ts
  notifyDataChange(index: number) {
    this.listeners.forEach(listener => {
      listener.onDatasetChange([{ type: DataOperationType.CHANGE, index: index }]);
    });
  }
  ```
* 方案二：保持[DataReloadOperation](../harmonyos-references/ts-rendering-control-lazyforeach.md#datareloadoperation12)操作，修改LazyForEach的参数keyGenerator，确保修改数据后生成的键值与修改前的键值不同，界面正常更新。

  ```ts
  LazyForEach(this.data2, (p: Person, index: number) => {
    Column({ space: 8 }) {
      // 人员信息
      Row({ space: 12 }) {
        Text(p.name)
          .fontSize(16)
          .fontWeight(FontWeight.Bold);
        Text(p.age + '岁')
          .fontSize(14)
          .fontColor('#666666');
        Text('#index: ' + index)
          .fontSize(12)
          .fontColor('#999999');
      }
      .width('100%')
      .justifyContent(FlexAlign.Center);

      // 按钮组
      // 设置keyGenerator场景调用notifyDataReload和notifyDataChange界面均会更新
      Row({ space: 12 }) {
        // RELOAD按钮
        Button('RELOAD +')
          .height(36)
          .width(100)
          .backgroundColor('#FF6B3C')
          .onClick(() => {
            p.age++;
            this.data2.notifyDataReload();
          });

        // CHANGE按钮
        Button('CHANGE +')
          .height(36)
          .width(100)
          .backgroundColor('#0A59F7')
          .onClick(() => {
            p.age++;
            this.data2.notifyDataChange(index);
          });
      };
    }
    .width('100%')
    .padding(12)
    .backgroundColor('#FAFAFA')
    .borderRadius(8);
  }, (p: Person) => JSON.stringify(p)); // keyGenerator
  ```

完整代码示例：

```ts
@Entry
@Component
struct LazyForeachPage {
  @State data1: MyDemoDataSource<Person> = new MyDemoDataSource<Person>([
    new Person('张三', 20)
  ]);
  @State data2: MyDemoDataSource<Person> = new MyDemoDataSource<Person>([
    new Person('李四', 20)
  ]);

  build() {
    Column() {
      // 标题
      Text('LazyForEach 刷新机制对比')
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .margin({ top: 16, bottom: 16 });

      Column() {
        // ===== 未设置keyGenerator =====
        Column() {
          // 卡片标题
          Column() {
            Text('未设置 keyGenerator')
              .fontSize(18)
              .fontWeight(FontWeight.Medium);
          }
          .width('100%')
          .padding(12)
          .backgroundColor('#F0F7FF')
          .borderRadius({ topLeft: 12, topRight: 12 });

          // 说明区域 - 1,2,3点说明
          Column() {
            Text('1. 数据未设置唯一key标识')
              .fontSize(14)
              .width('100%');
            Text('2. RELOAD ❌ 点击后界面不会更新')
              .fontSize(14)
              .fontColor('#FF6B3C')
              .width('100%');
            Text('3. CHANGE ✅ 点击后界面会更新')
              .fontSize(14)
              .fontColor('#0A59F7')
              .width('100%');
          }
          .width('100%')
          .padding(12)
          .backgroundColor('#FFFFFF');

          // 数据列表
          Column({ space: 12 }) {
            LazyForEach(this.data1, (p: Person, index: number) => {
              Column({ space: 8 }) {
                // 人员信息
                Row({ space: 12 }) {
                  Text(p.name)
                    .fontSize(16)
                    .fontWeight(FontWeight.Bold);
                  Text(p.age + '岁')
                    .fontSize(14)
                    .fontColor('#666666');
                  Text('#index: ' + index)
                    .fontSize(12)
                    .fontColor('#999999');
                }
                .width('100%')
                .justifyContent(FlexAlign.Center);

                // 按钮组
                Row({ space: 12 }) {
                  // RELOAD按钮 - 置灰显示
                  // 未设置keyGenerator场景调用notifyDataReload界面不会更新
                  Button('RELOAD +')
                    .height(36)
                    .width(100)
                    .backgroundColor('#CCCCCC')
                    .fontColor('#666666')
                    .onClick(() => {
                      p.age++;
                      this.data1.notifyDataReload();
                    });

                  // CHANGE按钮
                  // 未设置keyGenerator场景调用notifyDataChange界面会更新
                  Button('CHANGE +')
                    .height(36)
                    .width(100)
                    .backgroundColor('#0A59F7')
                    .onClick(() => {
                      p.age++;
                      this.data1.notifyDataChange(index);
                    });
                };
              }
              .width('100%')
              .padding(12)
              .backgroundColor('#FAFAFA')
              .borderRadius(8);
            });
          }
          .padding(12)
          .backgroundColor('#FFFFFF')
          .borderRadius({ bottomLeft: 12, bottomRight: 12 });
        }
        .layoutWeight(1)
        .margin(8)
        .backgroundColor('#FFFFFF')
        .borderRadius(12)
        .shadow({ radius: 4, color: '#1A000000' });

        // ===== 设置keyGenerator =====
        Column() {
          // 卡片标题
          Column() {
            Text('设置 keyGenerator')
              .fontSize(18)
              .fontWeight(FontWeight.Medium);
          }
          .width('100%')
          .padding(12)
          .backgroundColor('#F0F7FF')
          .borderRadius({ topLeft: 12, topRight: 12 });

          // 说明区域 - 1,2,3点说明
          Column() {
            Text('1. 数据使用JSON字符串作为唯一key')
              .fontSize(14)
              .width('100%');
            Text('2. RELOAD ✅ 点击后界面会更新')
              .fontSize(14)
              .fontColor('#FF6B3C')
              .width('100%');
            Text('3. CHANGE ✅ 点击后界面会更新')
              .fontSize(14)
              .fontColor('#0A59F7')
              .width('100%');
          }
          .width('100%')
          .padding(12)
          .backgroundColor('#FFFFFF');

          // 数据列表
          Column({ space: 12 }) {
            LazyForEach(this.data2, (p: Person, index: number) => {
              Column({ space: 8 }) {
                // 人员信息
                Row({ space: 12 }) {
                  Text(p.name)
                    .fontSize(16)
                    .fontWeight(FontWeight.Bold);
                  Text(p.age + '岁')
                    .fontSize(14)
                    .fontColor('#666666');
                  Text('#index: ' + index)
                    .fontSize(12)
                    .fontColor('#999999');
                }
                .width('100%')
                .justifyContent(FlexAlign.Center);

                // 按钮组
                // 设置keyGenerator场景调用notifyDataReload和notifyDataChange界面均会更新
                Row({ space: 12 }) {
                  // RELOAD按钮
                  Button('RELOAD +')
                    .height(36)
                    .width(100)
                    .backgroundColor('#FF6B3C')
                    .onClick(() => {
                      p.age++;
                      this.data2.notifyDataReload();
                    });

                  // CHANGE按钮
                  Button('CHANGE +')
                    .height(36)
                    .width(100)
                    .backgroundColor('#0A59F7')
                    .onClick(() => {
                      p.age++;
                      this.data2.notifyDataChange(index);
                    });
                };
              }
              .width('100%')
              .padding(12)
              .backgroundColor('#FAFAFA')
              .borderRadius(8);
            }, (p: Person) => JSON.stringify(p)); // keyGenerator
          }
          .padding(12)
          .backgroundColor('#FFFFFF')
          .borderRadius({ bottomLeft: 12, bottomRight: 12 });
        }
        .layoutWeight(1)
        .margin(8)
        .backgroundColor('#FFFFFF')
        .borderRadius(12)
        .shadow({ radius: 4, color: '#1A000000' });
      }
      .width('100%')
      .padding(8)
      .layoutWeight(1);
    }
    .height('100%')
    .width('100%')
    .backgroundColor('#F5F5F5')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
}

class Person {
  name: string;
  age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }
}

class BasicDataSource<T> implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: T[] = [];

  totalCount(): number {
    return 0;
  }

  getData(index: number): T | undefined {
    return this.originDataArray[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      this.listeners.push(listener);
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const position = this.listeners.indexOf(listener);
    if (position >= 0) {
      this.listeners.splice(position, 1);
    }
  }

  notifyDataReload() {
    this.listeners.forEach(listener => {
      listener.onDatasetChange([{ type: DataOperationType.RELOAD }]);
    });
  }

  notifyDataChange(index: number) {
    this.listeners.forEach(listener => {
      listener.onDatasetChange([{ type: DataOperationType.CHANGE, index: index }]);
    });
  }

}

class MyDemoDataSource<T> extends BasicDataSource<T> {
  private dataArray: T[] = [];

  constructor(dataArray: T[]) {
    super();
    this.dataArray = dataArray;
  }

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): T {
    return this.dataArray[index];
  }
}
```
