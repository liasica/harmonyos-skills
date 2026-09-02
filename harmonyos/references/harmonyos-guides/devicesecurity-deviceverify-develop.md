---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-develop
title: 应用设备状态检测
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 应用设备状态检测
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:30+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:18e7320f757283986698f218b27565b5602555ecbc96af0de079ff973984f6e7
---

## 场景介绍

应用通过调用Device Security Kit的getDeviceToken接口获取到DeviceToken，应用的服务器使用DeviceToken到Device Security服务器查询和管理应用在该设备的使用状态，应用在无法获取到持久化设备标识的情况下也可以对设备的应用状态进行记录和查询。

应用可以根据Device Security服务器返回的使用状态，判断应用是否在该设备上首次安装，或在该设备上用户是否已获取了优惠券等，以支撑业务进行新用户营销活动。

## 约束与限制

应用设备状态检测（DeviceVerify）能力不支持模拟器。支持设备：Phone、Tablet、PC/2in1、Wearable，从5.1.1(19)版本开始，新增支持TV设备。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Oevj-8LbQimH2Szg-k4gPQ/zh-cn_image_0000002706834284.png)

流程说明：

1. 开发者应用调用Device Security Kit的getDeviceToken接口获取DeviceToken。
2. Device Security Kit返回DeviceToken。
3. 开发者应用在业务请求（如领取优惠券请求）中把DeviceToken发送到应用的服务器。
4. 应用服务器发送DeviceVerify Rest请求到Device Security服务器，对该设备的标记状态（如是否已领取优惠券）进行查询（getDeviceStatus接口）和更新（setDeviceStatus接口）等操作。

   **说明** 

   Device Security服务器为每个设备的每个应用提供了2个bit的状态存储和查询能力，这2个bit的具体含义由应用自行定义。

   例如，可以使用bit 0来标识设备是否领取过新机礼包，bit0=false表示未领取，bit0=true表示已领取。用户在设备上领取新机礼包，应用服务器到Device Security服务器查询设备标记状态后，可根据bit0取值做相应处理。

   * 如果bit0=true，则表示该设备已经领取过了新机礼包，应用服务器可拒绝该设备继续领取新机礼包。
   * 如果bit0=false，则表示该设备未领取过新机礼包，应用服务器可向该设备的用户颁发新机礼包，并调用Device Security服务器的更新设备标记状态接口修改bit0为true。
5. Device Security服务器返回DeviceVerify响应。
6. 应用服务器根据Device Security服务器返回的响应进行相应的业务处理。
7. 应用服务器返回业务响应。

## 接口说明

