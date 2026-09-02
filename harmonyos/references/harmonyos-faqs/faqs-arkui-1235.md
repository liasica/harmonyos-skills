---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1235
title: 如何实现点击GridItem获取选中内容
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现点击GridItem获取选中内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:02009d7c0f0170d3317912c0b74cd0b94661fd1a80e497778ec4980c75729707
---

## 问题现象

使用Grid组件，如何实现点击item后高亮，再次点击则需要取消高亮，最后还要收集已选选项。

## 背景知识

* [Grid](../harmonyos-references/ts-container-grid.md)：网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。
* [GridItem](../harmonyos-references/ts-container-griditem.md)：网格容器中单项内容容器。

## 解决方案

1. 实现功能时将GridItem内容抽取为独立组件，为item内容设置点击事件，通过点击时状态变量的变化控制item背景色变化。
2. 想要获取选中的item，则需要通过item的点击事件将点击时获取到的index插入到数组中，并通过indexOf判断点击内容是否已存在数组中，当不存在时，将选中内容插入数组；当存在时，则不做插入操作。

完整示例参考如下：

```ts
class ProductInfo {
  public id: string;
  public productName: string;

  constructor(id: string, productName: string) {
    this.id = id;
    this.productName = productName;
  }
}

@Entry
@Component
struct GridHighLight {
  @State services: ProductInfo[] = [
    new ProductInfo('1', 'HUAWEI nova 12'),
    new ProductInfo('2', 'HUAWEI nova 11'),
    new ProductInfo('3', 'HUAWEI nova 13'),
    new ProductInfo('24', 'HUAWEI nova 14')
  ];
  clickThings: Array<string> = [];
  @Provide selectIndexList: Array<string> = [];

  build() {
    Column() {
      Grid() {
        ForEach(this.services, (item: ProductInfo) => {
          GridItem() {
            // 父组件中传递数据
            ToDoItem({ content: item.productName, selectIndex: item.id });
          };
        }, (item: ProductInfo): string => JSON.stringify(item));
      }
      .columnsTemplate('1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .width('90%')
      .height(300);

      Text('选中的');
      Text(`${this.selectIndexList}`);
    }
    .width('100%');
  }
}

// 将GridItem内容抽取为独立组件
@Component
export default struct ToDoItem {
  private content?: string;
  @State isComplete: boolean = false;
  private selectIndex?: string;
  @Consume selectIndexList: Array<string>;

  build() {
    Row() {
      Column() {
        Text(this.content);
      }
      .width('30%')
      .height(100)
      .backgroundColor(this.isComplete ? '#0D5AF5' : '#F1F3F5')
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height(60)
      .onClick(() => {
        // 通过状态变量控制背景色变化
        this.isComplete = !this.isComplete;
        if (this.selectIndex) {
          if (this.isComplete) {
            this.selectIndexList.push(this.selectIndex);
          } else {
            // 利用indexOf判断是否存在selectIndexList中
            let index = this.selectIndexList.indexOf(this.selectIndex);
            if (index !== -1) {
              this.selectIndexList.splice(index, 1);
            }
          }
        }
      });
    };
  }
}
```
