---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-no-stringify-lazyforeach-key
title: "@performance/hp-arkui-no-stringify-in-lazyforeach-key-generator"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-no-stringify-in-lazyforeach-key-generator
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2749585fc6dd84a1727df272d7dd6d8b5f125d5a15e370db79d55a19c8885370
---

在使用LazyForEach进行组件复用的key生成器函数里，不要使用stringify。

滑动丢帧场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-no-stringify-in-lazyforeach-key-generator": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
//源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
// 此处为复用的自定义组件
@Reusable
@Component
struct ChildComponent {
  @State desc: string = '';
  @State sum: number = 0;
  @State avg: number = 0;
  aboutToReuse(params: Record<string, Object>): void {
    this.desc = params.desc as string;
    this.sum = params.sum as number;
    this.avg = params.avg as number;
  }
  build() {
    Column() {
      Text('子组件' + this.desc)
        .fontSize(30)
        .fontWeight(30)
      Text('结果' + this.sum)
        .fontSize(30)
        .fontWeight(30)
      Text('平均值' + this.avg)
        .fontSize(30)
        .fontWeight(30)
    }
  }
}
class Item {
  advertInfos: Model[] = []
  productPrice: PriceInfo[] = []
  addresses: string[] = []
  id: string = ''
}
class Model {
  pictureUrl: string = ""
  name: string = ""
  comments: string = ""
  desc: string = ""
  linkParam: string = ""
  mcInfo: string = ""
  label: string = ""
  cgType: string = ""
  constructor(pictureUrl: string, name: string, comments: string, desc: string, linkParam: string, mcInfo: string,
    label: string, cgType: string) {
    this.pictureUrl = pictureUrl;
    this.name = name;
    this.comments = comments;
    this.desc = desc;
    this.linkParam = linkParam;
    this.mcInfo = mcInfo;
    this.label = label;
    this.cgType = cgType;
  }
}
class PriceInfo {
  price: number = 0;
  level: number = 1;
  constructor(price: number, level: number) {
    this.price = price;
    this.level = level;
  }
}
@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource();
  aboutToAppear(): void {
    for (let index = 0; index < 20; index++) {
      let item = new Item()
      for (let i = 0; i < 1000; i++) {
        item.advertInfos.push(new Model("Product A", "Product A", "Product A", "Product A", "Product A", "Product A", "Product A", "Product A"));
        item.productPrice.push(new PriceInfo(1.99, 123456));
        item.addresses.push("Beijing")
      }
      item.id = index.toString();
      this.data.pushData(item)
    }
  }
  build() {
    Column() {
      Text('Use the unique ID of an item as the key')
        .fontSize(12)
        .height('16')
        .margin({
          top: 5,
          bottom: 10
        })
      List() {
        LazyForEach(this.data, (item: Item) => {
          ListItem() {
            ChildComponent({ desc: item.id, sum: 0, avg: 0 })
          }
          .width('100%')
          .height('10%')
          .border({ width: 1 })
          .borderStyle(BorderStyle.Dashed)
        }, (item: Item) => item.id.toString())
      }
      .height('100%')
      .width('100%')
    }
  }
}
```

## 反例

```screen
//源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
// 此处为复用的自定义组件
@Reusable
@Component
struct ChildComponent {
  @State desc: string = '';
  @State sum: number = 0;
  @State avg: number = 0;

  aboutToReuse(params: Record<string, Object>): void {
    this.desc = params.desc as string;
    this.sum = params.sum as number;
    this.avg = params.avg as number;
  }

  build() {
    Column() {
      Text('子组件' + this.desc)
        .fontSize(30)
        .fontWeight(30)
      Text('结果' + this.sum)
        .fontSize(30)
        .fontWeight(30)
      Text('平均值' + this.avg)
        .fontSize(30)
        .fontWeight(30)
    }
  }
}

class Item {
  advertInfos: Model[] = []
  productPrice: PriceInfo[] = []
  addresses: string[] = []
  id: string = ''
}

class Model {
  pictureUrl: string = ""
  name: string = ""
  comments: string = ""
  desc: string = ""
  linkParam: string = ""
  mcInfo: string = ""
  label: string = ""
  cgType: string = ""

  constructor(pictureUrl: string, name: string, comments: string, desc: string, linkParam: string, mcInfo: string,
    label: string, cgType: string) {
    this.pictureUrl = pictureUrl;
    this.name = name;
    this.comments = comments;
    this.desc = desc;
    this.linkParam = linkParam;
    this.mcInfo = mcInfo;
    this.label = label;
    this.cgType = cgType;
  }
}

class PriceInfo {
  price: number = 0;
  level: number = 1;

  constructor(price: number, level: number) {
    this.price = price;
    this.level = level;
  }
}

@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource();

  aboutToAppear(): void {
    for (let index = 0; index < 20; index++) {
      let item = new Item()
      for (let i = 0; i < 1000; i++) {
        item.advertInfos.push(new Model("Product A", "Product A", "Product A", "Product A", "Product A", "Product A", "Product A", "Product A"));
        item.productPrice.push(new PriceInfo(1.99, 123456));
        item.addresses.push("Beijing")
      }
      item.id = index.toString();
      this.data.pushData(item)
    }
  }

  build() {
    Column() {
      Text('Use the time-consuming function `JSON.stringify (item)` to generate a key')
        .fontSize(12)
        .height('16')
        .margin({
          top: 5,
          bottom: 10
        })
      List() {
        LazyForEach(this.data, (item: Item) => {
          ListItem() {
            ChildComponent({ desc: item.id, sum: 0, avg: 0 })
          }
          .width('100%')
          .height('10%')
          .border({ width: 1 })
          .borderStyle(BorderStyle.Dashed)
        }, (item: Item) => JSON.stringify(item))
      }
      .height('100%')
      .width('100%')
    }
  }
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
