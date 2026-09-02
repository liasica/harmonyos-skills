---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-828
title: LazyForEach的键值与数据刷新异常问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > LazyForEach的键值与数据刷新异常问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:485725f4acc9c8c059e7e7153372809f11a7cdc26cc127bcbd4db68c3acb52e1
---

## 问题现象

在List、Grid等存在大量子组件的场景下，常使用LazyForEach进行数据懒加载渲染。但通常因使用错误，遇到UI刷新异常的问题，针对UI刷新异常，可以考虑从键值方面进行排查。

* 场景一：LazyForEach显示的数据混乱。

  列表滑动时显示的列表项顺序混乱，数据显示重复。问题代码如下：

  ```ts
  // 代码中引入的MyDataSource在解决方案中说明
  import { MyDataSource } from '../common/data';

  class Product {
    money: number = 0;
    text: string = '';
    title: string = '';
    data: string = '';

    constructor(money: number, text: string, title: string, data: string) {
      this.money = money;
      this.text = text;
      this.title = title;
      this.data = data;
    }
  }

  @Entry
  @Component
  struct KeyDemoOne {
    private data: MyDataSource<Product> = new MyDataSource<Product>();

    aboutToAppear(): void {
      // 请求数据模拟
      for (let i = 0; i < 100; i++) {
        let str: string = (i % 2 == 0) ? '限部分商品使用' : '全场可用';
        let product: Product = new Product(i, `满${i * 10}元立减`, str, `${i}天内有效`);
        this.data.pushData(product);
      }
    }

    build() {
      Column() {
        List({ space: 10 }) {
          LazyForEach(this.data, (item: Product) => {
            ListItem() {
              Row() {
                Column() {
                  Text(item.money.toString())
                    .margin({ top: 20, bottom: 20 })
                    .fontColor('#f9f4d7')
                    .borderRadius(5);
                  Text(item.text)
                    .textAlign(TextAlign.Center)
                    .fontSize(12)
                    .fontColor('#f9f4d7')
                    .borderRadius(5);
                }
                .width('30%')
                .height(100)
                .backgroundColor('#fe6a48');

                Column() {
                  Row() {
                    Text(item.title)
                      .textAlign(TextAlign.Start)
                      .margin({ top: 15, left: -110, bottom: 40 });
                  };

                  Row() {
                    Text(item.data)
                      .fontSize(10)
                      .margin({ left: -5, right: 25 });
                  };
                }
                .width('70%')
                .height(100)
                .backgroundColor('#f1f2f3');
              };
            };
          }, (item: Product) => item.title);
        };
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#ffffff');
    }
  }
  ```
