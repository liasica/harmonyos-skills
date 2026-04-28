---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-customdnsconfig
title: DnsConfiguration：定制DNS
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 使用HTTP协议进行网络通信 > 实现HTTP请求定制 > Configuration：高效实现定制功能 > DnsConfiguration：定制DNS
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:62a7cbeb5b44ad5eb1c6b9a6337ab5cd7814a60536c7ddb1051671890879873e
---

## 场景介绍

在远程通信服务框架中，Remote Communication Kit提供了一套高度可定制的 DNS（Domain Name System）请求规则服务，这一服务允许开发者根据自身需求调整 DNS 查询行为。此外，支持用户自定义 DNS 服务器设置。开发者可根据具体的网络环境或安全需求，选择最适合的 DNS 服务器进行配置。通过这些功能，开发者不仅能够实现网络管理的高效性，还能增强网络的安全性，确保数据传输的稳定与安全。DnsConfiguration中可设置dnsRules、dnsOverHttps。

* dnsRules（配置DNS规则）

  自定义DNS服务器（[DnsServers](../harmonyos-references/remote-communication-rcp.md#dnsservers)）：可指定自定义的DNS服务器提供解析服务。

  自定义静态DNS（[StaticDnsRules](../harmonyos-references/remote-communication-rcp.md#staticdnsrules)）：当默认的DNS不能正常解析部分域名，就需要手动添加静态DNS。添加静态DNS后，如果hostname匹配，则优先使用指定的地址。

  自定义动态DNS（[DynamicDnsRule](../harmonyos-references/remote-communication-rcp.md#dynamicdnsrule)）：除了添加静态DNS外，还可以添加动态DNS。动态DNS可看作一个可以根据hostname和port直接返回IP地址的函数，如果设置，则优先使用函数中返回的地址。

  注意

  针对同一域名配置多个静态或者动态DNS规则后，Remote Communication Kit将按照配置的规则轮询服务器。
* dnsOverHttps

  DNS over HTTPS配置（[DnsOverHttpsConfiguration](../harmonyos-references/remote-communication-rcp.md#dnsoverhttpsconfiguration)）：配置HTTPS上的DNS（DOH）设置，以加密的HTTPS协议进行DNS解析请求，避免原始DNS协议中用户的DNS解析请求被窃听或者修改的问题，实现保护用户隐私的目的。如果设置，则优先使用DNS服务器解析的地址。

## 约束与限制

定制DNS能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。

## 使用示例

下面以定制DNS服务器、重写DNS解析函数两个示例来说明如何进行DNS的定制，从而获取最佳的DNS性能体验。

### 定制DNS服务器

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建一个新的会话对象和请求，会话用于管理后续的网络请求。同时需要定义一个具体的请求，请求中指定了需要请求的URL。

   ```
   1. const session = rcp.createSession();
   2. // 其中的URL需要根据自身业务需要调整
   3. const request = new rcp.Request('https://example.com');
   ```
3. 设置请求的DNS规则，可根据自身业务的需要对DNS的ip和port进行设置。

   ```
   1. request.configuration = {
   2. dns: {
   3. dnsRules: [
   4. {
   5. ip: 'x.xxx.x.xx', // DNS服务器的IP地址
   6. port: 53, // DNS服务器的端口号
   7. },
   8. ]
   9. }
   10. };
   ```
4. 利用fetch发起网络请求并在成功或失败时进行响应的处理，此处只给出示例，对成功或失败的处理请根据实际业务来实现。

   ```
   1. session.fetch(request).then((response: rcp.Response) => {
   2. console.info(`The response is ${JSON.stringify(response)}`); // 处理成功响应
   3. // 关闭会话
   4. session.close();
   5. }).catch((err: BusinessError) => {
   6. console.error(`The error code is ${err.code}, error data is ${err.data}`); // 处理错误
   7. // 关闭会话
   8. session.close();
   9. })
   ```

### 定制DNS解析函数

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建一个新的会话对象和请求，会话用于管理后续的网络请求。同时需要定义一个具体的请求，请求中指定了需要请求的URL。

   ```
   1. const session = rcp.createSession();
   2. // 定义请求的URL（请根据实际需求调整）
   3. const requestURL = 'https://example.com';
   4. const request = new rcp.Request(requestURL);
   ```
3. 设置DNS解析规则，此处请根据自身业务进行逻辑处理，本例只给出简单示例。

   ```
   1. request.configuration = {
   2. dns: {
   3. dnsRules: (host: string, port: number): rcp.IpAddress[] => {
   4. if (host === 'example.com') {
   5. return ['x.xxx.x.xx', 'x.xxx.x.xx']; // 此处请根据实际情况填写
   6. }
   7. return [];
   8. }
   9. }
   10. };
   ```
4. 利用fetch发起网络请求并在成功或失败时进行响应的处理，此处只给出示例，对成功或失败的处理请根据实际业务来实现。

   ```
   1. session.fetch(request).then((response: rcp.Response) => {
   2. // 处理成功响应
   3. console.info(`The response is ${JSON.stringify(response)}`);
   4. // 关闭会话
   5. session.close();
   6. }).catch((err: BusinessError) => {
   7. // 处理错误
   8. console.error(`The error code is ${err.code}, error data is ${err.data}`);
   9. // 关闭会话
   10. session.close();
   11. })
   ```
