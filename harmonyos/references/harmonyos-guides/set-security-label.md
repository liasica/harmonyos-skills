---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/set-security-label
title: 设置分布式文件数据等级
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 分布式文件系统 > 设置分布式文件数据等级
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:19+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:4a2575e70c4345d4d087f3102cd0dcf8963456ac5d32af8f24d01c9d28f10412
---

不同设备本身的安全能力差异较大，一些小的嵌入式设备安全能力远弱于平板等设备类型。用户或者应用不同的文件数据有不同安全诉求，例如个人的健康信息和银行卡信息等不期望被弱设备读取。因此，HarmonyOS提供一套完整的数据分级、设备分级标准，并针对不同设备制定不同的数据流转策略，具体规则请参见[数据、设备安全分级](access-control-by-device-and-data-level.md)。

## 接口说明

API详细介绍请参见[ohos.file.securityLabel](../harmonyos-references/js-apis-file-securitylabel.md)。

**表1** 设置文件数据等级，其中“√”表示支持。

| 接口名 | 功能 | 接口类型 | 支持同步 | 支持异步 |
| --- | --- | --- | --- | --- |
| setSecurityLabel | 设置文件安全标签。 | 方法 | √ | √ |
| getSecurityLabel | 获取文件安全标签。 | 方法 | √ | √ |

注意

1. 对于不满足安全等级的文件，跨设备仍然可以看到该文件，但是无权限打开访问该文件。
2. 分布式文件系统的数据等级默认为S3，应用可以主动设置文件的安全等级。

## 开发示例

获取通用文件沙箱路径，并设置数据等级标签。示例中的context的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

```
1. import { securityLabel } from '@kit.CoreFileKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';
4. import { fileIo } from '@kit.CoreFileKit';
```

```
1. // 获取需要设备数据等级的文件沙箱路径，请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
2. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
3. let pathDir = context.filesDir;
4. let filePath = pathDir + '/test.txt';

6. // 打开文件
7. let file: fileIo.File | null = null;
8. try {
9. file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
10. // 设置文件的数据等级为s0
11. securityLabel.setSecurityLabel(filePath, 's0').then(() => {
12. console.info('Succeeded in setting security label.');
13. fileIo.closeSync(file);
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to set security label. Code: ${err.code}, message: ${err.message}`);
16. if (file) {
17. try {
18. fileIo.closeSync(file);
19. } catch (closeErr) {
20. console.error(`Failed to close file`);
21. }
22. }
23. });
24. } catch (err) {
25. console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}`);
26. if (file) {
27. try {
28. fileIo.closeSync(file);
29. } catch (closeErr) {
30. console.error(`Failed to close file`);
31. }
32. }
33. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/FileApiFileSample/entry/src/main/ets/pages/Index.ets#L264-L279)
