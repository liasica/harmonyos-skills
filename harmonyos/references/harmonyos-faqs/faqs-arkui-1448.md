---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1448
title: ArrayList类型的状态变量改变后无法触发UI的渲染刷新
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > ArrayList类型的状态变量改变后无法触发UI的渲染刷新
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:37c9da3e7ada439adff0b347f591c6abe5f9813362338fdad7d943c2266b8f84
---

## 问题现象

使用@State装饰ArrayList类型的数组变量时，数组成员发生变化无法触发UI渲染。问题代码如下：

```ts
import { ArrayList } from '@kit.ArkTS';
import { PromptAction } from '@ohos.arkui.UIContext';

@Entry
@Component
struct ArrayListPage1 {
  @State numItems: ArrayList<string> = new ArrayList();
  prompt: PromptAction = this.getUIContext().getPromptAction()

  aboutToAppear(): void {
    for (let index = 0; index < 2; index++) {
      this.numItems.add(`index:${index}`)
    }
  }

  build() {
    Column({ space: 10 }) {
      List({ space: 10 }) {
        ForEach(this.numItems.convertToArray(), (item: string) => {
          ListItem() {
            Text(item)
              .textAlign(TextAlign.Center)
              .backgroundColor('#330a59f7')
              .width('100%')
              .height(40)
              .borderRadius(10)
          }
        })
      }.margin({ left: 16, right: 16, bottom: 20 })

      Text(`状态变量数组长度：${this.numItems.length}`)
      Button('添加').onClick(() => {
        this.numItems.add('666')
        this.prompt.openToast({
          message: `最新查询数组长度${this.numItems.length}`
        })
      })
    }.width('100%')
    .height('100%')
  }
}
```

运行效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/J_8W3segRpOZdjCnhbUksw/zh-cn_image_0000002628604260.png "点击放大")

## 背景知识

* [@State装饰](../harmonyos-guides/arkts-state.md)的变量，或称为状态变量。一旦变量拥有了状态属性，当状态变量改变时，会触发其直接绑定的UI组件重新渲染。
* [ArrayList](../harmonyos-references/js-apis-arraylist.md)是一种线性数据结构，底层基于数组实现。

## 问题定位

变量改变后无法触发UI的渲染刷新，首先需要检查状态变量是否包含多层嵌套，因为@State仅能观察到第一层的变化。实际上，问题代码中仅包含一层嵌套。接着，检查@State装饰的变量是否为响应式数据，因为非响应式数据变化后，也不会触发页面重新渲染。

## 分析结论

ArrayList在使用[convertToArray()](../harmonyos-references/js-apis-arraylist.md#converttoarray)方法后得到的Array只是普通的数组，而非状态变量。数组改变时不会被UI观察到，无法触发UI的渲染刷新。只有直接用新的ArrayList覆盖原来的值，才会触发UI渲染，但是这种方法会导致不需要刷新的部分也刷新，影响应用的性能，所以不推荐使用。

## 修改建议

建议使用响应式的数据结构Array去替代ArrayList。示例代码如下：

```ts
import { PromptAction } from '@ohos.arkui.UIContext';

@Entry
@Component
struct ListPage {
  @State numItems: Array<string> = [];
  prompt: PromptAction = this.getUIContext().getPromptAction();

  aboutToAppear(): void {
    for (let index = 0; index < 2; index++) {
      this.numItems.push(`index:${index}`);
    }
  }

  build() {
    Column({ space: 10 }) {
      List({ space: 10 }) {
        ForEach(this.numItems, (item: string) => {
          ListItem() {
            Text(item)
              .textAlign(TextAlign.Center)
              .backgroundColor('#330a59f7')
              .width('100%')
              .height(40)
              .borderRadius(10);
          };
        });
      }.margin({ left: 16, right: 16, bottom: 20 });

      Text(`状态变量数组长度：${this.numItems.length}`);
      Button('添加').onClick(() => {
        this.numItems.push('index:666');
        this.prompt.openToast({ message: `最新查询数组长度${this.numItems.length}` }).catch(() => {
          console.error('出错啦！');
        });
      });
    }.width('100%')
    .height('100%');
  }
}
```
