---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-65
title: SideBarContainer如何设置controlButton属性
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > SideBarContainer如何设置controlButton属性
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:beea12444b2f442f7b37bd6b2653713b251b3803464fbb09035774346f11cf72
---

SideBarContainer组件提供侧边栏显示和隐藏功能。通过controlButton属性设置侧边栏控制按钮。参考代码如下：

```typescript
@Entry
@Component
struct SideBarContainerExample {
  normalIcon: Resource = $r("app.media.icon")
  selectedIcon: Resource = $r("app.media.icon")
  @State arr: number[] = [1, 2, 3]
  @State current: number = 1

  build() {
    SideBarContainer(SideBarContainerType.Embed) {
      Column() {
        ForEach(this.arr, (item: number, index) => {
          Column({ space: 5 }) {
            Image(this.current === item ? this.selectedIcon : this.normalIcon).width(64).height(64)
            Text("Index0" + item)
              .fontSize(25)
              .fontColor(this.current === item ? '#0A59F7' : '#999')
              .fontFamily('source-sans-pro,cursive,sans-serif')
          }
          .onClick(() => {
            this.current = item
          })
        })
      }.width('100%')
      .justifyContent(FlexAlign.SpaceEvenly)
      .backgroundColor('#19000000')

      Column() {
        Text('SideBarContainer content text1').fontSize(25)
        Text('SideBarContainer content text2').fontSize(25)
      }
      .margin({ top: 50, left: 20, right: 30 })
    }
    .sideBarWidth(150)
    .minSideBarWidth(50)
    .controlButton({
      left: 32,
      top: 32,
      width: 32,
      height: 32,
      icons: { shown: $r("app.media.icon"),
        hidden: $r("app.media.icon"),
        switching: $r("app.media.icon") }
    })
    .maxSideBarWidth(300)
    .onChange((value: boolean) => {
      console.info('status:' + value)
    })
  }
}
```

**参考链接**

[SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)
