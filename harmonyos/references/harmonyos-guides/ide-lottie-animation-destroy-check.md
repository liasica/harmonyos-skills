---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-lottie-animation-destroy-check
title: @performance/lottie-animation-destroy-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/lottie-animation-destroy-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:14+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:9c9d7c3efedce31c83eacb5054f00f4e51788e143146c1f6724ed0f6d51589af
---

该规则检测使用lottie加载的动画是否都正确销毁。

当使用lottie加载动画时，一般需要先通过lottie.loadAnimation将动画加载到内存，动画执行完毕后需要在合适的时机（例如：onDisAppear，onPageHide，aboutToDisappear）通过调用animationItem的destroy方法将单个动画销毁或者调用lottie.destroy()方法将当前页面所有动画销毁，如果动画未被销毁就会造成资源浪费，影响应用性能体验。

内存优化场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/lottie-animation-destroy-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例1

```
1. import lottie from '@ohos/lottie';   //需安装@ohos/lottie依赖后import
2. import { AnimationItem } from '@ohos/lottie';    //需安装@ohos/lottie依赖后import

4. const FRAME_START: number = 60;
5. const FRAME_END: number = 120;

7. @Entry
8. @Component
9. struct LottieAnimation1 {
10. private politeChickyController: CanvasRenderingContext2D = new CanvasRenderingContext2D();
11. private politeChicky: string = 'politeChicky';
12. private politeChickyPath: string = 'media/politeChicky.json';
13. private animateItem?: AnimationItem;

15. build() {
16. Canvas(this.politeChickyController)
17. .width(160)
18. .height(160)
19. .borderRadius(3)
20. .onReady(() => {
21. this.animateItem = lottie.loadAnimation({
22. container: this.politeChickyController,
23. renderer: 'canvas',
24. loop: true,
25. autoplay: true,
26. name: this.politeChicky,
27. path: this.politeChickyPath,
28. initialSegment: [FRAME_START, FRAME_END]
29. })
30. })
31. .onDisAppear(() => {
32. this.animateItem?.destroy();//只加载了一个Animation，可以使用animateItem的destroy接口
33. })
34. }
35. }
```

## 正例2

```
1. import lottie from '@ohos/lottie';
2. import { AnimationItem } from '@ohos/lottie';

4. // 动画播放的起始帧
5. const FRAME_START: number = 60;
6. // 动画播放的终止帧
7. const FRAME_END: number = 120;

9. @Entry
10. @Component
11. struct LottieAnimation2 {
12. private politeChickyController: CanvasRenderingContext2D = new CanvasRenderingContext2D();
13. // 动画名称
14. private politeChicky: string = 'politeChicky';
15. // hap包内动画资源文件路径，仅支持json格式
16. private politeChickyPath: string = 'media/politeChicky.json';
17. private animateItem: AnimationItem | null = null;

19. build() {
20. Canvas(this.politeChickyController)
21. .width(160)
22. .height(160)
23. .borderRadius(3)
24. .onReady(() => {
25. this.animateItem = lottie.loadAnimation({
26. container: this.politeChickyController,
27. renderer: 'canvas',
28. loop: true,
29. autoplay: true,
30. name: 'anim_name1',
31. path: this.politeChickyPath,
32. initialSegment: [FRAME_START, FRAME_END]
33. })
34. })
35. .onClick(() => {
36. this.animateItem = lottie.loadAnimation({
37. container: this.politeChickyController,
38. renderer: 'canvas',
39. loop: true,
40. autoplay: true,
41. name: 'anim_name2',
42. path: this.politeChickyPath,
43. initialSegment: [FRAME_START, FRAME_END]
44. })
45. })
46. }

48. onPageHide(): void {
49. lottie.destroy();
50. }
51. }
```

## 反例1

```
1. import lottie from '@ohos/lottie';
2. import { AnimationItem } from '@ohos/lottie';

4. const FRAME_START: number = 60;
5. const FRAME_END: number = 120;

7. @Entry
8. @Component
9. struct LottieAnimation1 {
10. private politeChickyController: CanvasRenderingContext2D = new CanvasRenderingContext2D();
11. private politeChicky: string = 'politeChicky';
12. private politeChickyPath: string = 'media/politeChicky.json';
13. private animateItem?: AnimationItem;

15. build() {
16. Canvas(this.politeChickyController)
17. .width(160)
18. .height(160)
19. .backgroundColor(Color.Gray)
20. .borderRadius(3)
21. .onReady(() => {
22. //告警
23. this.animateItem = lottie.loadAnimation({
24. container: this.politeChickyController,
25. renderer: 'canvas',
26. loop: true,
27. autoplay: true,
28. name: this.politeChicky,
29. path: this.politeChickyPath,
30. initialSegment: [FRAME_START, FRAME_END]
31. })
32. })
33. }
34. }
```

