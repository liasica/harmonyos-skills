---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-page
title: 启动指定页面
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > PageAbility组件开发指导 > 启动指定页面
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:57+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bc2d9e1cb6ec45c0b92e4e5d041e63b3dafd958f892a683a89b7d8b3c65ab1ef
---

当PageAbility的启动模式设置为单例时（具体设置方法和典型场景示例见[PageAbility的启动模式](pageability-launch-type.md)，缺省情况下是单实例模式），若PageAbility已被拉起，再次启动PageAbility会触发onNewWant回调（即非首次拉起）。开发者可以通过Want传递启动参数，例如开发者希望指定页面启动PageAbility，可以通过Want中的parameters参数传递pages信息，具体示例代码如下：

调用方PageAbility的app.ets中或者page中，使用startAbility再次拉起PageAbility，通过Want中的uri参数传递页面信息：

```
1. import featureAbility from '@ohos.ability.featureAbility';
2. import Want from '@ohos.app.ability.Want';
3. import hilog from '@ohos.hilog';

5. const TAG: string = 'PagePageAbilityFirst';
6. const domain: number = 0xFF00;
```

```
1. (async (): Promise<void> => {
2. let wantInfo: Want = {
3. bundleName: 'com.samples.famodelabilitydevelop',
4. abilityName: 'com.samples.famodelabilitydevelop.PageAbilitySingleton',
5. parameters: { page: 'pages/second' }
6. };
7. featureAbility.startAbility({ want: wantInfo }).then((data) => {
8. hilog.debug(domain, TAG, `restartAbility success : ${data}`);
9. });
10. })()
```

在目标端PageAbility的onNewWant回调中获取包含页面信息的want参数：

```
1. // GlobalContext.ts 构造单例对象
2. export class GlobalContext {
3. private constructor() {
4. }

6. private static instance: GlobalContext;
7. private _objects = new Map<string, Object>();

9. public static getContext(): GlobalContext {
10. if (!GlobalContext.instance) {
11. GlobalContext.instance = new GlobalContext();
12. }
13. return GlobalContext.instance;
14. }

16. getObject(value: string): Object | undefined {
17. return this._objects.get(value);
18. }

20. setObject(key: string, objectClass: Object): void {
21. this._objects.set(key, objectClass);
22. }
23. }
```

```
1. import Want from '@ohos.app.ability.Want';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import { GlobalContext } from '../utils/GlobalContext';

5. class PageAbilitySingleton {
6. onNewWant(want: Want) {
7. featureAbility.getWant().then((want) => {
8. GlobalContext.getContext().setObject('newWant', want);
9. })
10. }
11. }

13. export default new PageAbilitySingleton();
```

在目标端页面的自定义组件中获取包含页面信息的want参数并根据uri做路由处理：

```
1. import Want from '@ohos.app.ability.Want';
2. import router from '@ohos.router';
3. import { GlobalContext } from '../../utils/GlobalContext';

5. @Entry
6. @Component
7. struct First {
8. onPageShow() {
9. let newWant = GlobalContext.getContext().getObject('newWant') as Want;
10. if (newWant) {
11. if (newWant.parameters) {
12. if (newWant.parameters.page) {
13. router.pushUrl({ url: newWant.parameters.page as string});
14. GlobalContext.getContext().setObject("newWant", undefined)
15. }
16. }
17. }
18. }

20. build() {
21. Column() {
22. Row() {
23. Text('singleton_first_title')
24. .fontSize(24)
25. .fontWeight(FontWeight.Bold)
26. .textAlign(TextAlign.Start)
27. .margin({ top: 12, bottom: 11, right: 24, left: 24 })
28. }
29. .width('100%')
30. .height(56)
31. .justifyContent(FlexAlign.Start)

33. Image('pic_empty')
34. .width(120)
35. .height(120)
36. .margin({ top: 224 })

38. Text('no_content')
39. .fontSize(14)
40. .margin({ top: 8, bottom: 317, right: 152, left: 152 })
41. .fontColor('text_color')
42. .opacity(0.4)
43. }
44. .width('100%')
45. .height('100%')
46. .backgroundColor('backGrounding')
47. }
48. }
```

当PageAbility的启动模式设置为多实例模式或为首次启动单例模式的PageAbility时（具体设置方法和典型场景示例见[PageAbility的启动模式](pageability-launch-type.md)），在调用方PageAbility中，通过Want中的parameters参数传递要启动的指定页面的pages信息，调用startAbility()方法启动PageAbility。被调用方可以在onCreate中使用featureAbility的getWant方法获取Want，再通过调用router.pushUrl实现启动指定页面。

调用方的页面中实现按钮点击触发startAbility方法启动目标端PageAbility，startAbility方法的入参Want中携带指定页面信息，示例代码如下：

```
1. import featureAbility from '@ohos.ability.featureAbility';
2. import Want from '@ohos.app.ability.Want';
3. import { BusinessError } from '@ohos.base';
4. import fs from '@ohos.file.fs';
5. import promptAction from '@ohos.promptAction';
6. import worker from '@ohos.worker';
7. import hilog from '@ohos.hilog';

9. const TAG: string = 'PagePageAbilityFirst';
10. const domain: number = 0xFF00;

12. @Entry
13. @Component
14. struct PagePageAbilityFirst {
15. build() {
16. Column() {
17. // ...
18. List({ initialIndex: 0 }) {
19. // ...
20. ListItem() {
21. Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
22. // ...
23. }
24. .onClick(() => {
25. let want: Want = {
26. bundleName: 'com.samples.famodelabilitydevelop',
27. abilityName: 'com.samples.famodelabilitydevelop.PageAbilityStandard',
28. parameters: { page: 'pages/first' }
29. };
30. featureAbility.startAbility({ want: want }).then((data) => {
31. hilog.info(domain, TAG, `startAbility finish:${data}`);
32. }).catch((err: BusinessError) => {
33. hilog.info(domain, TAG, `startAbility failed errcode:${err.code}`);
34. })
35. })
36. }
37. // ...
38. ListItem() {
39. Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
40. // ...
41. }
42. .onClick(() => {
43. let want: Want = {
44. bundleName: 'com.samples.famodelabilitydevelop',
45. abilityName: 'com.samples.famodelabilitydevelop.PageAbilityStandard',
46. parameters: { page: 'pages/second' }
47. };
48. featureAbility.startAbility({ want: want }).then((data) => {
49. hilog.info(domain, TAG, `startAbility finish:${data}`);
50. }).catch((err: BusinessError) => {
51. hilog.info(domain, TAG, `startAbility failed errcode:${err.code}`);
52. })
53. })
54. }
55. // ...
56. }
57. // ...
58. }
59. // ...
60. }
61. }
```

目标端PageAbility的onCreate生命周期回调中通过featureAbility的getWant方法获取Want，并对参数进行解析，实现指定页面拉起：

```
1. import featureAbility from '@ohos.ability.featureAbility';
2. import router from '@ohos.router';

4. class PageAbilityStandard {
5. onCreate() {
6. featureAbility.getWant().then((want) => {
7. if (want.parameters) {
8. if (want.parameters.page) {
9. router.pushUrl({ url: want.parameters.page as string });
10. }
11. }
12. })
13. }
14. }

16. export default new PageAbilityStandard();
```
