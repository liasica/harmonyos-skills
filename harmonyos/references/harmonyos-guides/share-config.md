---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-config
title: 应用间配置共享 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 跨应用数据共享 > 一对多跨应用数据共享 > 应用间配置共享 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:edd7ea92790f452eb9492132dbd47518964844421f7b4fd9a654e9422a1720e5
---

## 场景介绍

应用间配置共享通过集中管理公共配置信息，在不同应用间共享配置，提升协作效率。

从API version 20开始，支持应用间配置共享。

## 运作机制

应用间配置共享运作机制如下所示：

1. **配置发布方（即数据提供方）**：负责提供默认共享配置项，并能动态修改配置项信息。当前支持静态配置和动态配置两种配置方式。
   * **静态配置**：应用包在安装时提供的默认共享配置项（不依赖应用启动即生效）。
   * **动态配置**：配置发布方通过调用相关接口可以动态新增、删除或修改配置项（不依赖应用升级）。
2. **配置访问方（即数据访问方）**：可通过调用接口获取配置信息、或者监听/取消监听配置变化。

## 约束与限制

一个应用最多可以发布32个配置项，这个数量是静态配置与动态配置的总和。

## 接口说明

以下接口为应用间配置共享的相关接口。详细接口和说明，请参考[应用间配置共享接口](../harmonyos-references/js-apis-data-datashare.md#datasharecreatedataproxyhandle20)。

### 公共接口

| 接口名称 | 描述 |
| --- | --- |
| createDataProxyHandle(): Promise<DataProxyHandle> | 创建数据代理操作句柄，可用于订阅、发布、获取等操作。 |

### 配置发布方接口

| 接口名称 | 描述 |
| --- | --- |
| publish(data: ProxyData[], config: DataProxyConfig): Promise<DataProxyResult[]> | 发布或修改配置项。 |
| delete(uris: string[], config: DataProxyConfig): Promise<DataProxyResult[]> | 删除配置项。 |

### 配置访问方接口

| 接口名称 | 描述 |
| --- | --- |
| get(uris: string[], config: DataProxyConfig): Promise<DataProxyGetResult[]> | 获取配置项信息。 |
| on(event: 'dataChange', uris: string[], config: DataProxyConfig, callback: AsyncCallback<DataProxyChangeInfo[]>): DataProxyResult[] | 监听配置项变化。 |
| off(event: 'dataChange', uris: string[], config: DataProxyConfig, callback?: AsyncCallback<DataProxyChangeInfo[]>): DataProxyResult[] | 取消监听配置项变化。 |

## 配置发布方

### module.json5 配置

配置发布方需要配置module.json5文件中的crossAppSharedConfig字段，通过crossAppSharedConfig字段引用shared\_config.json文件，shared\_config.json为共享配置文件，定义了应用希望与其他应用共享的配置项。共享配置文件需放置在工程resources/base/profile目录下，并通过$资源访问方式引用。

```
1. {
2. "module":{
3. "crossAppSharedConfig": "$profile:shared_config"
4. }
5. }
```

共享配置文件shared\_config.json的文件名"shared\_config"可自定义，根节点名称为crossAppSharedConfig，为对象数组，标识当前共享配置项的数量。（一个应用最多可以发布32个配置项，这个数量是静态配置项与动态配置项的总和。静态配置项数量超过32时，只解析前32个符合crossAppSharedConfig字段配置说明要求的配置项，其余配置项不生效。）

crossAppSharedConfig字段配置说明：

| 属性名称 | 含义 | 数据类型 | 必填 |
| --- | --- | --- | --- |
| uri | 共享配置项的全局唯一标识。固定格式为"datashareproxy://{bundleName}/{path}"，其中bundleName为配置发布方应用的bundleName，path可随意填写，但同一应用内不允许重复。uri最大长度为256字节。 | 字符串 | 是 |
| value | 共享配置项的值，最大长度为4096字节。 | 字符串 | 是 |
| allowList | 允许访问该共享配置项的应用程序列表。数组最大长度为256，超过256的部分不生效。数组中每个元素为应用的[appIdentifier](common-problem-of-application.md#什么是appidentifier)，单个appIdentifier为只包含数字的字符串，最大长度为128字节，超过128字节的appIdentifier不会生效。可使用[getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口来获取当前应用的appIdentifier。 | 字符串数组 | 是 |

```
1. {
2. "crossAppSharedConfig": [
3. {
4. "uri": "datashareproxy://com.example.example/key1",
5. "value": "SHARED_CONFIG_DEMO1",
6. "allowList": ["6917573629901742292"]
7. },
8. {
9. "uri": "datashareproxy://com.example.example/key2",
10. "value": "SHARED_CONFIG_DEMO2",
11. "allowList": ["6917573298752100864", "6917573298752100864"]
12. }
13. ]
14. }
```

### 静态配置

应用包在安装时提供的默认共享配置项，即在应用安装过程中，预先定义并设置好的共享配置项，这些配置项不依赖应用的启动即可生效。

### 动态配置

可通过调用publish接口或delete接口，动态新增、删除或修改配置项。

* 通过调用publish接口发布或修改配置项。

  ```
  1. function publishSharedConfig() {
  2. dataShare.createDataProxyHandle().then((dataProxyHandle) => {
  3. const newConfigData: dataShare.ProxyData[] = [
  4. {
  5. uri: 'datashareproxy://com.samples.shareconfig/config1',
  6. value: 'Value1',
  7. allowList: [
  8. 'appIdentifier1',
  9. 'appIdentifier2'
  10. ]
  11. },
  12. {
  13. uri: 'datashareproxy://com.samples.shareconfig/config2',
  14. value: 'Value2',
  15. allowList: [
  16. 'appIdentifier3',
  17. 'appIdentifier4'
  18. ]
  19. }
  20. ];
  21. const config: dataShare.DataProxyConfig = {
  22. type: dataShare.DataProxyType.SHARED_CONFIG,
  23. };
  24. dataProxyHandle.publish(newConfigData, config).then((results: dataShare.DataProxyResult[]) => {
  25. results.forEach((result) => {
  26. console.info(`URI: ${result.uri}, Result: ${result.result}`);
  27. });
  28. }).catch((error: BusinessError) => {
  29. console.error('Error publishing config:', error);
  30. });
  31. }).catch((error: BusinessError) => {
  32. console.error('Error creating DataProxyHandle:', error);
  33. });
  34. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/DataShare/ShareConfig/entry/src/main/ets/pages/Index.ets#L19-L55)
* 通过调用delete接口删除配置项。

  ```
  1. function deleteSharedConfig() {
  2. dataShare.createDataProxyHandle().then((dataProxyHandle) => {
  3. const urisToDelete: string[] = [
  4. 'datashareproxy://com.samples.shareconfig/config1',
  5. 'datashareproxy://com.samples.shareconfig/config2'
  6. ];
  7. const config: dataShare.DataProxyConfig = {
  8. type: dataShare.DataProxyType.SHARED_CONFIG,
  9. };
  10. dataProxyHandle.delete(urisToDelete, config).then((results: dataShare.DataProxyResult[]) => {
  11. results.forEach((result) => {
  12. console.info(`URI: ${result.uri}, Result: ${result.result}`);
  13. });
  14. }).catch((error: BusinessError) => {
  15. console.error('Error deleting config:', error);
  16. });
  17. }).catch((error: BusinessError) => {
  18. console.error('Error creating DataProxyHandle:', error);
  19. });
  20. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/DataShare/ShareConfig/entry/src/main/ets/pages/Index.ets#L57-L79)

## 配置访问方

配置访问方可以通过调用get、on或off接口来获取配置信息或监听/取消监听配置变化。

### 获取配置项信息

使用get接口获取配置信息。

```
1. function getSharedConfig() {
2. dataShare.createDataProxyHandle().then((dataProxyHandle) => {
3. const urisToGet: string[] = [
4. 'datashareproxy://com.samples.shareconfig/config1',
5. 'datashareproxy://com.samples.shareconfig/config2'
6. ];
7. const config: dataShare.DataProxyConfig = {
8. type: dataShare.DataProxyType.SHARED_CONFIG,
9. };
10. dataProxyHandle.get(urisToGet, config).then((results: dataShare.DataProxyGetResult[]) => {
11. results.forEach((result) => {
12. console.info(`URI: ${result.uri}, Result: ${result.result}, AllowList: ${result.allowList}`);
13. });
14. }).catch((error: BusinessError) => {
15. console.error('Error getting config:', error);
16. });
17. }).catch((error: BusinessError) => {
18. console.error('Error creating DataProxyHandle:', error);
19. });
20. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/DataShare/ShareConfig/entry/src/main/ets/pages/Index.ets#L81-L103)

### 监听/取消监听配置变化

使用on接口监听配置变化，使用off接口取消监听配置变化。

```
1. function watchConfigChanges() {
2. dataShare.createDataProxyHandle().then((dsProxyHelper) => {
3. const uris: string[] = [
4. 'datashareproxy://com.samples.shareconfig/config1',
5. 'datashareproxy://com.samples.shareconfig/config2'
6. ];
7. const config: dataShare.DataProxyConfig = {
8. type: dataShare.DataProxyType.SHARED_CONFIG,
9. };
10. const callback = (err: BusinessError<void>, changes: dataShare.DataProxyChangeInfo[]): void => {
11. if (err) {
12. console.error('err:', err);
13. } else {
14. changes.forEach((change) => {
15. console.info(`Change Type: ${change.type}, URI: ${change.uri}, Value: ${change.value}`);
16. });
17. }
18. };
19. // 监听配置变化
20. const listenResults: dataShare.DataProxyResult[] = dsProxyHelper.on('dataChange', uris, config, callback);
21. listenResults.forEach((result) => {
22. console.info(`URI: ${result.uri}, Result: ${result.result}`);
23. });
24. // 取消监听配置变化
25. const unListenResults: dataShare.DataProxyResult[] = dsProxyHelper.off('dataChange', uris, config, callback);
26. unListenResults.forEach((result) => {
27. console.info(`URI: ${result.uri}, Result: ${result.result}`);
28. });
29. }).catch((error: BusinessError) => {
30. console.error('Error creating DataProxyHandle:', error);
31. });
32. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/DataShare/ShareConfig/entry/src/main/ets/pages/Index.ets#L105-L139)
