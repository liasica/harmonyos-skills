---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/stop-pageability
title: 停止PageAbility
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > PageAbility组件开发指导 > 停止PageAbility
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:57+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:73feebdae6189e9b902afd19f70e8b9bf7a07b332a12e3f26f861f4ec306e308
---

停止PageAbility通过featureAbility中的terminateSelf接口实现。

**表1** featureAbility接口说明

| 接口名 | 接口描述 |
| --- | --- |
| terminateSelf() | 停止Ability。 |
| terminateSelfWithResult(parameter: AbilityResult) | 设置该PageAbility停止时返回给调用者的结果及数据并停止Ability。 |

如下示例展示了停止Ability的方法。

```
1. import featureAbility from '@ohos.ability.featureAbility';
2. import hilog from '@ohos.hilog';

4. const TAG: string = 'PagePageAbilityFirst';
5. const domain: number = 0xFF00;
```

```
1. // ...
2. (async (): Promise<void> => {
3. try {
4. hilog.info(domain, TAG, 'Begin to terminateSelf');
5. await featureAbility.terminateSelf();
6. hilog.info(domain, TAG, 'terminateSelf succeed');
7. } catch (error) {
8. hilog.error(domain, TAG, 'terminateSelf failed with ' + error);
9. }
10. })()
11. // ...
```
