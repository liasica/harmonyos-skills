---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-302
title: 如何获取组件渲染完成时间
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取组件渲染完成时间
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:170c82e46ea0a75f1885bbb14d52432df389bc8cec9055afc80a27487995c7f1
---

可以通过@kit.ArkUI.inspector(绘制完成回调) 接口获取绘制完成回调的通知。 创建ComponentObserver实例 ，注册draw事件监听 ，在aboutToAppear中记录开始时间，在listener中监听绘制完成的回调，获取绘制完成的时间。时间差即为组件渲染时间。示例代码如下：

```
1. import { inspector } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct GetComponentRenderTime {
6. @State startTime: number = 0;
7. private listener: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('IMAGE_ID');
8. // Calculate rendering duration: currentTime - this.startTime
9. private onDrawCompleteCallback = () => {
10. // 2. Time when the image component finishes drawing
11. console.info('onDrawComplete', new Date().getTime());
12. };

14. aboutToAppear() {
15. // 1. Time when rendering starts
16. this.startTime = new Date().getTime();
17. console.info('aboutToAppear', this.startTime);

19. // layout: Component layout completed
20. // draw: Component drawing completed
21. this.listener.on('draw', this.onDrawCompleteCallback);
22. }

24. aboutToDisappear() {
25. // Unregister callback before destruction
26. this.listener.off('draw', this.onDrawCompleteCallback);
27. }

29. build() {
30. Column() {
31. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
32. Row({ space: 5 }) {
33. Image($r('app.media.app_icon'))
34. .width(110)
35. .height(110)
36. .id('IMAGE_ID')
37. }
38. }
39. }
40. .height(320)
41. .width(360)
42. .padding({
43. right: 10,
44. top: 10
45. })
46. }
47. }
```

[GetComponentRenderingTime.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetComponentRenderingTime.ets#L21-L67)
