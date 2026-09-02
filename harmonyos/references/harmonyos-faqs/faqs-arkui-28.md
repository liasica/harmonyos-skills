---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-28
title: 如何设置分组列表的圆角和间距
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何设置分组列表的圆角和间距
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:40683909f5218598ba1d623d7f187ae33041c342c7a84fa0bd21a1881035a6c5
---

通过[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)中的ListItemGroupStyle设置分组列表的圆角，List的[space](../harmonyos-references/ts-container-list.md#接口)设置间距。可参考如下代码：

```ts
// xxx.ets
@Entry
@Component
struct ListItemGroupExample {
  private timeTable: TimeTable[] = [
    { projects: ['language'] },
    { projects: ['mathematics', 'English'] },
    { projects: ['physics', 'chemistry', 'biology'] },
    { projects: ['the fine arts', 'music', 'sport'] }
  ]

  build() {
    Column() {
      List({ space: 20 }) { // Set the spacing of the grouping list
        ForEach(this.timeTable, (item: TimeTable) => {
          ListItemGroup({ style: ListItemGroupStyle.CARD }) { // Set the rounded corners of the grouping list
            ForEach(item.projects, (project: string) => {
              ListItem() {
                Text(project)
                  .width("100%")
                  .height(100)
                  .fontSize(20)
                  .textAlign(TextAlign.Center)
                  .backgroundColor(0xFFFFFF)
              }
            }, (item: string) => item)
          }
        })
      }
      .width('90%')
      .sticky(StickyStyle.Header | StickyStyle.Footer)
      .scrollBar(BarState.Off)
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5, bottom: 5 })
  }
}

interface TimeTable {
  projects: string[];
}
```
