---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/app-compatibility-ui-component
title: UI自定义组件兼容性指导
breadcrumb: 版本说明 > 应用兼容性说明 > 应用开发中的兼容性场景开发指导 > UI自定义组件兼容性指导
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:18+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:b825e0ec018a6135b7995479c8e225c5125f19c573af9366c600c2b1dc26f38d
---

在UI自定义组件中，状态管理装饰器需要通过自定义组件进行API版本隔离。

例如：在滚动列表滑动复用场景，@ReusableV2自定义组件复用新特性的API是在SDK版本5.1.0(18)提供，为了让应用兼容在基于API版本5.0.0(12)的老设备正常运行，开发者可以使用deviceInfo.sdkApiVersion进行兼容性判断。

（1）开发者需要提供基于API版本5.0.0(12)的自定义组件“V1Component” 及 5.1.0(18)的复用自定义组件“ReuseComponentV2”；

（2）在LazyForEach中使用 deviceInfo.sdkApiVersion进行兼容判断使用哪个自定义组件。

代码示例如下：

```
1. import { deviceInfo } from '@kit.BasicServicesKit';

3. class BasicDataSource implements IDataSource {
4. private listener: DataChangeListener | undefined = undefined;
5. public dataArray: number[] = [];
6. totalCount(): number {
7. return this.dataArray.length;
8. }
9. getData(index: number): number {
10. return this.dataArray[index];
11. }
12. registerDataChangeListener(listener: DataChangeListener): void {
13. this.listener = listener;
14. }
15. unregisterDataChangeListener(listener: DataChangeListener): void {
16. this.listener = undefined;
17. }
18. }

20. @Entry
21. @ComponentV2
22. struct Index {
23. private data: BasicDataSource = new BasicDataSource();
24. aboutToAppear(): void {
25. for (let index = 1; index < 20; index++) {
26. this.data.dataArray.push(index);
27. }
28. }
29. build() {
30. List() {
31. LazyForEach(this.data, (item: number, index: number) => {
32. ListItem() {
33. if (deviceInfo.sdkApiVersion >= 18) {
34. ReuseComponentV2({ num: item }) // 在ROM的API版本是5.1.0(18)及以上，使用@ReusableV2的复用组件
35. } else {
36. V1Component({ num: item })  // 在ROM的API版本是5.1.0(18)以下，使用V1的的普通组件
37. }
38. }
39. }, (item: number, index: number) => index.toString())
40. }.cachedCount(1)
41. }
42. }

44. // 状态管理V1的自定义组件
45. @Component
46. struct V1Component {   // V1的复用自定义组件
47. @State num: number = 0;
48. aboutToAppear(): void {
49. console.log(`V1Component-- aboutToAppear`)  // 如果是5.1.0(18)以下的版本，V1的会创建
50. }
51. build() {
52. BaseCom(this.num)  // 公共UI
53. }
54. }
55. // 状态管理V2的自定义组件
56. @ReusableV2
57. @ComponentV2
58. struct ReuseComponentV2 {  // V2的复用自定义组件
59. @Param num: number = 0;
60. aboutToReuse(): void {
61. console.log(`ReuseComponentV2-- aboutToReusableV2`) // 如果是5.1.0(18)及以上的版本，V2复用组件生效
62. }

64. build() {
65. BaseCom(this.num)
66. }
67. }

69. // 公共的UI
70. @Builder function BaseCom(num: number) {  // 使用@Builder抽取公共UI组件
71. Column() {
72. Text('ReuseComponentChild num:' + num.toString())
73. }.height(200)
74. }
```

在上述示例中，通过deviceInfo.sdkApiVersion来判断API版本：

（1）当识别当前设备ROM的API版本是5.1.0(18)及以上版本的设备，V2的复用组件会生效，往下滑动页面，会打印"ReuseComponentV2-- aboutToReusableV2"日志，即“ReuseComponentV2”的组件在滑动过程被复用；

（2）如果是5.1.0(18)以下的版本，会创建V1组件，会打印"V1Component-- aboutToAppear"的日志，即“V1Component”的组件在滑动过程被创建。
