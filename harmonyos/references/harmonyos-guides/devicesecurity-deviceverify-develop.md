---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-develop
title: 应用设备状态检测
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 应用设备状态检测
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1c7bb44e76bbbf5d1af05197038afcf88f51a9995376911ade32998612df05a8
---

## 场景介绍

应用通过调用Device Security Kit的getDeviceToken接口获取到DeviceToken，应用的服务器使用DeviceToken到Device Security服务器查询和管理应用在该设备的使用状态，应用在无法获取到持久化设备标识的情况下也可以对设备的应用状态进行记录和查询。

应用可以根据Device Security服务器返回的使用状态，判断应用是否在该设备上首次安装，或在该设备上用户是否已获取了优惠券等，以支撑业务进行新用户营销活动。

## 约束与限制

应用设备状态检测（DeviceVerify）能力不支持模拟器。支持设备：Phone、Tablet、PC/2in1、Wearable，从5.1.1(19)版本开始，新增支持设备：TV。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/s2s-hfi-T7SBSOPhx3-EYw/zh-cn_image_0000002589244689.png?HW-CC-KV=V1&HW-CC-Date=20260429T053127Z&HW-CC-Expire=86400&HW-CC-Sign=3C542E740D8513DE52367CAFBD4D29DCB7416511CEEA53BACECA78C56F86EE72)

流程说明：

