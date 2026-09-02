---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-server-connect
title: 云侧服务准备
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > 云侧服务准备
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:59+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:2290a1f6db76a22150472a19800445e22347a0d50a0393fca33fd8883bcfcdcf
---

Payment Kit服务提供了支付系统相关的一系列API接口。为减少API接口的接入工作量，提供了相应java版本的Maven依赖用于云侧服务对接。

开发者可通过Maven集成来完成服务器开发环境的构建，以此来快速使用华为支付提供的API接口。

可下载[示例代码-服务端](https://gitcode.com/HarmonyOS_Samples/paymentkit-sample-code-serverdemo-java)用以快速完成商户服务器接入。

**说明** 

因业务发展需要，API接口响应、通知回调请求字段可能会发生变动，如开发者自行实现验签逻辑，一定要使用原始的字符串转为Map对象进行验签处理后再转换成自定义的业务对象去使用，以确保验签正常通过。

## 约束与限制

商户使用提供的示例代码接入华为支付前请确保网络已正常连接，可以从华为支付仓库地址正常拉取Maven依赖。

开发环境：[JDK](https://www.oracle.com/java/technologies/javase-downloads.html) 1.8及以上。

## 集成Maven依赖

在示例代码pom.xml文件中已配置仓库地址，如无法正常拉取依赖，可在Maven配置文件“settings.xml”中添加华为支付的Maven仓库地址。

```xml
<mirror>
  <id>central</id>
  <mirrorOf>central</mirrorOf>
  <url>https://developer.huawei.com/repo/</url>
</mirror>
```

在示例代码pom.xml文件中已引入jar包的Maven坐标。如商户自己构建工程则需在pom.xml文件中引入如下坐标：

```xml
<dependency>
  <groupId>com.huawei.petalpay</groupId>
  <artifactId>pay-java</artifactId>
  <version>1.0.0.331</version>
</dependency>
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

```shell
# 商户号
PETALPAY.MERC_NO=121540000***
# 商户私钥
PETALPAY.MERC_PRIVATE_KEY=MIIJQwIBADAN=9w0BAQEFAASCCS0wg******************************CldcDlDCSsdfDceCSDr+RyvJdfcXssdEA=
# 商户证书ID
PETALPAY.MERC_AUTH_ID=101540200089***
# 商户私钥签名类型
PETALPAY.SIGN_TYPE=RSA
# 鸿蒙支付服务域名
PETALPAY.SERVER_HOST=https://petalpay-developer.cloud.huawei.com.cn
# 鸿蒙支付服务验签公钥
PETALPAY.HW_PAY_PUBLIC_KEY_FOR_CALLBACK=6D015316F09CB747E4467******************************DB46DA4BD0960ADD500D84912
# 鸿蒙支付服务加密公钥（非必选）
PETALPAY.HW_PUBLIC_KEY_FOR_SESSIONKEY=042A7D32FA19C29D3E722D6C4ACAC0B******************************E5A5B1C8120DAC9882E4B093B9CE7A38296F87F41747D319A
# 商户号关联的APPID
PETALPAY.APPID=111831***
```

## 业务接口请求

1. 获取发起请求客户端对象

   可通过工具类MercConfigUtil提供的方法getMercConfig快速获取PetalPayConfig对象来构建请求客户端，对应配置项获取及配置参见[配置初始化](payment-server-connect.md#配置初始化)。

   ```java
   // 商户配置
   public static PetalPayConfig getMercConfig() {
       return PetalPayConfig.builder().callerId(MERC_NO) // （必填）商户号
           .appId(APP_ID) // （必填）商户号关联的APPID
           .privateKey(MERC_PRIVATE_KEY) // （必填）商户私钥
           .authId(MERC_AUTH_ID) // （必填）商户证书ID
           .signType(SIGN_TYPE) // （选填）商户公私钥类型，默认RSA加密
           .petalpayPublicKey(HW_PAY_PUBLIC_KEY_FOR_CALLBACK) // （非必填）验签公钥(和接口级配置needVerifyRsp对应，公钥和商户通知回调验签公钥同一个)
           .domainHost(SERVER_HOST).build();
   }
   ```

   **方式一**：使用默认实现的请求客户端工具类。通过PetalPayConfig构建请求客户端对象示例如下：

   ```java
   private static PetalPayClient payClient = new DefaultPetalPayClient(MercConfigUtil.getMercConfig());
   ```

   **方式二**：自定义实现请求客户端工具类。开发者如果需要自定义接口请求的client，用于处理请求中的日志打印等操作，可以通过继承PetalPayClient 来实现。示例如下：

   ```java
   public class MercPetalPayClient extends PetalPayClient {
       public MercPetalPayClient(PetalPayConfig petalPayConfig) {
           super(petalPayConfig);
       }
       @Override
       public String doPost(String url, Map<String, String> headers, String requestBody) throws Exception {
           // 开发者业务侧post请求实现
       }
       @Override
       public String doGet(String url, Map<String, String> headers, String requestBody) throws Exception {
           // 开发者业务侧get请求实现
       }
   }
   ```

   **说明** 

   * 需要使用最新开放的API接口，如示例代码未及时更新，未找到默认提供用于接口请求的对象信息，可直接调用PetalPayClient的execute方法构建接口请求。
   * 由于PetalPayClient.execute()方法及DefaultPetalPayClient实现涉及通过SecureRandom.getInstanceStrong()获取安全随机数，如果服务器熵值不足，可能会导致请求阻塞，以下处理方式可供参考：

     方式一：通过三方服务补充服务器熵值。以下为通过haveged服务补充熵值参考。

     ```shell
     # 查看熵值
     cat /proc/sys/kernel/random/entropy_avail
     # 安装haveged
     yum install haveged
     # 启动haveged
     systemctl start haveged.service
     # 开启haveged服务开机自启动
     systemctl enable haveged.service
     ```

     方式二：开发者参照DefaultPetalPayClient自定义实现请求客户端工具类并通过RequestConfig对象tranceId字段（建议每次请求都更新该字段）来主动传递tranceId，避免自动通过SecureRandom.getInstanceStrong()生成安全随机数导致请求阻塞。

     ```java
     public <T> T execute(String httpMethod, String apiUrl, Class<T> rspType, RequestConfig requestConfig, Object requestObj) throws Exception;
     ```
2. 组装请求参数

   预下单请求参数组装示例如下：

   ```java
   public static PreOrderCreateRequestV2 getPreOrderCreateRequestV2() {
       return PreOrderCreateRequestV2.builder()
           .mercOrderNo("pay-example-" + System.currentTimeMillis()) // 每次订单号都要变，请将pay-example-修改为商户自己的订单前缀
           .appId(MercConfigUtil.APP_ID)  // appId，需要配置为与商户绑定的正确的appId
           .mercNo(MercConfigUtil.MERC_NO) // 商户的商户号
           .tradeSummary("请修改为对应的商品简称") // 请修改为商品简称
           .totalAmount(2L)
           .callbackUrl("https://www.xxxxxx.com/hw/pay/callback") //回调通知地址，通知URL必须为直接可访问的URL，要求为https地址。最大长度为512。请替换为格式正确的结果通知回调地址。
           .build();
   }
   ```
3. 请求业务接口

   不同API接口调用URI不一样，详情请参见[API参考](../harmonyos-references/payment-prepay.md)文档。

   APP预下单请求示例如下：

   ```java
   public CommonResponse aggrPreOrderForAppV2() {
       // 组装对象
       PreOrderCreateRequestV2 preOrderReq = getPreOrderCreateRequestV2();
       PreOrderCreateResponse response = null;
       try {
           response = payClient.execute("POST", "/api/v2/aggr/preorder/create/app", PreOrderCreateResponse.class,
               preOrderReq);
       } catch (Exception e) {
           // todo 异常处理
           log.error("request error ", e);
           return CommonResponse.buildErrorRsp(e.getMessage());
       }
       if (!validResponse(response)) {
           // todo 异常处理
           log.error("response is invalid ", response);
           return CommonResponse.buildFailRsp(response);
       }
       // 获取prepayId构建orderStr返回
       return CommonResponse.buildSuccessRsp(payClient.buildOrderStr(response.getPrepayId()));
   }
   public static boolean validResponse(BaseGwRspWithSign rsp) {
       return rsp != null && "000000".equals(rsp.getResultCode());
   }
   ```

## 通知回调处理

可使用VerifyTools.getCallbackResult方法自动处理回调结果验签并返回响应给华为支付服务器以及实现CallBackHandleInterface接口来处理回调结果。

通知回调处理示例如下：

```java
public CallBackBaseResponse transactionResultNotify(@RequestBody Object callbackRequest) {
    String callbackStr = JSONObject.toJSONString(callbackRequest);
    return VerifyTools.getCallbackResult(callbackStr, MercConfigUtil.HW_PAY_PUBLIC_KEY_FOR_CALLBACK, new CallBackHandleInterface() {
        @Override
         public void fail(CallBackBaseResponse response, String reqString) {
              // 未获取到字节流或者验签失败
              // 商户自己业务处理
              log.error("CallBack failed: ", response != null ? response.getResultCode() : null);
         }
         @Override
         public void success(String reqString) {
              NotifyPaymentReq callbackReq = JSONObject.parseObject(reqString, NotifyPaymentReq.class);
              // 验签成功，商户自己业务处理
         }
    });
}
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

```java
import com.huawei.petalpay.paymentservice.apiservice.client.model.MgmtSubmercRsp;
import com.huawei.petalpay.paymentservice.core.client.DefaultPetalPayClient;
import com.huawei.petalpay.paymentservice.core.client.PetalPayClient;
import com.huawei.petalpay.paymentservice.core.config.RequestConfig;
import com.huawei.petalpay.paymentservice.core.tools.SM4Util;
import com.huawei.petalpay.paymentservice.example.common.MercConfigUtil;

public class SignRegister {
    public static void main(String[] args) {
        PetalPayClient payClient = new DefaultPetalPayClient(MercConfigUtil.getMercConfig());
        String sessionKey = SM4Util.getSM4GCMSessionKey();
        String message = "xxxxxx";
        RegisterSubmercReq req = new RegisterSubmercReq(SM4Util.getSM4GCMContent(sessionKey, message));
        RequestConfig config = RequestConfig.builder()
            .publicKeyForSessionKey(MercConfigUtil.HW_PUBLIC_KEY_FOR_SESSIONKEY)
            .sessionKey(sessionKey)
            .build();
        try {
            MgmtSubmercRsp response = payClient.execute("POST", "/api/v1/partner/mgmt/submerc/register",
                MgmtSubmercRsp.class, config, req);
        } catch (Exception e) {
            // todo 异常处理
        }
    }
    static class RegisterSubmercReq {
        private String message;
        public RegisterSubmercReq(String message) {
            this.message = message;
        }
    }
}
```
