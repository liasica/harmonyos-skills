---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rpc
title: @ohos.rpc (RPC通信)
breadcrumb: API参考 > 应用框架 > IPC Kit（进程间通信服务） > ArkTS API > @ohos.rpc (RPC通信)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:91064fbc57144040f6ceb00de6420f69b547309ee975e42b267c29bbff135ab9
---

本模块提供进程间通信能力，包括设备内的进程间通信（IPC）和设备间的进程间通信（RPC），前者基于Binder驱动，后者基于软总线驱动。

说明

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块从API version 9开始支持异常返回功能。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { rpc } from '@kit.IPCKit';
```

## ErrorCode9+

PhonePC/2in1TabletTVWearable

从API version 9起，IPC支持异常返回功能。错误码对应数值及含义如下。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CHECK\_PARAM\_ERROR | 401 | 检查参数失败。 |
| OS\_MMAP\_ERROR | 1900001 | 执行系统调用mmap失败。 |
| OS\_IOCTL\_ERROR | 1900002 | 在共享内存文件描述符上执行系统调用ioctl失败。 |
| WRITE\_TO\_ASHMEM\_ERROR | 1900003 | 向共享内存写数据失败。 |
| READ\_FROM\_ASHMEM\_ERROR | 1900004 | 从共享内存读数据失败。 |
| ONLY\_PROXY\_OBJECT\_PERMITTED\_ERROR | 1900005 | 只有proxy对象允许该操作。 |
| ONLY\_REMOTE\_OBJECT\_PERMITTED\_ERROR | 1900006 | 只有remote对象允许该操作。 |
| COMMUNICATION\_ERROR | 1900007 | 和远端对象进行进程间通信失败。 |
| PROXY\_OR\_REMOTE\_OBJECT\_INVALID\_ERROR | 1900008 | 非法的代理对象或者远端对象。 |
| WRITE\_DATA\_TO\_MESSAGE\_SEQUENCE\_ERROR | 1900009 | 向MessageSequence写数据失败。 |
| READ\_DATA\_FROM\_MESSAGE\_SEQUENCE\_ERROR | 1900010 | 读取MessageSequence数据失败。 |
| PARCEL\_MEMORY\_ALLOC\_ERROR | 1900011 | 序列化过程中内存分配失败。 |
| CALL\_JS\_METHOD\_ERROR | 1900012 | 执行JS回调方法失败。 |
| OS\_DUP\_ERROR | 1900013 | 执行系统调用dup失败。 |

## TypeCode12+

PhonePC/2in1TabletTVWearable

从API version 12起，IPC新增[writeArrayBuffer](js-apis-rpc.md#writearraybuffer12)和[readArrayBuffer](js-apis-rpc.md#readarraybuffer12)方法传递ArrayBuffer数据，传递数据时通过具体类型值来分辨业务是以哪一种TypedArray去进行数据的读写。类型码对应数值及含义如下。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INT8\_ARRAY | 0 | TypedArray类型为INT8\_ARRAY。 |
| UINT8\_ARRAY | 1 | TypedArray类型为UINT8\_ARRAY。 |
| INT16\_ARRAY | 2 | TypedArray类型为INT16\_ARRAY。 |
| UINT16\_ARRAY | 3 | TypedArray类型为UINT16\_ARRAY。 |
| INT32\_ARRAY | 4 | TypedArray类型为INT32\_ARRAY。 |
| UINT32\_ARRAY | 5 | TypedArray类型为UINT32\_ARRAY。 |
| FLOAT32\_ARRAY | 6 | TypedArray类型为FLOAT32\_ARRAY。 |
| FLOAT64\_ARRAY | 7 | TypedArray类型为FLOAT64\_ARRAY。 |
| BIGINT64\_ARRAY | 8 | TypedArray类型为BIGINT64\_ARRAY。 |
| BIGUINT64\_ARRAY | 9 | TypedArray类型为BIGUINT64\_ARRAY。 |

## MessageSequence9+

PhonePC/2in1TabletTVWearable

在RPC或IPC过程中，发送方可以使用MessageSequence提供的写方法，将待发送的数据以特定格式写入该对象。接收方可以使用MessageSequence提供的读方法从该对象中读取特定格式的数据。数据格式包括：基础类型及数组、IPC对象、接口描述符和自定义序列化对象。

### create9+

PhonePC/2in1TabletTVWearable

static create(): MessageSequence

静态方法，创建MessageSequence对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MessageSequence](js-apis-rpc.md#messagesequence9) | 返回创建的MessageSequence对象。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. hilog.info(0x0000, 'testTag', 'data is ' + data);

9. // 当MessageSequence对象不再使用，由业务主动调用reclaim方法去释放资源。
10. data.reclaim();
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
14. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
15. }
```

### reclaim9+

PhonePC/2in1TabletTVWearable

reclaim(): void

释放不再使用的MessageSequence对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let reply = rpc.MessageSequence.create();
7. reply.reclaim();
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### writeRemoteObject9+

PhonePC/2in1TabletTVWearable

writeRemoteObject(obj: IRemoteObject): void

序列化远程对象并将其写入[MessageSequence](js-apis-rpc.md#messagesequence9)对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | [IRemoteObject](js-apis-rpc.md#iremoteobject) | 是 | 要序列化并写入MessageSequence的远程对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900008 | The proxy or remote object is invalid. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestRemoteObject extends rpc.RemoteObject {
6. constructor(descriptor: string) {
7. super(descriptor);
8. }
9. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
10. option: rpc.MessageOption): boolean | Promise<boolean> {
11. // 根据业务实际逻辑，进行相应处理
12. return true;
13. }
14. }

16. try {
17. let data = rpc.MessageSequence.create();
18. let testRemoteObject = new TestRemoteObject("testObject");
19. data.writeRemoteObject(testRemoteObject);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
23. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
24. }
```

### readRemoteObject9+

PhonePC/2in1TabletTVWearable

readRemoteObject(): IRemoteObject

从MessageSequence读取远程对象。此方法用于反序列化MessageSequence对象以生成IRemoteObject。远程对象按写入MessageSequence的顺序读取。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IRemoteObject](js-apis-rpc.md#iremoteobject) | 读取到的远程对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900008 | The proxy or remote object is invalid. |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestRemoteObject extends rpc.RemoteObject {
6. constructor(descriptor: string) {
7. super(descriptor);
8. }
9. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
10. option: rpc.MessageOption): boolean | Promise<boolean> {
11. // 根据业务实际逻辑，进行相应处理
12. return true;
13. }
14. }

16. try {
17. let data = rpc.MessageSequence.create();
18. let testRemoteObject = new TestRemoteObject("testObject");
19. data.writeRemoteObject(testRemoteObject);
20. let proxy = data.readRemoteObject();
21. hilog.info(0x0000, 'testTag', 'readRemoteObject is ' + proxy);
22. } catch (error) {
23. let e: BusinessError = error as BusinessError;
24. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
25. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
26. }
```

### writeInterfaceToken9+

PhonePC/2in1TabletTVWearable

writeInterfaceToken(token: string): void

将接口描述符写入MessageSequence对象，远端对象可使用该信息校验本次通信。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | string | 是 | 字符串类型描述符，其长度应小于40960字节。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.The string length is greater than or equal to 40960 bytes;  4.The number of bytes copied to the buffer is different from the length of the obtained string. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeInterfaceToken("aaa");
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readInterfaceToken9+

PhonePC/2in1TabletTVWearable

readInterfaceToken(): string

从MessageSequence对象中读取接口描述符，接口描述符按写入MessageSequence的顺序读取，本地对象可使用该信息检验本次通信。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回读取到的接口描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeInterfaceToken("aaa");
8. let interfaceToken = data.readInterfaceToken();
9. hilog.info(0x0000, 'testTag', 'RpcServer: interfaceToken is ' + interfaceToken);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### getSize9+

PhonePC/2in1TabletTVWearable

getSize(): number

获取当前创建的MessageSequence对象的数据大小。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取的MessageSequence实例的数据大小。以字节为单位。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. let size = data.getSize();
8. hilog.info(0x0000, 'testTag', 'size is ' + size);
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
12. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
13. }
```

### getCapacity9+

PhonePC/2in1TabletTVWearable

getCapacity(): number

获取当前MessageSequence对象的容量大小。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取的MessageSequence实例的容量大小。以字节为单位。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. let result = data.getCapacity();
8. hilog.info(0x0000, 'testTag', 'capacity is ' + result);
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
12. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
13. }
```

### setSize9+

PhonePC/2in1TabletTVWearable

setSize(size: number): void

设置MessageSequence对象中包含的数据大小。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | MessageSequence实例的数据大小。以字节为单位。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeString('Hello World');
8. data.setSize(16);
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
12. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
13. }
```

### setCapacity9+

PhonePC/2in1TabletTVWearable

setCapacity(size: number): void

设置MessageSequence对象的存储容量。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | MessageSequence实例的存储容量。以字节为单位。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900009 | Failed to write data to the message sequence. |
| 1900011 | Memory allocation failed. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.setCapacity(100);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### getWritableBytes9+

PhonePC/2in1TabletTVWearable

getWritableBytes(): number

获取MessageSequence的可写字节空间大小。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取到的MessageSequence实例的可写字节空间。以字节为单位。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.setCapacity(100);
8. let getWritableBytes = data.getWritableBytes();
9. hilog.info(0x0000, 'testTag', 'RpcServer: getWritableBytes is ' + getWritableBytes);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### getReadableBytes9+

PhonePC/2in1TabletTVWearable

getReadableBytes(): number

获取MessageSequence的可读字节空间。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取到的MessageSequence实例的可读字节空间。以字节为单位。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeString("hello world");
8. let result = data.getReadableBytes();
9. hilog.info(0x0000, 'testTag', 'RpcServer: getReadableBytes is ' + result);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### getReadPosition9+

PhonePC/2in1TabletTVWearable

getReadPosition(): number

获取MessageSequence的读位置。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回MessageSequence实例中的当前读取位置。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeString("hello world");
8. let readPos = data.getReadPosition();
9. hilog.info(0x0000, 'testTag', 'readPos is ' + readPos);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### getWritePosition9+

PhonePC/2in1TabletTVWearable

getWritePosition(): number

获取MessageSequence的写位置。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回MessageSequence实例中的当前写入位置。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeInt(10);
8. let bwPos = data.getWritePosition();
9. hilog.info(0x0000, 'testTag', 'bwPos is ' + bwPos);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### rewindRead9+

PhonePC/2in1TabletTVWearable

rewindRead(pos: number): void

重新偏移读取位置到指定的位置。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pos | number | 是 | 开始读取数据的目标位置。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeInt(12);
8. data.writeString("sequence");
9. let number = data.readInt();
10. hilog.info(0x0000, 'testTag', 'number is ' + number);
11. data.rewindRead(0);
12. let number2 = data.readInt();
13. hilog.info(0x0000, 'testTag', 'rewindRead is ' + number2);
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
17. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
18. }
```

### rewindWrite9+

PhonePC/2in1TabletTVWearable

rewindWrite(pos: number): void

重新偏移写位置到指定的位置。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pos | number | 是 | 开始写入数据的目标位置。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeInt(4);
8. data.rewindWrite(0);
9. data.writeInt(5);
10. let number = data.readInt();
11. hilog.info(0x0000, 'testTag', 'rewindWrite is: ' + number);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
15. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
16. }
```

### writeByte9+

PhonePC/2in1TabletTVWearable

writeByte(val: number): void

将字节值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | number | 是 | 要写入的字节值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeByte(2);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readByte9+

PhonePC/2in1TabletTVWearable

readByte(): number

从MessageSequence实例中读取字节值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回字节值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeByte(2);
8. let ret = data.readByte();
9. hilog.info(0x0000, 'testTag', 'readByte is: ' +  ret);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeShort9+

PhonePC/2in1TabletTVWearable

writeShort(val: number): void

将短整数值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | number | 是 | 要写入的短整数值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeShort(8);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readShort9+

PhonePC/2in1TabletTVWearable

readShort(): number

从MessageSequence实例中读取短整数值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回短整数值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeShort(8);
8. let ret = data.readShort();
9. hilog.info(0x0000, 'testTag', 'readShort is ' + ret);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeInt9+

PhonePC/2in1TabletTVWearable

writeInt(val: number): void

将整数值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | number | 是 | 要写入的整数值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeInt(10);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readInt9+

PhonePC/2in1TabletTVWearable

readInt(): number

从MessageSequence实例中读取整数值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回整数值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeInt(10);
8. let ret = data.readInt();
9. hilog.info(0x0000, 'testTag', 'readInt is ' + ret);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeLong9+

PhonePC/2in1TabletTVWearable

writeLong(val: number): void

将长整数值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | number | 是 | 要写入的长整数值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeLong(10000);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readLong9+

PhonePC/2in1TabletTVWearable

readLong(): number

从MessageSequence实例中读取长整数值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回长整数值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeLong(10000);
8. let ret = data.readLong();
9. hilog.info(0x0000, 'testTag', 'readLong is ' + ret);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeFloat9+

PhonePC/2in1TabletTVWearable

writeFloat(val: number): void

将双精度浮点值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | number | 是 | 要写入的双精度浮点值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeFloat(1.2);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readFloat9+

PhonePC/2in1TabletTVWearable

readFloat(): number

从MessageSequence实例中读取双精度浮点值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回双精度浮点值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeFloat(1.2);
8. let ret = data.readFloat();
9. hilog.info(0x0000, 'testTag', 'readFloat is ' + ret);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeDouble9+

PhonePC/2in1TabletTVWearable

writeDouble(val: number): void

将双精度浮点值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | number | 是 | 要写入的双精度浮点值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeDouble(10.2);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readDouble9+

PhonePC/2in1TabletTVWearable

readDouble(): number

从MessageSequence实例中读取双精度浮点值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回双精度浮点值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeDouble(10.2);
8. let ret = data.readDouble();
9. hilog.info(0x0000, 'testTag', 'readDouble is ' +  ret);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeBoolean9+

PhonePC/2in1TabletTVWearable

writeBoolean(val: boolean): void

将布尔值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | boolean | 是 | 要写入的布尔值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeBoolean(false);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readBoolean9+

PhonePC/2in1TabletTVWearable

readBoolean(): boolean

从MessageSequence实例中读取布尔值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回读取到的布尔值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeBoolean(false);
8. let ret = data.readBoolean();
9. hilog.info(0x0000, 'testTag', 'readBoolean is ' + ret);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeChar9+

PhonePC/2in1TabletTVWearable

writeChar(val: number): void

将单个字符值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | number | 是 | 要写入的单个字符值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeChar(97);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readChar9+

PhonePC/2in1TabletTVWearable

readChar(): number

从MessageSequence实例中读取单个字符值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回单个字符值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeChar(97);
8. let ret = data.readChar();
9. hilog.info(0x0000, 'testTag', 'readChar is ' + ret);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeString9+

PhonePC/2in1TabletTVWearable

writeString(val: string): void

将字符串值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | string | 是 | 要写入的字符串值，其长度应小于40960字节。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.The string length is greater than or equal to 40960 bytes;  4.The number of bytes copied to the buffer is different from the length of the obtained string. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeString('abc');
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readString9+

PhonePC/2in1TabletTVWearable

readString(): string

从MessageSequence实例中读取字符串值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回字符串值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeString('abc');
8. let ret = data.readString();
9. hilog.info(0x0000, 'testTag', 'readString is ' + ret);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeParcelable9+

PhonePC/2in1TabletTVWearable

writeParcelable(val: Parcelable): void

将自定义序列化对象写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | [Parcelable](js-apis-rpc.md#parcelable9) | 是 | 要写入的可序列对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class MyParcelable implements rpc.Parcelable {
6. num: number = 0;
7. str: string = '';
8. constructor( num: number, str: string) {
9. this.num = num;
10. this.str = str;
11. }
12. marshalling(messageSequence: rpc.MessageSequence): boolean {
13. messageSequence.writeInt(this.num);
14. messageSequence.writeString(this.str);
15. return true;
16. }
17. unmarshalling(messageSequence: rpc.MessageSequence): boolean {
18. this.num = messageSequence.readInt();
19. this.str = messageSequence.readString();
20. return true;
21. }
22. }

24. try {
25. let parcelable = new MyParcelable(1, "aaa");
26. let data = rpc.MessageSequence.create();
27. data.writeParcelable(parcelable);
28. } catch (error) {
29. let e: BusinessError = error as BusinessError;
30. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
31. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
32. }
```

### readParcelable9+

PhonePC/2in1TabletTVWearable

readParcelable(dataIn: Parcelable): void

从MessageSequence实例中读取成员变量到指定的对象（dataIn）。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | [Parcelable](js-apis-rpc.md#parcelable9) | 是 | 需要从MessageSequence读取成员变量的对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect. |
| 1900010 | Failed to read data from the message sequence. |
| 1900012 | Failed to call the JS callback function. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class MyParcelable implements rpc.Parcelable {
6. num: number = 0;
7. str: string = '';
8. constructor( num: number, str: string) {
9. this.num = num;
10. this.str = str;
11. }
12. marshalling(messageSequence: rpc.MessageSequence): boolean {
13. messageSequence.writeInt(this.num);
14. messageSequence.writeString(this.str);
15. return true;
16. }
17. unmarshalling(messageSequence: rpc.MessageSequence): boolean {
18. this.num = messageSequence.readInt();
19. this.str = messageSequence.readString();
20. return true;
21. }
22. }

24. try {
25. let parcelable = new MyParcelable(1, "aaa");
26. let data = rpc.MessageSequence.create();
27. data.writeParcelable(parcelable);
28. let ret = new MyParcelable(0, "");
29. data.readParcelable(ret);
30. } catch (error) {
31. let e: BusinessError = error as BusinessError;
32. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
33. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
34. }
```

### writeByteArray9+

PhonePC/2in1TabletTVWearable

writeByteArray(byteArray: number[]): void

将字节数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteArray | number[] | 是 | 要写入的字节数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match;  4.The element does not exist in the array.  5.The type of the element in the array is incorrect. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. let ByteArrayVar = [1, 2, 3, 4, 5];
8. data.writeByteArray(ByteArrayVar);
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
12. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
13. }
```

### readByteArray9+

PhonePC/2in1TabletTVWearable

readByteArray(dataIn: number[]): void

从MessageSequence实例中读取字节数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | number[] | 是 | 要读取的字节数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match. |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. let ByteArrayVar = [1, 2, 3, 4, 5];
8. data.writeByteArray(ByteArrayVar);
9. let array: Array<number> = new Array(5);
10. data.readByteArray(array);
11. hilog.info(0x0000, 'testTag', 'readByteArray is  ' + array);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
15. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
16. }
```

### readByteArray9+

PhonePC/2in1TabletTVWearable

readByteArray(): number[]

从MessageSequence实例中读取字节数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回字节数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. let ByteArrayVar = [1, 2, 3, 4, 5];
8. data.writeByteArray(ByteArrayVar);
9. let array = data.readByteArray();
10. hilog.info(0x0000, 'testTag', 'readByteArray is  ' + array);
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
14. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
15. }
```

### writeShortArray9+

PhonePC/2in1TabletTVWearable

writeShortArray(shortArray: number[]): void

将短整数数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shortArray | number[] | 是 | 要写入的短整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match;  4.The element does not exist in the array;  5.The type of the element in the array is incorrect. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeShortArray([11, 12, 13]);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readShortArray9+

PhonePC/2in1TabletTVWearable

readShortArray(dataIn: number[]): void

从MessageSequence实例中读取短整数数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | number[] | 是 | 要读取的短整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match. |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeShortArray([11, 12, 13]);
8. let array: Array<number> = new Array(3);
9. data.readShortArray(array);
10. hilog.info(0x0000, 'testTag', 'readShortArray is  ' + array);
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
14. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
15. }
```

### readShortArray9+

PhonePC/2in1TabletTVWearable

readShortArray(): number[]

从MessageSequence实例中读取短整数数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回短整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeShortArray([11, 12, 13]);
8. let array = data.readShortArray();
9. hilog.info(0x0000, 'testTag', 'readShortArray is ' + array);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeIntArray9+

PhonePC/2in1TabletTVWearable

writeIntArray(intArray: number[]): void

将整数数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| intArray | number[] | 是 | 要写入的整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match;  4.The element does not exist in the array;  5.The type of the element in the array is incorrect. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeIntArray([100, 111, 112]);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readIntArray9+

PhonePC/2in1TabletTVWearable

readIntArray(dataIn: number[]): void

从MessageSequence实例中读取整数数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | number[] | 是 | 要读取的整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match. |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeIntArray([100, 111, 112]);
8. let array: Array<number> = new Array(3);
9. data.readIntArray(array);
10. hilog.info(0x0000, 'testTag', 'readIntArray is  ' + array);
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
14. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
15. }
```

### readIntArray9+

PhonePC/2in1TabletTVWearable

readIntArray(): number[]

从MessageSequence实例中读取整数数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeIntArray([100, 111, 112]);
8. let array = data.readIntArray();
9. hilog.info(0x0000, 'testTag', 'readIntArray is ' + array);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeLongArray9+

PhonePC/2in1TabletTVWearable

writeLongArray(longArray: number[]): void

将长整数数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| longArray | number[] | 是 | 要写入的长整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match;  4.The element does not exist in the array;  5.The type of the element in the array is incorrect. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeLongArray([1111, 1112, 1113]);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readLongArray9+

PhonePC/2in1TabletTVWearable

readLongArray(dataIn: number[]): void

从MessageSequence实例中读取的长整数数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | number[] | 是 | 要读取的长整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match. |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeLongArray([1111, 1112, 1113]);
8. let array: Array<number> = new Array(3);
9. data.readLongArray(array);
10. hilog.info(0x0000, 'testTag', 'readLongArray is ' + array);
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
14. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
15. }
```

### readLongArray9+

PhonePC/2in1TabletTVWearable

readLongArray(): number[]

从MessageSequence实例中读取所有的长整数数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回长整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeLongArray([1111, 1112, 1113]);
8. let array = data.readLongArray();
9. hilog.info(0x0000, 'testTag', 'readLongArray is ' + array);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeFloatArray9+

PhonePC/2in1TabletTVWearable

writeFloatArray(floatArray: number[]): void

将双精度浮点数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| floatArray | number[] | 是 | 要写入的双精度浮点数组。由于系统内部对float类型的数据是按照double处理的，使用时对于数组所占的总字节数应按照double类型来计算。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match;  4.The element does not exist in the array;  5.The type of the element in the array is incorrect. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeFloatArray([1.2, 1.3, 1.4]);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readFloatArray9+

PhonePC/2in1TabletTVWearable

readFloatArray(dataIn: number[]): void

从MessageSequence实例中读取双精度浮点数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | number[] | 是 | 要读取的双精度浮点数组。由于系统内部对float类型的数据是按照double处理的，使用时对于数组所占的总字节数应按照double类型来计算。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match. |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeFloatArray([1.2, 1.3, 1.4]);
8. let array: Array<number> = new Array(3);
9. data.readFloatArray(array);
10. hilog.info(0x0000, 'testTag', 'readFloatArray is ' + array);
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
14. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
15. }
```

### readFloatArray9+

PhonePC/2in1TabletTVWearable

readFloatArray(): number[]

从MessageSequence实例中读取双精度浮点数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回双精度浮点数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeFloatArray([1.2, 1.3, 1.4]);
8. let array = data.readFloatArray();
9. hilog.info(0x0000, 'testTag', 'readFloatArray is ' + array);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeDoubleArray9+

PhonePC/2in1TabletTVWearable

writeDoubleArray(doubleArray: number[]): void

将双精度浮点数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| doubleArray | number[] | 是 | 要写入的双精度浮点数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match;  4.The element does not exist in the array;  5.The type of the element in the array is incorrect. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeDoubleArray([11.1, 12.2, 13.3]);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readDoubleArray9+

