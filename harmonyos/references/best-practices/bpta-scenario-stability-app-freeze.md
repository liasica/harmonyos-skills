---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-scenario-stability-app-freeze
title: 应用冻屏类问题案例
breadcrumb: 最佳实践 > 稳定性 > 稳定性案例 > 应用冻屏类问题案例
category: best-practices
scraped_at: 2026-09-02T15:03:24+08:00
doc_updated_at: 2026-08-17
content_hash: sha256:63f814e304fc9588173f1b861af3c0962783f62a2909affc31fb8616b1886614
---

## ThreadBlock类问题案例-未正确使用锁

### 概述

由于没有考虑到多线程操作时锁的时序问题，从而导致死锁，触发ThreadBlock检测，原理可参考[THREAD\_BLOCK\_6S 应用主线程卡死超时](../harmonyos-guides/appfreeze-guidelines.md#thread_block_6s应用主线程卡死超时)。

### 问题现象

xxxservice上报THREAD\_BLOCK\_6S的AppFreeze问题。后台应用卡死时，用户无感知，但相关功能将不可用。

### 问题代码

代码中通过mutex\_.lock()加锁，但是在返回失败情况下未解锁，会导致其他线程一直等锁。

```cpp
bool ContainTarget(int target) {
    auto ret = std::find(sharedVec.begin(), sharedVec.end(), target);
    if (ret == sharedVec.end()) {
        return false;
    }
    return true;
}

int AppFreezeAdvise1() {
    // ...
    mtx.lock();
    if (ContainTarget(1)) {
        return -1;
        // 没有释放锁
    }
    // 没有释放锁
     return 0;
}
```

### 分析思路

请参考[应用冻屏问题定位步骤与思路](bpta-stability-app-freeze-way.md#section1950514261110)。

### 分析步骤

提取故障日志关键类别信息。

```screen
appfreeze: com.example.hmsapp.xxx THREAD_BLOCK_6S at 20240408082432
DisplayPowerInfo:powerState:AWAKE
```

从Foreground值可看出，应用此时处于后台。当真正的3s事件上报上来时，后台应用已卡**18s**前。

```screen
Module name:com.xxx.xxx.xxx
Version:1.2.2.202
VersionCode:1002002202
PreInstalled:Yes
Foreground:No  --> 后台
Pid:43675
Uid:20020029
Reason:THREAD_BLOCK_6S
```

THREAD\_BLOCK\_3S上报的时间为08:24:29:612；

THREAD\_BLOCK\_6S上报的时间为08:24:32:638，相隔3s符合预期。

```screen
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
DOMAIN:AAFWK
STRINGID:THREAD_BLOCK_6S
TIMESTAMP:2024/04/08-08:24:32:638
PID:43675
UID:20020029
PACKAGE_NAME:com.xxx.xxx.xxx
PROCESS_NAME:com.xxx.xxx.xxx
*******************************************
start time: 2024/04/08-08:24:29:627
DOMAIN = AAFWK
EVENTNAME = THREAD_BLOCK_3S
TIMESTAMP = 2024/04/08-08:24:29:612
PID = 43675
UID = 20020029
PACKAGE_NAME = com.xxx.xxx.xxx
PROCESS_NAME = com.xxx.xxx.xxx
```

3s上报时会抓取此时的EventHandler信息，时间为08:24:29.413，符合预期上报的原因为：App main thread is not response! 主线程无响应，当前正在运行的任务开始时间为08:24:01.514。

```screen
MSG = 
Fault time:2024/04/08-08:24:29
App main thread is not response!
mainHandler dump is:
 EventHandler dump begin curTime: 2024-04-08 08:24:29.413
 Event runner (Thread name = , Thread ID = 43675) is running
 Current Running: start at 2024-04-08 08:24:01.514, Event { send thread = 43675, send time = 2024-04-08 08:24:01.514, handle time = 2024-04-08 08:24:01.514, task name = uvLoopTask }
```

watchdog 任务位于高优先级队列（VIP priority event queue），如下图可发现：每隔3s就会抛一个任务到主线程去，符合预期。

THREAD\_BLOCK\_3S、THREAD\_BLOCK\_6S的队列一致，6s队列较3s队列多了一个event。

最早的一个event send time为**08:24:11.388**，与3s上报上来的时间08:24:29:612刚好差18s，符合预期。

```screen
 VIP priority event queue information:
 No.1 : Event { send thread = 43679, send time = 2024-04-08 08:24:11.388, handle time = 2024-04-08 08:24:11.388, id = 1, caller = [watchdog.cpp(Timer:139)] }
 No.2 : Event { send thread = 43679, send time = 2024-04-08 08:24:14.458, handle time = 2024-04-08 08:24:14.458, id = 1, caller = [watchdog.cpp(Timer:139)] }
 No.3 : Event { send thread = 43679, send time = 2024-04-08 08:24:17.383, handle time = 2024-04-08 08:24:17.383, id = 1, caller = [watchdog.cpp(Timer:139)] }
 No.4 : Event { send thread = 43679, send time = 2024-04-08 08:24:20.363, handle time = 2024-04-08 08:24:20.363, id = 1, caller = [watchdog.cpp(Timer:139)] }
 No.5 : Event { send thread = 43679, send time = 2024-04-08 08:24:23.418, handle time = 2024-04-08 08:24:23.418, id = 1, caller = [watchdog.cpp(Timer:139)] }
 No.6 : Event { send thread = 43679, send time = 2024-04-08 08:24:26.369, handle time = 2024-04-08 08:24:26.369, id = 1, caller = [watchdog.cpp(Timer:139)] }
 No.7 : Event { send thread = 43679, send time = 2024-04-08 08:24:29.412, handle time = 2024-04-08 08:24:29.412, id = 1, caller = [watchdog.cpp(Timer:139)] }
```

以上可总结：应用**主线程从08:24:01.514开始运行本次任务，第一次3s检测开始时间为08:24:11.388，真正开始卡住的时间在08:24:11左右。**

查看主线程栈：从xxx\_request\_client.so->libsamgr\_proxy.z.so->libipc\_core.z.so(OHOS::BinderConnector::WriteBinder)

可知：**此时，主线程发起了一个ipc请求，对端进程未返回导致卡死，堆栈如下所示：**

```screen
Tid:43675, Name:xxx
# 00 pc 0000000000168c44 /system/lib/ld-musl-aarch64.so.1(ioctl+176)(91b804d2409a13f27463debe9e19fb5d)
# 01 pc 0000000000049268 /system/lib64/platformsdk/libipc_core.z.so(OHOS::BinderConnector::WriteBinder(unsigned long, void*)+112)(e59500a4ea66775388332f6e3cc12fe3)
# 02 pc 0000000000054fd4 /system/lib64/platformsdk/libipc_core.z.so(OHOS::BinderInvoker::TransactWithDriver(bool)+296)(e59500a4ea66775388332f6e3cc12fe3)
# 03 pc 00000000000544c8 /system/lib64/platformsdk/libipc_core.z.so(OHOS::BinderInvoker::WaitForCompletion(OHOS::MessageParcel*, int*)+304)(e59500a4ea66775388332f6e3cc12fe3)
# 04 pc 0000000000053c84 /system/lib64/platformsdk/libipc_core.z.so(OHOS::BinderInvoker::SendRequest(int, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+312)(e59500a4ea66775388332f6e3cc12fe3)
# 05 pc 000000000002d6d8 /system/lib64/platformsdk/libipc_core.z.so(OHOS::IPCObjectProxy::SendRequestInner(bool, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+128)(e59500a4ea66775388332f6e3cc12fe3)
# 06 pc 0000000000030e00 /system/lib64/platformsdk/libipc_core.z.so(OHOS::IPCObjectProxy::GetProtoInfo()+396)(e59500a4ea66775388332f6e3cc12fe3)
# 07 pc 000000000002e990 /system/lib64/platformsdk/libipc_core.z.so(OHOS::IPCObjectProxy::WaitForInit()+292)(e59500a4ea66775388332f6e3cc12fe3)
# 08 pc 0000000000036cd0 /system/lib64/platformsdk/libipc_core.z.so(OHOS::IPCProcessSkeleton::FindOrNewObject(int)+116)(e59500a4ea66775388332f6e3cc12fe3)
# 09 pc 00000000000571cc /system/lib64/platformsdk/libipc_core.z.so(OHOS::BinderInvoker::UnflattenObject(OHOS::Parcel&)+272)(e59500a4ea66775388332f6e3cc12fe3)
# 10 pc 00000000000463a4 /system/lib64/platformsdk/libipc_core.z.so(OHOS::MessageParcel::ReadRemoteObject()+116)(e59500a4ea66775388332f6e3cc12fe3)
# 11 pc 000000000001250c /system/lib64/chipset-pub-sdk/libsamgr_proxy.z.so(OHOS::SystemAbilityManagerProxy::CheckSystemAbility(int, bool&)+952)(6f113f37ac6ac882cfa16077ad5b406a)
# 12 pc 0000000000010e7c /system/lib64/chipset-pub-sdk/libsamgr_proxy.z.so(OHOS::SystemAbilityManagerProxy::GetSystemAbilityWrapper(int, std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&)+232)(6f113f37ac6ac882cfa16077ad5b406a)
# 13 pc 00000000000118b8 /system/lib64/chipset-pub-sdk/libsamgr_proxy.z.so(OHOS::SystemAbilityManagerProxy::Recompute(int, int)+132)(6f113f37ac6ac882cfa16077ad5b406a)
# 14 pc 0000000000011170 /system/lib64/chipset-pub-sdk/libsamgr_proxy.z.so(OHOS::DynamicCache<int, OHOS::sptr<OHOS::IRemoteObject>>::QueryResult(int, int)+316)(6f113f37ac6ac882cfa16077ad5b406a)
# 15 pc 0000000000007e0c xxx_request_client.so(xxx::RPCRequestClient::GetService()+540)(557450139184527807025a632613fd76)
# 16 pc 0000000000008824 xxx_request_client.so(xxx::RPCRequestClient::Init()+16)(557450139184527807025a632613fd76)
# 17 pc 0000000000008d60 xxx_request_client.so(CreateRpcRequestByServiceName+104)(557450139184527807025a632613fd76)
# 18 pc 0000000000008f98 xxx_request_client.so(CreateRpcRequest+72)(557450139184527807025a632613fd76)
# 19 pc 0000000000002944 xxx_rpc_client.so(xxx::xxx::RpcRequestClient::RpcRequestClient()+224)(02343ed2fff69759d408b23eaf69fcde)
```

查看binderCatcher：**此时43675的主线程正在与979进程通信，抓取binder时已经卡了27s。**

```screen
PeerBinderCatcher -- pid==43675 layer_ == 1

BinderCatcher --

    43675:43675 to 979:0 code 5f475249 wait:27.104545829 s frz_state:1,  ns:-1:-1 to -1:-1, debug:35854:35854 to 52462:52462, active_code:0 active_thread:0, pending_async_proc=0  --> binder通信等待了27s
    57187:39147 to 28644:30753 code 0 wait:0.337894271 s frz_state:3,  ns:-1:-1 to -1:-1, debug:57187:39147 to 28644:30753, active_code:0 active_thread:0, pending_async_proc=0
    57187:39151 to 28644:28652 code 7 wait:0.531140625 s frz_state:3,  ns:-1:-1 to -1:-1, debug:57187:39151 to 28644:28652, active_code:0 active_thread:0, pending_async_proc=0
    57187:39150 to 28644:31297 code 0 wait:0.976419270 s frz_state:3,  ns:-1:-1 to -1:-1, debug:57187:39150 to 28644:31297, active_code:0 active_thread:0, pending_async_proc=0
    57187:38979 to 28644:32554 code 0 wait:0.22108334 s frz_state:3,  ns:-1:-1 to -1:-1, debug:57187:38979 to 28644:32554, active_code:0 active_thread:0, pending_async_proc=0
    57187:39149 to 28644:30754 code 0 wait:0.534261979 s frz_state:3,  ns:-1:-1 to -1:-1, debug:57187:39149 to 28644:30754, active_code:0 active_thread:0, pending_async_proc=0
    57187:38949 to 28644:31301 code 0 wait:0.977779166 s frz_state:3,  ns:-1:-1 to -1:-1, debug:57187:38949 to 28644:31301, active_code:0 active_thread:0, pending_async_proc=0
    57187:39172 to 28644:35667 code 0 wait:1.47387500 s frz_state:3,  ns:-1:-1 to -1:-1, debug:57187:39172 to 28644:35667, active_code:0 active_thread:0, pending_async_proc=0
    57187:39173 to 28644:28822 code 0 wait:0.565389063 s frz_state:3,  ns:-1:-1 to -1:-1, debug:57187:39173 to 28644:28822, active_code:0 active_thread:0, pending_async_proc=0
    1477:1676 to 1408:2026 code 17 wait:0.0 s frz_state:3,  ns:-1:-1 to -1:-1, debug:1477:1676 to 1408:2026, active_code:0 active_thread:0, pending_async_proc=0
    628:8136 to 979:0 code 2 wait:13166.722870859 s frz_state:1,  ns:-1:-1 to -1:-1, debug:628:8136 to 979:0, active_code:0 active_thread:0, pending_async_proc=0
```

查看979进程主线程栈：xxxserver在等待锁释放。**该问题即为典型的锁使用不当，导致的等锁卡死。**

```screen
Binder catcher stacktrace, type is peer, pid : 979
Result: 0 ( no error )
Timestamp:2024-04-08 08:24:29.000
Pid:979
Uid:3094
Process name:xxxserver
Process life time:60410s
Tid:979, Name:xxxserver
# 00 pc 00000000001aafc4 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+192)(91b804d2409a13f27463debe9e19fb5d)
# 01 pc 00000000001b0d50 /system/lib/ld-musl-aarch64.so.1(__pthread_mutex_timedlock_inner+592)(91b804d2409a13f27463debe9e19fb5d)
# 02 pc 00000000000c38e0 /system/lib64/libc++.so(std::__h::mutex::lock()+8)(0b61ba21a775725a1bd8802a393b133afbc503a5)   --> 调用了lock，然后等待
# 03 pc 00000000000086dc xxx_server.so(xxx::xxx::InitImpl(int, std::__h::vector<xxx::xxx::RpcHandle, std::__h::allocator<xxx::xxx::RpcHandle>> const&, std::__h::vector<xxx::xxx::RpcHandle, std::__h::allocator<xxx::xxx::RpcHandle>>&)+84)(f4bb275898d797b22eae35fe48db9009)
# 04 pc 000000000000798c xxx_request_server.so(xxx::RPCRequestStub::SyncExecute(OHOS::MessageParcel&, OHOS::MessageParcel&)+164)(70cbb10c758902c1e3e179efc93ce0af)
# 05 pc 0000000000008314 xxx_request_server.so(xxx::RPCRequestStub::OnRemoteRequest(unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+300)(70cbb10c758902c1e3e179efc93ce0af)
# 06 pc 00000000000153e4 /system/lib64/chipset-pub-sdk/libipc_single.z.so(OHOS::IPCObjectStub::SendRequest(unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+604)(25b3d63905ef47289c096ea42ba2d86a)
# 07 pc 000000000002b464 /system/lib64/chipset-pub-sdk/libipc_single.z.so(OHOS::IPC_SINGLE::BinderInvoker::OnTransaction(unsigned char const*)+1220)(25b3d63905ef47289c096ea42ba2d86a)
# 08 pc 000000000002baec /system/lib64/chipset-pub-sdk/libipc_single.z.so(OHOS::IPC_SINGLE::BinderInvoker::HandleCommandsInner(unsigned int)+368)(25b3d63905ef47289c096ea42ba2d86a)
# 09 pc 000000000002a6b0 /system/lib64/chipset-pub-sdk/libipc_single.z.so(OHOS::IPC_SINGLE::BinderInvoker::HandleCommands(unsigned int)+60)(25b3d63905ef47289c096ea42ba2d86a)
# 10 pc 000000000002a4dc /system/lib64/chipset-pub-sdk/libipc_single.z.so(OHOS::IPC_SINGLE::BinderInvoker::StartWorkLoop()+120)(25b3d63905ef47289c096ea42ba2d86a)
# 11 pc 000000000002bc2c /system/lib64/chipset-pub-sdk/libipc_single.z.so(OHOS::IPC_SINGLE::BinderInvoker::JoinThread(bool)+92)(25b3d63905ef47289c096ea42ba2d86a)
# 12 pc 0000000000004bd4 xxxserver(02cff7e5dce05d6d28096601458b6f6d)
# 13 pc 00000000000a3b58 /system/lib/ld-musl-aarch64.so.1(libc_start_main_stage2+64)(91b804d2409a13f27463debe9e19fb5d)
```

反编译后，确定对应卡锁代码行，结合上下文检测锁的使用。

### 修复方法

```cpp
int AppFreezeAdviseNegative() {
    // ...
    mtx.lock();
    if (ContainTarget(1)) {
        return -1;
    }
    // ...
     return 0;
}
```

修改为：

```cpp
int AppFreezeAdvisePositive() {
    // ...
    mtx.lock();
    if (ContainTarget(1)) {
        mtx.unlock();
        return -1;
    }
    mtx.unlock();
    // ...
    return 0;
}
```

结合上下文，合理调整锁的使用。

### 建议与总结

多线程交互时需要格外注意时序、死锁问题。

## APP\_INPUT\_BLOCK类典型案例-组件全量刷新

### 概述

由于线程繁忙，导致用户在合一桌面切换主题时，页面高概率卡死，点击无响应，然后闪退到锁屏界面，严重影响用户体验，从而触发APP\_INPUT\_BLOCK检测，原理可参考[日志差异性信息](../harmonyos-guides/appfreeze-guidelines.md#日志差异性信息)APP\_INPUT\_BLOCK 用户输入响应超时小节。

### 问题现象

用户在切换主题时突然卡死，有sceneboard的AppFreeze问题上报。

### 问题代码

组件的刷新复用通过其key值控制。页面更新时，key值不变复用之前的组件，key值变化更新组件及其子组件。

该函数用于生成桌面组件的key，并与themeStyle关联，当用户在桌面连续切换主题时，组件反复全量刷新，导致卡死。

```typescript
function getForeachKey(item : ItemType) : string {
    // ...
    return `${item.xxx2}${item.xxx2}...${item.themeStyle}`;
} // 这部分逻辑如果较为耗时，执行次数多，总时长就是发生冻屏的耗时操作
```

### 分析思路

请参考[应用冻屏问题定位步骤与思路](bpta-stability-app-freeze-way.md#section1950514261110)。

### 分析步骤

提取故障关键信息。

```screen
appfreeze: com.example.sceneboard APP_INPUT_BLOCK at 202403144059
DisplayPowerInfo:powerState:AWAKE
```

APP\_INPUT\_BLOCK 事件上报时间为 **14:40:59:440**。

```screen
DOMAIN:AAFWK
STRINGID:APP_INPUT_BLOCK
TIMESTAMP:2024/03/14-14:40:59:440 --> 故障上报时间
PID:2918
UID:20020017
PACKAGE_NAME:com.example.sceneboard
PROCESS_NAME:com.example.sceneboard
```

上报的原因是：User input does not respond! 用户输入事件没有响应。

可以看到，当前任务在主线程（Thread ID == Pid）上运行，任务从**14:40:53.499**开始运行，直到Fault time**14:40:58**仍未运行完。

```screen
MSG = 
Fault time:2024/03/14-14:40:58
User input does not respond!
mainHandler dump is:
 EventHandler dump begin curTime: 2024-03-14 02:40:58.520
 Event runner (Thread name = , Thread ID = 2918) is running
 Current Running: start at 2024-03-14 02:40:53.499, Event { send thread = 2918, send time = 2024-03-14 02:40:53.499, handle time = 2024-03-14 02:40:53.499, task name =  }
```

用户输入事件需要第一时间响应，所以同watchdog一样都在VIP priority event queue。

可以看出队列中已经有200+的input event阻塞中未被处理。

```screen
 VIP priority event queue information:
 No.1 : Event { send thread = 3370, send time = 2024-03-14 02:40:53.690, handle time = 2024-03-14 02:40:53.690, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.2 : Event { send thread = 3370, send time = 2024-03-14 02:40:53.699, handle time = 2024-03-14 02:40:53.699, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.3 : Event { send thread = 3370, send time = 2024-03-14 02:40:53.708, handle time = 2024-03-14 02:40:53.708, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.4 : Event { send thread = 3370, send time = 2024-03-14 02:40:53.717, handle time = 2024-03-14 02:40:53.717, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.5 : Event { send thread = 3370, send time = 2024-03-14 02:40:53.726, handle time = 2024-03-14 02:40:53.726, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.6 : Event { send thread = 3370, send time = 2024-03-14 02:40:53.736, handle time = 2024-03-14 02:40:53.736, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.7 : Event { send thread = 3370, send time = 2024-03-14 02:40:53.745, handle time = 2024-03-14 02:40:53.745, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.8 : Event { send thread = 3370, send time = 2024-03-14 02:40:53.754, handle time = 2024-03-14 02:40:53.754, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 ...
 No.190 : Event { send thread = 3370, send time = 2024-03-14 02:40:56.166, handle time = 2024-03-14 02:40:56.166, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.191 : Event { send thread = 3370, send time = 2024-03-14 02:40:56.176, handle time = 2024-03-14 02:40:56.176, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.192 : Event { send thread = 3370, send time = 2024-03-14 02:40:56.186, handle time = 2024-03-14 02:40:56.186, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.193 : Event { send thread = 2923, send time = 2024-03-14 02:40:56.196, handle time = 2024-03-14 02:40:56.196, id = 1, caller = [watchdog.cpp(Timer:140)] }
 No.194 : Event { send thread = 3370, send time = 2024-03-14 02:40:56.196, handle time = 2024-03-14 02:40:56.196, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.195 : Event { send thread = 3370, send time = 2024-03-14 02:40:56.206, handle time = 2024-03-14 02:40:56.206, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.196 : Event { send thread = 3370, send time = 2024-03-14 02:40:56.216, handle time = 2024-03-14 02:40:56.216, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.197 : Event { send thread = 3370, send time = 2024-03-14 02:40:56.226, handle time = 2024-03-14 02:40:56.226, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.198 : Event { send thread = 3370, send time = 2024-03-14 02:40:56.236, handle time = 2024-03-14 02:40:56.236, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.199 : Event { send thread = 3370, send time = 2024-03-14 02:40:56.245, handle time = 2024-03-14 02:40:56.245, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.200 : Event { send thread = 3370, send time = 2024-03-14 02:40:56.254, handle time = 2024-03-14 02:40:56.254, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.201 : Event { send thread = 3370, send time = 2024-03-14 02:40:56.265, handle time = 2024-03-14 02:40:56.265, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.202 : Event { send thread = 3370, send time = 2024-03-14 02:40:56.275, handle time = 2024-03-14 02:40:56.274, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.203 : Event { send thread = 3370, send time = 2024-03-14 02:40:56.284, handle time = 2024-03-14 02:40:56.284, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.204 : Event { send thread = 3370, send time = 2024-03-14 02:40:56.294, handle time = 2024-03-14 02:40:56.294, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
 No.205 : Event { send thread = 3370, send time = 2024-03-14 02:40:56.305, handle time = 2024-03-14 02:40:56.305, task name = , caller = [input_manager_impl.cpp(OnPointerEvent:465)] }
```

从逻辑上看，input event触发应用主线程任务开始执行，但是6s还没有执行完，导致应用冻屏（AppFreeze）；

因此，只需要关注input触发应用执行的具体任务，及对应任务执行超时的原因。

主线程栈：此时运行时状态，栈顶的ark\_jsruntime.so中的GetCurrentThreadId并非持锁阻塞或耗时很长的函数，抓到的栈为瞬时栈，没有参考意义。

```screen
Tid:2918, Name:example.sceneboard
# 00 pc 000000000009f73c /system/lib/ld-musl-aarch64.so.1(8fa55898166cd804dad43d909b5319cc)
# 01 pc 000000000054b7b4 /system/lib64/platformsdk/libark_jsruntime.so(panda::os::thread::GetCurrentThreadId()+12)(7715646e48f750f3dc31e660b056eb43)
# 02 pc 00000000002107a4 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::EcmaVM::CheckThread() const+200)(7715646e48f750f3dc31e660b056eb43)
# 03 pc 0000000000432998 /system/lib64/platformsdk/libark_jsruntime.so(panda::JSNApi::GetHandleAddr(panda::ecmascript::EcmaVM const*, unsigned long)+64)(7715646e48f750f3dc31e660b056eb43)
# 04 pc 000000000003eeb8 /system/lib64/platformsdk/libace_napi.z.so(ArkNativeReference::Get()+32)(c3a760aff0c73a2e76accaf518321fc9)
# 05 pc 0000000000043cb4 /system/lib64/platformsdk/libace_napi.z.so(napi_get_reference_value+48)(c3a760aff0c73a2e76accaf518321fc9)
# 06 pc 0000000000007564 /system/lib64/module/events/libemitter.z.so(OHOS::AppExecFwk::SearchCallbackInfo(napi_env__*, std::__h::variant<unsigned int, std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>>> const&, napi_value__*)+248)(8fe2937855aab3ea839419f952597511)
# 07 pc 0000000000007d8c /system/lib64/module/events/libemitter.z.so(OHOS::AppExecFwk::OnOrOnce(napi_env__*, napi_callback_info__*, bool)+568)(8fe2937855aab3ea839419f952597511)
# 08 pc 00000000000096d8 /system/lib64/module/events/libemitter.z.so(OHOS::AppExecFwk::JS_Once(napi_env__*, napi_callback_info__*) (.cfi)+84)(8fe2937855aab3ea839419f952597511)
# 09 pc 000000000002c8f0 /system/lib64/platformsdk/libace_napi.z.so(ArkNativeFunctionCallBack(panda::JsiRuntimeCallInfo*)+168)(c3a760aff0c73a2e76accaf518321fc9)
# 10 pc 0000000000187b48 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
# 11 pc 00000000002da5fc /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::InterpreterAssembly::Execute(panda::ecmascript::EcmaRuntimeCallInfo*)+416)(7715646e48f750f3dc31e660b056eb43)
# 12 pc 00000000002da5fc /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::InterpreterAssembly::Execute(panda::ecmascript::EcmaRuntimeCallInfo*)+416)(7715646e48f750f3dc31e660b056eb43)
# 13 pc 00000000003954a0 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::JSStableArray::HandleforEachOfStable(panda::ecmascript::JSThread*, panda::ecmascript::JSHandle<panda::ecmascript::JSObject>, panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue>, panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue>, unsigned int, unsigned int&)+596)(7715646e48f750f3dc31e660b056eb43)
# 14 pc 000000000018f4b0 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::builtins::BuiltinsArray::ForEach(panda::ecmascript::EcmaRuntimeCallInfo*)+840)(7715646e48f750f3dc31e660b056eb43)
...
```

接下来排查HiLog流水日志：

首先找到上报APP\_INPUT\_BLOCK的时间点，大约在13:40:59.448。事件上报完后，dfx将卡死的scb杀掉。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/GUuLMSdTTmO9exCtY3vSUA/zh-cn_image_0000002370565628.png)往前推6s左右，可以看到在14:40:53.498左右，有一个点击事件发给了scb。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/D2nnIT24QYCkhPSfaM3j7g/zh-cn_image_0000002404125265.png)这之间的6s存在大量的scb日志，判断是在进行更新渲染。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/dIX7HRRIRxGuK_dJRlthtg/zh-cn_image_0000002411349608.png)

查看对应时间点的trace：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/dNopGaA8RcS6JA7Phk7WWw/zh-cn_image_0000002404045457.png)发现scb主线程被占满，非常繁忙。耗时较长的任务是**CustomNodeUpdate SwiperPage**，后续需排查该组件里为何一直在刷新。