## 反例2

```
1. import lottie from '@ohos/lottie';
2. import { AnimationItem } from '@ohos/lottie';

4. // 动画播放的起始帧
5. const FRAME_START: number = 60;
6. // 动画播放的终止帧
7. const FRAME_END: number = 120;

9. //调用多次loadAnimation，但是只在onDisAppear销毁一次
10. @Entry
11. @Component
12. struct LottieAnimation4 {
13. private politeChickyController: CanvasRenderingContext2D = new CanvasRenderingContext2D();
14. // 动画名称
15. private politeChicky: string = 'politeChicky';
16. // hap包内动画资源文件路径，仅支持json格式
17. private politeChickyPath: string = 'media/politeChicky.json';
18. private animateItem: AnimationItem | null = null;
19. // 初始化点击次数
20. @State times: number = 0;

22. build() {
23. Stack({ alignContent: Alignment.TopStart }) {
24. // 动画
25. Canvas(this.politeChickyController)
26. .width(160)
27. .height(160)
28. .backgroundColor(Color.Gray)
29. .borderRadius(3)
30. .onReady(() => {
31. this.animateItem = lottie.loadAnimation({
32. container: this.politeChickyController,
33. renderer: 'canvas',
34. loop: true,
35. autoplay: true,
36. name: this.politeChicky,
37. path: this.politeChickyPath,
38. initialSegment: [FRAME_START, FRAME_END]
39. })
40. })
41. .onClick(() => {
42. this.animateItem = lottie.loadAnimation({
43. container: this.politeChickyController,
44. renderer: 'canvas',
45. loop: true,
46. autoplay: true,
47. name: this.politeChicky,
48. path: this.politeChickyPath,
49. initialSegment: [FRAME_START, FRAME_END]
50. })
51. this.times++;
52. })
53. .onDisAppear(()=> {
54. //上报此处animateItem，描述description不一样，如果无法找到动画名称，则直接建议用lottie.destroy
55. this.animateItem?.destroy();
56. })
57. // 响应动画的文本
58. Text('text')
59. .fontSize(16)
60. .margin(10)
61. .fontColor(Color.White)
62. }.margin({ top: 20 })
63. }
64. }
```

## 反例3

```
1. import lottie from '@ohos/lottie';
2. import { AnimationItem } from '@ohos/lottie';

4. // 动画播放的起始帧
5. const FRAME_START: number = 60;
6. // 动画播放的终止帧
7. const FRAME_END: number = 120;

9. //调用了销毁，但是不是全部销毁，上报
10. @Entry
11. @Component
12. struct LottieAnimation5 {
13. private politeChickyController: CanvasRenderingContext2D = new CanvasRenderingContext2D();
14. // 动画名称
15. private politeChicky: string = 'politeChicky';
16. // hap包内动画资源文件路径，仅支持json格式
17. private politeChickyPath: string = 'media/politeChicky.json';
18. private animateItem: AnimationItem | null = null;

20. build() {
21. Canvas(this.politeChickyController)
22. .width(160)
23. .height(160)
24. .backgroundColor(Color.Gray)
25. .borderRadius(3)
26. .onReady(() => {
27. this.animateItem = lottie.loadAnimation({
28. container: this.politeChickyController,
29. renderer: 'canvas',
30. loop: true,
31. autoplay: true,
32. name: 'anim_name1',
33. path: this.politeChickyPath,
34. initialSegment: [FRAME_START, FRAME_END]
35. })
36. })
37. .onClick(()=> {
38. this.animateItem = lottie.loadAnimation({
39. container: this.politeChickyController,
40. renderer: 'canvas',
41. loop: true,
42. autoplay: true,
43. name: 'anim_name2',
44. path: this.politeChickyPath,
45. initialSegment: [FRAME_START, FRAME_END]
46. })
47. })
48. .onDisAppear(()=>{
49. //上报lottie,只销毁一个
50. lottie.destroy('anim_name2');
51. })
52. }
53. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
