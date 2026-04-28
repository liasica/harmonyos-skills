---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-394
title: 如何对手势事件进行限流防止连续识别，例如500ms内不允许点击事件重复触发？如何对多个手势进行统一限流
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何对手势事件进行限流防止连续识别，例如500ms内不允许点击事件重复触发？如何对多个手势进行统一限流
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:003b3fee36c976a04f2d4a1a5a8265da68d9c046cae8f9a1efe9a25aec57409e
---

可以自定义节流函数。

```
1. // Debouncing: When a function is triggered multiple times within a certain period, debouncing ensures that the function is ultimately executed only once after a specified delay
2. export function debounce(func: (event: ClickEvent) => void, delay?: number) {
3. let timer: number;
4. return (event: ClickEvent) => {
5. clearTimeout(timer);
6. timer = setTimeout(() => {
7. func(event);
8. }, delay ? delay : 1000);
9. };
10. }

12. // Throttling: Execute only once within the specified time frame
13. export function throttle(func: (event: ClickEvent) => void, delay?: number) {
14. let inThrottle: boolean;
15. return (event: ClickEvent) => {
16. if (!inThrottle) {
17. func(event);
18. inThrottle = true;
19. setTimeout(() => inThrottle = false, delay ? delay : 1000);
20. }
21. };
22. }

24. @Entry
25. @Component
26. struct Index {
27. @State num: number = 0

29. build() {
30. Row() {
31. Column() {
32. Text(this.num.toString())
33. Button("click")
34. .onClick(
35. debounce(() => {
36. this.num++
37. }, 500))
38. }
39. .width('100%')
40. }
41. .height('100%')
42. }
43. }
```

[GestureRateLimiting.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GestureRateLimiting.ets#L21-L63)

如果手势在多处使用，且都需要限流，可以考虑用[GestureModifier](../harmonyos-references/ts-universal-attributes-gesture-modifier.md#gesturemodifier)。

以下示例，演示了TapGesture和LongPressGesture共用一个限流函数，即点击事件、长按事件在2000ms内只能触发一次。

```
1. class MyGesture implements GestureModifier {
2. interval: number = 2000;
3. private inThrottle: boolean = false;
4. private lastGestureType: string = '';

6. // Unified rate limiting processing
7. private throttleWrapper(eventType: string, callback: () => void) {
8. if (!this.inThrottle) {
9. this.inThrottle = true;
10. this.lastGestureType = eventType;
11. callback();

13. setTimeout(() => {
14. this.inThrottle = false;
15. this.lastGestureType = '';
16. }, this.interval);
17. }
18. }

20. applyGesture(event: UIGestureEvent): void {
21. // Create a unified gesture processing function
22. const handleTap = (gestureEvent: GestureEvent) => {
23. this.throttleWrapper('tap', () => {
24. console.info('---onTap---');
25. });
26. };

28. const handleLongPress = (gestureEvent: GestureEvent) => {
29. this.throttleWrapper('longPress', () => {
30. console.info('---onLongPress---');
31. });
32. };

34. // Add two gesture recognizers
35. event.addGesture(
36. new TapGestureHandler({ count: 1, fingers: 1 })
37. .onAction(handleTap)
38. );

40. event.addGesture(
41. new LongPressGestureHandler({ fingers: 1, duration: 600 })
42. .onAction(handleLongPress)
43. );
44. }
45. }

47. @Entry
48. @Component
49. struct Index {
50. @State message: string = 'Hello World';
51. @State modifier: MyGesture = new MyGesture();

53. build() {
54. RelativeContainer() {
55. Button(this.message)
56. .id('click')
57. .fontSize(50)
58. .fontWeight(FontWeight.Bold)
59. .alignRules({
60. center: { anchor: "__container__", align: VerticalAlign.Center },
61. middle: { anchor: "__container__", align: HorizontalAlign.Center }
62. })
63. .gestureModifier(this.modifier)
64. }
65. .height('100%')
66. .width('100%')
67. }
68. }
```

[CustomRateLimiting.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CustomRateLimiting.ets#L21-L89)
