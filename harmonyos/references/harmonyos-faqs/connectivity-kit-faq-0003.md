---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/connectivity-kit-faq-0003
title: WiFi信息获取常见问题
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 常见问题 > WiFi信息获取常见问题
category: harmonyos-faqs
scraped_at: 2026-11-27T10:51:23+08:00
doc_updated_at: 2026-11-26
content_hash: sha256:6cab1f4021a5724e9a760a87d2e3c8ab2abb71396217c24f8b0e368105baf900
---

**Q：设备连接Wi-Fi后，如何获取当前设备的IP地址？**

**A：**使用wifiManager模块获取ipInfo，然后转换为IP常用格式，注意wifiManager.getIpInfo()接口需要权限ohos.permission.GET\_WIFI\_INFO。参考代码如下：

```ts
import { wifiManager } from '@kit.ConnectivityKit';

let ipAddress = wifiManager.getIpInfo().ipAddress;
let ip = (ipAddress >>> 24) + "." + (ipAddress >> 16 & 0xFF) + "." + (ipAddress >> 8 & 0xFF) + "." + (ipAddress & 0xFF);
```

**Q：使用了wifiManager.getLinkedInfo，从WifiLinkedInfo里获取bssid作为WiFi的标识使用，但是从文档上看，只有系统应用才能申请ohos.permission.GET\_WIFI\_LOCAL\_MAC权限获取到真实MAC地址，否则只返回随机地址，有什么方法能获取到WiFi的唯一标识，用于实现WiFi打卡之类的功能？**

**A：**方案设计：

