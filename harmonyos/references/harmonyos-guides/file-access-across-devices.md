---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/file-access-across-devices
title: 跨设备文件共享和访问
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 分布式文件系统 > 跨设备文件共享和访问
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:054282c2c1aee3a66fe74a37e5a3c847536d7a751f1f7cfe4d9c024cdc182f3f
---

分布式文件系统为应用提供了跨设备文件访问的能力，开发者在两个设备上安装同一应用时，通过[基础文件接口](app-file-access.md)，可跨设备读写另一个设备上该应用[分布式目录](app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)（/data/storage/el2/distributedfiles/）下的文件。例如：多设备数据流转的场景，设备组网互联之后，设备A上的应用可访问设备B上的同应用分布式目录下的文件，当期望应用文件被其他设备访问时，只需将文件移动到分布式目录即可。

注意

* [distributedfiles](app-sandbox-directory.md#应用文件目录与应用文件路径)目录为本应用在多设备间共享文件的合集。为避免误删其他设备生成的文件，应用在执行删除操作前，请务必确认操作是否符合预期。
* [/data/storage/el2/distributedfiles/.remote\_share/](app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)目录由系统自动创建并管理。开发者不得手动删除该目录下的文件。该目录中的文件与应用的base目录直接映射（不占用额外存储空间），任何删除操作可能导致base目录中的原始文件永久丢失。

## 开发步骤

1. 完成分布式组网。

   将需要跨设备访问的两个设备登录同一账号，保证设备蓝牙和Wi-Fi功能开启，蓝牙无需互连，Wi-Fi无需接入同一个局域网。
2. 授权分布式数据同步权限。

   分布式数据同步权限的授权方式为user\_grant，因此需要调用requestPermissionsFromUser接口，以动态弹窗的方式向用户申请授权。示例中的context的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

   ```
   1. import { common, abilityAccessCtrl } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```

   ```
   1. let atManager = abilityAccessCtrl.createAtManager();
   2. try {
   3. // 以动态弹窗的方式向用户申请授权
   4. atManager.requestPermissionsFromUser(context, ['ohos.permission.DISTRIBUTED_DATASYNC']).then((result) => {
   5. console.info(`request permission result: ${JSON.stringify(result)}`);
   6. }).catch((err: BusinessError) => {
   7. console.error(`Failed to request permissions from user. Code: ${err.code}, message: ${err.message}`);
   8. })
   9. } catch (error) {
   10. let err: BusinessError = error as BusinessError;
   11. console.error(`Catch err. Failed to request permissions from user. Code: ${err.code}, message: ${err.message}`);
   12. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/DistributedFileSample/entry/src/main/ets/pages/Index.ets#L55-L68)
3. 访问跨设备文件。

   同一应用不同设备之间实现跨设备文件访问，只需要将对应的文件放在应用沙箱的分布式目录即可。

   设备A上在分布式目录下创建测试文件，并写入内容。示例中的context的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

   ```
   1. import { fileIo } from '@kit.CoreFileKit';
   2. import { common } from '@kit.AbilityKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```

   ```
   1. let pathDir: string = context.distributedFilesDir;
   2. // 获取分布式目录的文件路径
   3. let filePath: string = pathDir + '/test.txt';

   5. try {
   6. // 在分布式目录下创建文件
   7. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   8. console.info('Succeeded in creating.');
   9. // 向文件中写入内容
   10. fileIo.writeSync(file.fd, 'content');
   11. // 关闭文件
   12. fileIo.closeSync(file.fd);
   13. } catch (error) {
   14. let err: BusinessError = error as BusinessError;
   15. console.error(`Failed to openSync / writeSync / closeSync. Code: ${err.code}, message: ${err.message}`);
   16. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/DistributedFileSample/entry/src/main/ets/pages/Index.ets#L33-L50)

   设备B主动向设备A发起建链，建链成功后设备B可在分布式目录下读取测试文件。

   说明

   这里通过分布式设备管理的接口获取设备networkId，详见[设备管理接口](../harmonyos-references/js-apis-distributeddevicemanager.md)。

   ```
   1. import { fileIo } from '@kit.CoreFileKit';
   2. import { common } from '@kit.AbilityKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { buffer } from '@kit.ArkTS';
   5. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
   ```

   ```
   1. // 通过分布式设备管理的接口获取设备A的networkId信息
   2. // ···
   3. let dmInstance = distributedDeviceManager.createDeviceManager('com.example.hap');
   4. let deviceInfoList: distributedDeviceManager.DeviceBasicInfo[] = dmInstance.getAvailableDeviceListSync();
   5. if (deviceInfoList && deviceInfoList.length > 0) {
   6. console.info(`Success to get available device list`);
   7. let networkId = deviceInfoList[0].networkId;
   8. // 定义访问公共文件目录的回调
   9. let listeners : fileIo.DfsListeners = {
   10. onStatus: (networkId: string, status: number): void => {
   11. console.info('Failed to access public directory');
   12. }
   13. };
   14. // 开始跨设备文件访问
   15. fileIo.connectDfs(networkId, listeners).then(() => {
   16. console.info('Success to connect dfs');
   17. let pathDir: string = context.distributedFilesDir;
   18. // 获取分布式目录的文件路径
   19. let filePath: string = pathDir + '/test.txt';
   20. try {
   21. // 打开分布式目录下的文件
   22. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
   23. // 定义接收读取数据的缓存
   24. let arrayBuffer = new ArrayBuffer(4096);
   25. // 读取文件的内容，返回值是读取到的字节个数
   26. class Option {
   27. public offset: number = 0;
   28. public length: number = 0;
   29. };
   30. let option = new Option();
   31. option.length = arrayBuffer.byteLength;
   32. let num = fileIo.readSync(file.fd, arrayBuffer, option);
   33. // 打印读取到的文件数据
   34. let buf = buffer.from(arrayBuffer, 0, num);
   35. console.info('read result: ' + buf.toString());
   36. fileIo.closeSync(file);
   37. } catch (error) {
   38. let err: BusinessError = error as BusinessError;
   39. console.error(`Failed to openSync / readSync. Code: ${err.code}, message: ${err.message}`);
   40. }
   41. }).catch((error: BusinessError) => {
   42. let err: BusinessError = error as BusinessError;
   43. console.error(`Failed to connect dfs. Code: ${err.code}, message: ${err.message}`);
   44. });
   45. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/DistributedFileSample/entry/src/main/ets/pages/Index.ets#L73-L121)
4. B设备访问跨设备文件完成，断开链路。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
   3. import { fileIo } from '@kit.CoreFileKit';
   ```

   ```
   1. // 获取设备A的networkId
   2. // ···
   3. let dmInstance = distributedDeviceManager.createDeviceManager('com.example.hap');
   4. let deviceInfoList: distributedDeviceManager.DeviceBasicInfo[] = dmInstance.getAvailableDeviceListSync();
   5. if (deviceInfoList && deviceInfoList.length > 0) {
   6. console.info(`Success to get available device list`);
   7. let networkId = deviceInfoList[0].networkId;
   8. // 关闭跨设备文件访问
   9. fileIo.disconnectDfs(networkId).then(() => {
   10. console.info(`Success to disconnect dfs`);
   11. }).catch((err: BusinessError) => {
   12. console.error(`Failed to disconnect dfs. Code: ${err.code}, message: ${err.message}`);
   13. })
   14. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/DistributedFileSample/entry/src/main/ets/pages/Index.ets#L128-L145)