1. 开发者应用调用Device Security Kit的getDeviceToken接口获取DeviceToken。
2. Device Security Kit返回DeviceToken。
3. 开发者应用在业务请求（如领取优惠券请求）中把DeviceToken发送到应用的服务器。
4. 应用服务器发送DeviceVerify Rest请求到Device Security服务器，对该设备的标记状态（如是否已领取优惠券）进行查询（getDeviceStatus接口）和更新（setDeviceStatus接口）等操作。

   说明

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
| [getDeviceToken(): Promise<string>](../harmonyos-references/devicesecurity-deviceverify-api.md#getdevicetoken) | 获取本设备的DeviceToken |
| [checkDeviceToken](../harmonyos-references/devicesecurity-deviceverify-checkdevicetoken.md) | 验证deviceToken |
| [getDeviceStatus](../harmonyos-references/devicesecurity-deviceverify-getdevicestatus.md) | 查询设备标记状态 |
| [setDeviceStatus](../harmonyos-references/devicesecurity-deviceverify-updatedevicestatus.md) | 更新设备标记状态 |
| [delDeviceStatus](../harmonyos-references/devicesecurity-deviceverify-deletedevicestatus.md) | 删除设备标记状态 |

注意

当getDeviceToken接口由于网络不稳定或其他原因无法获取到DeviceToken时，应用需要考虑异常处理方案，避免出现应用依赖DeviceToken的基本功能不可用。例如应用重新调用getDeviceToken接口或采用其他风控因子进行判断。

## 开发步骤

### 客户端开发

说明

请确保已打开[“应用设备状态检测”开关](devicesecurity-deviceverify-activateservice.md)并[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。

1. 导入Device Security Kit模块及相关公共模块。

   ```
   1. import { deviceCertificate } from '@kit.DeviceSecurityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 获取设备deviceToken信息。

   ```
   1. const TAG = "DeviceCertificateJsTest";

   3. // 请求deviceToken，并处理结果
   4. try {
   5. deviceCertificate.getDeviceToken().then((token) => {
   6. hilog.info(0x0000, TAG, 'Succeeded in executing getDeviceToken');
   7. // 开发者处理deviceToken
   8. }).catch((err: BusinessError) => {
   9. hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', err.code, err.message);
   10. });
   11. } catch(err) {
   12. let error: BusinessError = err as BusinessError;
   13. hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', error.code, error.message);
   14. }
   ```

   说明

   deviceToken由Device Security Kit加密生成，每次调用生成Token均不一样，有效期1小时。

### 服务端开发

1. 获取凭证Token，详情请参见[基于服务账号生成鉴权令牌](devicesecurity-deviceverify-token.md)。
2. 可分别调用checkDeviceToken、getDeviceStatus、setDeviceStatus、delDeviceStatus接口，实现deviceToken验证、查询设备标记状态、更新设备标记状态及删除设备标记状态功能。更多接口信息请参见[REST API](../harmonyos-references/devicesecurity-deviceverify-api.md)。

   样例代码：

   ```
   1. import java.io.BufferedReader;
   2. import java.io.IOException;
   3. import java.io.InputStream;
   4. import java.io.InputStreamReader;
   5. import java.io.OutputStream;
   6. import java.net.HttpURLConnection;
   7. import java.net.URL;

   9. import com.alibaba.fastjson.JSONObject;

   11. public class DeviceTokenServer {
   12. // 使用应用设备状态检测功能获取的设备deviceToken
   13. static String deviceToken = "aes-gcm.gouLVEalfJxRLxt+3Gxh/orDAG9kDbkeFydkxGrDOHVJ3KEhiSDhIeW+/KH0ErqVxZ0vfkgtapaMu3yc0IND+lzC8ZH86NHxW+/GsqxYhvZ650TWUkanwdlZwYD0HPZ/KFnDPgIvGLvvWz1BdoPOOiFy5BuCQfGVNxl9OBTd7wsiJpl8kKywMRg/k1x61/8IpaH4F6tPrMV/Fv4N/WLfSHlC9AkB1ekZz4hxambDaXP8aXz59FYWItTl7tBOV09+JKnFqD0dB5ZmXjUhVLRKpYeGH8dPWG2gOmEksY6CsXvWBul+5HF76myfUeSvrWfD7Ee3+5Uuld3v+s8W+aFJkdUo8GSCF4xbiA+01BKnq0DIh0EKW/VJAQHjo/P/X/6jMwoDnbF7NWPmh827LHKQMIsN46zfke7qpdBsYpidKNxlXIb1azyAhD/izf5KQwkzwlVTctIvkUNH9XjTh1I6xb8yYb7TjZ7tnMGg2lWizNsejIcwAPqTTyXXupL5mPc8SwsZ424mDQhf1pCfacbZFaew0jWUC5ZQ2B8CiBeX";
   14. // 基于服务账号生成的鉴权令牌
   15. static String authorization = "Bearer eyJraWQiOiI5YTU5ZGRkZDZlYzY0MTgyYmUwMTc2MDNjZDU1YjEwNCIsInR5cCI6IkpXVCIsImFsZyI6IlBTMjU2In0.eyJhdWQiOiJodHRwczovL29hdXRoLWxvZ2luLmNsb3VkLmh1YXdlaS5jb20vb2F1dGgyL3YzL3Rva2VuIiwiaXNzIjoiMTE0MDIzMzQ1IiwiZXhwIjoxNzU0NDQ4NDU2LCJpYXQiOjE3NTQ0NDQ4NTZ9.cJEiLM53QBTSxzPjDAqK-HeteSv_qWxnAuEiwaN_udLQz78QZPcD54RFWSOqE459B0Y78hEL1-2eQlcCjbGn0OI2AQbwTwYzoRbLftAEyP5V9Juv1A-cfR8MoVapVdZ3pA9Jg6B5cBjcQLax-GTUJjevgI4PyTxQCIhLa-kaQq_h-KOnpcWlVUx2weLRAcGs4Tr3wYqdLnSPE7Hp_44C3S69dSoXoP8HL6-2L4aJzzvNn7uYoRiZAoCZoarJNHi7d8h9JEJ2K5vmaYV_lJ9l0_G4RDjpEmtCPOEkXLPIvjh5fwEBPyMZiUJqHyqTkdw8AjjgIaFe0wG9wCZk4sEo9GOruuy9tN6mEccFAEKbSf28gpUowWC23uKQPIYb9sdzrN8D3hpalrN5CDh1dv80wlhLxXeJOWWnfjCqYhA0m17UFC4xEhno-M52dEb4BODPsw-96xx02GX8_VqDDjjUmXEr6lwj4yLE_5feR1QFQS2NhC11Py4AzrsEPb9maFqR-bOUO2SfLdD1EjvMx2p-tELosFH8DmvwtbjNVYDN0zGEed150qhMtkDG9DUwT0dL3q_ikRq73syB9WbQrlpWeJAWBmazkb0EoSf24UO2rRjcZ0hGmgFIIH7AzHgw4Ok2ijCJ5uVIY59DUsXXUIBIH7tMyNUjrdZG0_ctDORrk_s";
   16. // Hap应用的包名
   17. static String bundleName = "com.huawei.myapplication.shoubiao412";

   19. public static void main(String[] args) throws IOException {
   20. checkDeviceToken();
   21. setDeviceStatus();
   22. getDeviceStatus();
   23. delDeviceStatus();
   24. }
   25. public static void checkDeviceToken() throws IOException {
   26. // 请求checkDeviceToken接口的地址
   27. String url = "https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/checkDeviceToken";
   28. URL obj = new URL(url);
   29. HttpURLConnection con = (HttpURLConnection) obj.openConnection();
   30. createRequestHeader(con);
   31. JSONObject postBody = createRequestBody();
   32. sendRequestAndReadResponse(con, postBody);
   33. }
   34. public static void getDeviceStatus() throws IOException {
   35. // 请求getDeviceStatus接口的地址
   36. String url = "https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/getDeviceStatus";
   37. URL obj = new URL(url);
   38. HttpURLConnection con = (HttpURLConnection) obj.openConnection();
   39. createRequestHeader(con);
   40. JSONObject postBody = createRequestBodyWithMode();
   41. sendRequestAndReadResponse(con, postBody);
   42. }
   43. public static void setDeviceStatus() throws IOException {
   44. // 请求setDeviceStatus接口的地址
   45. String url = "https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/setDeviceStatus";
   46. URL obj = new URL(url);
   47. HttpURLConnection con = (HttpURLConnection) obj.openConnection();
   48. createRequestHeader(con);
   49. JSONObject postBody = createRequestBodyWithBit();
   50. sendRequestAndReadResponse(con, postBody);
   51. }
   52. public static void delDeviceStatus() throws IOException {
   53. // 请求delDeviceStatus接口的地址
   54. String url = "https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/delDeviceStatus";
   55. URL obj = new URL(url);
   56. HttpURLConnection con = (HttpURLConnection) obj.openConnection();
   57. createRequestHeader(con);
   58. JSONObject postBody = createRequestBodyWithMode();
   59. sendRequestAndReadResponse(con, postBody);
   60. }
   61. public static JSONObject createRequestBody() {
   62. // 创建请求体
   63. JSONObject data = new JSONObject();
   64. data.put("deviceToken", deviceToken);
   65. // 可选，根据需要添加
   66. // data.put("transactionId", "xxx");
   67. // 应用服务器上的UTC时间
   68. data.put("timestamp", 1704038400000L);
   69. JSONObject postBody = new JSONObject();
   70. postBody.put("data", data);
   71. return postBody;
   72. }
   73. public static JSONObject createRequestBodyWithMode() {
   74. // 创建请求体
   75. JSONObject data = new JSONObject();
   76. // 设备标记状态的粒度。取值：1：应用级 2：开发者级
   77. data.put("mode", 1);
   78. data.put("deviceToken", deviceToken);
   79. // 可选，根据需要添加
   80. // data.put("transactionId", "xxx");
   81. // 应用服务器上的UTC时间
   82. data.put("timestamp", 1704038400000L);
   83. JSONObject postBody = new JSONObject();
   84. postBody.put("data", data);
   85. return postBody;
   86. }
   87. public static JSONObject createRequestBodyWithBit() {
   88. // 创建请求体
   89. JSONObject data = new JSONObject();
   90. // 设备标记状态的粒度。取值：1：应用级 2：开发者级
   91. data.put("mode", 1);
   92. data.put("deviceToken", deviceToken);
   93. // 可选，根据需要添加
   94. // data.put("transactionId", "xxx");
   95. // 应用服务器上的UTC时间
   96. data.put("timestamp", 1704038400000L);
   97. // 设备标记状态的第一位数据
   98. data.put("bit0", 1);
   99. // 设备标记状态的第二位数据
   100. data.put("bit1", 0);
   101. JSONObject postBody = new JSONObject();
   102. postBody.put("data", data);
   103. return postBody;
   104. }
   105. public static void createRequestHeader(HttpURLConnection con) throws IOException {
   106. con.setRequestMethod("POST");
   107. con.setDoOutput(true);

   109. // 设置请求头
   110. con.setRequestProperty("Content-Type", "application/json;charset=utf-8");
   111. con.setRequestProperty("Authorization", authorization);
   112. // 设置bundleName
   113. con.setRequestProperty("bundleName", bundleName);
   114. }
   115. public static void sendRequestAndReadResponse(HttpURLConnection con, JSONObject postBody) throws IOException {
   116. try (OutputStream os = con.getOutputStream()) {
   117. byte[] input = postBody.toString().getBytes("utf-8");
   118. os.write(input, 0, input.length);
   119. }
   120. // 读取响应码
   121. int responseCode = con.getResponseCode();
   122. System.out.println("Response Code: " + responseCode);

   124. InputStream stream;
   125. if (responseCode >= 200 && responseCode < 300) {
   126. stream = con.getInputStream();
   127. } else {
   128. // 获取错误信息
   129. stream = con.getErrorStream();
   130. }
   131. // 读取响应内容（无论是成功还是失败）
   132. StringBuilder response = new StringBuilder();
   133. String line;
   134. try (BufferedReader br = new BufferedReader(new InputStreamReader(stream, "utf-8"))) {
   135. while ((line = br.readLine()) != null) {
   136. response.append(line);
   137. }
   138. } catch (Exception e) {
   139. System.out.println(e);
   140. }
   141. System.out.println("Response Content: " + response.toString());
   142. }
   143. }
   ```

说明

1. 设备标记状态记录的存储期限为2年，存储期限从lastUpdateTime（最后一次更新时间）开始计算。
2. 开发者可以根据getDeviceStatus响应中的lastUpdateTime字段判断设备标记状态的有效期，例如开发者在5月份和6月份分别开展2个不同的优惠活动，可以根据lastUpdateTime字段判断用户已参加的优惠活动，比如lastUpdateTime为5月份，则表示用户参加了5月份的优惠活动。
