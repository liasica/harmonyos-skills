---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-background
title: 推送后台消息
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 推送场景化消息 > 推送后台消息
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:55+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:8bad98e55ec528c8fb28b1fde3d095d5631985ea83bd7161c2983428182b9e9b
---

## 场景介绍

后台消息用于内容不频繁更新的场景，不会显示通知、播放铃声或改变应用角标。终端设备接收到后台消息后，如果应用进程在前台则将消息内容传给应用；如果应用进程不在前台则缓存消息，等待应用启动后再传给应用。

说明

终端缓存消息默认仅缓存最新的一条消息，最多缓存7天。

## 约束与限制

推送后台消息能力支持Phone、Tablet、PC/2in1。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备。

## 频控规则

**调测阶段**，每个项目每日全网最多可推送1000条测试消息。发送测试消息需设置[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)为true。

**正式发布阶段**，单设备单应用下每日推送消息总条数受[设备消息频控](../harmonyos-references/push-msg-freq-control.md#设备消息频控)限制，系统会根据现网使用场景和流量进行管控，不合理的使用场景系统会进行频控。

说明

* 后台消息优先级较低，建议每小时不超过2条，否则消息可能会被丢弃。
* 后台消息推送会受设备电量状态、系统休眠、用户使用行为等影响，消息可能不会及时下发。

## 开发步骤

说明

开发者希望在应用进程不在前台时，可根据实际情况选择消息缓存的策略。

* 开发者仅需缓存终端侧的最新一条消息，可不执行步骤2~步骤4。
* 若开发者需缓存终端侧更多消息，可参考开发步骤2~步骤4开发适配端侧数据库并开启数据代理写入，Push Kit将后台消息写入数据库中，当您的应用进程在前台时，需要自行读取数据库中的消息。

1. 参见指导[获取Push Token](push-get-token.md)。
2. （可选）应用客户端参见[指导](data-persistence-by-rdb-store.md)新建一个数据库（如**pushmessage.db**），并严格按照如下格式创建一张数据表（如**t\_push\_message**）。

   | 字段名称 | 字段类型 | 说明 |
   | --- | --- | --- |
   | id | INTEGER | 自增主键。 |
   | message\_id | TEXT | 消息id。 |
   | push\_type | TEXT | 场景类型。 |
   | message\_action | INTEGER | 消息动作。 |
   | message | TEXT | 消息内容。 |
   | field1 | TEXT | 扩展字段1。 |
   | field2 | TEXT | 扩展字段2。 |
   | field3 | TEXT | 扩展字段3。 |
   | field4 | TEXT | 扩展字段4。 |
   | field5 | TEXT | 扩展字段5。 |
   | create\_time | INTEGER | 消息写入数据库的时间戳，单位毫秒（ms）。 |
3. （可选）在项目模块级目录的 src/main/resources/base/profile/ 下创建 **PushMessage.json** 文件，文件内容如下：

   ```
   1. {
   2. "path": "pushmessage/t_push_message",
   3. "type": "rdb",
   4. "scope": "application"
   5. }
   ```

   * path：值为步骤2中创建的数据表路径，格式为 **[数据库名称]/[数据表名称]** （如pushmessage/t\_push\_message）。
   * type：固定值为**rdb**，表示关系型数据库。
   * scope：表示数据库的范围，可填**application**（应用级）或**module**（hap模块级）。
4. （可选）在项目模块级目录的 src/main/module.json5 文件添加**proxyData** 如下配置：

   ```
   1. {
   2. "module": {
   3. "proxyData":[{
   4. "uri": "datashareproxy://{bundleName}/PushMessage",
   5. "requiredWritePermission": "ohos.permission.WRITE_PRIVACY_PUSH_DATA",
   6. "metadata":{
   7. "name": "dataProperties",
   8. "resource": "$profile:PushMessage"
   9. }
   10. }]
   11. }
   12. }
   ```

   * uri：固定格式为 datashareproxy://{bundleName}/PushMessage，请将 **{bundleName}** 替换为开发者应用的bundleName，PushMessage为固定名称，请勿随意更改。
   * requiredWritePermission：固定值为 **ohos.permission.WRITE\_PRIVACY\_PUSH\_DATA**，Push Kit需要使用该权限往数据库里写入后台消息数据。
   * metadata：扩展配置，name固定值为**dataProperties**，resource固定格式为 **$profile:文件名称**，文件名称固定为**PushMessage**。
5. 在项目中现有的UIAbility类（以PushMessageAbility为例）的onCreate()中，调用[receiveMessage](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)()方法接收后台消息。注意，您仅能使用UIAbility接收后台消息。

   ```
   1. // 文件路径: src/main/ets/abilities/PushMessageAbility.ets
   2. import { UIAbility } from '@kit.AbilityKit';
   3. import { pushService, pushCommon } from '@kit.PushKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   5. import { BusinessError } from '@kit.BasicServicesKit';

   7. /**
   8. * 此处以PushMessageAbility为例，接收后台消息内容
   9. */
   10. export default class PushMessageAbility extends UIAbility {
   11. onCreate(): void {
   12. try {
   13. pushService.receiveMessage('BACKGROUND', this, (data: pushCommon.PushPayload) => {
   14. // process message，并建议对Callback进行try-catch
   15. try {
   16. hilog.info(0x0000, 'testTag', 'Receive background message');
   17. } catch (e) {
   18. let errRes: BusinessError = e as BusinessError;
   19. hilog.error(0x0000, 'testTag', 'Failed to process data: %{public}d %{public}s', errRes.code, errRes.message);
   20. }
   21. });
   22. } catch (err) {
   23. let e: BusinessError = err as BusinessError;
   24. hilog.error(0x0000, 'testTag', 'Failed to get background message: %{public}d %{public}s', e.code, e.message);
   25. }
   26. }
   27. }
   ```
6. 在项目工程的 src/main/module.json5文件的abilities模块的**skills**标签中配置**actions**内容为**action.ohos.push.listener**（有且只能有一个ability定义该action，**若同时添加uris参数，则uris内容需为空**）。

   ```
   1. "abilities": [
   2. {
   3. "name": "PushMessageAbility",
   4. "srcEntry": "./ets/abilities/PushMessageAbility.ets",
   5. "launchType": "singleton",
   6. "startWindowIcon": "$media:startIcon",
   7. "startWindowBackground": "$color:start_window_background",
   8. "exported": false,
   9. "skills": [
   10. // 保持现有skill对象不变
   11. {
   12. "actions": [
   13. "com.app.action"
   14. ]
   15. },
   16. // 新增一个独立的skill对象，配置actions参数
   17. {
   18. "actions": [
   19. "action.ohos.push.listener"
   20. ]
   21. }
   22. ]
   23. }
   24. ]
   ```
7. 应用服务端调用REST API推送后台消息，消息详情可参见[场景化消息API接口功能介绍](../harmonyos-references/push-scenariozed-api-intro.md)，请求示例如下：

   ```
   1. // Request URL
   2. POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

   4. // Request Header
   5. Content-Type: application/json
   6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   7. push-type: 6

   9. // Request Body
   10. {
   11. "payload": {
   12. "extraData": "携带的额外数据",
   13. "proxyData": "ENABLE"
   14. },
   15. "target": {
   16. "token": ["MAMzLg**********lPW"]
   17. }
   18. }
   ```

   * [projectId]：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
   * Authorization：JWT格式字符串，可参见[Authorization](../harmonyos-references/push-scenariozed-api-request-struct.md#request-header)获取。
   * push-type：6表示后台消息场景。
   * token：Push Token，可参见[获取Push Token](push-get-token.md)获取。
   * extraData：携带的额外数据，字符串类型。详情请参见[extraData](../harmonyos-references/push-scenariozed-api-request-param.md#backgroundpayload-后台消息)。
   * proxyData（选填）：进程不存在时是否开启数据代理静默写入到应用自身缓存，当前只能传全大写"ENABLE"开启代理。若您不希望开启代理写入，请不要在消息体中填写此字段。详情请参见[proxyData](../harmonyos-references/push-scenariozed-api-request-param.md#backgroundpayload-后台消息)。

   当设备中的应用进程在前台时会直接拉起应用并将数据传递，您可以在[receiveMessage](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)()方法中获取消息数据。

   当应用进程不在前台且[proxyData](../harmonyos-references/push-scenariozed-api-request-param.md#backgroundpayload-后台消息)为“ENABLE”时，Push Kit将后台消息写入到数据库中，建议应用进程在前台时将数据库中数据迁移到您业务数据库中（**避免数据库大小无限制增长**）。当应用进程不在前台且无[proxyData](../harmonyos-references/push-scenariozed-api-request-param.md#backgroundpayload-后台消息)时则为缓存消息（**发送多条消息时仅缓存最新的一条**），等下次应用进程在前台时调用[getToken](../harmonyos-references/push-pushservice.md#pushservicegettoken-1)()接口，Push Kit将重新发送缓存消息，您可以在[receiveMessage](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)方法获取消息数据。
