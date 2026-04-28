---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-serviceability
title: 创建ServiceAbility
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > ServiceAbility组件开发指导 > 创建ServiceAbility
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:46cc949fd75dc7f6ca6c0f78b8fea489fab272a4aeeb04659fc9330a69180f1d
---

1. 创建ServiceAbility。

   通过DevEco Studio开发平台创建ServiceAbility时，DevEco Studio会默认生成onStart、onStop、onCommand方法，其他方法需要开发者自行实现，接口说明参见前述章节。开发者也可以添加其他Ability请求与ServiceAbility交互时的处理方法，示例如下：

   ```
   1. import { Want } from '@kit.AbilityKit';
   2. import { rpc } from '@kit.IPCKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. const TAG: string = '[Sample_FAModelAbilityDevelop]';
   6. const domain: number = 0xFF00;

   8. class FirstServiceAbilityStub extends rpc.RemoteObject {
   9. constructor(des: Object) {
   10. if (typeof des === 'string') {
   11. super(des);
   12. } else {
   13. return;
   14. }
   15. }

   17. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption): boolean {
   18. hilog.info(domain, TAG, 'ServiceAbility onRemoteRequest called');
   19. if (code === 1) {
   20. let string = data.readString();
   21. hilog.info(domain, TAG, `ServiceAbility string=${string}`);
   22. let result = Array.from(string).sort().join('');
   23. hilog.info(domain, TAG, `ServiceAbility result=${result}`);
   24. reply.writeString(result);
   25. } else {
   26. hilog.info(domain, TAG, 'ServiceAbility unknown request code');
   27. }
   28. return true;
   29. }
   30. }

   32. class ServiceAbility {
   33. onStart(): void {
   34. hilog.info(domain, TAG, 'ServiceAbility onStart');
   35. }

   37. onStop(): void {
   38. hilog.info(domain, TAG, 'ServiceAbility onStop');
   39. }

   41. onCommand(want: Want, startId: number): void {
   42. hilog.info(domain, TAG, 'ServiceAbility onCommand');
   43. }

   45. onConnect(want: Want): rpc.RemoteObject {
   46. hilog.info(domain, TAG, 'ServiceAbility onConnect' + want);
   47. return new FirstServiceAbilityStub('test');
   48. }

   50. onDisconnect(want: Want): void {
   51. hilog.info(domain, TAG, 'ServiceAbility onDisconnect' + want);
   52. }
   53. }

   55. export default new ServiceAbility();
   ```
2. 注册ServiceAbility。

   ServiceAbility需要在应用配置文件config.json中进行注册，注册类型type需要设置为service。"visible"属性表示ServiceAbility是否可以被其他应用调用，true表示可以被其他应用调用，false表示不能被其他应用调用（仅应用内可以调用）。若ServiceAbility需要被其他应用调用，注册ServiceAbility时需要设置"visible"为true，同时需要设置支持关联启动。ServiceAbility的启动规则详见[FA模型组件启动规则](component-startup-rules-fa.md)章节。

   ```
   1. {
   2. // ...
   3. "module": {
   4. // ...
   5. "abilities": [
   6. // ...
   7. {
   8. "name": ".ServiceAbility",
   9. "srcLanguage": "ets",
   10. "srcPath": "ServiceAbility",
   11. "icon": "$media:icon",
   12. "description": "$string:ServiceAbility_desc",
   13. "type": "service",
   14. "visible": true
   15. },
   16. // ...
   17. ]
   18. // ...
   19. }
   20. }
   ```
