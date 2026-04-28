---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-urpcapi
title: urpc
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > ArkTS API > urpc
category: harmonyos-references
scraped_at: 2026-04-28T08:08:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f0ea77038e1915769f9d816fbb978499e2c36e39cad4156f1dcdf31e77fdfd39
---

本模块提供URPC功能。应用程序可通过URPC提供的生成代码接口发起RPC请求。常见的URPC方法包括[urpcStubCreate](remote-communication-urpcapi.md#urpcstubcreate)、[UrpcCall](remote-communication-urpcapi.md#urpccall)、[UrpcCancel](remote-communication-urpcapi.md#urpccancel)、[UrpcDestroy](remote-communication-urpcapi.md#urpcdestroy)。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.1(13)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { urpc } from "@kit.RemoteCommunicationKit";
```

## FlowbufType

PhonePC/2in1TabletTVWearable

type FlowbufType =

'INT8' | 'UINT8' | 'INT16' | 'UINT16' | 'INT32' | 'UINT32' | 'INT64' | 'UINT64' | 'BOOL' | 'FLOAT' | 'DOUBLE' | 'STRING' | 'BYTES' | 'MESSAGE' | 'REPEATED\_INT8' | 'REPEATED\_UINT8' | 'REPEATED\_INT16' | 'REPEATED\_UINT16' | 'REPEATED\_INT32' | 'REPEATED\_UINT32' | 'REPEATED\_INT64' | 'REPEATED\_UINT64' | 'REPEATED\_BOOL' | 'REPEATED\_FLOAT' | 'REPEATED\_DOUBLE' | 'REPEATED\_STRING' | 'REPEATED\_BYTES' | 'REPEATED\_MESSAGE' | 'ARRAY\_INT8' | 'ARRAY\_UINT8' | 'ARRAY\_INT16' | 'ARRAY\_UINT16' | 'ARRAY\_INT32' | 'ARRAY\_UINT32' | 'ARRAY\_INT64' | 'ARRAY\_UINT64' | 'ARRAY\_BOOL' | 'ARRAY\_FLOAT' | 'ARRAY\_DOUBLE';

表示通过URPC通信允许传入和接收返回值的类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| 'INT8' | 表示参数类型为'INT8'。 |
| 'UINT8' | 表示参数类型为'UINT8'。 |
| 'INT16' | 表示参数类型为'INT16'。 |
| 'UINT16' | 表示参数类型为'UINT16'。 |
| 'INT32' | 表示参数类型为'INT32'。 |
| 'UINT32' | 表示参数类型为'UINT32'。 |
| 'INT64' | 表示参数类型为'INT64'。 |
| 'UINT64' | 表示参数类型为'UINT64'。 |
| 'BOOL' | 表示参数类型为'BOOL'。 |
| 'FLOAT' | 表示参数类型为'FLOAT'。 |
| 'DOUBLE' | 表示参数类型为'DOUBLE'。 |
| 'STRING' | 表示参数类型为'STRING'。 |
| 'BYTES' | 表示参数类型为'BYTES'。 |
| 'MESSAGE' | 表示参数类型为自定义的'MESSAGE'。 |
| 'REPEATED\_INT8' | 表示参数类型为可变长度的'INT8'数组，该字段为预留字段，在当前版本不能使用。 |
| 'REPEATED\_UINT8' | 表示参数类型为可变长度的'UINT8'数组，该字段为预留字段，在当前版本不能使用。 |
| 'REPEATED\_INT16' | 表示参数类型为可变长度的'INT16'数组，该字段为预留字段，在当前版本不能使用。 |
| 'REPEATED\_UINT16' | 表示参数类型为可变长度的'UINT16'数组，该字段为预留字段，在当前版本不能使用。 |
| 'REPEATED\_INT32' | 表示参数类型为可变长度的'INT32'数组，该字段为预留字段，在当前版本不能使用。 |
| 'REPEATED\_UINT32' | 表示参数类型为可变长度的'UINT32'数组，该字段为预留字段，在当前版本不能使用。 |
| 'REPEATED\_INT64' | 表示参数类型为可变长度的'INT64'数组，该字段为预留字段，在当前版本不能使用。 |
| 'REPEATED\_UINT64' | 表示参数类型为可变长度的'UINT64'数组，该字段为预留字段，在当前版本不能使用。 |
| 'REPEATED\_BOOL' | 表示参数类型为可变长度的'BOOL'数组，该字段为预留字段，在当前版本不能使用。 |
| 'REPEATED\_FLOAT' | 表示参数类型为可变长度的'INT8'数组，该字段为预留字段，在当前版本不能使用。 |
| 'REPEATED\_DOUBLE' | 表示参数类型为可变长度的'DOUBLE'数组，该字段为预留字段，在当前版本不能使用。 |
| 'REPEATED\_STRING' | 表示参数类型为可变长度的'STRING'数组，该字段为预留字段，在当前版本不能使用。 |
| 'REPEATED\_BYTES' | 表示参数类型为可变长度的'BYTES'数组，该字段为预留字段，在当前版本不能使用。 |
| 'REPEATED\_MESSAGE' | 表示参数类型为可变长度的自定义'MESSAGE'数组，该字段为预留字段，在当前版本不能使用。 |
| 'ARRAY\_INT8' | 表示参数类型为固定长度的'INT8'数组，该字段为预留字段，在当前版本不能使用。 |
| 'ARRAY\_UINT8' | 表示参数类型为固定长度的'UINT8'数组，该字段为预留字段，在当前版本不能使用。 |
| 'ARRAY\_INT16' | 表示参数类型为固定长度的'INT16'数组，该字段为预留字段，在当前版本不能使用。 |
| 'ARRAY\_UINT16' | 表示参数类型为固定长度的'UINT16'数组，该字段为预留字段，在当前版本不能使用。 |
| 'ARRAY\_INT32' | 表示参数类型为固定长度的'INT32'数组，该字段为预留字段，在当前版本不能使用。 |
| 'ARRAY\_UINT32' | 表示参数类型为固定长度的'UINT32'数组，该字段为预留字段，在当前版本不能使用。 |
| 'ARRAY\_INT64' | 表示参数类型为固定长度的'INT64'数组，该字段为预留字段，在当前版本不能使用。 |
| 'ARRAY\_UINT64' | 表示参数类型为固定长度的'UINT64'数组，该字段为预留字段，在当前版本不能使用。 |
| 'ARRAY\_BOOL' | 表示参数类型为固定长度的'BOOL'数组，该字段为预留字段，在当前版本不能使用。 |
| 'ARRAY\_FLOAT' | 表示参数类型为固定长度的'FLOAT'数组，该字段为预留字段，在当前版本不能使用。 |
| 'ARRAY\_DOUBLE' | 表示参数类型为固定长度的'DOUBLE'数组，该字段为预留字段，在当前版本不能使用。 |

## FlowbufElement<T>

PhonePC/2in1TabletTVWearable

FlowbufElement<T>用于定义非数组的URPC入参和返回值类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [FlowbufType](remote-communication-urpcapi.md#flowbuftype) | 否 | 否 | 表示通过URPC通信允许传入和接收返回值的类型。 |
| value | T | 否 | 否 | 表示该参数的具体数值。例如，如果type的值为'INT8'，则value为number类型，可配置0。 |
| name | string | 否 | 否 | 表示该参数的名称。 |

**示例：**

```
1. import { urpc } from "@kit.RemoteCommunicationKit"

3. let version: urpc.FlowbufElement<number> = {type: 'INT8', value: 0, name: ""};
```

## FlowbufArrayElement<T>

PhonePC/2in1TabletTVWearable

FlowbufArrayElement<T>用于定义数组类型的URPC入参和返回值类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [FlowbufType](remote-communication-urpcapi.md#flowbuftype) | 否 | 否 | 表示通过URPC通信允许传送和接收返回值的类型。 |
| value | T[] | 否 | 否 | 表示该参数的具体数值。例如，如果type的值为'ARRAY\_INT8'，则value为number[]类型，可配置[1,2,3]。 |
| length | number | 否 | 否 | 表示该参数数组的长度，长度范围[0, 2147483647]。 |

**示例：**

```
1. import { urpc } from "@kit.RemoteCommunicationKit"

3. let version: urpc.FlowbufArrayElement<number> = {type: 'ARRAY_INT8', value: [1,2,3], length: 3};
```

## urpcStubCreate

PhonePC/2in1TabletTVWearable

urpcStubCreate(config: UrpcInitConfiguration, funcList: string | string[]): Promise<UrpcStub>

创建UrpcStub，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**需要权限：** ohos.permission.INTERNET

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [UrpcInitConfiguration](remote-communication-urpcapi.md#urpcinitconfiguration) | 是 | stub配置。 |
| funcList | string | string[] | 是 | URPC函数调用列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[UrpcStub](remote-communication-urpcapi.md#urpcstub)> | Promise对象，返回可用于发出URPC请求的对象。 |

**错误码：**

错误码的详细介绍请参见[API错误码](remote-communication-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 10079100998 | Function name error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { urpc } from "@kit.RemoteCommunicationKit";

4. let node: urpc.IpAndPort = {
5. ip: '127.0.0.1',
6. port: 8000
7. }
8. let connect: urpc.UrpcConnectConfiguration = {
9. node: node,
10. protocol: 'eat',
11. }
12. let config: urpc.UrpcInitConfiguration = {
13. timeout: 3000,
14. mode: 'client',
15. connect: connect
16. }

18. const funcList:string[] = ["uploadFile"];
19. urpc.urpcStubCreate(config, funcList).then((urpcStub: urpc.UrpcStub) => {
20. urpcStub.destroy();
21. }).catch((err: BusinessError<string>) => {
22. console.error(`Failed to create urpc stub, error code ${err.code}, error info ${err.data}`);
23. })
```

## UrpcCall

PhonePC/2in1TabletTVWearable

type UrpcCall = (funcName: string, request: object, returnValue: object, config?: CallingOption) => UrpcPromise;

用于发起一个URPC请求，并接收来自服务器的响应。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| funcName | string | 是 | URPC请求函数名。 |
| request | object | 是 | URPC请求对象。对象体积最大值为1MB。如果超出最大值，抛出错误码[1007910001](remote-communication-error-code.md#section1007910001-请求数据传输错误)。 |
| returnValue | object | 是 | URPC响应对象。对象体积最大值为100KB。如果超出最大值，抛出错误码[1007910006](remote-communication-error-code.md#section1007910006-请求大小达到上限)。 |
| config | [CallingOption](remote-communication-urpcapi.md#callingoption) | 否 | 单次请求配置选项。该字段为预留字段，在当前版本并不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UrpcPromise](remote-communication-urpcapi.md#urpcpromise) | Promise对象，返回来自服务器的响应对象。 |

**错误码：** 错误码的详细介绍请参见[API错误码](remote-communication-error-code.md)。

## UrpcCancel

PhonePC/2in1TabletTVWearable

type UrpcCancel = (callingId?: number | number[]) => void;

用于取消指定或所有正在进行的URPC请求。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callingId | number | number[] | 否 | 取消指定callingId的请求。如果不填该字段表示取消本次UrpcStub对应的所有请求，取值范围[0, 2147483647]。 |

**错误码：** 错误码的详细介绍请参见[API错误码](remote-communication-error-code.md)。

## UrpcDestroy

PhonePC/2in1TabletTVWearable

type UrpcDestroy = () => void

用于销毁[UrpcStub](remote-communication-urpcapi.md#urpcstub)实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.1(13)

**错误码：** 错误码的详细介绍请参见[API错误码](remote-communication-error-code.md)。

## UrpcStub

PhonePC/2in1TabletTVWearable

表示可用于发出URPC请求的通信会话。它提供了各种远程调用方法（call、cancel、destroy）。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.1(13)

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 是 | 否 | UrpcStub的唯一标识id。 |
| call | [UrpcCall](remote-communication-urpcapi.md#urpccall) | 否 | 否 | 表示调用URPC请求。 |
| cancel | [UrpcCancel](remote-communication-urpcapi.md#urpccancel) | 否 | 否 | 表示取消URPC请求。 |
| destroy | [UrpcDestroy](remote-communication-urpcapi.md#urpcdestroy) | 否 | 否 | 表示销毁UrpcStub。 |

## UrpcInitConfiguration

PhonePC/2in1TabletTVWearable

SessionConfiguration接口定义了会话的配置参数，为开发者提供了对HTTP会话各个方面的详细控制。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mode | [UrpcMode](remote-communication-urpcapi.md#urpcmode) | 否 | 是 | URPC的运行模式，默认值为'client'，表示client模式。 |
| connect | [UrpcConnectConfiguration](remote-communication-urpcapi.md#urpcconnectconfiguration) | 否 | 否 | 指定与stub相关联的连接配置，包括ip地址和端口号、URPC连接协议、是否多径等配置项。 |
| timeout | number | 否 | 否 | 设置URPC的连接超时时间，表示请求等待多久后超时返回，单位是毫秒（ms），取值范围[0, 4294967295]。该字段为预留字段，在当前版本并不生效。 |

**示例：**

```
1. import { urpc } from "@kit.RemoteCommunicationKit";

3. let node: urpc.IpAndPort = {
4. ip: '127.0.0.1',
5. port: 8000
6. }
7. let connect: urpc.UrpcConnectConfiguration = {
8. node: node,
9. protocol: 'eat',
10. }
11. let config: urpc.UrpcInitConfiguration = {
12. timeout: 3000,
13. mode: 'client',
14. connect: connect
15. }
```

## UrpcMode

PhonePC/2in1TabletTVWearable

type UrpcMode = 'client';

当前仅支持填写'client'，表示该URPC节点为client模式，可主动发起请求，等待服务器的响应。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| 'client' | 表示URPC节点的模式，值固定为'client'。 |

## UrpcConnectConfiguration

PhonePC/2in1TabletTVWearable

UrpcConnectConfiguration配置URPC连接的关键信息，可以配置连接的ip和端口号，以及传输协议等可选参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| node | [IpAndPort](remote-communication-urpcapi.md#ipandport) | 否 | 否 | 连接的IP和端口配置。 |
| protocol | [UrpcProtocol](remote-communication-urpcapi.md#urpcprotocol) | 否 | 是 | 传输连接采用的协议类型，默认值为'eat'，表示采用eat协议。 |
| multiPath | boolean | 否 | 是 | 是否支持多路径传输，true表示支持多路径传输，多路径包含蜂窝网络和Wi-Fi；false表示不支持多路径传输，默认值为false。该字段为预留字段，在当前版本并不生效。 |
| flags | number | 否 | 是 | 证书标记位，非0表示开启证书校验。默认值为0，表示不开启证书校验。 |
| host | string | 否 | 是 | urpc服务的域名，默认值为空字符串。 |
| caPath | string | 否 | 是 | 校验证书的路径名称，默认值为空字符串。 |

**示例：**

```
1. import { urpc } from "@kit.RemoteCommunicationKit"

3. let node: urpc.IpAndPort = {
4. ip: '127.0.0.1',
5. port: 8000
6. }
7. let connect: urpc.UrpcConnectConfiguration = {
8. node: node,
9. protocol: 'eat',
10. multiPath: false,
11. flags: 0,
12. host: "127.0.0.1",
13. caPath: "data/single_urpc/eat.pem"
14. }
```

## IpAndPort

PhonePC/2in1TabletTVWearable

IpAndPort用于配置URPC的连接IP和端口号。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ip | string | 否 | 否 | 指定URPC的IPv4或IPv6地址。 |
| port | number | 否 | 否 | 指定URPC端口号，取值范围[0, 65535]。 |

**示例：**

```
1. import { urpc } from "@kit.RemoteCommunicationKit"

3. let node: urpc.IpAndPort = {
4. ip: '127.0.0.1',
5. port: 8000
6. }
```

## UrpcPromise

PhonePC/2in1TabletTVWearable

表示URPC请求的返回值

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| promise | Promise<Object> | 否 | 否 | URPC请求的响应对象。 |
| callingId | number | 否 | 否 | URPC请求的唯一标识Id，取值范围[0, 2147483647]。 |

## UrpcProtocol

PhonePC/2in1TabletTVWearable

type UrpcProtocol = 'eat'

当前仅支持填写'eat'，表示URPC的协议类型为eat。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| 'eat' | 表示URPC节点的协议类型，值固定为'eat'。 |

## CallingOption

PhonePC/2in1TabletTVWearable

用于配置URPC请求的优先级。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| priority | number | 否 | 是 | 配置URPC请求的优先级，默认为0，最大取值为3，表示优先级最高，优先级高的可以优先传输。该字段为预留字段，当前版本并不生效。 |
