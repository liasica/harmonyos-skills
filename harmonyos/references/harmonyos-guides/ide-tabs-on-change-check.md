---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tabs-on-change-check
title: "@performance/tabs-on-change-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/tabs-on-change-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8334b1df7f51f68c50bedfd4711021ef63ec1a87bfa770319f471a83aa242eec
---

推荐使用onAnimationStart事件设置切换标签动效。使用onChange事件会导致页面切换后再触发动效，造成效果延迟。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/tabs-on-change-check": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Builder
TabBuilder(id: number, index: number) {
  Column() {
    Text(this.tabBarArray[id].name)
      .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)
  }
  .alignItems(HorizontalAlign.Start)
}
build() {
  Tabs({ barPosition: BarPosition.Start }) {
    ForEach(this.tabBarArray, (tabsItem: NewsTypeModel, index: number) => {
      TabContent() {
      }.tabBar(this.TabBuilder(xx, xx))
    }, (item: NewsTypeModel) => JSON.stringify(item));
  }
  .onAnimationStart((_index: number, targetIndex: number, _event: TabsAnimationEvent) => {
    this.currentIndex = targetIndex;
  })
}
```

## 反例

```screen
@Builder
TabBuilder(id: number, index: number) {
  Column() {
    Text(this.tabBarArray[id].name)
      .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)
  }
  .alignItems(HorizontalAlign.Start)
}
build() {
  Tabs({ barPosition: BarPosition.Start }) {
    ForEach(this.tabBarArray, (tabsItem: NewsTypeModel, index: number) => {
      TabContent() {
      }.tabBar(this.TabBuilder(xx, xx))
    }, (item: NewsTypeModel) => JSON.stringify(item));
  }
  .onChange((_index: number) => {
    this.currentIndex = _index;
  })
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