对应领域排查后发现：swiperPage上将themeStyle加入到了key里面，key变化就会触发控件新建流程。

当切换主题或者切换图标风格时，桌面上控件会全量新建，使得主线程繁忙，导致输入事件未响应。

### 修复方法

仅在切换桌面组件风格时，才触发桌面组件的刷新，缩小刷新范围。

### 建议与总结

用户点击触发页面更新时，需要合理控制页面刷新的范围，考虑大量组件、频繁刷新等场景。

## LIFECYCLE\_TIMEOUT类典型案例-加载云图

### 概述

由于主线程中存在耗时操作，导致应用拉起、切前台等过程中卡死并闪退，触发LIFECYCLE\_TIMEOUT，原理可参考[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)。

### 问题现象

用户在打开云笔记时应用卡死后闪退。

### 问题代码

在循环中同步获取云图。

```screen
function xxxFunction1(fileUris : string[]): void {
    // ...
    for (const fileuri of fileUris) {
        let file = fileIo.openSync(fileuri, fileIo.OpenMode.READ_ONLY);
        // ...
    }
    // ...
} // 如果使用同步操作，需要考虑到容器弱网或无网等极端情况发生
```

### 分析思路

详见[应用冻屏类问题定位步骤与思路](bpta-stability-app-freeze-way.md#section1950514261110)。

### 分析步骤

提取故障关键信息：

```screen
sysfreeze: LIFECYCLE_TIMEOUT LIFECYCLE_TIMEOUT at 20240201100459
```

查看MSG信息：**foreground timeout，对应时长为 5s**。

```screen
MSG = 
Fault time:2024/02/01-10:04:57
ability:MainAbility foreground timeout.
server:
312522; AbilityRecord::ForegroundAbility; the ForegroundAbility lifecycle starts.
client:
312522; AbilityThread::ScheduleAbilityTransaction; the foreground lifecycle.
```

LIFECYCLE\_HALF\_TIMEOUT 上报时间为**10:04:57:538**；

LIFECYCLE\_TIMEOUT 上报时间为**10:04:59:965**；相隔约2.5s，符合预期。

```screen
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
DOMAIN:AAFWK
STRINGID:LIFECYCLE_TIMEOUT
TIMESTAMP:2024/02/01-10:04:59:965
PID:18083
UID:20020041
PACKAGE_NAME:com.example.notepad
PROCESS_NAME:com.example.notepad
*******************************************
start time: 2024/02/01-10:04:57:555
DOMAIN = AAFWK
EVENTNAME = LIFECYCLE_HALF_TIMEOUT
TIMESTAMP = 2024/02/01-10:04:57:538
PID = 18083
UID = 20020041
TID = 17286
PACKAGE_NAME = com.example.notepad
PROCESS_NAME = com.example.notepad
```

任务开始的时间为**10:04:54.778**，离LIFECYCLE\_HALF\_TIMEOUT相隔约2.5s，符合预期。

```screen
mainHandler dump is:
 EventHandler dump begin curTime: 2024-02-01 10:04:57.306
 Event runner (Thread name = , Thread ID = 18083) is running
 Current Running: start at 2024-02-01 10:04:54.798, Event { send thread = 18132, send time = 2024-02-01 10:04:54.778, handle time = 2024-02-01 10:04:54.778, task name = UIAbilityThread:SendResult }
 History event queue information:
 No. 0 : Event { send thread = 18083, send time = 2024-02-01 10:04:46.481, handle time = 2024-02-01 10:04:46.981, trigger time = 2024-02-01 10:04:46.982, completeTime time = 2024-02-01 10:04:46.982, task name =  }
 No. 1 : Event { send thread = 18132, send time = 2024-02-01 10:04:47.149, handle time = 2024-02-01 10:04:47.149, trigger time = 2024-02-01 10:04:47.149, completeTime time = 2024-02-01 10:04:47.197, task name = MainThread:BackgroundApplication }
 No. 2 : Event { send thread = 18083, send time = 2024-02-01 10:04:44.329, handle time = 2024-02-01 10:04:47.329, trigger time = 2024-02-01 10:04:47.329, completeTime time = 2024-02-01 10:04:47.329, task name =  }
 No. 3 : Event { send thread = 18087, send time = 2024-02-01 10:04:48.091, handle time = 2024-02-01 10:04:48.091, trigger time = 2024-02-01 10:04:48.091, completeTime time = 2024-02-01 10:04:48.091, task name =  }
 No. 4 : Event { send thread = 18087, send time = 2024-02-01 10:04:51.047, handle time = 2024-02-01 10:04:51.047, trigger time = 2024-02-01 10:04:51.048, completeTime time = 2024-02-01 10:04:51.048, task name =  }
 No. 5 : Event { send thread = 18087, send time = 2024-02-01 10:04:54.067, handle time = 2024-02-01 10:04:54.067, trigger time = 2024-02-01 10:04:54.067, completeTime time = 2024-02-01 10:04:54.067, task name =  }
 ...
```

查看对应的堆栈信息：libfs.z.so->libdatashare\_consumer.z.so->libipc\_core.z.so。

```screen
Tid:18083, Name:ei.example.notepad
# 00 pc 00000000001617a4 /system/lib/ld-musl-aarch64.so.1(ioctl+180)(4ca73cff61bea7c4a687eb0f71c9df69)
# 01 pc 000000000003e8a0 /system/lib64/platformsdk/libipc_core.z.so(OHOS::BinderConnector::WriteBinder(unsigned long, void*)+72)(3248fceb1fa676994734e0437430ce37)
# 02 pc 0000000000049f38 /system/lib64/platformsdk/libipc_core.z.so(OHOS::BinderInvoker::TransactWithDriver(bool)+296)(3248fceb1fa676994734e0437430ce37)
# 03 pc 00000000000496f8 /system/lib64/platformsdk/libipc_core.z.so(OHOS::BinderInvoker::WaitForCompletion(OHOS::MessageParcel*, int*)+116)(3248fceb1fa676994734e0437430ce37)
# 04 pc 00000000000490bc /system/lib64/platformsdk/libipc_core.z.so(OHOS::BinderInvoker::SendRequest(int, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+312)(3248fceb1fa676994734e0437430ce37)
# 05 pc 0000000000027700 /system/lib64/platformsdk/libipc_core.z.so(OHOS::IPCObjectProxy::SendRequestInner(bool, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+132)(3248fceb1fa676994734e0437430ce37)
# 06 pc 000000000002799c /system/lib64/platformsdk/libipc_core.z.so(OHOS::IPCObjectProxy::SendRequest(unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+140)(3248fceb1fa676994734e0437430ce37)
# 07 pc 000000000002640c /system/lib64/platformsdk/libdatashare_consumer.z.so(OHOS::DataShare::DataShareProxy::OpenFile(OHOS::Uri const&, std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&)+440)(e93b5085235269d4b7218ea7de64b69a)
# 08 pc 0000000000014b2c /system/lib64/platformsdk/libdatashare_consumer.z.so(OHOS::DataShare::ExtSpecialController::OpenFile(OHOS::Uri const&, std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&)+160)(e93b5085235269d4b7218ea7de64b69a)
# 09 pc 0000000000022c54 /system/lib64/platformsdk/libdatashare_consumer.z.so(OHOS::DataShare::DataShareHelperImpl::OpenFile(OHOS::Uri&, std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&)+96)(e93b5085235269d4b7218ea7de64b69a)
# 10 pc 0000000000108b34 /system/lib64/module/file/libfs.z.so(OHOS::FileManagement::ModuleFileIO::OpenFileByDatashare(std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&, unsigned int)+468)(152580bf9c379f11f29fdded278541bd)
# 11 pc 0000000000108264 /system/lib64/module/file/libfs.z.so(OHOS::FileManagement::ModuleFileIO::OpenFileByUri(std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&, unsigned int)+1760)(152580bf9c379f11f29fdded278541bd)
# 12 pc 00000000001077fc /system/lib64/module/file/libfs.z.so(OHOS::FileManagement::ModuleFileIO::Open::Sync(napi_env__*, napi_callback_info__*) (.cfi)+1036)(152580bf9c379f11f29fdded278541bd)
# 13 pc 000000000002bbf8 /system/lib64/platformsdk/libace_napi.z.so(ArkNativeFunctionCallBack(panda::JsiRuntimeCallInfo*)+168)(f5b81db475835ee752235c606b1c5e33)
# 14 pc 0000000000132e48 /system/lib64/module/arkcompiler/stub.an
```

通过binder可以看出与5235进程通信时长大于2.5s，符合预期。

```screen
PeerBinderCatcher -- pid==18083 layer_ == 1

BinderCatcher --

    18083:18083 to 5235:7437 code 2 wait:2.723147396 s,  ns:-1:-1 to -1:-1, debug:18083:18083 to 5235:7437, active_code:0 active_thread:0, pending_async_proc=0
    3462:3840 to 4956:4958 code 8 wait:261.213830169 s,  ns:-1:-1 to -1:-1, debug:3462:3840 to 4956:4958, active_code:0 active_thread:0, pending_async_proc=0
    3462:3621 to 4956:4981 code 8 wait:273.550283291 s,  ns:-1:-1 to -1:-1, debug:3462:3621 to 4956:4981, active_code:0 active_thread:0, pending_async_proc=0
```

5235是媒体库进程，该堆栈无有效信息。

```screen
Binder catcher stacktrace, type is peer, pid : 5235
Result: 0 ( no error )
Timestamp:2024-02-01 10:04:57.000
Pid:5235
Uid:20020079
Process name:com.medialibrary.medialibrarydata
Tid:5235, Name:edialibrarydata
# 00 pc 0000000000142d1c /system/lib/ld-musl-aarch64.so.1(epoll_wait+84)(4ca73cff61bea7c4a687eb0f71c9df69)
# 01 pc 000000000000fb74 /system/lib64/chipset-pub-sdk/libeventhandler.z.so(OHOS::AppExecFwk::EpollIoWaiter::WaitFor(std::__h::unique_lock<std::__h::mutex>&, long)+224)(a4d21072c08fd3ac639d5cf5b8fb8b51)
# 02 pc 0000000000019df8 /system/lib64/chipset-pub-sdk/libeventhandler.z.so(OHOS::AppExecFwk::EventQueue::WaitUntilLocked(std::__h::chrono::time_point<std::__h::chrono::steady_clock, std::__h::chrono::duration<long long, std::__h::ratio<1l, 1000000000l>>> const&, std::__h::unique_lock<std::__h::mutex>&)+180)(a4d21072c08fd3ac639d5cf5b8fb8b51)
# 03 pc 0000000000019c6c /system/lib64/chipset-pub-sdk/libeventhandler.z.so(OHOS::AppExecFwk::EventQueue::GetEvent()+128)(a4d21072c08fd3ac639d5cf5b8fb8b51)
# 04 pc 00000000000202b8 /system/lib64/chipset-pub-sdk/libeventhandler.z.so(OHOS::AppExecFwk::(anonymous namespace)::EventRunnerImpl::Run()+1164)(a4d21072c08fd3ac639d5cf5b8fb8b51)
# 05 pc 0000000000022388 /system/lib64/chipset-pub-sdk/libeventhandler.z.so(OHOS::AppExecFwk::EventRunner::Run()+120)(a4d21072c08fd3ac639d5cf5b8fb8b51)
# 06 pc 000000000007ea08 /system/lib64/platformsdk/libappkit_native.z.so(OHOS::AppExecFwk::MainThread::Start()+772)(183fe2babcfdd3e1ea4bca16a0e26a5d)
# 07 pc 0000000000011ac8 /system/bin/appspawn(RunChildProcessor+236)(7b715884c45cfe57b22df46fdaeeca88)
# 08 pc 0000000000034684 /system/bin/appspawn(AppSpawnChild+264)(7b715884c45cfe57b22df46fdaeeca88)
# 09 pc 00000000000344f4 /system/bin/appspawn(AppSpawnProcessMsg+380)(7b715884c45cfe57b22df46fdaeeca88)
# 10 pc 00000000000305a0 /system/bin/appspawn(OnReceiveRequest+1820)(7b715884c45cfe57b22df46fdaeeca88)
# 11 pc 0000000000017c58 /system/lib64/chipset-pub-sdk/libbegetutil.z.so(HandleRecvMsg_+260)(22f33d1b0218f31bad0dcc75cf348b90)
# 12 pc 00000000000178fc /system/lib64/chipset-pub-sdk/libbegetutil.z.so(HandleStreamEvent_+148)(22f33d1b0218f31bad0dcc75cf348b90)
# 13 pc 0000000000015478 /system/lib64/chipset-pub-sdk/libbegetutil.z.so(ProcessEvent+112)(22f33d1b0218f31bad0dcc75cf348b90)
# 14 pc 0000000000015090 /system/lib64/chipset-pub-sdk/libbegetutil.z.so(RunLoop_+308)(22f33d1b0218f31bad0dcc75cf348b90)
# 15 pc 000000000002eff4 /system/bin/appspawn(AppSpawnRun+116)(7b715884c45cfe57b22df46fdaeeca88)
# 16 pc 000000000001f438 /system/bin/appspawn(main+724)(7b715884c45cfe57b22df46fdaeeca88)
# 17 pc 00000000000a0974 /system/lib/ld-musl-aarch64.so.1(libc_start_main_stage2+64)(4ca73cff61bea7c4a687eb0f71c9df69)
# 18 pc 000000000001106c /system/bin/appspawn(_start_c+76)(7b715884c45cfe57b22df46fdaeeca88)
```

以上可以得到信息：应用通过文件系统Open::Sync同步通过uri加载文件，调用datashare请求媒体库文件数据。

查看对应时间点的流水信息：进程调用datashare加载云图后卡死，与堆栈信息吻合。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/1mh1jED1SzaLKTKpAjXFbQ/zh-cn_image_0000002370565632.png)查看具体代码：

