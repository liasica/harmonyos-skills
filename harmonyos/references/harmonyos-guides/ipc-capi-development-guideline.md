---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ipc-capi-development-guideline
title: IPC与RPC通信开发指导(C/C++)
breadcrumb: 指南 > 应用框架 > IPC Kit（进程间通信服务） > IPC与RPC通信开发指导(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:376af176f7b0a7c6ea60a99a829a7edcb3abee18b79309110b05c38a13d6d0ec
---

## 场景介绍

IPC让运行在不同进程间的Proxy和Stub实现互相通信。IPC CAPI是IPC Kit提供的C语言接口。

IPC CAPI接口不直接提供获取通信代理对象的能力，该功能由[Ability Kit](abilitykit-overview.md)提供。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/aFLkp3cfRFmsTiDuTgxfcg/zh-cn_image_0000002583478319.png?HW-CC-KV=V1&HW-CC-Date=20260427T234138Z&HW-CC-Expire=86400&HW-CC-Sign=C333A1CC3C384AF95D8838BB75F8FDEADB26EB93974A8CA58D509DB56EA6A38E)

进程间IPC通道的建立，请参考[Native子进程开发指导（C/C++）](capi-nativechildprocess-development-guideline.md)。本文重点介绍IPC CAPI的使用。

## 接口说明

**表1** IPC CAPI侧关键接口

| 接口名 | 描述 |
| --- | --- |
| typedef int (\*OH\_OnRemoteRequestCallback)  (uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply,  void \*userData); | Stub端用于处理远端数据请求的回调函数。 |
| OHIPCRemoteStub\* OH\_IPCRemoteStub\_Create  (const char \*descriptor, OH\_OnRemoteRequestCallback requestCallback,  OH\_OnRemoteDestroyCallback destroyCallback, void \*userData); | 创建OHIPCRemoteStub对象。 |
| int OH\_IPCRemoteProxy\_SendRequest(const OHIPCRemoteProxy \*proxy,  uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply,  const OH\_IPC\_MessageOption \*option); | IPC消息发送函数。 |
| struct OHIPCRemoteProxy; | 用于向远端发送请求的OHIPCRemoteProxy对象，需要依赖元能力接口返回。 |
| OHIPCDeathRecipient\* OH\_IPCDeathRecipient\_Create  (OH\_OnDeathRecipientCallback deathRecipientCallback,  OH\_OnDeathRecipientDestroyCallback destroyCallback,  void \*userData); | 创建用于监听远端OHIPCRemoteStub对象死亡的通知对象（OHIPCDeathRecipient对象）。 |
| int OH\_IPCRemoteProxy\_AddDeathRecipient(OHIPCRemoteProxy \*proxy,  OHIPCDeathRecipient \*recipient); | 向OHIPCRemoteProxy对象注册死亡监听，用于接收远端OHIPCRemoteStub对象死亡时的回调通知。 |

详细的接口说明请参考[IPCKit](../harmonyos-references/capi-ipckit.md)。

## 开发步骤

先创建服务端Stub对象，通过元能力获取其客户端代理Proxy对象，然后用Proxy对象与服务端Stub对象进行IPC通信，同时再注册远端对象的死亡通知回调，用于Proxy侧感知服务端Stub对象所在进程的死亡状态。

**动态库文件**

CMakeLists.txt中添加以下lib。

```
1. # ipc capi
2. libipc_capi.so
3. # 元能力，ability capi
4. libchild_process.so
```

**头文件**

```
1. #include <IPCKit/ipc_kit.h>
2. #include <AbilityKit/native_child_process.h>
```

