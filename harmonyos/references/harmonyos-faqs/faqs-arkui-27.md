---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-27
title: List组件如何实现多列效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > List组件如何实现多列效果
category: harmonyos-faqs
scraped_at: 2026-04-29T14:16:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7e3602cb9432ce616f3947290979610540b95d457b117cc37b54c82d8bb68bd6
---

设置[List](../harmonyos-references/ts-container-list.md)组件的lanes属性，以实现交叉轴上的多列布局。示例代码如下：

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ListExample {
5. @State arr: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];

7. build() {
8. Column() {
9. List() {
10. ForEach(this.arr, (item: string) => {
11. ListItem() {
12. Row() {
13. Text(item)
14. .fontColor(Color.Red)
15. .fontSize(40)
16. }
17. }
18. .width('100%')
19. .border({
20. width: 1,
21. color: Color.Black,
22. radius: 5
23. })
24. })
25. }
26. .lanes(3)
27. .alignListItem(ListItemAlign.Center)
28. }
29. .padding({ top: 30 })
30. }
31. }
```

[ListImplementsMultiColumnEffect.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ListImplementsMultiColumnEffect.ets#L21-L51)

效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/gg5dh4zbT7qDxs224BBE_Q/zh-cn_image_0000002194158740.png?HW-CC-KV=V1&HW-CC-Date=20260429T061435Z&HW-CC-Expire=86400&HW-CC-Sign=EBC6DF64076FB6357466986586ECF8C060FA1A9ADEADFE5640504031521FAFC7 "点击放大")
