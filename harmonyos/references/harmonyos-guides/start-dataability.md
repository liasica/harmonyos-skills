---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-dataability
title: 启动DataAbility
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > DataAbility组件开发指导 > 启动DataAbility
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:aabaaec42fa9cbc9d1596b8f3cb4b77d3ffe345bd00276a7b81dd489d8663f7e
---

启动DataAbility会获取一个工具接口类对象（DataAbilityHelper）。启动DataAbility的示例代码如下：

```
1. import featureAbility from '@ohos.ability.featureAbility';
2. import ability from '@ohos.ability.ability';

4. let uri: string = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
5. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(uri);
```
