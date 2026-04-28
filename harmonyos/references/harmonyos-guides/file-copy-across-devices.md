---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/file-copy-across-devices
title: 跨设备文件拷贝
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 分布式文件系统 > 跨设备文件拷贝
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bb5c8ab469762caf03daa55ce8818afefceba6a6e4b49bd3dd408e6fc96d16e4
---

分布式文件系统为应用提供了跨设备文件拷贝的能力，开发者可以通过[基础文件接口](../harmonyos-references/js-apis-file-fs.md)进行跨设备拷贝文件。例如：多设备数据流转的场景，设备组网互联之后，设备A上的应用可将沙箱文件拷贝到设备A的分布式目录下。设备B在粘贴时，从B设备的分布式目录下将文件拷贝到对应的沙箱文件中。

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
3. 执行跨设备文件拷贝操作。

   同一应用在不同设备之间实现跨设备文件拷贝，只需要将对应的文件放在应用沙箱的分布式目录即可。

   将A设备的待拷贝沙箱文件拷贝到A设备的分布式目录下。

   ```
   1. import { fileIo } from '@kit.CoreFileKit';
   2. import { common } from '@kit.AbilityKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { fileUri } from '@kit.CoreFileKit';
   ```

   ```
   1. let pathDir: string = context.filesDir;
   2. let distributedPathDir: string = context.distributedFilesDir;
   3. // 待拷贝文件沙箱路径
   4. let filePath: string = pathDir + '/src.txt';
   5. try {
   6. // 准备待拷贝沙箱文件
   7. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
   8. fileIo.writeSync(file.fd, 'Create file success');
   9. fileIo.closeSync(file);
   10. } catch (error) {
   11. console.error(`Failed to createFile. Code: ${error.code}, message: ${error.message}`);
   12. }

   14. // 获取待拷贝源文件uri
   15. let srcUri = fileUri.getUriFromPath(filePath);
   16. // 获取目标路径(分布式目录)的uri
   17. let destUri: string = fileUri.getUriFromPath(distributedPathDir + '/src.txt');
   18. try {
   19. // 将沙箱路径下的源文件拷贝到目标分布式目录下
   20. fileIo.copy(srcUri, destUri).then(()=>{
   21. console.info(`Succeeded in copying---. `);
   22. console.info(`src: ${srcUri} dest: ${destUri}`);
   23. }).catch((error: BusinessError)=>{
   24. let err: BusinessError = error as BusinessError;
   25. console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
   26. })
   27. } catch (error) {
   28. console.error(`Catch err. Failed to copy. Code: ${error.code}, message: ${error.message}`);
   29. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/DistributedFileSample/entry/src/main/ets/pages/Index.ets#L150-L180)

   B设备在获取A设备沙箱文件时，从B设备的分布式目录下将对应的文件拷贝走，以此完成跨设备拷贝。

   ```
   1. import { fileIo } from '@kit.CoreFileKit';
   2. import { common } from '@kit.AbilityKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { fileUri } from '@kit.CoreFileKit';
   5. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
   ```

   ```
   1. // ···
   2. let pathDir: string = context.filesDir;
   3. let distributedPathDir: string = context.distributedFilesDir;
   4. // 待拷贝文件的目标路径(沙箱路径)
   5. let destPath: string = pathDir + '/dest.txt';
   6. // 获取目标路径uri
   7. let destUri = fileUri.getUriFromPath(destPath);

   9. // 拷贝源文件路径(分布式目录)
   10. let srcPath = distributedPathDir + '/src.txt';
   11. // 获取源路径uri
   12. let srcUri: string = fileUri.getUriFromPath(srcPath);

   14. // 定义拷贝回调
   15. let progressListener: fileIo.ProgressListener = (progress: fileIo.Progress) => {
   16. console.info(`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
   17. };
   18. let options: fileIo.CopyOptions = {
   19. 'progressListener' : progressListener
   20. };
   21. // 通过分布式设备管理的接口获取设备A的networkId信息
   22. let dmInstance = distributedDeviceManager.createDeviceManager('com.example.hap');
   23. let deviceInfoList: distributedDeviceManager.DeviceBasicInfo[] = dmInstance.getAvailableDeviceListSync();
   24. if (deviceInfoList && deviceInfoList.length > 0) {
   25. console.info(`success to get available device list`);
   26. let networkId = deviceInfoList[0].networkId; // 这里只是两个设备连接，列表中首个即为A设备的networkId
   27. // 定义访问分布式目录的回调
   28. let listeners : fileIo.DfsListeners = {
   29. onStatus: (networkId: string, status: number): void => {
   30. console.error(`Failed to access public directory，${status}`);
   31. }
   32. };
   33. // 开始跨设备文件拷贝
   34. fileIo.connectDfs(networkId, listeners).then(()=>{
   35. try {
   36. // 将分布式目录下的文件拷贝到其他沙箱路径下
   37. fileIo.copy(srcUri, destUri, options).then(()=>{
   38. console.info(`Succeeded in copying from distributed path`);
   39. console.info(`src: ${srcUri} dest: ${destUri}`);
   40. fileIo.unlinkSync(srcPath); // 拷贝完成后清理分布式目录下的临时文件
   41. }).catch((error: BusinessError)=>{
   42. let err: BusinessError = error as BusinessError;
   43. console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
   44. })
   45. } catch (error) {
   46. console.error(`Catch err. Failed to copy. Code: ${error.code}, message: ${error.message}`);
   47. }
   48. }).catch((error: BusinessError) => {
   49. let err: BusinessError = error as BusinessError;
   50. console.error(`Failed to connect dfs. Code: ${err.code}, message: ${err.message}`);
   51. });
   52. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/DistributedFileSample/entry/src/main/ets/pages/Index.ets#L185-L240)
4. 跨设备文件拷贝完成，断开链路。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { distributedDeviceManager } from '@kit.DistributedServiceKit'
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
