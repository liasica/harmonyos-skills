---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-pageability
title: 创建PageAbility
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > PageAbility组件开发指导 > 创建PageAbility
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c93ef4299e17ad2e5210315d4a6a73295d738a56e4d4a95c9fc5027448e057d2
---

通过DevEco Studio开发平台创建PageAbility时，DevEco Studio会在app.js/app.ets中默认生成onCreate()和onDestroy()方法，其他方法需要开发者自行实现。接口说明参见[PageAbility的生命周期](pageability-lifecycle.md)，创建PageAbility示例如下：

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
12. hilog.info(domain, TAG, 'ability bundleName:' ,bundleName);
13. });
14. hilog.info(domain, TAG, 'Application onCreate');
15. }

17. onDestroy() {
18. hilog.info(domain, TAG, 'Application onDestroy');
19. }

21. onShow(): void {
22. hilog.info(domain, TAG, 'Application onShow');
23. }

25. onHide(): void {
26. hilog.info(domain, TAG, 'Application onHide');
27. }

29. onActive(): void {
30. hilog.info(domain, TAG, 'Application onActive');
31. }

33. onInactive(): void {
34. hilog.info(domain, TAG, 'Application onInactive');
35. }

37. onNewWant() {
38. hilog.info(domain, TAG, 'Application onNewWant');
39. }
40. }

42. export default new MainAbility();
```

PageAbility创建成功后，其abilities相关的配置项在config.json中体现，一个名字为EntryAbility的config.json配置文件示例如下：

```
1. {
2. "module": {
3. "abilities": [
4. {
5. "skills": [
6. {
7. "entities": [
8. "entity.system.home"
9. ],
10. "actions": [
11. "action.system.home"
12. ]
13. }
14. ],
15. "orientation": "unspecified",
16. "formsEnabled": false,
17. "name": ".MainAbility",
18. "srcLanguage": "ets",
19. "srcPath": "MainAbility",
20. "icon": "$media:icon",
21. "description": "$string:MainAbility_desc",
22. "label": "$string:MainAbility_label",
23. "type": "page",
24. "visible": true,
25. "launchType": "singleton"
26. },
27. ]
28. }
29. }
```

[FA模型](ability-terminology.md#fa模型)中，可以通过featureAbility的getContext接口获取应用上下文，进而使用上下文提供的能力。

**表1** featureAbility接口说明

| 接口名 | 接口描述 |
| --- | --- |
| getContext() | 获取应用上下文。 |

通过getContext获取应用上下文并获取分布式目录的示例如下：

```
1. import featureAbility from '@ohos.ability.featureAbility';
2. import fileIo from '@ohos.file.fs';
3. import promptAction from '@ohos.promptAction';
4. import hilog from '@ohos.hilog';

6. const TAG: string = 'PagePageAbilityFirst';
7. const domain: number = 0xFF00;
```

```
1. (async (): Promise<void> => {
2. let dir: string;
3. try {
4. hilog.info(domain, TAG, 'Begin to getOrCreateDistributedDir');
5. dir = await featureAbility.getContext().getOrCreateDistributedDir();
6. promptAction.showToast({
7. message: dir
8. });
9. hilog.info(domain, TAG, 'distribute dir is ' + dir);
10. let fd: number;
11. let path = dir + '/a.txt';
12. fd = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE).fd;
13. fileIo.close(fd);
14. } catch (error) {
15. hilog.error(domain, TAG, 'getOrCreateDistributedDir failed with : ' + error);
16. }
17. })()
```
