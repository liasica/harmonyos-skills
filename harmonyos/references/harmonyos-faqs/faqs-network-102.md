---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-102
title: ArkTS通过TCP检测多域名连通性并自动选择备用地址
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > ArkTS通过TCP检测多域名连通性并自动选择备用地址
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4037f9290fc5e4fd2dc0785aa1c23473479ec4ea40feba4df6c7405c8f8edec5
---

## 问题现象

在HarmonyOS应用中，App启动阶段需要判断网络是否可用。当前网络连接逻辑要求如下：

* 首先检测主地址https://app.xxx.cn:8443是否可连接。
* 若主地址连接失败，则依次尝试备用地址https://app1.xxx.cn:8443和https://app2.xxx.cn:8443。
* 每个地址的判断超时时长为2秒。
* 若有可连通地址，则将该地址设置为全局使用的Constants.DOMAIN，供后续网络请求使用。

该机制可保证在弱网或网络切换场景下，App能快速切换至可用地址，保障功能可用性。

## 背景知识

在ArkTS开发中，[NetworkKit](../harmonyos-guides/network-kit.md)提供了基于TCP的[socket](../harmonyos-guides/socket-connection.md)接口，可用于检测目标地址是否连通，而不依赖于上层[HTTP请求](../harmonyos-guides/http-request.md)。

相比传统的方式，TCP连接判断具有更低的延迟和更明确的网络连通性判定结果，适合用于冷启动时的网络环境选择。

此外，[BusinessError](../harmonyos-references/js-apis-base.md#businesserror)接口定义了连接失败的错误信息结构，可以通过错误码或错误信息进行异常判断与处理。

## 解决方案

该方案通过以下三步实现目标地址的连通性检测和优选逻辑：

1. 定义一个包含主地址和两个备用地址的优先级列表，每个地址包括host和port：

   ```screen
   // 仅供展示，请根据需要替换真实地址
   const PRIORITY_TARGETS: CheckTarget[] = [
     { name: '主地址', host: 'app.xxx.cn', port: 8443 },
     { name: '备用地址1', host: 'app1.xxx.cn', port: 8443 },
     { name: '备用地址2', host: 'app2.xxx.cn', port: 8443 },
   ];
   ```
2. 基于TCP实现网络连通性检测。使用socket.constructTCPSocketInstance()创建TCP套接字，并设置连接目标和超时时间（默认2000ms）。连接成功即视为网络连通，失败则记录错误信息。

   ```screen
   private async checkNetworkConnectivity(host: string, port: number): Promise<NetWorkResult> {
     return new Promise((resolve) => {
       let tcpSocket = socket.constructTCPSocketInstance();
       const connectOptions: ConnectOptions = {
         address: {
           address: host,
           port: port
         } as NetAddress,
         timeout: 2000
       };

       tcpSocket.connect(connectOptions, (error: BusinessError) => {
         if (!error) {
           tcpSocket.close();
           resolve({ isReachable: true });
         } else {
           resolve({
             isReachable: false,
             errorCode: `ERROR_${error.code}`,
             errorMessage: error.message
           });
         }
       });
     });
   }
   ```
3. 按照优先级依次检测并选用第一个可用地址。通过遍历PRIORITY\_TARGETS列表，逐一调用上一步的检测函数。若某个地址连通，则将其设置为全局使用的Constants.DOMAIN并立即返回成功；若均不可达则返回失败。

   ```screen
   private async checkWithPriority(): Promise<void> {
     this.isChecking = true;
     for (const target of PRIORITY_TARGETS) {
       hilog.error(0x0000, TAG, `正在检测 ${target.name} (${target.host}:${target.port})...`);
       const result = await this.checkNetworkConnectivity(target.host, target.port);
       if (result.isReachable) {
         hilog.error(0x0000, TAG, `✅ ${target.name} 连通！`);
         Constants.DOMAIN = `${target.host}:${target.port}`;
         break;
       } else {
         hilog.error(0x0000, TAG, `❌ ${target.name} 不可达: ${result.errorMessage}`);
       }
     }
     this.isChecking = false;
   }
   ```

通过以上实现，预期效果如下：

* 在2秒内完成主地址的连通性判断。
* 若主地址不可用，将自动判断备用地址，整个判断过程控制在合理的总耗时内（最多6秒）。
* Constants.DOMAIN被设置为首个可用地址，后续网络请求均基于该地址执行。

此方案可广泛应用于HarmonyOS Next版本App的冷启动初始化阶段，提高App网络初始化成功率和稳定性。运行本示例需要在工程的module.json5文件中添加网络权限ohos.permission.INTERNET。

完整示例代码如下：

* Index.ets代码：

```screen
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Constants } from '../constants/Constants';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { NetWorkResult, ConnectOptions, NetAddress, CheckTarget } from '../model/DataModel';

const TAG = 'NetworkTest';

// 仅供展示，请根据需要替换真实地址
const PRIORITY_TARGETS: CheckTarget[] = [
  { name: '主地址', host: 'app.xxx.cn', port: 8443 },
  { name: '备用地址1', host: 'app1.xxx.cn', port: 8443 },
  { name: '备用地址2', host: 'app2.xxx.cn', port: 8443 },
];

@Entry
@Component
struct Index {
  @State isChecking: boolean = false;

  private async checkWithPriority(): Promise<void> {
    this.isChecking = true;
    for (const target of PRIORITY_TARGETS) {
      hilog.error(0x0000, TAG, `正在检测 ${target.name} (${target.host}:${target.port})...`);
      const result = await this.checkNetworkConnectivity(target.host, target.port);
      if (result.isReachable) {
        hilog.error(0x0000, TAG, `✅ ${target.name} 连通！`);
        Constants.DOMAIN = `${target.host}:${target.port}`;
        break;
      } else {
        hilog.error(0x0000, TAG, `❌ ${target.name} 不可达: ${result.errorMessage}`);
      }
    }
    this.isChecking = false;
  }

  private async checkNetworkConnectivity(host: string, port: number): Promise<NetWorkResult> {
    return new Promise((resolve) => {
      let tcpSocket = socket.constructTCPSocketInstance();
      const connectOptions: ConnectOptions = {
        address: {
          address: host,
          port: port
        } as NetAddress,
        timeout: 2000
      };

      tcpSocket.connect(connectOptions, (error: BusinessError) => {
        if (!error) {
          tcpSocket.close();
          resolve({ isReachable: true });
        } else {
          resolve({
            isReachable: false,
            errorCode: `ERROR_${error.code}`,
            errorMessage: error.message
          });
        }
      });
    });
  }

  build() {
    Column() {
      Text('网络连通性检测')
        .fontSize(24)
        .margin(16)
        .fontWeight(FontWeight.Bold);

      Button(this.isChecking ? '检测中...' : '开始检测')
        .width(100)
        .margin(10)
        .onClick(async () => {
          if (!this.isChecking) {
            this.checkWithPriority();
          }
        });
    }
    .width('100%')
    .height('100%');
  }
}
```

* DataModel.ets代码：

```screen
export interface CheckTarget {
  name: string;
  host: string;
  port: number;
}

// 网络地址类型
export interface NetAddress {
  address: string;
  port: number;
}

export interface ConnectOptions {
  address: NetAddress;
  timeout: number;
}

export interface NetWorkResult {
  isReachable: boolean;
  errorCode?: string;
  errorMessage?: string;
}
```

* Constants.ets代码：

```screen
export class Constants {
  static DOMAIN: string = '';
}
```