在循环中同步加载fileUri是不合理的，当弱网环境或者同时加载大量数据时，极易出现卡死情况，应用侧需进行整改。

### 修复方法

同步加载改为异步加载，并使用标志位标识是否加载完毕，用户界面展示加载中效果。

```screen
function xxxFunction1(fileUris : string[]): void {
    // ...
    for (const fileuri of fileUris) {
        let file = fileIo.openSync(fileuri, fileIo.OpenMode.READ_ONLY);
        // ...
    }
    // ...
} // 如果使用同步操作，需要考虑到容器弱网或无网等极端情况发生
```

修改为：

```screen
async function xxxFunction2(fileUris : string[]) : Promise<void> {
    // ...
    AppStorage.setOrCreate<boolean>('isLoadingPic', true); // 用于页面load效果展示
    for (const fileuri of fileUris) {
        let file = await fileIo.open(fileuri, fileIo.OpenMode.READ_ONLY); // 改为异步加载
        // ...
    }
    // ...
}
```

### 建议与总结

1. 请求云侧数据需要验证充分，包括有网、弱网和无网场景下；
2. 不要在应用生命周期函数中做耗时操作。

## 资源高负载类典型案例

### 概述

该类问题一般由于整机资源问题导致进程执行慢或没有执行，从而出现应用冻屏（AppFreeze）问题。

### 问题现象

进程执行慢或者不执行，导致出现无响应。

### 分析思路

遇到此类问题时，需要结合AppFreeze日志中的日志信息和HiLog流水分析。具体而言就是发生故障时间段内故障进行HiLog打印不多，且故障日志获取的信息之间时间间隔较久，可以怀疑是整机资源出现问题。

### 分析步骤

查看CPU 故障时间内1min、5min和15min的平均负载（Load average）,该数值越大表示此时整机负载越高，数值越接近100表明负载越高，超过100表明负载极高。

```screen
Load average: 129. / 82.1 / 56.9; the cpu load average in 1 min, 5 min and 15 min
```

查看整机剩余可用内存信息（ReclaimAvailBuffer），数值越小表明此时整机可用内存越少，一般低于1G就会出现由于低内存造成的freeze场景。

```screen
MemoryCatcher --
some avg10=69.85 avg60=69.85 avg300=69.85 total=69
full avg10=69.85 avg60=69.85 avg300=69.85 total=69
//...
ReclaimAvailBuffer:                    6914048 kB
//...
```