WiFi打卡可通过[geoLocationManager.getCurrentWifiBssidForLocating](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentwifibssidforlocating14)接口，配合[ohos.permission.LOCATION](../harmonyos-guides/permissions-for-all-user.md#ohospermissionlocation)和[ohos.permission.APPROXIMATELY\_LOCATION](../harmonyos-guides/permissions-for-all-user.md#ohospermissionapproximately_location)权限来获取真实bssid。

* 实现思路：

  权限检查，代码如下：

  ```ts
  /**
     * 判断是否已获取相关权限的授权
     */
    private isPermissionGranted(): boolean {
      try {
        let bundleInfo: bundleManager.BundleInfo =
          bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
        let tokenId: number = bundleInfo.appInfo.accessTokenId;
        return this.atManager.checkAccessTokenSync(tokenId, 'ohos.permission.APPROXIMATELY_LOCATION') ===
        abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED &&
          this.atManager.checkAccessTokenSync(tokenId, 'ohos.permission.LOCATION') ===
        abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
      } catch (error) {
        console.error(`check permission err: ${JSON.stringify(error)}`);
      }
      return false;
    }
  ```

  获取bssid，代码如下：

  ```ts
  /**
     * 获取BSSID
     */
    private getConnectedWiFiBssid() {
      try {
        // 获取连接的Wi-Fi AP（Access Point）的Bssid（Basic Service Set Identifier）信息
        this.bssid = geoLocationManager.getCurrentWifiBssidForLocating();
        console.info(`get wifi bssid:${this.bssid}`);
      } catch (error) {
        console.error(`getCurrentWifiBssidForLocating: errCode:${error.code}, errMessage:${error.message}`);
      }
    }
  ```
* 完整示例代码如下：

  ```ts
  import { geoLocationManager } from '@kit.LocationKit';
  import { abilityAccessCtrl, bundleManager, common } from '@kit.AbilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { JSON } from '@kit.ArkTS';

  @Entry
  @Component
  struct Index {
    @State bssid: string = '';
    private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    private atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

    build() {
      Column({ space: 40 }) {
        Button('点击获取连接WiFi的BSSID')
          .width('60%')
          .onClick(() => {
            if (this.isPermissionGranted()) {
              this.getConnectedWiFiBssid();
            } else {
              this.requestPermissions();
            }
          });

        Text(`BSSID：${this.bssid}`)
          .width('100%')
          .textAlign(TextAlign.Center);

        Button('点击清空数据')
          .width('60%')
          .onClick(() => {
            this.bssid = '';
          });
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }

    /**
     * 判断是否已获取相关权限的授权
     */
    private isPermissionGranted(): boolean {
      try {
        let bundleInfo: bundleManager.BundleInfo =
          bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
        let tokenId: number = bundleInfo.appInfo.accessTokenId;
        return this.atManager.checkAccessTokenSync(tokenId, 'ohos.permission.APPROXIMATELY_LOCATION') ===
        abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED &&
          this.atManager.checkAccessTokenSync(tokenId, 'ohos.permission.LOCATION') ===
        abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
      } catch (error) {
        console.error(`check permission err: ${JSON.stringify(error)}`);
      }
      return false;
    }

    /**
     * 获取BSSID
     */
    private getConnectedWiFiBssid() {
      try {
        // 获取连接的Wi-Fi AP（Access Point）的Bssid（Basic Service Set Identifier）信息
        this.bssid = geoLocationManager.getCurrentWifiBssidForLocating();
        console.info(`get wifi bssid:${this.bssid}`);
      } catch (error) {
        console.error(`getCurrentWifiBssidForLocating: errCode:${error.code}, errMessage:${error.message}`);
      }
    }

    /**
     * 请求权限
     */
    private requestPermissions(): void {
      try {
        this.atManager.requestPermissionsFromUser(this.context, ['ohos.permission.APPROXIMATELY_LOCATION',
          'ohos.permission.LOCATION']).then((data) => {
          // 值0：有权限，则尝试获取BSSID
          if (data.authResults[0] === 0 && data.authResults[1] === 0) {
            this.getConnectedWiFiBssid();
            return;
          }

          // 值非0且非-1：未知值，可能业务逻辑存在问题：如权限名非法等
          if (data.authResults[0] !== -1 && data.authResults[1] !== -1) {
            this.showMyToast(`获取权限失败，检查业务逻辑，错误码：${data.authResults[0]}, ${data.authResults[1]}`);
            return;
          }

          // 值-1：缺少任一权限且已存在弹窗，直接返回，并toast提示
          if (data.dialogShownResults && (data.dialogShownResults[0] || data.dialogShownResults[1])) {
            this.showMyToast(`缺少必要权限，请重试`);
            return;
          }

          // 值-1：缺少任一权限且未弹窗，弹出半模态授权申请
          this.openPermissionsSetting();
        }).catch((err: Error) => {
          console.error(`requestPermissionsFromUser err: ${JSON.stringify(err)}`);
        });
      } catch (err) {
        console.error(`requestPermissionsFromUser err: ${JSON.stringify(err)}`);
      }
    }

    /**
     * 半模态弹窗请求权限
     */
    private openPermissionsSetting(): void {
      this.atManager.requestPermissionOnSetting(this.context, ['ohos.permission.APPROXIMATELY_LOCATION',
        'ohos.permission.LOCATION']).then((grantResult) => {
        if (grantResult[0] === 0 && grantResult[1] === 0) {
          this.getConnectedWiFiBssid();
          return;
        }
        this.showMyToast('缺少必要权限，请重试');
      }).catch((err: BusinessError) => {
        console.error(`data: ${JSON.stringify(err)}`);
      });
    }

    /**
     * 展示toast
     */
    private showMyToast(message: string) {
      try {
        this.getUIContext().getPromptAction().showToast({ duration: 3000, message: message });
      } catch (error) {
        console.error(`show toast occur err: ${JSON.stringify(error)}`);
      }
    }
  }
  ```

**Q：使用[wifiManager.getScanInfoList](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetscaninfolist10)接口扫描出来的bssid与[wifiManager.getLinkedInfo](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetlinkedinfo)接口扫描出的bssid不一致，这是什么原因？**

**A：**wifiManager.getScanInfoList和wifiManager.getLinkedInfo方法分别用于获取WiFi扫描信息列表和已连接的WiFi信息。

如果应用申请了ohos.permission.GET\_WIFI\_LOCAL\_MAC和ohos.permission.GET\_WIFI\_PEERS\_MAC权限（仅系统应用可申请），则返回结果中的bssid为真实设备地址，否则为随机设备地址。两个方法获取的bssid不一致的可能原因如下：

* getScanInfoList和getLinkedInfo方法的调用时间相差较大，由于数据更新和缓存机制导致不一致。
* 多个接入点（AP）使用同一ssid但具有不同的bssid，导致扫描出来的结果不一致。

**Q：wifiManager.getScanInfoList()接口是否有扫描次数限制？**

**A：**wifiManager.getScanInfoList()接口存在扫描频次限制：前台应用2分钟内最多发起4次扫描。参考[扫描管控](../harmonyos-guides/scan-development-guide.md#扫描管控)。

**Q：调用[wifiManager.startScan](../harmonyos-references/js-apis-wifimanager.md#wifimanagerstartscan21)接口频繁发起扫描时返回BusinessError 2501000，是什么原因？**

**A：**wifiManager.startScan接口存在扫描频次限制，应用程序在前台运行时，两分钟内最多可扫描四次。当短时间内频繁调用超过限制时，会返回BusinessError 2501000错误，等待一段时间后再次调用即可正常扫描。错误码详情参考[WIFI错误码](../harmonyos-references/errorcode-wifi.md#section2501000-sta内部异常)。

**Q：同一Wi-Fi断开重连后获取的BSSID不同，是什么原因？如何处理？**

**A：**BSSID是AP（无线接入点）的MAC地址，一个SSID下可以部署多台AP。企业办公网络普遍采用多台AP广播同一SSID的组网方式实现全覆盖和无缝漫游，每台AP有独立的BSSID。手机连接时实际关联的是SSID下的某台AP，断开重连后系统会按信号强度、负载均衡策略重新选择AP，因此获取到的BSSID可能不同。若需在Wi-Fi打卡场景中处理此问题，建议打卡服务端配置同一SSID下全部AP的BSSID白名单，而非预设单一BSSID。应用通过[geoLocationManager.getCurrentWifiBssidForLocating](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentwifibssidforlocating14)获取当前连接Wi-Fi的真实BSSID并上报服务端，服务端判定获取到的BSSID在白名单内即打卡成功。

**Q：[geoLocationManager.isWlanBssidMatched](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageriswlanbssidmatched21)接口的作用是匹配当前连接的WiFi，还是其他？**

**A：**isWlanBssidMatched不是匹配当前连接的WiFi，而是判断指定的BSSID（WiFi热点的物理地址）是否存在于最新的WLAN扫描结果中。也就是说，它检测的是设备周围环境中扫描到的WiFi热点（包括但不限于已连接的热点），常用于通过WiFi热点信号强度辅助判断设备是否处于某个位置附近。该接口属于位置服务（Location Kit），需要同时申请ohos.permission.LOCATION和ohos.permission.APPROXIMATELY\_LOCATION权限。调用前需确保设备“位置”开关已打开，否则会返回错误码3301100；发起扫描失败时返回3301800。将needStartScan设为false可复用最近一次扫描结果，能减少扫描带来的功耗；设为true则获取最新环境数据，结果更准确。即使设备未连接任何WiFi，只要周围扫描到了目标BSSID且信号强度达标，接口也会返回true，因此该接口适用于通过WiFi热点信号强度辅助判断设备位置的场景。