PhonePC/2in1TabletTVWearable

readDoubleArray(dataIn: number[]): void

从MessageSequence实例中读取双精度浮点数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | number[] | 是 | 要读取的双精度浮点数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match. |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeDoubleArray([11.1, 12.2, 13.3]);
8. let array: Array<number> = new Array(3);
9. data.readDoubleArray(array);
10. hilog.info(0x0000, 'testTag', 'readDoubleArray is ' + array);
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
14. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
15. }
```

### readDoubleArray9+

PhonePC/2in1TabletTVWearable

readDoubleArray(): number[]

从MessageSequence实例中读取所有双精度浮点数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回双精度浮点数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeDoubleArray([11.1, 12.2, 13.3]);
8. let array = data.readDoubleArray();
9. hilog.info(0x0000, 'testTag', 'readDoubleArray is ' + array);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeBooleanArray9+

PhonePC/2in1TabletTVWearable

writeBooleanArray(booleanArray: boolean[]): void

将布尔数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| booleanArray | boolean[] | 是 | 要写入的布尔数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match;  4.The element does not exist in the array. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeBooleanArray([false, true, false]);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readBooleanArray9+

PhonePC/2in1TabletTVWearable

readBooleanArray(dataIn: boolean[]): void

从MessageSequence实例中读取布尔数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | boolean[] | 是 | 要读取的布尔数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match. |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeBooleanArray([false, true, false]);
8. let array: Array<boolean> = new Array(3);
9. data.readBooleanArray(array);
10. hilog.info(0x0000, 'testTag', 'readBooleanArray is ' + array);
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
14. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
15. }
```

### readBooleanArray9+

PhonePC/2in1TabletTVWearable

readBooleanArray(): boolean[]

从MessageSequence实例中读取所有布尔数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean[] | 返回布尔数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeBooleanArray([false, true, false]);
8. let array = data.readBooleanArray();
9. hilog.info(0x0000, 'testTag', 'readBooleanArray is ' + array);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeCharArray9+

PhonePC/2in1TabletTVWearable

writeCharArray(charArray: number[]): void

将单个字符数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| charArray | number[] | 是 | 要写入的单个字符数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match;  4.The element does not exist in the array. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeCharArray([97, 98, 88]);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readCharArray9+

PhonePC/2in1TabletTVWearable

readCharArray(dataIn: number[]): void

从MessageSequence实例中读取单个字符数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | number[] | 是 | 要读取的单个字符数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match. |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeCharArray([97, 98, 88]);
8. let array: Array<number> = new Array(3);
9. data.readCharArray(array);
10. hilog.info(0x0000, 'testTag', 'readCharArray is ' + array);
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
14. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
15. }
```

### readCharArray9+

PhonePC/2in1TabletTVWearable

readCharArray(): number[]

从MessageSequence实例中读取单个字符数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回单个字符数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeCharArray([97, 98, 88]);
8. let array = data.readCharArray();
9. hilog.info(0x0000, 'testTag', 'readCharArray is ' + array);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeStringArray9+

PhonePC/2in1TabletTVWearable

writeStringArray(stringArray: string[]): void

将字符串数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stringArray | string[] | 是 | 要写入的字符串数组，数组单个元素的长度应小于40960字节。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match;  4.The string length is greater than or equal to 40960 bytes;  5.The number of bytes copied to the buffer is different from the length of the obtained string. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeStringArray(["abc", "def"]);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### readStringArray9+

PhonePC/2in1TabletTVWearable

readStringArray(dataIn: string[]): void

从MessageSequence实例中读取字符串数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | string[] | 是 | 要读取的字符串数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match. |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeStringArray(["abc", "def"]);
8. let array: Array<string> = new Array(2);
9. data.readStringArray(array);
10. hilog.info(0x0000, 'testTag', 'readStringArray is ' + array);
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
14. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
15. }
```

### readStringArray9+

PhonePC/2in1TabletTVWearable

readStringArray(): string[]

从MessageSequence实例中读取字符串数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 返回字符串数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let data = rpc.MessageSequence.create();
7. data.writeStringArray(["abc", "def"]);
8. let array = data.readStringArray();
9. hilog.info(0x0000, 'testTag', 'readStringArray is ' + array);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### writeNoException9+

PhonePC/2in1TabletTVWearable

writeNoException(): void

向MessageSequence写入“指示未发生异常”的信息。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestRemoteObject extends rpc.RemoteObject {
6. constructor(descriptor: string) {
7. super(descriptor);
8. }
9. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
10. option: rpc.MessageOption): boolean | Promise<boolean> {
11. if (code === 1) {
12. hilog.info(0x0000, 'testTag', 'RpcServer: onRemoteMessageRequest called');
13. try {
14. reply.writeNoException();
15. } catch (error) {
16. let e: BusinessError = error as BusinessError;
17. hilog.error(0x0000, 'testTag', 'rpc write no exception fail, errorCode ' + e.code);
18. hilog.error(0x0000, 'testTag', 'rpc write no exception fail, errorMessage ' + e.message);
19. }
20. return true;
21. } else {
22. hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
23. return false;
24. }
25. }
26. }
```

### readException9+

PhonePC/2in1TabletTVWearable

readException(): void

从MessageSequence中读取异常。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

说明

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // FA模型需要从@kit.AbilityKit导入featureAbility
2. // import { featureAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { Want, common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. let proxy: rpc.IRemoteObject | undefined;
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x0000, 'testTag', 'js onConnect called');
11. proxy = remoteProxy;
12. },
13. onDisconnect: (elementName) => {
14. hilog.info(0x0000, 'testTag', 'onDisconnect');
15. },
16. onFailed: () => {
17. hilog.info(0x0000, 'testTag', 'onFailed');
18. }
19. };
20. let want: Want = {
21. // 获取服务端包名和ability名称
22. bundleName: "com.ohos.server",
23. abilityName: "com.ohos.server.EntryAbility",
24. };

26. // FA模型使用此方法连接服务
27. // FA.connectAbility(want,connect);

29. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
30. let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
31. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
32. let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的sendMessageRequest接口方法发送消息

```
1. import { rpc } from '@kit.IPCKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. try {
6. let option = new rpc.MessageOption();
7. let data = rpc.MessageSequence.create();
8. let reply = rpc.MessageSequence.create();
9. data.writeNoException();
10. data.writeInt(6);
11. if (proxy != undefined) {
12. proxy.sendMessageRequest(1, data, reply, option)
13. .then((result: rpc.RequestResult) => {
14. if (result.errCode === 0) {
15. hilog.info(0x0000, 'testTag', 'sendMessageRequest got result');
16. result.reply.readException();
17. let num = result.reply.readInt();
18. hilog.info(0x0000, 'testTag', 'reply num: ' + num);
19. } else {
20. hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode: ' + result.errCode);
21. }
22. }).catch((e: Error) => {
23. hilog.error(0x0000, 'testTag', 'sendMessageRequest got exception: ' + JSON.stringify(e));
24. }).finally (() => {
25. hilog.info(0x0000, 'testTag', 'sendMessageRequest ends, reclaim parcel');
26. data.reclaim();
27. reply.reclaim();
28. });
29. }
30. } catch (error) {
31. let e: BusinessError = error as BusinessError;
32. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
33. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
34. }
```

### writeParcelableArray9+

PhonePC/2in1TabletTVWearable

writeParcelableArray(parcelableArray: Parcelable[]): void

将可序列化对象数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parcelableArray | [Parcelable](js-apis-rpc.md#parcelable9)[] | 是 | 要写入的可序列化对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match;  4.The element does not exist in the array. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class MyParcelable implements rpc.Parcelable {
6. num: number = 0;
7. str: string = '';
8. constructor(num: number, str: string) {
9. this.num = num;
10. this.str = str;
11. }
12. marshalling(messageSequence: rpc.MessageSequence): boolean {
13. messageSequence.writeInt(this.num);
14. messageSequence.writeString(this.str);
15. return true;
16. }
17. unmarshalling(messageSequence: rpc.MessageSequence): boolean {
18. this.num = messageSequence.readInt();
19. this.str = messageSequence.readString();
20. return true;
21. }
22. }

24. try {
25. let parcelable = new MyParcelable(1, "aaa");
26. let parcelable2 = new MyParcelable(2, "bbb");
27. let parcelable3 = new MyParcelable(3, "ccc");
28. let a = [parcelable, parcelable2, parcelable3];
29. let data = rpc.MessageSequence.create();
30. data.writeParcelableArray(a);
31. } catch (error) {
32. let e: BusinessError = error as BusinessError;
33. hilog.error(0x0000, 'testTag', 'rpc write parcelable array fail, errorCode ' + e.code);
34. hilog.error(0x0000, 'testTag', 'rpc write parcelable array fail, errorMessage ' + e.message);
35. }
```

### readParcelableArray9+

PhonePC/2in1TabletTVWearable

readParcelableArray(parcelableArray: Parcelable[]): void

从MessageSequence实例中读取可序列化对象数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parcelableArray | [Parcelable](js-apis-rpc.md#parcelable9)[] | 是 | 要读取的可序列化对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match;  4.The length of the array passed when reading is not equal to the length passed when writing to the array;  5.The element does not exist in the array. |
| 1900010 | Failed to read data from the message sequence. |
| 1900012 | Failed to call the JS callback function. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class MyParcelable implements rpc.Parcelable {
6. num: number = 0;
7. str: string = '';
8. constructor(num: number, str: string) {
9. this.num = num;
10. this.str = str;
11. }
12. marshalling(messageSequence: rpc.MessageSequence): boolean {
13. messageSequence.writeInt(this.num);
14. messageSequence.writeString(this.str);
15. return true;
16. }
17. unmarshalling(messageSequence: rpc.MessageSequence): boolean {
18. this.num = messageSequence.readInt();
19. this.str = messageSequence.readString();
20. return true;
21. }
22. }

24. try {
25. let parcelable = new MyParcelable(1, "aaa");
26. let parcelable2 = new MyParcelable(2, "bbb");
27. let parcelable3 = new MyParcelable(3, "ccc");
28. let a = [parcelable, parcelable2, parcelable3];
29. let data = rpc.MessageSequence.create();
30. data.writeParcelableArray(a);
31. let b = [new MyParcelable(0, ""), new MyParcelable(0, ""), new MyParcelable(0, "")];
32. data.readParcelableArray(b);
33. } catch (error) {
34. let e: BusinessError = error as BusinessError;
35. hilog.error(0x0000, 'testTag', 'rpc write parcelable array fail, errorCode ' + e.code);
36. hilog.error(0x0000, 'testTag', 'rpc write parcelable array fail, errorMessage ' + e.message);
37. }
```

### writeRemoteObjectArray9+

PhonePC/2in1TabletTVWearable

writeRemoteObjectArray(objectArray: IRemoteObject[]): void

将IRemoteObject对象数组写入MessageSequence。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| objectArray | [IRemoteObject](js-apis-rpc.md#iremoteobject)[] | 是 | 要写入MessageSequence的IRemoteObject对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match;  4.The element does not exist in the array;  5.The obtained remoteObject is null. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestRemoteObject extends rpc.RemoteObject {
6. constructor(descriptor: string) {
7. super(descriptor);
8. }
9. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
10. option: rpc.MessageOption): boolean | Promise<boolean> {
11. // 根据业务实际逻辑，进行相应处理
12. return true;
13. }
14. }

16. try {
17. let a = [new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"), new TestRemoteObject("testObject3")];
18. let data = rpc.MessageSequence.create();
19. data.writeRemoteObjectArray(a);
20. } catch (error) {
21. let e: BusinessError = error as BusinessError;
22. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
23. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
24. }
```

### readRemoteObjectArray9+

PhonePC/2in1TabletTVWearable

readRemoteObjectArray(objects: IRemoteObject[]): void

从MessageSequence读取IRemoteObject对象数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| objects | [IRemoteObject](js-apis-rpc.md#iremoteobject)[] | 是 | 从MessageSequence读取的IRemoteObject对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match;  4.The length of the array passed when reading is not equal to the length passed when writing to the array. |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestRemoteObject extends rpc.RemoteObject {
6. constructor(descriptor: string) {
7. super(descriptor);
8. }
9. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
10. option: rpc.MessageOption): boolean | Promise<boolean> {
11. // 根据业务实际逻辑，进行相应处理
12. return true;
13. }
14. }

16. try {
17. let a = [new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"), new TestRemoteObject("testObject3")];
18. let data = rpc.MessageSequence.create();
19. data.writeRemoteObjectArray(a);
20. let b: Array<rpc.IRemoteObject> = new Array(3);
21. data.readRemoteObjectArray(b);
22. hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + b);
23. } catch (error) {
24. let e: BusinessError = error as BusinessError;
25. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
26. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
27. }
```

### readRemoteObjectArray9+

PhonePC/2in1TabletTVWearable

readRemoteObjectArray(): IRemoteObject[]

从MessageSequence读取IRemoteObject对象数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IRemoteObject](js-apis-rpc.md#iremoteobject)[] | 返回IRemoteObject对象数组；当写入的是空数组时，返回的是null。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestRemoteObject extends rpc.RemoteObject {
6. constructor(descriptor: string) {
7. super(descriptor);
8. }
9. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
10. option: rpc.MessageOption): boolean | Promise<boolean> {
11. // 根据业务实际逻辑，进行相应处理
12. return true;
13. }
14. }

16. try {
17. let a = [new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"), new TestRemoteObject("testObject3")];
18. let data = rpc.MessageSequence.create();
19. let b = data.readRemoteObjectArray();
20. hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + b);
21. } catch (error) {
22. let e: BusinessError = error as BusinessError;
23. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
24. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
25. }
```

### closeFileDescriptor9+

PhonePC/2in1TabletTVWearable

static closeFileDescriptor(fd: number): void

静态方法，关闭给定的文件描述符。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 要关闭的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. try {
7. let filePath = "path/to/file";
8. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
9. rpc.MessageSequence.closeFileDescriptor(file.fd);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### dupFileDescriptor9+

PhonePC/2in1TabletTVWearable

static dupFileDescriptor(fd: number): number

静态方法，复制给定的文件描述符。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 表示已存在的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回新的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900013 | Failed to call dup. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. try {
7. let filePath = "path/to/file";
8. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
9. rpc.MessageSequence.dupFileDescriptor(file.fd);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### containFileDescriptors9+

PhonePC/2in1TabletTVWearable

containFileDescriptors(): boolean

检查此MessageSequence对象是否包含文件描述符。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：包含文件描述符，false：不包含文件描述符。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. try {
7. let sequence = rpc.MessageSequence.create();
8. let filePath = "path/to/file";
9. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
10. let containFD = sequence.containFileDescriptors();
11. hilog.info(0x0000, 'testTag', 'sequence after write fd containFd result is ' + containFD);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
15. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
16. }
```

### writeFileDescriptor9+

PhonePC/2in1TabletTVWearable

writeFileDescriptor(fd: number): void

写入文件描述符到MessageSequence。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. try {
7. let sequence = rpc.MessageSequence.create();
8. let filePath = "path/to/file";
9. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
10. sequence.writeFileDescriptor(file.fd);
11. } catch (error) {
12. let e: BusinessError = error as BusinessError;
13. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
14. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
15. }
```

### readFileDescriptor9+

PhonePC/2in1TabletTVWearable

readFileDescriptor(): number

从MessageSequence中读取文件描述符。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. try {
7. let sequence = rpc.MessageSequence.create();
8. let filePath = "path/to/file";
9. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
10. sequence.writeFileDescriptor(file.fd);
11. let readFD = sequence.readFileDescriptor();
12. hilog.info(0x0000, 'testTag', 'readFileDescriptor is ' + readFD);
13. } catch (error) {
14. let e: BusinessError = error as BusinessError;
15. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
16. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
17. }
```

### writeAshmem9+

PhonePC/2in1TabletTVWearable

writeAshmem(ashmem: Ashmem): void

将指定的匿名共享对象写入此MessageSequence。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ashmem | [Ashmem](js-apis-rpc.md#ashmem8) | 是 | 要写入MessageSequence的匿名共享对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter is not an instance of the Ashmem object. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let sequence = rpc.MessageSequence.create();
7. let ashmem = rpc.Ashmem.create("ashmem", 1024);
8. // ashmem里写入数据
9. let buffer = new ArrayBuffer(1024);
10. let int32View = new Int32Array(buffer);
11. for (let i = 0; i < int32View.length; i++) {
12. int32View[i] = i * 2 + 1;
13. }
14. let size = buffer.byteLength;
15. ashmem.mapReadWriteAshmem();
16. ashmem.writeDataToAshmem(buffer, size, 0);
17. // 将ashmem对象写入messageSequence对象中
18. sequence.writeAshmem(ashmem);
19. // 将传递的数据大小写入messageSequence对象中
20. sequence.writeInt(size);
21. } catch (error) {
22. let e: BusinessError = error as BusinessError;
23. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
24. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
25. }
```

### readAshmem9+

PhonePC/2in1TabletTVWearable

readAshmem(): Ashmem

从MessageSequence读取匿名共享对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Ashmem](js-apis-rpc.md#ashmem8) | 返回匿名共享对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let sequence = rpc.MessageSequence.create();
7. let ashmem = rpc.Ashmem.create("ashmem", 1024);
8. // ashmem里写入数据
9. let buffer = new ArrayBuffer(1024);
10. let int32View = new Int32Array(buffer);
11. for (let i = 0; i < int32View.length; i++) {
12. int32View[i] = i * 2 + 1;
13. }
14. let size = buffer.byteLength;
15. ashmem.mapReadWriteAshmem();
16. ashmem.writeDataToAshmem(buffer, size, 0);
17. // 将传递的数据大小写入messageSequence对象中
18. sequence.writeInt(size);
19. // 将ashmem对象写入messageSequence对象中
20. sequence.writeAshmem(ashmem);

22. // 读取传递的数据大小
23. let dataSize = sequence.readInt();
24. // 从messageSequence对象中读取ashmem对象
25. let ashmem1 = sequence.readAshmem();
26. // 从ashmem对象中读取数据
27. ashmem1.mapReadWriteAshmem();
28. let readResult = ashmem1.readDataFromAshmem(dataSize, 0);
29. let readInt32View = new Int32Array(readResult);
30. hilog.info(0x0000, 'testTag', 'read from Ashmem result is ' + readInt32View);
31. } catch (error) {
32. let e: BusinessError = error as BusinessError;
33. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
34. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
35. }
```

### getRawDataCapacity9+

PhonePC/2in1TabletTVWearable

getRawDataCapacity(): number

获取MessageSequence可以容纳的最大原始数据量。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回MessageSequence可以容纳的最大原始数据量，即128MB。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let sequence = rpc.MessageSequence.create();
7. let result = sequence.getRawDataCapacity();
8. hilog.info(0x0000, 'testTag', 'sequence get RawDataCapacity result is ' + result);
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
12. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
13. }
```

### writeRawData(deprecated)

PhonePC/2in1TabletTVWearable

writeRawData(rawData: number[], size: number): void

将原始数据写入MessageSequence对象。

说明

从API version 9 开始支持，API version 11 开始废弃，建议使用[writeRawDataBuffer](js-apis-rpc.md#writerawdatabuffer11)替代。

该接口是一次性接口，不允许在一次parcel通信中多次调用该接口。

该接口在传输数据时，当数据量较大时（超过32KB），会使用共享内存传输数据，此时需注意selinux配置。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rawData | number[] | 是 | 要写入的原始数据，大小不能超过128MB。 |
| size | number | 是 | 发送的原始数据大小，以字节为单位。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match;  4.The transferred size cannot be obtained;  5.The transferred size is less than or equal to 0;  6.The element does not exist in the array;  7.Failed to obtain typedArray information;  8.The array is not of type int32;  9.The length of typedarray is smaller than the size of the original data sent. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let sequence = rpc.MessageSequence.create();
7. let arr = [1, 2, 3, 4, 5];
8. sequence.writeRawData(arr, arr.length);
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
12. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
13. }
```

### writeRawDataBuffer11+

PhonePC/2in1TabletTVWearable

writeRawDataBuffer(rawData: ArrayBuffer, size: number): void

将原始数据写入MessageSequence对象。

说明

该接口是一次性接口，不允许在一次parcel通信中多次调用该接口。

该接口在传输数据时，当数据量较大时（超过32KB），会使用共享内存传输数据，此时需注意selinux配置。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rawData | ArrayBuffer | 是 | 要写入的原始数据，大小不能超过128MB。 |
| size | number | 是 | 发送的原始数据大小，以字节为单位。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.Failed to obtain arrayBuffer information;  4.The transferred size cannot be obtained;  5.The transferred size is less than or equal to 0;  6.The transferred size is greater than the byte length of ArrayBuffer. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let buffer = new ArrayBuffer(64 * 1024);
7. let int32View = new Int32Array(buffer);
8. for (let i = 0; i < int32View.length; i++) {
9. int32View[i] = i * 2 + 1;
10. }
11. let size = buffer.byteLength;
12. let sequence = rpc.MessageSequence.create();
13. sequence.writeRawDataBuffer(buffer, size);
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
17. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
18. }
```

### readRawData(deprecated)

PhonePC/2in1TabletTVWearable

readRawData(size: number): number[]

从MessageSequence读取原始数据。

说明

从API version 9 开始支持，API version 11 开始废弃，建议使用[readRawDataBuffer](js-apis-rpc.md#readrawdatabuffer11)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 要读取的原始数据的大小。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回原始数据（以字节为单位）。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let sequence = rpc.MessageSequence.create();
7. let arr = [1, 2, 3, 4, 5];
8. sequence.writeRawData(arr, arr.length);
9. let size = arr.length;
10. let result = sequence.readRawData(size);
11. hilog.info(0x0000, 'testTag', 'sequence read raw data result is ' + result);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
15. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
16. }
```

### readRawDataBuffer11+

PhonePC/2in1TabletTVWearable

readRawDataBuffer(size: number): ArrayBuffer

从MessageSequence读取原始数据。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 要读取的原始数据的大小。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 返回原始数据（以字节为单位）。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let buffer = new ArrayBuffer(64 * 1024);
7. let int32View = new Int32Array(buffer);
8. for (let i = 0; i < int32View.length; i++) {
9. int32View[i] = i * 2 + 1;
10. }
11. let size = buffer.byteLength;
12. let sequence = rpc.MessageSequence.create();
13. sequence.writeRawDataBuffer(buffer, size);
14. let result = sequence.readRawDataBuffer(size);
15. let readInt32View = new Int32Array(result);
16. hilog.info(0x0000, 'testTag', 'sequence read raw data result is ' + readInt32View);
17. } catch (error) {
18. let e: BusinessError = error as BusinessError;
19. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
20. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
21. }
```

### writeArrayBuffer12+

PhonePC/2in1TabletTVWearable

writeArrayBuffer(buf: ArrayBuffer, typeCode: TypeCode): void

将ArrayBuffer类型数据写入MessageSequence对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 要写入的ArrayBuffer数据。 |
| typeCode | [TypeCode](js-apis-rpc.md#typecode12) | 是 | ArrayBuffer数据具体是以哪一种TypedArray来访问和操作(会根据业务传递的类型枚举值去决定底层的写入方式，需要业务正确传递枚举值。) |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The parameter is an empty array;  2.The number of parameters is incorrect;  3.The parameter type does not match;  4.The obtained value of typeCode is incorrect;  5.Failed to obtain arrayBuffer information. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```
1. // TypeCode 类型枚举较多，示例代码以Int16Array为例
2. import { rpc } from '@kit.IPCKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. try {
7. let data = rpc.MessageSequence.create();
8. let buffer = new ArrayBuffer(10);
9. let int16View = new Int16Array(buffer);
10. for (let i = 0; i < int16View.length; i++) {
11. int16View[i] = i * 2 + 1;
12. }
13. data.writeArrayBuffer(buffer, rpc.TypeCode.INT16_ARRAY);
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
17. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
18. }
```

### readArrayBuffer12+

PhonePC/2in1TabletTVWearable

readArrayBuffer(typeCode: TypeCode): ArrayBuffer

从MessageSequence读取ArrayBuffer类型数据。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typeCode | [TypeCode](js-apis-rpc.md#typecode12) | 是 | ArrayBuffer数据具体是以哪一种TypedArray来访问和操作(会根据业务传递的类型枚举值去决定底层的读取方式，需要业务正确传递枚举值，读写枚举值不匹配会导致数据异常。) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 返回ArrayBuffer类型数据（以字节为单位）。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.The obtained value of typeCode is incorrect; |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```
1. // TypeCode 类型枚举较多，示例代码以Int16Array为例
2. import { rpc } from '@kit.IPCKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. try {
7. let data = rpc.MessageSequence.create();
8. let buffer = new ArrayBuffer(10);
9. let int16View = new Int16Array(buffer);
10. for (let i = 0; i < int16View.length; i++) {
11. int16View[i] = i * 2 + 1;
12. }
13. data.writeArrayBuffer(buffer, rpc.TypeCode.INT16_ARRAY);
14. let result = data.readArrayBuffer(rpc.TypeCode.INT16_ARRAY);
15. let readInt16View = new Int16Array(result);
16. hilog.info(0x0000, 'testTag', 'read ArrayBuffer result is ' + readInt16View);
17. } catch (error) {
18. let e: BusinessError = error as BusinessError;
19. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
20. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
21. }
```

## MessageParcel(deprecated)

PhonePC/2in1TabletTVWearable

在RPC过程中，发送方可以使用MessageParcel提供的写方法，将待发送的数据以特定格式写入该对象。接收方可以使用MessageParcel提供的读方法从该对象中读取特定格式的数据。数据格式包括：基础类型及数组、IPC对象、接口描述符和自定义序列化对象。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[MessageSequence](js-apis-rpc.md#messagesequence9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

### create(deprecated)

PhonePC/2in1TabletTVWearable

static create(): MessageParcel

静态方法，创建MessageParcel对象。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[create](js-apis-rpc.md#create9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 返回创建的MessageParcel对象。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. hilog.info(0x0000, 'testTag', 'data is ' + data);

8. // 当MessageParcel对象不再使用，由业务主动调用reclaim方法去释放资源。
9. data.reclaim();
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### reclaim(deprecated)

PhonePC/2in1TabletTVWearable

reclaim(): void

释放不再使用的MessageParcel对象。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[reclaim](js-apis-rpc.md#reclaim9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let reply = rpc.MessageParcel.create();
6. reply.reclaim();
7. } catch (error) {
8. hilog.error(0x0000, 'testTag', 'error ' + error);
9. }
```

