---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-customproxyconfig
title: ProxyConfiguration：定制代理
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 使用HTTP协议进行网络通信 > 实现HTTP请求定制 > Configuration：高效实现定制功能 > ProxyConfiguration：定制代理
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b058ff0473957db23982312eb4bf47cf09514bf0d81630d94329753ca9be147c
---

## 场景介绍

在远场通信框架中，ProxyConfiguration配置会话代理设置，提供system、no-proxy和WebProxy三种选项。

* system使用系统代理，适合快速部署；
* no-proxy不使用代理，适用于需直接访问特定资源或有代理限制的环境；
* WebProxy允许开发者自定义代理设置，解决特定网络问题，优化代理路径，提升性能和用户体验。

## 约束与限制

定制代理能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。

## 使用示例

下面将对框架提供的三种选项（'system'，'no-proxy'，'WebProxy'）以示例代码的方式进行说明。

### 'no-proxy'

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建一个新的会话对象和请求，会话用于管理后续的网络请求。

   ```
   1. const session = rcp.createSession();
   2. // 定义请求的URL（请根据实际需求调整）
   3. const requestURL = 'https://example.com';
   ```
3. 定义发起请求时需要的代理配置，在定义proxyConfiguration时选择'no-proxy'即可将代理方式选择为不使用代理方式。

   ```
   1. // 配置请求的proxy方式为'no-proxy'
   2. const configuration: rcp.Configuration = {
   3. proxy: 'no-proxy'
   4. }
   5. // 定义request并将请求configuration添加到request中
   6. const request = new rcp.Request(requestURL, "GET");
   7. request.configuration = configuration;
   ```
4. 利用fetch发起网络请求并在成功或失败时进行响应的处理，此处只给出示例，对成功或失败的处理请根据实际业务来实现。

   ```
   1. session.fetch(request).then((response: rcp.Response) => {
   2. // 处理请求成功响应
   3. console.info(`Response success, ${response}`);
   4. // 关闭会话
   5. session.close();
   6. }).catch((err: BusinessError) => {
   7. // 处理请求失败响应
   8. console.error(`The error code is ${err.code}, error data is ${err.data}`);
   9. // 关闭会话
   10. session.close();
   11. })
   ```

### 'system'

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建一个新的会话对象和请求，会话用于管理后续的网络请求。

   ```
   1. const session = rcp.createSession();
   2. // 定义请求的URL（请根据实际需求调整）
   3. const requestURL = 'https://example.com';
   ```
3. 定义发起请求时需要的代理配置，在定义proxyConfiguration时选择'system'即可将代理方式选择为使用系统代理方式。

   ```
   1. // 配置请求的proxy方式为'system'
   2. const configuration: rcp.Configuration = {
   3. proxy: 'system'
   4. }
   5. // 定义request并将请求configuration添加到request中
   6. const request = new rcp.Request(requestURL, "GET");
   7. request.configuration = configuration;
   ```
4. 利用fetch发起网络请求并在成功或失败时进行响应的处理，此处只给出示例，对成功或失败的处理请根据实际业务来实现。

   ```
   1. session.fetch(request).then((response: rcp.Response) => {
   2. // 处理请求成功响应
   3. console.info(`Response success, ${response}`);
   4. // 关闭会话
   5. session.close();
   6. }).catch((err: BusinessError) => {
   7. // 处理请求失败响应
   8. console.error(`The error code is ${err.code}, error data is ${err.data}`);
   9. // 关闭会话
   10. session.close();
   11. })
   ```

### WebProxy（自定义代理设置）

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建一个新的会话对象和请求，会话用于管理后续的网络请求。

   ```
   1. const session = rcp.createSession();
   2. // 定义请求的URL（请根据实际需求调整）
   3. const requestURL = 'https://example.com';
   ```
3. 通过WebProxy自定义代理配置，通过声明式方式。

   ```
   1. // 自定义proxy
   2. const configuration: rcp.Configuration = {
   3. proxy: {
   4. url: 'https://www.example.com',
   5. createTunnel: 'always',
   6. exclusions: [
   7. 'https://www.example1.com',
   8. 'https://www.example2.com'
   9. ]
   10. }
   11. }
   12. // 定义request并将请求configuration添加到request中
   13. const request = new rcp.Request(requestURL, "GET");
   14. request.configuration = configuration;
   ```
4. 利用fetch发起网络请求并在成功或失败时进行响应的处理，此处只给出示例，对成功或失败的处理请根据实际业务来实现。

   ```
   1. session.fetch(request).then((response: rcp.Response) => {
   2. // 处理请求成功响应
   3. console.info(`Response success, ${response}`);
   4. // 关闭会话
   5. session.close();
   6. }).catch((err: BusinessError) => {
   7. // 处理请求失败响应
   8. console.error(`The error code is ${err.code}, error data is ${err.data}`);
   9. // 关闭会话
   10. session.close();
   11. })
   ```