以下是DeviceVerify相关接口，包括ArkTS API和REST API，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-deviceverify-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [getDeviceToken(): Promise<string>](../harmonyos-references/devicesecurity-deviceverify-api.md#devicecertificategetdevicetoken) | 获取本设备的DeviceToken |
| [checkDeviceToken](../harmonyos-references/devicesecurity-deviceverify-checkdevicetoken.md) | 验证deviceToken |
| [getDeviceStatus](../harmonyos-references/devicesecurity-deviceverify-getdevicestatus.md) | 查询设备标记状态 |
| [setDeviceStatus](../harmonyos-references/devicesecurity-deviceverify-updatedevicestatus.md) | 更新设备标记状态 |
| [delDeviceStatus](../harmonyos-references/devicesecurity-deviceverify-deletedevicestatus.md) | 删除设备标记状态 |

**注意** 

当getDeviceToken接口由于网络不稳定或其他原因无法获取到DeviceToken时，应用需要考虑异常处理方案，避免出现应用依赖DeviceToken的基本功能不可用。例如应用重新调用getDeviceToken接口或采用其他风控因子进行判断。

## 开发步骤

### 客户端开发

**说明** 

请确保已打开[“应用设备状态检测”开关](devicesecurity-deviceverify-activateservice.md)并[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。

1. 导入Device Security Kit模块及相关公共模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { deviceCertificate } from '@kit.DeviceSecurityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 获取设备deviceToken信息。

   ```typescript
   const TAG: string = '[DevCertManagerModel]';

   function deviceTokenPromise(): Promise<String> {
     return new Promise((resolve, reject) => {
       try {
         deviceCertificate.getDeviceToken().then((token) => {
           hilog.info(0x0000, TAG, 'Succeeded in executing getDeviceToken success');
           resolve(token);
         }).catch((err: BusinessError) => {
           hilog.error(0x0000, TAG, '%{public}s', 'getDeviceToken failed! err code: ' + err.code +
             ' ,err message: ' + err.message);
           reject(err);
         });
       } catch (err) {
         let error: BusinessError = err as BusinessError;
         hilog.error(0x0000, TAG, '%{public}s', 'getDeviceToken failed! catch err code: ' + error.code +
           ' ,err message: ' + error.message);
         reject(err);
       }
     });
   }
   ```

   **说明** 

   deviceToken由Device Security Kit加密生成，每次调用生成Token均不一样，有效期1小时。

### 服务端开发

1. 获取凭证Token，详情请参见[基于服务账号生成鉴权令牌](devicesecurity-deviceverify-token.md)。
2. 可分别调用checkDeviceToken、getDeviceStatus、setDeviceStatus、delDeviceStatus接口，实现deviceToken验证、查询设备标记状态、更新设备标记状态及删除设备标记状态功能。更多接口信息请参见[REST API](../harmonyos-references/devicesecurity-deviceverify-api.md)。

   样例代码：

   ```typescript
   import java.io.BufferedReader;
   import java.io.IOException;
   import java.io.InputStream;
   import java.io.InputStreamReader;
   import java.io.OutputStream;
   import java.net.HttpURLConnection;
   import java.net.URL;

   import com.alibaba.fastjson.JSONObject;

   public class DeviceTokenServer {
       // 使用应用设备状态检测功能获取的设备deviceToken
       static String deviceToken = "aes-gcm.gouLVEalfJxRLxt+3Gxh/orDAG9kDbkeFydkxGrDOHVJ3KEhiSDhIeW+/KH0ErqVxZ0vfkgtapaMu3yc0IND+lzC8ZH86NHxW+/GsqxYhvZ650TWUkanwdlZwYD0HPZ/KFnDPgIvGLvvWz1BdoPOOiFy5BuCQfGVNxl9OBTd7wsiJpl8kKywMRg/k1x61/8IpaH4F6tPrMV/Fv4N/WLfSHlC9AkB1ekZz4hxambDaXP8aXz59FYWItTl7tBOV09+JKnFqD0dB5ZmXjUhVLRKpYeGH8dPWG2gOmEksY6CsXvWBul+5HF76myfUeSvrWfD7Ee3+5Uuld3v+s8W+aFJkdUo8GSCF4xbiA+01BKnq0DIh0EKW/VJAQHjo/P/X/6jMwoDnbF7NWPmh827LHKQMIsN46zfke7qpdBsYpidKNxlXIb1azyAhD/izf5KQwkzwlVTctIvkUNH9XjTh1I6xb8yYb7TjZ7tnMGg2lWizNsejIcwAPqTTyXXupL5mPc8SwsZ424mDQhf1pCfacbZFaew0jWUC5ZQ2B8CiBeX";
       // 基于服务账号生成的鉴权令牌
       static String authorization = "Bearer eyJraWQiOiI5YTU5ZGRkZDZlYzY0MTgyYmUwMTc2MDNjZDU1YjEwNCIsInR5cCI6IkpXVCIsImFsZyI6IlBTMjU2In0.eyJhdWQiOiJodHRwczovL29hdXRoLWxvZ2luLmNsb3VkLmh1YXdlaS5jb20vb2F1dGgyL3YzL3Rva2VuIiwiaXNzIjoiMTE0MDIzMzQ1IiwiZXhwIjoxNzU0NDQ4NDU2LCJpYXQiOjE3NTQ0NDQ4NTZ9.cJEiLM53QBTSxzPjDAqK-HeteSv_qWxnAuEiwaN_udLQz78QZPcD54RFWSOqE459B0Y78hEL1-2eQlcCjbGn0OI2AQbwTwYzoRbLftAEyP5V9Juv1A-cfR8MoVapVdZ3pA9Jg6B5cBjcQLax-GTUJjevgI4PyTxQCIhLa-kaQq_h-KOnpcWlVUx2weLRAcGs4Tr3wYqdLnSPE7Hp_44C3S69dSoXoP8HL6-2L4aJzzvNn7uYoRiZAoCZoarJNHi7d8h9JEJ2K5vmaYV_lJ9l0_G4RDjpEmtCPOEkXLPIvjh5fwEBPyMZiUJqHyqTkdw8AjjgIaFe0wG9wCZk4sEo9GOruuy9tN6mEccFAEKbSf28gpUowWC23uKQPIYb9sdzrN8D3hpalrN5CDh1dv80wlhLxXeJOWWnfjCqYhA0m17UFC4xEhno-M52dEb4BODPsw-96xx02GX8_VqDDjjUmXEr6lwj4yLE_5feR1QFQS2NhC11Py4AzrsEPb9maFqR-bOUO2SfLdD1EjvMx2p-tELosFH8DmvwtbjNVYDN0zGEed150qhMtkDG9DUwT0dL3q_ikRq73syB9WbQrlpWeJAWBmazkb0EoSf24UO2rRjcZ0hGmgFIIH7AzHgw4Ok2ijCJ5uVIY59DUsXXUIBIH7tMyNUjrdZG0_ctDORrk_s";
       // Hap应用的包名
       static String bundleName = "com.huawei.myapplication.shoubiao412";

       public static void main(String[] args) throws IOException {
           checkDeviceToken();
           setDeviceStatus();
           getDeviceStatus();
           delDeviceStatus();
       }
       public static void checkDeviceToken() throws IOException {
           // 请求checkDeviceToken接口的地址
           String url = "https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/checkDeviceToken";
           URL obj = new URL(url);
           HttpURLConnection con = (HttpURLConnection) obj.openConnection();
           createRequestHeader(con);
           JSONObject postBody = createRequestBody();
           sendRequestAndReadResponse(con, postBody);
       }
       public static void getDeviceStatus() throws IOException {
           // 请求getDeviceStatus接口的地址
           String url = "https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/getDeviceStatus";
           URL obj = new URL(url);
           HttpURLConnection con = (HttpURLConnection) obj.openConnection();
           createRequestHeader(con);
           JSONObject postBody = createRequestBodyWithMode();
           sendRequestAndReadResponse(con, postBody);
       }
       public static void setDeviceStatus() throws IOException {
           // 请求setDeviceStatus接口的地址
           String url = "https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/setDeviceStatus";
           URL obj = new URL(url);
           HttpURLConnection con = (HttpURLConnection) obj.openConnection();
           createRequestHeader(con);
           JSONObject postBody = createRequestBodyWithBit();
           sendRequestAndReadResponse(con, postBody);
       }
       public static void delDeviceStatus() throws IOException {
           // 请求delDeviceStatus接口的地址
           String url = "https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/delDeviceStatus";
           URL obj = new URL(url);
           HttpURLConnection con = (HttpURLConnection) obj.openConnection();
           createRequestHeader(con);
           JSONObject postBody = createRequestBodyWithMode();
           sendRequestAndReadResponse(con, postBody);
       }
       public static JSONObject createRequestBody() {
           // 创建请求体
           JSONObject data = new JSONObject();
           data.put("deviceToken", deviceToken);
           // 可选，根据需要添加
           // data.put("transactionId", "xxx");
           // 应用服务器上的UTC时间
           data.put("timestamp", 1704038400000L);
           JSONObject postBody = new JSONObject();
           postBody.put("data", data);
           return postBody;
       }
       public static JSONObject createRequestBodyWithMode() {
           // 创建请求体
           JSONObject data = new JSONObject();
           // 设备标记状态的粒度。取值：1：应用级 2：开发者级
           data.put("mode", 1);
           data.put("deviceToken", deviceToken);
           // 可选，根据需要添加
           // data.put("transactionId", "xxx");
           // 应用服务器上的UTC时间
           data.put("timestamp", 1704038400000L);
           JSONObject postBody = new JSONObject();
           postBody.put("data", data);
           return postBody;
       }
       public static JSONObject createRequestBodyWithBit() {
           // 创建请求体
           JSONObject data = new JSONObject();
           // 设备标记状态的粒度。取值：1：应用级 2：开发者级
           data.put("mode", 1);
           data.put("deviceToken", deviceToken);
           // 可选，根据需要添加
           // data.put("transactionId", "xxx");
           // 应用服务器上的UTC时间
           data.put("timestamp", 1704038400000L);
           // 设备标记状态的第一位数据
           data.put("bit0", 1);
           // 设备标记状态的第二位数据
           data.put("bit1", 0);
           JSONObject postBody = new JSONObject();
           postBody.put("data", data);
           return postBody;
       }
       public static void createRequestHeader(HttpURLConnection con) throws IOException {
           con.setRequestMethod("POST");
           con.setDoOutput(true);

           // 设置请求头
           con.setRequestProperty("Content-Type", "application/json;charset=utf-8");
           con.setRequestProperty("Authorization", authorization);
           // 设置bundleName
           con.setRequestProperty("bundleName", bundleName);
       }
       public static void sendRequestAndReadResponse(HttpURLConnection con, JSONObject postBody) throws IOException {
           try (OutputStream os = con.getOutputStream()) {
               byte[] input = postBody.toString().getBytes("utf-8");
               os.write(input, 0, input.length);
           }
           // 读取响应码
           int responseCode = con.getResponseCode();
           System.out.println("Response Code: " + responseCode);

           InputStream stream;
           if (responseCode >= 200 && responseCode < 300) {
               stream = con.getInputStream();
           } else {
               // 获取错误信息
               stream = con.getErrorStream();
           }
           // 读取响应内容（无论是成功还是失败）
           StringBuilder response = new StringBuilder();
           String line;
           try (BufferedReader br = new BufferedReader(new InputStreamReader(stream, "utf-8"))) {
               while ((line = br.readLine()) != null) {
                   response.append(line);
               }
           } catch (Exception e) {
               System.out.println(e);
           }
           System.out.println("Response Content: " + response.toString());
       }
   }
   ```

**说明** 

1. 设备标记状态记录的存储期限为2年，存储期限从lastUpdateTime（最后一次更新时间）开始计算。
2. 开发者可以根据getDeviceStatus响应中的lastUpdateTime字段判断设备标记状态的有效期，例如开发者在5月份和6月份分别开展2个不同的优惠活动，可以根据lastUpdateTime字段判断用户已参加的优惠活动，比如lastUpdateTime为5月份，则表示用户参加了5月份的优惠活动。
