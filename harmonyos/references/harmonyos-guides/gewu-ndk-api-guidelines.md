---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gewu-ndk-api-guidelines
title: 格物开发指导
breadcrumb: 指南 > NDK开发 > 代码开发 > 线程调度 > 格物开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0ae1a807d3df8963f47bd7255012c680418fc67af991276569b75f2bd5846856
---

## 场景介绍

从API version 20开始支持。端侧推理场景具有保障用户数据隐私、部署成本低、时延低、不受网络影响的高可用性等优点。但是，相比于云侧推理而言，端侧推理也面临着更大的挑战，因为端侧设备的内存资源受限、算力受限、对功耗敏感，并且还需要在运行端侧推理业务时保障用户体验、不卡顿。为了应对端侧推理的这些挑战，格物服务提供QoS感知的推理加速和资源管理优化能力。本文将指导开发者使用格物接口。

## 接口

### 错误码

OH\_QoS\_GewuErrorCode枚举型作为格物的错误码类型，各函数接口返回的错误码含义见接口描述。

### 会话句柄

会话句柄用于会话的管理。通过OH\_QoS\_GewuSession成功创建会话时可获得会话句柄，可用于提交/中止请求和销毁会话。

```
1. typedef unsigned int OH_QoS_GewuSession;
```

### 请求句柄

请求句柄用于请求的管理。通过OH\_QoS\_GewuSubmitRequest成功提交请求时可获得请求句柄，可用于中止请求。

```
1. typedef unsigned int OH_QoS_GewuRequest;
```

### 函数

| 函数名 | 简介 |
| --- | --- |
| OH\_QoS\_GewuCreateSession | 创建会话 |
| OH\_QoS\_GewuDestroySession | 销毁会话 |
| OH\_QoS\_GewuSubmitRequest | 提交请求 |
| OH\_QoS\_GewuAbortRequest | 中止请求 |

**OH\_QoS\_GewuCreateSession**

**描述**

OH\_QoS\_GewuCreateSession接口用于创建会话。

该接口异步处理请求，即该接口只是发起创建会话，并不会等到会话资源分配完成、模型加载完成才返回。格物优化端侧推理资源管理，可以动态按需加载资源。

会话对象的生命周期从OH\_QoS\_GewuCreateSession函数返回开始，到调用OH\_QoS\_GewuDestroySession为止。

**声明**

```
1. typedef struct {
2. OH_QoS_GewuSession session;
3. OH_QoS_GewuErrorCode error;
4. } OH_QoS_GewuCreateSessionResult;

6. OH_QoS_GewuCreateSessionResult OH_QoS_GewuCreateSession(const char* attributes);
```

**参数**

* const char\* attributes参数表示会话属性的json字符串。该json字符串支持以下字段：
  + "model": string 表示会话使用的模型的路径。

attributes json字符串例子：

```
1. {
2. "model": "/data/storage/el2/base/files/qwen2/"
3. }
```

**返回值**

如果创建会话成功，返回值OH\_QoS\_GewuCreateSessionResult里的error为OH\_QOS\_GEWU\_OK，而session为创建出来的会话句柄。

如果创建会话失败，返回值OH\_QoS\_GewuCreateSessionResult里的error为错误原因，其中OH\_QOS\_GEWU\_NOMEM表示没有足够的内存创建会话。

**OH\_QoS\_GewuDestroySession**

**描述**

OH\_QoS\_GewuDestroySession接口用于销毁会话。

建议用户应当等待至所有请求都已完成或中止，然后再调用该接口来销毁会话。如果调用该接口时还有正在进行的请求，那些请求将会被中止，且用户不会再收到回复。注意，在调用完该接口后，会话对象无法再被使用。

**声明**

```
1. OH_QoS_GewuErrorCode OH_QoS_GewuDestroySession(OH_QoS_GewuSession session);
```

**参数**

* OH\_QoS\_GewuSession session参数为要销毁的会话的句柄。

**返回值**

如果会话销毁成功，返回值为OH\_QOS\_GEWU\_OK。

如果会话销毁失败，返回值为错误原因，其中OH\_QOS\_GEWU\_NOENT表示找不到会话。

**OH\_QoS\_GewuSubmitRequest**

**描述**

OH\_QoS\_GewuSubmitRequest接口用于提交请求。该接口异步执行请求，即该接口只是发起请求，并不直接返回结果，该接口返回时请求可能尚未开始执行。请求的结果通过调用用户提供的回调返回给用户。

