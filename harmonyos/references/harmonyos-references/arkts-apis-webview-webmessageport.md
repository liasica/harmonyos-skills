---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport
title: Interface (WebMessagePort)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Interface (WebMessagePort)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:12+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:e9d2437af47d449594681facae2533d339d7ee8c0e26308d3aa66f30433b7544
---

通过WebMessagePort可以进行消息的发送以及接收，发送[WebMessageType](arkts-apis-webview-e.md#webmessagetype10)/[WebMessage](arkts-apis-webview-t.md#webmessage)类型消息给HTML5侧。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Interface首批接口从API version 9开始支持。
* 示例效果请以真机运行为准。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isExtentionType10+ | boolean | 否 | 是 | 创建WebMessagePort时是否指定使用扩展增强接口，[postMessageEventExt](arkts-apis-webview-webmessageport.md#postmessageeventext10)、[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。  true表示使用扩展增强接口，false表示不使用扩展增强接口。  默认值：false。 |

## postMessageEvent

PhonePC/2in1TabletTVWearable

postMessageEvent(message: WebMessage): void

发送[WebMessage](arkts-apis-webview-t.md#webmessage)类型消息给HTML5侧，必须先调用[onMessageEvent](arkts-apis-webview-webmessageport.md#onmessageevent)，否则会发送失败。完整示例代码参考[postMessage](arkts-apis-webview-webviewcontroller.md#postmessage)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | [WebMessage](arkts-apis-webview-t.md#webmessage) | 是 | 要发送的消息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100010 | Failed to post messages through the port. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. ports: webview.WebMessagePort[] = [];

11. build() {
12. Column() {
13. Button('postMessageEvent')
14. .onClick(() => {
15. try {
16. this.ports = this.controller.createWebMessagePorts();
17. this.controller.postMessage('__init_port__', [this.ports[0]], '*');
18. this.ports[1].postMessageEvent("post message from ets to html5");
19. } catch (error) {
20. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
21. }
22. })
23. Web({ src: 'www.example.com', controller: this.controller })
24. }
25. }
26. }
```

## onMessageEvent

PhonePC/2in1TabletTVWearable

onMessageEvent(callback: (result: WebMessage) => void): void

在应用侧的消息端口上注册回调函数，接收HTML5侧发送过来的[WebMessage](arkts-apis-webview-t.md#webmessage)类型消息。完整示例代码参考[postMessage](arkts-apis-webview-webviewcontroller.md#postmessage)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (result: [WebMessage](arkts-apis-webview-t.md#webmessage)) => void | 是 | 接收到的消息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100006 | Failed to register a message event for the port. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. ports: webview.WebMessagePort[] = [];

11. build() {
12. Column() {
13. Button('onMessageEvent')
14. .onClick(() => {
15. try {
16. this.ports = this.controller.createWebMessagePorts();
17. this.ports[1].onMessageEvent((msg) => {
18. if (typeof (msg) == "string") {
19. console.info("received string message from html5, string is:" + msg);
20. } else if (typeof (msg) == "object") {
21. if (msg instanceof ArrayBuffer) {
22. console.info("received arraybuffer from html5, length is:" + msg.byteLength);
23. } else {
24. console.info("not support");
25. }
26. } else {
27. console.info("not support");
28. }
29. })
30. } catch (error) {
31. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
32. }
33. })
34. Web({ src: 'www.example.com', controller: this.controller })
35. }
36. }
37. }
```

## postMessageEventExt10+

PhonePC/2in1TabletTVWearable

postMessageEventExt(message: WebMessageExt): void

发送[WebMessageType](arkts-apis-webview-e.md#webmessagetype10)类型消息给HTML5侧，必须先调用[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)，否则会发送失败。完整示例代码参考[onMessageEventExt](arkts-apis-webview-webmessageport.md#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | [WebMessageExt](arkts-apis-webview-webmessageext.md) | 是 | 要发送的消息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100010 | Failed to post messages through the port. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

## onMessageEventExt10+

PhonePC/2in1TabletTVWearable

onMessageEventExt(callback: (result: WebMessageExt) => void): void

在应用侧的消息端口上注册回调函数，接收HTML5侧发送过来的[WebMessageType](arkts-apis-webview-e.md#webmessagetype10)类型消息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (result: [WebMessageExt](arkts-apis-webview-webmessageext.md)) => void | 是 | 接收到的消息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100006 | Failed to register a message event for the port. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestObj {
6. test(str: string): ArrayBuffer {
7. let buf = new ArrayBuffer(str.length);
8. let buff = new Uint8Array(buf);

10. for (let i = 0; i < str.length; i++) {
11. buff[i] = str.charCodeAt(i);
12. }
13. return buf;
14. }
15. }

17. // 应用与网页互发消息的示例：使用"init_web_messageport"的通道，通过端口0在应用侧接收网页发送的消息，通过端口1在网页侧接收应用发送的消息。
18. @Entry
19. @Component
20. struct WebComponent {
21. controller: webview.WebviewController = new webview.WebviewController();
22. ports: webview.WebMessagePort[] = [];
23. nativePort: webview.WebMessagePort | null = null;
24. @State msg1: string = "";
25. @State msg2: string = "";
26. message: webview.WebMessageExt = new webview.WebMessageExt();
27. @State testObjtest: TestObj = new TestObj();

29. build() {
30. Column() {
31. Text(this.msg1).fontSize(16)
32. Text(this.msg2).fontSize(16)
33. Button('SendToH5 setString').margin({
34. right: 800,
35. })
36. .onClick(() => {
37. // 使用本侧端口发送消息给HTML5
38. try {
39. console.info("In ArkTS side send true start");
40. if (this.nativePort) {
41. this.message.setType(1);
42. this.message.setString("helloFromEts");
43. this.nativePort.postMessageEventExt(this.message);
44. }
45. }
46. catch (error) {
47. console.error(`In ArkTS side send message catch error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
48. }
49. })
50. Button('SendToH5 setNumber').margin({
51. top: 10,
52. right: 800,
53. })
54. .onClick(() => {
55. // 使用本侧端口发送消息给HTML5
56. try {
57. console.info("In ArkTS side send true start");
58. if (this.nativePort) {
59. this.message.setType(2);
60. this.message.setNumber(12345);
61. this.nativePort.postMessageEventExt(this.message);
62. }
63. }
64. catch (error) {
65. console.error(`In ArkTS side send message catch error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
66. }
67. })
68. Button('SendToH5 setBoolean').margin({
69. top: -90,
70. })
71. .onClick(() => {
72. // 使用本侧端口发送消息给HTML5
73. try {
74. console.info("In ArkTS side send true start");
75. if (this.nativePort) {
76. this.message.setType(3);
77. this.message.setBoolean(true);
78. this.nativePort.postMessageEventExt(this.message);
79. }
80. }
81. catch (error) {
82. console.error(`In ArkTS side send message catch error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
83. }
84. })
85. Button('SendToH5 setArrayBuffer').margin({
86. top: 10,
87. })
88. .onClick(() => {
89. // 使用本侧端口发送消息给HTML5
90. try {
91. console.info("In ArkTS side send true start");
92. if (this.nativePort) {
93. this.message.setType(4);
94. this.message.setArrayBuffer(this.testObjtest.test("Name=test&Password=test"));
95. this.nativePort.postMessageEventExt(this.message);
96. }
97. }
98. catch (error) {
99. console.error(`In ArkTS side send message catch error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
100. }
101. })
102. Button('SendToH5 setArray').margin({
103. top: -90,
104. left: 800,
105. })
106. .onClick(() => {
107. // 使用本侧端口发送消息给HTML5
108. try {
109. console.info("In ArkTS side send true start");
110. if (this.nativePort) {
111. this.message.setType(5);
112. this.message.setArray([1, 2, 3]);
113. this.nativePort.postMessageEventExt(this.message);
114. }
115. }
116. catch (error) {
117. console.error(`In ArkTS side send message catch error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
118. }
119. })
120. Button('SendToH5 setError').margin({
121. top: 10,
122. left: 800,
123. })
124. .onClick(() => {
125. // 使用本侧端口发送消息给HTML5
126. try {
127. console.info("In ArkTS side send true start");
128. throw new ReferenceError("ReferenceError");
129. }
130. catch (error) {
131. if (this.nativePort) {
132. this.message.setType(6);
133. this.message.setError(error);
134. this.nativePort.postMessageEventExt(this.message);
135. }
136. console.error(`In ArkTS side send message catch error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
137. }
138. })

140. Web({ src: $rawfile('index.html'), controller: this.controller })
141. .onPageEnd(() => {
142. console.info("In ArkTS side message onPageEnd init message channel");
143. // 1. 创建消息端口
144. this.ports = this.controller.createWebMessagePorts(true);
145. // 2. 发送端口1到HTML5
146. this.controller.postMessage("init_web_messageport", [this.ports[1]], "*");
147. // 3. 保存端口0到本地
148. this.nativePort = this.ports[0];
149. // 4. 设置回调函数
150. this.nativePort.onMessageEventExt((result) => {
151. console.info("In ArkTS side got message");
152. try {
153. let type = result.getType();
154. console.info("In ArkTS side getType:" + type);
155. switch (type) {
156. case webview.WebMessageType.STRING: {
157. this.msg1 = "result type:" + typeof (result.getString());
158. this.msg2 = "result getString:" + ((result.getString()));
159. break;
160. }
161. case webview.WebMessageType.NUMBER: {
162. this.msg1 = "result type:" + typeof (result.getNumber());
163. this.msg2 = "result getNumber:" + ((result.getNumber()));
164. break;
165. }
166. case webview.WebMessageType.BOOLEAN: {
167. this.msg1 = "result type:" + typeof (result.getBoolean());
168. this.msg2 = "result getBoolean:" + ((result.getBoolean()));
169. break;
170. }
171. case webview.WebMessageType.ARRAY_BUFFER: {
172. this.msg1 = "result type:" + typeof (result.getArrayBuffer());
173. this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
174. break;
175. }
176. case webview.WebMessageType.ARRAY: {
177. this.msg1 = "result type:" + typeof (result.getArray());
178. this.msg2 = "result getArray:" + result.getArray();
179. break;
180. }
181. case webview.WebMessageType.ERROR: {
182. this.msg1 = "result type:" + typeof (result.getError());
183. this.msg2 = "result getError:" + result.getError();
184. break;
185. }
186. default: {
187. this.msg1 = "default break, type:" + type;
188. break;
189. }
190. }
191. }
192. catch (error) {
193. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
194. }
195. });
196. })
197. }
198. }
199. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html lang="en-gb">
4. <head>
5. <title>WebView MessagePort Demo</title>
6. </head>

8. <body>
9. <h1>Html5 Send and Receive Message</h1>
10. <h3 id="msg">Receive string:</h3>
11. <h3 id="msg2">Receive arraybuffer:</h3>
12. <div style="font-size: 10pt; text-align: center;">
13. <input type="button" value="Send String" onclick="postStringToApp();" /><br/>
14. </div>
15. </body>
16. <script src="index.js"></script>
17. </html>
```

```
1. //index.js
2. var h5Port;
3. window.addEventListener('message', function(event) {
4. if (event.data == 'init_web_messageport') {
5. if(event.ports[0] != null) {
6. h5Port = event.ports[0]; // 1. 保存从ets侧发送过来的端口
7. h5Port.onmessage = function(event) {
8. console.info("hwd In html got message");
9. // 2. 接收ets侧发送过来的消息.
10. var result = event.data;
11. console.info("In html got message, typeof: ", typeof(result));
12. console.info("In html got message, result: ", (result));
13. if (typeof(result) == "string") {
14. console.info("In html got message, String: ", result);
15. document.getElementById("msg").innerHTML  =  "String:" + result;
16. } else if (typeof(result) == "number") {
17. console.info("In html side got message, number: ", result);
18. document.getElementById("msg").innerHTML = "Number:" + result;
19. } else if (typeof(result) == "boolean") {
20. console.info("In html side got message, boolean: ", result);
21. document.getElementById("msg").innerHTML = "Boolean:" + result;
22. } else if (typeof(result) == "object") {
23. if (result instanceof ArrayBuffer) {
24. document.getElementById("msg2").innerHTML  =  "ArrayBuffer:" + result.byteLength;
25. console.info("In html got message, byteLength: ", result.byteLength);
26. } else if (result instanceof Error) {
27. console.info("In html error message, err:" + (result));
28. console.info("In html error message, typeof err:" + typeof(result));
29. document.getElementById("msg2").innerHTML  =  "Error:" + result.name + ", msg:" + result.message;
30. } else if (result instanceof Array) {
31. console.info("In html got message, Array");
32. console.info("In html got message, Array length:" + result.length);
33. console.info("In html got message, Array[0]:" + (result[0]));
34. console.info("In html got message, typeof Array[0]:" + typeof(result[0]));
35. document.getElementById("msg2").innerHTML  =  "Array len:" + result.length + ", value:" + result;
36. } else {
37. console.info("In html got message, not any instance of support type");
38. document.getElementById("msg").innerHTML  = "not any instance of support type";
39. }
40. } else {
41. console.info("In html got message, not support type");
42. document.getElementById("msg").innerHTML  = "not support type";
43. }
44. }
45. h5Port.onmessageerror = (event) => {
46. console.error(`hwd In html Error receiving message: ${event}`);
47. };
48. }
49. }
50. })

52. // 使用h5Port往ets侧发送String类型的消息.
53. function postStringToApp() {
54. if (h5Port) {
55. console.info("In html send string message");
56. h5Port.postMessage("hello");
57. console.info("In html send string message end");
58. } else {
59. console.error("In html h5port is null, please init first");
60. }
61. }
```

## close

PhonePC/2in1TabletTVWearable

close(): void

不需要发送消息时关闭该消息端口。在使用close前，请先使用[createWebMessagePorts](arkts-apis-webview-webviewcontroller.md#createwebmessageports)创建消息端口。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. msgPort: webview.WebMessagePort[] = [];

11. build() {
12. Column() {
13. // 先使用createWebMessagePorts创建端口。
14. Button('createWebMessagePorts')
15. .onClick(() => {
16. try {
17. this.msgPort = this.controller.createWebMessagePorts();
18. console.info("createWebMessagePorts size:" + this.msgPort.length)
19. } catch (error) {
20. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
21. }
22. })
23. Button('close')
24. .onClick(() => {
25. try {
26. if (this.msgPort && this.msgPort.length == 2) {
27. this.msgPort[1].close();
28. this.msgPort = [];
29. } else {
30. console.error("msgPort is null, Please initialize first");
31. }
32. } catch (error) {
33. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
34. }
35. })
36. Web({ src: 'www.example.com', controller: this.controller })
37. }
38. }
39. }
```
