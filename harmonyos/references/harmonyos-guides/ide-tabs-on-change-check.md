---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tabs-on-change-check
title: @performance/tabs-on-change-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/tabs-on-change-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:19+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:c9cb8f131f1ebeb300d5b31d79409e38f0ee04c1579b42032e826e0100029fff
---

推荐使用onAnimationStart事件设置切换标签动效。避免使用onChange事件会导致页面切换后再触发动效，造成效果延迟。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/tabs-on-change-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Builder
2. TabBuilder(id: number, index: number) {
3. Column() {
4. Text(this.tabBarArray[id].name)
5. .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)
6. }
7. .alignItems(HorizontalAlign.Start)
8. }
9. build() {
10. Tabs({ barPosition: BarPosition.Start }) {
11. ForEach(this.tabBarArray, (tabsItem: NewsTypeModel, index: number) => {
12. TabContent() {
13. }.tabBar(this.TabBuilder(xx, xx))
14. }, (item: NewsTypeModel) => JSON.stringify(item));
15. }
16. .onAnimationStart((_index: number, targetIndex: number, _event: TabsAnimationEvent) => {
17. this.currentIndex = targetIndex;
18. })
19. }
```

## 反例

```
1. @Builder
2. TabBuilder(id: number, index: number) {
3. Column() {
4. Text(this.tabBarArray[id].name)
5. .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)
6. }
7. .alignItems(HorizontalAlign.Start)
8. }
9. build() {
10. Tabs({ barPosition: BarPosition.Start }) {
11. ForEach(this.tabBarArray, (tabsItem: NewsTypeModel, index: number) => {
12. TabContent() {
13. }.tabBar(this.TabBuilder(xx, xx))
14. }, (item: NewsTypeModel) => JSON.stringify(item));
15. }
16. .onChange((_index: number) => {
17. this.currentIndex = _index;
18. })
19. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
