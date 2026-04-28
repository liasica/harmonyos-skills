---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-pc-phones-sandbox
title: 分享内容直达应用界面
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与PC/2in1碰一碰分享 > 分享内容直达应用界面
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ac2bc759148da565d2711922ef3e5ce9587827842f6df6de66ee4ec04f997440
---

从6.0.0(20)版本开始，沙箱接收能力支持PC/2in1设备；从6.1.0(23)版本开始，新增支持Tablet设备。

PC/2in1、Tablet设备创新交互方案：支持手机轻贴屏幕即可将单/多文件快速传输至PC/2in1或Tablet设备应用沙箱，传输完成后通知目标应用接收文件列表，实现无缝预览与编辑。

沙箱接收仅支持文件类型的数据，应用需指定支持接收的文件类型和最大数量。

* 若类型不匹配，则跳过已注册的沙箱接口能力，采用华为分享默认逻辑接收文件数据。参考：[目标设备接收分享数据一步直达体验](share-access-one-step.md)。
* 若数量不匹配，则通过系统弹窗提示用户异常。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
   2. import { systemShare, harmonyShare } from '@kit.ShareKit';
   3. import { common } from '@kit.AbilityKit';
   ```
2. 进入可接收数据的窗口，注册沙箱接收事件。

   ```
   1. aboutToAppear(): void {
   2. let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
   3. windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
   4. capabilities: [{ // 设置接收端支持的数据类型及数量
   5. utd: utd.UniformDataType.IMAGE,
   6. maxSupportedCount: 1,
   7. }]
   8. }
   9. // 注册沙箱接收'dataReceive'监听事件
   10. harmonyShare.on('dataReceive', capabilityRegistry, (receivableTarget: harmonyShare.ReceivableTarget) => {
   11. let uiContext: UIContext = this.getUIContext();
   12. let context = uiContext.getHostContext() as common.UIAbilityContext;
   13. receivableTarget.receive(context.filesDir, { // 此路径仅为示例 使用时请替换实际路径
   14. onDataReceived: (sharedData: systemShare.SharedData) => {
   15. let sharedRecords = sharedData.getRecords();
   16. sharedRecords.forEach((record: systemShare.SharedRecord) => {
   17. // 处理分享数据
   18. });
   19. },
   20. onResult(resultCode: harmonyShare.ShareResultCode) {
   21. if (resultCode === harmonyShare.ShareResultCode.SHARE_SUCCESS) {
   22. // To do things.
   23. }
   24. }
   25. });
   26. });
   27. }
   ```
3. 关闭可接收数据的窗口，解除沙箱接收事件。

   ```
   1. aboutToDisappear(): void {
   2. let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
   3. windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
   4. capabilities: [{
   5. utd: utd.UniformDataType.IMAGE,
   6. maxSupportedCount: 1,
   7. }]
   8. }
   9. // 解除沙箱接收'dataReceive'监听事件
   10. harmonyShare.off('dataReceive', capabilityRegistry);
   11. }
   ```

## 拒绝本次沙箱接收

当本次沙箱接收回调触发时，如果应用因为业务实现需要拒绝本次接收时，可使用[ReceivableTarget.reject()](../harmonyos-references/share-harmony-share.md#reject-1)方法拒绝本次接收。

```
1. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
2. import { harmonyShare } from '@kit.ShareKit';

4. @Component
5. export default struct Index {
6. aboutToAppear(): void {
7. let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
8. windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
9. capabilities: [{
10. utd: utd.UniformDataType.IMAGE,
11. maxSupportedCount: 1,
12. }]
13. }
14. // 注册沙箱接收'dataReceive'监听事件
15. harmonyShare.on('dataReceive', capabilityRegistry, (receivableTarget: harmonyShare.ReceivableTarget) => {
16. receivableTarget.reject(harmonyShare.ReceivableErrorCode.NO_RECEIVABLE_ERROR);
17. });
18. }

20. aboutToDisappear(): void {
21. let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
22. windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
23. capabilities: [{
24. utd: utd.UniformDataType.IMAGE,
25. maxSupportedCount: 1,
26. }]
27. }
28. // 解除沙箱接收'dataReceive'监听事件
29. harmonyShare.off('dataReceive', capabilityRegistry);
30. }

32. build() {
33. }
34. }
```
