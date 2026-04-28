---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-34
title: 如何监听当前屏幕的横竖屏状态？如何实现页面跟随屏幕横竖屏自动旋转
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何监听当前屏幕的横竖屏状态？如何实现页面跟随屏幕横竖屏自动旋转
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:06+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:048332cad5bf2019f7cc77d1c312ef04aa67987058decc39a9f4da128f76024d
---

应用可以使用 display.on 监听屏幕状态的变化。

页面跟随屏幕旋转的方法如下：

1、Ability级别配置：在模块配置文件module.json5中配置abilities的orientation属性"。

2、动态设置窗口方向：使用 window.setPreferredOrientation。

```
1. import { window, display } from '@kit.ArkUI';

3. const TAG = 'ScreenTest'
4. const ORIENTATION: Array<string> = ['Portrait', 'Landscape', 'Reverse Portrait', 'Reverse Landscape']

6. @Entry
7. @Component
8. struct ScreenTest {
9. context = this.getUIContext();
10. @State rotation: number = 0
11. @State message: string = ORIENTATION[this.rotation]

13. aboutToAppear() {
14. this.setOrientation()

16. let callback = async () => {
17. // ...
18. }
19. try {
20. display.on("change", callback); // Listen for screen state changes
21. } catch (exception) {
22. console.error(TAG, 'Failed to register callback. Code: ' + JSON.stringify(exception));
23. }
24. }

26. setOrientation() {
27. try {
28. window.getLastWindow(this.context.getHostContext(), (err, data) => { // 获取window实例
29. if (err.code) {
30. console.error(TAG, 'Failed to obtain the top window. Cause: ' + JSON.stringify(err));
31. return;
32. }
33. let windowClass = data;
34. console.info(TAG, 'Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));

36. let orientation = window.Orientation.AUTO_ROTATION; // 设置窗口方向为传感器自动旋转模式。
37. try {
38. windowClass.setPreferredOrientation(orientation, (err) => {
39. if (err.code) {
40. console.error(TAG, 'Failed to set window orientation. Cause: ' + JSON.stringify(err));
41. return;
42. }
43. console.info(TAG, 'Succeeded in setting window orientation.');
44. });
45. } catch (exception) {
46. console.error(TAG, 'Failed to set window orientation. Cause: ' + JSON.stringify(exception));
47. }
48. ;
49. });
50. } catch (exception) {
51. console.error(TAG, 'Failed to obtain the top window. Cause: ' + JSON.stringify(exception));
52. }
53. ;
54. }

56. build() {
57. Row() {
58. Column() {
59. Text(`${this.rotation}`).fontSize(25)
60. Text(`${this.message}`).fontSize(25)
61. }
62. .width("100%")
63. }
64. .height("100%")
65. }
66. }
```

[ScreenorizontalVerticalStatus.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ScreenorizontalVerticalStatus.ets#L21-L86)

**参考链接**

[display.on](../harmonyos-references/js-apis-display.md#displayonaddremovechange)、[设置窗口的显示方向属性](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)