### writeRemoteObject(deprecated)

PhonePC/2in1TabletTVWearable

writeRemoteObject(object: IRemoteObject): boolean

序列化远程对象并将其写入MessageParcel对象。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeRemoteObject](js-apis-rpc.md#writeremoteobject9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| object | [IRemoteObject](js-apis-rpc.md#iremoteobject) | 是 | 要序列化并写入MessageParcel的远程对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：操作成功，false：操作失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class TestRemoteObject extends rpc.RemoteObject {
5. constructor(descriptor: string) {
6. super(descriptor);
7. }
8. onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
9. // 根据业务实际逻辑，进行相应处理
10. return true;
11. }
12. }

14. try {
15. let data = rpc.MessageParcel.create();
16. let testRemoteObject = new TestRemoteObject("testObject");
17. data.writeRemoteObject(testRemoteObject);
18. } catch (error) {
19. hilog.error(0x0000, 'testTag', 'error ' + error);
20. }
```

### readRemoteObject(deprecated)

PhonePC/2in1TabletTVWearable

readRemoteObject(): IRemoteObject

从MessageParcel读取远程对象。此方法用于反序列化MessageParcel对象以生成IRemoteObject。远程对象按写入MessageParcel的顺序读取。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readRemoteObject](js-apis-rpc.md#readremoteobject9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IRemoteObject](js-apis-rpc.md#iremoteobject) | 读取到的远程对象。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class TestRemoteObject extends rpc.RemoteObject {
5. constructor(descriptor: string) {
6. super(descriptor);
7. }
8. onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
9. option: rpc.MessageOption): boolean {
10. // 根据业务实际逻辑，进行相应处理
11. return true;
12. }
13. }

15. try {
16. let data = rpc.MessageParcel.create();
17. let testRemoteObject = new TestRemoteObject("testObject");
18. data.writeRemoteObject(testRemoteObject);
19. let proxy = data.readRemoteObject();
20. hilog.info(0x0000, 'testTag', 'readRemoteObject is ' + proxy);
21. } catch (error) {
22. hilog.error(0x0000, 'testTag', 'error ' + error);
23. }
```

### writeInterfaceToken(deprecated)

PhonePC/2in1TabletTVWearable

writeInterfaceToken(token: string): boolean

