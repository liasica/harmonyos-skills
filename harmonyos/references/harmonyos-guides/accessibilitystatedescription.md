---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/accessibilitystatedescription
title: 自定义控件播报状态的场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 自定义控件播报状态的场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:44c47bdf76225b6870fb08e782f0dab18ab637b4cb548f91910ccb49458d1373
---

## 设计场景

可切换状态的控件可以处于“已选中”或“未选中”状态，屏幕朗读功能可以从控件的语义属性中推导出默认状态说明标签。在某些情况下，推导出的默认状态说明标签不能完全适用于应用场景，此时可以通过[accessibilityStateDescription](../harmonyos-references/ts-universal-attributes-accessibility.md)指定状态说明标签进行判断。屏幕朗读模式下，若指定了可点击控件的状态说明标签，当用户聚焦控件或执行双击操作后，屏幕朗读会播报指定的状态说明标签。

## accessibilityStateDescription说明

* [description](../harmonyos-references/ts-universal-attributes-accessibility.md)：指定组件的状态说明标签，支持string类型和Resource类型，默认值为空。

## 开发实例

如下示例实现一个收藏按钮，点击可切换状态，播报指定的状态说明标签：

```
1. @Entry
2. @Component
3. struct Rule_2_1_14 {
4. title: string = 'Rule 2.1.14';
5. // 收藏按钮状态，表示是否被选中
6. @State private isSelected: boolean = false;

8. build() {
9. NavDestination() {
10. Column() {
11. Button() {
12. // 根据状态显示不同的图标
13. Image(this.isSelected ? $r('app.media.favorIcon') : $r('app.media.unfavorIcon'))
14. .width(30)
15. .height(30)
16. }
17. // 指定按钮的状态说明标签，"已收藏"或"未收藏"
18. .accessibilityStateDescription(this.isSelected ? "已收藏" : "未收藏")
19. // 设置按钮的选中状态
20. .accessibilitySelected(this.isSelected)
21. // 按钮点击事件处理程序，切换选中状态
22. .onClick(() => {
23. this.isSelected = !this.isSelected;
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. .title(this.title)
30. }
31. }
```
