---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-728
title: ListItemGroup如何使用三元运算符
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > ListItemGroup如何使用三元运算符
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eaad2b9cf9a588f99b389849120ff3aa9b9c0a5bdf31dd13a1ae83aef019bea5
---

## 问题现象

ListItemGroup如何使用三元运算符，渲染不同的组件？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/WvGzHW18TXeRZoR-RwQ-QA/zh-cn_image_0000002658794589.gif "点击放大")

## 背景知识

* [ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)：用来展示列表item分组，宽度默认充满List组件，必须配合List组件来使用。
* [cryptoFramework](../harmonyos-references/js-apis-cryptoframework.md)：对于安全要求比较高的场景，推荐使用加解密算法库框架[@ohos.security.cryptoFramework](../harmonyos-references/js-apis-cryptoframework.md)包生成安全随机数。

## 解决方案

使用[ListItemGroupOptions对象说明](../harmonyos-references/ts-container-listitemgroup.md#listitemgroupoptions对象说明)下面的参数headerComponent。

```ts
import { ComponentContent } from '@kit.ArkUI';
import cryptoFramework from '@ohos.security.cryptoFramework';

// 1.定义不同的头部组件
@Builder
function aList() {
  Text('Aa')
    .fontSize(20)
    .height('48vp')
    .width('100%')
    .padding(10)
    .backgroundColor($r('sys.color.background_tertiary'));
}

@Builder
function bList() {
  Text('Bb')
    .fontSize(20)
    .height('48vp')
    .width('100%')
    .padding(10)
    .backgroundColor($r('sys.color.background_tertiary'));
}

@Entry
@Component
struct Index {
  private list?: MyDataSource2;
  // 2.状态管理
  @State isActive: boolean = true;
  headerA?: ComponentContent<string> = undefined;
  headerB?: ComponentContent<string> = undefined;

  // 3.初始化组件
  aboutToAppear() {
    let rand = cryptoFramework.createRandom();
    // 设置生成随机数的字节长度为1
    let randData = rand.generateRandomSync(1);
    // 自定义范围(0-10之内)
    let num: number = randData.data[0] * 10 / 255;
    const listItem: MyDataSource1[] = [];
    for (let date = 1; date < ~~num + 3; date++) {
      const strs: string[] = [];
      for (let index = 1; index < ~~num + 30; index++) {
        strs.push(`hello${index}`);
      }
      let dayData = new MyDataSource1(strs);
      listItem.push(dayData);
    }
    this.list = new MyDataSource2(listItem);
    this.headerA = new ComponentContent(this.getUIContext(), wrapBuilder(aList));
    this.headerB = new ComponentContent(this.getUIContext(), wrapBuilder(bList));
  }

  build() {
    Column() {
      // 4.切换按钮
      Button('true').onClick(() => {
        this.isActive = true;
      });
      Button('false').onClick(() => {
        this.isActive = false;
      })
        .margin({ top: 3, bottom: 3 });
      // 5.列表组件
      List({ space: 20 }) {
        LazyForEach(this.list, (item: MyDataSource1) => {
          // 6.使用三元运算符动态切换头部
          ListItemGroup({ headerComponent: this.isActive ? this.headerA : this.headerB }) {
            LazyForEach(item, (order: string,) => {
              ListItem() {
                Text(order)
                  .width('100%')
                  .height(60)
                  .fontSize(20)
                  .textAlign(TextAlign.Center)
                  .backgroundColor(0xFFFFFF);
              }.padding({ top: 5 });
            });
          };
        });
      }
      .height('100%')
      .cachedCount(1)
      .width('90%')
      .sticky(StickyStyle.Header | StickyStyle.Footer)
      .scrollBar(BarState.Off);
    }
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 });
  }
}

class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: string[] = [];

  public totalCount(): number {
    return 0;
  }

  public getData(index: number): string | MyDataSource1 {
    return this.originDataArray[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      this.listeners.push(listener);
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
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
}

class MyDataSource1 extends BasicDataSource {
  private dataArray: string[] = [];
  public title?: string;
  public header?: CustomBuilder;

  constructor(dataArray: string[]) {
    super();
    this.dataArray = dataArray;
  }

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

class MyDataSource2 extends BasicDataSource {
  private dataArray: MyDataSource1[] = [];

  constructor(dataArray: MyDataSource1[]) {
    super();
    this.dataArray = dataArray;
  }

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): MyDataSource1 {
    return this.dataArray[index];
  }

  public addData(index: number, data: MyDataSource1): void {
    this.dataArray.splice(index, 0, data);
    this.notifyDataAdd(index);
  }

  public pushData(data: MyDataSource1): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}
```