将接口描述符写入MessageParcel对象，远端对象可使用该信息校验本次通信。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeInterfaceToken](js-apis-rpc.md#writeinterfacetoken9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | string | 是 | 字符串类型描述符，其长度应小于40960字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：操作成功，false：操作失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeInterfaceToken("aaa");
7. hilog.info(0x0000, 'testTag', 'RpcServer: writeInterfaceToken is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readInterfaceToken(deprecated)

PhonePC/2in1TabletTVWearable

readInterfaceToken(): string

从MessageParcel中读取接口描述符，接口描述符按写入MessageParcel的顺序读取，本地对象可使用该信息检验本次通信。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readInterfaceToken](js-apis-rpc.md#readinterfacetoken9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回读取到的接口描述符。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeInterfaceToken("aaa");
7. let interfaceToken = data.readInterfaceToken();
8. hilog.info(0x0000, 'testTag', 'RpcServer: interfaceToken is ' + interfaceToken);
9. } catch (error) {
10. hilog.error(0x0000, 'testTag', 'error ' + error);
11. }
```

### getSize(deprecated)

PhonePC/2in1TabletTVWearable

getSize(): number

获取当前MessageParcel的数据大小。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[getSize](js-apis-rpc.md#getsize9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取的MessageParcel的数据大小。以字节为单位。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. data.writeInt(1);
7. let size = data.getSize();
8. hilog.info(0x0000, 'testTag', 'size is ' + size);
9. } catch (error) {
10. hilog.error(0x0000, 'testTag', 'error ' + error);
11. }
```

### getCapacity(deprecated)

PhonePC/2in1TabletTVWearable

getCapacity(): number

获取当前MessageParcel的容量。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[getCapacity](js-apis-rpc.md#getcapacity9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取的MessageParcel的容量大小。以字节为单位。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.getCapacity();
7. hilog.info(0x0000, 'testTag', 'capacity is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### setSize(deprecated)

PhonePC/2in1TabletTVWearable

setSize(size: number): boolean

设置MessageParcel实例中包含的数据大小。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[setSize](js-apis-rpc.md#setsize9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | MessageParcel实例的数据大小。以字节为单位。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：设置成功，false：设置失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let setSize = data.setSize(16);
7. hilog.info(0x0000, 'testTag', 'setSize is ' + setSize);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### setCapacity(deprecated)

PhonePC/2in1TabletTVWearable

setCapacity(size: number): boolean

设置MessageParcel实例的存储容量。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[setCapacity](js-apis-rpc.md#setcapacity9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | MessageParcel实例的存储容量。以字节为单位。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：设置成功，false：设置失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.setCapacity(100);
7. hilog.info(0x0000, 'testTag', 'setCapacity is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### getWritableBytes(deprecated)

PhonePC/2in1TabletTVWearable

getWritableBytes(): number

获取MessageParcel的可写字节空间。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[getWritableBytes](js-apis-rpc.md#getwritablebytes9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取到的MessageParcel的可写字节空间。以字节为单位。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. data.writeInt(1);
7. let getWritableBytes = data.getWritableBytes();
8. hilog.info(0x0000, 'testTag', 'RpcServer: getWritableBytes is ' + getWritableBytes);
9. } catch (error) {
10. hilog.error(0x0000, 'testTag', 'error ' + error);
11. }
```

### getReadableBytes(deprecated)

PhonePC/2in1TabletTVWearable

getReadableBytes(): number

获取MessageParcel的可读字节空间。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[getReadableBytes](js-apis-rpc.md#getreadablebytes9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取到的MessageParcel的可读字节空间。以字节为单位。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. data.writeInt(1);
7. let result = data.getReadableBytes();
8. hilog.info(0x0000, 'testTag', 'RpcServer: getReadableBytes is ' + result);
9. } catch (error) {
10. hilog.error(0x0000, 'testTag', 'error ' + error);
11. }
```

### getReadPosition(deprecated)

PhonePC/2in1TabletTVWearable

getReadPosition(): number

获取MessageParcel的读位置。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[getReadPosition](js-apis-rpc.md#getreadposition9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回MessageParcel实例中的当前读取位置。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let readPos = data.getReadPosition();
7. hilog.info(0x0000, 'testTag', 'readPos is ' + readPos);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### getWritePosition(deprecated)

PhonePC/2in1TabletTVWearable

getWritePosition(): number

获取MessageParcel的写位置。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[getWritePosition](js-apis-rpc.md#getwriteposition9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回MessageParcel实例中的当前写入位置。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. data.writeInt(10);
7. let bwPos = data.getWritePosition();
8. hilog.info(0x0000, 'testTag', 'bwPos is ' + bwPos);
9. } catch (error) {
10. hilog.error(0x0000, 'testTag', 'error ' + error);
11. }
```

### rewindRead(deprecated)

PhonePC/2in1TabletTVWearable

rewindRead(pos: number): boolean

重新偏移读取位置到指定的位置。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[rewindRead](js-apis-rpc.md#rewindread9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pos | number | 是 | 开始读取数据的目标位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：读取位置发生更改，false：读取位置未发生更改。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. data.writeInt(12);
7. data.writeString("parcel");
8. let number = data.readInt();
9. hilog.info(0x0000, 'testTag', 'number is ' + number);
10. data.rewindRead(0);
11. let number2 = data.readInt();
12. hilog.info(0x0000, 'testTag', 'rewindRead is ' + number2);
13. } catch (error) {
14. hilog.error(0x0000, 'testTag', 'error ' + error);
15. }
```

### rewindWrite(deprecated)

PhonePC/2in1TabletTVWearable

rewindWrite(pos: number): boolean

重新偏移写位置到指定的位置。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[rewindWrite](js-apis-rpc.md#rewindwrite9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pos | number | 是 | 开始写入数据的目标位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入位置发生更改，false：写入位置未发生更改。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. data.writeInt(4);
7. data.rewindWrite(0);
8. data.writeInt(5);
9. let number = data.readInt();
10. hilog.info(0x0000, 'testTag', 'rewindWrite is ' + number);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
```

### writeByte(deprecated)

PhonePC/2in1TabletTVWearable

writeByte(val: number): boolean

将字节值写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeByte](js-apis-rpc.md#writebyte9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | number | 是 | 要写入的字节值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeByte(2);
7. hilog.info(0x0000, 'testTag', 'writeByte is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readByte(deprecated)

PhonePC/2in1TabletTVWearable

readByte(): number

从MessageParcel实例中读取字节值。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readByte](js-apis-rpc.md#readbyte9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回字节值。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeByte(2);
7. hilog.info(0x0000, 'testTag', 'writeByte is ' + result);
8. let ret = data.readByte();
9. hilog.info(0x0000, 'testTag', 'readByte is ' + ret);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeShort(deprecated)

PhonePC/2in1TabletTVWearable

writeShort(val: number): boolean

将短整数值写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeShort](js-apis-rpc.md#writeshort9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | number | 是 | 要写入的短整数值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeShort(8);
7. hilog.info(0x0000, 'testTag', 'writeShort is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readShort(deprecated)

PhonePC/2in1TabletTVWearable

readShort(): number

从MessageParcel实例中读取短整数值。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readShort](js-apis-rpc.md#readshort9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回短整数值。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeShort(8);
7. hilog.info(0x0000, 'testTag', 'writeShort is ' + result);
8. let ret = data.readShort();
9. hilog.info(0x0000, 'testTag', 'readShort is ' + ret);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeInt(deprecated)

PhonePC/2in1TabletTVWearable

writeInt(val: number): boolean

将整数值写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeInt](js-apis-rpc.md#writeint9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | number | 是 | 要写入的整数值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeInt(10);
7. hilog.info(0x0000, 'testTag', 'writeInt is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readInt(deprecated)

PhonePC/2in1TabletTVWearable

readInt(): number

从MessageParcel实例中读取整数值。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readInt](js-apis-rpc.md#readint9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回整数值。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeInt(10);
7. hilog.info(0x0000, 'testTag', 'writeInt is ' + result);
8. let ret = data.readInt();
9. hilog.info(0x0000, 'testTag', 'readInt is ' + ret);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeLong(deprecated)

PhonePC/2in1TabletTVWearable

writeLong(val: number): boolean

将长整数值写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeLong](js-apis-rpc.md#writelong9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | number | 是 | 要写入的长整数值 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeLong(10000);
7. hilog.info(0x0000, 'testTag', 'writeLong is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readLong(deprecated)

PhonePC/2in1TabletTVWearable

readLong(): number

从MessageParcel实例中读取长整数值。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readLong](js-apis-rpc.md#readlong9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回长整数值。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeLong(10000);
7. hilog.info(0x0000, 'testTag', 'writeLong is ' + result);
8. let ret = data.readLong();
9. hilog.info(0x0000, 'testTag', 'readLong is ' + ret);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeFloat(deprecated)

PhonePC/2in1TabletTVWearable

writeFloat(val: number): boolean

将双精度浮点值写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeFloat](js-apis-rpc.md#writefloat9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | number | 是 | 要写入的双精度浮点值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeFloat(1.2);
7. hilog.info(0x0000, 'testTag', 'writeFloat is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readFloat(deprecated)

PhonePC/2in1TabletTVWearable

readFloat(): number

从MessageParcel实例中读取双精度浮点值。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readFloat](js-apis-rpc.md#readfloat9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回双精度浮点值。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeFloat(1.2);
7. hilog.info(0x0000, 'testTag', 'writeFloat is ' + result);
8. let ret = data.readFloat();
9. hilog.info(0x0000, 'testTag', 'readFloat is ' + ret);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeDouble(deprecated)

PhonePC/2in1TabletTVWearable

writeDouble(val: number): boolean

将双精度浮点值写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeDouble](js-apis-rpc.md#writedouble9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | number | 是 | 要写入的双精度浮点值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeDouble(10.2);
7. hilog.info(0x0000, 'testTag', 'writeDouble is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readDouble(deprecated)

PhonePC/2in1TabletTVWearable

readDouble(): number

从MessageParcel实例中读取双精度浮点值。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readDouble](js-apis-rpc.md#readdouble9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回双精度浮点值。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeDouble(10.2);
7. hilog.info(0x0000, 'testTag', 'writeDouble is ' + result);
8. let ret = data.readDouble();
9. hilog.info(0x0000, 'testTag', 'readDouble is ' + ret);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeBoolean(deprecated)

PhonePC/2in1TabletTVWearable

writeBoolean(val: boolean): boolean

将布尔值写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeBoolean](js-apis-rpc.md#writeboolean9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | boolean | 是 | 要写入的布尔值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeBoolean(false);
7. hilog.info(0x0000, 'testTag', 'writeBoolean is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readBoolean(deprecated)

PhonePC/2in1TabletTVWearable

readBoolean(): boolean

从MessageParcel实例中读取布尔值。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readBoolean](js-apis-rpc.md#readboolean9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回读取到的布尔值。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeBoolean(false);
7. hilog.info(0x0000, 'testTag', 'writeBoolean is ' + result);
8. let ret = data.readBoolean();
9. hilog.info(0x0000, 'testTag', 'readBoolean is ' + ret);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeChar(deprecated)

PhonePC/2in1TabletTVWearable

writeChar(val: number): boolean

将单个字符值写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeChar](js-apis-rpc.md#writechar9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | number | 是 | 要写入的单个字符值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeChar(97);
7. hilog.info(0x0000, 'testTag', 'writeChar is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readChar(deprecated)

PhonePC/2in1TabletTVWearable

readChar(): number

从MessageParcel实例中读取单个字符值。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readChar](js-apis-rpc.md#readchar9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回单个字符值。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeChar(97);
7. hilog.info(0x0000, 'testTag', 'writeChar is ' + result);
8. let ret = data.readChar();
9. hilog.info(0x0000, 'testTag', 'readChar is ' + ret);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeString(deprecated)

PhonePC/2in1TabletTVWearable

writeString(val: string): boolean

将字符串值写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeString](js-apis-rpc.md#writestring9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | string | 是 | 要写入的字符串值，其长度应小于40960字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeString('abc');
7. hilog.info(0x0000, 'testTag', 'writeString is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readString(deprecated)

PhonePC/2in1TabletTVWearable

readString(): string

从MessageParcel实例中读取字符串值。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readString](js-apis-rpc.md#readstring9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回字符串值。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeString('abc');
7. hilog.info(0x0000, 'testTag', 'writeString is ' + result);
8. let ret = data.readString();
9. hilog.info(0x0000, 'testTag', 'readString is ' + ret);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeSequenceable(deprecated)

PhonePC/2in1TabletTVWearable

writeSequenceable(val: Sequenceable): boolean

将自定义序列化对象写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeParcelable](js-apis-rpc.md#writeparcelable9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | [Sequenceable](js-apis-rpc.md#sequenceabledeprecated) | 是 | 要写入的可序列对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class MySequenceable implements rpc.Sequenceable {
5. num: number = 0;
6. str: string = '';
7. constructor(num: number, str: string) {
8. this.num = num;
9. this.str = str;
10. }
11. marshalling(messageParcel: rpc.MessageParcel): boolean {
12. messageParcel.writeInt(this.num);
13. messageParcel.writeString(this.str);
14. return true;
15. }
16. unmarshalling(messageParcel: rpc.MessageParcel): boolean {
17. this.num = messageParcel.readInt();
18. this.str = messageParcel.readString();
19. return true;
20. }
21. }

23. try {
24. let sequenceable = new MySequenceable(1, "aaa");
25. let data = rpc.MessageParcel.create();
26. let result = data.writeSequenceable(sequenceable);
27. hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
28. } catch (error) {
29. hilog.error(0x0000, 'testTag', 'error ' + error);
30. }
```

### readSequenceable(deprecated)

PhonePC/2in1TabletTVWearable

readSequenceable(dataIn: Sequenceable): boolean

从MessageParcel实例中读取成员变量到指定的对象（dataIn）。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readParcelable](js-apis-rpc.md#readparcelable9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | [Sequenceable](js-apis-rpc.md#sequenceabledeprecated) | 是 | 需要从MessageParcel读取成员变量的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：反序列化成功，false：反序列化失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class MySequenceable implements rpc.Sequenceable {
5. num: number = 0;
6. str: string = '';
7. constructor(num: number, str: string) {
8. this.num = num;
9. this.str = str;
10. }
11. marshalling(messageParcel: rpc.MessageParcel): boolean {
12. messageParcel.writeInt(this.num);
13. messageParcel.writeString(this.str);
14. return true;
15. }
16. unmarshalling(messageParcel: rpc.MessageParcel): boolean {
17. this.num = messageParcel.readInt();
18. this.str = messageParcel.readString();
19. return true;
20. }
21. }

23. try {
24. let sequenceable = new MySequenceable(1, "aaa");
25. let data = rpc.MessageParcel.create();
26. let result = data.writeSequenceable(sequenceable);
27. hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
28. let ret = new MySequenceable(0, "");
29. let result2 = data.readSequenceable(ret);
30. hilog.info(0x0000, 'testTag', 'readSequenceable is ' + result2);
31. } catch (error) {
32. hilog.error(0x0000, 'testTag', 'error ' + error);
33. }
```

### writeByteArray(deprecated)

PhonePC/2in1TabletTVWearable

writeByteArray(byteArray: number[]): boolean

将字节数组写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeByteArray](js-apis-rpc.md#writebytearray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteArray | number[] | 是 | 要写入的字节数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let ByteArrayVar = [1, 2, 3, 4, 5];
7. let result = data.writeByteArray(ByteArrayVar);
8. hilog.info(0x0000, 'testTag', 'writeByteArray is ' + result);
9. } catch (error) {
10. hilog.error(0x0000, 'testTag', 'error ' + error);
11. }
```

### readByteArray(deprecated)

PhonePC/2in1TabletTVWearable

readByteArray(dataIn: number[]): void

从MessageParcel实例中读取字节数组，并将其写入到创建的空数组中。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readByteArray](js-apis-rpc.md#readbytearray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | number[] | 是 | 要读取的字节数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let ByteArrayVar = [1, 2, 3, 4, 5];
7. let result = data.writeByteArray(ByteArrayVar);
8. let array: Array<number> = new Array(5);
9. data.readByteArray(array);
10. hilog.info(0x0000, 'testTag', 'readByteArray is ' + array);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
```

### readByteArray(deprecated)

PhonePC/2in1TabletTVWearable

readByteArray(): number[]

从MessageParcel实例中读取字节数组。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readByteArray](js-apis-rpc.md#readbytearray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回字节数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let ByteArrayVar = [1, 2, 3, 4, 5];
7. let result = data.writeByteArray(ByteArrayVar);
8. hilog.info(0x0000, 'testTag', 'writeByteArray is ' + result);
9. let array = data.readByteArray();
10. hilog.info(0x0000, 'testTag', 'readByteArray is ' + array);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
```

### writeShortArray(deprecated)

PhonePC/2in1TabletTVWearable

writeShortArray(shortArray: number[]): boolean

将短整数数组写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeShortArray](js-apis-rpc.md#writeshortarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shortArray | number[] | 是 | 要写入的短整数数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeShortArray([11, 12, 13]);
7. hilog.info(0x0000, 'testTag', 'writeShortArray is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readShortArray(deprecated)

PhonePC/2in1TabletTVWearable

readShortArray(dataIn: number[]): void

从MessageParcel实例中读取短整数数组，并将其写入到创建的空数组中。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readShortArray](js-apis-rpc.md#readshortarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | number[] | 是 | 要读取的短整数数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeShortArray([11, 12, 13]);
7. hilog.info(0x0000, 'testTag', 'writeShortArray is ' + result);
8. let array: Array<number> = new Array(3);
9. data.readShortArray(array);
10. hilog.info(0x0000, 'testTag', 'readShortArray is ' + array);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
```

### readShortArray(deprecated)

PhonePC/2in1TabletTVWearable

readShortArray(): number[]

从MessageParcel实例中读取短整数数组。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readShortArray](js-apis-rpc.md#readshortarray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回短整数数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeShortArray([11, 12, 13]);
7. hilog.info(0x0000, 'testTag', 'writeShortArray is ' + result);
8. let array = data.readShortArray();
9. hilog.info(0x0000, 'testTag', 'readShortArray is ' + array);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeIntArray(deprecated)

PhonePC/2in1TabletTVWearable

writeIntArray(intArray: number[]): boolean

将整数数组写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeIntArray](js-apis-rpc.md#writeintarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| intArray | number[] | 是 | 要写入的整数数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeIntArray([100, 111, 112]);
7. hilog.info(0x0000, 'testTag', 'writeIntArray is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readIntArray(deprecated)

PhonePC/2in1TabletTVWearable

readIntArray(dataIn: number[]): void

从MessageParcel实例中读取整数数组，并将其写入到创建的空数组中。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readIntArray](js-apis-rpc.md#readintarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | number[] | 是 | 要读取的整数数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeIntArray([100, 111, 112]);
7. hilog.info(0x0000, 'testTag', 'writeIntArray is ' + result);
8. let array: Array<number> = new Array(3);
9. data.readIntArray(array);
10. hilog.info(0x0000, 'testTag', 'readIntArray is ' + array);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
```

### readIntArray(deprecated)

PhonePC/2in1TabletTVWearable

readIntArray(): number[]

从MessageParcel实例中读取整数数组。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readIntArray](js-apis-rpc.md#readintarray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回整数数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeIntArray([100, 111, 112]);
7. hilog.info(0x0000, 'testTag', 'writeIntArray is ' + result);
8. let array = data.readIntArray();
9. hilog.info(0x0000, 'testTag', 'readIntArray is ' + array);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeLongArray(deprecated)

PhonePC/2in1TabletTVWearable

writeLongArray(longArray: number[]): boolean

将长整数数组写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeLongArray](js-apis-rpc.md#writelongarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| longArray | number[] | 是 | 要写入的长整数数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeLongArray([1111, 1112, 1113]);
7. hilog.info(0x0000, 'testTag', 'writeLongArray is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readLongArray(deprecated)

PhonePC/2in1TabletTVWearable

readLongArray(dataIn: number[]): void

从MessageParcel实例中读取长整数数组，并将其写入到创建的空数组中。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readLongArray](js-apis-rpc.md#readlongarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | number[] | 是 | 要读取的长整数数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeLongArray([1111, 1112, 1113]);
7. hilog.info(0x0000, 'testTag', 'writeLongArray is ' + result);
8. let array: Array<number> = new Array(3);
9. data.readLongArray(array);
10. hilog.info(0x0000, 'testTag', 'readLongArray is ' + array);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
```

### readLongArray(deprecated)

PhonePC/2in1TabletTVWearable

readLongArray(): number[]

从MessageParcel实例中读取长整数数组。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readLongArray](js-apis-rpc.md#readlongarray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回长整数数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeLongArray([1111, 1112, 1113]);
7. hilog.info(0x0000, 'testTag', 'writeLongArray is ' + result);
8. let array = data.readLongArray();
9. hilog.info(0x0000, 'testTag', 'readLongArray is ' + array);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeFloatArray(deprecated)

PhonePC/2in1TabletTVWearable

writeFloatArray(floatArray: number[]): boolean

将双精度浮点数组写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeFloatArray](js-apis-rpc.md#writefloatarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| floatArray | number[] | 是 | 要写入的双精度浮点数组。由于系统内部对float类型的数据是按照double处理的，使用时对于数组所占的总字节数应按照double类型来计算。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeFloatArray([1.2, 1.3, 1.4]);
7. hilog.info(0x0000, 'testTag', 'writeFloatArray is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readFloatArray(deprecated)

PhonePC/2in1TabletTVWearable

readFloatArray(dataIn: number[]): void

从MessageParcel实例中读取双精度浮点数组，并将其写入到创建的空数组中。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readFloatArray](js-apis-rpc.md#readfloatarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | number[] | 是 | 要读取的双精度浮点数组。由于系统内部对float类型的数据是按照double处理的，使用时对于数组所占的总字节数应按照double类型来计算。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeFloatArray([1.2, 1.3, 1.4]);
7. hilog.info(0x0000, 'testTag', 'writeFloatArray is ' + result);
8. let array: Array<number> = new Array(3);
9. data.readFloatArray(array);
10. hilog.info(0x0000, 'testTag', 'readFloatArray is ' + array);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
```

### readFloatArray(deprecated)

PhonePC/2in1TabletTVWearable

readFloatArray(): number[]

从MessageParcel实例中读取双精度浮点数组。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readFloatArray](js-apis-rpc.md#readfloatarray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回双精度浮点数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeFloatArray([1.2, 1.3, 1.4]);
7. hilog.info(0x0000, 'testTag', 'writeFloatArray is ' + result);
8. let array = data.readFloatArray();
9. hilog.info(0x0000, 'testTag', 'readFloatArray is ' + array);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeDoubleArray(deprecated)

PhonePC/2in1TabletTVWearable

writeDoubleArray(doubleArray: number[]): boolean

将双精度浮点数组写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeDoubleArray](js-apis-rpc.md#writedoublearray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| doubleArray | number[] | 是 | 要写入的双精度浮点数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeDoubleArray([11.1, 12.2, 13.3]);
7. hilog.info(0x0000, 'testTag', 'writeDoubleArray is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readDoubleArray(deprecated)

PhonePC/2in1TabletTVWearable

readDoubleArray(dataIn: number[]): void

从MessageParcel实例中读取双精度浮点数组，并将其写入到创建的空数组中。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readDoubleArray](js-apis-rpc.md#readdoublearray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | number[] | 是 | 要读取的双精度浮点数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeDoubleArray([11.1, 12.2, 13.3]);
7. hilog.info(0x0000, 'testTag', 'writeDoubleArray is ' + result);
8. let array: Array<number> = new Array(3);
9. data.readDoubleArray(array);
10. hilog.info(0x0000, 'testTag', 'readDoubleArray is ' + array);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
```

### readDoubleArray(deprecated)

PhonePC/2in1TabletTVWearable

readDoubleArray(): number[]

从MessageParcel实例中读取双精度浮点数组。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readDoubleArray](js-apis-rpc.md#readdoublearray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回双精度浮点数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeDoubleArray([11.1, 12.2, 13.3]);
7. hilog.info(0x0000, 'testTag', 'writeDoubleArray is ' + result);
8. let array = data.readDoubleArray();
9. hilog.info(0x0000, 'testTag', 'readDoubleArray is ' + array);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeBooleanArray(deprecated)

PhonePC/2in1TabletTVWearable

writeBooleanArray(booleanArray: boolean[]): boolean

将布尔数组写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeBooleanArray](js-apis-rpc.md#writebooleanarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| booleanArray | boolean[] | 是 | 要写入的布尔数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeBooleanArray([false, true, false]);
7. hilog.info(0x0000, 'testTag', 'writeBooleanArray is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readBooleanArray(deprecated)

PhonePC/2in1TabletTVWearable

readBooleanArray(dataIn: boolean[]): void

从MessageParcel实例中读取布尔数组，并将其写入到创建的空数组中。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readBooleanArray](js-apis-rpc.md#readbooleanarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | boolean[] | 是 | 要读取的布尔数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeBooleanArray([false, true, false]);
7. hilog.info(0x0000, 'testTag', 'writeBooleanArray is ' + result);
8. let array: Array<boolean> = new Array(3);
9. data.readBooleanArray(array);
10. hilog.info(0x0000, 'testTag', 'readBooleanArray is ' + array);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
```

### readBooleanArray(deprecated)

PhonePC/2in1TabletTVWearable

readBooleanArray(): boolean[]

从MessageParcel实例中读取布尔数组。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readBooleanArray](js-apis-rpc.md#readbooleanarray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean[] | 返回布尔数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeBooleanArray([false, true, false]);
7. hilog.info(0x0000, 'testTag', 'writeBooleanArray is ' + result);
8. let array = data.readBooleanArray();
9. hilog.info(0x0000, 'testTag', 'readBooleanArray is ' + array);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeCharArray(deprecated)

PhonePC/2in1TabletTVWearable

writeCharArray(charArray: number[]): boolean

将单个字符数组写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeCharArray](js-apis-rpc.md#writechararray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| charArray | number[] | 是 | 要写入的单个字符数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeCharArray([97, 98, 88]);
7. hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readCharArray(deprecated)

PhonePC/2in1TabletTVWearable

readCharArray(dataIn: number[]): void

从MessageParcel实例中读取单个字符数组，并将其写入到创建的空数组中。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readCharArray](js-apis-rpc.md#readchararray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | number[] | 是 | 要读取的单个字符数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeCharArray([97, 98, 99]);
7. hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
8. let array: Array<number> = new Array(3);
9. data.readCharArray(array);
10. hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
```

### readCharArray(deprecated)

PhonePC/2in1TabletTVWearable

readCharArray(): number[]

从MessageParcel实例中读取单个字符数组。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readCharArray](js-apis-rpc.md#readchararray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回单个字符数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeCharArray([97, 98, 99]);
7. hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
8. let array = data.readCharArray();
9. hilog.info(0x0000, 'testTag', 'readCharArray is ' + array);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeStringArray(deprecated)

PhonePC/2in1TabletTVWearable

writeStringArray(stringArray: string[]): boolean

将字符串数组写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeStringArray](js-apis-rpc.md#writestringarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stringArray | string[] | 是 | 要写入的字符串数组，数组单个元素的长度应小于40960字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeStringArray(["abc", "def"]);
7. hilog.info(0x0000, 'testTag', 'writeStringArray is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### readStringArray(deprecated)

PhonePC/2in1TabletTVWearable

readStringArray(dataIn: string[]): void

从MessageParcel实例中读取字符串数组，并将其写入到创建的空数组中。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readStringArray](js-apis-rpc.md#readstringarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | string[] | 是 | 要读取的字符串数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeStringArray(["abc", "def"]);
7. hilog.info(0x0000, 'testTag', 'writeStringArray is ' + result);
8. let array: Array<string> = new Array(2);
9. data.readStringArray(array);
10. hilog.info(0x0000, 'testTag', 'readStringArray is ' + array);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
```

### readStringArray(deprecated)

PhonePC/2in1TabletTVWearable

readStringArray(): string[]

从MessageParcel实例中读取字符串数组。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[readStringArray](js-apis-rpc.md#readstringarray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 返回字符串数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let data = rpc.MessageParcel.create();
6. let result = data.writeStringArray(["abc", "def"]);
7. hilog.info(0x0000, 'testTag', 'writeStringArray is ' + result);
8. let array = data.readStringArray();
9. hilog.info(0x0000, 'testTag', 'readStringArray is ' + array);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### writeNoException(deprecated)

PhonePC/2in1TabletTVWearable

writeNoException(): void

向MessageParcel写入“指示未发生异常”的信息。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[writeNoException](js-apis-rpc.md#writenoexception9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class MyDeathRecipient implements rpc.DeathRecipient {
5. onRemoteDied() {
6. hilog.info(0x0000, 'testTag', 'server died');
7. }
8. }
9. class TestRemoteObject extends rpc.RemoteObject {
10. constructor(descriptor: string) {
11. super(descriptor);
12. }

14. onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
15. if (code === 1) {
16. hilog.info(0x0000, 'testTag', 'RpcServer: onRemoteRequest called');
17. reply.writeNoException();
18. return true;
19. } else {
20. hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
21. return false;
22. }
23. }
24. }
```

### readException(deprecated)

PhonePC/2in1TabletTVWearable

readException(): void

从MessageParcel中读取异常。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[readException](js-apis-rpc.md#readexception9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**示例：**

说明

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // FA模型需要从@kit.AbilityKit导入featureAbility
2. // import { featureAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { Want, common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. let proxy: rpc.IRemoteObject | undefined;
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x0000, 'testTag', 'js onConnect called');
11. proxy = remoteProxy;
12. },
13. onDisconnect: (elementName) => {
14. hilog.info(0x0000, 'testTag', 'onDisconnect');
15. },
16. onFailed: () => {
17. hilog.info(0x0000, 'testTag', 'onFailed');
18. }
19. };
20. let want: Want = {
21. // 获取服务端包名和ability名称
22. bundleName: "com.ohos.server",
23. abilityName: "com.ohos.server.EntryAbility",
24. };

26. // FA模型使用此方法连接服务
27. // FA.connectAbility(want,connect);

29. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
30. let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
31. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
32. let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的sendRequest接口方法发送消息

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let option = new rpc.MessageOption();
6. let data = rpc.MessageParcel.create();
7. let reply = rpc.MessageParcel.create();
8. data.writeNoException();
9. data.writeString('hello');
10. if (proxy != undefined) {
11. let a = proxy.sendRequest(1, data, reply, option) as Object;
12. let b = a as Promise<rpc.SendRequestResult>;
13. b.then((result: rpc.SendRequestResult) => {
14. if (result.errCode === 0) {
15. hilog.info(0x0000, 'testTag', 'sendRequest got result');
16. result.reply.readException();
17. let msg = result.reply.readString();
18. hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
19. } else {
20. hilog.error(0x0000, 'testTag', 'sendRequest failed, errCode: ' + result.errCode);
21. }
22. }).catch((e: Error) => {
23. hilog.error(0x0000, 'testTag', 'sendRequest got exception: ' + JSON.stringify(e));
24. }).finally (() => {
25. hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
26. data.reclaim();
27. reply.reclaim();
28. });
29. }
30. } catch (error) {
31. hilog.error(0x0000, 'testTag', 'error ' + error);
32. }
```

### writeSequenceableArray(deprecated)

PhonePC/2in1TabletTVWearable

writeSequenceableArray(sequenceableArray: Sequenceable[]): boolean

将可序列化对象数组写入MessageParcel实例。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeParcelableArray](js-apis-rpc.md#writeparcelablearray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sequenceableArray | [Sequenceable](js-apis-rpc.md#sequenceabledeprecated)[] | 是 | 要写入的可序列化对象数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class MySequenceable implements rpc.Sequenceable {
5. num: number = 0;
6. str: string = '';
7. constructor(num: number, str: string) {
8. this.num = num;
9. this.str = str;
10. }
11. marshalling(messageParcel: rpc.MessageParcel): boolean {
12. messageParcel.writeInt(this.num);
13. messageParcel.writeString(this.str);
14. return true;
15. }
16. unmarshalling(messageParcel: rpc.MessageParcel): boolean {
17. this.num = messageParcel.readInt();
18. this.str = messageParcel.readString();
19. return true;
20. }
21. }

23. try {
24. let sequenceable = new MySequenceable(1, "aaa");
25. let sequenceable2 = new MySequenceable(2, "bbb");
26. let sequenceable3 = new MySequenceable(3, "ccc");
27. let a = [sequenceable, sequenceable2, sequenceable3];
28. let data = rpc.MessageParcel.create();
29. let result = data.writeSequenceableArray(a);
30. hilog.info(0x0000, 'testTag', 'writeSequenceableArray is ' + result);
31. } catch (error) {
32. hilog.error(0x0000, 'testTag', 'error ' + error);
33. }
```

### readSequenceableArray(deprecated)

PhonePC/2in1TabletTVWearable

readSequenceableArray(sequenceableArray: Sequenceable[]): void

从MessageParcel实例中读取可序列化对象数组。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[readParcelableArray](js-apis-rpc.md#readparcelablearray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sequenceableArray | [Sequenceable](js-apis-rpc.md#sequenceabledeprecated)[] | 是 | 要读取的可序列化对象数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class MySequenceable implements rpc.Sequenceable {
5. num: number = 0;
6. str: string = '';
7. constructor(num: number, str: string) {
8. this.num = num;
9. this.str = str;
10. }
11. marshalling(messageParcel: rpc.MessageParcel): boolean {
12. messageParcel.writeInt(this.num);
13. messageParcel.writeString(this.str);
14. return true;
15. }
16. unmarshalling(messageParcel: rpc.MessageParcel): boolean {
17. this.num = messageParcel.readInt();
18. this.str = messageParcel.readString();
19. return true;
20. }
21. }

23. try {
24. let sequenceable = new MySequenceable(1, "aaa");
25. let sequenceable2 = new MySequenceable(2, "bbb");
26. let sequenceable3 = new MySequenceable(3, "ccc");
27. let a = [sequenceable, sequenceable2, sequenceable3];
28. let data = rpc.MessageParcel.create();
29. let result = data.writeSequenceableArray(a);
30. hilog.info(0x0000, 'testTag', 'writeSequenceableArray is ' + result);
31. let b = [new MySequenceable(0, ""), new MySequenceable(0, ""), new MySequenceable(0, "")];
32. data.readSequenceableArray(b);
33. } catch (error) {
34. hilog.error(0x0000, 'testTag', 'error ' + error);
35. }
```

### writeRemoteObjectArray(deprecated)

PhonePC/2in1TabletTVWearable

writeRemoteObjectArray(objectArray: IRemoteObject[]): boolean

将IRemoteObject对象数组写入MessageParcel。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[writeRemoteObjectArray](js-apis-rpc.md#writeremoteobjectarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| objectArray | [IRemoteObject](js-apis-rpc.md#iremoteobject)[] | 是 | 要写入MessageParcel的IRemoteObject对象数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class TestRemoteObject extends rpc.RemoteObject {
5. constructor(descriptor: string) {
6. super(descriptor);
7. }
8. onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
9. option: rpc.MessageOption): boolean {
10. // 具体处理由业务决定
11. return true;
12. }
13. }

15. try {
16. let a = [new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"), new TestRemoteObject("testObject3")];
17. let data = rpc.MessageParcel.create();
18. let result = data.writeRemoteObjectArray(a);
19. hilog.info(0x0000, 'testTag', 'writeRemoteObjectArray is ' + result);
20. } catch (error) {
21. hilog.error(0x0000, 'testTag', 'error ' + error);
22. }
```

### readRemoteObjectArray(deprecated)

PhonePC/2in1TabletTVWearable

readRemoteObjectArray(objects: IRemoteObject[]): void

从MessageParcel读取IRemoteObject对象数组，并将其写入到创建的空数组中。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[readRemoteObjectArray](js-apis-rpc.md#readremoteobjectarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| objects | [IRemoteObject](js-apis-rpc.md#iremoteobject)[] | 是 | 从MessageParcel读取的IRemoteObject对象数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class TestRemoteObject extends rpc.RemoteObject {
5. constructor(descriptor: string) {
6. super(descriptor);
7. }
8. onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
9. option: rpc.MessageOption): boolean {
10. // 具体处理由业务决定
11. return true;
12. }
13. }

15. try {
16. let a = [new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"),
17. new TestRemoteObject("testObject3")];
18. let data = rpc.MessageParcel.create();
19. data.writeRemoteObjectArray(a);
20. let b: Array<rpc.IRemoteObject> = new Array(3);
21. data.readRemoteObjectArray(b);
22. hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + b);
23. } catch (error) {
24. hilog.error(0x0000, 'testTag', 'error ' + error);
25. }
```

### readRemoteObjectArray(deprecated)

PhonePC/2in1TabletTVWearable

readRemoteObjectArray(): IRemoteObject[]

从MessageParcel读取IRemoteObject对象数组。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[readRemoteObjectArray](js-apis-rpc.md#readremoteobjectarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IRemoteObject](js-apis-rpc.md#iremoteobject)[] | 返回IRemoteObject对象数组。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class TestRemoteObject extends rpc.RemoteObject {
5. constructor(descriptor: string) {
6. super(descriptor);
7. }
8. onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
9. option: rpc.MessageOption): boolean {
10. // 具体处理由业务决定
11. return true;
12. }
13. }

15. try {
16. let a = [new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"),
17. new TestRemoteObject("testObject3")];
18. let data = rpc.MessageParcel.create();
19. let result = data.writeRemoteObjectArray(a);
20. hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + result);
21. let b = data.readRemoteObjectArray();
22. hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + b);
23. } catch (error) {
24. hilog.error(0x0000, 'testTag', 'error ' + error);
25. }
```

### closeFileDescriptor(deprecated)

PhonePC/2in1TabletTVWearable

static closeFileDescriptor(fd: number): void

静态方法，关闭给定的文件描述符。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[closeFileDescriptor](js-apis-rpc.md#closefiledescriptor9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 要关闭的文件描述符。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. try {
6. let filePath = "path/to/file";
7. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
8. rpc.MessageParcel.closeFileDescriptor(file.fd);
9. } catch (error) {
10. hilog.error(0x0000, 'testTag', 'error ' + error);
11. }
```

### dupFileDescriptor(deprecated)

PhonePC/2in1TabletTVWearable

static dupFileDescriptor(fd: number) :number

静态方法，复制给定的文件描述符。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[dupFileDescriptor](js-apis-rpc.md#dupfiledescriptor9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 表示已存在的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回新的文件描述符。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. try {
6. let filePath = "path/to/file";
7. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
8. rpc.MessageParcel.dupFileDescriptor(file.fd);
9. } catch (error) {
10. hilog.error(0x0000, 'testTag', 'error ' + error);
11. }
```

### containFileDescriptors(deprecated)

PhonePC/2in1TabletTVWearable

containFileDescriptors(): boolean

检查此MessageParcel对象是否包含文件描述符。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[containFileDescriptors](js-apis-rpc.md#containfiledescriptors9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：包含文件描述符，false：未包含文件描述符。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. try {
6. let parcel = new rpc.MessageParcel();
7. let filePath = "path/to/file";
8. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
9. let writeResult = parcel.writeFileDescriptor(file.fd);
10. hilog.info(0x0000, 'testTag', 'parcel writeFd result is ' + writeResult);
11. let containFD = parcel.containFileDescriptors();
12. hilog.info(0x0000, 'testTag', 'parcel after write fd containFd result is ' + containFD);
13. } catch (error) {
14. hilog.error(0x0000, 'testTag', 'error ' + error);
15. }
```

### writeFileDescriptor(deprecated)

PhonePC/2in1TabletTVWearable

writeFileDescriptor(fd: number): boolean

写入文件描述符到MessageParcel。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[writeFileDescriptor](js-apis-rpc.md#writefiledescriptor9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：操作成功，false：操作失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. try {
6. let parcel = new rpc.MessageParcel();
7. let filePath = "path/to/file";
8. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
9. let writeResult = parcel.writeFileDescriptor(file.fd);
10. hilog.info(0x0000, 'testTag', 'parcel writeFd result is ' + writeResult);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
```

### readFileDescriptor(deprecated)

PhonePC/2in1TabletTVWearable

readFileDescriptor(): number

从MessageParcel中读取文件描述符。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[readFileDescriptor](js-apis-rpc.md#readfiledescriptor9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回文件描述符。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. try {
6. let parcel = new rpc.MessageParcel();
7. let filePath = "path/to/file";
8. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
9. parcel.writeFileDescriptor(file.fd);
10. let readFD = parcel.readFileDescriptor();
11. hilog.info(0x0000, 'testTag', 'parcel read fd is ' + readFD);
12. } catch (error) {
13. hilog.error(0x0000, 'testTag', 'error ' + error);
14. }
```

### writeAshmem(deprecated)

PhonePC/2in1TabletTVWearable

writeAshmem(ashmem: Ashmem): boolean

将指定的匿名共享对象写入此MessageParcel。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[writeAshmem](js-apis-rpc.md#writeashmem9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ashmem | [Ashmem](js-apis-rpc.md#ashmem8) | 是 | 要写入MessageParcel的匿名共享对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let parcel = new rpc.MessageParcel();
6. let ashmem = rpc.Ashmem.createAshmem("ashmem", 1024);
7. let isWriteSuccess = parcel.writeAshmem(ashmem);
8. hilog.info(0x0000, 'testTag', 'write ashmem to result is ' + isWriteSuccess);
9. } catch (error) {
10. hilog.error(0x0000, 'testTag', 'error ' + error);
11. }
```

### readAshmem(deprecated)

PhonePC/2in1TabletTVWearable

readAshmem(): Ashmem

从MessageParcel读取匿名共享对象。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[readAshmem](js-apis-rpc.md#readashmem9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Ashmem](js-apis-rpc.md#ashmem8) | 返回匿名共享对象。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let parcel = new rpc.MessageParcel();
6. let ashmem = rpc.Ashmem.createAshmem("ashmem", 1024);
7. let isWriteSuccess = parcel.writeAshmem(ashmem);
8. hilog.info(0x0000, 'testTag', 'write ashmem to result is ' + isWriteSuccess);
9. let readAshmem = parcel.readAshmem();
10. hilog.info(0x0000, 'testTag', 'read ashmem to result is ' + readAshmem);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
```

### getRawDataCapacity(deprecated)

PhonePC/2in1TabletTVWearable

getRawDataCapacity(): number

获取MessageParcel可以容纳的最大原始数据量。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[getRawDataCapacity](js-apis-rpc.md#getrawdatacapacity9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回MessageParcel可以容纳的最大原始数据量，即128MB。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let parcel = new rpc.MessageParcel();
6. let result = parcel.getRawDataCapacity();
7. hilog.info(0x0000, 'testTag', 'parcel get RawDataCapacity result is ' + result);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error ' + error);
10. }
```

### writeRawData(deprecated)

PhonePC/2in1TabletTVWearable

writeRawData(rawData: number[], size: number): boolean

将原始数据写入MessageParcel对象。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[writeRawDataBuffer](js-apis-rpc.md#writerawdatabuffer11)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rawData | number[] | 是 | 要写入的原始数据，大小不能超过128MB。 |
| size | number | 是 | 发送的原始数据大小，以字节为单位。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let parcel = new rpc.MessageParcel();
6. let arr = [1, 2, 3, 4, 5];
7. let isWriteSuccess = parcel.writeRawData(arr, arr.length);
8. hilog.info(0x0000, 'testTag', 'parcel write raw data result is ' + isWriteSuccess);
9. } catch (error) {
10. hilog.error(0x0000, 'testTag', 'error ' + error);
11. }
```

### readRawData(deprecated)

PhonePC/2in1TabletTVWearable

readRawData(size: number): number[]

从MessageParcel读取原始数据。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[readRawDataBuffer](js-apis-rpc.md#readrawdatabuffer11)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 要读取的原始数据的大小。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回原始数据（以字节为单位）。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let parcel = new rpc.MessageParcel();
6. let arr = [1, 2, 3, 4, 5];
7. let isWriteSuccess = parcel.writeRawData(arr, arr.length);
8. hilog.info(0x0000, 'testTag', 'parcel write raw data result is ' + isWriteSuccess);
9. let result = parcel.readRawData(5);
10. hilog.info(0x0000, 'testTag', 'parcel read raw data result is ' + result);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
```

## Parcelable9+

PhonePC/2in1TabletTVWearable

在进程间通信（IPC）期间，将类的对象写入MessageSequence并从MessageSequence中恢复它们。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

### marshalling9+

PhonePC/2in1TabletTVWearable

marshalling(dataOut: MessageSequence): boolean

将此可序列对象封送到MessageSequence中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataOut | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 可序列对象将被封送到的MessageSequence对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：封送成功，false：封送失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class MyParcelable implements rpc.Parcelable {
5. num: number = 0;
6. str: string = '';
7. constructor(num: number, str: string) {
8. this.num = num;
9. this.str = str;
10. }
11. marshalling(messageSequence: rpc.MessageSequence): boolean {
12. messageSequence.writeInt(this.num);
13. messageSequence.writeString(this.str);
14. return true;
15. }
16. unmarshalling(messageSequence: rpc.MessageSequence): boolean {
17. this.num = messageSequence.readInt();
18. this.str = messageSequence.readString();
19. hilog.info(0x0000, 'testTag', 'readInt is ' + this.num + ' readString is ' + this.str);
20. return true;
21. }
22. }

24. try {
25. let parcelable = new MyParcelable(1, "aaa");
26. let data = rpc.MessageSequence.create();
27. data.writeParcelable(parcelable);
28. let ret = new MyParcelable(0, "");
29. data.readParcelable(ret);
30. } catch (error) {
31. hilog.error(0x0000, 'testTag', 'error ' + error);
32. }
```

### unmarshalling9+

PhonePC/2in1TabletTVWearable

unmarshalling(dataIn: MessageSequence): boolean

从MessageSequence中解封此可序列对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 已将可序列对象封送到其中的MessageSequence对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：反序列化成功，false：反序列化失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class MyParcelable implements rpc.Parcelable {
5. num: number = 0;
6. str: string = '';
7. constructor(num: number, str: string) {
8. this.num = num;
9. this.str = str;
10. }
11. marshalling(messageSequence: rpc.MessageSequence): boolean {
12. messageSequence.writeInt(this.num);
13. messageSequence.writeString(this.str);
14. return true;
15. }
16. unmarshalling(messageSequence: rpc.MessageSequence): boolean {
17. this.num = messageSequence.readInt();
18. this.str = messageSequence.readString();
19. hilog.info(0x0000, 'testTag', 'readInt is ' + this.num + ' readString is ' + this.str);
20. return true;
21. }
22. }

24. try {
25. let parcelable = new MyParcelable(1, "aaa");
26. let data = rpc.MessageSequence.create();
27. data.writeParcelable(parcelable);
28. let ret = new MyParcelable(0, "");
29. data.readParcelable(ret);
30. } catch (error) {
31. hilog.error(0x0000, 'testTag', 'error ' + error);
32. }
```

## Sequenceable(deprecated)

PhonePC/2in1TabletTVWearable

在进程间通信（IPC）期间，将类的对象写入MessageParcel并从MessageParcel中恢复它们。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[Parcelable](js-apis-rpc.md#parcelable9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

### marshalling(deprecated)

PhonePC/2in1TabletTVWearable

marshalling(dataOut: MessageParcel): boolean

将此可序列对象封送到MessageParcel中。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[marshalling](js-apis-rpc.md#marshalling9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataOut | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 可序列对象将被封送到的MessageParcel对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：封送成功，false：封送失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class MySequenceable implements rpc.Sequenceable {
5. num: number = 0;
6. str: string = '';
7. constructor(num: number, str: string) {
8. this.num = num;
9. this.str = str;
10. }
11. marshalling(messageParcel: rpc.MessageParcel): boolean {
12. messageParcel.writeInt(this.num);
13. messageParcel.writeString(this.str);
14. return true;
15. }
16. unmarshalling(messageParcel: rpc.MessageParcel): boolean {
17. this.num = messageParcel.readInt();
18. this.str = messageParcel.readString();
19. return true;
20. }
21. }

23. try {
24. let sequenceable = new MySequenceable(1, "aaa");
25. let data = rpc.MessageParcel.create();
26. let result = data.writeSequenceable(sequenceable);
27. hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
28. let ret = new MySequenceable(0, "");
29. let result2 = data.readSequenceable(ret);
30. hilog.info(0x0000, 'testTag', 'readSequenceable is ' + result2);
31. } catch (error) {
32. hilog.error(0x0000, 'testTag', 'error ' + error);
33. }
```

### unmarshalling(deprecated)

PhonePC/2in1TabletTVWearable

unmarshalling(dataIn: MessageParcel): boolean

从MessageParcel中解封此可序列对象。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[unmarshalling](js-apis-rpc.md#unmarshalling9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataIn | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 已将可序列对象封送到其中的MessageParcel对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：反序列化成功，false：反序列化失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class MySequenceable implements rpc.Sequenceable {
5. num: number = 0;
6. str: string = '';
7. constructor(num: number, str: string) {
8. this.num = num;
9. this.str = str;
10. }
11. marshalling(messageParcel: rpc.MessageParcel): boolean {
12. messageParcel.writeInt(this.num);
13. messageParcel.writeString(this.str);
14. return true;
15. }
16. unmarshalling(messageParcel: rpc.MessageParcel): boolean {
17. this.num = messageParcel.readInt();
18. this.str = messageParcel.readString();
19. return true;
20. }
21. }

23. try {
24. let sequenceable = new MySequenceable(1, "aaa");
25. let data = rpc.MessageParcel.create();
26. let result = data.writeSequenceable(sequenceable);
27. hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
28. let ret = new MySequenceable(0, "");
29. let result2 = data.readSequenceable(ret);
30. hilog.info(0x0000, 'testTag', 'readSequenceable is ' + result2);
31. } catch (error) {
32. hilog.error(0x0000, 'testTag', 'error ' + error);
33. }
```

## IRemoteBroker

PhonePC/2in1TabletTVWearable

远端对象的代理持有者。用于获取代理对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

### asObject

PhonePC/2in1TabletTVWearable

asObject(): IRemoteObject

需派生类实现，获取代理或远端对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IRemoteObject](js-apis-rpc.md#iremoteobject) | 如果调用者是RemoteObject对象，则直接返回本身；如果调用者是[RemoteProxy](js-apis-rpc.md#remoteproxy)对象，则返回它的持有者[IRemoteObject](js-apis-rpc.md#iremoteobject)。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';

3. class TestAbility extends rpc.RemoteObject {
4. asObject() {
5. return this;
6. }
7. }
8. let remoteObject = new TestAbility("testObject").asObject();
```

**示例：**

说明

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // FA模型需要从@kit.AbilityKit导入featureAbility
2. // import { featureAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { Want, common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. let proxy: rpc.IRemoteObject | undefined;
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x0000, 'testTag', 'js onConnect called');
11. proxy = remoteProxy;
12. },
13. onDisconnect: (elementName) => {
14. hilog.info(0x0000, 'testTag', 'onDisconnect');
15. },
16. onFailed: () => {
17. hilog.info(0x0000, 'testTag', 'onFailed');
18. }
19. };
20. let want: Want  = {
21. // 获取服务端包名和ability名称
22. bundleName: "com.ohos.server",
23. abilityName: "com.ohos.server.EntryAbility",
24. };

26. // FA模型使用此方法连接服务
27. // FA.connectAbility(want,connect);

29. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
30. let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
31. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
32. let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的asObject接口方法获取代理或远端对象

```
1. import { rpc } from '@kit.IPCKit';

3. class TestProxy {
4. remote: rpc.IRemoteObject;
5. constructor(remote: rpc.IRemoteObject) {
6. this.remote = remote;
7. }
8. asObject() {
9. return this.remote;
10. }
11. }
12. if (proxy != undefined) {
13. let iRemoteObject = new TestProxy(proxy).asObject();
14. }
```

## DeathRecipient

PhonePC/2in1TabletTVWearable

用于订阅远端对象的死亡通知。当被订阅该通知的远端对象死亡时，本端可收到消息，调用[onRemoteDied](js-apis-rpc.md#onremotedied)接口。远端对象死亡可以为远端对象所在进程死亡，远端对象所在设备关机或重启，当远端对象与本端对象属于不同设备时，也可为远端对象离开组网时。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

### onRemoteDied

PhonePC/2in1TabletTVWearable

onRemoteDied(): void

在成功添加死亡通知订阅后，当远端对象死亡时，将自动调用本方法。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class MyDeathRecipient implements rpc.DeathRecipient {
5. onRemoteDied() {
6. hilog.info(0x0000, 'testTag', 'server died');
7. }
8. }
```

## RequestResult9+

PhonePC/2in1TabletTVWearable

发送请求的响应结果。

\*\*系统能力：\*\*以下各项对应的系统能力均为SystemCapability.Communication.IPC.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| errCode | number | 否 | 否 | 错误码。 |
| code | number | 否 | 否 | 消息代码。 |
| data | [MessageSequence](js-apis-rpc.md#messagesequence9) | 否 | 否 | 发送给对端进程的MessageSequence对象。 |
| reply | [MessageSequence](js-apis-rpc.md#messagesequence9) | 否 | 否 | 对端进程返回的MessageSequence对象。 |

## SendRequestResult(deprecated)

PhonePC/2in1TabletTVWearable

发送请求的响应结果。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[RequestResult](js-apis-rpc.md#requestresult9)替代。

\*\*系统能力：\*\*以下各项对应的系统能力均为SystemCapability.Communication.IPC.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| errCode | number | 否 | 否 | 错误码。 |
| code | number | 否 | 否 | 消息代码。 |
| data | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 否 | 否 | 发送给对端进程的MessageParcel对象。 |
| reply | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 否 | 否 | 对端进程返回的MessageParcel对象。 |

## CallingInfo23+

PhonePC/2in1TabletTVWearable

IPC上下文信息，包括PID和UID、本端和对端设备ID、检查接口调用是否在同一设备上。

\*\*系统能力：\*\*以下各项对应的系统能力均为SystemCapability.Communication.IPC.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| callerPid | number | 是 | 否 | 调用者的PID。 |
| callerUid | number | 是 | 否 | 调用者的UID。 |
| callerTokenId | number | 是 | 否 | 调用者的TokenId。 |
| remoteDeviceId | string | 是 | 否 | 对端设备的设备ID，仅RPC场景有效。 |
| localDeviceId | string | 是 | 否 | 本端设备的设备ID，仅RPC场景有效。 |
| isLocalCalling | boolean | 是 | 否 | 当前通信对端是否为本设备进程。true：调用在同一台设备，false：调用未在同一台设备。 |

## IRemoteObject

PhonePC/2in1TabletTVWearable

该接口可用于查询或获取接口描述符、添加或删除死亡通知、转储对象状态到特定文件、发送消息。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

### getLocalInterface9+

PhonePC/2in1TabletTVWearable

getLocalInterface(descriptor: string): IRemoteBroker

查询接口描述符的字符串。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | string | 是 | 接口描述符的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IRemoteBroker](js-apis-rpc.md#iremotebroker) | 返回绑定到指定接口描述符的IRemoteBroker对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.The string length is greater than or equal to 40960 bytes;  4.The number of bytes copied to the buffer is different from the length of the obtained string. |

### queryLocalInterface(deprecated)

PhonePC/2in1TabletTVWearable

queryLocalInterface(descriptor: string): IRemoteBroker

查询接口描述符的字符串。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[getLocalInterface](js-apis-rpc.md#getlocalinterface9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | string | 是 | 接口描述符的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IRemoteBroker](js-apis-rpc.md#iremotebroker) | 返回绑定到指定接口描述符的IRemoteBroker对象。 |

### sendRequest(deprecated)

PhonePC/2in1TabletTVWearable

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容。如果为选项设置了同步模式，则期约将在sendRequest返回时兑现，回复内容在reply报文里。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[sendMessageRequest](js-apis-rpc.md#sendmessagerequest9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 本次请求调用的消息码[1-16777215]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：发送成功，false：发送失败。 |

### sendMessageRequest9+

PhonePC/2in1TabletTVWearable

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): Promise<RequestResult>

以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendMessageRequest返回时兑现，回复内容在reply报文里。使用Promise异步回调。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 本次请求调用的消息码[1-16777215]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 保存待发送数据的MessageSequence对象。 |
| reply | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 接收应答数据的MessageSequence对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RequestResult](js-apis-rpc.md#requestresult9)> | Promise对象，返回一个期约，兑现值是requestResult实例。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.Failed to obtain the passed object instance. |

### sendRequest(deprecated)

PhonePC/2in1TabletTVWearable

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): Promise<SendRequestResult>

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendRequest返回时兑现，回复内容在reply报文里。使用Promise异步回调。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[sendMessageRequest](js-apis-rpc.md#sendmessagerequest9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 本次请求调用的消息码[1-16777215]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SendRequestResult](js-apis-rpc.md#sendrequestresultdeprecated)> | Promise对象，返回一个期约，兑现值是sendRequestResult实例。 |

### sendMessageRequest9+

PhonePC/2in1TabletTVWearable

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callback: AsyncCallback<RequestResult>): void

以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendRequest返回时收到回调，回复内容在reply报文里。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 本次请求调用的消息码[1-16777215]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 保存待发送数据的MessageSequence对象。 |
| reply | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 接收应答数据的MessageSequence对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |
| callback | AsyncCallback<[RequestResult](js-apis-rpc.md#requestresult9)> | 是 | 回调函数。当消息发送成功时，可从RequestResult中读取服务端返回的数据。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.Failed to obtain the passed object instance. |

### sendRequest(deprecated)

PhonePC/2in1TabletTVWearable

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption, callback: AsyncCallback<SendRequestResult>): void

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendRequest返回时收到回调，回复内容在reply报文里。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[sendMessageRequest](js-apis-rpc.md#sendmessagerequest9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 本次请求调用的消息码[1-16777215]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |
| callback | AsyncCallback<[SendRequestResult](js-apis-rpc.md#sendrequestresultdeprecated)> | 是 | 接收发送结果的回调。 |

### registerDeathRecipient9+

PhonePC/2in1TabletTVWearable

registerDeathRecipient(recipient: DeathRecipient, flags: number): void

注册用于接收远程对象死亡通知的回调。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recipient | [DeathRecipient](js-apis-rpc.md#deathrecipient) | 是 | 要注册的回调。 |
| flags | number | 是 | 死亡通知标志。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.The callback used to receive remote object death notifications is empty. |
| 1900005 | Operation allowed only for the proxy object. |
| 1900008 | The proxy or remote object is invalid. |

### addDeathRecipient(deprecated)

PhonePC/2in1TabletTVWearable

addDeathRecipient(recipient: DeathRecipient, flags: number): boolean

注册用于接收远程对象死亡通知的回调。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[registerDeathRecipient](js-apis-rpc.md#registerdeathrecipient9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recipient | [DeathRecipient](js-apis-rpc.md#deathrecipient) | 是 | 要注册的回调。 |
| flags | number | 是 | 死亡通知标志。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：回调注册成功，false：回调注册失败。 |

### unregisterDeathRecipient9+

PhonePC/2in1TabletTVWearable

unregisterDeathRecipient(recipient: DeathRecipient, flags: number): void

注销用于接收远程对象死亡通知的回调。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recipient | [DeathRecipient](js-apis-rpc.md#deathrecipient) | 是 | 要注销的回调。 |
| flags | number | 是 | 死亡通知标志。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.The callback used to receive remote object death notifications is empty. |
| 1900005 | Operation allowed only for the proxy object. |
| 1900008 | The proxy or remote object is invalid. |

### removeDeathRecipient(deprecated)

PhonePC/2in1TabletTVWearable

removeDeathRecipient(recipient: DeathRecipient, flags: number): boolean

注销用于接收远程对象死亡通知的回调。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[unregisterDeathRecipient](js-apis-rpc.md#unregisterdeathrecipient9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recipient | [DeathRecipient](js-apis-rpc.md#deathrecipient) | 是 | 要注销的回调。 |
| flags | number | 是 | 死亡通知标志。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：回调注销成功，false：回调注销失败。 |

### getDescriptor9+

PhonePC/2in1TabletTVWearable

getDescriptor(): string

获取对象的接口描述符，接口描述符为字符串。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回接口描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900008 | The proxy or remote object is invalid. |

### getInterfaceDescriptor(deprecated)

PhonePC/2in1TabletTVWearable

getInterfaceDescriptor(): string

获取对象的接口描述符，接口描述符为字符串。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[getDescriptor](js-apis-rpc.md#getdescriptor9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回接口描述符。 |

### isObjectDead

PhonePC/2in1TabletTVWearable

isObjectDead(): boolean

检查当前对象是否死亡。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：对象死亡，false：对象未死亡。 |

## RemoteProxy

PhonePC/2in1TabletTVWearable

实现IRemoteObject代理对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

### 属性

PhonePC/2in1TabletTVWearable

\*\*系统能力：\*\*以下各项对应的系统能力均为SystemCapability.Communication.IPC.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| PING\_TRANSACTION | number | 是 | 否 | 内部指令码，用于测试IPC服务是否正常。 |
| DUMP\_TRANSACTION | number | 是 | 否 | 内部指令码，获取IPC服务相关的状态信息。 |
| INTERFACE\_TRANSACTION | number | 是 | 否 | 内部指令码，获取对端接口描述符。 |
| MIN\_TRANSACTION\_ID | number | 是 | 否 | 最小有效指令码。 |
| MAX\_TRANSACTION\_ID | number | 是 | 否 | 最大有效指令码。 |

### sendRequest(deprecated)

PhonePC/2in1TabletTVWearable

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendRequest返回时兑现，回复内容在reply报文里。

说明

从API version 7 开始支持，API version 8 开始废弃，建议使用[sendMessageRequest](js-apis-rpc.md#sendmessagerequest9-2)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 本次请求调用的消息码[1-16777215]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：发送成功，false：发送失败。 |

**示例：**

说明

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // FA模型需要从@kit.AbilityKit导入featureAbility
2. // import { featureAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { Want, common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. let proxy: rpc.IRemoteObject | undefined;
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x0000, 'testTag', 'js onConnect called');
11. proxy = remoteProxy;
12. },
13. onDisconnect: (elementName) => {
14. hilog.info(0x0000, 'testTag', 'onDisconnect');
15. },
16. onFailed: () => {
17. hilog.info(0x0000, 'testTag', 'onFailed');
18. }
19. };
20. let want: Want = {
21. // 获取服务端包名和ability名称
22. bundleName: "com.ohos.server",
23. abilityName: "com.ohos.server.EntryAbility",
24. };

26. // FA模型使用此方法连接服务
27. // FA.connectAbility(want,connect);

29. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
30. let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
31. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
32. let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的sendRequest接口方法发送消息

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let option = new rpc.MessageOption();
6. let data = rpc.MessageParcel.create();
7. let reply = rpc.MessageParcel.create();
8. data.writeInt(1);
9. data.writeString("hello");
10. if (proxy != undefined) {
11. let ret: boolean = proxy.sendRequest(1, data, reply, option);
12. if (ret) {
13. hilog.info(0x0000, 'testTag', 'sendRequest got result');
14. let msg = reply.readString();
15. hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
16. } else {
17. hilog.error(0x0000, 'testTag', 'sendRequest failed');
18. }
19. hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
20. data.reclaim();
21. reply.reclaim();
22. }
23. } catch (error) {
24. hilog.error(0x0000, 'testTag', 'error: ' + error);
25. }
```

### sendMessageRequest9+

PhonePC/2in1TabletTVWearable

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): Promise<RequestResult>

以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendMessageRequest返回时兑现，回复内容在reply报文里。使用Promise异步回调。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 本次请求调用的消息码[1-16777215]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 保存待发送数据的MessageSequence对象。 |
| reply | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 接收应答数据的MessageSequence对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RequestResult](js-apis-rpc.md#requestresult9)> | Promise对象，返回一个期约，兑现值是requestResult实例。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.Failed to obtain the passed object instance. |

**示例：**

说明

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // FA模型需要从@kit.AbilityKit导入featureAbility
2. // import { featureAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { Want, common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. let proxy: rpc.IRemoteObject | undefined;
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x0000, 'testTag', 'js onConnect called');
11. proxy = remoteProxy;
12. },
13. onDisconnect: (elementName) => {
14. hilog.info(0x0000, 'testTag', 'onDisconnect');
15. },
16. onFailed: () => {
17. hilog.info(0x0000, 'testTag', 'onFailed');
18. }
19. };
20. let want: Want = {
21. // 获取服务端包名和ability名称
22. bundleName: "com.ohos.server",
23. abilityName: "com.ohos.server.EntryAbility",
24. };

26. // FA模型使用此方法连接服务
27. // FA.connectAbility(want,connect);

29. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
30. let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
31. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
32. let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的sendMessageRequest接口方法发送消息

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let option = new rpc.MessageOption();
6. let data = rpc.MessageSequence.create();
7. let reply = rpc.MessageSequence.create();
8. data.writeInt(1);
9. data.writeString("hello");
10. if (proxy != undefined) {
11. proxy.sendMessageRequest(1, data, reply, option)
12. .then((result: rpc.RequestResult) => {
13. if (result.errCode === 0) {
14. hilog.info(0x0000, 'testTag', 'sendMessageRequest got result');
15. let num = result.reply.readInt();
16. let msg = result.reply.readString();
17. hilog.info(0x0000, 'testTag', 'reply num: ' + num);
18. hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
19. } else {
20. hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode: ' + result.errCode);
21. }
22. }).catch((e: Error) => {
23. hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error: ' + JSON.stringify(e));
24. }).finally (() => {
25. hilog.info(0x0000, 'testTag', 'sendMessageRequest ends, reclaim parcel');
26. data.reclaim();
27. reply.reclaim();
28. });
29. }
30. } catch (error) {
31. hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error: ' + error);
32. }
```

### sendRequest(deprecated)

PhonePC/2in1TabletTVWearable

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): Promise<SendRequestResult>

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendRequest返回时兑现，回复内容在reply报文里。使用Promise异步回调。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[sendMessageRequest](js-apis-rpc.md#sendmessagerequest9-2)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 本次请求调用的消息码[1-16777215]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SendRequestResult](js-apis-rpc.md#sendrequestresultdeprecated)> | Promise对象，返回一个期约，兑现值是sendRequestResult实例。 |

**示例：**

说明

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // FA模型需要从@kit.AbilityKit导入featureAbility
2. // import { featureAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { Want, common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. let proxy: rpc.IRemoteObject | undefined;
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x0000, 'testTag', 'js onConnect called');
11. proxy = remoteProxy;
12. },
13. onDisconnect: (elementName) => {
14. hilog.info(0x0000, 'testTag', 'onDisconnect');
15. },
16. onFailed: () => {
17. hilog.info(0x0000, 'testTag', 'onFailed');
18. }
19. };
20. let want: Want = {
21. // 获取服务端包名和ability名称
22. bundleName: "com.ohos.server",
23. abilityName: "com.ohos.server.EntryAbility",
24. };

26. // FA模型使用此方法连接服务
27. // FA.connectAbility(want,connect);

29. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
30. let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
31. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
32. let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的sendRequest接口方法发送消息

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let option = new rpc.MessageOption();
6. let data = rpc.MessageParcel.create();
7. let reply = rpc.MessageParcel.create();
8. data.writeInt(1);
9. data.writeString("hello");
10. if (proxy != undefined) {
11. let a = proxy.sendRequest(1, data, reply, option) as Object;
12. let b = a as Promise<rpc.SendRequestResult>;
13. b.then((result: rpc.SendRequestResult) => {
14. if (result.errCode === 0) {
15. hilog.info(0x0000, 'testTag', 'sendRequest got result');
16. let num = result.reply.readInt();
17. let msg = result.reply.readString();
18. hilog.info(0x0000, 'testTag', 'reply num: ' + num);
19. hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
20. } else {
21. hilog.error(0x0000, 'testTag', 'sendRequest failed, errCode: ' + result.errCode);
22. }
23. }).catch((e: Error) => {
24. hilog.error(0x0000, 'testTag', 'sendRequest failed, error: ' + JSON.stringify(e));
25. }).finally (() => {
26. hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
27. data.reclaim();
28. reply.reclaim();
29. });
30. }
31. } catch (error) {
32. hilog.error(0x0000, 'testTag', 'sendRequest failed, error: ' + error);
33. }
```

### sendMessageRequest9+

PhonePC/2in1TabletTVWearable

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callback: AsyncCallback<RequestResult>): void