**声明**

```
1. typedef struct {
2. OH_QoS_GewuRequest request;
3. OH_QoS_GewuErrorCode error;
4. } OH_QoS_GewuSubmitRequestResult;

6. typedef void (*OH_QoS_GewuOnResponse)(void* context, const char* response);

8. OH_QoS_GewuSubmitRequestResult OH_QoS_GewuSubmitRequest(OH_QoS_GewuSession session, const char* request,
9. OH_QoS_GewuOnResponse callback, void* context);
```

**参数**

OH\_QoS\_GewuSubmitRequest函数的各参数如下：

* OH\_QoS\_GewuSession session参数是会话句柄，表示请求要提交到哪个会话。
* const char\* request参数为请求的json字符串，支持以下字段：
  + "messages": array. 表示消息的数组其中每个元素支持以下字段：
    - "role": string. 消息的角色类型。其中"developer"表示开发者或系统提供的指示，"user"表示用户输入，"assistant"表示模型生成结果。
    - "content": string. 消息内容。
  + "stream": boolean or null. 是否使能流式推理，默认为非流式。
* OH\_QoS\_GewuOnResponse callback参数为请求的回调函数。
* void\* context参数为用户提供的上下文指针，用于传递给回调函数。一般用法中，用户代码可通过该参数找到与收到的回复对应的请求，从而进行相应的处理。

另外，OH\_QoS\_GewuOnResponse回调函数的各参数如下：

* void\* context参数是调用OH\_QoS\_GewuSubmitRequest时传进来的context指针。
* const char\* response参数是回复的json字符串，包含以下字段：
  + "message": 回复消息，包含以下字段：
    - "role": string. 消息的角色类型，应为"assistant"。
    - "content": string. 消息内容。
  + "finish\_reason": string or null. 停止原因，可能的值如下：
    - null: 表示没有停止。流式推理中会有多次回复，只有最后一次回复有非空的"finish\_reason"。而非流式推理只有一次回复，且"finish\_reason"非空。
    - "stop": 正常停止。
    - "abort": 用户主动提前中止。
    - "length": token数超过限制。

**返回值**

如果提交请求成功，返回值OH\_QoS\_GewuSubmitRequestResult里的error为OH\_QOS\_GEWU\_OK，request为请求句柄。

如果提交请求失败，返回值OH\_QoS\_GewuSubmitRequestResult里的error为错误原因，其中OH\_QOS\_GEWU\_NOMEM表示没有足够的内存处理该请求。

**OH\_QoS\_GewuAbortRequest**

**描述**

OH\_QoS\_GewuAbortRequest接口用于提前中止请求。

正常情况下，用户调用OH\_QoS\_GewuSubmitRequest接口提交请求后，等待至推理完成（即收到"finish\_reason"不为空的回复），不需要调用OH\_QoS\_GewuAbortRequest接口。

只有当用户希望提前中止推理请求的时候，才需要调用OH\_QoS\_GewuAbortRequest接口。

成功调用该函数后，用户不会再收到该请求的回复，且该请求句柄无法再被使用。

**声明**

```
1. OH_QoS_GewuErrorCode OH_QoS_GewuAbortRequest(OH_QoS_GewuSession session, OH_QoS_GewuRequest request);
```

**参数**

* OH\_QoS\_GewuSession session参数为请求所述的会话的句柄。
* OH\_QoS\_GewuRequest request参数为要中止的请求的句柄。

**返回值**

如果请求中止成功，返回值为OH\_QOS\_GEWU\_OK。

如果请求中止失败，返回值为错误原因，其中OH\_QOS\_GEWU\_NOENT表示找不到请求。

## 示例

示例如下:

