---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-prefetch-tool-class
title: 预加载工具类
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 调用预加载 > 添加预加载依赖类 > 预加载工具类
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d4dbb6a47638a75f74bb067abb497e3d5bdce963ef9afcf32f9f6e04cb7171e4
---

在“entry/src/main/ets/common”目录下新增GlobalContext.ets和PreferenceUtil.ets。

## GlobalContext

全局上下文类，提供全局上下文句柄的初始化和获取功能。参考示例如下：

```
1. import { common } from '@kit.AbilityKit';

3. export class GlobalContext {
4. private static context: common.UIAbilityContext;

6. public static initContext(context: common.UIAbilityContext): void {
7. GlobalContext.context = context;
8. }

10. public static getContext(): common.UIAbilityContext {
11. return GlobalContext.context;
12. }
13. }
```

## PreferenceUtil

首选项工具类，提供数据读取和存储功能。参考示例如下：

```
1. import dataPreferences from '@ohos.data.preferences';
2. import { Context } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;
6. const TAG = 'PreferenceUtil';
7. const DEFAULT_STORE_NAME: string = "prefetchDefaultStore";

9. export class PreferenceUtil {
10. private static cachedPreferences: Map<string, dataPreferences.Preferences> = new Map();

12. private constructor() {
13. }

15. public static async getValue(context: Context, storeName: string,
16. key: string): Promise<dataPreferences.ValueType | null> {
17. try {
18. let store = await PreferenceUtil.getStore(context, storeName);
19. PreferenceUtil.updateStoreCache(storeName, store);
20. const result = await store.get(key, '');
21. return result;
22. } catch (err) {
23. hilog.error(DOMAIN, TAG,
24. `getValue from ${storeName} error, key:${key}, err:${err.message}`);
25. return null;
26. }
27. }

29. public static getValueSync(context: Context, storeName: string, key: string): dataPreferences.ValueType | null {
30. try {
31. let store = PreferenceUtil.getStoreSync(context, storeName);
32. PreferenceUtil.updateStoreCache(storeName, store);
33. const result = store.getSync(key, '');
34. return result;
35. } catch (err) {
36. hilog.error(DOMAIN, TAG,
37. `getValueSync from ${storeName} error, key:${key}, err:${err.message}`);
38. return null;
39. }
40. }

42. public static async setValue(context: Context, storeName: string, key: string,
43. value: dataPreferences.ValueType): Promise<void> {
44. try {
45. let store = await PreferenceUtil.getStore(context, storeName);
46. PreferenceUtil.updateStoreCache(storeName, store);
47. await store.put(key, value);
48. await store.flush();
49. } catch (err) {
50. hilog.error(DOMAIN, TAG, `putValue from ${storeName} error, key:${key}, err:${err.message}`);
51. }
52. }

55. private static async getStore(context: Context, storeName: string): Promise<dataPreferences.Preferences> {
56. let actualStoreName = !storeName ? DEFAULT_STORE_NAME : storeName;
57. let store = PreferenceUtil.cachedPreferences.get(actualStoreName);
58. if (store) {
59. return store;
60. }
61. hilog.info(DOMAIN, TAG, `there is no cached store:${actualStoreName}, begin to get one`);
62. return dataPreferences.getPreferences(context, actualStoreName);
63. }

65. private static getStoreSync(context: Context, storeName: string): dataPreferences.Preferences {
66. let actualStoreName = !storeName ? DEFAULT_STORE_NAME : storeName;
67. let store = PreferenceUtil.cachedPreferences.get(actualStoreName);
68. if (store) {
69. return store;
70. }
71. hilog.info(DOMAIN, TAG, `getStoreSync there is no cached store:${actualStoreName}, begin to get one`);
72. return dataPreferences.getPreferencesSync(context, { name: actualStoreName });
73. }

75. private static updateStoreCache(storeName: string, store: dataPreferences.Preferences): void {
76. if (!PreferenceUtil.cachedPreferences.has(storeName)) {
77. PreferenceUtil.cachedPreferences.set(storeName, store);
78. }
79. }
80. }
```