以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendMessageRequest返回后的某个时机执行回调，回复内容在RequestResult的reply报文里。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 本次请求调用的消息码[1-16777215]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 保存待发送数据的MessageSequence对象。 |
| reply | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 接收应答数据的MessageSequence对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |
| callback | AsyncCallback<[RequestResult](js-apis-rpc.md#requestresult9)> | 是 | 回调函数。当消息发送成功时，可从RequestResult中读取服务端返回的数据。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.Failed to obtain the passed object instance. |

### sendRequest(deprecated)

PhonePC/2in1TabletTVWearable

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption, callback: AsyncCallback<SendRequestResult>): void

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendRequest返回时收到回调，回复内容在reply报文里。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[sendMessageRequest](js-apis-rpc.md#sendmessagerequest9-3)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 本次请求调用的消息码[1-16777215]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |
| callback | AsyncCallback<[SendRequestResult](js-apis-rpc.md#sendrequestresultdeprecated)> | 是 | 接收发送结果的回调。 |

### getLocalInterface9+

PhonePC/2in1TabletTVWearable

getLocalInterface(interfaceDes: string): IRemoteBroker

查询并获取当前接口描述符对应的本地接口对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| interfaceDes | string | 是 | 需要查询的接口描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IRemoteBroker](js-apis-rpc.md#iremotebroker) | 默认返回Null，标识该接口是一个代理侧接口。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | check param failed |
| 1900006 | Operation allowed only for the remote object. |

**示例：**

说明

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // FA模型需要从@kit.AbilityKit导入featureAbility
2. // import { featureAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { Want, common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. let proxy: rpc.IRemoteObject | undefined;
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x0000, 'testTag', 'js onConnect called');
11. proxy = remoteProxy;
12. },
13. onDisconnect: (elementName) => {
14. hilog.info(0x0000, 'testTag', 'onDisconnect');
15. },
16. onFailed: () => {
17. hilog.info(0x0000, 'testTag', 'onFailed');
18. }
19. };
20. let want: Want = {
21. // 获取服务端包名和ability名称
22. bundleName: "com.ohos.server",
23. abilityName: "com.ohos.server.EntryAbility",
24. };

