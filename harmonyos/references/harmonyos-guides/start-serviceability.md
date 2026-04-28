---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-serviceability
title: 启动ServiceAbility
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > ServiceAbility组件开发指导 > 启动ServiceAbility
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:260e71d94c2ca6bd75525f2d8b8c622dc979991b0994c34ae29af40d08290eca
---

ServiceAbility的启动与其他Ability并无区别，应用开发者可以在PageAbility中通过featureAbility的startAbility接口拉起ServiceAbility，在ServiceAbility中通过particleAbility的startAbility接口拉起ServiceAbility。ServiceAbility的启动规则详见[FA模型组件启动规则](component-startup-rules-fa.md)章节。

如下示例展示了在PageAbility中通过startAbility启动bundleName为"com.example.myapplication"，abilityName为"ServiceAbility"的ServiceAbility的方法。启动[FA模型](ability-terminology.md#fa模型)的ServiceAbility时，需要在abilityName前拼接bundleName字符串。

```
1. import featureAbility from '@ohos.ability.featureAbility';
2. import Want from '@ohos.app.ability.Want';
3. import promptAction from '@ohos.promptAction';
4. import hilog from '@ohos.hilog';

6. const TAG: string = 'PageServiceAbility';
7. const domain: number = 0xFF00;

9. @Entry
10. @Component
11. struct PageServiceAbility {
12. async startServiceAbility(): Promise<void> {
13. try {
14. hilog.info(domain, TAG, 'Begin to start ability');
15. let want: Want = {
16. bundleName: 'com.samples.famodelabilitydevelop',
17. abilityName: 'com.samples.famodelabilitydevelop.ServiceAbility'
18. };
19. await featureAbility.startAbility({ want });
20. promptAction.showToast({
21. message: 'start_service_success_toast'
22. });
23. hilog.info(domain, TAG, `Start ability succeed`);
24. } catch (error) {
25. hilog.error(domain, TAG, 'Start ability failed with ' + error);
26. }
27. }
28. build() {
29. // ...
30. }
31. }
```

执行上述代码后，Ability将通过[startAbility()](../harmonyos-references/js-apis-ability-featureability.md#featureabilitystartability)方法来启动ServiceAbility。

* 如果ServiceAbility尚未运行，则系统会先调用onStart()来初始化ServiceAbility，再回调Service的onCommand()方法来启动ServiceAbility。
* 如果ServiceAbility正在运行，则系统会直接回调ServiceAbility的onCommand()方法来启动ServiceAbility。
