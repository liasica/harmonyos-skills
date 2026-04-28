---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-350
title: bindPopup适配Web组件长按菜单功能，设置offset控制弹窗的偏移
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > bindPopup适配Web组件长按菜单功能，设置offset控制弹窗的偏移
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5be39d8f6c81011accf2d8c21c75154d0d9835415e0f27e10d5daf967e98dcbf
---

由于WebView组件本身不支持直接绑定Popup，需在同层添加透明占位组件作为Popup载体，可以在 WebView 组件前（同层）添加一个大小为 0 的组件来承载 bindPopup。根据当前 UX 规范，弹出菜单的边距左右各为 7vp，以确保其在屏幕范围内。具体代码如下：

```
1. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct BindPopupOffset {
7. controller: webview.WebviewController = new webview.WebviewController();
8. private result: WebContextMenuResult | undefined = undefined;
9. @State linkUrl: string = '';
10. @State offsetX: number = 0;
11. @State offsetY: number = 0;
12. @State showMenu: boolean = false;

15. @Builder
16. menuBuilder() {
17. Menu() {
18. MenuItem({
19. content: 'copy picture',
20. })
21. .width(100)
22. .height(50)
23. .onClick(() => {
24. this.result?.copyImage();
25. this.showMenu = false;
26. })
27. MenuItem({
28. content: 'cut'
29. })
30. .width(100)
31. .height(50)
32. .onClick(() => {
33. this.result?.cut();
34. this.showMenu = false;
35. })
36. }
37. .width(150)
38. .backgroundColor('#eeeeee')
39. }

42. build() {
43. Column() {
44. Row()
45. .width(0)
46. .height(0)
47. .position({ x: 0, y: 0 })
48. .bindPopup(this.showMenu,
49. {
50. builder: this.menuBuilder(),
51. enableArrow: false,
52. placement: Placement.LeftTop,
53. targetSpace: 0,
54. shadow: {
55. radius: 0
56. },
57. offset: {
58. x: this.offsetX - 7,
59. y: this.offsetY
60. },
61. mask: false,
62. onStateChange: (e) => {
63. if (!e.isVisible) {
64. this.showMenu = false;
65. this.result?.closeContextMenu();
66. }
67. }
68. })

70. // index.html It should include elements that trigger the contextmenu event.
71. Web({ src: $rawfile('index.html'), controller: this.controller })//Trigger custom pop ups
72. .onContextMenuShow((event) => {
73. if (event) {
74. this.result = event.result;
75. this.showMenu = true;
76. this.offsetX = Math.max(this.getUIContext().px2vp(event?.param.x() ?? 0) - 0, 0);
77. this.offsetY = Math.max(this.getUIContext().px2vp(event?.param.y() ?? 0) - 0, 0);
78. }
79. return true;
80. })
81. }
82. }
83. }
```

[BindPopupAdaptsToTheWeb.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/BindPopupAdaptsToTheWeb.ets#L21-L103)