26. // FA模型使用此方法连接服务
27. // FA.connectAbility(want,connect);

29. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
30. let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
31. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
32. let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的getLocalInterface接口方法查询接口对象

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. if (proxy != undefined) {
6. try {
7. let broker: rpc.IRemoteBroker = proxy.getLocalInterface("testObject");
8. hilog.info(0x0000, 'testTag', 'getLocalInterface is ' + broker);
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. hilog.error(0x0000, 'testTag', 'rpc get local interface fail, errorCode ' + e.code);
12. hilog.error(0x0000, 'testTag', 'rpc get local interface fail, errorMessage ' + e.message);
13. }
14. }
```

### queryLocalInterface(deprecated)

PhonePC/2in1TabletTVWearable

queryLocalInterface(interface: string): IRemoteBroker

查询并获取当前接口描述符对应的本地接口对象。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[getLocalInterface](js-apis-rpc.md#getlocalinterface9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| interface | string | 是 | 需要查询的接口描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IRemoteBroker](js-apis-rpc.md#iremotebroker) | 默认返回Null，标识该接口是一个代理侧接口。 |

**示例：**

说明

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // FA模型需要从@kit.AbilityKit导入featureAbility
2. // import { featureAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { Want, common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. let proxy: rpc.IRemoteObject | undefined;
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x0000, 'testTag', 'js onConnect called');
11. proxy = remoteProxy;
12. },
13. onDisconnect: (elementName) => {
14. hilog.info(0x0000, 'testTag', 'onDisconnect');
15. },
16. onFailed: () => {
17. hilog.info(0x0000, 'testTag', 'onFailed');
18. }
19. };
20. let want: Want = {
21. // 获取服务端包名和ability名称
22. bundleName: "com.ohos.server",
23. abilityName: "com.ohos.server.EntryAbility",
24. };

26. // FA模型使用此方法连接服务
27. // FA.connectAbility(want,connect);

29. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
30. let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
31. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
32. let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的queryLocalInterface接口获取接口对象

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. if (proxy != undefined) {
5. let broker: rpc.IRemoteBroker = proxy.queryLocalInterface("testObject");
6. hilog.info(0x0000, 'testTag', 'queryLocalInterface is ' + broker);
7. }
```

### registerDeathRecipient9+

PhonePC/2in1TabletTVWearable

registerDeathRecipient(recipient: DeathRecipient, flags: number): void

注册用于接收远程对象死亡通知的回调。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recipient | [DeathRecipient](js-apis-rpc.md#deathrecipient) | 是 | 要注册的回调。 |
| flags | number | 是 | 死亡通知标志。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.The callback used to receive remote object death notifications is empty. |
| 1900008 | The proxy or remote object is invalid. |

**示例：**

说明

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // FA模型需要从@kit.AbilityKit导入featureAbility
2. // import { featureAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { Want, common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. let proxy: rpc.IRemoteObject | undefined;
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x0000, 'testTag', 'js onConnect called');
11. proxy = remoteProxy;
12. },
13. onDisconnect: (elementName) => {
14. hilog.info(0x0000, 'testTag', 'onDisconnect');
15. },
16. onFailed: () => {
17. hilog.info(0x0000, 'testTag', 'onFailed');
18. }
19. };
20. let want: Want = {
21. // 获取服务端包名和ability名称
22. bundleName: "com.ohos.server",
23. abilityName: "com.ohos.server.EntryAbility",
24. };

26. // FA模型使用此方法连接服务
27. // FA.connectAbility(want,connect);

29. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
30. let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
31. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
32. let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的registerDeathRecipient接口注册死亡回调

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class MyDeathRecipient implements rpc.DeathRecipient {
6. onRemoteDied() {
7. hilog.info(0x0000, 'testTag', 'server died');
8. }
9. }
10. if (proxy != undefined) {
11. try {
12. let deathRecipient = new MyDeathRecipient();
13. proxy.registerDeathRecipient(deathRecipient, 0);
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. hilog.error(0x0000, 'testTag', 'proxy register deathRecipient fail, errorCode ' + e.code);
17. hilog.error(0x0000, 'testTag', 'proxy register deathRecipient fail, errorMessage ' + e.message);
18. }
19. }
```

### addDeathRecipient(deprecated)

PhonePC/2in1TabletTVWearable

addDeathRecipient(recipient: DeathRecipient, flags: number): boolean

注册用于接收远程对象死亡通知的回调。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[registerDeathRecipient](js-apis-rpc.md#registerdeathrecipient9-1)类替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recipient | [DeathRecipient](js-apis-rpc.md#deathrecipient) | 是 | 收件人表示要注册的回调。 |
| flags | number | 是 | 死亡通知标志。保留参数。设置为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：回调注册成功，false：回调注册失败。 |

**示例：**

说明

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // FA模型需要从@kit.AbilityKit导入featureAbility
2. // import { featureAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { Want, common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. let proxy: rpc.IRemoteObject | undefined;
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x0000, 'testTag', 'js onConnect called');
11. proxy = remoteProxy;
12. },
13. onDisconnect: (elementName) => {
14. hilog.info(0x0000, 'testTag', 'onDisconnect');
15. },
16. onFailed: () => {
17. hilog.info(0x0000, 'testTag', 'onFailed');
18. }
19. };
20. let want: Want = {
21. // 获取服务端包名和ability名称
22. bundleName: "com.ohos.server",
23. abilityName: "com.ohos.server.EntryAbility",
24. };

26. // FA模型使用此方法连接服务
27. // FA.connectAbility(want,connect);

29. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
30. let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
31. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
32. let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的addDeathRecipient接口方法新增死亡回调

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class MyDeathRecipient implements rpc.DeathRecipient {
5. onRemoteDied() {
6. hilog.info(0x0000, 'testTag', 'server died');
7. }
8. }
9. if (proxy != undefined) {
10. let deathRecipient = new MyDeathRecipient();
11. proxy.addDeathRecipient(deathRecipient, 0);
12. }
```

### unregisterDeathRecipient9+

PhonePC/2in1TabletTVWearable

unregisterDeathRecipient(recipient: DeathRecipient, flags: number): void

注销用于接收远程对象死亡通知的回调。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recipient | [DeathRecipient](js-apis-rpc.md#deathrecipient) | 是 | 要注销的回调。 |
| flags | number | 是 | 死亡通知标志。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.The callback used to receive remote object death notifications is empty. |
| 1900008 | The proxy or remote object is invalid. |

**示例：**

说明

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // FA模型需要从@kit.AbilityKit导入featureAbility
2. // import { featureAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { Want, common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. let proxy: rpc.IRemoteObject | undefined;
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x0000, 'testTag', 'js onConnect called');
11. proxy = remoteProxy;
12. },
13. onDisconnect: (elementName) => {
14. hilog.info(0x0000, 'testTag', 'onDisconnect');
15. },
16. onFailed: () => {
17. hilog.info(0x0000, 'testTag', 'onFailed');
18. }
19. };
20. let want: Want = {
21. // 获取服务端包名和ability名称
22. bundleName: "com.ohos.server",
23. abilityName: "com.ohos.server.EntryAbility",
24. };

26. // FA模型使用此方法连接服务
27. // FA.connectAbility(want,connect);

29. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
30. let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
31. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
32. let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的unregisterDeathRecipient接口方法注销死亡回调

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class MyDeathRecipient implements rpc.DeathRecipient {
6. onRemoteDied() {
7. hilog.info(0x0000, 'testTag', 'server died');
8. }
9. }
10. if (proxy != undefined) {
11. try {
12. let deathRecipient = new MyDeathRecipient();
13. proxy.registerDeathRecipient(deathRecipient, 0);
14. proxy.unregisterDeathRecipient(deathRecipient, 0);
15. } catch (error) {
16. let e: BusinessError = error as BusinessError;
17. hilog.error(0x0000, 'testTag', 'proxy unregister deathRecipient fail, errorCode ' + e.code);
18. hilog.error(0x0000, 'testTag', 'proxy unregister deathRecipient fail, errorMessage ' + e.message);
19. }
20. }
```

### removeDeathRecipient(deprecated)

PhonePC/2in1TabletTVWearable

removeDeathRecipient(recipient: DeathRecipient, flags: number): boolean

注销用于接收远程对象死亡通知的回调。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[unregisterDeathRecipient](js-apis-rpc.md#unregisterdeathrecipient9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recipient | [DeathRecipient](js-apis-rpc.md#deathrecipient) | 是 | 要注销的死亡回调。 |
| flags | number | 是 | 死亡通知标志。保留参数。设置为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：回调注销成功，false：回调注销失败。 |

**示例：**

说明

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // FA模型需要从@kit.AbilityKit导入featureAbility
2. // import { featureAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { Want, common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. let proxy: rpc.IRemoteObject | undefined;
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x0000, 'testTag', 'js onConnect called');
11. proxy = remoteProxy;
12. },
13. onDisconnect: (elementName) => {
14. hilog.info(0x0000, 'testTag', 'onDisconnect');
15. },
16. onFailed: () => {
17. hilog.info(0x0000, 'testTag', 'onFailed');
18. }
19. };
20. let want: Want = {
21. // 获取服务端包名和ability名称
22. bundleName: "com.ohos.server",
23. abilityName: "com.ohos.server.EntryAbility",
24. };

26. // FA模型使用此方法连接服务
27. // FA.connectAbility(want,connect);

29. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
30. let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
31. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
32. let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的removeDeathRecipient接口方法去注册死亡回调

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class MyDeathRecipient implements rpc.DeathRecipient {
5. onRemoteDied() {
6. hilog.info(0x0000, 'testTag', 'server died');
7. }
8. }
9. if (proxy != undefined) {
10. let deathRecipient = new MyDeathRecipient();
11. proxy.addDeathRecipient(deathRecipient, 0);
12. proxy.removeDeathRecipient(deathRecipient, 0);
13. }
```

### getDescriptor9+

PhonePC/2in1TabletTVWearable

getDescriptor(): string

获取对象的接口描述符，接口描述符为字符串。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回接口描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900007 | communication failed. |
| 1900008 | The proxy or remote object is invalid. |

**示例：**

说明

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // FA模型需要从@kit.AbilityKit导入featureAbility
2. // import { featureAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { Want, common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. let proxy: rpc.IRemoteObject | undefined;
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x0000, 'testTag', 'js onConnect called');
11. proxy = remoteProxy;
12. },
13. onDisconnect: (elementName) => {
14. hilog.info(0x0000, 'testTag', 'onDisconnect');
15. },
16. onFailed: () => {
17. hilog.info(0x0000, 'testTag', 'onFailed');
18. }
19. };
20. let want: Want = {
21. // 获取服务端包名和ability名称
22. bundleName: "com.ohos.server",
23. abilityName: "com.ohos.server.EntryAbility",
24. };

26. // FA模型使用此方法连接服务
27. // FA.connectAbility(want,connect);

29. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
30. let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
31. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
32. let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的getDescriptor接口方法获取对象的接口描述符

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. if (proxy != undefined) {
6. try {
7. let descriptor: string = proxy.getDescriptor();
8. hilog.info(0x0000, 'testTag', 'descriptor is ' + descriptor);
9. } catch (error) {
10. let e: BusinessError = error as BusinessError;
11. hilog.error(0x0000, 'testTag', 'rpc get interface descriptor fail, errorCode ' + e.code);
12. hilog.error(0x0000, 'testTag', 'rpc get interface descriptor fail, errorMessage ' + e.message);
13. }
14. }
```

### getInterfaceDescriptor(deprecated)

PhonePC/2in1TabletTVWearable

getInterfaceDescriptor(): string

查询当前代理对象接口的描述符。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[getDescriptor](js-apis-rpc.md#getdescriptor9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前的接口描述符。 |

**示例：**

说明

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // FA模型需要从@kit.AbilityKit导入featureAbility
2. // import { featureAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { Want, common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. let proxy: rpc.IRemoteObject | undefined;
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x0000, 'testTag', 'js onConnect called');
11. proxy = remoteProxy;
12. },
13. onDisconnect: (elementName) => {
14. hilog.info(0x0000, 'testTag', 'onDisconnect');
15. },
16. onFailed: () => {
17. hilog.info(0x0000, 'testTag', 'onFailed');
18. }
19. };
20. let want: Want = {
21. // 获取服务端包名和ability名称
22. bundleName: "com.ohos.server",
23. abilityName: "com.ohos.server.EntryAbility",
24. };

26. // FA模型使用此方法连接服务
27. // FA.connectAbility(want,connect);

29. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
30. let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
31. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
32. let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的getInterfaceDescriptor接口方法查询当前代理对象接口的描述符

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. if (proxy != undefined) {
5. let descriptor: string = proxy.getInterfaceDescriptor();
6. hilog.info(0x0000, 'testTag', 'descriptor is ' + descriptor);
7. }
```

### isObjectDead

PhonePC/2in1TabletTVWearable

isObjectDead(): boolean

指示对应的RemoteObject是否死亡。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：对应的对象已经死亡，false：对应的对象未死亡。 |

**示例：**

说明

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // FA模型需要从@kit.AbilityKit导入featureAbility
2. // import { featureAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { Want, common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. let proxy: rpc.IRemoteObject | undefined;
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x0000, 'testTag', 'js onConnect called');
11. proxy = remoteProxy;
12. },
13. onDisconnect: (elementName) => {
14. hilog.info(0x0000, 'testTag', 'onDisconnect');
15. },
16. onFailed: () => {
17. hilog.info(0x0000, 'testTag', 'onFailed');
18. }
19. };
20. let want: Want = {
21. // 获取服务端包名和ability名称
22. bundleName: "com.ohos.server",
23. abilityName: "com.ohos.server.EntryAbility",
24. };

26. // FA模型使用此方法连接服务
27. // FA.connectAbility(want,connect);

29. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
30. let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
31. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
32. let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的isObjectDead接口方法判断当前对象是否已经死亡

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. if (proxy != undefined) {
5. let isDead: boolean = proxy.isObjectDead();
6. hilog.info(0x0000, 'testTag', 'isObjectDead is ' + isDead);
7. }
```

## MessageOption

PhonePC/2in1TabletTVWearable

公共消息选项，使用指定的标志类型，构造指定的MessageOption对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

### 属性

PhonePC/2in1TabletTVWearable

\*\*系统能力：\*\*以下各项对应的系统能力均为SystemCapability.Communication.IPC.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| TF\_SYNC | number | 是 | 否 | 同步调用标识。 |
| TF\_ASYNC | number | 是 | 否 | 异步调用标识。 |
| TF\_ACCEPT\_FDS | number | 是 | 否 | 指示sendMessageRequest9+接口可以传递文件描述符。 |
| TF\_WAIT\_TIME | number | 是 | 否 | RPC等待时间(单位/秒)，IPC场景下无效。默认等待为8秒（不建议修改等待时间）。 |

### constructor9+

PhonePC/2in1TabletTVWearable

constructor(async?: boolean)

MessageOption构造函数。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| async | boolean | 否 | true：表示异步调用标志，false：表示同步调用标志。默认同步调用。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';

3. class TestRemoteObject extends rpc.MessageOption {
4. constructor(async: boolean) {
5. super(async);
6. }
7. }
```

### constructor

PhonePC/2in1TabletTVWearable

constructor(syncFlags?: number, waitTime?: number)

MessageOption构造函数。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| syncFlags | number | 否 | 同步调用或异步调用标志，同步调用标志：0；异步调用标志：1。默认同步调用。 |
| waitTime | number | 否 | 调用rpc最长等待时间。默认TF\_WAIT\_TIME。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';

3. class TestRemoteObject extends rpc.MessageOption {
4. constructor(syncFlags?: number,waitTime?: number) {
5. super(syncFlags,waitTime);
6. }
7. }
```

### isAsync9+

PhonePC/2in1TabletTVWearable

isAsync(): boolean

获取[sendMessageRequest](js-apis-rpc.md#sendmessagerequest9-2)调用中确定同步或是异步的标志。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：异步调用成功，false：同步调用成功。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let option = new rpc.MessageOption();
6. let result = option.isAsync();
7. } catch (error) {
8. hilog.info(0x0000, 'testTag', 'error ' + error);
9. }
```

### setAsync9+

PhonePC/2in1TabletTVWearable

setAsync(isAsync: boolean): void

设置[sendMessageRequest](js-apis-rpc.md#sendmessagerequest9-2)调用中确定同步或是异步的标志。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isAsync | boolean | 是 | true：表示异步调用标志，false：表示同步调用标志。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let option = new rpc.MessageOption();
6. option.setAsync(true);
7. } catch (error) {
8. hilog.info(0x0000, 'testTag', 'error ' + error);
9. }
```

### getFlags

PhonePC/2in1TabletTVWearable

getFlags(): number

获取同步调用或异步调用标志。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 调用成功返回同步调用或异步调用标志。同步调用标志：0，异步调用标志：1。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let option = new rpc.MessageOption();
6. hilog.info(0x0000, 'testTag', 'create object successfully');
7. let flag = option.getFlags();
8. hilog.info(0x0000, 'testTag', 'run getFlags success, flag is ' + flag);
9. option.setFlags(rpc.MessageOption.TF_ASYNC);
10. hilog.info(0x0000, 'testTag', 'run setFlags success');
11. let flag2 = option.getFlags();
12. hilog.info(0x0000, 'testTag', 'run getFlags success, flag2 is ' + flag2);
13. } catch (error) {
14. hilog.error(0x0000, 'testTag', 'error ' + error);
15. }
```

### setFlags

PhonePC/2in1TabletTVWearable

setFlags(flags: number): void

设置同步调用或异步调用标志。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flags | number | 是 | 同步调用或异步调用标志。同步调用标志：0；异步调用标志：1 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let option = new rpc.MessageOption();
6. option.setFlags(rpc.MessageOption.TF_ASYNC);
7. hilog.info(0x0000, 'testTag', 'run setFlags success');
8. let flag = option.getFlags();
9. hilog.info(0x0000, 'testTag', 'run getFlags success, flag is ' + flag);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
```

### getWaitTime

PhonePC/2in1TabletTVWearable

getWaitTime(): number

获取rpc调用的最长等待时间。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | rpc最长等待时间。默认TF\_WAIT\_TIME。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let option = new rpc.MessageOption();
6. let time = option.getWaitTime();
7. hilog.info(0x0000, 'testTag', 'run getWaitTime success, time is ' + time);
8. option.setWaitTime(16);
9. let time2 = option.getWaitTime();
10. hilog.info(0x0000, 'testTag', 'run getWaitTime success, time is ' + time2);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
```

### setWaitTime

PhonePC/2in1TabletTVWearable

setWaitTime(waitTime: number): void

设置rpc调用最长等待时间。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| waitTime | number | 是 | rpc调用最长等待时间，上限为3000秒。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let option = new rpc.MessageOption();
6. option.setWaitTime(16);
7. let time = option.getWaitTime();
8. hilog.info(0x0000, 'testTag', 'run getWaitTime success, time is ' + time);
9. } catch (error) {
10. hilog.error(0x0000, 'testTag', 'error ' + error);
11. }
```

## IPCSkeleton

PhonePC/2in1TabletTVWearable

用于获取IPC上下文信息，包括获取UID和PID、获取本端和对端设备ID、检查接口调用是否在同一设备上。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

### getContextObject

PhonePC/2in1TabletTVWearable

static getContextObject(): IRemoteObject

静态方法，获取系统能力的管理者。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IRemoteObject](js-apis-rpc.md#iremoteobject) | 返回系统能力管理者。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let samgr = rpc.IPCSkeleton.getContextObject();
6. hilog.info(0x0000, 'testTag', 'RpcServer: getContextObject result: ' + samgr);
7. } catch (error) {
8. hilog.error(0x0000, 'testTag', 'error ' + error);
9. }
```