```
1. #include <future>
2. #define LOG_TAG "DEMO"
3. #include <hilog/log.h>
4. #include <nlohmann/json.hpp>
5. #include <qos/qos.h>
6. #include <string>

8. #define DEMO_LOGD(fmt, ...) OH_LOG_DEBUG(LOG_APP, fmt, ##__VA_ARGS__)
9. #define DEMO_LOGI(fmt, ...) OH_LOG_INFO(LOG_APP, fmt, ##__VA_ARGS__)
10. #define DEMO_LOGW(fmt, ...) OH_LOG_WARN(LOG_APP, fmt, ##__VA_ARGS__)
11. #define DEMO_LOGE(fmt, ...) OH_LOG_ERROR(LOG_APP, fmt, ##__VA_ARGS__)

13. using json = nlohmann::json;

15. /* 用于保存聊天状态 */
16. struct ChatContext {
17. public:
18. ChatContext()
19. {
20. future = promise.get_future();
21. }

23. void Join()
24. {
25. assert(future.valid());
26. std::string stopReasonStr = future.get();
27. DEMO_LOGI("stopReasonStr=%s", stopReasonStr.c_str());
28. }

30. std::promise<std::string> promise;
31. std::future<std::string> future;
32. std::string responseContent;
33. bool earlyAbort = false;
34. };

36. /* 接收到推理结果时的回调函数 */
37. void OnChatResponse(void *context, const char *response)
38. {
39. ChatContext *chatContext = static_cast<ChatContext *>(context);
40. if (chatContext->earlyAbort) {
41. DEMO_LOGD("ignore response after early abort");
42. return;
43. }
44. try {
45. json responseJson = json::parse(response);
46. chatContext->responseContent += responseJson.at("message").at("content").get<std::string>();
47. json finishReasonJson = responseJson.at("finish_reason");
48. if (!finishReasonJson.is_null()) {
49. /* finish */
50. std::string finishReasonStr = finishReasonJson.get<std::string>();
51. chatContext->promise.set_value(finishReasonStr);
52. } else if (chatContext->responseContent.find("\n") != std::string::npos) {
53. /* customized stop */
54. chatContext->promise.set_value("customized");
55. chatContext->earlyAbort = true;
56. } else {
57. /* continue */
58. ;
59. }
60. } catch (json::exception &e) {
61. DEMO_LOGE("failed to parse response: %s", e.what());
62. }
63. }

65. int Demo(void)
66. {
67. DEMO_LOGI("Demo starts");
68. json attrJson = {
69. /* 模型文件位置，根据实际情况修改 */
70. {"model", "/data/storage/el2/base/files/qwen2-awq"},
71. };
72. std::string attrStr = attrJson.dump(4);

74. /* 创建会话 */
75. OH_QoS_GewuCreateSessionResult createResult = OH_QoS_GewuCreateSession(attrStr.c_str());
76. if (createResult.error != OH_QOS_GEWU_OK) {
77. DEMO_LOGE("failed to create session, error=%d", (int)createResult.error);
78. return -1;
79. }
80. OH_QoS_GewuSession session = createResult.session;

82. /* 创建并提交请求 */
83. ChatContext context;
84. json requestJson = {
85. {"messages", json::array({
86. {{"role", "developer"}, {"content", "You are a helpful assistant"}},
87. {{"role", "user"}, {"content", "What is LLM?"}},
88. })},
89. {"stream", true},
90. };
91. std::string requestStr = requestJson.dump(4);
92. OH_QoS_GewuSubmitRequestResult submitResult = OH_QoS_GewuSubmitRequest(session, requestStr.c_str(),
93. OnChatResponse, &context);
94. if (submitResult.error != OH_QOS_GEWU_OK) {
95. DEMO_LOGE("failed to submit request, error=%d", (int)submitResult.error);
96. return -1;
97. }
98. OH_QoS_GewuRequest request = submitResult.request;
99. context.Join();

101. /* 提前中止请求 */
102. if (context.earlyAbort) {
103. OH_QoS_GewuErrorCode error = OH_QoS_GewuAbortRequest(session, request);
104. if (error != OH_QOS_GEWU_OK) {
105. DEMO_LOGE("failed to abort request, error=%d", (int)error);
106. return -1;
107. }
108. }

110. /* 打印结果 */
111. DEMO_LOGI("response: %s", context.responseContent.c_str());

113. /* 销毁会话 */
114. OH_QoS_GewuErrorCode error = OH_QoS_GewuDestroySession(session);
115. if (error != OH_QOS_GEWU_OK) {
116. DEMO_LOGE("failed to destroy session, error=%d", (int)error);
117. return -1;
118. }
119. return 0;
120. }
```

说明

在demo代码中，使用了第三方库nlohmann/json来简化JSON数据的解析与构造。nlohmann/json是一个现代C++的JSON库，提供了直观、简洁的方式来处理JSON数据。

它的设计理念是让JSON操作像使用STL容器一样自然。

开发者可以下载json.hpp文件并放入项目的include目录即可使用，无需额外链接库文件。
