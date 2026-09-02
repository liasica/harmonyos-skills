---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1536
title: Tabs如何根据TabBar数量更改页签栏排布
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Tabs如何根据TabBar数量更改页签栏排布
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5fdaef61249e73b3e857797901f92cb406c4c77f6103bbe68e9d078015801bde
---

## 问题现象

应用中有的Tabs页面的数量是通过服务端返回的结果动态显示的，TabBar的数量较多时保持均分显示，但是数量较少时希望能够靠拢显示，避免有大量的留白间距影响视觉体验。

## 背景知识

[Tabs组件](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。

* [barGridAlign](../harmonyos-references/ts-container-tabs.md#bargridalign10)：以栅格化方式设置TabBar的可见区域。
* 可以通过改变入参[BarGridColumnOptions](../harmonyos-references/ts-container-tabs.md#bargridcolumnoptions10对象说明)动态调整TabBar的显示效果。

## 解决方案

设置Tabs的barGridAlign属性，通过调整BarGridColumnOptions的sm和margin属性，以达到TabBar靠拢或者均分的效果。

用户在输入框输入小于等于10的数字后，以4为阈值：TabBar数量小于4时，页签靠拢显示；TabBar数量大于等于4时，页签均分显示。

```ts
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
struct TabsView {
  @State tabList: string[] = [];
  tabsController: TabsController = new TabsController();
  currentIndex: number = 0;
  tabsNum: number = 0;
  controller: TextInputController = new TextInputController();

  private generateCharacterList(n: number): string[] {
    let list: string[] = [];
    for (let i = 1; i <= n; i++) {
      list.push(i.toString());
    }
    return list;
  }

  build() {
    Column() {
      Row() {
        TextInput({ text: `${this.tabsNum}`, placeholder: 'input your tab number', controller: this.controller })
          .backgroundColor('#ffd9dbd9')
          .borderWidth(1)
          .type(InputType.Number)
          .width('90%')
          .onChange((value: string) => {
            let tabNum = Number(value);
            if (tabNum > 10) {
              this.getUIContext().getPromptAction().showToast({
                message: 'tab number must be little then 10',
                duration: 2000,
                showMode: promptAction.ToastShowMode.DEFAULT,
                bottom: 80
              });
              return;
            }
            this.tabList = this.generateCharacterList(Number(value));
          });
      };

      Tabs({ controller: this.tabsController }) {
        ForEach(this.tabList, (item: string) => {
          TabContent() {
            Column() {
              Text(item);
            }.width('100%').height('100%')
            .justifyContent(FlexAlign.Center);
          }.tabBar(item);
        }, (item: string) => item);
      }
      .width('100%')
      .height('100%')
      .barGridAlign({ sm: 4, margin: this.tabList.length < 4 ? 80 : 0 })
      .onChange((index: number) => {
        this.currentIndex = index;
      });
    };
  }
}
```

## 总结

要实现Tabs组件中的TabBar根据数量均分或者靠拢显示，通过设置Tabs组件的barGridAlign属性调整。
