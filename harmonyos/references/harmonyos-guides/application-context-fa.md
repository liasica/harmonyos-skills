---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-fa
title: FA模型的Context
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > FA模型的Context
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:beae8e1db4302cc06d4266458eb4ef886718e8b297a6f5adbbab3434d399a302
---

[FA模型](ability-terminology.md#fa模型)下只有一个Context。Context中的所有功能都是通过方法来提供的，它提供了一些featureAbility中不存在的方法，相当于featureAbility的一个扩展和补全。

## 接口说明

FA模型下使用Context，需要通过featureAbility下的接口getContext来获取，而在此之前，需要先导入对应的包：

```
1. import featureAbility from '@ohos.ability.featureAbility';
```

然后使用如下方式获取对应的Context对象：

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context = featureAbility.getContext();
```

最终返回的对象为Context，其对应的接口说明请参见[接口文档](../harmonyos-references/js-apis-inner-app-context.md)。

## 开发步骤

1. 查询Bundle信息。

   ```
   1. import featureAbility from '@ohos.ability.featureAbility';
   2. import hilog from '@ohos.hilog';

   4. const TAG: string = 'MainAbility';
   5. const domain: number = 0xFF00;

   7. class MainAbility {
   8. onCreate() {
   9. // 获取context并调用相关方法
   10. let context = featureAbility.getContext();
   11. context.getBundleName((data, bundleName) => {
   12. hilog.info(domain, TAG, 'ability bundleName:' + bundleName);
   13. });
   14. hilog.info(domain, TAG, 'Application onCreate');
   15. }
   16. }

   18. export default new MainAbility();
   ```
2. 设置当前featureAbility的显示方向。

   ```
   1. import featureAbility from '@ohos.ability.featureAbility';
   2. import bundle from '@ohos.bundle';
   3. import hilog from '@ohos.hilog';

   5. const TAG: string = 'PageAbilitySingleton';
   6. const domain: number = 0xFF00;

   8. class PageAbilitySingleton {
   9. onCreate() {
   10. // 获取context并调用相关方法
   11. let context = featureAbility.getContext();
   12. context.setDisplayOrientation(bundle.DisplayOrientation.PORTRAIT).then(() => {
   13. hilog.info(domain, TAG, 'Set display orientation.');
   14. })
   15. hilog.info(domain, TAG, 'Application onCreate');
   16. }

   18. onDestroy() {
   19. hilog.info(domain, TAG, 'Application onDestroy');
   20. }
   21. }

   23. export default new PageAbilitySingleton();
   ```
