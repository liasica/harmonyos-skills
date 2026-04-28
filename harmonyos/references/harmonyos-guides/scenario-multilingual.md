---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-multilingual
title: 多语种场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 多语种场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5d8157cca4fd122aed5e200e2e2f07e98ae2da36b8ec8407a99196d5ee0ead0e
---

## 设计场景

当对朗读内容进行标注时，须对标注字符串进行多语种翻译，具体支持的语种和应用本身界面支持的语种保持一致。若采用多个字符串进行朗读内容的拼接，需考虑多语种的情况，避免拼接后朗读错误，例如阿拉伯语从右到左。

## 开发实例

```
1. @Entry
2. @Component
3. export struct Rule_2_1_10 {
4. title: string = 'Rule 2.1.10'
5. private multilingual: string = 'It is convenient: 屏幕朗读已开启 and use'

7. build() {
8. NavDestination() {
9. Column() {
10. Flex({
11. direction: FlexDirection.Column,
12. alignItems: ItemAlign.Center,
13. justifyContent: FlexAlign.Center,
14. }) {
15. Row() {
16. Text(this.multilingual)
17. .fontSize(30)
18. .fontColor(Color.Blue)
19. }
20. .width('80%')
21. }
22. .width('100%')
23. .height('100%')
24. .backgroundColor(Color.White)
25. }
26. }.title(this.title)
27. }
28. }
```