[ChildProcessSample.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessIpc/entry/src/main/cpp/ChildProcessSample.cpp#L17-L22)

**子进程实现**

```
1. #include <IPCKit/ipc_kit.h>
2. // ...
3. #include <IPCKit/ipc_cremote_object.h>
4. #include <IPCKit/ipc_cparcel.h>
5. #include <IPCKit/ipc_error_code.h>

7. class IpcCapiStubTest {
8. public:
9. explicit IpcCapiStubTest();
10. ~IpcCapiStubTest();
11. OHIPCRemoteStub *GetRemoteStub();
12. static int OnRemoteRequest(uint32_t code, const OHIPCParcel *data, OHIPCParcel *reply, void *userData);

14. private:
15. OHIPCRemoteStub *stub_{nullptr};
16. };

18. IpcCapiStubTest::IpcCapiStubTest()
19. {
20. // 创建stub对象
21. stub_ = OH_IPCRemoteStub_Create("testIpc", &IpcCapiStubTest::OnRemoteRequest, nullptr, this);
22. }

24. IpcCapiStubTest::~IpcCapiStubTest()
25. {
26. if (stub_ != nullptr) {
27. OH_IPCRemoteStub_Destroy(stub_);
28. }
29. }

31. OHIPCRemoteStub *IpcCapiStubTest::GetRemoteStub() { return stub_; }

33. int IpcCapiStubTest::OnRemoteRequest(uint32_t code, const OHIPCParcel *data, OHIPCParcel *reply, void *userData)
34. {
35. return OH_IPC_SUCCESS;
36. }

38. IpcCapiStubTest g_ipcStubObj;

40. extern "C" {
41. OHIPCRemoteStub *NativeChildProcess_OnConnect()
42. {
43. // ipcRemoteStub指向子进程实现的ipc stub对象，用于接收来自主进程的IPC消息并响应
44. // 子进程根据业务逻辑控制其生命周期
45. return g_ipcStubObj.GetRemoteStub();
46. }

48. void NativeChildProcessMainProc()
49. {
50. // 相当于子进程的Main函数，实现子进程的业务逻辑
51. // ...
52. // 函数返回后子进程随即退出
53. }

55. } // extern "C"
```

[ChildProcessSample.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessIpc/entry/src/main/cpp/ChildProcessSample.cpp#L16-L76)

**主进程实现**

```
1. #include <IPCKit/ipc_kit.h>
2. #include <AbilityKit/native_child_process.h>
3. // ...
4. static void OnNativeChildProcessStarted(int errCode, OHIPCRemoteProxy *remoteProxy)
5. {
6. if (errCode != NCP_NO_ERROR) {
7. // 子进程未能正常启动时的异常处理
8. // ...
9. return;
10. }

12. // 保存remoteProxy对象，后续基于IPC Kit提供的API同子进程间进行IPC通信
13. // 耗时操作建议转移到独立线程去处理，避免长时间阻塞回调线程
14. // IPC对象使用完毕后，需要调用OH_IPCRemoteProxy_Destroy方法释放
15. // ...
16. }

18. void CreateNativeChildProcess()
19. {
20. // 第一个参数"libchildprocesssample.so"为实现了子进程必要导出方法的动态库文件名称
21. int32_t ret = OH_Ability_CreateNativeChildProcess("libchildprocesssample.so", OnNativeChildProcessStarted);
22. if (ret != NCP_NO_ERROR) {
23. // 子进程未能正常启动时的异常处理
24. // ...
25. }
26. g_result = ret;
27. }
```

[MainProcessSample.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessIpc/entry/src/main/cpp/MainProcessSample.cpp#L16-L167)

**Proxy侧实现**

```
1. #include "IpcProxy.h"
2. #include <IPCKit/ipc_error_code.h>
3. #include "Ipchelper.h"

5. IpcProxy::IpcProxy(OHIPCRemoteProxy *ipcProxy)
6. : ipcProxy_(ipcProxy)
7. {
8. }

10. IpcProxy::~IpcProxy()
11. {
12. if (ipcProxy_ != nullptr) {
13. OH_IPCRemoteProxy_Destroy(ipcProxy_);
14. }
15. }

17. bool IpcProxy::RequestExitChildProcess(int32_t exitCode)
18. {
19. if (ipcProxy_ == nullptr) {
20. return false;
21. }

23. StdUniPtrIpcParcel data(OH_IPCParcel_Create(), OH_IPCParcel_Destroy);
24. StdUniPtrIpcParcel reply(OH_IPCParcel_Create(), OH_IPCParcel_Destroy);
25. if (data == nullptr || reply == nullptr) {
26. return false;
27. }

29. if (!WriteInterfaceToken(data.get()) ||
30. OH_IPCParcel_WriteInt32(data.get(), exitCode) != OH_IPC_SUCCESS) {
31. return false;
32. }

34. OH_IPC_MessageOption ipcOpt;
35. ipcOpt.mode = OH_IPC_REQUEST_MODE_SYNC;
36. ipcOpt.timeout = 0;
37. ipcOpt.reserved = nullptr;
38. int ret = OH_IPCRemoteProxy_SendRequest(ipcProxy_, IPC_ID_REQUEST_EXIT_PROCESS, data.get(), reply.get(), &ipcOpt);
39. if (ret != OH_IPC_SUCCESS) {
40. return false;
41. }

43. return true;
44. }

46. int32_t IpcProxy::Add(int32_t a, int32_t b)
47. {
48. if (ipcProxy_ == nullptr) {
49. return INT32_MIN;
50. }

52. int32_t result = INT32_MIN;
53. StdUniPtrIpcParcel data(OH_IPCParcel_Create(), OH_IPCParcel_Destroy);
54. StdUniPtrIpcParcel reply(OH_IPCParcel_Create(), OH_IPCParcel_Destroy);
55. if (data == nullptr || reply == nullptr) {
56. return result;
57. }

59. if (!WriteInterfaceToken(data.get()) ||
60. OH_IPCParcel_WriteInt32(data.get(), a) != OH_IPC_SUCCESS ||
61. OH_IPCParcel_WriteInt32(data.get(), b) != OH_IPC_SUCCESS) {
62. return result;
63. }

65. OH_IPC_MessageOption ipcOpt;
66. ipcOpt.mode = OH_IPC_REQUEST_MODE_SYNC;
67. ipcOpt.timeout = 0;
68. ipcOpt.reserved = nullptr;
69. int ret = OH_IPCRemoteProxy_SendRequest(ipcProxy_, IPC_ID_ADD, data.get(), reply.get(), &ipcOpt);
70. if (ret != OH_IPC_SUCCESS) {
71. return result;
72. }

74. OH_IPCParcel_ReadInt32(reply.get(), &result);
75. return result;
76. }

78. int32_t IpcProxy::StartNativeChildProcess()
79. {
80. if (ipcProxy_ == nullptr) {
81. return INT32_MIN;
82. }

84. int32_t result = INT32_MIN;
85. StdUniPtrIpcParcel data(OH_IPCParcel_Create(), OH_IPCParcel_Destroy);
86. StdUniPtrIpcParcel reply(OH_IPCParcel_Create(), OH_IPCParcel_Destroy);
87. if (data == nullptr || reply == nullptr) {
88. return result;
89. }

91. if (!WriteInterfaceToken(data.get())) {
92. return result;
93. }

95. OH_IPC_MessageOption ipcOpt;
96. ipcOpt.mode = OH_IPC_REQUEST_MODE_SYNC;
97. ipcOpt.timeout = 0;
98. ipcOpt.reserved = nullptr;
99. int ret = OH_IPCRemoteProxy_SendRequest(
100. ipcProxy_, IPC_ID_START_NATIVE_CHILD_PROCESS, data.get(), reply.get(), &ipcOpt);
101. if (ret != OH_IPC_SUCCESS) {
102. return result;
103. }

105. OH_IPCParcel_ReadInt32(reply.get(), &result);
106. return result;
107. }

109. bool IpcProxy::WriteInterfaceToken(OHIPCParcel* data)
110. {
111. return OH_IPCParcel_WriteInterfaceToken(data, interfaceToken_) == OH_IPC_SUCCESS;
112. }
```

[IpcProxy.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessIpc/entry/src/main/cpp/IpcProxy.cpp#L16-L129)

**Stub侧实现**

```
1. #include "IpcStub.h"
2. #include <IPCKit/ipc_error_code.h>
3. #include <cstring>
4. #include <new>

6. IpcStub::IpcStub()
7. {
8. ipcStub_ = OH_IPCRemoteStub_Create("NativeChildIPCStubSample",
9. IpcStub::OnRemoteRequest, IpcStub::OnRemoteObjectDestroy, this);
10. }

12. IpcStub::~IpcStub()
13. {
14. OH_IPCRemoteStub_Destroy(ipcStub_);
15. }

17. OHIPCRemoteStub* IpcStub::GetIpcStub()
18. {
19. return ipcStub_;
20. }

22. void IpcStub::OnRemoteObjectDestroy(void *userData)
23. {
24. }

26. int IpcStub::OnRemoteRequest(uint32_t code, const OHIPCParcel *data, OHIPCParcel *reply, void *userData)
27. {
28. if (userData == nullptr) {
29. return OH_IPC_CHECK_PARAM_ERROR;
30. }

32. if (!CheckInterfaceToken(data)) {
33. return OH_IPC_CHECK_PARAM_ERROR;
34. }

36. int ret;
37. IpcStub *thiz = reinterpret_cast<IpcStub*>(userData);
38. switch (code) {
39. case IPC_ID_REQUEST_EXIT_PROCESS:
40. ret = thiz->HandleRequestExitChildProcess(data, reply);
41. break;

43. case IPC_ID_ADD:
44. ret = thiz->HandleAdd(data, reply);
45. break;

47. case IPC_ID_START_NATIVE_CHILD_PROCESS:
48. ret = thiz->HandleStartNativeChildProcess(data, reply);
49. break;

51. default:
52. ret = OH_IPC_CODE_OUT_OF_RANGE;
53. break;
54. }

56. return ret;
57. }

59. void* IpcStub::OnIpcMemAlloc(int32_t len)
60. {
61. // limit ipc memory alloc size to 128 bytes
62. if (len > 128) {
63. return nullptr;
64. }

66. return new (std::nothrow) char[len];
67. }

69. void IpcStub::ReleaseIpcMem(void* ipcMem)
70. {
71. delete[] reinterpret_cast<char*>(ipcMem);
72. }

74. bool IpcStub::CheckInterfaceToken(const OHIPCParcel* data)
75. {
76. char *token;
77. int32_t tokenLen;
78. int ret = OH_IPCParcel_ReadInterfaceToken(data, &token, &tokenLen, IpcStub::OnIpcMemAlloc);
79. if (ret != OH_IPC_SUCCESS) {
80. return false;
81. }

83. bool tokenCheckRes = strcmp(token, interfaceToken_) == 0;
84. ReleaseIpcMem(token);
85. return tokenCheckRes;
86. }

88. int IpcStub::HandleRequestExitChildProcess(const OHIPCParcel *data, OHIPCParcel *reply)
89. {
90. int exitCode = 0;
91. if (OH_IPCParcel_ReadInt32(data, &exitCode) != OH_IPC_SUCCESS) {
92. return OH_IPC_PARCEL_READ_ERROR;
93. }
94. int32_t ret = RequestExitChildProcess(exitCode) ? 1 : 0;
95. return OH_IPCParcel_WriteInt32(reply, ret);
96. }

98. int32_t IpcStub::HandleAdd(const OHIPCParcel *data, OHIPCParcel *reply)
99. {
100. int32_t a = 0;
101. int32_t b = 0;
102. if (OH_IPCParcel_ReadInt32(data, &a) != OH_IPC_SUCCESS ||
103. OH_IPCParcel_ReadInt32(data, &b) != OH_IPC_SUCCESS) {
104. return OH_IPC_PARCEL_READ_ERROR;
105. }

107. int32_t result = Add(a, b);
108. if (OH_IPCParcel_WriteInt32(reply, result) != OH_IPC_SUCCESS) {
109. return OH_IPC_PARCEL_WRITE_ERROR;
110. }

112. return OH_IPC_SUCCESS;
113. }

115. int IpcStub::HandleStartNativeChildProcess(const OHIPCParcel *data, OHIPCParcel *reply)
116. {
117. int32_t ret = StartNativeChildProcess();
118. return OH_IPCParcel_WriteInt32(reply, ret);
119. }
```

[IpcStub.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessIpc/entry/src/main/cpp/IpcStub.cpp#L16-L136)