### getCallingPid

PhonePC/2in1TabletTVWearable

static getCallingPid(): number

静态方法，获取调用者的PID。此方法由[RemoteObject](js-apis-rpc.md#remoteobject)对象在IPC上下文环境（[onRemoteMessageRequest](js-apis-rpc.md#onremotemessagerequest9)）中调用，不在则返回本进程的PID。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回调用者的PID。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class Stub extends rpc.RemoteObject {
5. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
6. option: rpc.MessageOption): boolean | Promise<boolean> {
7. try {
8. let callerPid = rpc.IPCSkeleton.getCallingPid();
9. hilog.info(0x0000, 'testTag', 'RpcServer: getCallingPid result: ' + callerPid);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
13. return true;
14. }
15. }
```

### getCallingUid

PhonePC/2in1TabletTVWearable

static getCallingUid(): number

静态方法，获取调用者的UID。此方法由[RemoteObject](js-apis-rpc.md#remoteobject)对象在IPC上下文环境（[onRemoteMessageRequest](js-apis-rpc.md#onremotemessagerequest9)）中调用，不在则返回本进程的UID。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回调用者的UID。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class Stub extends rpc.RemoteObject {
5. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
6. option: rpc.MessageOption): boolean | Promise<boolean> {
7. try {
8. let callerUid = rpc.IPCSkeleton.getCallingUid();
9. hilog.info(0x0000, 'testTag', 'RpcServer: getCallingUid result: ' + callerUid);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
13. return true;
14. }
15. }
```

### getCallingTokenId8+

PhonePC/2in1TabletTVWearable

static getCallingTokenId(): number

静态方法，获取调用者的TokenId，用于被调用方对调用方的身份校验。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回调用者的TokenId。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class Stub extends rpc.RemoteObject {
5. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
6. option: rpc.MessageOption): boolean | Promise<boolean> {
7. try {
8. let callerTokenId = rpc.IPCSkeleton.getCallingTokenId();
9. hilog.info(0x0000, 'testTag', 'RpcServer: getCallingTokenId result: ' + callerTokenId);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
13. return true;
14. }
15. }
```

### getCallingDeviceID

PhonePC/2in1TabletTVWearable

static getCallingDeviceID(): string

静态方法，获取调用者进程所在的设备ID。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回调用者进程所在的设备ID。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class Stub extends rpc.RemoteObject {
5. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
6. option: rpc.MessageOption): boolean | Promise<boolean> {
7. try {
8. let callerDeviceID = rpc.IPCSkeleton.getCallingDeviceID();
9. hilog.info(0x0000, 'testTag', 'RpcServer: callerDeviceID is ' + callerDeviceID);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
13. return true;
14. }
15. }
```

### getLocalDeviceID

PhonePC/2in1TabletTVWearable

static getLocalDeviceID(): string

静态方法，获取本端设备ID。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回本地设备的ID。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class Stub extends rpc.RemoteObject {
5. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
6. option: rpc.MessageOption): boolean | Promise<boolean> {
7. try {
8. let localDeviceID = rpc.IPCSkeleton.getLocalDeviceID();
9. hilog.info(0x0000, 'testTag', 'RpcServer: localDeviceID is ' + localDeviceID);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
13. return true;
14. }
15. }
```

### isLocalCalling

PhonePC/2in1TabletTVWearable

static isLocalCalling(): boolean

静态方法，检查当前通信对端是否是本设备的进程。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：调用在同一台设备，false：调用未在同一台设备。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class Stub extends rpc.RemoteObject {
5. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
6. option: rpc.MessageOption): boolean | Promise<boolean> {
7. try {
8. let isLocalCalling = rpc.IPCSkeleton.isLocalCalling();
9. hilog.info(0x0000, 'testTag', 'RpcServer: isLocalCalling is ' + isLocalCalling);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
13. return true;
14. }
15. }
```

### flushCmdBuffer9+

PhonePC/2in1TabletTVWearable

static flushCmdBuffer(object: IRemoteObject): void

静态方法，将所有挂起的命令从指定的RemoteProxy刷新到相应的RemoteObject。建议在任何时间执行敏感操作之前调用此方法。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| object | [IRemoteObject](js-apis-rpc.md#iremoteobject) | 是 | 指定的RemoteProxy。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestRemoteObject extends rpc.RemoteObject {
6. constructor(descriptor: string) {
7. super(descriptor);
8. }
9. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
10. option: rpc.MessageOption): boolean | Promise<boolean> {
11. // 根据业务实际逻辑，进行相应处理
12. return true;
13. }
14. }
15. try {
16. let remoteObject = new TestRemoteObject("aaa");
17. rpc.IPCSkeleton.flushCmdBuffer(remoteObject);
18. } catch (error) {
19. let e: BusinessError = error as BusinessError;
20. hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorCode ' + e.code);
21. hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorMessage ' + e.message);
22. }
```

### flushCommands(deprecated)

PhonePC/2in1TabletTVWearable

static flushCommands(object: IRemoteObject): number

静态方法，将所有挂起的命令从指定的RemoteProxy刷新到相应的RemoteObject。建议在任何时间执行敏感操作之前调用此方法。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[flushCmdBuffer](js-apis-rpc.md#flushcmdbuffer9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| object | [IRemoteObject](js-apis-rpc.md#iremoteobject) | 是 | 指定的RemoteProxy。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 如果操作成功，返回0；如果输入对象为空或RemoteObject，或者操作失败，返回错误代码。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class TestRemoteObject extends rpc.RemoteObject {
5. constructor(descriptor: string) {
6. super(descriptor);
7. }
8. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
9. option: rpc.MessageOption): boolean | Promise<boolean> {
10. // 根据业务实际逻辑，进行相应处理
11. return true;
12. }
13. }
14. try {
15. let remoteObject = new TestRemoteObject("aaa");
16. let ret = rpc.IPCSkeleton.flushCommands(remoteObject);
17. hilog.info(0x0000, 'testTag', 'RpcServer: flushCommands result: ' + ret);
18. } catch (error) {
19. let e: BusinessError = error as BusinessError;
20. hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorCode ' + e.code);
21. hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorMessage ' + e.message);
22. }
```

### resetCallingIdentity

PhonePC/2in1TabletTVWearable

static resetCallingIdentity(): string

静态方法，将远程用户的UID和PID替换为本地用户的UID和PID。它可以用于身份验证等场景。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回包含远程用户的UID和PID的字符串。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class Stub extends rpc.RemoteObject {
5. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
6. option: rpc.MessageOption): boolean | Promise<boolean> {
7. try {
8. let callingIdentity = rpc.IPCSkeleton.resetCallingIdentity();
9. hilog.info(0x0000, 'testTag', 'RpcServer: callingIdentity is ' + callingIdentity);
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'error ' + error);
12. }
13. return true;
14. }
15. }
```

### restoreCallingIdentity9+

PhonePC/2in1TabletTVWearable

static restoreCallingIdentity(identity: string): void

静态方法，将UID和PID恢复为远程用户的UID和PID。它通常在使用resetCallingIdentity后调用，需要resetCallingIdentity返回的远程用户的UID和PID。该接口仅支持在IPC上下文（[onRemoteMessageRequest](js-apis-rpc.md#onremotemessagerequest9)）中使用，否则直接返回。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| identity | string | 是 | 标识表示包含远程用户UID和PID的字符串，其长度应小于40960字节。由resetCallingIdentity返回。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.The string length is greater than or equal to 40960 bytes;  4.The number of bytes copied to the buffer is different from the length of the obtained string. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class Stub extends rpc.RemoteObject {
5. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
6. option: rpc.MessageOption): boolean | Promise<boolean> {
7. try {
8. let callingIdentity = rpc.IPCSkeleton.resetCallingIdentity();
9. hilog.info(0x0000, 'testTag', 'RpcServer: callingIdentity is ' + callingIdentity);
10. rpc.IPCSkeleton.restoreCallingIdentity(callingIdentity);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error ' + error);
13. }
14. return true;
15. }
16. }
```

### setCallingIdentity(deprecated)

PhonePC/2in1TabletTVWearable

static setCallingIdentity(identity: string): boolean

静态方法，将UID和PID恢复为远程用户的UID和PID。它通常在使用resetCallingIdentity后调用，需要resetCallingIdentity返回的远程用户的UID和PID。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[restoreCallingIdentity](js-apis-rpc.md#restorecallingidentity9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| identity | string | 是 | 标识表示包含远程用户UID和PID的字符串。由resetCallingIdentity返回。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：设置成功，false：设置失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class Stub extends rpc.RemoteObject {
5. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
6. option: rpc.MessageOption): boolean | Promise<boolean> {
7. try {
8. let callingIdentity = rpc.IPCSkeleton.resetCallingIdentity();
9. hilog.info(0x0000, 'testTag', 'RpcServer: callingIdentity is ' + callingIdentity);
10. let ret = rpc.IPCSkeleton.setCallingIdentity(callingIdentity);
11. hilog.info(0x0000, 'testTag', 'RpcServer: setCallingIdentity is ' + ret);
12. } catch (error) {
13. hilog.error(0x0000, 'testTag', 'error ' + error);
14. }
15. return true;
16. }
17. }
```

## RemoteObject

PhonePC/2in1TabletTVWearable

实现远程对象。服务提供者必须继承此类。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

### constructor

PhonePC/2in1TabletTVWearable

constructor(descriptor: string)

RemoteObject构造函数。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | string | 是 | 接口描述符，其长度应小于40960字节。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';

3. class TestRemoteObject extends rpc.RemoteObject {
4. constructor(descriptor: string) {
5. super(descriptor);
6. }
7. }
```

### sendRequest(deprecated)

PhonePC/2in1TabletTVWearable

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendRequest返回时兑现，回复内容在reply报文里。

说明

从API version 7 开始支持，API version 8 开始废弃，建议使用[sendMessageRequest](js-apis-rpc.md#sendmessagerequest9-4)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 本次请求调用的消息码[1-16777215]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：发送成功，false：发送失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class testRemoteObject extends rpc.RemoteObject {
5. onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
6. option: rpc.MessageOption): boolean {
7. // 根据业务实际逻辑，进行相应处理
8. return true;
9. }
10. }
11. try {
12. let testRemoteObject = new TestRemoteObject("testObject");
13. let option = new rpc.MessageOption();
14. let data = rpc.MessageParcel.create();
15. let reply = rpc.MessageParcel.create();
16. data.writeInt(1);
17. data.writeString("hello");
18. let ret: boolean = testRemoteObject.sendRequest(1, data, reply, option);
19. if (ret) {
20. hilog.info(0x0000, 'testTag', 'sendRequest got result');
21. let msg = reply.readString();
22. hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
23. } else {
24. hilog.error(0x0000, 'testTag', 'sendRequest failed');
25. }
26. hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
27. data.reclaim();
28. reply.reclaim();
29. } catch (error) {
30. hilog.error(0x0000, 'testTag', 'error ' + error);
31. }
```

### sendMessageRequest9+

PhonePC/2in1TabletTVWearable

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): Promise<RequestResult>

以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendMessageRequest返回时兑现，回复内容在reply报文里。使用Promise异步回调。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 本次请求调用的消息码[1-16777215]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 保存待发送数据的MessageSequence对象。 |
| reply | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 接收应答数据的MessageSequence对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RequestResult](js-apis-rpc.md#requestresult9)> | Promise对象，返回一个期约，兑现值是RequestResult实例。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.Failed to obtain the passed object instance. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class TestRemoteObject extends rpc.RemoteObject {
5. constructor(descriptor: string) {
6. super(descriptor);
7. }
8. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
9. option: rpc.MessageOption): boolean | Promise<boolean> {
10. // 根据业务实际逻辑，进行相应处理
11. return true;
12. }
13. }
14. try {
15. let testRemoteObject = new TestRemoteObject("testObject");
16. let option = new rpc.MessageOption();
17. let data = rpc.MessageSequence.create();
18. let reply = rpc.MessageSequence.create();
19. data.writeInt(1);
20. data.writeString("hello");
21. testRemoteObject.sendMessageRequest(1, data, reply, option)
22. .then((result: rpc.RequestResult) => {
23. if (result.errCode === 0) {
24. hilog.info(0x0000, 'testTag', 'sendMessageRequest got result');
25. let num = result.reply.readInt();
26. let msg = result.reply.readString();
27. hilog.info(0x0000, 'testTag', 'reply num: ' + num);
28. hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
29. } else {
30. hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode: ' + result.errCode);
31. }
32. }).catch((e: Error) => {
33. hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error: ' + JSON.stringify(e));
34. }).finally (() => {
35. hilog.info(0x0000, 'testTag', 'sendMessageRequest ends, reclaim parcel');
36. data.reclaim();
37. reply.reclaim();
38. });
39. } catch (error) {
40. hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error: ' + error);
41. }
```

### sendRequest(deprecated)

PhonePC/2in1TabletTVWearable

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): Promise<SendRequestResult>

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendRequest返回时兑现，回复内容在reply报文里。使用Promise异步回调。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[sendMessageRequest](js-apis-rpc.md#sendmessagerequest9-4)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 本次请求调用的消息码[1-16777215]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SendRequestResult](js-apis-rpc.md#sendrequestresultdeprecated)> | Promise对象，返回一个期约，兑现值是sendRequestResult实例。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class TestRemoteObject extends rpc.RemoteObject {
5. constructor(descriptor: string) {
6. super(descriptor);
7. }
8. onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
9. // 根据业务实际逻辑，进行相应处理
10. return true;
11. }
12. }
13. try {
14. let testRemoteObject = new TestRemoteObject("testObject");
15. let option = new rpc.MessageOption();
16. let data = rpc.MessageParcel.create();
17. let reply = rpc.MessageParcel.create();
18. data.writeInt(1);
19. data.writeString("hello");
20. let a = testRemoteObject.sendRequest(1, data, reply, option) as Object;
21. let b = a as Promise<rpc.SendRequestResult>;
22. b.then((result: rpc.SendRequestResult) => {
23. if (result.errCode === 0) {
24. hilog.info(0x0000, 'testTag', 'sendRequest got result');
25. let num = result.reply.readInt();
26. let msg = result.reply.readString();
27. hilog.info(0x0000, 'testTag', 'reply num: ' + num);
28. hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
29. } else {
30. hilog.error(0x0000, 'testTag', 'sendRequest failed, errCode: ' + result.errCode);
31. }
32. }).catch((e: Error) => {
33. hilog.error(0x0000, 'testTag', 'sendRequest failed, error: ' + JSON.stringify(e));
34. }).finally (() => {
35. hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
36. data.reclaim();
37. reply.reclaim();
38. });
39. } catch (error) {
40. hilog.error(0x0000, 'testTag', 'error: ' + error);
41. }
```

### sendMessageRequest9+

PhonePC/2in1TabletTVWearable

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callback: AsyncCallback<RequestResult>): void

以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendMessageRequest返回时收到回调，回复内容在reply报文里。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 本次请求调用的消息码[1-16777215]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 保存待发送数据的MessageSequence对象。 |
| reply | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 接收应答数据的MessageSequence对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |
| callback | AsyncCallback<[RequestResult](js-apis-rpc.md#requestresult9)> | 是 | 回调函数。当消息发送成功时，可从RequestResult中读取服务端返回的数据。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.Failed to obtain the passed object instance. |

### sendRequest(deprecated)

PhonePC/2in1TabletTVWearable

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption, callback: AsyncCallback<SendRequestResult>): void

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendRequest返回时收到回调，回复内容在reply报文里。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[sendMessageRequest](js-apis-rpc.md#sendmessagerequest9-5)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 本次请求调用的消息码[1-16777215]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |
| callback | AsyncCallback<[SendRequestResult](js-apis-rpc.md#sendrequestresultdeprecated)> | 是 | 接收发送结果的回调。 |

### onRemoteMessageRequest23+

PhonePC/2in1TabletTVWearable

onRemoteMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callingInfo?: CallingInfo): boolean | Promise<boolean>

sendMessageRequest请求的响应处理函数，服务端在该函数里同步或异步地处理请求，回复结果，该接口可从入参callingInfo中获取IPC上下文信息。

说明

开发者应优先选择重写带有CallingInfo参数的onRemoteMessageRequest方法，其中可以自由实现同步和异步的消息处理。

开发者同时重写onRemoteRequest和onRemoteMessageRequest方法时，仅onRemoteMessageRequest方法生效。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 对端发送的服务请求码。 |
| data | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 携带客户端调用参数的MessageSequence对象。 |
| reply | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 写入结果的MessageSequence对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 指示操作是同步还是异步。 |
| callingInfo | [CallingInfo](js-apis-rpc.md#callinginfo23) | 否 | 获取IPC上下文信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Promise<boolean> | - 若在onRemoteMessageRequest中同步处理请求，则返回一个布尔值。返回true表示操作成功，返回false表示操作失败。  - 若在onRemoteMessageRequest中异步处理请求，则返回一个Promise对象。返回true表示操作成功，返回false表示操作失败。 |

**示例：**

```
1. // 重写onRemoteMessageRequest方法同步处理请求
2. import { rpc } from '@kit.IPCKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. class TestRemoteObject extends rpc.RemoteObject {
6. constructor(descriptor: string) {
7. super(descriptor);
8. }

10. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
11. option: rpc.MessageOption, callingInfo?: rpc.CallingInfo): boolean | Promise<boolean> {
12. if (code === 1) {
13. hilog.info(0x0000, 'testTag', 'RpcServer: sync onRemoteMessageRequest is called');
14. let pid = callingInfo?.callerPid;
15. return true;
16. } else {
17. hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
18. return false;
19. }
20. }
21. }
```

**示例：**

```
1. // 重写onRemoteMessageRequest方法异步处理请求
2. import { rpc } from '@kit.IPCKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. class TestRemoteObject extends rpc.RemoteObject {
6. constructor(descriptor: string) {
7. super(descriptor);
8. }

10. async onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
11. option: rpc.MessageOption, callingInfo?: rpc.CallingInfo): Promise<boolean> {
12. if (code === 1) {
13. hilog.info(0x0000, 'testTag', 'RpcServer: async onRemoteMessageRequest is called');
14. let pid = callingInfo?.callerPid;
15. } else {
16. hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
17. return false;
18. }
19. await new Promise((resolve: (data: rpc.RequestResult) => void) => {
20. setTimeout(resolve, 100);
21. })
22. return true;
23. }
24. }
```

**示例：**

```
1. // 同时重写onRemoteMessageRequest和onRemoteRequest方法同步处理请求
2. import { rpc } from '@kit.IPCKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. class TestRemoteObject extends rpc.RemoteObject {
6. constructor(descriptor: string) {
7. super(descriptor);
8. }

10. onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
11. if (code === 1) {
12. hilog.info(0x0000, 'testTag', 'RpcServer: sync onRemoteMessageRequest is called');
13. return true;
14. } else {
15. hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
16. return false;
17. }
18. }
19. // 同时调用仅会执行onRemoteMessageRequest
20. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
21. option: rpc.MessageOption, callingInfo?: rpc.CallingInfo): boolean | Promise<boolean> {
22. if (code === 1) {
23. hilog.info(0x0000, 'testTag', 'RpcServer: async onRemoteMessageRequest is called');
24. let pid = callingInfo?.callerPid;
25. } else {
26. hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
27. return false;
28. }
29. return true;
30. }
31. }
```

### onRemoteMessageRequest9+

PhonePC/2in1TabletTVWearable

onRemoteMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): boolean | Promise<boolean>

sendMessageRequest请求的响应处理函数，服务端在该函数里同步或异步地处理请求，回复结果。

说明

开发者应优先选择重写onRemoteMessageRequest方法，其中可以自由实现同步和异步的消息处理。

开发者同时重写onRemoteRequest和onRemoteMessageRequest方法时，仅onRemoteMessageRequest方法生效。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 对端发送的服务请求码。 |
| data | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 携带客户端调用参数的MessageSequence对象。 |
| reply | [MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 写入结果的MessageSequence对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 指示操作是同步还是异步。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Promise<boolean> | - 若在onRemoteMessageRequest中同步处理请求，则返回一个布尔值。返回true表示操作成功，返回false表示操作失败。  - 若在onRemoteMessageRequest中异步处理请求，则返回一个Promise对象。返回true表示操作成功，返回false表示操作失败。 |

**示例：**

```
1. // 重写onRemoteMessageRequest方法同步处理请求
2. import { rpc } from '@kit.IPCKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. class TestRemoteObject extends rpc.RemoteObject {
6. constructor(descriptor: string) {
7. super(descriptor);
8. }

10. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
11. option: rpc.MessageOption): boolean {
12. if (code === 1) {
13. hilog.info(0x0000, 'testTag', 'RpcServer: sync onRemoteMessageRequest is called');
14. return true;
15. } else {
16. hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
17. return false;
18. }
19. }
20. }
```

**示例：**

```
1. // 重写onRemoteMessageRequest方法异步处理请求
2. import { rpc } from '@kit.IPCKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. class TestRemoteObject extends rpc.RemoteObject {
6. constructor(descriptor: string) {
7. super(descriptor);
8. }

10. async onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
11. option: rpc.MessageOption): Promise<boolean> {
12. if (code === 1) {
13. hilog.info(0x0000, 'testTag', 'RpcServer: async onRemoteMessageRequest is called');
14. } else {
15. hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
16. return false;
17. }
18. await new Promise((resolve: (data: rpc.RequestResult) => void) => {
19. setTimeout(resolve, 100);
20. })
21. return true;
22. }
23. }
```

**示例：**

```
1. // 同时重写onRemoteMessageRequest和onRemoteRequest方法同步处理请求
2. import { rpc } from '@kit.IPCKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. class TestRemoteObject extends rpc.RemoteObject {
6. constructor(descriptor: string) {
7. super(descriptor);
8. }

10. onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
11. if (code === 1) {
12. hilog.info(0x0000, 'testTag', 'RpcServer: sync onRemoteMessageRequest is called');
13. return true;
14. } else {
15. hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
16. return false;
17. }
18. }
19. // 同时调用仅会执行onRemoteMessageRequest
20. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
21. option: rpc.MessageOption): boolean | Promise<boolean> {
22. if (code === 1) {
23. hilog.info(0x0000, 'testTag', 'RpcServer: async onRemoteMessageRequest is called');
24. } else {
25. hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
26. return false;
27. }
28. return true;
29. }
30. }
```

### onRemoteRequest(deprecated)

PhonePC/2in1TabletTVWearable

onRemoteRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean

sendRequest请求的响应处理函数，服务端在该函数里处理请求，回复结果。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[onRemoteMessageRequest](js-apis-rpc.md#onremotemessagerequest9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 对端发送的服务请求码。 |
| data | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 携带客户端调用参数的MessageParcel对象。 |
| reply | [MessageParcel](js-apis-rpc.md#messageparceldeprecated) | 是 | 写入结果的MessageParcel对象。 |
| options | [MessageOption](js-apis-rpc.md#messageoption) | 是 | 指示操作是同步还是异步。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：操作成功，false：操作失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class TestRemoteObject extends rpc.RemoteObject {
5. constructor(descriptor: string) {
6. super(descriptor);
7. }
8. onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
9. if (code === 1) {
10. hilog.info(0x0000, 'testTag', 'RpcServer: onRemoteRequest called');
11. return true;
12. } else {
13. hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
14. return false;
15. }
16. }
17. }
```

### getCallingUid

PhonePC/2in1TabletTVWearable

getCallingUid(): number

