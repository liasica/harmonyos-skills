---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-onanimationstart-in-swiper
title: @performance/hp-arkui-use-onAnimationStart-for-swiper-preload
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-onAnimationStart-for-swiper-preload
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:09+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ded9efa24f5ca03a7ce6d048f51e59da668f9459affbcc1b3b05235b81d34ebc
---

建议Swiper预加载机制搭配 OnAnimationStart 接口回调使用。

滑动丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-use-onAnimationStart-for-swiper-preload": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import image from '@ohos.multimedia.image';
2. // 源码文件，请以工程实际为准
3. import { MyDataSource } from './MyDataSource';
4. import { PhotoItem } from './component/ChildComponent';
5. import { MyObject } from './data/DataEntry';

7. @Entry
8. @Component
9. struct MyComponent {
10. cacheCount: number = 1;
11. swiperController: SwiperController = new SwiperController();
12. private data: MyDataSource = new MyDataSource([]);

14. build() {
15. Swiper(this.swiperController) {
16. LazyForEach(this.data, (item: MyObject, index?: number) => {
17. // 源码文件，请以工程实际为准
18. PhotoItem({ myIndex: index, dataSource: this.data })
19. }, (item: MyObject) => item.id) // item唯一id
20. }
21. .cachedCount(this.cacheCount)
22. .indicator(true)
23. .loop(false)
24. // 在OnAnimationStart接口回调中进行预加载资源的操作
25. .onAnimationStart((index: number, targetIndex: number) => {
26. if (targetIndex !== index) {
27. try {
28. // 获取resourceManager资源管理器
29. const resourceMgr = this.getUIContext().getHostContext()?.resourceManager;
30. // 获取rawfile文件夹下icon.png的ArrayBuffer
31. let str = "item" + (targetIndex + this.cacheCount + 2) + ".jpg";
32. resourceMgr?.getRawFileContent(str).then((value) => {
33. // 创建imageSource
34. const imageSource = image.createImageSource(value.buffer);
35. imageSource.createPixelMap().then((value) => {
36. this.data.addData(targetIndex + this.cacheCount + 1, {
37. description: "" + (targetIndex + this.cacheCount + 1),
38. image: value
39. })
40. })
41. })
42. } catch (err) {
43. console.log("error code" + err);
44. }
45. }
46. })
47. .width('100%')
48. .height('100%')
49. }
50. }
```

## 反例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';
3. import { PhotoItem } from './component/ChildComponent';
4. import { MyObject } from './data/DataEntry';

7. @Entry
8. @Component
9. struct MyComponent {
10. cacheCount: number = 1;
11. swiperController: SwiperController = new SwiperController();
12. private data: MyDataSource = new MyDataSource([]);
13. context = getContext(this);

15. build() {
16. // Swiper组件没有使用OnAnimationStart进行预加载
17. Swiper(this.swiperController) {
18. LazyForEach(this.data, (item: MyObject, index?: number) => {
19. // 源码文件，请以工程实际为准
20. PhotoItem({ myIndex: index, dataSource: this.data })
21. }, (item: MyObject) => item.id)
22. }
23. .cachedCount(this.cacheCount)
24. .indicator(true)
25. .loop(false)
26. .width('100%')
27. .height('100%')
28. }
29. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
