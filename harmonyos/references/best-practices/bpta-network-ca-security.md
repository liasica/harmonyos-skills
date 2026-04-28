---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-network-ca-security
title: 网络连接安全配置
breadcrumb: 最佳实践 > 应用安全 > 网络连接安全配置
category: best-practices
scraped_at: 2026-04-28T08:22:17+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:319d7d5c217c5458f789d60d72c6f62c9e82f175cfe678b9145f58e080b725ba
---

## 概述

应用与服务器之间的数据传输需确保安全，保护数据的机密性和完整性，防止敏感数据被窃取和篡改。推荐使用传输层安全协议（TLS）保护数据安全。

当应用通过HTTPS访问云侧服务器时，如果信任了用户安装的CA证书，用户可以通过网络代理工具（如Fiddler、Charles）对HTTPS消息进行中间人攻击，如查看、篡改请求和响应消息，这可能导致应用或云侧服务器产生安全风险。因此，通过HTTPS访问云侧服务器时，应配置CA证书进行合法性校验。

本文介绍如何配置CA证书以进行合法性校验，避免应用或云侧服务器的安全风险。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/kbFd_EfPRQa8cShu7MAdag/zh-cn_image_0000002457689021.png?HW-CC-KV=V1&HW-CC-Date=20260428T002216Z&HW-CC-Expire=86400&HW-CC-Sign=DF4207751616ECC1713C1EA12063D8211A4BE8E545D42E964BEEA77CC4D5D220 "点击放大")

## 配置CA证书对服务器进行合法性校验

当应用通过TLS协议连接服务器时，服务器会提供证书链来证明其身份，应用需要使用可信的CA（证书颁发机构）证书对服务器证书链进行合法性校验。

服务器根据场景使用不同类型的CA颁发的证书链：

1. 权威CA证书，如CFCA、GlobalSign CA机构的根CA证书，满足业界管理规范并通过审计认证，可信度高。
2. 企业自建的CA证书，用于企业内部服务器的证书链。企业内部应用直接信任此类CA证书。

系统提供3种CA证书管理方式：

1. 系统预置CA证书：系统预置了业界主流的权威CA证书。
2. 应用管理的CA证书：应用可在Hap内预置可信的CA证书，如企业内部自建的CA证书。
3. 用户安装的CA证书：通过系统设置界面安装的私有CA证书。这类证书可信度较低，可能被用于中间人攻击。

开发者应结合应用的业务场景，在不影响业务功能的前提下，合理设置可信CA证书的范围：

