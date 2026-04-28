---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-screen-reading
title: 标注屏幕朗读内容的场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 标注屏幕朗读内容的场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:439416efc78c61fb0341b9e8e66ea2b2119c156ab8b17628a67a233e42a714cd
---

## 设计场景

屏幕朗读提取信息进行朗读时无障碍文本的优先级大于显示文本，即当无障碍文本不为空时，会朗读无障碍文本，否则朗读显示文本。因此，在进行应用设计时，需要遵守如下规则：

* 对于文本类控件，尽量使用显示文本来表达信息，使视障用户和视力健全用户可以获取到相同的信息。
* 对于文本类控件，如果除显示文本外，还额外提供了颜色等视觉效果为视力健全用户提供了更多信息的场景，可采用无障碍文本为视障用户提供更多的信息用于朗读。
* 对于非文本类控件，可采用无障碍文本为视障用户提供朗读信息。

## 开发实例

以accessibilityText( ) 设置无障碍文本为例，accessibilityText( ) 设置无障碍文本。聚焦button时朗读效果为："Accessibility text，按钮"。

```
1. @Entry
2. @Component
3. export struct Rule_2_1_1 {
4. title: string = 'Rule 2.1.1';
5. shortText: string = 'Button';
6. longText: string = 'Accessibility text';

8. build() {
9. NavDestination() {
10. Column() {
11. Blank()
12. Button(this.shortText)
13. .accessibilityText(this.longText)
14. .align(Alignment.Center)
15. .fontSize(20)
16. Blank()
17. }
18. .width('100%')
19. .height('100%')
20. }
21. .title(this.title)
22. }
23. }
```