* 场景二：LazyForEach修改数据后UI不刷新。

  修改数据源中的数据项后，数据的修改在UI中未刷新，显示的还是初始的数据。问题代码如下：

  ```ts
  // 代码中引入的MyDataSource在解决方案中说明
  import { MyDataSource } from '../common/data';

  class Product {
    money: number = 0;
    text: string = '';
    title: string = '';
    data: string = '';
    id: string = '';

    constructor(money: number, text: string, title: string, data: string, id: string) {
      this.money = money;
      this.text = text;
      this.title = title;
      this.data = data;
      this.id = id;
    }
  }

  @Entry
  @Component
  struct KeyDemoTwo {
    private data: MyDataSource<Product> = new MyDataSource<Product>();

    aboutToAppear(): void {
      // 请求数据模拟
      for (let i = 0; i < 100; i++) {
        let id = i.toString(); // 设置一个唯一的id，实际业务中可以使用其他唯一值作为键值
        let str: string = (i % 2 == 0) ? '限部分商品使用' : '全场可用';
        let product: Product = new Product(i, `满${i * 10}元立减`, str, `${i}天内有效`, id);
        this.data.pushData(product);
      }
    }

    build() {
      Column() {
        Button('修改数据')
          .onClick(() => {
            let index = 3;
            let product: Product = this.data.getData(index);
            product.title = '已使用';
            this.data.setData(product, index);
          })
          .margin({ top: 16, bottom: 16 });

        List({ space: 10 }) {
          LazyForEach(this.data, (item: Product) => {
            ListItem() {
              Row() {
                Column() {
                  Text(item.money.toString())
                    .margin({ top: 20, bottom: 20 })
                    .fontColor('#f9f4d7')
                    .borderRadius(5);
                  Text(item.text)
                    .textAlign(TextAlign.Center)
                    .fontSize(12)
                    .fontColor('#f9f4d7')
                    .borderRadius(5);
                }
                .width('30%')
                .height(100)
                .backgroundColor('#fe6a48');

                Column() {
                  Row() {
                    Text(item.title)
                      .textAlign(TextAlign.Start)
                      .margin({ top: 15, left: -110, bottom: 40 });
                  };

                  Row() {
                    Text(item.data)
                      .fontSize(10)
                      .margin({ left: -5, right: 25 });
                  };
                }
                .width('70%')
                .height(100)
                .backgroundColor('#f1f2f3');
              };
            };
          }, (item: Product) => item.id); // 使用唯一值作为键值
        };
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#ffffff');
    }
  }
  ```

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)：列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
* [LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)：LazyForEach从数据源中按需迭代数据，并在每次迭代时创建相应组件。当LazyForEach用于滚动容器时，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会销毁并回收组件以降低内存占用。
* [键值生成规则](../harmonyos-guides/arkts-rendering-control-lazyforeach.md#键值生成规则)：在LazyForEach循环渲染过程中，系统为每个item生成一个唯一且持久的键值，用于标识对应的组件。键值变化时，ArkUI框架将视为该数组元素已被替换或修改，并基于新的键值创建新的组件。
* keyGenerator：键值生成函数，用于给数据源中的每一个数据项生成唯一且固定的键值。修改数据源中的一个数据项若不影响其生成的键值，则对应组件不会被更新，否则此处组件就会被重建更新。详细参考LazyForEach[接口](../harmonyos-references/ts-rendering-control-lazyforeach.md#接口)。键值应满足以下条件：
  + 键值具有唯一性，每个数据项对应的键值互不相同。
  + 键值具有一致性，数据项不变时对应的键值也不变。

## 问题定位

对于LazyForEach使用过程中常见的UI刷新异常，可以考虑先从键值方面进行排查，主要排查：

1. 键值生成函数是否设置，设置是否合理。
2. 键值是否具有唯一性和一致性。

场景一：在UI更新时，如果出现重复的键值，框架可能无法正常工作。在问题代码中，使用了title属性作为键值，键值不唯一导致数据渲染混乱。

场景二：键值变化时，ArkUI框架将视为该数组元素已被替换或修改，并基于新的键值创建新的组件。问题代码中修改的是title属性，但键值使用的是id，键值未变化导致组件不会重新渲染。

## 分析结论

在LazyForEach中使用重复的键值，可能会导致框架无法正常工作，数据渲染混乱。当修改数据时，若对应的键值未发生变化，也会导致组件不刷新。

## 修改建议

* 场景一：LazyForEach显示的数据混乱。

  方案：使用唯一的值作为键值，保障每个列表项的键值不同。

  ```ts
  import { MyDataSource } from '../common/data';

  class Product {
    money: number = 0;
    text: string = '';
    title: string = '';
    data: string = '';
    id: string = '';

    constructor(money: number, text: string, title: string, data: string, id: string) {
      this.money = money;
      this.text = text;
      this.title = title;
      this.data = data;
      this.id = id;
    }
  }

  @Entry
  @Component
  struct KeyDemoOne {
    private data: MyDataSource<Product> = new MyDataSource<Product>();

    aboutToAppear(): void {
      // 请求数据模拟
      for (let i = 0; i < 100; i++) {
        let id = i.toString(); // 设置一个唯一的id，实际业务中可以使用其他唯一值作为键值
        let str: string = (i % 2 == 0) ? '限部分商品使用' : '全场可用';
        let product: Product = new Product(i, `满${i * 10}元立减`, str, `${i}天内有效`, id);
        this.data.pushData(product);
      }
    }

    build() {
      Column() {
        List({ space: 10 }) {
          LazyForEach(this.data, (item: Product) => {
            ListItem() {
              Row() {
                Column() {
                  Text(item.money.toString())
                    .margin({ top: 20, bottom: 20 })
                    .fontColor('#f9f4d7')
                    .borderRadius(5);
                  Text(item.text)
                    .textAlign(TextAlign.Center)
                    .fontSize(12)
                    .fontColor('#f9f4d7')
                    .borderRadius(5);
                }
                .width('30%')
                .height(100)
                .backgroundColor('#fe6a48');

                Column() {
                  Row() {
                    Text(item.title)
                      .textAlign(TextAlign.Start)
                      .margin({ top: 15, left: -110, bottom: 40 });
                  };

                  Row() {
                    Text(item.data)
                      .fontSize(10)
                      .margin({ left: -5, right: 25 });
                  };
                }
                .width('70%')
                .height(100)
                .backgroundColor('#f1f2f3');
              };
            };
          }, (item: Product) => item.id); // 使用唯一值作为键值
        };
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#ffffff');
    }
  }
  ```
* 场景二：LazyForEach修改数据后UI不刷新。

  方案：针对问题场景，可以考虑将修改的属性作为键值的一部分，实际业务中可以根据情况设置合理的键值。

  ```ts
  import { MyDataSource } from '../common/data';

  class Product {
    money: number = 0;
    text: string = '';
    title: string = '';
    data: string = '';
    id: string = '';

    constructor(money: number, text: string, title: string, data: string, id: string) {
      this.money = money;
      this.text = text;
      this.title = title;
      this.data = data;
      this.id = id;
    }
  }

  @Entry
  @Component
  struct KeyDemoTwo {
    private data: MyDataSource<Product> = new MyDataSource<Product>();
    private counter: number = 0;

    aboutToAppear(): void {
      // 请求数据模拟
      for (let i = 0; i < 100; i++) {
        let id = i.toString(); // 设置一个唯一的id，实际业务中可以使用其他唯一值作为键值
        let str: string = (i % 2 == 0) ? '限部分商品使用' : '全场可用';
        let product: Product = new Product(i, `满${i * 10}元立减`, str, `${i}天内有效`, id);
        this.data.pushData(product);
      }
    }

    build() {
      Column() {
        Button('修改数据')
          .onClick(() => {
            let index = 3;
            let product: Product = this.data.getData(index);
            product.title = `已使用${++this.counter}次`;
            this.data.setData(product, index);
          })
          .margin({ top: 16, bottom: 16 });

        List({ space: 10 }) {
          LazyForEach(this.data, (item: Product) => {
            ListItem() {
              Row() {
                Column() {
                  Text(item.money.toString())
                    .margin({ top: 20, bottom: 20 })
                    .fontColor('#f9f4d7')
                    .borderRadius(5);
                  Text(item.text)
                    .textAlign(TextAlign.Center)
                    .fontSize(12)
                    .fontColor('#f9f4d7')
                    .borderRadius(5);
                }
                .width('30%')
                .height(100)
                .backgroundColor('#fe6a48');

                Column() {
                  Row() {
                    Text(item.title)
                      .textAlign(TextAlign.Start)
                      .margin({ top: 15, left: -110, bottom: 40 });
                  };

                  Row() {
                    Text(item.data)
                      .fontSize(10)
                      .margin({ left: -5, right: 25 });
                  };
                }
                .width('70%')
                .height(100)
                .backgroundColor('#f1f2f3');
              };
            };
          }, (item: Product) => item.id + item.title); // 可以根据实际业务设置，让键值随数据修改变化
        };
      }
      .width('100%')
      .height('90%')
      .backgroundColor('#ffffff');
    }
  }
  ```

  示例中使用的LazyForEach的数据源，根据实际业务需要在指定目录下定义（例如entry/src/main/ets/common/data.ets）：

  ```ts
  class BasicDataSource<T> implements IDataSource {
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

  // LazyForEach的数据源需要实现IDataSource接口
  export class MyDataSource<T> extends BasicDataSource<T> {
    private dataArray: T[] = [];

    public setData(data: T, index: number): void {
      if (this.dataArray.length > index) {
        this.dataArray[index] = data;
        this.notifyDataChange(index);
      }
    }

    public getAllData(): T[] {
      return this.dataArray;
    }

    public totalCount(): number {
      return this.dataArray.length;
    }

    public getData(index: number): T {
      return this.dataArray[index];
    }

    public pushData(data: T): void {
      this.dataArray.push(data);
      this.notifyDataAdd(this.dataArray.length - 1);
    }
  }
  ```

## 总结

LazyForEach依赖唯一键值来标识组件。不管是原来的数据数组中key值不唯一还是增删修改数组后key值不唯一，都会导致组件渲染异常。异常的表现在item缺失，重复等。