获取通信对端的进程Uid。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回通信对端的进程Uid。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class TestRemoteObject extends rpc.RemoteObject {
5. constructor(descriptor: string) {
6. super(descriptor);
7. }
8. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
9. option: rpc.MessageOption): boolean | Promise<boolean> {
10. // 根据业务实际逻辑，进行相应处理
11. return true;
12. }
13. }
14. try {
15. let testRemoteObject = new TestRemoteObject("testObject");
16. hilog.info(0x0000, 'testTag', 'RpcServer: getCallingUid: ' + testRemoteObject.getCallingUid());
17. } catch (error) {
18. hilog.error(0x0000, 'testTag', 'error: ' + error);
19. }
```

### getCallingPid

PhonePC/2in1TabletTVWearable

getCallingPid(): number

获取通信对端的进程Pid。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回通信对端的进程Pid。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class TestRemoteObject extends rpc.RemoteObject {
5. constructor(descriptor: string) {
6. super(descriptor);
7. }
8. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
9. option: rpc.MessageOption): boolean | Promise<boolean> {
10. // 根据业务实际逻辑，进行相应处理
11. return true;
12. }
13. }
14. try {
15. let testRemoteObject = new TestRemoteObject("testObject");
16. hilog.info(0x0000, 'testTag', 'RpcServer: getCallingPid: ' + testRemoteObject.getCallingPid());
17. } catch (error) {
18. hilog.error(0x0000, 'testTag', 'error: ' + error);
19. }
```

### getLocalInterface9+

PhonePC/2in1TabletTVWearable

getLocalInterface(descriptor: string): IRemoteBroker

查询接口描述符的字符串。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | string | 是 | 接口描述符的字符串，其长度应小于40960字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IRemoteBroker](js-apis-rpc.md#iremotebroker) | 返回绑定到指定接口描述符的IRemoteBroker对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.The string length is greater than or equal to 40960 bytes;  4.The number of bytes copied to the buffer is different from the length of the obtained string. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestRemoteObject extends rpc.RemoteObject {
6. constructor(descriptor: string) {
7. super(descriptor);
8. }
9. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
10. option: rpc.MessageOption): boolean | Promise<boolean> {
11. // 根据业务实际逻辑，进行相应处理
12. return true;
13. }
14. }
15. try {
16. let testRemoteObject = new TestRemoteObject("testObject");
17. testRemoteObject.getLocalInterface("testObject");
18. } catch (error) {
19. let e: BusinessError = error as BusinessError;
20. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
21. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
22. }
```

### queryLocalInterface(deprecated)

PhonePC/2in1TabletTVWearable

queryLocalInterface(descriptor: string): IRemoteBroker

查询并获取当前接口描述符对应的远端对象是否已经存在。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[getLocalInterface](js-apis-rpc.md#getlocalinterface9-2)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | string | 是 | 需要查询的接口描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IRemoteBroker](js-apis-rpc.md#iremotebroker) | 如果接口描述符对应的远端对象存在，则返回该远端对象，否则返回Null。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class TestRemoteObject extends rpc.RemoteObject {
5. constructor(descriptor: string) {
6. super(descriptor);
7. }
8. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
9. option: rpc.MessageOption): boolean | Promise<boolean> {
10. // 根据业务实际逻辑，进行相应处理
11. return true;
12. }
13. }
14. try {
15. let testRemoteObject = new TestRemoteObject("testObject");
16. testRemoteObject.queryLocalInterface("testObject");
17. } catch (error) {
18. hilog.error(0x0000, 'testTag', 'error: ' + error);
19. }
```

### getDescriptor9+

PhonePC/2in1TabletTVWearable

getDescriptor(): string

获取对象的接口描述符。接口描述符为字符串。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回接口描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900008 | The proxy or remote object is invalid. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestRemoteObject extends rpc.RemoteObject {
6. constructor(descriptor: string) {
7. super(descriptor);
8. }
9. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
10. option: rpc.MessageOption): boolean | Promise<boolean> {
11. // 根据业务实际逻辑，进行相应处理
12. return true;
13. }
14. }
15. try {
16. let testObject = new TestRemoteObject("ipcTest");
17. let descriptor = testObject.getDescriptor();
18. hilog.info(0x0000, 'testTag', 'RpcServer: descriptor is ' + descriptor);
19. } catch (error) {
20. let e: BusinessError = error as BusinessError;
21. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
22. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
23. }
```

### getInterfaceDescriptor(deprecated)

PhonePC/2in1TabletTVWearable

getInterfaceDescriptor(): string

查询接口描述符。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[getDescriptor](js-apis-rpc.md#getdescriptor9-2)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回接口描述符。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class TestRemoteObject extends rpc.RemoteObject {
5. constructor(descriptor: string) {
6. super(descriptor);
7. }
8. onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
9. option: rpc.MessageOption): boolean | Promise<boolean> {
10. // 根据业务实际逻辑，进行相应处理
11. return true;
12. }
13. }

15. try {
16. let testRemoteObject = new TestRemoteObject("testObject");
17. let descriptor = testRemoteObject.getInterfaceDescriptor();
18. hilog.info(0x0000, 'testTag', 'RpcServer: descriptor is: ' + descriptor);
19. } catch (error) {
20. hilog.error(0x0000, 'testTag', 'error ' + error);
21. }
```

### modifyLocalInterface9+

PhonePC/2in1TabletTVWearable

modifyLocalInterface(localInterface: IRemoteBroker, descriptor: string): void

此接口用于把接口描述符和IRemoteBroker对象绑定。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localInterface | [IRemoteBroker](js-apis-rpc.md#iremotebroker) | 是 | 将与描述符绑定的IRemoteBroker对象。 |
| descriptor | string | 是 | 用于与IRemoteBroker对象绑定的描述符，其长度应小于40960字节。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.The string length is greater than or equal to 40960 bytes;  4.The number of bytes copied to the buffer is different from the length of the obtained string. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class MyDeathRecipient implements rpc.DeathRecipient {
6. onRemoteDied() {
7. hilog.info(0x0000, 'testTag', 'server died');
8. }
9. }
10. class TestRemoteObject extends rpc.RemoteObject {
11. constructor(descriptor: string) {
12. super(descriptor);
13. try {
14. this.modifyLocalInterface(this, descriptor);
15. } catch (error) {
16. let e: BusinessError = error as BusinessError;
17. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
18. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
19. }
20. }
21. registerDeathRecipient(recipient: MyDeathRecipient, flags: number) {
22. // 方法逻辑需开发者根据业务需要实现
23. }
24. unregisterDeathRecipient(recipient: MyDeathRecipient, flags: number) {
25. // 方法逻辑需开发者根据业务需要实现
26. }
27. }
28. let testRemoteObject = new TestRemoteObject("testObject");
```

### attachLocalInterface(deprecated)

PhonePC/2in1TabletTVWearable

attachLocalInterface(localInterface: IRemoteBroker, descriptor: string): void

此接口用于把接口描述符和IRemoteBroker对象绑定。

说明

从API version 7 开始支持，API version 9 开始废弃，建议使用[modifyLocalInterface](js-apis-rpc.md#modifylocalinterface9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localInterface | [IRemoteBroker](js-apis-rpc.md#iremotebroker) | 是 | 将与描述符绑定的IRemoteBroker对象。 |
| descriptor | string | 是 | 用于与IRemoteBroker对象绑定的描述符。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class MyDeathRecipient implements rpc.DeathRecipient {
5. onRemoteDied() {
6. hilog.info(0x0000, 'testTag', 'server died');
7. }
8. }
9. class TestRemoteObject extends rpc.RemoteObject {
10. constructor(descriptor: string) {
11. super(descriptor);
12. this.attachLocalInterface(this, descriptor);
13. }
14. addDeathRecipient(recipient: MyDeathRecipient, flags: number): boolean {
15. // 方法逻辑需开发者根据业务需要实现
16. return true;
17. }
18. removeDeathRecipient(recipient: MyDeathRecipient, flags: number): boolean {
19. // 方法逻辑需开发者根据业务需要实现
20. return true;
21. }
22. }
23. let testRemoteObject = new TestRemoteObject("testObject");
```

## Ashmem8+

PhonePC/2in1TabletTVWearable

提供与匿名共享内存对象相关的方法，包括创建、关闭、映射和取消映射Ashmem、从Ashmem读取数据和写入数据、获取Ashmem大小、设置Ashmem保护。

共享内存只适用与本设备内跨进程通信。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

### 属性

PhonePC/2in1TabletTVWearable

\*\*系统能力：\*\*以下各项对应的系统能力均为SystemCapability.Communication.IPC.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| PROT\_EXEC | number | 是 | 否 | 映射内存保护类型，代表映射的内存可执行。 |
| PROT\_NONE | number | 是 | 否 | 映射内存保护类型，代表映射的内存不可访问。 |
| PROT\_READ | number | 是 | 否 | 映射内存保护类型，代表映射的内存可读。 |
| PROT\_WRITE | number | 是 | 否 | 映射内存保护类型，代表映射的内存可写。 |

### create9+

PhonePC/2in1TabletTVWearable

static create(name: string, size: number): Ashmem

静态方法，根据指定的名称和大小创建Ashmem对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | Ashmem名称，用于查询Ashmem信息，其长度不能为0。 |
| size | number | 是 | Ashmem的大小，其大小应大于0，以字节为单位。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Ashmem](js-apis-rpc.md#ashmem8) | 返回创建的Ashmem对象；如果创建失败，返回null。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.The Ashmem name passed is empty;  4.The Ashmem size passed is less than or equal to 0. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
7. hilog.info(0x0000, 'testTag', 'create ashmem: ' + ashmem);
8. let size = ashmem.getAshmemSize();
9. hilog.info(0x0000, 'testTag',  'size is ' + size);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### createAshmem(deprecated)

PhonePC/2in1TabletTVWearable

static createAshmem(name: string, size: number): Ashmem

静态方法，根据指定的名称和大小创建Ashmem对象。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[create](js-apis-rpc.md#create9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 名称，用于查询Ashmem信息。 |
| size | number | 是 | Ashmem的大小，以字节为单位。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Ashmem](js-apis-rpc.md#ashmem8) | 返回创建的Ashmem对象；如果创建失败，返回null。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let ashmem = rpc.Ashmem.createAshmem("ashmem", 1024*1024);
6. hilog.info(0x0000, 'testTag', 'create ashmem: ' + ashmem);
7. let size = ashmem.getAshmemSize();
8. hilog.info(0x0000, 'testTag',  'size is ' + size);
9. } catch (error) {
10. hilog.error(0x0000, 'testTag', 'error ' + error);
11. }
```

### create9+

PhonePC/2in1TabletTVWearable

static create(ashmem: Ashmem): Ashmem

静态方法，通过复制现有Ashmem对象的文件描述符(fd)来创建Ashmem对象。两个Ashmem对象指向同一个共享内存区域。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ashmem | [Ashmem](js-apis-rpc.md#ashmem8) | 是 | 已存在的Ashmem对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Ashmem](js-apis-rpc.md#ashmem8) | 返回创建的Ashmem对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The passed parameter is not an Ashmem object;  3.The ashmem instance for obtaining packaging is empty. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
7. let ashmem2 = rpc.Ashmem.create(ashmem);
8. let size = ashmem2.getAshmemSize();
9. hilog.info(0x0000, 'testTag', 'size is ' + size);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
14. }
```

### createAshmemFromExisting(deprecated)

PhonePC/2in1TabletTVWearable

static createAshmemFromExisting(ashmem: Ashmem): Ashmem

静态方法，通过复制现有Ashmem对象的文件描述符(fd)来创建Ashmem对象。两个Ashmem对象指向同一个共享内存区域。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[create](js-apis-rpc.md#create9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ashmem | [Ashmem](js-apis-rpc.md#ashmem8) | 是 | 已存在的Ashmem对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Ashmem](js-apis-rpc.md#ashmem8) | 返回创建的Ashmem对象。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
6. let ashmem2 = rpc.Ashmem.createAshmemFromExisting(ashmem);
7. let size = ashmem2.getAshmemSize();
8. hilog.info(0x0000, 'testTag', 'size is ' + size);
9. } catch (error) {
10. hilog.error(0x0000, 'testTag', 'error is ' + error);
11. }
```

### closeAshmem8+

PhonePC/2in1TabletTVWearable

closeAshmem(): void

关闭这个Ashmem。

说明

关闭Ashmem对象前需要先解除地址映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
6. ashmem.closeAshmem();
7. } catch (error) {
8. hilog.error(0x0000, 'testTag', 'error is ' + error);
9. }
```

### unmapAshmem8+

PhonePC/2in1TabletTVWearable

unmapAshmem(): void

删除该Ashmem对象的地址映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
6. ashmem.unmapAshmem();
7. } catch (error) {
8. hilog.error(0x0000, 'testTag', 'error is ' + error);
9. }
```

### getAshmemSize8+

PhonePC/2in1TabletTVWearable

getAshmemSize(): number

获取Ashmem对象的内存大小。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回Ashmem对象的内存大小。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
6. let size = ashmem.getAshmemSize();
7. hilog.info(0x0000, 'testTag', ' size is ' + size);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error is ' + error);
10. }
```

### mapTypedAshmem9+

PhonePC/2in1TabletTVWearable

mapTypedAshmem(mapType: number): void

在此进程的虚拟地址空间上创建共享文件映射，映射区域大小由此Ashmem对象指定。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mapType | number | 是 | 指定映射的内存区域的保护等级。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.The passed mapType exceeds the maximum protection level. |
| 1900001 | Failed to call mmap. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
7. ashmem.mapTypedAshmem(rpc.Ashmem.PROT_READ | rpc.Ashmem.PROT_WRITE);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### mapAshmem(deprecated)

PhonePC/2in1TabletTVWearable

mapAshmem(mapType: number): boolean

在此进程的虚拟地址空间上创建共享文件映射，映射区域大小由此Ashmem对象指定。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[mapTypedAshmem](js-apis-rpc.md#maptypedashmem9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mapType | number | 是 | 指定映射的内存区域的保护等级。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：映射成功，false：映射失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
6. let mapReadAndWrite = ashmem.mapAshmem(rpc.Ashmem.PROT_READ | rpc.Ashmem.PROT_WRITE);
7. hilog.info(0x0000, 'testTag', 'map ashmem result is ' + mapReadAndWrite);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error is ' + error);
10. }
```

### mapReadWriteAshmem9+

PhonePC/2in1TabletTVWearable

mapReadWriteAshmem(): void

在此进程虚拟地址空间上创建可读写的共享文件映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900001 | Failed to call mmap. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
7. ashmem.mapReadWriteAshmem();
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### mapReadAndWriteAshmem(deprecated)

PhonePC/2in1TabletTVWearable

mapReadAndWriteAshmem(): boolean

在此进程虚拟地址空间上创建可读写的共享文件映射。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[mapReadWriteAshmem](js-apis-rpc.md#mapreadwriteashmem9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：映射成功，false：映射失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
6. let mapResult = ashmem.mapReadAndWriteAshmem();
7. hilog.info(0x0000, 'testTag', 'map ashmem result is ' + mapResult);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error is ' + error);
10. }
```

### mapReadonlyAshmem9+

PhonePC/2in1TabletTVWearable

mapReadonlyAshmem(): void

在此进程虚拟地址空间上创建只读的共享文件映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1900001 | Failed to call mmap. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
7. ashmem.mapReadonlyAshmem();
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
12. }
```

### mapReadOnlyAshmem(deprecated)

PhonePC/2in1TabletTVWearable

mapReadOnlyAshmem(): boolean

在此进程虚拟地址空间上创建只读的共享文件映射。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[mapReadonlyAshmem](js-apis-rpc.md#mapreadonlyashmem9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：映射成功，false：映射失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
6. let mapResult = ashmem.mapReadOnlyAshmem();
7. hilog.info(0x0000, 'testTag', 'Ashmem mapReadOnlyAshmem result is ' + mapResult);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'error is ' + error);
10. }
```

### setProtectionType9+

PhonePC/2in1TabletTVWearable

setProtectionType(protectionType: number): void

设置映射内存区域的保护等级。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| protectionType | number | 是 | 要设置的保护类型。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900002 | Failed to call ioctl. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
7. ashmem.setProtectionType(rpc.Ashmem.PROT_READ);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'Rpc set protection type fail, errorCode ' + e.code);
11. hilog.error(0x0000, 'testTag', 'Rpc set protection type fail, errorMessage ' + e.message);
12. }
```

### setProtection(deprecated)

PhonePC/2in1TabletTVWearable

setProtection(protectionType: number): boolean

设置映射内存区域的保护等级。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[setProtectionType](js-apis-rpc.md#setprotectiontype9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| protectionType | number | 是 | 要设置的保护类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：设置成功，false：设置失败。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
6. let result = ashmem.setProtection(rpc.Ashmem.PROT_READ);
7. hilog.info(0x0000, 'testTag', 'Ashmem setProtection result is ' + result);
8. } catch (error) {
9. let e: BusinessError = error as BusinessError;
10. hilog.error(0x0000, 'testTag', 'error ' + error);
11. }
```

### writeDataToAshmem11+

PhonePC/2in1TabletTVWearable

writeDataToAshmem(buf: ArrayBuffer, size: number, offset: number): void

将数据写入此Ashmem对象关联的共享文件。

说明

对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](js-apis-rpc.md#mapreadwriteashmem9)进行映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 写入Ashmem对象的数据。 |
| size | number | 是 | 要写入的数据大小。 |
| offset | number | 是 | 要写入的数据在此Ashmem对象关联的内存区间的起始位置。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.Failed to obtain arrayBuffer information. |
| 1900003 | Failed to write data to the shared memory. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let buffer = new ArrayBuffer(1024);
7. let int32View = new Int32Array(buffer);
8. for (let i = 0; i < int32View.length; i++) {
9. int32View[i] = i * 2 + 1;
10. }
11. let size = buffer.byteLength;
12. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
13. ashmem.mapReadWriteAshmem();
14. ashmem.writeDataToAshmem(buffer, size, 0);
15. } catch (error) {
16. let e: BusinessError = error as BusinessError;
17. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
18. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
19. }
```

### writeAshmem(deprecated)

PhonePC/2in1TabletTVWearable

writeAshmem(buf: number[], size: number, offset: number): void

将数据写入此Ashmem对象关联的共享文件。

说明

从API version 9 开始支持，API version 11 开始废弃，建议使用[writeDataToAshmem](js-apis-rpc.md#writedatatoashmem11)替代。

对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](js-apis-rpc.md#mapreadwriteashmem9)进行映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | number[] | 是 | 写入Ashmem对象的数据。 |
| size | number | 是 | 要写入的数据大小。 |
| offset | number | 是 | 要写入的数据在此Ashmem对象关联的内存区间的起始位置。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match;  3.The element does not exist in the array. |
| 1900003 | Failed to write data to the shared memory. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
7. ashmem.mapReadWriteAshmem();
8. let ByteArrayVar = [1, 2, 3, 4, 5];
9. ashmem.writeAshmem(ByteArrayVar, 5, 0);
10. } catch (error) {
11. let e: BusinessError = error as BusinessError;
12. hilog.error(0x0000, 'testTag', 'Rpc write to ashmem fail, errorCode ' + e.code);
13. hilog.error(0x0000, 'testTag', 'Rpc write to ashmem fail, errorMessage ' + e.message);
14. }
```

### writeToAshmem(deprecated)

PhonePC/2in1TabletTVWearable

writeToAshmem(buf: number[], size: number, offset: number): boolean

将数据写入此Ashmem对象关联的共享文件。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[writeDataToAshmem](js-apis-rpc.md#writedatatoashmem11)替代。

对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](js-apis-rpc.md#mapreadwriteashmem9)进行映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | number[] | 是 | 写入Ashmem对象的数据。 |
| size | number | 是 | 要写入的数据大小。 |
| offset | number | 是 | 要写入的数据在此Ashmem对象关联的内存区间的起始位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：如果数据写入成功，false：在其他情况下，如数据写入越界或未获得写入权限。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
6. let mapResult = ashmem.mapReadAndWriteAshmem();
7. hilog.info(0x0000, 'testTag', 'RpcTest map ashmem result is ' + mapResult);
8. let ByteArrayVar = [1, 2, 3, 4, 5];
9. let writeResult = ashmem.writeToAshmem(ByteArrayVar, 5, 0);
10. hilog.info(0x0000, 'testTag', 'write to Ashmem result is ' + writeResult);
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'error is ' + error);
13. }
```

### readDataFromAshmem11+

PhonePC/2in1TabletTVWearable

readDataFromAshmem(size: number, offset: number): ArrayBuffer

从此Ashmem对象关联的共享文件中读取数据。

说明

对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](js-apis-rpc.md#mapreadwriteashmem9)进行映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 要读取的数据的大小。 |
| offset | number | 是 | 要读取的数据在此Ashmem对象关联的内存区间的起始位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 返回读取的数据。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900004 | Failed to read data from the shared memory. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let buffer = new ArrayBuffer(1024);
7. let int32View = new Int32Array(buffer);
8. for (let i = 0; i < int32View.length; i++) {
9. int32View[i] = i * 2 + 1;
10. }
11. let size = buffer.byteLength;
12. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
13. ashmem.mapReadWriteAshmem();
14. ashmem.writeDataToAshmem(buffer, size, 0);
15. let readResult = ashmem.readDataFromAshmem(size, 0);
16. let readInt32View = new Int32Array(readResult);
17. hilog.info(0x0000, 'testTag', 'read from Ashmem result is ' + readInt32View);
18. } catch (error) {
19. let e: BusinessError = error as BusinessError;
20. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
21. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
22. }
```

### readAshmem(deprecated)

PhonePC/2in1TabletTVWearable

readAshmem(size: number, offset: number): number[]

从此Ashmem对象关联的共享文件中读取数据。

说明

从API version 9 开始支持，API version 11 开始废弃，建议使用[readDataFromAshmem](js-apis-rpc.md#readdatafromashmem11)替代。

对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](js-apis-rpc.md#mapreadwriteashmem9)进行映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 要读取的数据的大小。 |
| offset | number | 是 | 要读取的数据在此Ashmem对象关联的内存区间的起始位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回读取的数据。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](errorcode-rpc.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.The number of parameters is incorrect;  2.The parameter type does not match. |
| 1900004 | Failed to read data from the shared memory. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
7. ashmem.mapReadWriteAshmem();
8. let ByteArrayVar = [1, 2, 3, 4, 5];
9. ashmem.writeAshmem(ByteArrayVar, 5, 0);
10. let readResult = ashmem.readAshmem(5, 0);
11. hilog.info(0x0000, 'testTag', 'read from Ashmem result is ' + readResult);
12. } catch (error) {
13. let e: BusinessError = error as BusinessError;
14. hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
15. hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
16. }
```

### readFromAshmem(deprecated)

PhonePC/2in1TabletTVWearable

readFromAshmem(size: number, offset: number): number[]

从此Ashmem对象关联的共享文件中读取数据。

说明

从API version 8 开始支持，API version 9 开始废弃，建议使用[readDataFromAshmem](js-apis-rpc.md#readdatafromashmem11)替代。

对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](js-apis-rpc.md#mapreadwriteashmem9)进行映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 要读取的数据的大小。 |
| offset | number | 是 | 要读取的数据在此Ashmem对象关联的内存区间的起始位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回读取的数据。 |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
6. let mapResult = ashmem.mapReadAndWriteAshmem();
7. hilog.info(0x0000, 'testTag', 'RpcTest map ashmem result is ' + mapResult);
8. let ByteArrayVar = [1, 2, 3, 4, 5];
9. let writeResult = ashmem.writeToAshmem(ByteArrayVar, 5, 0);
10. hilog.info(0x0000, 'testTag', 'write to Ashmem result is ' + writeResult);
11. let readResult = ashmem.readFromAshmem(5, 0);
12. hilog.info(0x0000, 'testTag', 'read to Ashmem result is ' + readResult);
13. } catch (error) {
14. hilog.error(0x0000, 'testTag', 'error is ' + error);
15. }
```
