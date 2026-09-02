---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-19
title: 如何解决两层Tabs出现滑动冲突的情况
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决两层Tabs出现滑动冲突的情况
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:9924f02ee55ac5b45837cd88a4cb21f4960a9a84792beeee92c254556a09c6b0
---

通过给外层Tabs设置scrollable(false)实现两层Tabs嵌套底部导航+顶部导航的组合，参考代码如下：

```typescript
@Entry
@Component
struct TwoLayerTabNestedSliding {
  build() {
    Column() {
      Tabs({ barPosition: BarPosition.End }) {
        TabContent() {
          Column() {
            Tabs() {
              TabContent() {
                Text('Focus on content')
              }
              .tabBar('follow with interest')
              TabContent() {
                Text('The content of the game')
              }
              .tabBar('game')
            }
          }
          .backgroundColor('#f08a34')
          .width('100%')
        }
        .tabBar('home page')
        TabContent() {
          Column() {
            Tabs() {
              TabContent() {
                Text('The content of technology')
              }
              .tabBar('science and technology')
              TabContent() {
                Text('The content of the video')
              }
              .tabBar('video')
            }
          }
          .backgroundColor('#f08a34')
          .width('100%')
        }
        .tabBar('find')
      }
      .scrollable(false)
    }
    .width('100%')
    .height('100%')
  }
}
```

[限制导航栏的滑动切换](../harmonyos-guides/arkts-navigation-tabs.md#双层tabs嵌套滑动)
