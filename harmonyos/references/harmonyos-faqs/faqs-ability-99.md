---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-99
title: 如何判断App的启动来源
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何判断App的启动来源
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a8154f1c903fc1ddf2cf3739e00c2d579d5ac2e46bb2284240fbd6fe5a878ccf
---

通过startAbility()启动应用时，want参数中的parameters属性可以携带拉起方的信息。系统在parameters中提供了一些预置的key，例如，可以通过ohos.aafwk.param.callerBundleName获取拉起方的BundleName。

示例如下：

拉起端：

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Entry
6. @Component
7. struct Index {
8. context = this.getUIContext();

10. build() {
11. Row() {
12. Column() {
13. Button('open app')
14. .onClick(() => {
15. let want: Want = {
16. action: 'ohos.want.action.viewData',
17. entities: ['entity.system.home']
18. }
19. let context = this.context.getHostContext() as common.UIAbilityContext;
20. context.startAbility(want, (err: BusinessError) => {
21. if (err.code) {
22. // 处理业务逻辑错误
23. hilog.error(0x0000, 'testTag', `startAbility failed, code is ${err.code}, message is ${err.message}`);
24. return;
25. }
26. // 执行正常业务
27. hilog.info(0x0000, 'testTag', 'startAbility succeed');
28. });
29. })
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```

[SourceAppLaunch.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/SourceAppLaunch.ets#L21-L55)

接收端：

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. hilog.info(0x0000, 'testTag', `app resource is:${want.parameters?.['ohos.aafwk.param.callerBundleName']}`);
7. // ...
8. }

10. // ...
11. }
```

[EntryAbilitySouce.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/entryability/EntryAbilitySouce.ets#L6-L16)

**参考链接**

[Want](../harmonyos-references/js-apis-app-ability-want.md#want)
