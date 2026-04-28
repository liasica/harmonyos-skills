---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-303
title: Toggle组件设置拖动的同时如何屏蔽其本身的点击手势
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Toggle组件设置拖动的同时如何屏蔽其本身的点击手势
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f6b529ea629c865c143cfe60a3bdf21ae11014ac0008fd57196d0b13573a8469
---

通过isDragging状态变量区分拖动与点击操作，在拖动过程中屏蔽toggleIsOn的状态变更，示例代码如下：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct ToggleDrag {
7. @State offsetX: number = 0;
8. @State offsetY: number = 0;
9. @State positionX: number = 0;
10. @State positionY: number = 0;
11. @State toggleIsOn: boolean = true;
12. // Marks whether the current drag state is used to block click events
13. private isDragging: boolean = false;

16. build() {
17. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
18. Toggle({ type: ToggleType.Button, isOn: this.toggleIsOn }) {
19. Text('Toggle')
20. }
21. .selectedColor(Color.Pink)
22. // Onchange callback precedes onActionEnd
23. .onChange((isOn: boolean) => {
24. hilog.info(0x0000, 'TOGGLE_DRAG', 'xxx %{public}s', `onClick Toggle, isOn: ${isOn}`);
25. console.info('isDragging======' + this.isDragging);
26. if (isOn === this.toggleIsOn) {
27. return;
28. } else {
29. this.toggleIsOn = isOn;
30. }
31. if (this.isDragging) {
32. this.toggleIsOn = !this.toggleIsOn;
33. }
34. })
35. .translate({ x: this.offsetX, y: this.offsetY })
36. .gesture(
37. PanGesture()
38. .onActionStart(() => {
39. this.isDragging = true;
40. })
41. .onActionUpdate((event: GestureEvent) => {
42. this.offsetX = this.positionX + event.offsetX;
43. this.offsetY = this.positionY + event.offsetY;
44. })
45. .onActionEnd(() => {
46. this.positionX = this.offsetX;
47. this.positionY = this.offsetY;
48. this.isDragging = false;
49. })
50. )
51. }
52. }
53. }
```

[ToggleComponentBlocksClickGestures.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ToggleComponentBlocksClickGestures.ets#L21-L73)

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/2NbazlMjSnS9N0SsNsf5Ww/zh-cn_image_0000002229758509.png?HW-CC-KV=V1&HW-CC-Date=20260428T002615Z&HW-CC-Expire=86400&HW-CC-Sign=9707286761A525C152B04D7D1104E11DA2361FDE483CCA0692836B37AA1D1650)
