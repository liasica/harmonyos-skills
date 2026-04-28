---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-230
title: Component如何监听应用前后台切换
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Component如何监听应用前后台切换
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6801236862db540528b4f6f5fb15ef14922cfc96c1aa5b1d086d66b902551768
---

应用的前后台生命周期与页面和组件无关，组件仅能感知aboutToAppear和aboutToDisappear事件。若组件需要感知应用的前后台切换，可以使用[ApplicationContext.on('applicationStateChange')](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextonapplicationstatechange10)注册对当前应用前后台状态变化的监听。也可以设置一个应用前后台状态的变量。在UIAbility中对应的生命周期函数中更改此变量，并在组件中监听AppStorage状态变量的变化，执行相应的逻辑。

参考代码如下：

```
1. // EntryAbility中
2. export default class EntryAbility extends UIAbility {
3. onWindowStageCreate(windowStage: window.WindowStage): void {
4. AppStorage.setOrCreate<boolean>('isOnForeground', undefined);
5. }

7. onForeground(): void {
8. AppStorage.set<boolean>('isOnForeground', true);
9. }

11. onBackground(): void {
12. AppStorage.set<boolean>('isOnForeground', false);
13. }
14. }
```

[EntryAbilityMonitorTheFrontAndBack.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityMonitorTheFrontAndBack.ets#L27-L40)

```
1. @Entry
2. @Component
3. struct ComponentListenFrontAndBack {
4. @State message: string = 'Hello World';
5. @StorageLink('isOnForeground') isOnForeground: boolean = true;

7. build() {
8. Row() {
9. Column() {
10. Text(this.message)
11. .fontSize(50)
12. .fontWeight(FontWeight.Bold)
13. ForegroundAwareComponent({ isOnForeground: this.isOnForeground })
14. }
15. .width('100%')
16. }
17. .height('100%')
18. }
19. }

21. @Component
22. struct ForegroundAwareComponent {
23. @Watch('change') @Link isOnForeground: boolean;
24. @State message: string = 'video';

26. build() {
27. Text('message')
28. .fontSize(50)
29. .fontWeight(FontWeight.Bold)
30. .onClick(() => {
31. this.message += this.isOnForeground;
32. console.info('' + this.isOnForeground);
33. })
34. }

36. change() {
37. if (this.isOnForeground) {
38. console.info('The component is on foreground.');
39. } else {
40. console.info('The component is on background.');
41. }
42. }
43. }
```

[MonitorFrontAndBackOfApplication.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/MonitorFrontAndBackOfApplication.ets#L21-L64)
