---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-61
title: 如何判断当前网络能否上网
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何判断当前网络能否上网
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:40b8008468eb3d799ee4e142f8e57e8c552f940bee7c2fdc8b0886dd157fe536
---

可以使用@ohos.net.connection的能力，在网络连接状态发生变化时，判断当前网络是否可以访问互联网，并将判断结果存储到AppStorage中。需要判断网络连接状态时，直接从AppStorage获取结果。参考代码如下：

```typescript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
export struct NetJudge {
  public static netConnection: connection.NetConnection | undefined = undefined;
  private static JUDGE_NET_TAG: string = 'NetJudge.currNet.isUseful';

  init() {
    NetJudge.netConnection = connection.createNetConnection();
    NetJudge.netConnection.register(() => {
      console.info('connection register success');
    });

    NetJudge.netConnection.on('netAvailable', (data) => {
      console.info('NetJudge  netAvailable ');
      AppStorage.setOrCreate(NetJudge.JUDGE_NET_TAG, this.judgeHasNet());
    });

    NetJudge.netConnection.on('netUnavailable', () => {
      console.info('NetJudge  netUnavailable ');
      AppStorage.setOrCreate(NetJudge.JUDGE_NET_TAG, this.judgeHasNet());
    });

    NetJudge.netConnection.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
      AppStorage.setOrCreate(NetJudge.JUDGE_NET_TAG, this.judgeHasNet());
    });

    // Subscribe to network connection information change events. You can only receive this event notification after calling register
    NetJudge.netConnection.on('netConnectionPropertiesChange', (data: connection.NetConnectionPropertyInfo) => {
      AppStorage.setOrCreate(NetJudge.JUDGE_NET_TAG, this.judgeHasNet());
    });

    NetJudge.netConnection.on('netLost', () => {
      AppStorage.setOrCreate(NetJudge.JUDGE_NET_TAG, this.judgeHasNet());
    });
  }

  regist() {
    if (NetJudge.netConnection === undefined) {
      this.init();
    }
  }

  judgeHasNet(): boolean {
    try { // Get current network connection
      let netHandle = connection.getDefaultNetSync();

      // 0-100 Reserved connections for the system
      if (!netHandle || netHandle.netId < 100) {
        return false;
      }

      // Get the properties of the connection
      let netCapability = connection.getNetCapabilitiesSync(netHandle);
      let cap = netCapability.networkCap;
      if (!cap) {
        return false;
      }

      for (let em of cap) {
        if (connection.NetCap.NET_CAPABILITY_VALIDATED === em) {
          return true;
        }
      }
    } catch (e) {
      let err = e as BusinessError;
      console.info('get netInfo error ：' + JSON.stringify(err));
    }
    return false;
  }

  build() {
    Column({ space: 10 }) {
      Button('如何判断当前网络能否上网')
        .onClick(() => {
          this.regist();
        })
    }
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```
