---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-215
title: 如何动态控制键盘绑定在不同的TextInput上
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:55+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3676c0fd82632e11cc26b20107e5215109facc63f0713e1a98c86f17b32b6fb0
---

软键盘的收起和弹出与输入框的获焦和失焦相关。可以通过 focusControl 动态控制输入框焦点的转移，从而控制软键盘的显示和隐藏。将焦点转移到目标输入框可以实现键盘的动态切换。参考代码如下：

```
1. @Entry
2. @Component
3. struct DynamicControlKeyboard {
4. // Whether focus is on "key1" TextInput
5. private flag: boolean = true;
6. @Builder
7. customKeyboardBuilder() {
8. Row() {
9. Text('Customize keyboard')
10. }
11. .justifyContent(FlexAlign.Center)
12. .width('1260px')
13. .height('1161px')
14. .backgroundColor(Color.Brown)
15. }
16. build() {
17. Column({space: 10}) {
18. TextInput()
19. .key('key1')
20. .onAppear(() => {
21. focusControl.requestFocus('key1');
22. })
23. .defaultFocus(true)
24. TextInput()
25. .key('key2')
26. .customKeyboard(this.customKeyboardBuilder())
27. Button('Switch TextInput')
28. .onClick(() => {
29. if (this.flag) {
30. console.info('TextInput2 ==> ' + focusControl.requestFocus('key2'));
31. } else {
32. console.info('TextInput1 ==> ' + focusControl.requestFocus('key1'));
33. }
34. this.flag = !this.flag;
35. })
36. Button()
37. .width(0)
38. .height(0)
39. .key('key3')
40. }
41. .padding({ top: 20 })
42. .width('100%')
43. .height('100%')
44. .onClick(() => {
45. focusControl.requestFocus('key3');
46. })
47. }
48. }
```

[DynamicallyControlKeyboardBinding.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DynamicallyControlKeyboardBinding.ets#L21-L68)

效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/ZKISCP9mTCCU8O6HyriW-w/zh-cn_image_0000002426207326.png?HW-CC-KV=V1&HW-CC-Date=20260428T002554Z&HW-CC-Expire=86400&HW-CC-Sign=50B0F0233AC9303E5284EC9D3FEA983CE7D4A870D30672F2DC6346FDD27F1FA6)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/HirB88-dTJ-IPvw5I3UcVA/zh-cn_image_0000002426218940.png?HW-CC-KV=V1&HW-CC-Date=20260428T002554Z&HW-CC-Expire=86400&HW-CC-Sign=2BF5C0036EC60DFCBE1CDC11E396D2CA46747B35B6BC8CD79ADD15652164B6FE)

**参考链接**

[focusControl](../harmonyos-references/ts-universal-attributes-focus.md#focuscontrol9)