* 面向互联网用户的应用，建议只[配置信任系统预置的CA证书](bpta-network-ca-security.md#section121091116142117)。
* 只访问企业内部服务器的应用，建议只[配置信任应用管理的CA证书](bpta-network-ca-security.md#section05271716102218)。
* 同时访问企业内部服务器和互联网服务的应用，建议根据访问的服务器域名分别配置[信任系统预置的CA证书](bpta-network-ca-security.md#section121091116142117)或[应用管理的CA证书](bpta-network-ca-security.md#section05271716102218)。
* 应用开发和调测过程中需要进行网络抓包以定位问题和测试，建议仅在调测版本[配置信任用户安装的CA证书](bpta-network-ca-security.md#section12518142215236)。
* 应用需支持通过企业代理服务器访问应用服务器，可信任企业MDM系统或设备管理员用户手动安装[CA证书](bpta-network-ca-security.md#section12518142215236)。然而，设备管理员用户可能通过代理工具抓取应用网络数据，建议在应用层实施安全防护，如对敏感数据进行二次加密或签名。
* 对于需要较高网络安全的应用（如金融支付、银行类应用），配置CA证书后，通过[SSL Pinning方式](bpta-network-ca-security.md#section4337175511234)绑定服务器证书的公钥，以增强安全性。

## 网络连接安全配置

### 配置信任系统预置的CA证书

面向互联网用户提供服务的应用，通常只需信任系统预置的CA证书。[Network Kit（网络服务）](../harmonyos-guides/network-kit.md)和[Remote Communication Kit（远场通信服务）](../harmonyos-guides/remote-communication-kit-guide.md)的HTTPS连接已默认信任系统预置的CA证书。

说明

系统Network Kit和Remote Communication Kit的HTTPS连接默认信任系统预置的CA证书和用户安装的CA证书，可[配置不信任用户安装的CA证书](bpta-network-ca-security.md#section11935814273)提升安全性。

如果应用使用第三方库进行网络连接，需要手动设置系统预置的CA证书路径：/etc/security/certificates。

**示例**

使用三方库[curl](https://gitee.com/openharmony-sig/tpc_c_cplusplus/tree/master/thirdparty/curl)进行HTTPS连接，通过下面代码设置信任的CA证书路径：

```
1. curl_easy_setopt(curl, CURLOPT_CATH, "/etc/security/certificates");
```

[Cybersecurity.md](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/Cybersecurity.md#L21-L21)

### 配置不信任用户安装的CA证书

**Network Kit和Remote Communication Kit配置不信任用户安装的CA证书**：在src/main/resources/base/profile/network\_config.json[配置文件](../harmonyos-guides/http-request.md#配置证书校验)中进行配置。

```
1. {
2. "network-security-config": {
3. ... ...
4. },
5. "trust-global-user-ca": false,  //Configure whether to trust the CA certificate manually installed by the enterprise MDM system or device administrator. The default value is true
6. "trust-current-user-ca": false  // Configure whether to trust the CA certificate installed by the current user. The default value is true
7. }
```

[Cybersecurity.md](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/Cybersecurity.md#L30-L36)

### 配置信任应用管理的CA证书

如果应用服务器使用企业内部自建的CA证书，可以在Hap包中预置这些CA证书，并配置信任。

* Network Kit和Remote Communication Kit可以通过src/main/resources/base/profile/network\_config.json文件进行配置。例如，可以将应用级信任的 CA 证书预置到/data/storage/el1/bundle/entry/resources/resfile/appCaCert目录，将特定域名信任的CA 证书预置到/data/storage/el1/bundle/entry/resources/resfile/domainCaCert目录。

  ```
  1. {
  2. "network-security-config": {
  3. "base-config": {
  4. "trust-anchors": [
  5. {
  6. "certificates": "/data/storage/el1/bundle/entry/resources/resfile/appCaCert"
  7. }
  8. ]
  9. },
  10. "domain-config": [
  11. {
  12. "domains": [
  13. {
  14. "include-subdomains": true,
  15. "name": "example.com"
  16. }
  17. ],
  18. "trust-anchors": [
  19. {
  20. "certificates": "/data/storage/el1/bundle/entry/resources/resfile/domainCaCert"
  21. }
  22. ]
  23. }
  24. ]
  25. }
  26. }
  ```

  [Cybersecurity.md](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/Cybersecurity.md#L45-L70)

  Network Kit也支持在发起HTTPS请求的代码中[指定信任的CA证书路径](../harmonyos-references/js-apis-http.md#httprequestoptions)：

  ```
  1. httpRequest.request( 'EXAMPLE_URL',  {
  2. method: http.RequestMethod.POST,
  3. header: {
  4. 'Content-Type': 'application/json'
  5. },
  6. extraData: 'data to send',
  7. expectDataType: http.HttpDataType.STRING,
  8. connectTimeout: 60000,
  9. caPath:'/data/storage/el1/bundle/entry/resources/resfile/domainCaCert', // Specifies the trusted CA certificate path
  10. }, (err: BusinessError, data: http.HttpResponse) => {
  11. // ...
  12. })
  ```

  [NetworkTrust.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/NetworkTrust.ets#L26-L37)

  Remote Communication Kit也支持在代码中[指定信任的CA证书路径](../harmonyos-references/remote-communication-rcp.md#section1597118916425)：

  ```
  1. const caPath: rcp.CertificateAuthority = {
  2. folderPath: '/data/storage/el1/bundle/entry/resources/resfile/appCaCert', // Specify trusted CA certificate path
  3. }
  4. const securityConfig: rcp.SecurityConfiguration = {
  5. remoteValidation: caPath
  6. };
  7. // Use the security configuration in the session creation
  8. const sessionWithSecurityConfig = rcp.createSession({ requestConfiguration: { security: securityConfig } });
  ```

  [NetworkTrust.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/NetworkTrust.ets#L46-L53)

说明

系统Network Kit和Remote Communication Kit在完成上述配置后，HTTPS连接仍信任系统预置的CA证书和用户安装的CA证书。如需提升安全性，可[配置不信任用户安装的CA证书](bpta-network-ca-security.md#section11935814273)。

* 如果应用使用三方库进行网络连接，需要在代码中设置应用管理的CA证书路径。例如，使用三方库[curl](https://gitee.com/openharmony-sig/tpc_c_cplusplus/tree/master/thirdparty/curl)进行HTTPS连接时，可以通过以下代码设置信任的CA证书路径：

  ```
  1. curl_easy_setopt(curl, CURLOPT_CATH, "/data/storage/el1/bundle/entry/resources/resfile/domainCaCert");
  ```

  [Cybersecurity.md](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/Cybersecurity.md#L78-L78)

### 配置信任用户安装的CA证书

用户安装的CA证书可信度较低，除以下场景外，建议应用不信任用户安装的CA证书：

1. 应用开发和调测过程中需要进行网络抓包以定位问题和测试。用户通过系统的设置界面安装的CA证书，保存在目录：**/data/certificates/user\_cacerts/{userid}** ，其中 userid 从100开始。

   **注意：**在商用发布的应用版本中应该不信任用户安装的CA证书。
2. 面向2B企业应用的场景，应用需支持通过企业代理服务器访问应用服务器。设备需通过企业的MDM系统或设备管理员用户手工安装CA证书，并保存在目录：**/data/certificates/user\_cacerts/0**。

### 配置SSL Pinning证书锁定

应用默认信任系统预置的CA证书。如果预置的CA颁发了不可信证书，应用将面临攻击风险。对于需要高网络安全的应用，如金融支付和银行类应用，可以通过配置SSL Pinning证书锁定方式，仅信任指定服务器证书的公钥。

配置SSL Pinning支持两种方式。如果服务器域名固定，建议采用静态SSL Pinning。否则，采用动态SSL Pinning。

说明

SSL Pinning要求应用云侧服务器证书的公钥不能变化。如果公钥发生变化，需要修改应用内配置的证书公钥，否则应用的网络连接将失败。因此，建议SSL Pinning配置始终包含至少一个备用公钥。

应用还可以设置SSL Pinning的到期时间。到期后，证书将不再被锁定，这有助于在服务器证书公钥变化时防止尚未更新的应用出现连接问题。然而，设置SSL Pinning的到期时间可能会使攻击者绕过证书锁定。

请开发者评估并决定是否配置SSL Pinning证书锁定。如果应用在应用层对敏感信息进行了加密或签名，则安全风险较低。

1. 通过network\_config.json文件进行静态SSL Pinning配置：

   ```
   1. {
   2. "network-security-config": {
   3. "domain-config": [
   4. {
   5. "domains": [
   6. {
   7. "include-subdomains": true,
   8. "name": "server.com"
   9. }
   10. ],
   11. "pin-set": {
   12. "expiration": "2024-11-08",
   13. "pin": [
   14. {
   15. "digest-algorithm": "sha256",
   16. "digest": "g8CsdcpyAKxmLoWFvMd2hC7ZDUy7L4E2NYOi1i8qEtE=" // Hash of the server certificate public key
   17. }
   18. ]
   19. }
   20. }
   21. ]
   22. }
   23. }
   ```

   [Cybersecurity.md](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/Cybersecurity.md#L87-L109)

   具体可参考配置指导的[“证书锁定”](../harmonyos-guides/http-request.md#证书锁定)章节。
2. 通过在代码中动态设置进行动态SSL Pinning配置：
   * Network Kit配置动态SSL Pinning：

     ```
     1. certificatePinning: [ //Optional, supports dynamic setting of certificate lock configuration information. This property is supported since API 12
     2. {
     3. publicKeyHash: 'g8CsdcpyAKxmLoWFvMd2hC7ZDUy7L4E2NYOi1i8qEtE=', // Hash of the server certificate public key
     4. hashAlgorithm: 'SHA-256'
     5. }, {
     6. publicKeyHash: 'MGFiY2UyMDk5ZjEyMzI3MWQ4MDMyY2E4ODEzMmY3EtE=', // Hash of the secondary public key of the server certificate
     7. hashAlgorithm: 'SHA-256'
     8. }
     9. ]
     ```

     [Cybersecurity.md](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/Cybersecurity.md#L118-L126)

     具体可参考配置指导的[“certificatePinning”参数说明](../harmonyos-references/js-apis-http.md#httprequestoptions)。
   * Remote Communication Kit配置动态SSL Pinning：

     ```
     1. const keyHash: string = 'g8CsdcpyAKxmLoWFvMd2hC7ZDUy7L4E2NYOi1i8qEtE='; // Public key of the server certificate
     2. const session = rcp.createSession();
     3. const request = new rcp.Request(HTTP_SERVER);
     4. const pin: rcp.CertificatePinning = {
     5. kind: 'public-key',
     6. publicKeyHash: keyHash,
     7. hashAlgorithm: 'SHA-256'
     8. };
     9. request.configuration = {
     10. security: {
     11. certificatePinning: pin,
     12. }
     13. };
     14. const resp = await session.fetch(request);
     ```

     [NetworkTrust.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/NetworkTrust.ets#L63-L76)

     具体可参考配置指导的[“certificatePinning”参数说明](../harmonyos-references/remote-communication-rcp.md#section1597118916425)。
