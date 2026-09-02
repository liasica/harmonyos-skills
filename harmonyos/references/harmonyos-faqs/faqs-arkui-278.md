---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-278
title: 如何实现List/Swiper/Grid嵌套滚动的下拉刷新和上拉加载更多
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现List/Swiper/Grid嵌套滚动的下拉刷新和上拉加载更多
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f6b24cc21d2665114ca1d79af6dcdd24dd006d986e0b2345448951f089fad7fe
---

开发者可通过Refresh组件嵌套List实现下拉刷新。刷新逻辑在onRefreshing回调方法中执行。上拉加载更多给List添加onReachEnd事件回调，列表滑动到底部时触发。示例代码如下：

```ts
build() {
  Column() {
    // Search box at the top
    this.searchBarBuilder()
    // Pull down refresh component
    Refresh({ refreshing: $$this.isRefreshing }) {
      // List component as long list layout
      List({ space: 10 }) {
        // ListItem Customize the Swiper carousel module
        ListItem() {
          this.bannerBuilder()
        }
        // ListItem Custom Grid Quick Access Module
        ListItem() {
          this.quickBuilder()
        }
        // ListItem Custom Column Flash Sale Module
        ListItem() {
          this.flashBuilder()
        }
        // ListItemGroup Product Classification List
        this.productsBuilder()
        // 最后ListItem Customize bottom loading for more
        ListItem() {
          this.footerLoadingBuilder()
        }.height(50).width('100%').backgroundColor(0xeeeeee)
      }
      .sticky(StickyStyle.Header)
      .height('100%')
      // List component hits bottom to simulate network requests
      .onReachEnd(() => {
        // Load more data logic
      })
    }
    // Pull down refresh simulation network request
    .onRefreshing(() => {
      // Data refresh logic
    })
    .layoutWeight(1)
    .width('100%')
  }
}
```
