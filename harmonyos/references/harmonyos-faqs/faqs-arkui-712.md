---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-712
title: Grid如何展开与收起二级子GridItem
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Grid如何展开与收起二级子GridItem
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:8c05376a30c6d466bb4d8b513c1d7485510bd34dbe2959e90822f0e694ae4bbc
---

## 问题现象

网格容器Grid如何实现展开与收起二级子GridItem功能？

## 背景知识

* [Grid](../harmonyos-references/ts-container-grid.md)：网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。
* [GridLayoutOptions](../harmonyos-references/ts-container-grid.md#gridlayoutoptions10对象说明)：Grid布局选项。

| GridLayoutOptions参数 | 说明 |
| --- | --- |
| regularSize | 大小规则的GridItem在Grid中占的行数和列数，只支持占1行1列即[1, 1]。 |
| irregularIndexes | 指定的GridItem索引在Grid中的大小是不规则的。当不设置onGetIrregularSizeByIndex时，irregularIndexes中GridItem的默认大小为垂直滚动Grid的一整行或水平滚动Grid的一整列。 |

## 解决方案

通过设置GridLayoutOptions布局选项中regularSize和irregularIndexes参数，给目标GridItem下一行添加一组数据。实现思路如下：

1. 通过设置变量进行判断是否展开子级。
2. 通过设置的列数，计算一级GridItem总行数、点击GridItem所在行。
3. 向当前点击GridItem的下一行(获取当前行最末端的索引)添加一条数据到一级GridItem中，用于展示二级GridItem。
4. 修改GridLayoutOptions中的regularSize和irregularIndexes参数用于实现添加数据独占一行。

示例代码如下：

CollapseMenu.ets：

```ts
export class CollapseMenu {
  columns: number = 4; // 列
  isExpanded: boolean = false; // 是否展开
  layoutOptions: GridLayoutOptions = {
    // Grid布局选项
    regularSize: [1, 1]
  };
  index: number = 0; // 数组索引 0
  firstMenu: Array<ESObject> = []; // 一级菜单
  secondMenu: Array<ESObject> = []; // 二级菜单
  targetIndex: number = -1; // 追加数据索引,从0开始
  clickIndex: number = -1; // 选中索引
  expandedRow: number = -1; // 展开行数
  totalRows: number = 0; // 计算总行数 从1开始
  rowIndex: number = 0; // 点击行数 从0开始
  isLastRow: boolean = false; // 是否是最后一行

  // 初始化一级数据
  public setFirstMenu(arr: Array<ESObject>) {
    this.firstMenu = arr;
  };

  // 初始化二级数据
  public setSecondMenu(arr: Array<ESObject>) {
    this.secondMenu = arr;
  };

  // 初始化列
  public setColumns(column: number) {
    this.columns = column;
  };

  // 设置网格布局
  public setLayoutOptions(gridLayoutOptions: GridLayoutOptions) {
    this.layoutOptions = gridLayoutOptions;
  };

  public addSecondMenu(index: number) {
    if (!this.isExpanded) {
      this.totalRows = Math.ceil(this.firstMenu.length / this.columns); // 计算总行数 从1开始
      this.rowIndex = Math.floor(index / this.columns); // 计算所在行 从0开始
      this.firstMenu.splice(index + (this.columns - index % this.columns), 0,
        this.secondMenu); // 向当前点击menu的下一行(获取当前行最末端的索引)添加一条数据到一级grid中，用于展示二级grid
      this.isLastRow = this.rowIndex === this.totalRows - 1; // 是否是最后一行
      this.targetIndex = this.isLastRow ? this.firstMenu.length - 1 : (this.rowIndex + 1) * 4;
      this.layoutOptions = {
        regularSize: [1, 1], // 追加数据独占一行
        irregularIndexes: [this.targetIndex] // 下一行添加一个GridItem从0开始独占一行
      };
      this.isExpanded = true;
      this.clickIndex = index;
    } else {
      this.firstMenu.splice(this.targetIndex, 1);
      // 点击同一个元素
      if (this.clickIndex === index) {
        this.isExpanded = false;
        this.layoutOptions = {
          regularSize: [1, 1],
        };
      } else {
        this.clickIndex = index > this.targetIndex ? index - 1 : index;
        this.totalRows = Math.ceil(this.firstMenu.length / this.columns);
        this.rowIndex = Math.floor(this.clickIndex / this.columns);
        this.firstMenu.splice(this.clickIndex + (this.columns - this.clickIndex % this.columns), 0, this.secondMenu);
        this.isLastRow = this.rowIndex === this.totalRows - 1;
        this.targetIndex = this.isLastRow ? this.firstMenu.length - 1 : (this.rowIndex + 1) * 4;
        this.layoutOptions = {
          regularSize: [1, 1],
          irregularIndexes: [this.targetIndex]
        };
      };      
    };
  };
};
```

Index.ets：

```ts
import { CollapseMenu as collapseMenu } from './CollapseMenu';

@Entry
@Component
struct Index {
  @State collapseMenu: collapseMenu = new collapseMenu();
  arr: Array<string> = ['1', '2', '3', '4', '5', '6'];
  child: Array<string> = ['child1', 'child2', 'child3', 'child4', 'child5'];

  aboutToAppear(): void {
    this.collapseMenu.setFirstMenu(this.arr);
    this.collapseMenu.setSecondMenu(this.child);
  }

  @Builder
  commonBuilder(param: string) {
    // 自定义菜单样式
    Column() {
      Image($r('app.media.startIcon'))
        .width(60)
        .height(60)
        .margin({ top: 10 })
        .syncLoad(true);
      Text(param)
        .fontColor(Color.Black)
        .fontSize(12)
        .margin({ top: 5, bottom: 10 })
        .height(20);
    };
  }

  build() {
    Column() {
      Grid(undefined, this.collapseMenu.layoutOptions) {
        ForEach(this.collapseMenu.firstMenu, (item: ESObject, index: number) => {
          if (this.collapseMenu.isExpanded && this.collapseMenu.targetIndex === index) {
            // 二级
            GridItem() {
              Column() {
                Grid() {
                  ForEach(item, (child: string) => {
                    GridItem() {
                      this.commonBuilder(child);
                    };
                  });
                }
                .columnsTemplate('1fr '.repeat(this.collapseMenu.columns));
              };
            }
            .backgroundColor('#f1f1f1');
          } else {
            // 一级
            GridItem() {
              Stack({ alignContent: Alignment.Bottom }) {
                this.commonBuilder(item);
                if (this.collapseMenu.isExpanded && this.collapseMenu.clickIndex === index) {
                  // 当一级菜单被点击，对应的一级item添加倒三角形
                  Row()
                    .width(0)
                    .height(0)
                    .border({
                      width: 10,
                      color: {
                        left: '#00ff0000',
                        right: '#00b02020',
                        top: '#00ff0000',
                        bottom: '#f1f1f1'
                      }
                    });
                }
              };
            }
            .onClick(() => {
              this.collapseMenu.addSecondMenu(index);
            });
          }
        });
      }
      .columnsTemplate('1fr '.repeat(this.collapseMenu.columns)); // 分为四列
    };
  };
};
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/apadc61uQ-ClKSdwCojAAg/zh-cn_image_0000002655584712.png "点击放大")

## 总结

适用于网格布局下的二级菜单展示需求。
