---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-server-connect
title: 云侧服务准备
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > 云侧服务准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f75927a4b79579db4447f2906d6402e6e6ec4a7743acdadd87a633a3bc608bb8
---

Payment Kit服务提供了支付系统相关的一系列API接口。为减少API接口的接入工作量，提供了相应java版本的Maven依赖用于云侧服务对接。

开发者可通过Maven集成来完成服务器开发环境的构建，以此来快速使用华为支付提供的API接口。

可下载[示例代码-服务端](https://gitcode.com/HarmonyOS_Samples/paymentkit-sample-code-serverdemo-java)用以快速完成商户服务器接入。

说明

因业务发展需要，API接口响应、通知回调请求字段可能会发生变动，如开发者自行实现验签逻辑，一定要使用原始的字符串转为Map对象进行验签处理后再转换成自定义的业务对象去使用，以确保验签正常通过。

## 约束与限制

商户使用提供的示例代码接入华为支付前请确保网络已正常连接，可以从华为支付仓库地址正常拉取Maven依赖。

开发环境：[JDK](https://www.oracle.com/java/technologies/javase-downloads.html) 1.8及以上。

## 集成Maven依赖

在示例代码pom.xml文件中已配置仓库地址，如无法正常拉取依赖，可在Maven配置文件“settings.xml”中添加华为支付的Maven仓库地址。

```
1. <mirror>
2. <id>central</id>
3. <mirrorOf>central</mirrorOf>
4. <url>https://developer.huawei.com/repo/</url>
5. </mirror>
```

在示例代码pom.xml文件中已引入jar包的Maven坐标。如商户自己构建工程则需在pom.xml文件中引入如下坐标：

```
1. <dependency>
2. <groupId>com.huawei.petalpay</groupId>
3. <artifactId>pay-java</artifactId>
4. <version>1.0.0.331</version>
5. </dependency>
```

## 配置初始化

将以下商户相关配置添加到示例代码配置文件src/main/resources/petalpayconfig.properties。

1. 商户号，获取方式请参见[查询商户号信息](../pay-docs/hwzf-shanghuhao-0000001725982508.md)。
2. 商户私钥，获取途径请参考[准备证书](payment-certificates-config.md)。
3. 商户私钥签名类型，RSA或SM2。
4. 商户证书ID，获取方式请参见[上传商户证书](payment-certificates-config.md#上传商户证书)。
5. 鸿蒙支付服务验签公钥，获取方式请参见[下载华为支付证书](payment-certificates-config.md#下载华为支付证书)。
6. 鸿蒙支付服务加密公钥（非必选），涉及接口入参敏感字段（接口会做标注）加密时需配置，参见[敏感信息处理](payment-server-connect.md#敏感信息处理)。
7. 商户号关联的APPID，获取方式请参见[AppID管理及关联](../pay-docs/hwzf-appidguanli-0000001757041165.md)。

配置内容示例如下：

```
1. # 商户号
2. PETALPAY.MERC_NO=121540000***
3. # 商户私钥
4. PETALPAY.MERC_PRIVATE_KEY=MIIJQwIBADAN=9w0BAQEFAASCCS0wg******************************CldcDlDCSsdfDceCSDr+RyvJdfcXssdEA=
5. # 商户证书ID
6. PETALPAY.MERC_AUTH_ID=101540200089***
7. # 商户私钥签名类型
8. PETALPAY.SIGN_TYPE=RSA
9. # 鸿蒙支付服务域名
10. PETALPAY.SERVER_HOST=https://petalpay-developer.cloud.huawei.com.cn
11. # 鸿蒙支付服务验签公钥
12. PETALPAY.HW_PAY_PUBLIC_KEY_FOR_CALLBACK=6D015316F09CB747E4467******************************DB46DA4BD0960ADD500D84912
13. # 鸿蒙支付服务加密公钥（非必选）
14. PETALPAY.HW_PUBLIC_KEY_FOR_SESSIONKEY=042A7D32FA19C29D3E722D6C4ACAC0B******************************E5A5B1C8120DAC9882E4B093B9CE7A38296F87F41747D319A
15. # 商户号关联的APPID
16. PETALPAY.APPID=111831***
```

## 业务接口请求

1. 获取发起请求客户端对象

   可通过工具类MercConfigUtil提供的方法getMercConfig快速获取PetalPayConfig对象来构建请求客户端，对应配置项获取及配置参见[配置初始化](payment-server-connect.md#配置初始化)。

   ```
   1. // 商户配置
   2. public static PetalPayConfig getMercConfig() {
   3. return PetalPayConfig.builder().callerId(MERC_NO) // （必填）商户号
   4. .appId(APP_ID) // （必填）商户号关联的APPID
   5. .privateKey(MERC_PRIVATE_KEY) // （必填）商户私钥
   6. .authId(MERC_AUTH_ID) // （必填）商户证书ID
   7. .signType(SIGN_TYPE) // （选填）商户公私钥类型，默认RSA加密
   8. .petalpayPublicKey(HW_PAY_PUBLIC_KEY_FOR_CALLBACK) // （非必填）验签公钥(和接口级配置needVerifyRsp对应，公钥和商户通知回调验签公钥同一个)
   9. .domainHost(SERVER_HOST).build();
   10. }
   ```

   **方式一**：使用默认实现的请求客户端工具类。通过PetalPayConfig构建请求客户端对象示例如下：

   ```
   1. private static PetalPayClient payClient = new DefaultPetalPayClient(MercConfigUtil.getMercConfig());
   ```

   **方式二**：自定义实现请求客户端工具类。开发者如果需要自定义接口请求的client，用于处理请求中的日志打印等操作，可以通过继承PetalPayClient 来实现。示例如下：

   ```
   1. public class MercPetalPayClient extends PetalPayClient {
   2. public MercPetalPayClient(PetalPayConfig petalPayConfig) {
   3. super(petalPayConfig);
   4. }
   5. @Override
   6. public String doPost(String url, Map<String, String> headers, String requestBody) throws Exception {
   7. // todo
   8. }
   9. @Override
   10. public String doGet(String url, Map<String, String> headers, String requestBody) throws Exception {
   11. // todo
   12. }
   13. }
   ```

   说明

   * 需要使用最新开放的API接口，如示例代码未及时更新，未找到默认提供用于接口请求的对象信息，可直接调用PetalPayClient的execute方法构建接口请求。
   * 由于PetalPayClient.execute()方法及DefaultPetalPayClient实现涉及通过SecureRandom.getInstanceStrong()获取安全随机数，如果服务器熵值不足，可能会导致请求阻塞，以下处理方式可供参考：

     方式一：通过三方服务补充服务器熵值。以下为通过haveged服务补充熵值参考。

     ```
     1. # 查看熵值
     2. cat /proc/sys/kernel/random/entropy_avail
     3. # 安装haveged
     4. yum install haveged
     5. # 启动haveged
     6. systemctl start haveged.service
     7. # 开启haveged服务开机自启动
     8. systemctl enable haveged.service
     ```

     方式二：开发者参照DefaultPetalPayClient自定义实现请求客户端工具类并通过RequestConfig对象tranceId字段（建议每次请求都更新该字段）来主动传递tranceId，避免自动通过SecureRandom.getInstanceStrong()生成安全随机数导致请求阻塞。

     ```
     1. public <T> T execute(String httpMethod, String apiUrl, Class<T> rspType, RequestConfig requestConfig, Object requestObj) throws Exception;
     ```
2. 组装请求参数

   预下单请求参数组装示例如下：

   ```
   1. public static PreOrderCreateRequestV2 getPreOrderCreateRequestV2() {
   2. return PreOrderCreateRequestV2.builder()
   3. .mercOrderNo("pay-example-" + System.currentTimeMillis()) // 每次订单号都要变，请将pay-example-修改为商户自己的订单前缀
   4. .appId(MercConfigUtil.APP_ID)  // appId，需要配置为与商户绑定的正确的appId
   5. .mercNo(MercConfigUtil.MERC_NO) // 商户的商户号
   6. .tradeSummary("请修改为对应的商品简称") // 请修改为商品简称
   7. .totalAmount(2L)
   8. .callbackUrl("https://www.xxxxxx.com/hw/pay/callback") //回调通知地址，通知URL必须为直接可访问的URL，要求为https地址。最大长度为512。请替换为格式正确的结果通知回调地址。
   9. .build();
   10. }
   ```
3. 请求业务接口

   不同API接口调用URI不一样，详情请参见[API参考](../harmonyos-references/payment-prepay.md)文档。

   APP预下单请求示例如下：

   ```
   1. public CommonResponse aggrPreOrderForAppV2() {
   2. // 组装对象
   3. PreOrderCreateRequestV2 preOrderReq = getPreOrderCreateRequestV2();
   4. PreOrderCreateResponse response = null;
   5. try {
   6. response = payClient.execute("POST", "/api/v2/aggr/preorder/create/app", PreOrderCreateResponse.class,
   7. preOrderReq);
   8. } catch (Exception e) {
   9. // todo 异常处理
   10. log.error("request error ", e);
   11. return CommonResponse.buildErrorRsp(e.getMessage());
   12. }
   13. if (!validResponse(response)) {
   14. // todo 异常处理
   15. log.error("response is invalid ", response);
   16. return CommonResponse.buildFailRsp(response);
   17. }
   18. // 获取prepayId构建orderStr返回
   19. return CommonResponse.buildSuccessRsp(payClient.buildOrderStr(response.getPrepayId()));
   20. }
   21. public static boolean validResponse(BaseGwRspWithSign rsp) {
   22. return rsp != null && "000000".equals(rsp.getResultCode());
   23. }
   ```

## 通知回调处理

可使用VerifyTools.getCallbackResult方法自动处理回调结果验签并返回响应给华为支付服务器以及实现CallBackHandleInterface接口来处理回调结果。

通知回调处理示例如下：

```
1. public CallBackBaseResponse transactionResultNotify(@RequestBody Object callbackRequest) {
2. String callbackStr = JSONObject.toJSONString(callbackRequest);
3. return VerifyTools.getCallbackResult(callbackStr, MercConfigUtil.HW_PAY_PUBLIC_KEY_FOR_CALLBACK, new CallBackHandleInterface() {
4. @Override
5. public void fail(CallBackBaseResponse response, String reqString) {
6. // 未获取到字节流或者验签失败
7. // 商户自己业务处理
8. log.error("CallBack failed: ", response != null ? response.getResultCode() : null);
9. }
10. @Override
11. public void success(String reqString) {
12. NotifyPaymentReq callbackReq = JSONObject.parseObject(reqString, NotifyPaymentReq.class);
13. // 验签成功，商户自己业务处理
14. }
15. });
16. }
```

关于通知回调更多具体要求可参考[通知回调接口说明](../harmonyos-references/payment-rest-overview.md#通知回调接口说明)。

## 敏感信息处理

为了保证API接口请求通信过程中敏感信息字段（如用户的住址、银行卡号、手机号码等，涉及加密字段会在具体API接口中标注）的机密性，鸿蒙支付服务要求加密上送。 如开发者使用对应业务接口涉及字段加密，请联系华为侧工程师获取对应的SM2加密公钥（合作咨询可[点击此处](payment-service-support.md)）。

**涉及密钥**：

| 密钥类型 | 来源 | 作用 |
| --- | --- | --- |
| SM2 | 华为支付提供。 | 加密开发者生成的SM4密钥。 |
| SM4 | 开发者生成。 | 加密敏感信息字段。 |

**处理逻辑：**

1、开发者生成SM4对称密钥，用于加密敏感数据内容并作为入参传递给华为支付。

2、开发者使用华为支付提供的SM2密钥加密生成的SM4对称密钥并通过[PayMercAuth](../harmonyos-references/payment-model.md#paymercauth).sessionKey字段传递给华为支付用于解密敏感信息。

本质为SM4对称密钥加密，示例代码如下：

```
1. import com.huawei.petalpay.paymentservice.apiservice.client.model.MgmtSubmercRsp;
2. import com.huawei.petalpay.paymentservice.core.client.DefaultPetalPayClient;
3. import com.huawei.petalpay.paymentservice.core.client.PetalPayClient;
4. import com.huawei.petalpay.paymentservice.core.config.RequestConfig;
5. import com.huawei.petalpay.paymentservice.core.tools.SM4Util;
6. import com.huawei.petalpay.paymentservice.example.common.MercConfigUtil;

8. public class SignRegister {
9. public static void main(String[] args) {
10. PetalPayClient payClient = new DefaultPetalPayClient(MercConfigUtil.getMercConfig());
11. String sessionKey = SM4Util.getSM4GCMSessionKey();
12. String message = "xxxxxx";
13. RegisterSubmercReq req = new RegisterSubmercReq(SM4Util.getSM4GCMContent(sessionKey, message));
14. RequestConfig config = RequestConfig.builder()
15. .publicKeyForSessionKey(MercConfigUtil.HW_PUBLIC_KEY_FOR_SESSIONKEY)
16. .sessionKey(sessionKey)
17. .build();
18. try {
19. MgmtSubmercRsp response = payClient.execute("POST", "/api/v1/partner/mgmt/submerc/register",
20. MgmtSubmercRsp.class, config, req);
21. } catch (Exception e) {
22. // todo 异常处理
23. }
24. }
25. static class RegisterSubmercReq {
26. private String message;
27. public RegisterSubmercReq(String message) {
28. this.message = message;
29. }
30. }
31. }
```
