---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hmaf-function
title: 通过Function组件拉起智能体
breadcrumb: 指南 > AI > Agent Framework Kit（智能体框架服务） > 通过Function组件拉起智能体
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:52+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:a4162fe3c3f87def01a205748eace312a2416d5f41d8e0bc4e5941e8aaf5abfa
---

## 场景介绍

* Function组件分为图标组件和按钮组件，无标题时默认显示图标组件，有标题时默认显示按钮组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/wJNym3f6RjGTIxDQFWZRrw/zh-cn_image_0000002589325579.png?HW-CC-KV=V1&HW-CC-Date=20260429T054050Z&HW-CC-Expire=86400&HW-CC-Sign=134DB6D332108DE842A407024491C6D0631B5B0AA7BD7E670408F0F464116C22)
* Function图标组件效果：综合型入口。不带用户意图，可作为应用内智能体主入口。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/Ln33v-peSzS1dsHuXy-1sA/zh-cn_image_0000002589245517.png?HW-CC-KV=V1&HW-CC-Date=20260429T054050Z&HW-CC-Expire=86400&HW-CC-Sign=200CE83032BA3AEA663121F78A9EE95515652FC669E35D3780A61034FDB53287)
* Function按钮组件：允许应用自定义功能描述的组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/15su13K5RCCWHJLBq7XL1A/zh-cn_image_0000002558765710.png?HW-CC-KV=V1&HW-CC-Date=20260429T054050Z&HW-CC-Expire=86400&HW-CC-Sign=9A2FCA6341E52601208EA22231BB2ABFEAB92CED7F0AB1518A27D87E9C152416)

## 开发前准备

* 创建智能体，具体请参见[快速创建智能体](../service/quick-start-0000002469548009.md)。
* 关联应用，具体请参见[关联应用](../service/related-applications-0000002437785706.md)。
* 确保已在终端设备上登录华为账号，并且处于联网状态。

## 开发步骤

1. 从项目根目录进入/src/main/ets/pages/Index.ets文件，将FunctionComponent及相关其它类引入到工程。

   ```
   1. import { FunctionComponent, FunctionController } from '@kit.AgentFrameworkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { common } from '@kit.AbilityKit';
   ```
2. （可选）可以在组件加载前通过[isAgentSupport](../harmonyos-references/hmaf-function-component.md#isagentsupport)来判断当前的agentId是否可用，若agentId有效且Agent功能支持时再加载组件。

   ```
   1. @State isAgentSupport: boolean = false;

   3. aboutToAppear() {
   4. this.checkAgentSupport()
   5. }
   6. async checkAgentSupport() {
   7. try {
   8. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
   9. this.isAgentSupport = await this.controller.isAgentSupport(context, this.agentId)
   10. } catch (err) {
   11. hilog.error(0x0001, 'AgentExample', `err code: ${err.code}, message: ${err.message}`)
   12. }
   13. }

   15. build() {
   16. Column() {
   17. if (this.isAgentSupport) {
   18. FunctionComponent({
   19. agentId: this.agentId,
   20. onError: (err: BusinessError) => {
   21. hilog.error(0x0001, 'AgentExample', `err: ${JSON.stringify(err)}, message: ${err.message}`);
   22. },
   23. options: {
   24. title: '智能创建',
   25. queryText: '创建一个新的模式'
   26. }
   27. })
   28. }
   29. }
   30. }
   ```
3. 构建一个简单配置的页面，在页面中引入FunctionComponent组件，并传入对应的参数。其中agentId、onError是必填参数。其他可选参数可参见[FunctionComponent（功能组件）](../harmonyos-references/hmaf-function-component.md)。Function组件布局可参考[组件布局](arkts-layout-development.md)。

   ```
   1. @Entry
   2. @Component
   3. export struct AgentExample {
   4. private controller: FunctionController = new FunctionController();
   5. private agentId: string = 'agentproxy65481da1fa2293a8482d45'; // 智能体对应的agentid，由小艺智能体平台在创建智能体时指定
   6. build() {
   7. Column() {
   8. FunctionComponent({
   9. agentId: this.agentId,
   10. onError: (err: BusinessError) => {
   11. hilog.error(0x0001, 'AgentExample', `err: ${JSON.stringify(err)}, message: ${err.message}`);
   12. },
   13. options: {
   14. title: '',
   15. queryText: ''
   16. },
   17. controller: this.controller
   18. })
   19. }
   20. }
   21. }
   ```
4. 添加订阅事件。

   ```
   1. aboutToAppear() {
   2. this.initListeners();
   3. }
   4. initListeners() {
   5. this.controller?.on('agentDialogOpened', this.onAgentOpenedCallback);
   6. this.controller?.on('agentDialogClosed', this.onAgentClosedCallback);
   7. }
   8. onAgentOpenedCallback = () => {
   9. hilog.info(0x0001, 'AgentExample', 'agent dialog opened callback');
   10. };
   11. onAgentClosedCallback = () => {
   12. hilog.info(0x0001, 'AgentExample', 'agent dialog closed callback');
   13. };
   14. aboutToDisappear() {
   15. this.controller?.off('agentDialogOpened');
   16. this.controller?.off('agentDialogClosed');
   17. }

   19. build() {
   20. Column() {
   21. FunctionComponent({
   22. agentId: this.agentId,
   23. onError: (err: BusinessError) => {
   24. hilog.error(0x0001, 'AgentExample', `err: ${JSON.stringify(err)}, message: ${err.message}`);
   25. },
   26. controller: this.controller
   27. })
   28. }
   29. }
   ```

## 开发实例

点击按钮，打开智能体对话框。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. import {
5. FunctionComponent,
6. FunctionController
7. } from '@kit.AgentFrameworkKit';

9. @Entry
10. @Component
11. export struct AgentExample {
12. private controller: FunctionController = new FunctionController();
13. private agentId: string = 'agentproxy65481da1fa2293a8482d45';

15. aboutToAppear() {
16. this.initListeners();
17. }
18. initListeners() {
19. this.controller?.on('agentDialogOpened', this.onAgentOpenedCallback);
20. this.controller?.on('agentDialogClosed', this.onAgentClosedCallback);
21. }
22. onAgentOpenedCallback = () => {
23. hilog.info(0x0001, 'AgentExample', 'agent dialog opened callback');
24. };
25. onAgentClosedCallback = () => {
26. hilog.info(0x0001, 'AgentExample', 'agent dialog closed callback');
27. };
28. aboutToDisappear() {
29. this.controller?.off('agentDialogOpened');
30. this.controller?.off('agentDialogClosed');
31. }

33. build() {
34. Column() {
35. FunctionComponent({
36. agentId: this.agentId,
37. onError: (err: BusinessError) => {
38. hilog.error(0x0001, 'AgentExample', `err: ${JSON.stringify(err)}, message: ${err.message}`);
39. },
40. options: {
41. title: '智能创建',
42. queryText: '创建一个新的情景',
43. isShowShadow: true
44. },
45. controller: this.controller
46. })
47. }
48. }
49. }
```
