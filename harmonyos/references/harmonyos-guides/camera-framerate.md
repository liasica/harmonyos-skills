---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-framerate
title: 动态调整预览帧率(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 动态调整预览帧率(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ffdce7099ebf0f91441b88345950d69ca034e84dbecda76bd163a9489a0f2f8b
---

动态调整帧率是直播、视频等场景下控制预览效果的重要能力之一。应用可通过此能力，显式地控制流输出帧率，以适应不同帧率下的业务目标。

某些场景下降低帧率可在相机设备启用时降低功耗。

## 约束与限制

支持的帧率范围及帧率的设置依赖于硬件能力的实现，不同的硬件平台可能拥有不同的默认帧率。

## 开发流程

相机使用预览功能前，均需要创建相机会话。完成会话配置后，应用提交和开启会话，才可以开始调用相机相关功能。

流程图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/RVoJs3E3QIm5OeDWPeLLwQ/zh-cn_image_0000002583438627.png?HW-CC-KV=V1&HW-CC-Date=20260427T234603Z&HW-CC-Expire=86400&HW-CC-Sign=F8878D1CCFDEDD4769BDF2786F22AD60BF557623B7BA41EF69DEDD9A0DA642ED)

与普通的[预览](camera-preview.md)流程相比，动态调整预览帧率的注意点如图上标识：

1. 调用[createSession](../harmonyos-references/arkts-apis-camera-cameramanager.md#createsession11)创建会话（Session）时，需要指定模式为NORMAL\_PHOTO或NORMAL\_VIDEO。

   仅当Session处于NORMAL\_PHOTO或NORMAL\_VIDEO模式时，支持调整预览流帧率。调整帧率的创建会话方式见[创建Session会话并指定模式](camera-framerate.md#创建session会话并指定模式)。
2. [动态调整帧率](camera-framerate.md#调整帧率)的操作，可在启动预览前后任意时刻调用。
3. [动态调整帧率](camera-framerate.md#调整帧率)在预览里属于可选操作，可以完成：

   * 查询当前支持调整的帧率范围
   * 设置当前帧率
   * 获取当前生效的帧率设置

如何配置会话（Session）、释放资源，请参考[会话管理](camera-session-management.md) > [预览](camera-preview.md)，或是[完整流程](camera-framerate.md#完整流程)示例。

## 导入依赖

导入camera接口，接口中提供了相机相关的属性和方法，导入方法如下。

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

## 创建Session会话并指定模式

相机使用预览等功能前，均需完成[相机管理](camera-device-management.md)和创建相机会话，调用[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)的[createSession](../harmonyos-references/arkts-apis-camera-cameramanager.md#createsession11)创建一个会话。

创建会话时需指定[SceneMode](../harmonyos-references/arkts-apis-camera-e.md#scenemode11)为NORMAL\_PHOTO或NORMAL\_VIDEO，创建出的Session处于拍照或录像模式。

以创建Session会话并指定为NORMAL\_PHOTO模式为例：

```
1. function createPhotoSession(cameraManager: camera.CameraManager): camera.Session | undefined {
2. let session: camera.Session | undefined = undefined;
3. try {
4. // 创建Session会话并指定为NORMAL_PHOTO模式
5. session = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
6. } catch (error) {
7. let err = error as BusinessError;
8. console.error(`Failed to create the session instance. error: ${err}`);
9. }
10. return session;
11. }
```

## 调整帧率

1. 调用[PreviewOutput](../harmonyos-references/arkts-apis-camera-previewoutput.md)的[getSupportedFrameRates](../harmonyos-references/arkts-apis-camera-previewoutput.md#getsupportedframerates12)，查询当前支持的帧率范围。

   说明

   需要在Session调用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)完成配流之后调用。

   ```
   1. function getSupportedFrameRange(previewOutput: camera.PreviewOutput): Array<camera.FrameRateRange> {
   2. // 获取支持的帧率范围，不同的硬件平台可能提供不同的帧率范围
   3. return previewOutput.getSupportedFrameRates();
   4. }
   ```
2. 根据实际开发需求，调用[PreviewOutput](../harmonyos-references/arkts-apis-camera-previewoutput.md)类提供的[setFrameRate](../harmonyos-references/arkts-apis-camera-previewoutput.md#setframerate12)接口对帧率进行动态调整。

   说明

   **调用时机：**

   * 需要在Session调用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)完成配流之后调用。
   * 可在Session调用[start](../harmonyos-references/arkts-apis-camera-session.md#start11)启动预览前后任意时刻调用。

   **setFrameRate调用限制：**

   * 在调用setFrameRate接口设置非固定帧率后，不支持再次调用该接口重新设置动态帧率。
   * 在调用setFrameRate接口设置固定帧率后，支持重新设置固定帧率，但必须保证新设置的帧率可以整除之前设置的帧率或者被之前设置的帧率整除。

   ```
   1. function setFrameRate(previewOutput: camera.PreviewOutput, minFps: number, maxFps: number): void {
   2. try {
   3. previewOutput.setFrameRate(minFps, maxFps);
   4. } catch (error) {
   5. let err = error as BusinessError;
   6. console.error(`Failed to setFrameRate for previewOutput. error: ${err}`);
   7. }
   8. }
   ```
3. （可选）通过[PreviewOutput](../harmonyos-references/arkts-apis-camera-previewoutput.md)提供的[getActiveFrameRate](../harmonyos-references/arkts-apis-camera-previewoutput.md#getactiveframerate12)接口查询已设置过并生效的帧率。

   仅通过[setFrameRate](../harmonyos-references/arkts-apis-camera-previewoutput.md#setframerate12)接口显式设置过帧率才可查询当前生效帧率信息。

   ```
   1. function getActiveFrameRange(previewOutput: camera.PreviewOutput): camera.FrameRateRange {
   2. return previewOutput.getActiveFrameRate();
   3. }
   ```

## 完整流程

结合上述开发流程1~3，完整的session配流及previewOutput在session.start前后调整帧率示例代码如下。

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function sessionConfig(cameraManager: camera.CameraManager, cameraInput: camera.CameraInput,
5. previewOutput: camera.PreviewOutput): Promise<void> {
6. try {
7. let session: camera.Session | undefined = undefined;
8. // 创建CaptureSession实例
9. session = createPhotoSession(cameraManager);
10. if (session === undefined) {
11. return;
12. }
13. // 开始配置会话
14. session.beginConfig();
15. // 把CameraInput加入到会话
16. session.addInput(cameraInput);
17. // 把previewOutput加入到会话
18. session.addOutput(previewOutput);
19. // 提交配置信息
20. await session.commitConfig();
21. // 获取当前支持的帧率范围
22. let supportFrameRateArray: Array<camera.FrameRateRange> = getSupportedFrameRange(previewOutput);

24. console.info(`frame rate supported by previewOutput: ${JSON.stringify(supportFrameRateArray)}`);
25. // 可在start前对帧率进行设置
26. if (supportFrameRateArray.length !== 0) {
27. // 将帧率设置为第一组帧率范围的最大值
28. setFrameRate(previewOutput, supportFrameRateArray[0].max, supportFrameRateArray[0].max);
29. }
30. // 获取当前生效的帧率设置
31. let activeFrameRateArray: camera.FrameRateRange = getActiveFrameRange(previewOutput);
32. console.info(`current effective frame rate for this previewOutput: ${activeFrameRateArray}`);
33. // 开始会话工作并启动预览
34. await session.start();
35. // 可在start后对帧率进行设置
36. if (supportFrameRateArray.length !== 0) {
37. // 可将帧率设置为最大值的一半（能否设置成功取决于平台是否支持）
38. setFrameRate(previewOutput, supportFrameRateArray[0].max / 2, supportFrameRateArray[0].max / 2);
39. }
40. // 获取当前生效的帧率设置
41. activeFrameRateArray = getActiveFrameRange(previewOutput);
42. console.info(`current effective frame rate for this previewOutput: ${activeFrameRateArray}`);
43. } catch (error) {
44. let err = error as BusinessError;
45. console.error(`sessionConfig fail : ${err}`);
46. }
47. }
```
